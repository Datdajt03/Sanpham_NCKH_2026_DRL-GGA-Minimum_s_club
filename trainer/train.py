"""
trainer/train.py — Huấn luyện tác tử PPO trong môi trường tiến hóa thích nghi (AOS).
Ghi nhận chính xác quỹ đạo tiến hóa (convergence curve & action probabilities) theo từng thế hệ (generations).
Hiển thị mức sử dụng CPU & GPU cập nhật theo thời gian thực (Real-time Live Progress Monitor).
"""
import sys
import time
import torch
import psutil
import numpy as np
from typing import Dict, Any, Optional
from configs.config import ExperimentConfig
from environment.env import SClubEnvironment
from .progress import update_worker_status


def train_agent(
    agent, 
    env: SClubEnvironment, 
    config: ExperimentConfig,
    progress_meta: Optional[Dict[str, Any]] = None
) -> Dict[str, Any]:
    """
    Thực hiện 1 lượt chạy tiến hóa (1 Seed Run) qua max_generations thế hệ.
    Tác tử PPO thực hiện Online Adaptive Operator Selection (AOS),
    học và cập nhật trọng số trực tuyến qua các thế hệ.
    Đồng thời cập nhật trạng thái thời gian thực cho Live Parallel Dashboard.
    """
    metrics = {
        'episode_rewards': [],
        'cover_sizes': [],
        'convergence_curve': [],
        'action_probs': [],
        'policy_losses': [],
        'value_losses': [],
        'entropies': [],
        'kl_divs': [],
        'runtime_seconds': 0.0
    }
    
    start_time = time.time()
    state = env.reset()
    done = False
    
    # Ghi nhận trạng thái khởi tạo ban đầu (Thế hệ 0)
    initial_cover = env.get_cover_size()
    metrics['convergence_curve'].append(float(env.best_overall_fitness))
    metrics['cover_sizes'].append(int(initial_cover))
    metrics['action_probs'].append(agent.get_action_probs(state).tolist())

    step_count = 0
    max_steps = config.max_generations

    while not done and step_count < max_steps:
        step_count += 1
        
        # 1. Thu thập xác suất chọn toán tử tại trạng thái hiện tại
        probs = agent.get_action_probs(state)
        
        # 2. Chọn toán tử tiến hóa (Crossover / Feasible Mut / Diversify Mut)
        action = agent.select_action(state, train=True)
        
        # 3. Môi trường thực thi toán tử trên quần thể
        next_state, reward, done, info = env.step(action)

        # 4. Lưu bước chuyển trạng thái vào Rollout Buffer của PPO
        agent.store_transition(state, action, reward, done)

        # 5. Cập nhật mạng PPO nếu đủ batch_size
        update_info = agent.update(next_state)
        if update_info is not None:
            metrics['policy_losses'].append(float(update_info['policy_loss']))
            metrics['value_losses'].append(float(update_info['value_loss']))
            metrics['entropies'].append(float(update_info['entropy']))
            metrics['kl_divs'].append(float(update_info['kl']))

        # 6. Ghi nhận dữ liệu từng thế hệ
        metrics['episode_rewards'].append(float(reward))
        metrics['convergence_curve'].append(float(env.best_overall_fitness))
        metrics['cover_sizes'].append(int(env.get_cover_size()))
        metrics['action_probs'].append(probs.tolist())

        # 7. Cập nhật tiến độ vào shared_dict cho Live Parallel Dashboard
        if progress_meta is not None and progress_meta.get('shared_status') is not None:
            cur_best = env.best_overall_individual.num_clubs if env.best_overall_individual else env.get_cover_size()
            is_feas = bool(env.best_overall_individual.is_feasible) if env.best_overall_individual else True
            update_worker_status(
                shared_status=progress_meta['shared_status'],
                seed_idx=progress_meta['seed_idx'],
                seed_val=progress_meta['seed_val'],
                worker_id=progress_meta.get('worker_id', progress_meta['seed_idx']),
                condition=progress_meta['condition'],
                cond_idx=progress_meta.get('cond_idx', 1),
                total_conds=progress_meta.get('total_conds', 8),
                gen=step_count,
                max_gen=max_steps,
                best_cover=cur_best,
                is_feasible=is_feas,
                elapsed=time.time() - start_time,
                status="RUNNING"
            )

        state = next_state

    # Cập nhật lần cuối các mẫu còn lại trong buffer nếu có
    final_update = agent.update(state)
    if final_update is not None:
        metrics['policy_losses'].append(float(final_update['policy_loss']))
        metrics['value_losses'].append(float(final_update['value_loss']))
        metrics['entropies'].append(float(final_update['entropy']))
        metrics['kl_divs'].append(float(final_update['kl']))

    metrics['runtime_seconds'] = float(time.time() - start_time)
    return metrics