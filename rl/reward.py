"""
rl/reward.py — Tính toán hàm phần thưởng đa thành phần (Dense Multi-component Reward).
Định hướng tác tử tối ưu hóa số lượng club đồng thời bảo toàn tính khả thi của s-club.
"""
import numpy as np


def compute_reward(
    prev_best_f: float,
    curr_best_f: float,
    prev_feas_ratio: float,
    curr_feas_ratio: float,
    prev_violation: float,
    curr_violation: float,
    stagnated: bool,
    alpha1: float = 10.0,
    alpha2: float = 5.0,
    alpha3: float = 5.0,
    alpha4: float = 1.0
) -> float:
    """
    Hàm tính phần thưởng định hướng thông minh:
      1. +α1 : Nếu nghiệm tốt nhất được cải thiện (Best fitness giảm).
      2. +Bonus : Nếu đạt nghiệm tối ưu tuyệt đối (Cover = 1).
      3. +α2 : Nếu tỷ lệ nghiệm khả thi tăng lên.
      4. -α3 : Nếu mức độ vi phạm đường kính tăng lên.
      5. -Penalty : Nếu phá vỡ cấu trúc khả thi làm tăng số nhóm vô ích.
      6. -α4 : Nếu bị trì trệ không có cải thiện.
    """
    reward = 0.0

    # 1. Cải thiện Best Fitness
    if curr_best_f < prev_best_f:
        delta_f = (prev_best_f - curr_best_f) / max(1.0, prev_best_f)
        reward += alpha1 * (1.0 + delta_f)
        if curr_best_f <= 1.0:
            reward += 15.0  # Thưởng lớn khi chạm đáy tối ưu tuyệt đối
    
    # 2. Cải thiện Feasible Ratio (Tỷ lệ khả thi)
    elif curr_feas_ratio > prev_feas_ratio:
        delta_rho = curr_feas_ratio - prev_feas_ratio
        reward += alpha2 * delta_rho

    # 3. Phạt nếu làm tăng vi phạm đường kính
    if curr_violation > prev_violation:
        delta_v = (curr_violation - prev_violation) / max(1.0, prev_violation)
        reward -= alpha3 * delta_v

    # 4. Phạt nếu quần thể đã 100% khả thi mà làm tăng số lượng nhóm
    if prev_feas_ratio >= 0.99 and curr_best_f > prev_best_f:
        reward -= 2.5

    # 5. Phạt khi bị trì trệ (stagnation)
    if stagnated:
        reward -= alpha4

    return float(reward)
