"""
rl/ppo.py — Cài đặt thuật toán PPO-AOS Agent và các Baseline Agent đối chiếu.
"""
import torch
import torch.nn as nn
import torch.optim as optim
import numpy as np
from typing import Dict, Any, Optional

from configs.config import ExperimentConfig
from .policy import ActorNetwork
from .value import CriticNetwork
from .buffer import PPOBuffer
from .state import StateNormalizer


class AdaptiveOperatorAgent:
    """
    Tác tử PPO (Proximal Policy Optimization) điều phối lựa chọn toán tử thích nghi (PPO-AOS).
    """
    def __init__(self, config: ExperimentConfig):
        self.config = config
        self.device = torch.device(config.device)
        
        self.actor = ActorNetwork(
            state_dim=config.state_dim, 
            num_operators=config.num_operators, 
            hidden_dim=config.hidden_dim
        ).to(self.device)
        
        self.critic = CriticNetwork(
            state_dim=config.state_dim, 
            hidden_dim=config.hidden_dim
        ).to(self.device)
        
        self.optimizer = optim.Adam([
            {'params': self.actor.parameters(), 'lr': config.learning_rate},
            {'params': self.critic.parameters(), 'lr': config.learning_rate}
        ], eps=1e-5)
        
        self.buffer = PPOBuffer(gamma=config.discount)
        self.normalizer = StateNormalizer(state_dim=config.state_dim)
        
        self.last_state = None
        self.last_action = None
        self.last_log_prob = None
        self.last_value = None

    def select_action(self, state: np.ndarray, train: bool = True) -> int:
        """Lựa chọn toán tử dựa trên trạng thái hiện tại."""
        norm_state = self.normalizer.normalize(state)
        state_t = torch.tensor(norm_state, dtype=torch.float32, device=self.device).unsqueeze(0)
        
        if train:
            self.normalizer.update(state)
            with torch.no_grad():
                dist = self.actor(state_t)
                action_t = dist.sample()
                log_prob_t = dist.log_prob(action_t)
                value_t = self.critic(state_t)
                
            action = int(action_t.item())
            self.last_state = norm_state
            self.last_action = action
            self.last_log_prob = float(log_prob_t.item())
            self.last_value = float(value_t.item())
            return action
        else:
            with torch.inference_mode():
                probs = self.actor.get_action_probs(state_t).squeeze(0)
                return int(torch.argmax(probs).item())

    def get_action_probs(self, state: np.ndarray) -> np.ndarray:
        """Trả về mảng xác suất [p_crossover, p_feasible_mut, p_diversify_mut]."""
        norm_state = self.normalizer.normalize(state)
        state_t = torch.tensor(norm_state, dtype=torch.float32, device=self.device).unsqueeze(0)
        with torch.inference_mode():
            probs = self.actor.get_action_probs(state_t).squeeze(0).cpu().numpy()
        return probs

    def store_transition(self, state: np.ndarray, action: int, reward: float, done: bool):
        """Lưu bước chuyển trạng thái vào Rollout Buffer."""
        if self.last_state is not None:
            self.buffer.store(
                state=self.last_state,
                action=self.last_action,
                reward=reward,
                log_prob=self.last_log_prob,
                value=self.last_value,
                done=done
            )

    def update(self, next_state: np.ndarray) -> Optional[Dict[str, float]]:
        """Cập nhật trọng số mạng Actor và Critic bằng PPO Clipped Objective."""
        if self.buffer.size() < self.config.batch_size:
            return None

        norm_next_state = self.normalizer.normalize(next_state)
        next_state_t = torch.tensor(norm_next_state, dtype=torch.float32, device=self.device).unsqueeze(0)
        with torch.no_grad():
            last_value = float(self.critic(next_state_t).item())

        policy_losses = []
        value_losses = []
        entropies = []
        kl_divs = []

        for _ in range(self.config.ppo_epochs):
            stop_early = False
            for b_states, b_actions, b_old_log_probs, b_old_values, b_returns, b_advantages in self.buffer.get_batches(self.config.batch_size, last_value):
                b_states = b_states.to(self.device)
                b_actions = b_actions.to(self.device)
                b_old_log_probs = b_old_log_probs.to(self.device)
                b_old_values = b_old_values.to(self.device)
                b_returns = b_returns.to(self.device)
                b_advantages = b_advantages.to(self.device)

                # 1. Actor Loss (Clipped Surrogate)
                dist = self.actor(b_states)
                new_log_probs = dist.log_prob(b_actions)
                entropy = dist.entropy().mean()

                ratio = torch.exp(new_log_probs - b_old_log_probs)
                surr1 = ratio * b_advantages
                surr2 = torch.clamp(ratio, 1.0 - self.config.clip_eps, 1.0 + self.config.clip_eps) * b_advantages
                actor_loss = -torch.min(surr1, surr2).mean() - self.config.entropy_coef * entropy

                # 2. Critic Loss với Value Function Clipping (Chuẩn Stable-Baselines3)
                values = self.critic(b_states).squeeze(-1)
                values_clipped = b_old_values + torch.clamp(values - b_old_values, -self.config.clip_eps, self.config.clip_eps)
                vf_loss1 = (values - b_returns) ** 2
                vf_loss2 = (values_clipped - b_returns) ** 2
                value_loss = self.config.value_coef * 0.5 * torch.max(vf_loss1, vf_loss2).mean()

                # 3. Total Loss & Optimization
                total_loss = actor_loss + value_loss

                self.optimizer.zero_grad()
                total_loss.backward()
                nn.utils.clip_grad_norm_(
                    list(self.actor.parameters()) + list(self.critic.parameters()), 
                    self.config.grad_clip
                )
                self.optimizer.step()

                # Tracking metrics & Approximate KL
                with torch.no_grad():
                    approx_kl = ((ratio - 1.0) - torch.log(ratio)).mean().item()
                    kl_divs.append(approx_kl)
                    policy_losses.append(actor_loss.item())
                    value_losses.append(value_loss.item())
                    entropies.append(entropy.item())

                    # Target KL Early Stopping (CleanRL / SB3 Standard: dừng sớm nếu policy trôi quá 0.05)
                    if approx_kl > 0.05:
                        stop_early = True
                        break
            if stop_early:
                break

        self.buffer.clear()

        return {
            'policy_loss': float(np.mean(policy_losses)) if policy_losses else 0.0,
            'value_loss': float(np.mean(value_losses)) if value_losses else 0.0,
            'entropy': float(np.mean(entropies)) if entropies else 0.0,
            'kl': float(np.mean(kl_divs)) if kl_divs else 0.0,
        }


# ==========================================
# CÁC BASELINE AGENTS ĐỐI CHỨNG
# ==========================================

class NoReinforcementLearningAgent:
    """Baseline 1: Uniform Operator Selection (Xác suất đồng đều cố định 1/3)."""
    def __init__(self, config: ExperimentConfig):
        self.num_operators = config.num_operators

    def select_action(self, state: np.ndarray, train: bool = True) -> int:
        return int(np.random.choice(self.num_operators))

    def get_action_probs(self, state: np.ndarray) -> np.ndarray:
        return np.full(self.num_operators, 1.0 / self.num_operators, dtype=np.float32)

    def store_transition(self, *args, **kwargs):
        pass

    def update(self, *args, **kwargs):
        return None


class FixedOperatorStrategyAgent:
    """Baseline 2: Thuật toán di truyền nhóm GGA chuẩn của Thầy (Fixed Grouping Genetic Algorithm: pc=0.90, pm=0.05)."""
    def __init__(self, config: ExperimentConfig):
        self.num_operators = config.num_operators

    def select_action(self, state: np.ndarray, train: bool = True) -> int:
        return 3  # Action 3: Standard Teacher's GGA

    def get_action_probs(self, state: np.ndarray) -> np.ndarray:
        return np.array([0.90, 0.05, 0.05], dtype=np.float32)

    def store_transition(self, *args, **kwargs):
        pass

    def update(self, *args, **kwargs):
        return None


class RandomOperatorSelectionAgent:
    """Baseline 3: Pure Random Selection."""
    def __init__(self, config: ExperimentConfig):
        self.num_operators = config.num_operators

    def select_action(self, state: np.ndarray, train: bool = True) -> int:
        return int(np.random.randint(0, self.num_operators))

    def get_action_probs(self, state: np.ndarray) -> np.ndarray:
        return np.full(self.num_operators, 1.0 / self.num_operators, dtype=np.float32)

    def store_transition(self, *args, **kwargs):
        pass

    def update(self, *args, **kwargs):
        return None
