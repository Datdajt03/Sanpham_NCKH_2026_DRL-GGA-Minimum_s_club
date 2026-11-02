"""
configs/config.py — Tập trung cấu hình và siêu tham số cho toàn bộ hệ thống EVO-RL.
Đồng bộ chính xác 100% theo Bảng 1 trong bài báo của Thầy và tự động nhận diện GPU.
"""
import os
from dataclasses import dataclass, field
from typing import List, Optional
import torch

# Danh sách 20 seeds cố định chuẩn từ seedun.md
DEFAULT_FIXED_SEEDS = [
    17032026, 21042026, 23052026, 26062026, 13092026,
    20260317, 20260421, 20260523, 20260626, 20260913,
    11223344, 12344321, 13572468, 24681357, 31415926,
    27182818, 52013140, 20252026, 64086408, 86088608
]


def load_seeds_from_file(seed_file_path: Optional[str] = None) -> List[int]:
    """
    Đọc danh sách seed cố định từ file seedun.md.
    Nếu không tìm thấy hoặc xảy ra lỗi, sẽ tự động dùng DEFAULT_FIXED_SEEDS.
    """
    if seed_file_path is None:
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        seed_file_path = os.path.join(base_dir, "seedun.md")

    if os.path.exists(seed_file_path):
        try:
            seeds = []
            with open(seed_file_path, "r", encoding="utf-8") as f:
                for line in f:
                    line = line.strip()
                    if not line or line.startswith("#"):
                        continue
                    # Trích xuất số nguyên từ dòng (hỗ trợ cả dòng số thuần túy hoặc dạng markdown '- 17032026')
                    digits = "".join(c for c in line if c.isdigit())
                    if digits:
                        seeds.append(int(digits))
            if seeds:
                return seeds
        except Exception as e:
            print(f"[!] Cảnh báo: Lỗi khi đọc file seed ({seed_file_path}): {e}. Dùng 20 seed mặc định.")

    return list(DEFAULT_FIXED_SEEDS)


def get_fixed_seeds(num_seeds: Optional[int] = None, seed_file_path: Optional[str] = None) -> List[int]:
    """Trả về đúng số lượng seeds cố định yêu cầu từ file seedun.md."""
    seeds = load_seeds_from_file(seed_file_path)
    if num_seeds is not None and num_seeds > 0:
        if num_seeds <= len(seeds):
            return seeds[:num_seeds]
        else:
            # Nếu yêu cầu nhiều hơn số seed hiện có, lặp lại tuần hoàn có bù trừ
            return seeds * (num_seeds // len(seeds)) + seeds[:(num_seeds % len(seeds))]
    return seeds


@dataclass
class ExperimentConfig:
    # 1. Cấu hình bài toán đồ thị
    s_club_threshold: int = 2        # Ngưỡng đường kính s-club (s >= 2)
    penalty_lambda: float = 10.0     # Hệ số hình phạt vi phạm đường kính / liên thông

    # 2. Cấu hình giải thuật tiến hóa (Evolutionary Algorithm / GGA - Chuẩn theo bài của Thầy)
    pop_size: int = 100              # Kích thước quần thể = 100 (khớp chính xác Bảng 1 của Thầy)
    offspring_size: int = 20         # Số lượng cá thể con sinh ra mỗi thế hệ
    tournament_size: int = 3         # Kích thước chọn lọc giải đấu
    mutation_rate: float = 0.05      # Tỉ lệ đột biến = 0.05 (khớp chính xác Bảng 1 của Thầy)
    crossover_rate: float = 0.9      # Tỉ lệ lai ghép = 0.9 (khớp chính xác Bảng 1 của Thầy)
    max_generations: int = 200       # Số thế hệ tối đa trong 1 episode (T)
    stagnation_limit: int = 100      # Số thế hệ không cải thiện tối đa để dừng sớm (L)

    # 3. Cấu hình PPO Controller (Reinforcement Learning)
    state_dim: int = 5               # Vector trạng thái 5 chiều [f_min, f_avg, rho_feas, phi_bar, tau]
    num_operators: int = 3           # 3 toán tử: [0: Crossover, 1: Feasible Mut, 2: Diversify Mut]
    hidden_dim: int = 64             # Số nơ-ron lớp ẩn MLP (nhẹ, nhanh)
    learning_rate: float = 0.0003    # Tốc độ học Adam
    discount: float = 0.99           # Hệ số chiết khấu gamma
    clip_eps: float = 0.2            # Hệ số clip epsilon của PPO
    entropy_coef: float = 0.01       # Trọng số khuyến khích entropy (thăm dò ổn định)
    value_coef: float = 0.5          # Trọng số hàm mất mát Value Critic
    grad_clip: float = 1.0           # Cắt ngắn gradient
    batch_size: int = 32             # Kích thước mini-batch cập nhật PPO
    ppo_epochs: int = 4              # Số lượt tối ưu hóa qua buffer
    max_epochs: int = 200            # Số episode huấn luyện tác tử

    # 4. Trọng số hàm phần thưởng (Reward Weights)
    alpha1: float = 10.0             # Thưởng khi giảm số lượng club (cải thiện best fitness)
    alpha2: float = 5.0              # Thưởng khi tăng tỷ lệ nghiệm khả thi (rho_feas)
    alpha3: float = 5.0              # Phạt khi tăng độ vi phạm đường kính
    alpha4: float = 1.0              # Phạt khi không có tiến bộ (stagnation)

    # 5. Cấu hình thực nghiệm & thống kê
    num_seeds: int = 20              # Số lượng hạt giống cố định (20 fixed seeds từ seedun.md)
    num_workers: int = 10           # Số lượng tiến trình chạy song song (mặc định 10 seeds cùng lúc)
    fixed_seeds: List[int] = field(default_factory=load_seeds_from_file)
    conditions: List[str] = field(default_factory=lambda: [
        "PPO-AOS", "MAB-AOS", "Greedy-AOS", "I-MSM", "CCA", "No-RL", "Fixed", "Random"
    ])
    # Tự động nhận diện GPU nếu có, ngược lại chạy CPU đa luồng
    device: str = "cuda" if torch.cuda.is_available() else "cpu"