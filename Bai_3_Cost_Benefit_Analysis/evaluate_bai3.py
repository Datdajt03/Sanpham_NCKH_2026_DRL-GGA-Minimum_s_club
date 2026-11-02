"""
Bai_3_Cost_Benefit_Analysis/evaluate_bai3.py — Chạy thực nghiệm bóc tách chi phí tính toán cho Bài 3.
"""
import os
import time
import random
import torch
import numpy as np
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
from .config_bai3 import Bai3Config
from .engine_bai3 import MicroCostProfilerBai3, SClubEnvironmentBai3


def set_seed(seed: int):
    random.seed(seed)
    np.random.seed(seed)
    torch.manual_seed(seed)
    if torch.cuda.is_available():
        torch.cuda.manual_seed_all(seed)


def create_agent_bai3(condition: str, config: Bai3Config):
    exp_cfg = ExperimentConfig()
    exp_cfg.state_dim = config.state_dim
    exp_cfg.num_operators = config.num_operators
    exp_cfg.hidden_dim = config.hidden_dim
    exp_cfg.learning_rate = config.learning_rate
    exp_cfg.discount = config.discount
    exp_cfg.clip_eps = config.clip_eps
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


def run_single_seed_bai3(
    graph_path: str,
    dataset_name: str,
    graph_type: str,
    condition: str,
    seed: int,
    config: Bai3Config
) -> Tuple[Dict[str, Any], Dict[float, int]]:
    """Chạy 1 lượt và phân rã chính xác runtime từng micro-giây cho Bài 3."""
    set_seed(seed)
    raw_g = load_graph(graph_path)
    graph = SClubGraph(raw_g, s=config.s_club_threshold)
    v_cnt = graph.n_nodes
    e_cnt = graph.n_edges
    density = (2.0 * e_cnt) / (v_cnt * (v_cnt - 1)) if v_cnt > 1 else 0.0
    profiler = MicroCostProfilerBai3()

    start_wall = time.perf_counter()
    env = SClubEnvironmentBai3(graph, config, profiler)
    agent = create_agent_bai3(condition, config)

    state = env.reset()
    done = False
    step_count = 0

    while not done and step_count < config.max_generations:
        step_count += 1
        
        t_inf = time.perf_counter()
        action = agent.select_action(state, train=True)
        profiler.runtime_ppo_inference += (time.perf_counter() - t_inf)

        next_state, reward, done, info = env.step(action)

        if condition == "PPO-AOS":
            agent.store_transition(state, action, reward, done)
            if step_count % config.update_interval == 0:
                t_up = time.perf_counter()
                up_info = agent.update(next_state)
                profiler.runtime_ppo_update += (time.perf_counter() - t_up)
                if up_info is not None:
                    profiler.count_ppo_updates += 1

        state = next_state

    total_time = time.perf_counter() - start_wall
    profiler.runtime_total = total_time

    for b_sec in config.time_budgets_sec:
        if b_sec not in profiler.time_budget_snapshots:
            profiler.time_budget_snapshots[b_sec] = env.best_overall_individual.num_clubs

    cost_record = {
        'dataset': dataset_name,
        'graph_type': graph_type,
        'n': v_cnt,
        'm': e_cnt,
        'density': density,
        'method': condition,
        'seed': seed,
        'best_k': env.best_overall_individual.num_clubs,
        'runtime_total': profiler.runtime_total,
        'runtime_fitness_diameter': profiler.runtime_fitness_diameter,
        'runtime_repair': profiler.runtime_repair,
        'runtime_operator': profiler.runtime_operator,
        'runtime_ppo_inference': profiler.runtime_ppo_inference,
        'runtime_ppo_update': profiler.runtime_ppo_update,
        'number_of_ppo_updates': profiler.count_ppo_updates,
        'number_of_operator_calls': profiler.count_operator_calls,
        'fitness_evaluations': profiler.fitness_evaluations,
        'memory_peak_mb': profiler.memory_peak_mb
    }

    return cost_record, profiler.time_budget_snapshots
