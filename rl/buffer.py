"""
rl/buffer.py — Bộ đệm Rollout Buffer lưu trữ quỹ đạo và tính toán GAE (Generalized Advantage Estimation).
Tuân thủ đầy đủ chuẩn kiến trúc Stable-Baselines3 và CleanRL.
"""
import torch
import numpy as np
from typing import Generator, Tuple


class PPOBuffer:
    """
    Lưu trữ các bước chuyển trạng thái (s_t, a_t, r_t, s_{t+1}, log_pi, V(s_t), done)
    và tính toán hàm Advantage ước lượng (GAE-Lambda).
    """
    def __init__(self, gamma: float = 0.99, gae_lambda: float = 0.95):
        self.gamma = gamma
        self.gae_lambda = gae_lambda
        
        self.states = []
        self.actions = []
        self.rewards = []
        self.log_probs = []
        self.values = []
        self.dones = []

    def store(self, state: np.ndarray, action: int, reward: float, log_prob: float, value: float, done: bool):
        self.states.append(state)
        self.actions.append(action)
        self.rewards.append(reward)
        self.log_probs.append(log_prob)
        self.values.append(value)
        self.dones.append(done)

    def size(self) -> int:
        return len(self.states)

    def clear(self):
        self.states.clear()
        self.actions.clear()
        self.rewards.clear()
        self.log_probs.clear()
        self.values.clear()
        self.dones.clear()

    def compute_returns_and_advantages(self, last_value: float = 0.0) -> Tuple[torch.Tensor, torch.Tensor, torch.Tensor, torch.Tensor, torch.Tensor, torch.Tensor]:
        r"""
        Tính toán Returns và Advantages bằng GAE-Lambda:
          A_t = \sum_{l=0}^{\infty} (\gamma \lambda)^l \delta_{t+l}^V
          \delta_t^V = r_t + \gamma V(s_{t+1}) (1 - d_t) - V(s_t)
        """
        n_steps = len(self.rewards)
        advantages = np.zeros(n_steps, dtype=np.float32)
        last_gae = 0.0

        for t in reversed(range(n_steps)):
            if t == n_steps - 1:
                next_non_terminal = 1.0 - float(self.dones[t])
                next_val = last_value
            else:
                next_non_terminal = 1.0 - float(self.dones[t])
                next_val = self.values[t + 1]

            delta = self.rewards[t] + self.gamma * next_val * next_non_terminal - self.values[t]
            last_gae = delta + self.gamma * self.gae_lambda * next_non_terminal * last_gae
            advantages[t] = last_gae

        returns = advantages + np.array(self.values, dtype=np.float32)

        # Chuẩn hóa Advantage để ổn định gradient
        adv_mean = np.mean(advantages)
        adv_std = np.std(advantages) + 1e-8
        norm_advantages = (advantages - adv_mean) / adv_std

        b_states = torch.tensor(np.array(self.states), dtype=torch.float32)
        b_actions = torch.tensor(np.array(self.actions), dtype=torch.long)
        b_log_probs = torch.tensor(np.array(self.log_probs), dtype=torch.float32)
        b_values = torch.tensor(np.array(self.values), dtype=torch.float32)
        b_returns = torch.tensor(returns, dtype=torch.float32)
        b_advantages = torch.tensor(norm_advantages, dtype=torch.float32)

        return b_states, b_actions, b_log_probs, b_values, b_returns, b_advantages

    def get_batches(self, batch_size: int, last_value: float = 0.0) -> Generator:
        b_states, b_actions, b_log_probs, b_values, b_returns, b_advantages = self.compute_returns_and_advantages(last_value)
        total_samples = len(self.states)
        indices = np.arange(total_samples)
        np.random.shuffle(indices)

        for start_idx in range(0, total_samples, batch_size):
            batch_indices = indices[start_idx:start_idx + batch_size]
            yield (
                b_states[batch_indices],
                b_actions[batch_indices],
                b_log_probs[batch_indices],
                b_values[batch_indices],
                b_returns[batch_indices],
                b_advantages[batch_indices]
            )
