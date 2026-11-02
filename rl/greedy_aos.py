"""
rl/greedy_aos.py — Cài đặt Greedy Adaptive Operator Selection (Greedy-AOS).

Định vị khoa học:
  Baseline trả lời câu hỏi phản biện quan trọng:
  "Tại sao cần PPO (Deep RL)? Liệu chỉ cần chọn toán tử có hiệu năng / phần thưởng cao nhất gần đây là đủ?"

Cơ chế hoạt động:
  1. Duy trì ước lượng giá trị phần thưởng Q_hat(a) cho từng toán tử a in {0: Crossover, 1: Feasible Mut, 2: Diversify Mut}.
  2. Cập nhật Q_hat(a) qua Exponential Moving Average (EMA) dựa trên reward thực tế từ môi trường:
       Q_hat(a) <- (1 - alpha) * Q_hat(a) + alpha * reward
  3. Lựa chọn toán tử theo chiến lược epsilon-Greedy:
       - Với xác suất 1 - epsilon: chọn a* = argmax_a Q_hat(a) (Khai thác tối đa toán tử tốt nhất).
       - Với xác suất epsilon (mặc định 0.05 - 0.1): chọn ngẫu nhiên đều để tránh hiện tượng bỏ đói toán tử (starvation).
"""
import numpy as np
from typing import Dict, Any, Optional
from configs.config import ExperimentConfig


class GreedyAOSAgent:
    """
    Greedy-AOS Agent: Lựa chọn toán tử có reward / cải thiện tốt nhất gần nhất.
    """
    def __init__(self, config: ExperimentConfig, alpha: float = 0.3, epsilon: float = 0.1):
        """
        Args:
            config: Cấu hình thực nghiệm.
            alpha: Tốc độ cập nhật EMA (0 < alpha <= 1).
            epsilon: Xác suất thăm dò ngẫu nhiên để tránh nghẽn.
        """
        self.config = config
        self.num_operators = config.num_operators
        self.alpha = alpha
        self.epsilon = epsilon
        
        # Khởi tạo giá trị ước lượng ban đầu bằng nhau (Optimistic Initialization)
        self.q_values = np.ones(self.num_operators, dtype=np.float32) * 1.0
        self.selection_counts = np.zeros(self.num_operators, dtype=np.int32)
        
        self.last_action: Optional[int] = None

    def select_action(self, state: np.ndarray, train: bool = True) -> int:
        """
        Lựa chọn toán tử:
          - Nếu train=True: Áp dụng epsilon-greedy (argmax Q_hat với xác suất 1-eps).
          - Nếu train=False: Chọn thuần túy argmax Q_hat.
        """
        if train and np.random.rand() < self.epsilon:
            action = int(np.random.choice(self.num_operators))
        else:
            # Chọn toán tử có Q-value cao nhất (nếu bằng nhau thì chọn ngẫu nhiên giữa các max)
            max_val = np.max(self.q_values)
            best_actions = np.where(self.q_values == max_val)[0]
            action = int(np.random.choice(best_actions))

        self.last_action = action
        self.selection_counts[action] += 1
        return action

    def get_action_probs(self, state: np.ndarray) -> np.ndarray:
        """
        Trả về phân phối xác suất chọn toán tử [p_0, p_1, p_2]
        dựa trên giá trị Q hiện tại (Softmax phân bổ để phục vụ vẽ biểu đồ và phân tích).
        """
        # Softmax với nhiệt độ T=1.0 để trực quan hóa mức độ ưu tiên
        shifted = self.q_values - np.max(self.q_values)
        exp_q = np.exp(np.clip(shifted, -20.0, 20.0))
        sum_exp = np.sum(exp_q)
        if sum_exp > 0:
            return (exp_q / sum_exp).astype(np.float32)
        return np.full(self.num_operators, 1.0 / self.num_operators, dtype=np.float32)

    def store_transition(self, state: np.ndarray, action: int, reward: float, done: bool):
        """
        Cập nhật ước lượng Q-value của toán tử vừa thực thi theo EMA:
          Q_hat(a) <- (1 - alpha) * Q_hat(a) + alpha * reward
        """
        if action is not None and 0 <= action < self.num_operators:
            self.q_values[action] = (1.0 - self.alpha) * self.q_values[action] + self.alpha * float(reward)

    def update(self, next_state: np.ndarray) -> Optional[Dict[str, float]]:
        """Greedy-AOS là thuật toán phi tham số trực tiếp, không cần huấn luyện mạng nơ-ron."""
        return None
