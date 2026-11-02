"""
Bai_3_Cost_Benefit_Analysis/config_bai3.py — Cấu hình và siêu tham số cho Bài báo 3.
Trọng tâm: Đo lường chi phí tính toán (Overhead profiling), phân tích Pareto Quality vs Runtime và Break-even analysis.
"""
import os
import torch
from dataclasses import dataclass, field
from typing import List


@dataclass
class Bai3Config:
    # 1. Cấu hình bài toán đồ thị
    s_club_threshold: int = 2
    penalty_lambda: float = 0.0

    # 2. Cấu hình GA
    pop_size: int = 100
    offspring_size: int = 20
    tournament_size: int = 2
    max_generations: int = 200
    stagnation_limit: int = 100

    # 3. Cấu hình RL & Updates
    state_dim: int = 5
    num_operators: int = 3
    hidden_dim: int = 256
    learning_rate: float = 0.0003
    discount: float = 0.99
    clip_eps: float = 0.2
    batch_size: int = 32
    ppo_epochs: int = 4
    update_interval: int = 20

    # 4. Ngân sách thời gian cố định để đo Time-Normalized Performance (giây)
    time_budgets_sec: List[float] = field(default_factory=lambda: [0.5, 1.0, 2.0, 5.0, 10.0, 30.0, 60.0])

    # 5. Cấu hình thực nghiệm & output
    num_seeds: int = 20
    num_workers: int = 10            # Số luồng song song (10 workers)
    conditions: List[str] = field(default_factory=lambda: [
        "PPO-AOS", "MAB-AOS", "Greedy-AOS", "No-RL", "Fixed", "Random"
    ])
    device: str = "cuda" if torch.cuda.is_available() else "cpu"
    output_dir: str = os.path.join(os.path.dirname(__file__), "results_bai3")
