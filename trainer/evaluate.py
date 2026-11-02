"""
trainer/evaluate.py — Đánh giá mô hình và chạy thực nghiệm đa hạt giống (20 independent seeds).
Đảm bảo ghi nhận chính xác 100% nghiệm tối ưu sau toàn bộ các thế hệ tiến hóa.
"""
import os
os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"
import random
import time
import torch
import numpy as np
from typing import Dict, Any, List, Optional, Tuple

from configs.config import ExperimentConfig
from problem.graph import SClubGraph
from environment.env import SClubEnvironment
from rl.ppo import (
    AdaptiveOperatorAgent,
    NoReinforcementLearningAgent,
    FixedOperatorStrategyAgent,
    RandomOperatorSelectionAgent
)
from rl.greedy_aos import GreedyAOSAgent
from rl.mab_aos import MABAOSAgent
from problem.imsm import run_imsm
from problem.cca import run_cca
from .train import train_agent


def set_seed(seed: int):
    """Cố định seed ngẫu nhiên cho tất cả các thư viện để đảm bảo khả năng tái lập."""
    random.seed(seed)
    np.random.seed(seed)
    torch.manual_seed(seed)
    if torch.cuda.is_available():
        torch.cuda.manual_seed_all(seed)


def create_agent(condition_name: str, config: ExperimentConfig):
    """Khởi tạo agent tương ứng với chiến lược đối chứng."""
    if condition_name == "PPO-AOS":
        return AdaptiveOperatorAgent(config)
    elif condition_name in ("MAB-AOS", "UCB-AOS"):
        return MABAOSAgent(config)
    elif condition_name == "Greedy-AOS":
        return GreedyAOSAgent(config)
    elif condition_name == "No-RL":
        return NoReinforcementLearningAgent(config)
    elif condition_name == "Fixed":
        return FixedOperatorStrategyAgent(config)
    elif condition_name == "Random":
        return RandomOperatorSelectionAgent(config)
    else:
        raise ValueError(f"Chiến lược không hợp lệ: {condition_name}")


def evaluate_agent(
    agent, 
    env: SClubEnvironment, 
    num_episodes: int = 1
) -> Dict[str, Any]:
    """Chạy đánh giá mô hình trên môi trường độc lập."""
    rewards = []
    cover_sizes = []
    feasibilities = []

    for _ in range(num_episodes):
        state = env.reset()
        done = False
        ep_reward = 0.0

        while not done:
            action = agent.select_action(state, train=False)
            state, reward, done, info = env.step(action)
            ep_reward += reward

        rewards.append(ep_reward)
        cover_sizes.append(env.get_cover_size())
        feasibilities.append(env.is_fully_covered())

    return {
        'eval_mean_reward': float(np.mean(rewards)) if rewards else 0.0,
        'eval_best_cover': int(np.min(cover_sizes)) if cover_sizes else 0,
        'eval_mean_cover': float(np.mean(cover_sizes)) if cover_sizes else 0.0,
        'eval_feasible_rate': float(np.mean(feasibilities)) if feasibilities else 0.0,
        'is_valid_solution': env.validate_solution()
    }


def run_single_seed(
    seed: int, 
    condition_name: str, 
    graph: SClubGraph, 
    config: ExperimentConfig,
    progress_meta: Optional[Dict[str, Any]] = None
) -> Dict[str, Any]:
    """Chạy một lượt thực nghiệm trên một hạt giống ngẫu nhiên độc lập."""
    set_seed(seed)
    graph.clear_cache()
    
    # 1. Nhánh xử lý đặc thù cho thuật toán xấp xỉ tham lam lặp I-MSM
    if condition_name == "I-MSM":
        if progress_meta is not None and progress_meta.get('shared_status') is not None:
            from .progress import update_worker_status
            update_worker_status(
                shared_status=progress_meta['shared_status'],
                seed_idx=progress_meta['seed_idx'],
                seed_val=progress_meta['seed_val'],
                worker_id=progress_meta.get('worker_id', progress_meta['seed_idx']),
                condition=condition_name,
                cond_idx=progress_meta.get('cond_idx', 1),
                total_conds=progress_meta.get('total_conds', 8),
                gen=1,
                max_gen=50,
                best_cover=graph.n_nodes,
                is_feasible=True,
                elapsed=0.0,
                status="RUNNING"
            )
        imsm_res = run_imsm(graph, config, seed=seed)
        if progress_meta is not None and progress_meta.get('shared_status') is not None:
            from .progress import update_worker_status
            update_worker_status(
                shared_status=progress_meta['shared_status'],
                seed_idx=progress_meta['seed_idx'],
                seed_val=progress_meta['seed_val'],
                worker_id=progress_meta.get('worker_id', progress_meta['seed_idx']),
                condition=condition_name,
                cond_idx=progress_meta.get('cond_idx', 1),
                total_conds=progress_meta.get('total_conds', 8),
                gen=50,
                max_gen=50,
                best_cover=imsm_res['best_cover'],
                is_feasible=imsm_res['is_feasible'],
                elapsed=imsm_res['runtime'],
                status="RUNNING"
            )
        return {
            'seed': seed,
            'condition': condition_name,
            'best_cover': imsm_res['best_cover'],
            'best_fitness': imsm_res['best_fitness'],
            'avg_fitness': imsm_res['avg_fitness'],
            'diameter_violation': imsm_res['mean_violation'],
            'diversity': imsm_res['diversity'],
            'stagnation_steps': 0,
            'is_feasible': imsm_res['is_feasible'],
            'runtime_seconds': imsm_res['runtime'],
            'best_solution_clubs': imsm_res.get('best_solution_clubs', {}),
            'club_sizes': imsm_res.get('club_sizes', []),
            'train_metrics': imsm_res['history'],
            'eval_metrics': {
                'eval_mean_reward': 0.0,
                'eval_best_cover': imsm_res['best_cover'],
                'eval_mean_cover': float(imsm_res['best_cover']),
                'eval_feasible_rate': 1.0 if imsm_res['is_feasible'] else 0.0,
                'is_valid_solution': imsm_res['is_feasible']
            },
            'convergence_curve': imsm_res['history']['convergence_curve'],
            'action_probs': imsm_res['history']['action_probs'],
        }

    # 2. Nhánh xử lý cho thuật toán đối chứng văn hiến CCA (Club-Cover-Approx)
    if condition_name == "CCA":
        if progress_meta is not None and progress_meta.get('shared_status') is not None:
            from .progress import update_worker_status
            update_worker_status(
                shared_status=progress_meta['shared_status'],
                seed_idx=progress_meta['seed_idx'],
                seed_val=progress_meta['seed_val'],
                worker_id=progress_meta.get('worker_id', progress_meta['seed_idx']),
                condition=condition_name,
                cond_idx=progress_meta.get('cond_idx', 1),
                total_conds=progress_meta.get('total_conds', 8),
                gen=1,
                max_gen=50,
                best_cover=graph.n_nodes,
                is_feasible=True,
                elapsed=0.0,
                status="RUNNING"
            )
        cca_res = run_cca(graph, config, seed=seed)
        if progress_meta is not None and progress_meta.get('shared_status') is not None:
            from .progress import update_worker_status
            update_worker_status(
                shared_status=progress_meta['shared_status'],
                seed_idx=progress_meta['seed_idx'],
                seed_val=progress_meta['seed_val'],
                worker_id=progress_meta.get('worker_id', progress_meta['seed_idx']),
                condition=condition_name,
                cond_idx=progress_meta.get('cond_idx', 1),
                total_conds=progress_meta.get('total_conds', 8),
                gen=50,
                max_gen=50,
                best_cover=cca_res['best_cover'],
                is_feasible=cca_res['is_feasible'],
                elapsed=cca_res['runtime'],
                status="RUNNING"
            )
        return {
            'seed': seed,
            'condition': condition_name,
            'best_cover': cca_res['best_cover'],
            'best_fitness': cca_res['best_fitness'],
            'avg_fitness': cca_res['avg_fitness'],
            'diameter_violation': cca_res['mean_violation'],
            'diversity': cca_res['diversity'],
            'stagnation_steps': 0,
            'is_feasible': cca_res['is_feasible'],
            'runtime_seconds': cca_res['runtime'],
            'best_solution_clubs': cca_res.get('best_solution_clubs', {}),
            'club_sizes': cca_res.get('club_sizes', []),
            'train_metrics': cca_res['history'],
            'eval_metrics': {
                'eval_mean_reward': 0.0,
                'eval_best_cover': cca_res['best_cover'],
                'eval_mean_cover': float(cca_res['best_cover']),
                'eval_feasible_rate': 1.0 if cca_res['is_feasible'] else 0.0,
                'is_valid_solution': cca_res['is_feasible']
            },
            'convergence_curve': cca_res['history']['convergence_curve'],
            'action_probs': cca_res['history']['action_probs'],
        }

    # 3. Nhánh xử lý cho các thuật toán tiến hóa (PPO-AOS, MAB-AOS, Greedy-AOS, No-RL, Fixed, Random)
    agent = create_agent(condition_name, config)
    env = SClubEnvironment(graph, config)

    start_t = time.time()
    train_metrics = train_agent(agent, env, config, progress_meta=progress_meta)
    total_time = time.time() - start_t

    # Lấy nghiệm tối ưu thực sự đạt được qua toàn bộ các thế hệ tiến hóa
    best_ind = env.best_overall_individual if env.best_overall_individual is not None else env.population.best_individual
    best_cover = int(best_ind.num_clubs) if best_ind else int(env.get_cover_size())
    best_fitness = float(env.best_overall_fitness)
    avg_fitness = float(env.population.avg_fitness) if env.population else best_fitness
    is_feasible = bool(best_ind.is_feasible) if best_ind else bool(env.is_fully_covered())
    diameter_violation = float(best_ind.diameter_violation) if best_ind else 0.0
    diversity = float(env.population.diversity) if env.population else 0.0
    stagnation_steps = int(env.stagnation_count)
    clubs_dict = {int(k): [int(v) for v in nodes] for k, nodes in best_ind.get_clubs().items()} if best_ind else {}
    club_sizes = [len(v) for v in clubs_dict.values()] if clubs_dict else []
    # Trích xuất chỉ số đánh giá trực tiếp từ đợt tiến hóa (Zero Redundant Computation)
    eval_metrics = {
        'eval_mean_reward': float(np.mean(train_metrics['episode_rewards'])) if train_metrics.get('episode_rewards') else 0.0,
        'eval_best_cover': best_cover,
        'eval_mean_cover': float(best_cover),
        'eval_feasible_rate': 1.0 if is_feasible else 0.0,
        'is_valid_solution': is_feasible
    }

    return {
        'seed': seed,
        'condition': condition_name,
        'best_cover': best_cover,
        'best_fitness': best_fitness,
        'avg_fitness': avg_fitness,
        'diameter_violation': diameter_violation,
        'diversity': diversity,
        'stagnation_steps': stagnation_steps,
        'is_feasible': is_feasible,
        'runtime_seconds': float(total_time),
        'best_solution_clubs': clubs_dict,
        'club_sizes': club_sizes,
        'train_metrics': train_metrics,
        'eval_metrics': eval_metrics,
        'convergence_curve': train_metrics['convergence_curve'],
        'action_probs': train_metrics['action_probs'],
    }


def run_single_seed_full_pipeline(
    seed_idx: int,
    seed_val: int,
    raw_ig_graph,
    config: ExperimentConfig,
    output_dir: Optional[str] = None,
    graph_info: Optional[Dict[str, Any]] = None,
    hardware_info: Optional[str] = None,
    shared_status: Optional[Any] = None,
    total_seeds: int = 20
) -> Tuple[int, int, Dict[str, Dict[str, Any]]]:
    """
    Thực thi độc lập toàn bộ các thuật toán (conditions) cho 1 Seed.
    Tự động xuất file kết quả riêng results_seed_X.md/json và trả về dữ liệu.
    An toàn 100% khi chạy trong môi trường đa tiến trình (Multiprocessing).
    """
    import gc
    import os
    
    # Cân bằng luồng CPU cho từng worker: tránh tranh chấp luồng (Thread Contention)
    threads_per_worker = max(1, (os.cpu_count() or 12) // max(1, config.num_workers))
    try:
        torch.set_num_threads(threads_per_worker)
    except Exception:
        pass

    set_seed(seed_val)
    graph = SClubGraph(raw_ig_graph, s=config.s_club_threshold)
    
    seed_data_by_condition = {}
    total_conds = len(config.conditions)

    for cond_idx, condition in enumerate(config.conditions, start=1):
        progress_meta = {
            'shared_status': shared_status,
            'seed_idx': seed_idx,
            'seed_val': seed_val,
            'worker_id': ((seed_idx - 1) % config.num_workers) + 1,
            'condition': condition,
            'cond_idx': cond_idx,
            'total_conds': total_conds,
            'total_seeds': total_seeds
        }
        res = run_single_seed(seed_val, condition, graph, config, progress_meta=progress_meta)
        seed_data_by_condition[condition] = res

    # Đánh dấu seed đã hoàn thành
    if shared_status is not None:
        from .progress import update_worker_status
        update_worker_status(
            shared_status=shared_status,
            seed_idx=seed_idx,
            seed_val=seed_val,
            worker_id=((seed_idx - 1) % config.num_workers) + 1,
            condition="HOÀN TẤT",
            cond_idx=total_conds,
            total_conds=total_conds,
            gen=config.max_generations,
            max_gen=config.max_generations,
            best_cover=min(r['best_cover'] for r in seed_data_by_condition.values()),
            is_feasible=True,
            elapsed=0.0,
            status="FINISHED"
        )

    graph.clear_cache()
    gc.collect()

    if output_dir:
        from analysis.export import export_single_seed_result
        export_single_seed_result(
            seed_idx=seed_idx,
            seed_val=seed_val,
            seed_data_by_condition=seed_data_by_condition,
            output_dir=output_dir,
            graph_info=graph_info,
            hardware_info=hardware_info
        )

    return seed_idx, seed_val, seed_data_by_condition

