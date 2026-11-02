"""
Bai_2_DeepRL_AOS_Suitability/evaluate_bai2.py — Điều phối chạy thực nghiệm và xuất đầy đủ 4 bộ dữ liệu Bài 2.
"""
import os
import time
import random
import torch
import numpy as np
import pandas as pd
from typing import Dict, Any, List, Tuple

from dataset.loader import load_graph
from problem.graph import SClubGraph
from configs.config import ExperimentConfig
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
from .config_bai2 import Bai2Config
from .engine_bai2 import DetailedTrackerBai2, SClubEnvironmentBai2


def set_seed(seed: int):
    random.seed(seed)
    np.random.seed(seed)
    torch.manual_seed(seed)
    if torch.cuda.is_available():
        torch.cuda.manual_seed_all(seed)


def create_agent_bai2(condition: str, config: Bai2Config):
    exp_cfg = ExperimentConfig()
    exp_cfg.state_dim = config.state_dim
    exp_cfg.num_operators = config.num_operators
    exp_cfg.hidden_dim = config.hidden_dim
    exp_cfg.learning_rate = config.learning_rate
    exp_cfg.discount = config.discount
    exp_cfg.clip_eps = config.clip_eps
    exp_cfg.entropy_coef = config.entropy_coef
    exp_cfg.value_coef = config.value_coef
    exp_cfg.grad_clip = config.grad_clip
    exp_cfg.batch_size = config.batch_size
    exp_cfg.ppo_epochs = config.ppo_epochs

    if condition == "PPO-AOS":
        return AdaptiveOperatorAgent(exp_cfg)
    elif condition == "MAB-AOS":
        return MABAOSAgent(exp_cfg)
    elif condition == "Greedy-AOS":
        return GreedyAOSAgent(exp_cfg)
    elif condition == "No-RL":
        return NoReinforcementLearningAgent(exp_cfg)
    elif condition == "Fixed":
        return FixedOperatorStrategyAgent(exp_cfg)
    elif condition == "Random":
        return RandomOperatorSelectionAgent(exp_cfg)
    else:
        raise ValueError(f"Unknown condition: {condition}")


def run_single_seed_bai2(
    graph_path: str,
    dataset_name: str,
    graph_type: str,
    condition: str,
    seed: int,
    config: Bai2Config
) -> Tuple[Dict[str, Any], List[Dict[str, Any]], List[Dict[str, Any]]]:
    """Chạy 1 lượt thực nghiệm đầy đủ và thu thập toàn bộ dữ liệu Bài 2."""
    set_seed(seed)
    raw_g = load_graph(graph_path)
    graph = SClubGraph(raw_g, s=config.s_club_threshold)
    v_cnt = graph.n_nodes
    e_cnt = graph.n_edges
    density = (2.0 * e_cnt) / (v_cnt * (v_cnt - 1)) if v_cnt > 1 else 0.0
    tracker = DetailedTrackerBai2(dataset_name, condition, seed, graph.n_nodes)
    tracker.start()

    start_wall = time.perf_counter()

    exp_cfg = ExperimentConfig()
    exp_cfg.s_club_threshold = config.s_club_threshold
    exp_cfg.max_generations = config.max_generations

    # Nhánh Heuristics: I-MSM / CCA
    if condition == "I-MSM":
        res = run_imsm(graph, exp_cfg, seed=seed)
        elapsed = time.perf_counter() - start_wall
        run_record = {
            'dataset': dataset_name, 'graph_type': graph_type,
            'n': v_cnt, 'm': e_cnt, 'density': density, 's': config.s_club_threshold,
            'method': condition, 'seed': seed,
            'best_k': res['best_cover'], 'final_k': res['best_cover'],
            'mean_k': float(res['best_cover']), 'median_k': float(res['best_cover']), 'worst_k': res['best_cover'],
            'feasible_rate': 1.0 if res['is_feasible'] else 0.0,
            'best_violation': 0, 'mean_violation': 0.0,
            'fitness_evaluations': res.get('iterations', 100),
            'generations': 0,
            'runtime': elapsed,
            'time_to_first_feasible': elapsed if res['is_feasible'] else None,
            'time_to_best': elapsed,
            'status': 'SUCCESS'
        }
        return run_record, [], []

    elif condition == "CCA":
        res = run_cca(graph, exp_cfg, seed=seed)
        elapsed = time.perf_counter() - start_wall
        run_record = {
            'dataset': dataset_name, 'graph_type': graph_type,
            'n': v_cnt, 'm': e_cnt, 'density': density, 's': config.s_club_threshold,
            'method': condition, 'seed': seed,
            'best_k': res['best_cover'], 'final_k': res['best_cover'],
            'mean_k': float(res['best_cover']), 'median_k': float(res['best_cover']), 'worst_k': res['best_cover'],
            'feasible_rate': 1.0 if res['is_feasible'] else 0.0,
            'best_violation': 0, 'mean_violation': 0.0,
            'fitness_evaluations': graph.n_nodes,
            'generations': 0,
            'runtime': elapsed,
            'time_to_first_feasible': elapsed if res['is_feasible'] else None,
            'time_to_best': elapsed,
            'status': 'SUCCESS' if res['is_feasible'] else 'FAILED'
        }
        return run_record, [], []

    # Nhánh Tiến hóa + AOS
    env = SClubEnvironmentBai2(graph, config, tracker)
    agent = create_agent_bai2(condition, config)

    state = env.reset()
    done = False
    step_count = 0

    while not done and step_count < config.max_generations:
        step_count += 1
        action = agent.select_action(state, train=True)
        next_state, reward, done, info = env.step(action)

        if condition == "PPO-AOS":
            agent.store_transition(state, action, reward, done)
            if step_count % config.update_interval == 0:
                agent.update(next_state)

        state = next_state

    total_runtime = time.perf_counter() - start_wall
    all_k = [ind.num_clubs for ind in env.population.individuals if ind.is_feasible]
    if not all_k:
        all_k = [env.best_overall_individual.num_clubs]

    run_record = {
        'dataset': dataset_name,
        'graph_type': graph_type,
        'n': v_cnt,
        'm': e_cnt,
        'density': density,
        's': config.s_club_threshold,
        'method': condition,
        'seed': seed,
        'best_k': env.best_overall_individual.num_clubs,
        'final_k': env.population.best_individual.num_clubs,
        'mean_k': float(np.mean(all_k)),
        'median_k': float(np.median(all_k)),
        'worst_k': int(np.max(all_k)),
        'feasible_rate': float(env.population.feasible_ratio),
        'best_violation': int(env.best_overall_individual.diameter_violation),
        'mean_violation': float(env.population.mean_violation),
        'fitness_evaluations': tracker.eval_count,
        'generations': step_count,
        'runtime': total_runtime,
        'time_to_first_feasible': tracker.time_to_first_feasible if tracker.time_to_first_feasible is not None else total_runtime,
        'time_to_best': tracker.time_to_best if tracker.time_to_best is not None else total_runtime,
        'status': 'SUCCESS'
    }

    return run_record, tracker.anytime_logs, tracker.op_history
