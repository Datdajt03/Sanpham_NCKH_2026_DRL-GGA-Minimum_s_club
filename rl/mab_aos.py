"""
rl/mab_aos.py — Cài đặt Multi-Armed Bandit Adaptive Operator Selection (MAB-AOS / UCB1-AOS).

Định vị khoa học:
  Baseline đối chứng quan trọng bậc nhất của bài báo:
  "PPO (Deep RL có trạng thái) có thực sự vượt trội hơn cơ chế Multi-Armed Bandit (AOS phi trạng thái) kinh điển hay không?"

Cơ chế hoạt động (Chuẩn UCB1 theo Fialho et al., IEEE TEVC / GECCO):
  1. K cánh tay (Arms) tương ứng với K toán tử tiến hóa (K=3: Crossover, Feasible Mut, Diversify Mut).
  2. Mỗi cánh tay a duy trì:
       - N(a): Số lần toán tử a đã được chọn.
       - W(a): Tổng phần thưởng tích lũy thu được từ toán tử a.
       - X_bar(a) = W(a) / N(a): Phần thưởng trung bình.
  3. Ở các thế hệ đầu (t < K): Thử tuần tự từng toán tử 1 lần để có dữ liệu ban đầu.
  4. Ở các thế hệ tiếp theo (t >= K): Chọn toán tử tối đa hóa điểm UCB1:
       a_t = argmax_a [ X_norm(a) + c * sqrt( (2 * ln(t)) / N(a) ) ]
       trong đó c là hằng số cân bằng giữa Khai thác (Exploitation) và Thăm dò (Exploration), mặc định c = sqrt(2) ~ 1.414.
  5. Tự động chuẩn hóa Reward về miền [0, 1] qua min-max động để đảm bảo giá trị UCB1 có ý nghĩa toán học chính xác.
"""
import numpy as np
from typing import Dict, Any, Optional
from configs.config import ExperimentConfig


class MABAOSAgent:
    """
    MAB-AOS (UCB1) Agent: Tác tử Multi-Armed Bandit chọn toán tử thích nghi.
    """
    def __init__(self, config: ExperimentConfig, c: float = 1.414):
        """
        Args:
            config: Cấu hình thực nghiệm.
            c: Hằng số thăm dò UCB (Exploration constant, mặc định sqrt(2)).
        """
        self.config = config
        self.num_operators = config.num_operators
        self.c = c
        
        self.counts = np.zeros(self.num_operators, dtype=np.int32)
        self.total_rewards = np.zeros(self.num_operators, dtype=np.float32)
        self.total_steps: int = 0
        
        # Biên động min/max reward để chuẩn hóa về [0, 1]
        self.min_reward: float = 0.0
        self.max_reward: float = 1.0
        
        self.last_action: Optional[int] = None

    def select_action(self, state: np.ndarray, train: bool = True) -> int:
        """
        Lựa chọn toán tử theo công thức UCB1:
          - Nếu còn toán tử chưa được kích hoạt: Chọn toán tử đó trước.
          - Ngược lại: Chọn a* = argmax [ X_bar(a) + c * sqrt(2 * ln(t) / N(a)) ].
        """
        # 1. Giai đoạn khởi động: Thử mỗi toán tử ít nhất 1 lần
        for op in range(self.num_operators):
            if self.counts[op] == 0:
                self.last_action = op
                return op

        if not train:
            # Khi đánh giá, chọn toán tử có trung bình reward cao nhất
            means = self.total_rewards / np.maximum(self.counts, 1)
            action = int(np.argmax(means))
            self.last_action = action
            return action

        # 2. Tính toán điểm UCB1 chuẩn
        t = max(1, self.total_steps)
        ucb_values = np.zeros(self.num_operators, dtype=np.float32)
        
        r_range = max(1e-5, self.max_reward - self.min_reward)

        for op in range(self.num_operators):
            mean_r = self.total_rewards[op] / self.counts[op]
            norm_mean = (mean_r - self.min_reward) / r_range
            norm_mean = np.clip(norm_mean, 0.0, 1.0)
            
            exploration_bonus = self.c * np.sqrt((2.0 * np.log(t)) / self.counts[op])
            ucb_values[op] = norm_mean + exploration_bonus

        max_ucb = np.max(ucb_values)
        best_ops = np.where(ucb_values == max_ucb)[0]
        action = int(np.random.choice(best_ops))

        self.last_action = action
        return action

    def get_action_probs(self, state: np.ndarray) -> np.ndarray:
        """
        Trả về phân phối xác suất đại diện cho mức độ ưu tiên của từng toán tử
        (Softmax trên điểm UCB1 hoặc tần suất chọn để phục vụ trực quan hóa biểu đồ).
        """
        if self.total_steps == 0 or np.any(self.counts == 0):
            return np.full(self.num_operators, 1.0 / self.num_operators, dtype=np.float32)

        t = max(1, self.total_steps)
        ucb_values = np.zeros(self.num_operators, dtype=np.float32)
        r_range = max(1e-5, self.max_reward - self.min_reward)

        for op in range(self.num_operators):
            mean_r = self.total_rewards[op] / max(1, self.counts[op])
            norm_mean = (mean_r - self.min_reward) / r_range
            bonus = self.c * np.sqrt((2.0 * np.log(t)) / max(1, self.counts[op]))
            ucb_values[op] = norm_mean + bonus

        shifted = ucb_values - np.max(ucb_values)
        exp_u = np.exp(np.clip(shifted, -20.0, 20.0))
        sum_exp = np.sum(exp_u)
        if sum_exp > 0:
            return (exp_u / sum_exp).astype(np.float32)
        return np.full(self.num_operators, 1.0 / self.num_operators, dtype=np.float32)

    def store_transition(self, state: np.ndarray, action: int, reward: float, done: bool):
        """
        Cập nhật thống kê của cánh tay (Arm) vừa được chọn.
        """
        if action is not None and 0 <= action < self.num_operators:
            self.counts[action] += 1
            self.total_rewards[action] += float(reward)
            self.total_steps += 1
            
            # Cập nhật biên min/max reward trực tuyến
            self.min_reward = min(self.min_reward, float(reward))
            self.max_reward = max(self.max_reward, float(reward))

    def update(self, next_state: np.ndarray) -> Optional[Dict[str, float]]:
        """MAB-AOS cập nhật trực tiếp theo thống kê giải tích, không cần SGD."""
        return None
