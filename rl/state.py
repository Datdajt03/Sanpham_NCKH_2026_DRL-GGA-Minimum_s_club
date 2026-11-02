"""
rl/state.py — Trích xuất và chuẩn hóa vector trạng thái (State Vector 5 chiều).
"""
import numpy as np
from problem.population import Population


def extract_state(
    population: Population, 
    stagnation_count: int, 
    stagnation_limit: int, 
    n_nodes: int, 
    s: int
) -> np.ndarray:
    """
    Trích xuất vector trạng thái 5 chiều chuẩn hóa:
      z_t = [f_min_norm, f_avg_norm, rho_feas, phi_bar_norm, tau_norm]
      
    1. f_min_norm  : Fitness tốt nhất chuẩn hóa trên số đỉnh [0, 1]
    2. f_avg_norm  : Fitness trung bình chuẩn hóa [0, 1]
    3. rho_feas    : Tỷ lệ nghiệm khả thi [0, 1]
    4. phi_bar_norm: Độ vi phạm đường kính trung bình chuẩn hóa [0, 1]
    5. tau_norm    : Số bước trì trệ chuẩn hóa theo giới hạn dừng sớm [0, 1]
    """
    f_min = population.best_fitness
    f_avg = population.avg_fitness
    rho_feas = population.feasible_ratio
    phi_bar = population.mean_violation

    # Chuẩn hóa về [0, 1]
    f_min_norm = float(np.clip(f_min / max(1, n_nodes), 0.0, 1.0))
    f_avg_norm = float(np.clip(f_avg / max(1, n_nodes), 0.0, 1.0))
    rho_feas_norm = float(np.clip(rho_feas, 0.0, 1.0))
    phi_bar_norm = float(np.clip(phi_bar / max(1, s + 1), 0.0, 1.0))
    tau_norm = float(np.clip(stagnation_count / max(1, stagnation_limit), 0.0, 1.0))

    state = np.array([f_min_norm, f_avg_norm, rho_feas_norm, phi_bar_norm, tau_norm], dtype=np.float32)
    return state


class StateNormalizer:
    """Bộ chuẩn hóa thích nghi trực tuyến (Online Running Normalizer) sử dụng thuật toán Welford."""
    def __init__(self, state_dim: int = 5):
        self.state_dim = state_dim
        self.mean = np.zeros(state_dim, dtype=np.float32)
        self.var = np.ones(state_dim, dtype=np.float32)
        self.count = 0

    def update(self, state: np.ndarray):
        self.count += 1
        delta = state - self.mean
        self.mean += delta / self.count
        delta2 = state - self.mean
        self.var += delta * delta2

    def normalize(self, state: np.ndarray) -> np.ndarray:
        if self.count < 2:
            return state
        std = np.sqrt(self.var / (self.count - 1)) + 1e-8
        return np.clip((state - self.mean) / std, -5.0, 5.0)
