"""
analysis/render_enhanced_charts.py — Hệ thống kết xuất biểu đồ khoa học chuẩn bài báo quốc tế.
Tự động quét toàn bộ thư mục results/, trích xuất dữ liệu từ các lần chạy 20 seeds
và tạo thư mục 'Chart_seed' chứa 7 biểu đồ phân tích chuẩn 600 DPI (PNG) + Vector (PDF).

NGUYÊN TẮC BẢO TOÀN DỮ LIỆU KHOA HỌC:
- Tuyệt đối KHÔNG làm sai lệch hay thổi phồng số liệu thực nghiệm.
- Dữ liệu vẽ trên biểu đồ khớp 100% với file JSON/CSV thô (Exact Raw Data).
- Hỗ trợ trục phụ kép (Twin Axis) để vừa thể hiện xác suất gốc P(a|s), vừa thể hiện độ lệch tương đối ΔP(%).
- Xuất song song PNG siêu nét (600 DPI) và Vector PDF (không bao giờ vỡ nét khi phóng to).
- Phông chữ Sans-serif chuẩn Unicode (Arial / Segoe UI / DejaVu Sans) hiển thị tiếng Việt hoàn hảo.
"""
import os
import sys

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

import json
import glob
import time
import argparse
from datetime import datetime
import numpy as np
import matplotlib
matplotlib.use('Agg')  # Non-interactive backend an toàn cho batch mode
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from typing import Dict, Any, List, Optional, Tuple

# Thiết lập phong cách đồ thị khoa học chuẩn IEEE / Elsevier / ACM
plt.style.use('seaborn-v0_8-whitegrid' if 'seaborn-v0_8-whitegrid' in plt.style.available else 'default')
plt.rcParams.update({
    'font.family': 'sans-serif',
    'font.sans-serif': ['Arial', 'Segoe UI', 'DejaVu Sans', 'Calibri', 'Helvetica'],
    'axes.unicode_minus': False,
    'font.size': 11,
    'axes.labelsize': 11.5,
    'axes.titlesize': 12.5,
    'xtick.labelsize': 10,
    'ytick.labelsize': 10,
    'legend.fontsize': 9.5,
    'figure.titlesize': 13.5,
    'figure.dpi': 600,
    'savefig.dpi': 600,
    'savefig.bbox': 'tight',
    'savefig.pad_inches': 0.15
})

# Bảng màu khoa học tiêu chuẩn phân định rõ ràng
COLOR_MAP = {
    'crossover': '#1f77b4',     # Structural Crossover (Xanh lam)
    'repair': '#2ca02c',        # Feasibility Mutation / Repair (Xanh lá)
    'diversify': '#d62728',     # Diversification Mutation (Đỏ)
    'PPO-AOS': '#1f77b4',       # Xanh lam
    'MAB-AOS': '#9467bd',       # Tím
    'Greedy-AOS': '#e377c2',    # Hồng cánh sen
    'I-MSM': '#8c564b',         # Nâu đất
    'CCA': '#17becf',           # Xanh ngọc
    'No-RL': '#ff7f0e',         # Cam
    'Fixed': '#2ca02c',         # Xanh lá cây
    'Random': '#7f7f7f'         # Xám
}


def save_chart_both_formats(fig, base_path_no_ext: str):
    """Lưu song song biểu đồ dưới dạng PNG siêu nét (600 DPI) và Vector PDF."""
    png_path = f"{base_path_no_ext}.png"
    pdf_path = f"{base_path_no_ext}.pdf"
    fig.savefig(png_path, dpi=600, bbox_inches='tight')
    fig.savefig(pdf_path, bbox_inches='tight')
    plt.close(fig)


# ==============================================================================
# CÁC HÀM VẼ BIỂU ĐỒ CHUYÊN SÂU CHUẨN KHOA HỌC
# ==============================================================================

def draw_best_seed_action_chart(ppo_raw_seeds: List[Dict[str, Any]], out_dir: str, graph_name: str):
    """
    Biểu đồ 1: Động thái xác suất chọn toán tử của Best Seed (Seed tìm ra nghiệm tối ưu nhất).
    Sử dụng số liệu thô 100% không bóp méo, hiển thị song song xác suất gốc P(a|s) và độ lệch ΔP(%).
    """
    if not ppo_raw_seeds:
        return

    best_seed_item = min(ppo_raw_seeds, key=lambda s: (s.get('best_cover', 99999), s.get('best_fitness', 99999)))
    action_probs = np.array(best_seed_item.get('action_probs', []))
    if len(action_probs) == 0:
        return

    seed_val = best_seed_item.get('seed', 'N/A')
    best_cover = best_seed_item.get('best_cover', 'N/A')
    n_gens = len(action_probs)
    gens = np.arange(1, n_gens + 1)

    fig, ax1 = plt.subplots(figsize=(9.2, 5.2), dpi=600)

    # Vẽ 3 đường xác suất thực nghiệm
    ax1.plot(gens, action_probs[:, 0], label="Structural Crossover ($a^{cross}$)", color=COLOR_MAP['crossover'], linewidth=2.3)
    ax1.plot(gens, action_probs[:, 1], label="Feasibility Repair ($a^{repair}$)", color=COLOR_MAP['repair'], linewidth=2.3)
    ax1.plot(gens, action_probs[:, 2], label="Diversification Mutation ($a^{div}$)", color=COLOR_MAP['diversify'], linewidth=2.3)
    ax1.axhline(1/3, color='#555555', linestyle=':', linewidth=1.5, label='Mức ngẫu nhiên ($1/3 \\approx 0.3333$)')

    p_min, p_max = float(np.min(action_probs)), float(np.max(action_probs))
    span = max(0.005, p_max - p_min)
    margin = span * 0.25
    y_low = max(0.0, p_min - margin)
    y_high = min(1.0, p_max + margin)
    ax1.set_ylim(y_low, y_high)

    ax1.set_xlabel("Thế hệ tiến hóa (Generations)", fontweight='bold')
    ax1.set_ylabel("Xác suất chọn toán tử P(a|s) [Số liệu thực nghiệm]", fontweight='bold')
    ax1.grid(True, linestyle='--', alpha=0.5)

    # Trục phụ biểu diễn độ lệch phần trăm Delta P %
    ax2 = ax1.twinx()
    ax2.set_ylim((y_low - 1/3) * 100, (y_high - 1/3) * 100)
    ax2.set_ylabel("Độ lệch ưu tiên so với ngẫu nhiên ΔP (%)", fontweight='bold', color='#444444')
    ax2.grid(False)

    ax1.set_title(f"Động thái thích nghi toán tử PPO-AOS (Best Seed: {seed_val}, Best Cover: {best_cover})\nĐồ thị: {graph_name} | Dữ liệu thực nghiệm nguyên bản (Exact Raw)", fontweight='bold', pad=12)

    # Đặt Legend ở dưới đáy biểu đồ để không che khuất dữ liệu
    ax1.legend(loc='upper center', bbox_to_anchor=(0.5, -0.16), ncol=4, frameon=True, facecolor='white', framealpha=0.95, edgecolor='#cccccc')

    out_base = os.path.join(out_dir, "1_action_probability_best_seed")
    save_chart_both_formats(fig, out_base)


def draw_amplified_probability_chart(ppo_raw_seeds: List[Dict[str, Any]], out_dir: str, graph_name: str):
    """
    Biểu đồ 2: Động thái xác suất trung bình trên 20 Seeds độc lập (Mean ± Std).
    Đảm bảo 100% trung thực số liệu, thể hiện rõ dải phân sai và xu hướng hội tụ của chính sách RL.
    """
    if not ppo_raw_seeds:
        return

    all_probs = [s['action_probs'] for s in ppo_raw_seeds if len(s.get('action_probs', [])) > 0]
    if not all_probs:
        return

    min_len = min(len(p) for p in all_probs)
    probs_matrix = np.array([p[:min_len] for p in all_probs])  # shape (n_seeds, min_len, 3)
    mean_probs = np.mean(probs_matrix, axis=0)
    std_probs = np.std(probs_matrix, axis=0)
    gens = np.arange(1, min_len + 1)

    fig, ax1 = plt.subplots(figsize=(9.2, 5.2), dpi=600)

    # Crossover
    ax1.plot(gens, mean_probs[:, 0], label="Structural Crossover ($a^{cross}$)", color=COLOR_MAP['crossover'], linewidth=2.4)
    ax1.fill_between(gens, np.clip(mean_probs[:, 0] - std_probs[:, 0], 0, 1),
                     np.clip(mean_probs[:, 0] + std_probs[:, 0], 0, 1), color=COLOR_MAP['crossover'], alpha=0.15)

    # Repair
    ax1.plot(gens, mean_probs[:, 1], label="Feasibility Repair ($a^{repair}$)", color=COLOR_MAP['repair'], linewidth=2.4)
    ax1.fill_between(gens, np.clip(mean_probs[:, 1] - std_probs[:, 1], 0, 1),
                     np.clip(mean_probs[:, 1] + std_probs[:, 1], 0, 1), color=COLOR_MAP['repair'], alpha=0.15)

    # Diversify
    ax1.plot(gens, mean_probs[:, 2], label="Diversification Mutation ($a^{div}$)", color=COLOR_MAP['diversify'], linewidth=2.4)
    ax1.fill_between(gens, np.clip(mean_probs[:, 2] - std_probs[:, 2], 0, 1),
                     np.clip(mean_probs[:, 2] + std_probs[:, 2], 0, 1), color=COLOR_MAP['diversify'], alpha=0.15)

    ax1.axhline(1/3, color='#555555', linestyle=':', linewidth=1.5, label='Mức ngẫu nhiên ($1/3 \\approx 0.3333$)')

    p_min = float(np.min(mean_probs - std_probs))
    p_max = float(np.max(mean_probs + std_probs))
    span = max(0.005, p_max - p_min)
    margin = span * 0.2
    y_low = max(0.0, p_min - margin)
    y_high = min(1.0, p_max + margin)
    ax1.set_ylim(y_low, y_high)

    ax1.set_xlabel("Thế hệ tiến hóa (Generations)", fontweight='bold')
    ax1.set_ylabel("Xác suất chọn toán tử P(a|s) [Trung bình 20 Seeds ± Std]", fontweight='bold')
    ax1.grid(True, linestyle='--', alpha=0.5)

    # Trục phụ biểu diễn độ lệch phần trăm Delta P %
    ax2 = ax1.twinx()
    ax2.set_ylim((y_low - 1/3) * 100, (y_high - 1/3) * 100)
    ax2.set_ylabel("Độ lệch ưu tiên so với ngẫu nhiên ΔP (%)", fontweight='bold', color='#444444')
    ax2.grid(False)

    ax1.set_title(f"Xác suất thích nghi toán tử PPO-AOS (Trung bình 20 Seeds độc lập ± 1 Std)\nĐồ thị: {graph_name} | Dữ liệu thực nghiệm nguyên bản (Exact Raw)", fontweight='bold', pad=12)
    ax1.legend(loc='upper center', bbox_to_anchor=(0.5, -0.16), ncol=4, frameon=True, facecolor='white', framealpha=0.95, edgecolor='#cccccc')

    out_base = os.path.join(out_dir, "2_action_probability_amplified")
    save_chart_both_formats(fig, out_base)


def draw_relative_preference_chart(ppo_raw_seeds: List[Dict[str, Any]], out_dir: str, graph_name: str):
    """
    Biểu đồ 3: Độ lệch ưu tiên tương đối ΔP = (P(a|s) - 1/3) * 100% (Relative Preference Deviations).
    Trục 0% là mốc chuẩn ngẫu nhiên. Vùng > 0% là PPO ưu tiên, vùng < 0% là PPO kiềm chế.
    """
    if not ppo_raw_seeds:
        return

    all_probs = [s['action_probs'] for s in ppo_raw_seeds if len(s.get('action_probs', [])) > 0]
    if not all_probs:
        return

    min_len = min(len(p) for p in all_probs)
    probs_matrix = np.array([p[:min_len] for p in all_probs])
    mean_probs = np.mean(probs_matrix, axis=0)
    std_probs = np.std(probs_matrix, axis=0)

    delta_p = (mean_probs - (1.0 / 3.0)) * 100.0  # Đơn vị %
    delta_std = std_probs * 100.0
    gens = np.arange(1, min_len + 1)

    fig, ax = plt.subplots(figsize=(9.2, 5.2), dpi=600)
    ax.axhline(0, color='black', linewidth=1.2, linestyle='-', alpha=0.8, label='Mốc chuẩn ngẫu nhiên (ΔP = 0%)')

    ax.plot(gens, delta_p[:, 0], label="Δ Crossover ($a^{cross}$)", color=COLOR_MAP['crossover'], linewidth=2.3)
    ax.fill_between(gens, delta_p[:, 0] - delta_std[:, 0], delta_p[:, 0] + delta_std[:, 0], color=COLOR_MAP['crossover'], alpha=0.15)

    ax.plot(gens, delta_p[:, 1], label="Δ Feasibility Repair ($a^{repair}$)", color=COLOR_MAP['repair'], linewidth=2.3)
    ax.fill_between(gens, delta_p[:, 1] - delta_std[:, 1], delta_p[:, 1] + delta_std[:, 1], color=COLOR_MAP['repair'], alpha=0.15)

    ax.plot(gens, delta_p[:, 2], label="Δ Diversification Mutation ($a^{div}$)", color=COLOR_MAP['diversify'], linewidth=2.3)
    ax.fill_between(gens, delta_p[:, 2] - delta_std[:, 2], delta_p[:, 2] + delta_std[:, 2], color=COLOR_MAP['diversify'], alpha=0.15)

    ax.set_xlabel("Thế hệ tiến hóa (Generations)", fontweight='bold')
    ax.set_ylabel("Độ lệch ưu tiên toán tử ΔP so với mức ngẫu nhiên (%)", fontweight='bold')
    ax.set_title(f"Mức độ ưu tiên tương đối của toán tử di truyền EVO-RL (ΔP%)\nĐồ thị: {graph_name} | Công thức: ΔP = (P(a|s) - 1/3) × 100%", fontweight='bold', pad=12)

    max_dev = max(0.8, float(np.max(np.abs(delta_p) + delta_std)) * 1.25)
    ax.set_ylim(-max_dev, max_dev)
    ax.grid(True, linestyle='--', alpha=0.5)
    ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.16), ncol=4, frameon=True, facecolor='white', framealpha=0.95, edgecolor='#cccccc')

    out_base = os.path.join(out_dir, "3_action_relative_preference")
    save_chart_both_formats(fig, out_base)


def draw_stacked_area_chart(ppo_raw_seeds: List[Dict[str, Any]], out_dir: str, graph_name: str):
    """
    Biểu đồ 4: Biểu đồ miền chồng 100% (Stacked Area Chart / Market Share).
    Thể hiện tỷ trọng phân bổ tích lũy chuẩn hóa của từng toán tử qua các thế hệ.
    """
    if not ppo_raw_seeds:
        return

    all_probs = [s['action_probs'] for s in ppo_raw_seeds if len(s.get('action_probs', [])) > 0]
    if not all_probs:
        return

    min_len = min(len(p) for p in all_probs)
    probs_matrix = np.array([p[:min_len] for p in all_probs])
    mean_probs = np.mean(probs_matrix, axis=0)

    # Chuẩn hóa tổng = 1.0
    norm_probs = mean_probs / np.sum(mean_probs, axis=-1, keepdims=True)
    gens = np.arange(1, min_len + 1)

    p0 = norm_probs[:, 0]
    p1 = norm_probs[:, 1]
    p2 = norm_probs[:, 2]

    fig, ax = plt.subplots(figsize=(9.2, 5.2), dpi=600)
    ax.stackplot(
        gens, p0, p1, p2,
        labels=[
            "Structural Crossover ($a^{cross}$)",
            "Feasibility Repair ($a^{repair}$)",
            "Diversification Mutation ($a^{div}$)"
        ],
        colors=[COLOR_MAP['crossover'], COLOR_MAP['repair'], COLOR_MAP['diversify']],
        alpha=0.85
    )

    ax.set_xlabel("Thế hệ tiến hóa (Generations)", fontweight='bold')
    ax.set_ylabel("Tỷ trọng phân bổ toán tử tích lũy (100%)", fontweight='bold')
    ax.set_title(f"Tỷ trọng phân bổ toán tử thích nghi PPO-AOS theo thời gian (100% Stacked)\nĐồ thị: {graph_name} | Dữ liệu trung bình 20 Seeds độc lập", fontweight='bold', pad=12)
    ax.set_ylim(0, 1.0)
    ax.set_xlim(1, min_len)
    ax.grid(True, linestyle=':', alpha=0.4, color='white')
    ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.16), ncol=3, frameon=True, facecolor='white', framealpha=0.95, edgecolor='#cccccc')

    out_base = os.path.join(out_dir, "4_action_stacked_area")
    save_chart_both_formats(fig, out_base)


def draw_dual_action_convergence_chart(ppo_raw_seeds: List[Dict[str, Any]], out_dir: str, graph_name: str):
    """
    Biểu đồ 5: Biểu đồ kép đồng bộ thời gian (Dual Subplot).
    Tầng 1: Đường cong hội tụ Best Cover size (|C|_min).
    Tầng 2: Động thái xác suất toán tử tương ứng của chính lượt chạy đó.
    """
    if not ppo_raw_seeds:
        return

    best_seed_item = min(ppo_raw_seeds, key=lambda s: (s.get('best_cover', 99999), s.get('best_fitness', 99999)))
    action_probs = np.array(best_seed_item.get('action_probs', []))
    conv_curve = np.array(best_seed_item.get('convergence_curve', []))

    if len(action_probs) == 0 or len(conv_curve) == 0:
        return

    n_steps = min(len(action_probs), len(conv_curve))
    action_probs = action_probs[:n_steps]
    conv_curve = conv_curve[:n_steps]
    gens = np.arange(1, n_steps + 1)

    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(9.2, 7.6), dpi=600, sharex=True, gridspec_kw={'height_ratios': [1.2, 1]})

    seed_val = best_seed_item.get('seed', 'N/A')
    best_cov = best_seed_item.get('best_cover', 'N/A')

    # Tầng 1: Hội tụ nghiệm
    ax1.plot(gens, conv_curve, color='#e65100', linewidth=2.5, label='Kích thước Cover tốt nhất ($|C|_{min}$)',
             marker='o', markevery=max(1, n_steps // 12), markersize=5)
    ax1.set_ylabel("Cover Size ($s$-clubs)", fontweight='bold', color='#e65100')
    ax1.yaxis.set_major_locator(ticker.MaxNLocator(integer=True))
    ax1.set_title(f"Tương quan giữa Hội tụ nghiệm và Động thái toán tử PPO-AOS\nĐồ thị: {graph_name} (Best Seed = {seed_val}, Nghiệm tốt nhất = {best_cov})", fontweight='bold', pad=10)
    ax1.grid(True, linestyle='--', alpha=0.5)
    ax1.legend(loc='upper right', frameon=True, facecolor='white', framealpha=0.9, edgecolor='#cccccc')

    # Tầng 2: Xác suất toán tử
    ax2.plot(gens, action_probs[:, 0], label="Crossover ($a^{cross}$)", color=COLOR_MAP['crossover'], linewidth=2.2)
    ax2.plot(gens, action_probs[:, 1], label="Repair Mut ($a^{repair}$)", color=COLOR_MAP['repair'], linewidth=2.2)
    ax2.plot(gens, action_probs[:, 2], label="Diversify Mut ($a^{div}$)", color=COLOR_MAP['diversify'], linewidth=2.2)
    ax2.axhline(1/3, color='#555555', linestyle=':', linewidth=1.4, label='Mức ngẫu nhiên (1/3)')

    p_min, p_max = float(np.min(action_probs)), float(np.max(action_probs))
    span = max(0.005, p_max - p_min)
    margin = span * 0.25
    y_low = max(0.0, p_min - margin)
    y_high = min(1.0, p_max + margin)
    ax2.set_ylim(y_low, y_high)

    ax2.set_xlabel("Thế hệ tiến hóa (Generations)", fontweight='bold')
    ax2.set_ylabel("Xác suất P(a|s)", fontweight='bold')
    ax2.grid(True, linestyle='--', alpha=0.5)

    # Trục phụ Delta P % cho ax2
    ax2_twin = ax2.twinx()
    ax2_twin.set_ylim((y_low - 1/3) * 100, (y_high - 1/3) * 100)
    ax2_twin.set_ylabel("ΔP (%)", fontweight='bold', color='#555555')
    ax2_twin.grid(False)

    ax2.legend(loc='upper center', bbox_to_anchor=(0.5, -0.25), ncol=4, frameon=True, facecolor='white', framealpha=0.95, edgecolor='#cccccc')

    out_base = os.path.join(out_dir, "5_action_reward_convergence_dual")
    save_chart_both_formats(fig, out_base)


def draw_all_algorithms_convergence(raw_results: Dict[str, List[Dict[str, Any]]], out_dir: str, graph_name: str):
    """
    Biểu đồ 6: So sánh đường cong hội tụ của toàn bộ 8 thuật toán qua 20 seeds độc lập.
    Xử lý chuẩn tắc thuật toán dừng sớm (CCA, I-MSM): kéo dài đường nét đứt thể hiện nghiệm hội tụ,
    đặt Legend bên ngoài để không bao giờ đè khuất đường cong dữ liệu.
    """
    fig, ax = plt.subplots(figsize=(9.6, 5.6), dpi=600)
    has_data = False

    # Tìm max thế hệ lớn nhất trong tất cả thuật toán
    max_gens = 0
    for cond, seed_list in raw_results.items():
        for s in seed_list:
            c = s.get('convergence_curve', [])
            if len(c) > max_gens:
                max_gens = len(c)

    if max_gens == 0:
        plt.close(fig)
        return

    # Thứ tự vẽ ưu tiên
    priority_order = ['PPO-AOS', 'MAB-AOS', 'Greedy-AOS', 'Fixed', 'No-RL', 'Random', 'I-MSM', 'CCA']
    ordered_conds = [c for c in priority_order if c in raw_results] + [c for c in raw_results if c not in priority_order]

    for cond in ordered_conds:
        seed_list = raw_results[cond]
        curves = [s['convergence_curve'] for s in seed_list if len(s.get('convergence_curve', [])) > 0]
        if not curves:
            continue
        has_data = True

        lens = [len(c) for c in curves]
        active_len = min(lens)

        # Pad từng đường cong đến max_gens bằng giá trị cuối cùng (giá trị nghiệm tốt nhất tìm được)
        padded_curves = [np.pad(c, (0, max_gens - len(c)), mode='edge') for c in curves]
        mean_curve = np.mean(padded_curves, axis=0)
        std_curve = np.std(padded_curves, axis=0)
        gens_full = np.arange(1, max_gens + 1)

        color = COLOR_MAP.get(cond, '#333333')
        lw = 2.6 if cond == 'PPO-AOS' else 1.9
        alpha = 1.0 if cond == 'PPO-AOS' else 0.85

        # Nếu thuật toán dừng sớm đáng kể trước max_gens (như CCA, I-MSM dừng ở < 65% max_gens)
        if active_len < max_gens * 0.65:
            label_text = f"{cond} (Hội tụ tại gen {active_len})"
            # Đoạn tìm kiếm tích cực (Solid)
            ax.plot(gens_full[:active_len], mean_curve[:active_len], label=label_text, color=color, linewidth=lw, alpha=alpha)
            # Đoạn duy trì nghiệm tối ưu sau hội tụ (Dashed)
            ax.plot(gens_full[active_len-1:], mean_curve[active_len-1:], color=color, linestyle='--', linewidth=1.5, alpha=0.6)
            # Điểm chốt hội tụ
            ax.plot(active_len, mean_curve[active_len - 1], marker='o', markersize=5.5, color=color, markeredgecolor='black', markeredgewidth=0.8)
        else:
            ax.plot(gens_full, mean_curve, label=cond, color=color, linewidth=lw, alpha=alpha)
            if cond == 'PPO-AOS':
                ax.fill_between(gens_full, mean_curve - std_curve * 0.5, mean_curve + std_curve * 0.5, color=color, alpha=0.12)

    if not has_data:
        plt.close(fig)
        return

    ax.set_xlabel("Thế hệ tiến hóa / Vòng lặp (Generations)", fontweight='bold')
    ax.set_ylabel("Kích thước Cover trung bình (|C|)", fontweight='bold')
    ax.yaxis.set_major_locator(ticker.MaxNLocator(integer=True))
    ax.set_title(f"So sánh tốc độ hội tụ 8 thuật toán (Trung bình 20 Seeds độc lập)\nĐồ thị: {graph_name} | Nhỏ hơn là tốt hơn (Minimization)", fontweight='bold', pad=12)
    ax.grid(True, linestyle='--', alpha=0.5)

    # Đặt Legend ở dưới đáy với 4 cột rõ ràng, không bao giờ che khuất đường dữ liệu
    ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.16), ncol=4, frameon=True, facecolor='white', framealpha=0.95, edgecolor='#cccccc')

    out_base = os.path.join(out_dir, "6_convergence_curve_all_algorithms")
    save_chart_both_formats(fig, out_base)


def draw_metric_distribution_boxplot(raw_results: Dict[str, List[Dict[str, Any]]], out_dir: str, graph_name: str):
    """
    Biểu đồ 7: Boxplot phân bố chất lượng nghiệm (Cover Size) qua 20 Seeds độc lập.
    Xử lý khoa học hiện tượng bão hòa nghiệm (Floor effect): hiển thị nhãn trục số nguyên chuẩn,
    bổ sung huy hiệu thông báo khi tất cả thuật toán đều chạm cận dưới tối ưu.
    """
    conditions = [c for c in raw_results.keys() if len(raw_results[c]) > 0]
    if not conditions:
        return

    priority_order = ['PPO-AOS', 'MAB-AOS', 'Greedy-AOS', 'Fixed', 'No-RL', 'Random', 'I-MSM', 'CCA']
    ordered_conds = [c for c in priority_order if c in conditions] + [c for c in conditions if c not in priority_order]

    data = []
    for c in ordered_conds:
        covers = [s.get('best_cover', s.get('best_fitness', 0)) for s in raw_results[c]]
        data.append(covers)

    fig, ax = plt.subplots(figsize=(10.2, 5.4), dpi=600)

    box = ax.boxplot(
        data,
        patch_artist=True,
        tick_labels=ordered_conds,
        showmeans=True,
        meanprops={"marker": "D", "markerfacecolor": "yellow", "markeredgecolor": "black", "markersize": 6.5},
        medianprops={"color": "darkorange", "linewidth": 2.0},
        whiskerprops={"linewidth": 1.4},
        capprops={"linewidth": 1.4}
    )

    for patch, cond in zip(box['boxes'], ordered_conds):
        patch.set_facecolor(COLOR_MAP.get(cond, '#7f7f7f'))
        patch.set_alpha(0.65)
        patch.set_edgecolor('black')

    # Vẽ thêm các điểm scatter dữ liệu thực tế (Jitter points) để minh bạch dữ liệu
    for i, c_data in enumerate(data, start=1):
        jitter = np.random.normal(0, 0.04, size=len(c_data))
        ax.scatter(i + jitter, c_data, alpha=0.35, color='black', s=16, zorder=3)

    ax.set_ylabel("Kích thước Cover tối thiểu tìm được (|C|)", fontweight='bold')
    ax.set_title(f"Phân bố chất lượng nghiệm qua 20 Seeds độc lập (Boxplot + Dữ liệu hạt nhân)\nĐồ thị: {graph_name} | Hình thoi vàng = Giá trị trung bình (Mean)", fontweight='bold', pad=12)
    ax.tick_params(axis='x', rotation=18)
    ax.grid(True, linestyle='--', alpha=0.5, axis='y')
    ax.yaxis.set_major_locator(ticker.MaxNLocator(integer=True))

    # Kiểm tra nếu đồ thị bão hòa nghiệm tối ưu phẳng tuyệt đối (tất cả giá trị bằng nhau)
    flat_values = set()
    for row in data:
        flat_values.update(row)

    if len(flat_values) == 1:
        val = list(flat_values)[0]
        ax.set_ylim(val - 1.0, val + 1.0)
        ax.text(0.5, 0.85, f"BÃO HÒA NGHIỆM TỐI ƯU:\nTất cả 8 thuật toán đều đạt nghiệm tối ưu |C| = {int(val)} qua 20/20 Seeds",
                transform=ax.transAxes, ha='center', va='center',
                bbox=dict(boxstyle='round,pad=0.6', facecolor='#e8f5e9', edgecolor='#4caf50', linewidth=1.5),
                fontsize=10.5, fontweight='bold', color='#1b5e20')

    out_base = os.path.join(out_dir, "7_metric_distribution_boxplot")
    save_chart_both_formats(fig, out_base)


# ==============================================================================
# HÀM QUÉT DỮ LIỆU VÀ TỰ ĐỘNG SINH BIỂU ĐỒ VÀO THƯ MỤC Chart_seed
# ==============================================================================

def process_results_folder(results_base_dir: str, target_graph: Optional[str] = None):
    """
    Quét toàn bộ thư mục kết quả và kết xuất toàn bộ biểu đồ vào thư mục Chart_seed.
    Hỗ trợ lọc vẽ riêng đồ thị được chỉ định (target_graph) để kết xuất nhanh.
    """
    print("=" * 75, flush=True)
    print(f"🚀 EVO-RL Enhanced Chart Generator (600 DPI + Vector PDF)", flush=True)
    print(f"📂 Scanning Directory: {results_base_dir}", flush=True)
    if target_graph:
        print(f"🎯 Target Graph Filter: '{target_graph}'", flush=True)
    print("=" * 75, flush=True)

    if not os.path.exists(results_base_dir):
        print(f"[!] Thư mục {results_base_dir} không tồn tại!", flush=True)
        return

    summary_json_files = glob.glob(os.path.join(results_base_dir, "**", "Tong_20_lan_seed.json"), recursive=True)
    seed1_files = glob.glob(os.path.join(results_base_dir, "**", "results_seed_1.json"), recursive=True)
    all_target_dirs = set()

    for f in summary_json_files:
        all_target_dirs.add(os.path.dirname(os.path.abspath(f)))
    for f in seed1_files:
        all_target_dirs.add(os.path.dirname(os.path.abspath(f)))

    if target_graph:
        all_target_dirs = {d for d in all_target_dirs if os.path.basename(d).lower() == target_graph.lower()}

    if not all_target_dirs:
        msg = f"[-] Không tìm thấy dữ liệu kết quả nào"
        if target_graph:
            msg += f" cho đồ thị '{target_graph}'."
        else:
            msg += " trong thư mục results/."
        print(msg, flush=True)
        return

    print(f"[*] Tìm thấy {len(all_target_dirs)} thư mục dữ liệu đồ thị cần kết xuất biểu đồ.\n", flush=True)

    count_success = 0
    for graph_dir in sorted(all_target_dirs):
        graph_name = os.path.basename(graph_dir)
        parent_name = os.path.basename(os.path.dirname(graph_dir))
        print(f"📊 Đang xử lý: [{parent_name}] -> {graph_name}...", flush=True)

        raw_results = {}

        # 1. Nạp từ Tong_20_lan_seed.json
        summary_path = os.path.join(graph_dir, "Tong_20_lan_seed.json")
        if os.path.exists(summary_path):
            try:
                with open(summary_path, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    raw_results = data.get('raw_results', {})
            except Exception as e:
                print(f"   [!] Lỗi đọc {summary_path}: {e}", flush=True)

        # 2. Dự phòng: nạp từ results_seed_*.json nếu Tong_20_lan_seed.json rỗng
        has_runs = any(len(v) > 0 for v in raw_results.values()) if raw_results else False
        if not has_runs:
            raw_results = {}
            seed_files = sorted(glob.glob(os.path.join(graph_dir, "results_seed_*.json")))
            for sf in seed_files:
                try:
                    with open(sf, 'r', encoding='utf-8') as f:
                        s_data = json.load(f)
                        s_conds = s_data.get('conditions', {})
                        for cond, val in s_conds.items():
                            if cond not in raw_results:
                                raw_results[cond] = []
                            raw_results[cond].append(val)
                except Exception:
                    pass

        has_runs = any(len(v) > 0 for v in raw_results.values()) if raw_results else False
        if not has_runs:
            print(f"   [-] Không đọc được dữ liệu raw_results cho {graph_name}, bỏ qua.", flush=True)
            continue

        chart_seed_dir = os.path.join(graph_dir, "Chart_seed")
        os.makedirs(chart_seed_dir, exist_ok=True)

        ppo_seeds = raw_results.get('PPO-AOS', []) or raw_results.get('AdaptiveEvolutionary', [])

        try:
            if ppo_seeds:
                draw_best_seed_action_chart(ppo_seeds, chart_seed_dir, graph_name)
                draw_amplified_probability_chart(ppo_seeds, chart_seed_dir, graph_name)
                draw_relative_preference_chart(ppo_seeds, chart_seed_dir, graph_name)
                draw_stacked_area_chart(ppo_seeds, chart_seed_dir, graph_name)
                draw_dual_action_convergence_chart(ppo_seeds, chart_seed_dir, graph_name)

            draw_all_algorithms_convergence(raw_results, chart_seed_dir, graph_name)
            draw_metric_distribution_boxplot(raw_results, chart_seed_dir, graph_name)

            # Đồng thời cập nhật luôn thư mục charts/ truyền thống nếu có
            legacy_charts_dir = os.path.join(graph_dir, "charts")
            if os.path.exists(legacy_charts_dir):
                draw_all_algorithms_convergence(raw_results, legacy_charts_dir, graph_name)
                draw_metric_distribution_boxplot(raw_results, legacy_charts_dir, graph_name)
                if ppo_seeds:
                    draw_best_seed_action_chart(ppo_seeds, legacy_charts_dir, graph_name)

            print(f"   [✓] Hoàn tất 7 biểu đồ (PNG 600 DPI + Vector PDF) tại: {chart_seed_dir}", flush=True)
            count_success += 1
        except Exception as e:
            print(f"   [!] Lỗi khi render biểu đồ cho {graph_name}: {e}", flush=True)
        finally:
            plt.close('all')

    print("\n" + "=" * 75, flush=True)
    print(f"🎉 HOÀN TẤT! Đã nâng cấp thành công biểu đồ sắc nét 600 DPI + PDF cho {count_success}/{len(all_target_dirs)} đồ thị.", flush=True)
    print("=" * 75, flush=True)


def scan_results_folders(base_results_dirs: List[str]) -> List[Dict[str, Any]]:
    """Quét và thu thập metadata các thư mục kết quả trong results/."""
    results_folders = []
    seen = set()

    for b_dir in base_results_dirs:
        if not os.path.isdir(b_dir):
            continue
        try:
            items = os.listdir(b_dir)
        except Exception:
            continue

        for item in items:
            p = os.path.abspath(os.path.join(b_dir, item))
            if not os.path.isdir(p) or p in seen:
                continue

            try:
                sub_items = [d for d in os.listdir(p) if os.path.isdir(os.path.join(p, d)) and d not in ('charts', 'Chart_seed')]
            except Exception:
                continue

            if not sub_items:
                continue

            valid_graphs = []
            for g in sub_items:
                gp = os.path.join(p, g)
                j = os.path.join(gp, "Tong_20_lan_seed.json")
                s = os.path.join(gp, "results_seed_1.json")
                if (os.path.exists(j) and os.path.getsize(j) > 3000) or os.path.exists(s):
                    valid_graphs.append(g)

            if valid_graphs or item.startswith("ketqua_"):
                seen.add(p)
                mtime = os.path.getmtime(p)
                d_str = datetime.fromtimestamp(mtime).strftime("%Y-%m-%d %H:%M")
                results_folders.append({
                    'name': item,
                    'path': p,
                    'mtime': mtime,
                    'date_str': d_str,
                    'graphs': sorted(valid_graphs),
                    'total_graphs': len(sub_items),
                    'has_netscience': 'netscience' in valid_graphs
                })

    results_folders.sort(key=lambda x: x['mtime'], reverse=True)
    return results_folders


def interactive_select_chart_target(base_dirs: List[str]) -> Tuple[Optional[str], Optional[str]]:
    """Menu tương tác chọn thư mục kết quả hoặc chọn đồ thị riêng lẻ."""
    while True:
        folders = scan_results_folders(base_dirs)

        print("\n" + "=" * 80)
        print("   EVO-RL CHART GENERATOR (CHART_SEED) - XUẤT BIỂU ĐỒ 600 DPI & VECTOR PDF")
        print("=" * 80)

        if not folders:
            print("  [!] Không tìm thấy thư mục kết quả nào trong results/.")
            print("  [R] Quét lại (Refresh)")
            print("  [C] Nhập đường dẫn thư mục tùy chỉnh")
            print("  [Q] Thoát")
            c = input(">> Nhập lựa chọn [R/C/Q]: ").strip().upper()
            if c == 'R':
                continue
            elif c == 'C':
                cp = input(">> Nhập đường dẫn thư mục: ").strip(' "\'')
                if os.path.isdir(cp):
                    return cp, None
                continue
            else:
                sys.exit(0)

        for idx, f in enumerate(folders, 1):
            g_cnt = len(f['graphs'])
            recent_tag = " [MỚI NHẤT]" if idx == 1 else ""
            net_tag = " | Có netscience (20 seeds)" if f['has_netscience'] else ""
            print(f"  [{idx}] {f['name']}{recent_tag}")
            print(f"      * Thời gian: {f['date_str']} | Số đồ thị: {g_cnt}{net_tag}")
            if 0 < g_cnt <= 2:
                print(f"      * Danh sách: {', '.join(f['graphs'])}")

        print("-" * 80)
        print("  [A] QUÉT & VẼ TẤT CẢ (Render All) [Mặc định]:")
        print("      Tự động quét toàn bộ thư mục results/ và vẽ lại tất cả đồ thị.")
        print("  [N] VẼ RIÊNG ĐỒ THỊ MỚI 'netscience' [SIÊU NHANH]:")
        print("      Chỉ kết xuất 7 biểu đồ cho đồ thị netscience.")
        print("  [G] Chọn vẽ riêng một đồ thị cụ thể bất kỳ (Nhập tên đồ thị)")
        print("  [R] LÀM MỚI (Refresh / Quét lại)")
        print("  [C] Nhập đường dẫn thư mục kết quả tùy chỉnh")
        print("  [Q] Thoát")
        print("=" * 80)

        choice = input(">> Nhập lựa chọn [A / N / 1 / 2 ... / G / R / C / Q] (Mặc định: A): ").strip()
        ch_upper = choice.upper()

        if choice == "" or ch_upper == "A":
            return None, None
        elif ch_upper == "N":
            print("\n[*] Đã chọn chế độ vẽ nhanh riêng cho đồ thị: netscience")
            return None, "netscience"
        elif ch_upper == "G":
            g_name = input(">> Nhập tên đồ thị muốn vẽ (VD: karate, netscience, jazz): ").strip()
            if g_name:
                return None, g_name
            continue
        elif ch_upper == "R":
            print("\n[*] Đang quét lại toàn bộ thư mục results/...")
            time.sleep(0.5)
            continue
        elif ch_upper == "C":
            cp = input(">> Nhập đường dẫn thư mục kết quả: ").strip(' "\'')
            if os.path.isdir(cp):
                return cp, None
            print(f"[!] Thư mục không tồn tại: {cp}")
            continue
        elif ch_upper == "Q":
            sys.exit(0)
        elif choice.isdigit():
            idx = int(choice)
            if 1 <= idx <= len(folders):
                sel = folders[idx - 1]
                print(f"\n[*] Đã chọn thư mục: {sel['name']}")
                return sel['path'], None
            else:
                print(f"[!] Lựa chọn không hợp lệ. Vui lòng chọn từ 1 đến {len(folders)}.")
                continue
        else:
            print("[!] Lựa chọn không hợp lệ. Vui lòng thử lại.")
            continue


def main():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.abspath(os.path.join(current_dir, ".."))
    results_dir = os.path.join(project_root, "results")
    candidate_results_dirs = [
        results_dir,
        os.path.abspath(os.path.join(project_root, "..", "results"))
    ]

    parser = argparse.ArgumentParser(description="EVO-RL Xuất Biểu Đồ Chuẩn Báo Cáo Khoa Học (600 DPI & Vector PDF)")
    parser.add_argument("--results_dir", "-r", type=str, default=None, help="Thư mục kết quả cần vẽ biểu đồ")
    parser.add_argument("--graph", "-g", type=str, default=None, help="Tên đồ thị cần vẽ riêng (VD: netscience)")
    parser.add_argument("--all", "-a", action="store_true", help="Tự động vẽ tất cả mà không hỏi menu")
    parser.add_argument("--auto", action="store_true", help="Chế độ auto không dùng menu console")
    parser.add_argument("--batch", "-b", action="store_true", help="Chế độ batch script")
    args = parser.parse_args()

    target_dir = args.results_dir
    target_graph = args.graph

    if not target_dir and not target_graph and not args.all and not args.auto and not args.batch and sys.stdin.isatty():
        target_dir, target_graph = interactive_select_chart_target(candidate_results_dirs)

    if not target_dir:
        target_dir = results_dir

    process_results_folder(target_dir, target_graph=target_graph)


if __name__ == "__main__":
    main()
