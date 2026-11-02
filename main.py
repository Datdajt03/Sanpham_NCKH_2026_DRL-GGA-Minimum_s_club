"""
main.py — Điều phối toàn bộ hệ thống thực nghiệm EVO-RL Minimum s-Club Cover.
Tuân thủ kiến trúc 7 tầng sạch sẽ:
  Dataset -> Problem -> Operators -> RL Controller -> Environment -> Trainer -> Analysis

Mỗi lần chạy sẽ tự động tạo thư mục: results/ketqua_YYYY-MM-DD_HH-MM-SS/ để lưu trữ toàn bộ dữ liệu độc lập.
"""
import os
os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"
import sys
import argparse
import time
import random
from datetime import datetime

# Đảm bảo UTF-8 cho Windows console
if sys.stdout is not None:
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

# Thêm thư mục hiện tại vào Python path
current_dir = os.path.dirname(os.path.abspath(__file__))
if current_dir not in sys.path:
    sys.path.insert(0, current_dir)

import torch
# Tối ưu hóa đa luồng CPU cho toàn bộ 12 nhân của máy
if hasattr(os, 'cpu_count') and os.cpu_count():
    torch.set_num_threads(os.cpu_count())

# Tối ưu hóa tối đa công suất GPU NVIDIA (cuDNN Benchmark & Tensor Cores)
if torch.cuda.is_available():
    torch.backends.cudnn.benchmark = True
    try:
        torch.set_float32_matmul_precision('high')
    except Exception:
        pass

from configs.config import ExperimentConfig, get_fixed_seeds
from dataset.loader import load_graph, discover_graph_files
from dataset.selector import interactive_dataset_selector
from problem.graph import SClubGraph
from trainer.evaluate import run_single_seed, run_single_seed_full_pipeline
from analysis.statistics import (
    compute_condition_statistics, 
    compute_all_summary_statistics,
    find_best_seed_per_condition,
    find_global_best_solution
)

from analysis.export import export_single_seed_result, export_summary_20_seeds
from analysis.charts import generate_all_charts
from concurrent.futures import ProcessPoolExecutor, as_completed



import threading
import ctypes

class LiveHardwareMonitor(threading.Thread):
    """Luồng giám sát tài nguyên CPU (12 Cores), RAM và GPU RTX 3050 cập nhật liên tục thời gian thực."""
    def __init__(self):
        super().__init__(daemon=True)
        self.running = True
        self.cur_cpu = 0.0
        self.cur_ram = ""
        self.cur_vram = ""
        self.max_cpu = 0.0
        self.max_vram = 0.0

    def run(self):
        while self.running:
            try:
                import psutil
                cpu_p = psutil.cpu_percent(interval=0.5)
                ram = psutil.virtual_memory()
                ram_used = ram.used / (1024 ** 3)
                ram_tot = ram.total / (1024 ** 3)
                
                vram_str = "N/A"
                if torch.cuda.is_available():
                    vram_alloc = torch.cuda.memory_allocated() / (1024 ** 2)
                    vram_res = torch.cuda.memory_reserved() / (1024 ** 2)
                    vram_tot = torch.cuda.get_device_properties(0).total_memory / (1024 ** 2)
                    vram_str = f"{vram_alloc:.0f}MB Act ({vram_res:.0f}MB Res)/{vram_tot:.0f}MB"
                    self.max_vram = max(self.max_vram, vram_alloc)

                self.cur_cpu = cpu_p
                self.cur_ram = f"{ram_used:.1f}GB/{ram_tot:.1f}GB"
                self.cur_vram = vram_str
                self.max_cpu = max(self.max_cpu, cpu_p)

                # Cập nhật liên tục lên thanh Tiêu đề cửa sổ CMD / Terminal theo thời gian thực
                title_str = f"🚀 EVO-RL MSCC | CPU: {cpu_p:4.1f}% (12 Cores) | RAM: {self.cur_ram} | GPU RTX 3050: {vram_str}"
                if os.name == 'nt':
                    ctypes.windll.kernel32.SetConsoleTitleW(title_str)
            except Exception:
                time.sleep(1.0)


# Luồng giám sát phần cứng
hw_monitor = None

def start_hardware_monitor():
    """Khởi động luồng giám sát thời gian thực CPU/RAM/GPU."""
    global hw_monitor
    if hw_monitor is None:
        hw_monitor = LiveHardwareMonitor()
        hw_monitor.start()



def get_hardware_status_str() -> str:
    """Trả về chuỗi giám sát tài nguyên phần cứng CPU (12 Cores), RAM và GPU RTX 3050 (VRAM)."""
    try:
        import psutil
        cpu_p = psutil.cpu_percent(interval=None)
        ram = psutil.virtual_memory()
        ram_used = ram.used / (1024 ** 3)
        ram_tot = ram.total / (1024 ** 3)
        
        gpu_str = ""
        if torch.cuda.is_available():
            vram_alloc = torch.cuda.memory_allocated() / (1024 ** 2)
            vram_res = torch.cuda.memory_reserved() / (1024 ** 2)
            vram_tot = torch.cuda.get_device_properties(0).total_memory / (1024 ** 2)
            gpu_str = f" | GPU RTX 3050: {vram_alloc:.0f}MB Act ({vram_res:.0f}MB Res)/{vram_tot:.0f}MB"
            
        return f"[CPU: {cpu_p:4.1f}% | RAM: {ram_used:.1f}GB/{ram_tot:.1f}GB{gpu_str}]"
    except Exception:
        return "[CPU: 12 Cores Đa luồng | GPU: RTX 3050 Active]"


def run_single_graph_experiment(
    graph_name: str, 
    raw_ig_graph, 
    config: ExperimentConfig, 
    session_out_dir: str
) -> dict:
    """Thực thi toàn bộ thí nghiệm trên một đồ thị cụ thể và xuất kết quả theo từng seed."""
    # Tạo folder riêng mang tên tập dữ liệu bên trong folder phiên chạy có timestamp
    graph_out_dir = os.path.join(session_out_dir, graph_name)
    os.makedirs(graph_out_dir, exist_ok=True)
    charts_dir = os.path.join(graph_out_dir, "charts")
    os.makedirs(charts_dir, exist_ok=True)

    # Hiển thị cấu hình phần cứng Hybrid (CPU + GPU)
    gpu_available = torch.cuda.is_available()
    gpu_name = torch.cuda.get_device_name(0) if gpu_available else "Không khả dụng"
    n_cpus = os.cpu_count() or 4
    hw_info = f"Hybrid Co-Processing [CPU: {n_cpus} Cores song song (GA/C++ igraph) + GPU: {gpu_name} (PPO Tensor Cores)]" if gpu_available else f"CPU Đa luồng [{n_cpus} Cores]"

    v_cnt = raw_ig_graph.vcount()
    e_cnt = raw_ig_graph.ecount()
    density = (2.0 * e_cnt) / (v_cnt * (v_cnt - 1)) if v_cnt > 1 else 0.0
    graph_info = {
        'name': graph_name,
        'n_nodes': v_cnt,
        'n_edges': e_cnt,
        'density': float(density),
        's': int(config.s_club_threshold)
    }

    # Sử dụng danh sách 20 hạt giống cố định chuẩn từ file seedun.md
    seed_values = get_fixed_seeds(config.num_seeds)

    print("\n" + "=" * 90)
    print(f" THỰC NGHIỆM TRÊN ĐỒ THỊ: [{graph_name}]")
    print(f"   * Kiến trúc xử lý:   {hw_info}")
    print(f"   * Số đỉnh (Vertices): {v_cnt} | Số cạnh (Edges): {e_cnt} | Mật độ (Density): {density:.4f}")
    print(f"   * Ngưỡng đường kính s-club: s = {config.s_club_threshold}")
    print(f"   * Số lần seed:       {len(seed_values)} seeds cố định (từ seedun.md)")
    print(f"   * Danh sách seeds:   {seed_values}")
    print(f"   * Số workers song song: {config.num_workers} seeds cùng lúc (Đa tiến trình)")
    print(f"   * Số thế hệ tối đa:  {config.max_generations} generations")
    print(f"   * Thư mục lưu kết quả: {graph_out_dir}")
    print(f"   * Thư mục lưu biểu đồ: {charts_dir}")
    print("=" * 90)

    raw_results = {cond: [] for cond in config.conditions}

    if config.num_workers > 1:
        import multiprocessing
        from trainer.progress import LiveParallelDashboard
        
        print(f"\n---> Bắt đầu chạy {config.num_seeds} seeds song song ({config.num_workers} seeds/đợt trên đa nhân CPU):", flush=True)
        seed_results_dict = {}
        
        manager = multiprocessing.Manager()
        shared_status = manager.dict()
        
        dashboard = LiveParallelDashboard(
            shared_status_dict=shared_status,
            num_workers=config.num_workers,
            total_seeds=config.num_seeds,
            conditions=config.conditions,
            refresh_interval=1.0
        )
        dashboard.start()

        with ProcessPoolExecutor(max_workers=config.num_workers) as executor:
            future_to_seed = {
                executor.submit(
                    run_single_seed_full_pipeline,
                    seed_idx,
                    seed_val,
                    raw_ig_graph,
                    config,
                    graph_out_dir,
                    graph_info,
                    hw_info,
                    shared_status,
                    config.num_seeds
                ): (seed_idx, seed_val)
                for seed_idx, seed_val in enumerate(seed_values, start=1)
            }

            for future in as_completed(future_to_seed):
                seed_idx, seed_val = future_to_seed[future]
                try:
                    s_idx, s_val, seed_data_by_condition = future.result()
                    seed_results_dict[s_idx] = seed_data_by_condition
                    hw_status = get_hardware_status_str()
                    print(f"\n--- [Hoàn thành Seed {s_idx:02d}/{config.num_seeds:02d}] (Seed Value: {s_val}) {hw_status} ---", flush=True)
                    for condition in config.conditions:
                        res = seed_data_by_condition[condition]
                        print(f"  * {condition:<12} | Cover={res['best_cover']:<3} | Feasible={res['is_feasible']} | Time={res['runtime_seconds']:.2f}s", flush=True)
                except Exception as exc:
                    print(f"[!] Seed #{seed_idx:02d} gặp lỗi: {exc}", flush=True)

        dashboard.stop()
        try:
            manager.shutdown()
        except Exception:
            pass

        # Gom kết quả theo đúng thứ tự hạt giống 1..N
        for seed_idx in range(1, config.num_seeds + 1):
            if seed_idx in seed_results_dict:
                for condition in config.conditions:
                    raw_results[condition].append(seed_results_dict[seed_idx][condition])

        if torch.cuda.is_available():
            torch.cuda.empty_cache()
    else:
        print(f"\n---> Bắt đầu chạy tuần tự {config.num_seeds} lượt hạt giống (Seeds 1..{config.num_seeds}):", flush=True)
        graph = SClubGraph(raw_ig_graph, s=config.s_club_threshold)
        total_conds = len(config.conditions)
        for seed_idx, seed_val in enumerate(seed_values, start=1):
            hw_status = get_hardware_status_str()
            print(f"\n--- [Seed {seed_idx:02d}/{config.num_seeds:02d}] (Seed Value: {seed_val}) {hw_status} ---", flush=True)
            seed_data_by_condition = {}

            for cond_idx, condition in enumerate(config.conditions, start=1):
                t0 = time.time()
                res = run_single_seed(seed_val, condition, graph, config)
                elapsed = time.time() - t0
                raw_results[condition].append(res)
                seed_data_by_condition[condition] = res
                print(f"  * {condition:<12} | Cover={res['best_cover']:<3} | Feasible={res['is_feasible']} | Time={elapsed:.2f}s", flush=True)

            export_single_seed_result(
                seed_idx=seed_idx,
                seed_val=seed_val,
                seed_data_by_condition=seed_data_by_condition,
                output_dir=graph_out_dir,
                graph_info=graph_info,
                hardware_info=hw_info
            )
            if torch.cuda.is_available():
                torch.cuda.empty_cache()

    # Tính toán các chỉ số thống kê tổng hợp và kiểm định Wilcoxon
    summary_stats = compute_all_summary_statistics(raw_results)

    # Xuất file tổng hợp 20 lần seed: Tong_20_lan_seed.json và Tong_20_lan_seed.md
    export_summary_20_seeds(
        summary_stats=summary_stats,
        raw_results=raw_results,
        graph_name=graph_name,
        output_dir=graph_out_dir,
        graph_info=graph_info,
        seed_values=seed_values,
        hardware_info=hw_info
    )

    # Sinh các biểu đồ phân tích vào thư mục charts của riêng tập dữ liệu đó
    generate_all_charts(raw_results, charts_dir)

    # In bảng kết quả tổng quan ra màn hình Console
    print("\n" + "=" * 90)
    print(f" KẾT QUẢ TỔNG HỢP: [{graph_name}] (Hoàn thành {config.num_seeds} Seeds)")
    print("=" * 90)
    print(f"{'Thuật toán':<15} | {'Best':<6} | {'Mean ± Std':<18} | {'Median':<8} | {'Worst':<6} | {'Feasible':<10} | {'Wilcoxon':<12} | {'Time TB':<10}")
    print("-" * 90)

    for cond, st in summary_stats.items():
        p_val = st.get('p_value_vs_ppo', 1.0)
        sig = st.get('stat_significance', '=')
        p_val_str = f"p={p_val:.3f} [{sig}]" if cond != 'PPO-AOS' else f"p={p_val:.3f} [Gốc =]"
        print(f"{cond:<15} | {st['cover_min']:<6} | {st['cover_mean']:>5.2f} ± {st['cover_std']:<5.2f}   | {st['cover_median']:<8.1f} | {st['cover_max']:<6} | {st['feasible_rate']*100:>7.1f}%   | {p_val_str:<12} | {st['time_mean']:>6.2f}s")




    
    # Liệt kê Seed chạy tốt nhất của từng thuật toán trong 20 seeds
    best_seeds_per_cond = find_best_seed_per_condition(raw_results)
    global_best = find_global_best_solution(raw_results)
    
    print("-" * 90)
    print(f" ⭐ HẠT GIỐNG CHẠY TỐT NHẤT TRONG {config.num_seeds} LẦN SEED (BEST SEED PER ALGORITHM):")
    print("-" * 90)
    print(f"{'Thuật toán':<15} | {'Lần chạy Best':<14} | {'Seed Value':<12} | {'Cover':<6} | {'Fitness':<10} | {'Time':<8} | {'Tần suất đạt Best':<18}")
    print("-" * 90)
    for cond, b_st in best_seeds_per_cond.items():
        pct = (b_st['all_best_seeds_count'] / config.num_seeds) * 100.0 if config.num_seeds > 0 else 100.0
        freq_str = f"{b_st['all_best_seeds_count']}/{config.num_seeds} seeds ({pct:.0f}%)"
        print(f"{cond:<15} | Seed #{b_st['best_seed_index']:02d}        | {b_st['best_seed_value']:<12} | {b_st['best_cover']:<6} | {b_st['best_fitness']:<10.2f} | {b_st['runtime_seconds']:>6.2f}s | {freq_str:<18}")

    if global_best:
        print("-" * 90)
        print(f" 🏆 HẠT GIỐNG TỐT NHẤT TOÀN CỤC (GLOBAL BEST SEED):")
        print(f"    * Thuật toán đạt Best toàn diện : {global_best['algorithm']}")
        print(f"    * Lần chạy                      : Seed #{global_best['seed_index']:02d} / {config.num_seeds} (Giá trị Seed: {global_best['seed_value']} từ seedun.md)")
        print(f"    * Kích thước tập phủ kỷ lục     : {global_best['best_cover']} s-clubs (Fitness = {global_best['best_fitness']:.2f}) | Thời gian: {global_best['runtime_seconds']:.2f}s")
        print(f"    * Cấu trúc phân bổ số đỉnh/cụm  : {global_best['club_sizes']}")

    print("=" * 90)
    print(f" Đã lưu thành công các file tại folder: {graph_out_dir}")
    print(f"   * {config.num_seeds} file: results_seed_1.md/json ... results_seed_{config.num_seeds}.md/json")
    print(f"   * File tổng: Tong_20_lan_seed.md và Tong_20_lan_seed.json")
    print(f"   * Bảng CSV: summary_metrics.csv (kèm thông tin Best Seed)")
    print(f"   * Biểu đồ riêng: {charts_dir}/\n")

    return summary_stats



def parse_graph_selection(input_str: str, graph_names: list, graph_files: dict) -> list:
    """
    Hỗ trợ phân tích cú pháp lựa chọn linh hoạt:
      - '0' hoặc 'all': Chạy tất cả
      - Số đơn lẻ: '3'
      - Danh sách số: '1, 3, 5' hoặc '1 3 5'
      - Dải số (Range): '1-5' hoặc '2-6, 9'
      - Tên file / từ khóa: 'karate,chesapeake,dolphins' hoặc 'johnson8-2-4.clq'
    """
    input_str = input_str.strip()
    if not input_str:
        return []
    if input_str == '0' or input_str.lower() in ('all', 'tatca', 'tat ca'):
        return list(graph_names)

    selected = []
    # Tách chuỗi theo dấu phẩy, chấm phẩy, tab hoặc khoảng trắng
    raw_tokens = [t.strip().strip('"').strip("'") for t in input_str.replace(',', ' ').replace(';', ' ').split() if t.strip()]

    for token in raw_tokens:
        clean_token = token
        # Bỏ phần mở rộng nếu người dùng gõ kèm .clq, .graph, .gml, v.v.
        for ext in ['.clq', '.graph.bz2', '.graph', '.gml', '.txt', '.bz2', '.edges']:
            if clean_token.lower().endswith(ext):
                clean_token = clean_token[:-len(ext)]
                break

        # 1. Dải số dạng A-B (ví dụ: 1-5)
        if '-' in clean_token and len(clean_token.split('-')) == 2:
            parts = clean_token.split('-')
            if parts[0].isdigit() and parts[1].isdigit():
                start, end = int(parts[0]), int(parts[1])
                for idx in range(start, end + 1):
                    if 1 <= idx <= len(graph_names):
                        name = graph_names[idx - 1]
                        if name not in selected:
                            selected.append(name)
                continue

        # 2. Số thứ tự đơn lẻ (ví dụ: 3)
        if clean_token.isdigit():
            idx = int(clean_token)
            if 1 <= idx <= len(graph_names):
                name = graph_names[idx - 1]
                if name not in selected:
                    selected.append(name)
            continue

        # 3. Khớp chính xác tên đồ thị (Exact match, không phân biệt hoa thường)
        matched_exact = False
        for name in graph_names:
            if clean_token.lower() == name.lower():
                if name not in selected:
                    selected.append(name)
                matched_exact = True
                break
        if matched_exact:
            continue

        # 4. Tìm kiếm gần đúng theo tên (substring match)
        for name in graph_names:
            if clean_token.lower() in name.lower():
                if name not in selected:
                    selected.append(name)

    return selected



def interactive_menu(graph_files: dict, config: ExperimentConfig) -> tuple:
    """
    Menu điều khiển tương tác trực quan (Master Console Menu) cho EVO-RL MSCC.
    """
    graph_names = list(graph_files.keys())
    type1_graphs = [
        'karate', 'chesapeake', 'dolphins', 'lesmis', 'polbooks',
        'adjnoun', 'football', 'jazz', 'celegansneural', 'netscience',
        'celegans_metabolic', 'email'
    ]
    type2_graphs = [
        'johnson8-2-4', 'johnson8-4-4', 'johnson16-2-4', 'MANN_a9', 'C125.9',
        'hamming6-2', 'hamming6-4', 'hamming8-2',
        'keller4', 'c-fat200-1', 'c-fat200-5', 'brock200_1', 'brock200_2',
        'brock200_3', 'gen200_p0.9_44', 'gen200_p0.9_55', 'san200_0.9_2',
        'san200_0.9_3'
    ]
    demo_graphs = ['karate', 'chesapeake', 'dolphins', 'johnson8-2-4']

    while True:
        print("\n" + "=" * 80)
        print("     🚀 HỆ THỐNG PHẦN MỀM TỔNG HỢP NCKH - EVO-RL MSCC FRAMEWORK")
        print("   Tối Ưu Hóa Tiến Hóa Kết Hợp Học Tăng Cường Sâu (PPO-AOS) Cho Minimum s-Club Cover")
        print("=" * 80)
        print(f"  * Số đồ thị benchmark tìm thấy: {len(graph_names)} đồ thị (12 Real-world Type 1 + 18 DIMACS Type 2)")
        print(f"  * Cấu hình mặc định: s={config.s_club_threshold}, seeds={config.num_seeds}, workers={config.num_workers}, epochs={config.max_generations}, pop_size={config.pop_size}")
        print("=" * 80)
        print("\n --- [A] CHƯƠNG TRÌNH THỰC NGHIỆM MÔ HÌNH (EVO-RL MSCC) ---")
        print("  [1] Chạy Thử Nhanh (Demo 4 đồ thị: karate, chesapeake, dolphins, johnson8-2-4)")
        print("  [2] Chạy Nhóm 1 - 12 Mạng Thực Tế (Type 1: karate, jazz, email, netscience...)")
        print("  [3] Chạy Nhóm 2 - 18 Đồ Thị Chuẩn DIMACS (Type 2: johnson, brock, gen, san...)")
        print("  [4] Chạy Toàn Bộ 30 Đồ Thị Benchmark Chuẩn Quốc Tế (Type 1 + Type 2)")
        print("  [5] Tự Nhập / Dán Danh Sách Tên Đồ Thị Tùy Chọn")
        print("  [6] Giao Diện Tương Tác Chọn Đồ Thị TUI (Phím mũi tên, Space, Enter)")
        print("  [7] Tùy Chỉnh Siêu Tham Số Nâng Cao (s, seeds, workers, epochs, pop_size)")
        print("\n --- [B] PHÂN TÍCH, XUẤT BIỂU ĐỒ & BÁO CÁO KHOA HỌC ---")
        print("  [8] Xuất Toàn Bộ Biểu Đồ Phân Tích & Hội Tụ (600 DPI PNG & Vector PDF)")
        print("  [9] Tổng Hợp Bảng Số Liệu Báo Cáo & Kiểm Định Thống Kê Wilcoxon")
        print("\n --- [C] CÔNG CỤ & TIỆN ÍCH HỆ THỐNG ---")
        print("  [10] Kiểm Tra Toàn Diện Hệ Thống (9 giai đoạn kiểm chứng tự động)")
        print("  [11] Kiểm Tra Môi Trường & GPU (check_env.py)")
        print("\n  [0] Thoát chương trình")
        print("=" * 80)

        choice = input(">> Nhập lựa chọn của bạn (0-11): ").strip()
        if choice == '1':
            selected = [g for g in demo_graphs if g in graph_files]
            return selected, config
        elif choice == '2':
            selected = [g for g in type1_graphs if g in graph_files]
            return selected, config
        elif choice == '3':
            selected = [g for g in type2_graphs if g in graph_files]
            return selected, config
        elif choice == '4':
            return list(graph_names), config
        elif choice == '5':
            c_input = input("\n>> Nhập hoặc dán danh sách tên đồ thị (cách nhau bởi dấu phẩy hoặc khoảng trắng): ").strip()
            if not c_input:
                print("[!] Chưa nhập tên đồ thị nào.")
                continue
            selected = parse_graph_selection(c_input, graph_names, graph_files)
            if not selected:
                print(f"[!] Không tìm thấy đồ thị nào khớp với '{c_input}'.")
                continue
            return selected, config
        elif choice == '6':
            selected = interactive_dataset_selector(graph_files)
            if not selected:
                print("[!] Không có đồ thị nào được chọn.")
                continue
            return selected, config
        elif choice == '7':
            print("\n--- Tùy chỉnh siêu tham số nâng cao ---")
            dset_in = input(f"   Danh sách đồ thị (hoặc 'all') [mặc định 'karate,jazz']: ").strip()
            if not dset_in:
                dset_in = "karate,jazz"
            selected = parse_graph_selection(dset_in, graph_names, graph_files)
            if not selected:
                selected = ['karate']

            try:
                s_in = input(f"   Ngưỡng đường kính s-club [{config.s_club_threshold}]: ").strip()
                if s_in: config.s_club_threshold = int(s_in)
                gen_in = input(f"   Số thế hệ / epochs [{config.max_generations}]: ").strip()
                if gen_in:
                    config.max_generations = int(gen_in)
                    config.max_epochs = int(gen_in)
                seeds_in = input(f"   Số seeds [{config.num_seeds}]: ").strip()
                if seeds_in: config.num_seeds = int(seeds_in)
                workers_in = input(f"   Số workers song song [{config.num_workers}]: ").strip()
                if workers_in: config.num_workers = int(workers_in)
                pop_in = input(f"   Kích thước quần thể pop_size [{config.pop_size}]: ").strip()
                if pop_in: config.pop_size = int(pop_in)
            except Exception as ex:
                print(f"   [!] Nhập lỗi ({ex}), sử dụng giá trị mặc định.")
            return selected, config
        elif choice == '8':
            import subprocess
            subprocess.run([sys.executable, os.path.join(current_dir, "analysis", "render_enhanced_charts.py")])
            input("\n>> Nhấn [ENTER] để quay lại menu chính...")
            continue
        elif choice == '9':
            import subprocess
            subprocess.run([sys.executable, os.path.join(current_dir, "Tong_hop_so_lieu_phan_bien", "extract_and_consolidate.py")])
            input("\n>> Nhấn [ENTER] để quay lại menu chính...")
            continue
        elif choice == '10':
            import subprocess
            subprocess.run([sys.executable, os.path.join(current_dir, "verify_system.py")])
            input("\n>> Nhấn [ENTER] để quay lại menu chính...")
            continue
        elif choice == '11':
            import subprocess
            subprocess.run([sys.executable, os.path.join(current_dir, "check_env.py")])
            input("\n>> Nhấn [ENTER] để quay lại menu chính...")
            continue
        elif choice in ('0', 'q', 'exit', 'quit'):
            print("\n[*] Đang thoát. Cảm ơn bạn đã sử dụng EVO-RL MSCC Framework!")
            sys.exit(0)
        else:
            print("[!] Lựa chọn không hợp lệ. Vui lòng nhập từ 0 đến 11.")


def main():
    parser = argparse.ArgumentParser(description="EVO-RL: Deep RL-assisted Genetic Algorithm for Minimum s-Club Cover")
    parser.add_argument("--data_dir", type=str, default=os.path.join(current_dir, "pbodulieu"), help="Thư mục chứa đồ thị benchmark")
    parser.add_argument("--graph", type=str, default=None, help="Tên hoặc danh sách file đồ thị (vd: 'karate,jazz' hoặc 'johnson8-2-4.clq')")
    parser.add_argument("--run", type=str, default=None, help="Chỉ số hoặc dải đồ thị để chạy tự động (vd: '1,3,5' hoặc '1-5')")
    parser.add_argument("--all", action="store_true", help="Chạy tất cả đồ thị tìm thấy")
    parser.add_argument("--tui", action="store_true", help="Mở giao diện bảng tương tác TUI chọn đồ thị")
    parser.add_argument("--out_dir", type=str, default=os.path.join(current_dir, "results"), help="Thư mục lưu kết quả")
    parser.add_argument("--s", type=int, default=2, help="Ngưỡng đường kính s-club (mặc định s=2)")
    parser.add_argument("--epochs", type=int, default=200, help="Số thế hệ / epochs (mặc định 200)")
    parser.add_argument("--seeds", type=int, default=20, help="Số hạt giống ngẫu nhiên (mặc định 20)")
    parser.add_argument("--workers", type=int, default=10, help="Số tiến trình chạy song song (mặc định 10 seeds cùng lúc)")
    parser.add_argument("--pop_size", type=int, default=100, help="Kích thước quần thể di truyền (mặc định 100)")

    args = parser.parse_args()

    config = ExperimentConfig()
    config.s_club_threshold = args.s
    config.max_epochs = args.epochs
    config.max_generations = args.epochs
    config.num_seeds = args.seeds
    config.num_workers = args.workers
    config.pop_size = args.pop_size

    data_dir = args.data_dir
    graph_files = discover_graph_files(data_dir)

    if not graph_files:
        # Tự động tìm ở thư mục cha nếu đang chạy từ thư mục con (ví dụ Sanpham_nckh)
        parent_pbodulieu = os.path.abspath(os.path.join(current_dir, "..", "pbodulieu"))
        if os.path.exists(parent_pbodulieu):
            data_dir = parent_pbodulieu
            graph_files = discover_graph_files(data_dir)

    if not graph_files:
        print(f"[!] Không tìm thấy file đồ thị (.clq, .gml, .graph.bz2) nào trong: {data_dir}")
        return

    graph_names = list(graph_files.keys())

    # Tự động tạo thư mục phiên chạy mang tên ketqua kèm Ngày và Giờ (Timestamp)
    timestamp_str = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    session_dir_name = f"ketqua_{timestamp_str}"
    session_out_dir = os.path.join(args.out_dir, session_dir_name)
    os.makedirs(session_out_dir, exist_ok=True)

    print(f"\n[+] Thư mục lưu trữ phiên chạy: {session_out_dir}")

    # Khởi động luồng giám sát tài nguyên
    start_hardware_monitor()

    # Xác định danh sách đồ thị cần chạy
    selected_targets = []
    if args.graph:
        selected_targets = parse_graph_selection(args.graph, graph_names, graph_files)
        if not selected_targets:
            print(f"\n[!] Không tìm thấy đồ thị nào phù hợp với danh sách nhập: '{args.graph}'")
            return
    elif args.run is not None:
        selected_targets = parse_graph_selection(args.run, graph_names, graph_files)
        if not selected_targets:
            print(f"\n[!] Không tìm thấy đồ thị nào phù hợp với chỉ số: '{args.run}'")
            return
    elif args.all:
        selected_targets = list(graph_names)
    elif args.tui:
        selected_targets = interactive_dataset_selector(graph_files)
        if not selected_targets:
            print("\n[!] Không có đồ thị nào được chọn.")
            return
    else:
        # Chế độ tương tác qua Menu Console (Interactive Master Console Menu)
        selected_targets, config = interactive_menu(graph_files, config)
        if not selected_targets:
            print("\n[!] Không có đồ thị nào được chọn.")
            return

    # Hiển thị thông tin tóm tắt số lượng đồ thị được chọn
    print("\n" + "=" * 90)
    print(f" [V] ĐÃ XÁC NHẬN VÀ CHỌN THÀNH CÔNG: {len(selected_targets)} ĐỒ THỊ BENCHMARK")
    print("=" * 90)
    print(" Danh sách đồ thị sẽ thực nghiệm:")
    for i, name in enumerate(selected_targets, 1):
        print(f"   {i:2d}. {name}")
    print("-" * 90)
    print(f" Cấu hình thực nghiệm:")
    print(f"   * Số hạt giống (Seeds)          : {config.num_seeds} seeds cố định (từ seedun.md)")
    print(f"   * Số luồng song song (Workers)  : {config.num_workers} workers đa luồng")
    print(f"   * Ngưỡng đường kính s-club (s)  : s = {config.s_club_threshold}")
    print(f"   * Số thế hệ tối đa (Epochs/Gen) : {config.max_generations} thế hệ")
    print(f"   * Kích thước quần thể (Pop Size): {config.pop_size}")
    print(f"   * Thư mục lưu kết quả           : {session_out_dir}")
    print("=" * 90 + "\n")

    # Thực thi tuần tự từng đồ thị
    for i, name in enumerate(selected_targets, 1):
        print(f"\n>>> [Tiến trình: Đồ thị {i}/{len(selected_targets)}] Bắt đầu: {name}")
        try:
            G = load_graph(graph_files[name])
            run_single_graph_experiment(name, G, config, session_out_dir)
        except Exception as ex:
            print(f"[!] Lỗi khi chạy {name}: {ex}")

    print(f"\n[V] Hoàn tất toàn bộ {len(selected_targets)} đồ thị trong phiên chạy! Dữ liệu đã lưu tại: {session_out_dir}")


if __name__ == "__main__":
    main()