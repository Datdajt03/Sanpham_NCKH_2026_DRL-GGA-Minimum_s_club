"""
Bai_2_DeepRL_AOS_Suitability/config_bai2.py — Cấu hình và siêu tham số cho Bài báo 2.
Trọng tâm: Đánh giá đa chiều hiệu năng, độ ổn định, tốc độ hội tụ và động học chính sách DRL-AOS.
"""
import os
import torch
from dataclasses import dataclass, field
from typing import List


@dataclass
class Bai2Config:
    # 1. Cấu hình bài toán đồ thị
    s_club_threshold: int = 2        # Chuẩn s = 2
    penalty_lambda: float = 0.0      # Sẽ tự động gán = n_nodes + 1 nếu = 0.0

    # 2. Cấu hình giải thuật tiến hóa nhóm (GGA)
    pop_size: int = 100              # Kích thước quần thể
    offspring_size: int = 20         # Số lượng cá thể con mỗi thế hệ
    tournament_size: int = 2         # Binary tournament
    crossover_rate: float = 1.0      # Tỷ lệ lai ghép
    mutation_rate_repair: float = 0.05  # Tỷ lệ đột biến sửa (5% đỉnh)
    mutation_rate_div: float = 0.20     # Tỷ lệ đột biến đa dạng (20% đỉnh)
    max_generations: int = 200       # Số thế hệ tối đa (T)
    stagnation_limit: int = 100      # Giới hạn đình trệ (L)
    elitism_count: int = 2           # Số lượng cá thể tinh hoa giữ lại

    # 3. Cấu hình PPO-AOS Controller
    state_dim: int = 5               # [f_min_norm, f_avg_norm, rho_feas, phi_bar_norm, tau_norm]
    num_operators: int = 3           # [0: a^cross, 1: a^repair, 2: a^div]
    hidden_dim: int = 256            # 2 lớp ẩn 256-256
    learning_rate: float = 0.0003    # Tốc độ học Adam
    discount: float = 0.99           # Gamma
    clip_eps: float = 0.2            # Epsilon clip
    entropy_coef: float = 0.01       # Hệ số entropy
    value_coef: float = 0.5          # Trọng số Critic loss
    grad_clip: float = 1.0           # Gradient clipping
    batch_size: int = 32             # Mini-batch
    ppo_epochs: int = 4              # Epochs per update
    update_interval: int = 20        # Cập nhật online mỗi K thế hệ

    # 4. Trọng số hàm phần thưởng Feasibility-Aware
    alpha1: float = 10.0             # Thưởng cải thiện f_min
    alpha2: float = 5.0              # Thưởng tăng tỷ lệ khả thi
    alpha3: float = 5.0              # Phạt tăng mức vi phạm trung bình
    alpha4: float = 1.0              # Phạt đình trệ

    # 5. Cấu hình thực nghiệm & output
    num_seeds: int = 20              # 20 independent paired seeds
    num_workers: int = 10            # Số luồng song song (10 workers)
    conditions: List[str] = field(default_factory=lambda: [
        "PPO-AOS", "MAB-AOS", "Greedy-AOS", "No-RL", "Fixed", "Random", "I-MSM", "CCA"
    ])
    device: str = "cuda" if torch.cuda.is_available() else "cpu"
    output_dir: str = os.path.join(os.path.dirname(__file__), "results_bai2")
