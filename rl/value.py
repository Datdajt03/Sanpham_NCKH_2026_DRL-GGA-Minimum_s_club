"""
rl/value.py — Mạng Critic (Value Network) để ước lượng hàm giá trị trạng thái V(s).
"""
import torch
import torch.nn as nn
import numpy as np


def layer_init(layer: nn.Linear, std: float = np.sqrt(2), bias_const: float = 0.0) -> nn.Linear:
    nn.init.orthogonal_(layer.weight, std)
    nn.init.constant_(layer.bias, bias_const)
    return layer


class CriticNetwork(nn.Module):
    """
    Mạng Critic (MLP 2 lớp ẩn):
    Nhận đầu vào: Vector trạng thái 5 chiều
    Đầu ra: Giá trị vô hướng V(s) đại diện cho kỳ vọng phần thưởng tích lũy.
    """
    def __init__(self, state_dim: int = 5, hidden_dim: int = 64):
        super().__init__()
        self.net = nn.Sequential(
            layer_init(nn.Linear(state_dim, hidden_dim)),
            nn.Tanh(),
            layer_init(nn.Linear(hidden_dim, hidden_dim)),
            nn.Tanh(),
            layer_init(nn.Linear(hidden_dim, 1), std=1.0)
        )

    def forward(self, state: torch.Tensor) -> torch.Tensor:
        return self.net(state)
