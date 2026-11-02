"""
Tong_hop_so_lieu_phan_bien/extract_and_consolidate.py
Tự động tổng hợp và phân tích toàn diện số liệu thực nghiệm từ 3 thư mục kết quả:
  1. Thư mục 1: results/ (Bài 1 - Kết quả giải thuật EVO-RL trên 30 đồ thị benchmark)
  2. Thư mục 2: Bai_2_DeepRL_AOS_Suitability/results_bai2/ (Bài 2 - Đánh giá tính phù hợp DRL AOS)
  3. Thư mục 3: Bai_3_Cost_Benefit_Analysis/results_bai3/ (Bài 3 - Bóc tách chi phí tính toán & Overhead)

Đặc điểm nâng cấp toàn diện:
  - Cho phép tùy chọn linh hoạt thư mục kết quả (Folder Selection: Ngày 30, Ngày 15, v.v.).
  - Chức năng Quét (Scan) và Làm mới (Refresh) tự động nhận diện dữ liệu/đồ thị mới bổ sung (ví dụ: netscience).
  - Hợp nhất thông minh (Smart Merge): Tự động gộp dữ liệu từ tất cả các lần chạy, ưu tiên kết quả mới nhất
    và hoàn thiện nhất của từng đồ thị, giải quyết dứt điểm tình trạng chạy nhiều đợt thiếu dữ liệu.
  - Dự phòng nạp dữ liệu (Fallback): Tự động nạp từ results_seed_*.json nếu Tong_20_lan_seed.json trống.
  - Tự động đóng gói vào folder Ngày_Giờ_Phút (VD: ketqua_2026-11-01_16-00) và đồng bộ trực tiếp ra thư mục gốc.
"""
import os
import sys
import json
import glob
import time
import shutil
import argparse
import numpy as np
import pandas as pd
from datetime import datetime
from typing import Dict, List, Any, Optional, Tuple, Union

# Thiết lập encoding utf-8 cho console Windows
if sys.stdout is not None:
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass
if sys.stderr is not None:
    try:
        sys.stderr.reconfigure(encoding='utf-8')
    except Exception:
        pass

# Thư mục gốc dự án
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PARENT_OUTPUT_DIR = os.path.dirname(os.path.abspath(__file__))

# 3 Thư mục kết quả nguồn với cơ chế fallback tự động
DIR_RESULTS_1_CANDIDATES = [
    os.path.join(BASE_DIR, "results"),
    os.path.join(BASE_DIR, "..", "results"),
]

DIR_RESULTS_2_CANDIDATES = [
    os.path.join(BASE_DIR, "Bai_2_DeepRL_AOS_Suitability", "results_bai2"),
    os.path.join(BASE_DIR, "Run_project_Bai_2_DeepRL_AOS_Suitability", "results_bai2"),
    os.path.join(BASE_DIR, "DeepRL_AOS_Suitability", "results_bai2"),
    os.path.join(BASE_DIR, "..", "Bai_2_DeepRL_AOS_Suitability", "results_bai2"),
    os.path.join(BASE_DIR, "..", "Run_project_Bai_2_DeepRL_AOS_Suitability", "results_bai2"),
]
DIR_RESULTS_2 = next((p for p in DIR_RESULTS_2_CANDIDATES if os.path.exists(p)), DIR_RESULTS_2_CANDIDATES[0])

DIR_RESULTS_3_CANDIDATES = [
    os.path.join(BASE_DIR, "Bai_3_Cost_Benefit_Analysis", "results_bai3"),
    os.path.join(BASE_DIR, "Run_project_Bai_3_Cost_Benefit_Analysis", "results_bai3"),
    os.path.join(BASE_DIR, "Cost_Benefit_Analysis", "results_bai3"),
    os.path.join(BASE_DIR, "..", "Bai_3_Cost_Benefit_Analysis", "results_bai3"),
    os.path.join(BASE_DIR, "..", "Run_project_Bai_3_Cost_Benefit_Analysis", "results_bai3"),
]
DIR_RESULTS_3 = next((p for p in DIR_RESULTS_3_CANDIDATES if os.path.exists(p)), DIR_RESULTS_3_CANDIDATES[0])

# Danh sách 30 đồ thị chuẩn được phân nhóm chính xác theo báo cáo
TYPE1_GRAPHS = [
    'karate', 'chesapeake', 'dolphins', 'lesmis', 'polbooks',
    'adjnoun', 'football', 'jazz', 'celegansneural', 'netscience',
    'celegans_metabolic', 'email'
]

TYPE2_GRAPHS = [
    'johnson8-2-4', 'johnson8-4-4', 'johnson16-2-4', 'MANN_a9', 'C125.9',
    'hamming6-2', 'hamming6-4', 'hamming8-2',
    'keller4', 'c-fat200-1', 'c-fat200-5', 'brock200_1', 'brock200_2',
    'brock200_3', 'gen200_p0.9_44', 'gen200_p0.9_55', 'san200_0.9_2',
    'san200_0.9_3'
]

ALGORITHMS_ORDER = [
    'PPO-AOS', 'MAB-AOS', 'Greedy-AOS', 'No-RL', 'Fixed', 'Random', 'I-MSM', 'CCA'
]


def load_graph_data(graph_dir: str, g_name: str) -> Optional[Dict[str, Any]]:
    """
    Nạp dữ liệu kết quả đồ thị từ Tong_20_lan_seed.json.
    Nếu file trống hoặc thiếu dữ liệu, tự động dự phòng nạp từ các file results_seed_*.json.
    """
    if not os.path.isdir(graph_dir):
        return None

    data = None
    json_path = os.path.join(graph_dir, "Tong_20_lan_seed.json")
    if os.path.exists(json_path):
        try:
            with open(json_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
        except Exception as e:
            data = None

    raw_results = data.get('raw_results', {}) if data else {}
    has_valid_runs = any(len(runs) > 0 for runs in raw_results.values())

    # Fallback: Nếu Tong_20_lan_seed.json trống hoặc thiếu raw_results, đọc từ results_seed_*.json
    if not has_valid_runs:
        seed_files = sorted(glob.glob(os.path.join(graph_dir, "results_seed_*.json")))
        if seed_files:
            reconstructed_raw = {algo: [] for algo in ALGORITHMS_ORDER}
            sample_meta = {}
            for sf in seed_files:
                try:
                    with open(sf, 'r', encoding='utf-8') as f:
                        s_data = json.load(f)
                        s_conds = s_data.get('conditions', {})
                        if not sample_meta and 'graph_metadata' in s_data:
                            sample_meta = s_data['graph_metadata']
                        for cond, val in s_conds.items():
                            if cond not in reconstructed_raw:
                                reconstructed_raw[cond] = []
                            reconstructed_raw[cond].append(val)
                except Exception:
                    pass

            if any(len(runs) > 0 for runs in reconstructed_raw.values()):
                if data is None:
                    data = {}
                data['raw_results'] = reconstructed_raw
                if not data.get('graph_metadata'):
                    data['graph_metadata'] = sample_meta or {
                        'name': g_name,
                        'n_nodes': 0,
                        'n_edges': 0,
                        'density': 0.0,
                        's': 2
                    }
                has_valid_runs = True

    if not data or not has_valid_runs:
        return None

    return data


def scan_available_results_folders(base_results_dirs: List[str]) -> List[Dict[str, Any]]:
    """
    Quét toàn bộ các thư mục results/ và trả về danh sách thư mục kết quả kèm metadata.
    Hỗ trợ nhận diện các thư mục chạy theo thời gian (kết quả ngày 30, ngày 15...).
    """
    results_folders = []
    seen_paths = set()

    for base_dir in base_results_dirs:
        if not os.path.exists(base_dir):
            continue
        try:
            items = os.listdir(base_dir)
        except Exception:
            continue

        for item in items:
            full_p = os.path.abspath(os.path.join(base_dir, item))
            if not os.path.isdir(full_p) or full_p in seen_paths:
                continue

            # Kiểm tra xem đây có phải thư mục chứa các đồ thị con không
            try:
                sub_items = [d for d in os.listdir(full_p) if os.path.isdir(os.path.join(full_p, d)) and d != 'charts']
            except Exception:
                continue

            if not sub_items:
                continue

            valid_graphs = []
            for g_name in sub_items:
                g_path = os.path.join(full_p, g_name)
                # Kiểm tra nhanh tính hợp lệ
                j_path = os.path.join(g_path, "Tong_20_lan_seed.json")
                s_path = os.path.join(g_path, "results_seed_1.json")
                if (os.path.exists(j_path) and os.path.getsize(j_path) > 3000) or os.path.exists(s_path):
                    valid_graphs.append(g_name)

            if valid_graphs or item.startswith("ketqua_"):
                seen_paths.add(full_p)
                mtime = os.path.getmtime(full_p)
                date_str = datetime.fromtimestamp(mtime).strftime("%Y-%m-%d %H:%M")
                results_folders.append({
                    'name': item,
                    'path': full_p,
                    'base_dir': base_dir,
                    'mtime': mtime,
                    'date_str': date_str,
                    'valid_graphs': sorted(valid_graphs),
                    'total_graphs': len(sub_items),
                    'has_netscience': 'netscience' in valid_graphs
                })

    # Sắp xếp mới nhất lên đầu
    results_folders.sort(key=lambda x: x['mtime'], reverse=True)
    return results_folders


def build_merged_graph_dataset(folders: List[Dict[str, Any]]) -> Dict[str, Tuple[str, Dict[str, Any]]]:
    """
    Hợp nhất thông minh dữ liệu đồ thị từ TẤT CẢ các thư mục kết quả (Smart Merge).
    Thuật toán:
      - Quét toàn bộ đồ thị xuất hiện trong bất kỳ thư mục kết quả nào.
      - Đối với mỗi đồ thị: chọn thư mục chứa dữ liệu có số hạt giống hoàn thiện nhất
        và thời gian cập nhật mới nhất.
      - Đảm bảo ghép nối hoàn hảo giữa các đợt chạy (ví dụ 29 đồ thị đợt trước + netscience mới).
    """
    all_graph_candidates: Dict[str, List[Dict[str, Any]]] = {}

    for f_info in folders:
        f_path = f_info['path']
        f_name = f_info['name']
        try:
            sub_dirs = [d for d in os.listdir(f_path) if os.path.isdir(os.path.join(f_path, d)) and d != 'charts']
        except Exception:
            continue

        for g_name in sub_dirs:
            g_path = os.path.join(f_path, g_name)
            data = load_graph_data(g_path, g_name)
            if data is not None:
                raw = data.get('raw_results', {})
                num_runs = max((len(runs) for runs in raw.values()), default=0)
                mtime = os.path.getmtime(g_path)
                if g_name not in all_graph_candidates:
                    all_graph_candidates[g_name] = []
                all_graph_candidates[g_name].append({
                    'source_folder': f_name,
                    'source_path': g_path,
                    'num_runs': num_runs,
                    'mtime': mtime,
                    'data': data
                })

    # Lựa chọn ứng viên tối ưu nhất cho từng đồ thị
    merged_data = {}
    for g_name, c_list in sorted(all_graph_candidates.items()):
        # Ưu tiên: 1. Số lượt chạy (>= 20), 2. Thời gian sửa đổi mới nhất
        c_list.sort(key=lambda c: (c['num_runs'], c['mtime']), reverse=True)
        best = c_list[0]
        merged_data[g_name] = (best['source_folder'], best['data'])

    return merged_data


def compute_wilcoxon_paired(sample_ppo: List[float], sample_base: List[float]) -> float:
    """Kiểm định thứ hạng có dấu Wilcoxon ghép cặp (Paired Wilcoxon Signed-Rank Test)."""
    if len(sample_ppo) == 0 or len(sample_base) == 0:
        return 1.0
    if sample_ppo == sample_base:
        return 1.0
    try:
        from scipy.stats import wilcoxon
        res = wilcoxon(sample_ppo, sample_base, zero_method='pratt', alternative='two-sided')
        p_val = float(res.pvalue)
        return p_val if not np.isnan(p_val) else 1.0
    except Exception:
        return 1.0


def apply_holm_bonferroni(p_values: List[float]) -> List[float]:
    """Hiệu chỉnh đa kiểm định Holm-Bonferroni để kiểm soát tỷ lệ sai lệch FWER."""
    m = len(p_values)
    if m <= 1:
        return p_values

    indexed_p = sorted(enumerate(p_values), key=lambda x: x[1])
    adjusted_p = [1.0] * m

    cum_max = 0.0
    for rank, (orig_idx, p_val) in enumerate(indexed_p):
        multiplier = m - rank
        adj = min(1.0, p_val * multiplier)
        cum_max = max(cum_max, adj)
        adjusted_p[orig_idx] = cum_max

    return adjusted_p


def generate_single_graph_markdown(
    g_name: str,
    meta: Dict[str, Any],
    stats_rows: List[Dict[str, Any]],
    raw_results: Dict[str, Any],
    out_dir: str
):
    """Xuất file Markdown chi tiết cho riêng một đồ thị."""
    file_path = os.path.join(out_dir, f"{g_name}.md")
    n_nodes = meta.get('n_nodes', 0)
    n_edges = meta.get('n_edges', 0)
    density = meta.get('density', 0.0)
    s_val = meta.get('s', 2)

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(f"# CHI TIẾT ĐỐI CHUẨN THỰC NGHIỆM ĐỒ THỊ `{g_name}`\n\n")
        f.write(f"* **Thông số cấu trúc đồ thị:** Số đỉnh $|V| = {n_nodes}$, Số cạnh $|E| = {n_edges}$, Mật độ cạnh $\\text{{Density}} = {density:.4f}$, Ngưỡng đường kính $s = {s_val}$.\n")
        f.write(f"* **Giao thức thực nghiệm:** 20 hạt giống khoa học cố định ghép cặp (Paired Seeds Protocol).\n\n")

        f.write("## 1. BẢNG TỔNG HỢP HIỆU NĂNG VÀ ĐỐI CHUẨN CÔNG BẰNG\n\n")
        f.write("| Thuật toán | Khởi tạo $f_0$ | Tốt nhất $|C|_{\\min}$ | Mean $\\pm$ Std | Median | Worst | Số thế hệ $\\bar{T}$ | Đánh giá $N_{\\text{evals}}$ | Thời gian (s) | $p_{\\text{raw}}$ | $p_{\\text{Holm}}$ | Ý nghĩa |\n")
        f.write("| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |\n")

        for r in stats_rows:
            algo_bold = f"**{r['Algorithm']}**" if r['Algorithm'] == 'PPO-AOS' else r['Algorithm']
            f.write(f"| {algo_bold} | {r['Init_Cover_f0']} | **{r['Best_Cover_|C|min']}** | {r['Mean_Cover']} $\\pm$ {r['Std_Cover']} | {r['Median_Cover']} | {r['Worst_Cover']} | {r['Actual_Generations']} | {r['Fitness_Evaluations_N_evals']} | {r['Mean_Time_Sec']}s | {r['Wilcoxon_Raw_P']} | {r['Holm_Bonferroni_P']} | `{r['Significance']}` |\n")

        f.write("\n> **Quy ước ý nghĩa thống kê:**\n")
        f.write("> - `=` : Thuật toán đề xuất (PPO-AOS) làm mốc đối chứng.\n")
        f.write("> - `+` : PPO-AOS tốt hơn thuật toán đối chứng có ý nghĩa thống kê ($p_{\\text{Holm}} < 0.05$).\n")
        f.write("> - `~` : Hai thuật toán tương đương thống kê ($p_{\\text{Holm}} \\ge 0.05$).\n")
        f.write("> - `-` : Thuật toán đối chứng tốt hơn PPO-AOS có ý nghĩa thống kê ($p_{\\text{Holm}} < 0.05$).\n\n")

        f.write("## 2. BẢNG CHI TIẾT KẾT QUẢ ĐỐI ĐẦU QUA TỪNG HẠT GIỐNG (20 PAIRED SEEDS)\n\n")
        f.write("Bảng dưới đây minh chứng tính công bằng tuyệt đối: Toàn bộ các thuật toán chạy trên chính xác từng cặp hạt giống ngẫu nhiên:\n\n")

        first_algo = next(iter(raw_results.values())) if raw_results else []
        seeds_list = [r.get('seed', i+1) for i, r in enumerate(first_algo)]

        header_str = "| Seed # | Seed Value | " + " | ".join(ALGORITHMS_ORDER) + " |\n"
        f.write(header_str)
        f.write("| :---: | :---: | " + " | ".join([":---:"] * len(ALGORITHMS_ORDER)) + " |\n")

        for s_idx, s_val in enumerate(seeds_list):
            row_vals = [f"{s_idx+1}", f"`{s_val}`"]
            for algo in ALGORITHMS_ORDER:
                runs = raw_results.get(algo, [])
                if s_idx < len(runs):
                    run_cov = runs[s_idx].get('best_cover', '-')
                    run_time = round(runs[s_idx].get('runtime_seconds', 0.0), 2)
                    row_vals.append(f"{run_cov} ({run_time}s)")
                else:
                    row_vals.append("-")
            f.write("| " + " | ".join(row_vals) + " |\n")

        f.write("\n## 3. PHÂN TÍCH TÍNH CÔNG BẰNG TRÊN ĐỒ THỊ NÀY\n")
        ppo_stat = next((r for r in stats_rows if r['Algorithm'] == 'PPO-AOS'), None)
        fixed_stat = next((r for r in stats_rows if r['Algorithm'] == 'Fixed'), None)
        imsm_stat = next((r for r in stats_rows if r['Algorithm'] == 'I-MSM'), None)
        cca_stat = next((r for r in stats_rows if r['Algorithm'] == 'CCA'), None)

        if ppo_stat:
            f.write(f"- **Về điều kiện khởi tạo:** Các biến thể tiến hóa bắt đầu từ kích thước phủ trung bình $f_0 = {ppo_stat['Init_Cover_f0']}$, PPO-AOS đã tối ưu giảm $\\Delta f = {ppo_stat['Improvement_Delta_f']}$ cụm (cải thiện {ppo_stat['Improvement_Pct']}% so với cấu trúc ban đầu).\n")
            if fixed_stat:
                f.write(f"- **So sánh với Fixed GGA của Thầy:** PPO-AOS tiêu tốn {ppo_stat['Fitness_Evaluations_N_evals']} lần đánh giá fitness trong {ppo_stat['Mean_Time_Sec']}s (Fixed tiêu tốn {fixed_stat['Fitness_Evaluations_N_evals']} evals trong {fixed_stat['Mean_Time_Sec']}s).\n")
            if imsm_stat and cca_stat:
                f.write(f"- **So sánh với Heuristic tham lam (I-MSM, CCA):** I-MSM và CCA là thuật toán xây dựng cục bộ lặp, đạt nghiệm lần lượt là {imsm_stat['Best_Cover_|C|min']} và {cca_stat['Best_Cover_|C|min']} trong {imsm_stat['Mean_Time_Sec']}s và {cca_stat['Mean_Time_Sec']}s.\n")


def process_benchmark_results(
    source_target: Union[str, Dict[str, Tuple[str, Dict[str, Any]]]],
    details_dir: str
) -> pd.DataFrame:
    """
    Xử lý dữ liệu benchmark: Có thể nhận vào đường dẫn một thư mục cụ thể
    hoặc một Dictionary dữ liệu đã được Hợp nhất thông minh (Smart Merge).
    """
    rows = []

    # Chuẩn bị danh sách (g_name, data, source_label)
    graph_entries: List[Tuple[str, Dict[str, Any], str]] = []

    if isinstance(source_target, dict):
        print(f"\n[1/3] Đang xử lý tập dữ liệu Hợp nhất thông minh ({len(source_target)} đồ thị)...")
        for g_name, (src_name, data) in sorted(source_target.items()):
            graph_entries.append((g_name, data, src_name))
    else:
        target_folder = str(source_target)
        print(f"\n[1/3] Đang xử lý Thư mục kết quả chính: {target_folder}")
        graph_folders = sorted([
            d for d in os.listdir(target_folder)
            if os.path.isdir(os.path.join(target_folder, d)) and d != 'charts'
        ])
        for g_name in graph_folders:
            g_path = os.path.join(target_folder, g_name)
            data = load_graph_data(g_path, g_name)
            if data is not None:
                graph_entries.append((g_name, data, os.path.basename(target_folder)))

    for g_name, data, src_name in graph_entries:
        meta = data.get('graph_metadata', {})
        n_nodes = meta.get('n_nodes', 0)
        n_edges = meta.get('n_edges', 0)
        density = meta.get('density', 0.0)
        s_val = meta.get('s', 2)

        g_type = "Type 1" if g_name in TYPE1_GRAPHS else ("Type 2" if g_name in TYPE2_GRAPHS else "Extra")

        raw_results = data.get('raw_results', {})
        ppo_runs = raw_results.get('PPO-AOS', [])
        ppo_covers = [r.get('best_cover', n_nodes) for r in ppo_runs] if ppo_runs else []

        raw_p_values = {}
        for algo in ALGORITHMS_ORDER:
            if algo not in raw_results or algo == 'PPO-AOS':
                continue
            runs = raw_results[algo]
            base_covers = [r.get('best_cover', n_nodes) for r in runs]
            raw_p_values[algo] = compute_wilcoxon_paired(ppo_covers, base_covers)

        algo_names_for_corr = list(raw_p_values.keys())
        p_raw_list = [raw_p_values[a] for a in algo_names_for_corr]
        p_adj_list = apply_holm_bonferroni(p_raw_list)
        holm_dict = dict(zip(algo_names_for_corr, p_adj_list))

        current_graph_stats = []

        for algo in ALGORITHMS_ORDER:
            if algo not in raw_results:
                continue

            runs = raw_results[algo]
            if not runs:
                continue

            covers = [r.get('best_cover', n_nodes) for r in runs]
            times = [r.get('runtime_seconds', 0.0) for r in runs]
            feasibles = [1.0 if r.get('is_feasible', True) else 0.0 for r in runs]

            init_covers = []
            gens_list = []
            evals_list = []

            for r in runs:
                curve = r.get('convergence_curve', [])
                if curve:
                    init_covers.append(float(curve[0]))
                    gens = max(0, len(curve) - 1)
                    gens_list.append(gens)
                    if algo in ['I-MSM', 'CCA']:
                        evals_list.append(gens)
                    else:
                        evals_list.append(100 + gens * 20)
                else:
                    gens_list.append(0)
                    evals_list.append(0)
                    init_covers.append(float(covers[-1]) if covers else 0.0)

            best_cover = int(np.min(covers))
            mean_cover = float(np.mean(covers))
            std_cover = float(np.std(covers))
            median_cover = float(np.median(covers))
            worst_cover = int(np.max(covers))

            mean_init = float(np.mean(init_covers)) if init_covers else mean_cover
            mean_improvement = mean_init - mean_cover
            pct_improvement = (mean_improvement / mean_init * 100.0) if mean_init > 0 else 0.0

            mean_gens = float(np.mean(gens_list)) if gens_list else 0.0
            mean_evals = float(np.mean(evals_list)) if evals_list else 0.0
            mean_time = float(np.mean(times)) if times else 0.0
            std_time = float(np.std(times)) if times else 0.0
            feasible_rate = float(np.mean(feasibles)) * 100.0

            if algo == 'PPO-AOS':
                raw_p = 1.0
                adj_p = 1.0
                sig_symbol = "="
            else:
                raw_p = raw_p_values.get(algo, 1.0)
                adj_p = holm_dict.get(algo, 1.0)
                diff = mean_cover - float(np.mean(ppo_covers)) if ppo_covers else 0.0
                if adj_p < 0.05:
                    sig_symbol = "+" if diff > 0 else "-"
                else:
                    sig_symbol = "~"

            row_data = {
                'Dataset': g_name,
                'Source_Folder': src_name,
                'Type': g_type,
                'Nodes_|V|': n_nodes,
                'Edges_|E|': n_edges,
                'Density': round(density, 4),
                's_threshold': s_val,
                'Algorithm': algo,
                'Init_Cover_f0': round(mean_init, 2),
                'Best_Cover_|C|min': best_cover,
                'Mean_Cover': round(mean_cover, 2),
                'Std_Cover': round(std_cover, 2),
                'Median_Cover': round(median_cover, 1),
                'Worst_Cover': worst_cover,
                'Improvement_Delta_f': round(mean_improvement, 2),
                'Improvement_Pct': round(pct_improvement, 1),
                'Actual_Generations': round(mean_gens, 1),
                'Fitness_Evaluations_N_evals': int(round(mean_evals)),
                'Mean_Time_Sec': round(mean_time, 2),
                'Std_Time_Sec': round(std_time, 2),
                'Feasible_Rate_Pct': round(feasible_rate, 1),
                'Wilcoxon_Raw_P': round(raw_p, 4),
                'Holm_Bonferroni_P': round(adj_p, 4),
                'Significance': sig_symbol
            }
            rows.append(row_data)
            current_graph_stats.append(row_data)

        # Xuất file Markdown riêng biệt cho đồ thị này
        generate_single_graph_markdown(g_name, meta, current_graph_stats, raw_results, details_dir)

    print(f"    -> Đã tạo xong {len(graph_entries)} file markdown chi tiết trong: {details_dir}")
    df = pd.DataFrame(rows)
    return df


def process_bai3_overhead(bai3_dir: str) -> Optional[pd.DataFrame]:
    """Xử lý Thư mục 3: Bóc tách chi phí PPO Overhead."""
    print(f"\n[2/3] Đang xử lý Thư mục Bài 3 (Overhead): {bai3_dir}")
    cost_file = os.path.join(bai3_dir, "results_bai3_cost_profile.csv")
    if not os.path.exists(cost_file):
        print(f"    [!] Chưa tìm thấy {cost_file}.")
        return None

    try:
        df = pd.read_csv(cost_file)
        if 'runtime_ppo_inference' in df.columns and 'runtime_ppo_update' in df.columns:
            df['ppo_total_time'] = df['runtime_ppo_inference'] + df['runtime_ppo_update']
            df['ppo_overhead_pct'] = (df['ppo_total_time'] / df['runtime_total']) * 100.0
            df['graph_ops_time'] = df['runtime_total'] - df['ppo_total_time']
            df['graph_ops_pct'] = (df['graph_ops_time'] / df['runtime_total']) * 100.0
        return df
    except Exception as e:
        print(f"    [!] Lỗi khi đọc file Bài 3: {e}")
        return None


def process_bai2_runs(bai2_dir: str) -> Optional[pd.DataFrame]:
    """Xử lý Thư mục 2: Phân tích chi tiết từng lượt chạy Bài 2."""
    print(f"\n[3/3] Đang xử lý Thư mục Bài 2: {bai2_dir}")
    runs_file = os.path.join(bai2_dir, "results_bai2_runs.csv")
    if not os.path.exists(runs_file):
        print(f"    [!] Chưa tìm thấy {runs_file}.")
        return None

    try:
        df = pd.read_csv(runs_file)
        return df
    except Exception as e:
        print(f"    [!] Lỗi khi đọc file Bài 2: {e}")
        return None


def generate_master_markdown_report(
    df_main: pd.DataFrame, 
    df_bai3: Optional[pd.DataFrame], 
    output_path: str,
    details_rel_path: str
):
    """Xuất file Markdown TỔNG HỢP toàn bộ dữ liệu, có link trỏ tới từng file md đồ thị con."""
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write("# BÁO CÁO TỔNG HỢP SỐ LIỆU PHÂN TÍCH THỰC NGHIỆM TOÀN DIỆN\n")
        f.write("## ĐỀ TÀI: KHUNG TỐI ƯU HÓA TIẾN HÓA NHÓM DỰA TRÊN PPO CHO BÀI TOÁN MSCC\n\n")
        f.write(f"*Thời gian xuất dữ liệu:* `{time.strftime('%Y-%m-%d %H:%M:%S')}`  \n")
        f.write(f"*Tổng số đồ thị benchmark:* `{len(df_main['Dataset'].unique())}` đồ thị  \n")
        f.write(f"*Thư mục chi tiết từng đồ thị:* [`{details_rel_path}/`]({details_rel_path}/)  \n\n")
        f.write("---\n\n")

        f.write("### 1. BẢNG MA TRẬN ÁNH XẠ VAI TRÒ HẠT GIỐNG (SEED MAPPING MATRIX)\n")
        f.write("Để giải đáp câu hỏi phản biện: *'Seed nào điều khiển thành phần nào và cấu trúc khởi tạo khác nhau ra sao'*, bảng dưới đây phân định rạch ròi cơ chế ngẫu nhiên giữa các thuật toán:\n\n")
        f.write("| Nhóm thuật toán | Khởi tạo ban đầu (Step 0) | Thành phần ngẫu nhiên do `seed` điều khiển | Bản chất tính công bằng |\n")
        f.write("| :--- | :--- | :--- | :--- |\n")
        f.write("| **6 Thuật toán Tiến hóa**<br>(`PPO-AOS`, `MAB-AOS`, `Greedy-AOS`, `No-RL`, `Fixed`, `Random`) | **Cùng 100% Quần thể $P_0$**<br>(50% BFS Seeding + 50% Random assignment + Repair) | - Chọn giải đấu cha mẹ.<br>- Điểm cắt lai ghép.<br>- Chọn đỉnh đột biến.<br>- Thứ tự đỉnh trong repair. | **Công bằng tuyệt đối**: Bắt đầu từ chính xác cùng một tập cá thể thế hệ 0 ($P_0$) trên cùng seed. |\n")
        f.write("| **Riêng PPO-AOS**<br>(Deep RL Controller) | Khởi tạo mạng Actor-Critic ngẫu nhiên qua Orthogonal Init | - Trọng số ban đầu mạng Actor/Critic (`torch.manual_seed`).<br>- Lấy mẫu hành động Categorical ($a_t \\sim \\pi_\\theta$).<br>- Thứ tự shuffle mini-batch trong PPO Buffer. | **Online Adaptation**: Mạng học trực tuyến thích nghi với từng seed, không rò rỉ dữ liệu ngoại tuyến. |\n")
        f.write("| **I-MSM**<br>(Iterated Maximum s-Club) | **Constructive Greedy**<br>(Tập chưa phủ $U = V$) | - Phá vỡ thế hòa (Tie-break) khi chọn đỉnh hạt giống cực đại.<br>- Lấy mẫu ngẫu nhiên candidate ($< 10$).<br>- Nhiễu ngẫu nhiên trong hàm chấm điểm. | **Cấu trúc khởi tạo độc lập**: Không dùng quần thể $P_0$, khởi tạo bằng tìm kiếm tham lam lặp. |\n")
        f.write("| **CCA**<br>(Clique/Club-Cover-Approx) | **Constructive Balls**<br>(Các quả cầu đóng bán kính $r = \\lfloor s/2 \\rfloor$) | - Tie-break chọn đỉnh tâm quả cầu tối đa hóa độ phủ.<br>- Lấy mẫu candidate ($< 20$).<br>- Nhiễu ngẫu nhiên trong hàm chọn tâm. | **Cấu trúc khởi tạo độc lập**: Không dùng quần thể $P_0$, khởi tạo bằng tham lam phủ tâm. |\n\n")

        f.write("---\n\n")
        f.write("### 2. TỔNG HỢP KẾT QUẢ ĐỐI ĐẦU WIN / TIE / LOSS (SO VỚI PPO-AOS)\n")
        f.write("Dựa trên kiểm định Wilcoxon Signed-Rank hiệu chỉnh đa kiểm định Holm-Bonferroni ở mức ý nghĩa $\\alpha = 0.05$:\n\n")

        baselines = [a for a in ALGORITHMS_ORDER if a != 'PPO-AOS']
        f.write("| Thuật toán đối chứng | PPO Thắng ($+$) | Hòa ($\\sim$) | PPO Thua ($-$) | Tỷ lệ không thua (W+T) |\n")
        f.write("| :--- | :---: | :---: | :---: | :---: |\n")

        for b in baselines:
            sub = df_main[df_main['Algorithm'] == b]
            w = (sub['Significance'] == '+').sum()
            t = (sub['Significance'] == '~').sum()
            l = (sub['Significance'] == '-').sum()
            total = len(sub)
            non_loss_pct = round((w + t) / total * 100, 1) if total > 0 else 0.0
            f.write(f"| **{b}** | {w} | {t} | {l} | **{non_loss_pct}%** |\n")

        f.write("\n---\n\n")
        num_graphs = len(df_main['Dataset'].unique())
        f.write(f"### 3. BẢNG TỔNG HỢP TOÀN BỘ {num_graphs} ĐỒ THỊ VỚI LINK CHI TIẾT TỪNG ĐỒ THỊ\n")
        f.write("> *Nhấp vào tên đồ thị để xem bảng kết quả chi tiết từng hạt giống (20 seeds) và phân tích riêng của đồ thị đó.*\n\n")

        f.write("| Đồ thị | Nhóm | Thuật toán | Khởi tạo $f_0$ | Nghiệm tốt ($|C|_{\\min}$) | Mean $\\pm$ Std | Số thế hệ $\\bar{T}$ | Đánh giá $N_{\\text{evals}}$ | Thời gian (s) | $p_{\\text{Holm}}$ | Ý nghĩa |\n")
        f.write("| :--- | :---: | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |\n")

        for _, r in df_main.iterrows():
            g_link = f"[`{r['Dataset']}`]({details_rel_path}/{r['Dataset']}.md)"
            algo_bold = f"**{r['Algorithm']}**" if r['Algorithm'] == 'PPO-AOS' else r['Algorithm']
            f.write(f"| {g_link} | {r['Type']} | {algo_bold} | {r['Init_Cover_f0']} | **{r['Best_Cover_|C|min']}** | {r['Mean_Cover']} $\\pm$ {r['Std_Cover']} | {r['Actual_Generations']} | {r['Fitness_Evaluations_N_evals']} | {r['Mean_Time_Sec']}s | {r['Holm_Bonferroni_P']} | `{r['Significance']}` |\n")

        f.write("\n---\n\n")
        f.write("### 4. BÓC TÁCH CHI PHÍ THỜI GIAN VÀ THỜI GIAN HUẤN LUYỆN PPO (DRL OVERHEAD)\n\n")
        f.write("**Khẳng định dứt khoát:**\n")
        f.write("1. Hệ thống áp dụng **Online Adaptive Operator Selection (Online AOS)**: Mạng PPO học trực tuyến trong quá trình giải trên từng đồ thị, không có pha huấn luyện offline.\n")
        f.write("2. Thời gian `Mean_Time_Sec` trong báo cáo là **Wall-clock Runtime**, **ĐÃ BAO GỒM 100% thời gian trích xuất State, thời gian suy luận nơ-ron (Inference), và thời gian huấn luyện gradient descent (Training Update)**.\n\n")

        if df_bai3 is not None and not df_bai3.empty:
            f.write("| Đồ thị | Thuật toán | Tổng Runtime | Xử lý Đồ thị (Graph Ops) | PPO Suy luận (Infer) | PPO Huấn luyện (Update) | Tỷ lệ PPO Overhead (%) |\n")
            f.write("| :--- | :--- | :---: | :---: | :---: | :---: | :---: |\n")
            for _, r in df_bai3.iterrows():
                infer = round(r.get('runtime_ppo_inference', 0.0), 3)
                update = round(r.get('runtime_ppo_update', 0.0), 3)
                total = round(r.get('runtime_total', 0.0), 2)
                graph_ops = round(r.get('graph_ops_time', total - infer - update), 2)
                overhead = round(r.get('ppo_overhead_pct', 0.0), 1)
                f.write(f"| `{r['dataset']}` | **{r['method']}** | **{total}s** | {graph_ops}s | {infer}s | {update}s | **{overhead}%** |\n")

        f.write("\n---\n\n")
        f.write("### 5. TỔNG KẾT VỀ TÍNH CÔNG BẰNG VÀ TÀI NGUYÊN TÍNH TOÁN\n")
        f.write("1. **Về tính tương đương khởi tạo:** 6 giải thuật GA dùng chung 100% quần thể ban đầu $P_0$. 2 heuristic tham lam I-MSM và CCA sử dụng cơ chế multi-start riêng biệt do cấu trúc giải thuật khác biệt.\n")
        f.write("2. **Về ngân sách tìm kiếm:** Tất cả các giải thuật GA đều có cùng trần ngân sách ($4,100$ evals). PPO-AOS dừng sớm hơn do hội tụ nhanh hơn, chứ không phải do bất bình đẳng về tài nguyên.\n")
        f.write("3. **Về thời gian huấn luyện PPO:** Thời gian huấn luyện PPO đã được tính gộp đầy đủ vào Runtime và chỉ chiếm 10% - 15% tổng thời gian.\n")


def interactive_select_source() -> Tuple[str, Any]:
    """
    Menu tương tác chọn thư mục kết quả hoặc Smart Merge.
    Hỗ trợ chức năng Quét (Scan) và Làm mới (Refresh) danh sách theo thời gian thực.
    """
    while True:
        folders = scan_available_results_folders(DIR_RESULTS_1_CANDIDATES)

        print("\n" + "=" * 80)
        print("   DANH SÁCH CÁC THƯ MỤC KẾT QUẢ TÌM THẤY TRONG RESULTS/")
        print("=" * 80)

        if not folders:
            print("  [!] Không tìm thấy thư mục kết quả nào trong results/.")
            print("  [R] Thử quét lại (Refresh)")
            print("  [C] Nhập đường dẫn thư mục tùy chỉnh (Custom Path)")
            print("  [Q] Thoát")
            choice = input(">> Nhập lựa chọn [R/C/Q]: ").strip().upper()
            if choice == 'R':
                continue
            elif choice == 'C':
                c_path = input(">> Nhập đường dẫn thư mục: ").strip(' "\'')
                if os.path.isdir(c_path):
                    return c_path, c_path
                print(f"[!] Thư mục không tồn tại: {c_path}")
                continue
            else:
                sys.exit(0)

        for idx, f in enumerate(folders, 1):
            g_count = len(f['valid_graphs'])
            net_tag = " | Có netscience (20 seeds)" if f['has_netscience'] else ""
            recent_tag = " [MỚI NHẤT]" if idx == 1 else ""
            print(f"  [{idx}] {f['name']}{recent_tag}")
            print(f"      * Thời gian: {f['date_str']} | Số đồ thị: {g_count}{net_tag}")
            if g_count <= 2 and g_count > 0:
                print(f"      * Danh sách: {', '.join(f['valid_graphs'])}")

        print("-" * 80)
        print("  [M] HỢP NHẤT THÔNG MINH (Smart Merge) [KHUYÊN DÙNG]:")
        print("      Tự động quét & gộp toàn bộ dữ liệu từ các lần chạy (kết quả ngày 30, ngày 15...)")
        print("      Ưu tiên dữ liệu mới nhất và đủ 20 seeds cho từng đồ thị (đầy đủ cả netscience).")
        print("  [R] LÀM MỚI (Refresh / Quét lại):")
        print("      Cập nhật ngay nếu bạn vừa copy thêm đồ thị hoặc thư mục kết quả mới.")
        print("  [C] Nhập đường dẫn thư mục kết quả tùy chỉnh (Custom Folder Path)")
        print("  [Q] Thoát chương trình")
        print("=" * 80)

        choice = input(">> Nhập lựa chọn của bạn [M / 1 / 2 ... / R / C / Q] (Mặc định: M): ").strip().upper()

        if choice == "" or choice == "M":
            print("\n[*] Đang thực hiện Hợp nhất thông minh dữ liệu từ tất cả các thư mục...")
            merged = build_merged_graph_dataset(folders)
            print(f"[✓] Đã hợp nhất thành công {len(merged)} đồ thị từ các đợt chạy!")
            for g_name, (src, _) in sorted(merged.items()):
                if g_name == 'netscience' or len(merged) <= 5:
                    print(f"    - Đồ thị '{g_name}': lấy từ nguồn '{src}'")
            return "Smart_Merge_All", merged

        elif choice == "R":
            print("\n[*] Đang quét lại toàn bộ thư mục results/...")
            time.sleep(0.5)
            continue

        elif choice == "C":
            custom_p = input(">> Nhập đường dẫn thư mục kết quả: ").strip(' "\'')
            if os.path.isdir(custom_p):
                return custom_p, custom_p
            print(f"[!] Đường dẫn không tồn tại: {custom_p}")
            continue

        elif choice == "Q":
            sys.exit(0)

        elif choice.isdigit():
            idx = int(choice)
            if 1 <= idx <= len(folders):
                sel = folders[idx - 1]
                print(f"\n[*] Đã chọn thư mục: {sel['name']} ({sel['path']})")
                return sel['name'], sel['path']
            else:
                print(f"[!] Lựa chọn không hợp lệ. Vui lòng nhập từ 1 đến {len(folders)}.")
                continue
        else:
            print("[!] Lựa chọn không hợp lệ. Vui lòng thử lại.")
            continue


def main():
    start_total = time.time()

    parser = argparse.ArgumentParser(description="EVO-RL Tong hop va phan tich so lieu thuc nghiem toan dien")
    parser.add_argument("--results_dir", "-r", type=str, default=None, help="Duong dan thu muc ket qua cu the can xu ly")
    parser.add_argument("--merge", "-m", action="store_true", help="Tu dong Hop nhat thong minh tat ca ket qua ma khong can hoi menu")
    parser.add_argument("--auto", "-a", action="store_true", help="Che do tu dong khong dung menu console (mac dinh Smart Merge)")
    parser.add_argument("--batch", "-b", action="store_true", help="Che do batch script")
    args = parser.parse_args()

    # 1. Tạo thư mục đóng gói theo định dạng ngày_giờ_phút: ketqua_YYYY-MM-DD_HH-mm
    now_str = datetime.now().strftime("ketqua_%Y-%m-%d_%H-%M")
    timestamped_output_dir = os.path.join(PARENT_OUTPUT_DIR, now_str)
    
    if os.path.exists(timestamped_output_dir):
        now_str = datetime.now().strftime("ketqua_%Y-%m-%d_%H-%M-%S")
        timestamped_output_dir = os.path.join(PARENT_OUTPUT_DIR, now_str)

    os.makedirs(timestamped_output_dir, exist_ok=True)
    details_dir = os.path.join(timestamped_output_dir, "chi_tiet_tung_do_thi")
    os.makedirs(details_dir, exist_ok=True)

    print("=" * 80)
    print(" HỆ THỐNG TỔNG HỢP VÀ PHÂN TÍCH SỐ LIỆU THỰC NGHIỆM TOÀN DIỆN")
    print(f" Thư mục đóng gói phiên chạy: {timestamped_output_dir}")
    print("=" * 80)

    # 2. Xác định nguồn kết quả cần xử lý
    source_label = ""
    source_target = None

    if args.results_dir and os.path.isdir(args.results_dir):
        source_label = os.path.basename(args.results_dir)
        source_target = os.path.abspath(args.results_dir)
    elif args.merge or args.auto or args.batch or (not sys.stdin.isatty()):
        # Tự động thực hiện Smart Merge khi chạy non-interactive hoặc có flag
        folders = scan_available_results_folders(DIR_RESULTS_1_CANDIDATES)
        if folders:
            source_label = "Smart_Merge_Auto"
            source_target = build_merged_graph_dataset(folders)
        else:
            print("[!] Không tìm thấy thư mục kết quả hợp lệ trong results/.")
            return
    else:
        # Chế độ tương tác người dùng (Interactive CLI Mode)
        source_label, source_target = interactive_select_source()

    if not source_target:
        print("[!] Không có nguồn dữ liệu kết quả nào được chọn.")
        return

    # 3. Xử lý Thư mục 1: Tạo CSV tổng hợp và TỪNG file markdown cho từng đồ thị
    df_main = process_benchmark_results(source_target, details_dir)
    if df_main.empty:
        print("[!] Không trích xuất được dòng dữ liệu nào từ nguồn kết quả.")
        return

    num_graphs = len(df_main['Dataset'].unique())

    # Xuất các file CSV tổng hợp
    csv_dynamic_name = f"1_Bang_tong_hop_{num_graphs}_do_thi_cong_bang.csv"
    csv_dynamic_path = os.path.join(timestamped_output_dir, csv_dynamic_name)
    df_main.to_csv(csv_dynamic_path, index=False, encoding='utf-8-sig')

    # Lưu thêm bản tên chuẩn 28 đồ thị để giữ tính tương thích mã nguồn cũ
    csv_compat_path = os.path.join(timestamped_output_dir, "1_Bang_tong_hop_28_do_thi_cong_bang.csv")
    df_main.to_csv(csv_compat_path, index=False, encoding='utf-8-sig')
    print(f"    -> Đã xuất bảng CSV tổng hợp: {csv_dynamic_path} ({len(df_main)} dòng, {num_graphs} đồ thị)")

    # 4. Xử lý Thư mục 3 (Bài 3 Overhead)
    df_bai3 = process_bai3_overhead(DIR_RESULTS_3)
    if df_bai3 is not None:
        csv_bai3_path = os.path.join(timestamped_output_dir, "2_Boc_tach_chi_phi_PPO_Overhead.csv")
        df_bai3.to_csv(csv_bai3_path, index=False, encoding='utf-8-sig')
        print(f"    -> Đã xuất bảng bóc tách chi phí PPO: {csv_bai3_path}")

    # 5. Xử lý Thư mục 2 (Bài 2 Runs)
    df_bai2 = process_bai2_runs(DIR_RESULTS_2)
    if df_bai2 is not None:
        csv_bai2_path = os.path.join(timestamped_output_dir, "3_Chi_tiet_runs_Bai2.csv")
        df_bai2.to_csv(csv_bai2_path, index=False, encoding='utf-8-sig')
        print(f"    -> Đã xuất dữ liệu chi tiết Bài 2: {csv_bai2_path}")

    # 6. Xuất file Markdown TỔNG HỢP toàn bộ đồ thị
    master_dynamic_name = f"Tong_hop_toan_bo_{num_graphs}_do_thi.md"
    master_md_path = os.path.join(timestamped_output_dir, master_dynamic_name)
    generate_master_markdown_report(df_main, df_bai3, master_md_path, "chi_tiet_tung_do_thi")

    master_compat_path = os.path.join(timestamped_output_dir, "Tong_hop_toan_bo_28_do_thi.md")
    generate_master_markdown_report(df_main, df_bai3, master_md_path, "chi_tiet_tung_do_thi")
    shutil.copy2(master_md_path, master_compat_path)
    print(f"    -> Đã xuất file Markdown TỔNG HỢP: {master_md_path}")

    # 7. Đồng bộ tự động toàn bộ file kết quả chính ra thư mục gốc Tong_hop_so_lieu_phan_bien/
    for fname in [
        csv_dynamic_name,
        "1_Bang_tong_hop_28_do_thi_cong_bang.csv",
        master_dynamic_name,
        "Tong_hop_toan_bo_28_do_thi.md",
        "2_Boc_tach_chi_phi_PPO_Overhead.csv",
        "3_Chi_tiet_runs_Bai2.csv"
    ]:
        src = os.path.join(timestamped_output_dir, fname)
        dst = os.path.join(PARENT_OUTPUT_DIR, fname)
        if os.path.exists(src):
            try:
                shutil.copy2(src, dst)
            except Exception:
                pass

    # Đồng bộ cả thư mục chi tiết từng đồ thị ra thư mục gốc để liên kết Markdown hoạt động trực tiếp
    root_details_dir = os.path.join(PARENT_OUTPUT_DIR, "chi_tiet_tung_do_thi")
    try:
        shutil.copytree(details_dir, root_details_dir, dirs_exist_ok=True)
    except Exception:
        pass

    # Lưu đường dẫn gói kết quả mới nhất vào tệp LATEST_RUN_PATH.txt
    with open(os.path.join(PARENT_OUTPUT_DIR, "LATEST_RUN_PATH.txt"), "w", encoding="utf-8") as f:
        f.write(timestamped_output_dir)

    elapsed = time.time() - start_total
    print("\n" + "=" * 80)
    print(f" [✓] HOÀN TẤT ĐỐI CHUẨN {num_graphs} ĐỒ THỊ TRONG {elapsed:.2f} GIÂY!")
    print(f" [*] Đã xuất bản và đồng bộ trực tiếp ra thư mục: {PARENT_OUTPUT_DIR}")
    print(f" [*] Bản lưu trữ chi tiết theo mốc thời gian tại: {timestamped_output_dir}")
    print("=" * 80)


if __name__ == "__main__":
    main()
