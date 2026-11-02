"""
agent.py — Triển khai đúng theo paper EVO-RL (ban2)

4 điều kiện so sánh:
  1. AdaptiveOperatorAgent     — PPO controller chọn trong 3 toán tử
  2. NoReinforcementLearningAgent — xác suất toán tử cố định (1/3 đều nhau)
  3. FixedOperatorStrategyAgent  — luôn chọn toán tử 0 (crossover)
  4. RandomOperatorSelectionAgent — chọn ngẫu nhiên đều

State vector (5 chiều) theo paper:
  z_t = [f_min, f_avg, rho_feas, phi_bar, tau]

Action space (3 toán tử):
  0 = structural_crossover
  1 = feasibility_preserving_mutation
  2 = diversification_mutation

PPO theo paper:
  hidden_dim = 64, lr = 0.0001, clip_eps = 0.2, entropy_coef = 0.01
  discount = 0.99, batch_size = 32, grad_clip = 1.0
"""
import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.distributions import Categorical
import numpy as np

from experiment_config import ExperimentConfig

config = ExperimentConfig()

NUM_OPERATORS = 3   # {crossover, repair_mut, diversify_mut}
STATE_DIM     = 5   # [f_min, f_avg, rho_feas, phi_bar, tau] theo paper
HIDDEN_DIM    = config.hidden_dim
CLIP_EPS      = config.clip_eps
ENTROPY_COEF  = config.entropy_coef
GAMMA         = config.discount
LR            = config.learning_rate
BATCH_SIZE    = config.batch_size
GRAD_CLIP     = config.grad_clip


class StateNormalizer:
    """Running normalizer để chuẩn hóa state vector."""
    def __init__(self, state_dim):
        self.state_dim = state_dim
        self.means = np.zeros(state_dim, dtype=np.float32)
        self.vars = np.zeros(state_dim, dtype=np.float32)
        self.count = 0

    def update(self, x):
        self.count += 1
        delta = x - self.means
        self.means += delta / self.count
        delta2 = x - self.means
        self.vars += delta * delta2

    def normalize(self, x):
        if self.count < 2:
            return x
        stds = np.sqrt(self.vars / self.count)
        stds = np.where(stds < 1e-4, 1.0, stds)
        return (x - self.means) / stds


# ── Shared MLP backbone ──────────────────────────────────────────────────────

class PolicyValueNet(nn.Module):
    """MLP 2 tầng, đầu ra policy + value (actor-critic cho PPO)."""
    def __init__(self, state_dim=STATE_DIM, hidden_dim=HIDDEN_DIM, n_actions=NUM_OPERATORS):
        super().__init__()
        self.shared = nn.Sequential(
            nn.Linear(state_dim, hidden_dim),
            nn.ReLU(),
            nn.Linear(hidden_dim, hidden_dim),
            nn.ReLU(),
        )
        self.policy_head = nn.Linear(hidden_dim, n_actions)   # logits
        self.value_head  = nn.Linear(hidden_dim, 1)           # V(s)

    def forward(self, x):
        h = self.shared(x)
        logits = self.policy_head(h)
        value  = self.value_head(h).squeeze(-1)
        return logits, value

    def get_action(self, state_tensor):
        """Trả về (action, log_prob, value) để dùng trong PPO rollout."""
        logits, value = self.forward(state_tensor)
        dist   = Categorical(logits=logits)
        action = dist.sample()
        return action.item(), dist.log_prob(action), value


# ── PPO update ───────────────────────────────────────────────────────────────

class PPOBuffer:
    """Lưu trữ một đoạn rollout để cập nhật PPO."""
    def __init__(self):
        self.states, self.actions, self.rewards = [], [], []
        self.log_probs, self.values, self.dones = [], [], []

    def store(self, state, action, reward, log_prob, value, done):
        self.states.append(state)
        self.actions.append(action)
        self.rewards.append(reward)
        self.log_probs.append(log_prob)
        self.values.append(value)
        self.dones.append(done)

    def clear(self):
        self.__init__()

    def compute_gae(self, last_value=0.0, gamma=GAMMA, lam=0.95):
        """GAE (Generalized Advantage Estimation) with variance reduction."""
        rewards = torch.tensor(self.rewards, dtype=torch.float32)
        dones = torch.tensor(self.dones, dtype=torch.float32)
        values = torch.stack(self.values).detach().cpu()
        
        advantages = torch.zeros_like(rewards)
        last_gae = 0.0
        
        next_values = torch.cat([values[1:], torch.tensor([last_value])])
        
        for t in reversed(range(len(rewards))):
            delta = rewards[t] + gamma * next_values[t] * (1.0 - dones[t]) - values[t]
            advantages[t] = last_gae = delta + gamma * lam * (1.0 - dones[t]) * last_gae
            
        returns = advantages + values
        return returns, advantages


def ppo_update(net, optimizer, buffer: PPOBuffer, last_value=0.0, n_epochs=4):
    """Cập nhật PPO sử dụng GAE và mini-batch."""
    returns, advantages = buffer.compute_gae(last_value, gamma=GAMMA, lam=0.95)
    
    device = next(net.parameters()).device
    states     = torch.tensor(np.array(buffer.states), dtype=torch.float32).to(device)
    actions    = torch.tensor(buffer.actions, dtype=torch.long).to(device)
    old_lps    = torch.stack(buffer.log_probs).detach().to(device)
    returns    = returns.to(device)
    advantages = advantages.to(device)

    # Chuẩn hóa advantages
    advantages = (advantages - advantages.mean()) / (advantages.std() + 1e-8)

    policy_losses = []
    value_losses = []
    entropies = []
    kls = []

    dataset_size = states.size(0)
    mini_batch_size = min(32, dataset_size)

    for _ in range(n_epochs):
        permutation = torch.randperm(dataset_size)
        for start_idx in range(0, dataset_size, mini_batch_size):
            batch_indices = permutation[start_idx : start_idx + mini_batch_size]
            
            b_states = states[batch_indices]
            b_actions = actions[batch_indices]
            b_old_lps = old_lps[batch_indices]
            b_returns = returns[batch_indices]
            b_advantages = advantages[batch_indices]

            logits, values = net(b_states)
            dist    = Categorical(logits=logits)
            new_lps = dist.log_prob(b_actions)
            entropy = dist.entropy().mean()

            ratio = torch.exp(new_lps - b_old_lps)
            surr1 = ratio * b_advantages
            surr2 = torch.clamp(ratio, 1 - CLIP_EPS, 1 + CLIP_EPS) * b_advantages

            policy_loss = -torch.min(surr1, surr2).mean()
            value_loss  = F.mse_loss(values, b_returns)
            loss = policy_loss + 0.5 * value_loss - ENTROPY_COEF * entropy

            optimizer.zero_grad()
            loss.backward()
            nn.utils.clip_grad_norm_(net.parameters(), GRAD_CLIP)
            optimizer.step()

            # Tính toán KL Divergence xấp xỉ
            log_ratio = new_lps - b_old_lps
            approx_kl = ((torch.exp(log_ratio) - 1) - log_ratio).mean()

            policy_losses.append(policy_loss.item())
            value_losses.append(value_loss.item())
            entropies.append(entropy.item())
            kls.append(approx_kl.item())

    return {
        'policy_loss': float(np.mean(policy_losses)),
        'value_loss':  float(np.mean(value_losses)),
        'entropy':     float(np.mean(entropies)),
        'kl':          float(np.mean(kls))
    }


# ── Agent 1: AdaptiveOperatorAgent (PPO) ────────────────────────────────────

class AdaptiveOperatorAgent:
    """EVO-RL agent: dùng PPO để chọn toán tử theo state 10 chiều cải tiến."""
    def __init__(self, state_dim=STATE_DIM, action_dim=NUM_OPERATORS):
        self.net = PolicyValueNet(state_dim, HIDDEN_DIM, action_dim)
        self.optimizer = torch.optim.Adam(self.net.parameters(), lr=LR)
        self.scheduler = torch.optim.lr_scheduler.StepLR(self.optimizer, step_size=50, gamma=0.5)
        self.buffer = PPOBuffer()
        self.normalizer = StateNormalizer(state_dim)
        self._last_log_prob = None
        self._last_value    = None

    def select_action(self, state, train=True):
        """state: np.array shape (10,) — state vector cải tiến."""
        if train:
            self.normalizer.update(state)
        norm_state = self.normalizer.normalize(state)
        s = torch.tensor(norm_state, dtype=torch.float32)
        
        with torch.set_grad_enabled(train):
            logits, value = self.net(s)
            if train:
                dist   = Categorical(logits=logits)
                action = dist.sample()
                self._last_log_prob = dist.log_prob(action)
                self._last_value    = value
                return action.item()
            else:
                action = torch.argmax(logits).item()
                return action

    def get_action_probs(self, state):
        norm_state = self.normalizer.normalize(state)
        s = torch.tensor(norm_state, dtype=torch.float32)
        with torch.no_grad():
            logits, _ = self.net(s)
            probs = F.softmax(logits, dim=-1)
        return probs.cpu().numpy().tolist()

    def store_transition(self, state, action, reward, done):
        norm_state = self.normalizer.normalize(state)
        self.buffer.store(
            norm_state, action, reward,
            self._last_log_prob, self._last_value, done)

    def update(self, next_state=None):
        if len(self.buffer.states) >= BATCH_SIZE:
            last_value = 0.0
            if next_state is not None:
                norm_next = self.normalizer.normalize(next_state)
                s_tensor = torch.tensor(norm_next, dtype=torch.float32)
                with torch.no_grad():
                    _, val = self.net(s_tensor)
                    last_value = val.item()
            metrics = ppo_update(self.net, self.optimizer, self.buffer, last_value=last_value)
            self.buffer.clear()
            return metrics
        return None

    # Compat: policy_network cho train.py gốc
    @property
    def policy_network(self):
        return self.net


# ── Agent 2: NoReinforcementLearningAgent ────────────────────────────────────

class NoReinforcementLearningAgent:
    """Không có RL — xác suất toán tử cố định đều (1/3 mỗi loại)."""
    def __init__(self, state_dim=STATE_DIM, action_dim=NUM_OPERATORS):
        self.policy_network = PolicyValueNet(state_dim, HIDDEN_DIM, action_dim)
        # Freeze hoàn toàn — không học
        for p in self.policy_network.parameters():
            p.requires_grad_(False)

    def select_action(self, state, train=True):
        return int(torch.randint(0, NUM_OPERATORS, (1,)).item())

    def get_action_probs(self, state):
        return [1.0/NUM_OPERATORS] * NUM_OPERATORS

    def store_transition(self, *args): pass
    def update(self, *args, **kwargs): pass


# ── Agent 3: FixedOperatorStrategyAgent ──────────────────────────────────────

class FixedOperatorStrategyAgent:
    """Lịch trình cố định: xoay vòng 0→1→2→0→... mỗi lần gọi."""
    def __init__(self, state_dim=STATE_DIM, action_dim=NUM_OPERATORS):
        self.policy_network = PolicyValueNet(state_dim, HIDDEN_DIM, action_dim)
        for p in self.policy_network.parameters():
            p.requires_grad_(False)
        self._step = 0

    def select_action(self, state, train=True):
        op = self._step % NUM_OPERATORS
        self._step += 1
        return op

    def get_action_probs(self, state):
        probs = [0.0] * NUM_OPERATORS
        probs[self._step % NUM_OPERATORS] = 1.0
        return probs

    def store_transition(self, *args): pass
    def update(self, *args, **kwargs): pass


# ── Agent 4: RandomOperatorSelectionAgent ────────────────────────────────────

class RandomOperatorSelectionAgent:
    """Chọn toán tử hoàn toàn ngẫu nhiên đều."""
    def __init__(self, state_dim=STATE_DIM, action_dim=NUM_OPERATORS):
        self.policy_network = PolicyValueNet(state_dim, HIDDEN_DIM, action_dim)
        for p in self.policy_network.parameters():
            p.requires_grad_(False)

    def select_action(self, state, train=True):
        return int(np.random.randint(0, NUM_OPERATORS))

    def get_action_probs(self, state):
        return [1.0/NUM_OPERATORS] * NUM_OPERATORS

    def store_transition(self, *args): pass
    def update(self, *args, **kwargs): pass