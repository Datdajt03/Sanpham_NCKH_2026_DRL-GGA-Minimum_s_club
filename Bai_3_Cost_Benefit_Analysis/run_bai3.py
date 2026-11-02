"""
Bai_3_Cost_Benefit_Analysis/run_bai3.py — CLI Runner chạy thực nghiệm cho Bài 3.
Cách dùng:
    python run_bai3.py --datasets Type1 --seeds 5
    python run_bai3.py --datasets all --seeds 20 --workers 4
"""
import os
import sys
if sys.stdout is not None:
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass
import argparse
import pandas as pd
from concurrent.futures import ProcessPoolExecutor, as_completed

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
for p in [parent_dir, current_dir]:
    if p not in sys.path:
        sys.path.insert(0, p)

from dataset.loader import discover_graph_files
from configs.config import get_fixed_seeds

try:
    from Bai_3_Cost_Benefit_Analysis.config_bai3 import Bai3Config
    from Bai_3_Cost_Benefit_Analysis.evaluate_bai3 import run_single_seed_bai3
    from Bai_3_Cost_Benefit_Analysis.analysis_bai3 import analyze_and_export_bai3_results
except ImportError:
    from config_bai3 import Bai3Config
    from evaluate_bai3 import run_single_seed_bai3
    from analysis_bai3 import analyze_and_export_bai3_results

TYPE1_NAMES = {
    'karate', 'chesapeake', 'dolphins', 'lesmis', 'polbooks',
    'football', 'jazz', 'celegans_metabolic', 'email'
}


def main():
    parser = argparse.ArgumentParser(description="Chạy thực nghiệm Bài 3 (Cost-Benefit & Overhead Analysis)")
    parser.add_argument('--datasets', type=str, default='Type1', choices=['Type1', 'Type2', 'all', 'demo'],
                        help="Tập dữ liệu (Type1, Type2, all, demo)")
    parser.add_argument('--seeds', type=int, default=20, help="Số lượng seeds cố định ghép cặp (từ seedun.md)")
    parser.add_argument('--workers', type=int, default=10, help="Số tiến trình chạy song song (10 workers)")
    parser.add_argument('--output', type=str, default=None, help="Thư mục xuất kết quả")
    args = parser.parse_args()

    config = Bai3Config()
    config.num_seeds = args.seeds
    config.num_workers = args.workers
    if args.output:
        config.output_dir = args.output

    os.makedirs(config.output_dir, exist_ok=True)
    data_dir = os.path.join(parent_dir, "pbodulieu")
    if not os.path.exists(data_dir):
        alt_dir = os.path.abspath(os.path.join(parent_dir, "..", "pbodulieu"))
        if os.path.exists(alt_dir):
            data_dir = alt_dir
    graph_dict = discover_graph_files(data_dir)

    all_graphs = []
    for name, fpath in graph_dict.items():
        gtype = "Type 1" if name in TYPE1_NAMES else "Type 2"
        all_graphs.append({'name': name, 'path': fpath, 'type': gtype})

    if args.datasets == 'Type1':
        target_graphs = [g for g in all_graphs if g['type'] == 'Type 1']
    elif args.datasets == 'Type2':
        target_graphs = [g for g in all_graphs if g['type'] == 'Type 2']
    elif args.datasets == 'demo':
        target_graphs = [g for g in all_graphs if g['name'] in ('karate', 'football', 'johnson8-2-4')]
    else:
        target_graphs = all_graphs

    fixed_seeds = get_fixed_seeds(config.num_seeds)
    print(f"=== BẮT ĐẦU THỰC NGHIỆM BÀI 3 (Cost-Benefit & Overhead Analysis) ===")
    print(f"Số lượng đồ thị: {len(target_graphs)} | Số seeds: {len(fixed_seeds)} (cố định từ seedun.md) | Số thuật toán: {len(config.conditions)}")
    print(f"Danh sách seeds: {fixed_seeds}")
    print(f"Thư mục lưu kết quả: {config.output_dir}")

    all_cost_records = []
    all_budget_records = []

    tasks = []
    for g in target_graphs:
        for cond in config.conditions:
            for seed_val in fixed_seeds:
                tasks.append((g['path'], g['name'], g['type'], cond, seed_val, config))

    print(f"Tổng số tác vụ cần thực thi: {len(tasks)}")

    completed = 0
    with ProcessPoolExecutor(max_workers=config.num_workers) as executor:
        futures = {
            executor.submit(run_single_seed_bai3, p, name, gtype, cond, s, config): (name, cond, s)
            for (p, name, gtype, cond, s, config) in tasks
        }
        for fut in as_completed(futures):
            name, cond, s = futures[fut]
            completed += 1
            try:
                cost_rec, snapshots = fut.result()
                all_cost_records.append(cost_rec)
                for b_sec, best_k in snapshots.items():
                    all_budget_records.append({
                        'dataset': name,
                        'method': cond,
                        'seed': s,
                        'time_budget_sec': b_sec,
                        'best_k_achieved': best_k
                    })
                print(f"[{completed}/{len(tasks)}] Hoàn thành: {name} | {cond} | Seed {s} -> Total: {cost_rec['runtime_total']:.2f}s (Inf: {cost_rec['runtime_ppo_inference']*1000:.1f}ms, Up: {cost_rec['runtime_ppo_update']*1000:.1f}ms)")
            except Exception as e:
                print(f"❌ Lỗi tại: {name} | {cond} | Seed {s}: {e}")

    cost_df = pd.DataFrame(all_cost_records)
    analyze_and_export_bai3_results(cost_df, all_budget_records, config.output_dir)
    print("\n✅ HOÀN TẤT THỰC NGHIỆM VÀ XUẤT DỮ LIỆU BÀI 3 THÀNH CÔNG!")


if __name__ == '__main__':
    main()
