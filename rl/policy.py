"""
rl/policy.py — Mạng Actor (Policy Network) để dự đoán phân bố xác suất chọn toán tử.
"""
import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.distributions import Categorical


import numpy as np


def layer_init(layer: nn.Linear, std: float = np.sqrt(2), bias_const: float = 0.0) -> nn.Linear:
    """Khởi tạo trọng số trực giao (Orthogonal Initialization) chuẩn cho RL."""
    nn.init.orthogonal_(layer.weight, std)
    nn.init.constant_(layer.bias, bias_const)
    return layer


class ActorNetwork(nn.Module):
    """
    Mạng Actor (MLP 2 lớp ẩn):
    Nhận đầu vào: Vector trạng thái 5 chiều
    Đầu ra: Phân bố xác suất Categorical trên 3 toán tử di truyền.
    """
    def __init__(self, state_dim: int = 5, num_operators: int = 3, hidden_dim: int = 64):
        super().__init__()
        self.net = nn.Sequential(
            layer_init(nn.Linear(state_dim, hidden_dim)),
            nn.Tanh(),
            layer_init(nn.Linear(hidden_dim, hidden_dim)),
            nn.Tanh(),
            layer_init(nn.Linear(hidden_dim, num_operators), std=0.01)
        )

    def forward(self, state: torch.Tensor) -> Categorical:
        logits = self.net(state)
        return Categorical(logits=logits)

    def get_action_probs(self, state: torch.Tensor) -> torch.Tensor:
        """Trả về mảng xác suất softmax của 3 toán tử (tối ưu hóa inference_mode)."""
        with torch.inference_mode():
            logits = self.net(state)
            return F.softmax(logits, dim=-1)
