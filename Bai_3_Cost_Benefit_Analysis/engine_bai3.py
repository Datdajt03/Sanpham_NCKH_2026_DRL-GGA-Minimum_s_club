"""
Bai_3_Cost_Benefit_Analysis/engine_bai3.py — Môi trường có Bộ đếm thời gian vi mô (Microsecond Profiler).
Bóc tách chính xác runtime của từng thành phần: BFS check, Repair, Operator, PPO Inference, PPO Backprop Update và Memory Peak.
"""
import time
import psutil
import torch
import numpy as np
from typing import Dict, Any, List, Tuple

from problem.graph import SClubGraph
from problem.individual import Individual
from problem.population import Population
from problem.fitness import evaluate_individual
from operators.crossover import structural_crossover
from operators.mutation import split_club_mutation, merge_clubs_mutation, transfer_vertex_mutation
from operators.repair import repair_individual
from operators.selection import tournament_selection, survivor_selection
from rl.state import extract_state
from rl.reward import compute_reward
from .config_bai3 import Bai3Config


class MicroCostProfilerBai3:
    """Bộ đếm vi mô ghi nhận chi phí thời gian và bộ nhớ từng dòng lệnh."""
    def __init__(self):
        self.runtime_total = 0.0
        self.runtime_fitness_diameter = 0.0
        self.runtime_repair = 0.0
        self.runtime_operator = 0.0
        self.runtime_ppo_inference = 0.0
        self.runtime_ppo_update = 0.0
        
        self.count_ppo_updates = 0
        self.count_operator_calls = 0
        self.fitness_evaluations = 0
        self.memory_peak_mb = 0.0
        
        self.time_budget_snapshots = {}

    def update_memory_peak(self):
        try:
            mem = psutil.Process().memory_info().rss / (1024 * 1024)
            if torch.cuda.is_available():
                gpu_mem = torch.cuda.max_memory_allocated() / (1024 * 1024)
                mem = max(mem, gpu_mem)
            self.memory_peak_mb = max(self.memory_peak_mb, mem)
        except Exception:
            pass


class SClubEnvironmentBai3:
    """Môi trường tiến hóa tích hợp bộ phân rã runtime cho Bài 3."""
    def __init__(self, graph: SClubGraph, config: Bai3Config, profiler: MicroCostProfilerBai3):
        self.graph = graph
        self.config = config
        self.profiler = profiler
        
        self.lambda_val = config.penalty_lambda if config.penalty_lambda > 0 else (graph.n_nodes + 1)
        self.population = None
        self.generation = 0
        self.stagnation_count = 0
        
        self.best_overall_individual = None
        self.best_overall_fitness = float('inf')
        
        self.prev_best_f = float('inf')
        self.prev_feas_ratio = 0.0
        self.prev_violation = float('inf')
        self.start_wall_time = 0.0

    def reset(self) -> np.ndarray:
        self.start_wall_time = time.perf_counter()
        self.population = Population(size=self.config.pop_size, n_nodes=self.graph.n_nodes)
        
        t0 = time.perf_counter()
        for ind in self.population.individuals:
            evaluate_individual(ind, self.graph, self.lambda_val)
            self.profiler.fitness_evaluations += 1
        self.profiler.runtime_fitness_diameter += (time.perf_counter() - t0)

        self.population.update_statistics()
        self.best_overall_individual = self.population.best_individual.copy()
        self.best_overall_fitness = self.population.best_fitness
        
        self.prev_best_f = self.best_overall_fitness
        self.prev_feas_ratio = self.population.feasible_ratio
        self.prev_violation = self.population.mean_violation
        self.generation = 0
        self.stagnation_count = 0

        state = extract_state(
            population=self.population,
            stagnation_count=self.stagnation_count,
            stagnation_limit=self.config.stagnation_limit,
            n_nodes=self.graph.n_nodes,
            s=self.config.s_club_threshold
        )
        return state

    def step(self, action: int) -> Tuple[np.ndarray, float, bool, Dict[str, Any]]:
        offspring_list = []
        n_offspring = self.config.offspring_size

        for _ in range(n_offspring):
            t_op = time.perf_counter()
            if action == 0:
                p1 = tournament_selection(self.population, self.config.tournament_size)
                p2 = tournament_selection(self.population, self.config.tournament_size)
                child = structural_crossover(p1, p2, self.graph)
            elif action == 1:
                p = tournament_selection(self.population, self.config.tournament_size)
                if np.random.rand() < 0.6:
                    child = merge_clubs_mutation(p, self.graph)
                else:
                    child = transfer_vertex_mutation(p, self.graph)
            else:
                p = tournament_selection(self.population, self.config.tournament_size)
                if self.population.feasible_ratio >= 0.99 and self.population.best_fitness <= 2.0:
                    child = merge_clubs_mutation(p, self.graph)
                elif np.random.rand() < 0.6:
                    child = split_club_mutation(p, self.graph)
                else:
                    child = transfer_vertex_mutation(p, self.graph)
            self.profiler.runtime_operator += (time.perf_counter() - t_op)
            self.profiler.count_operator_calls += 1

            t_rep = time.perf_counter()
            child = repair_individual(child, self.graph, self.config.s_club_threshold)
            self.profiler.runtime_repair += (time.perf_counter() - t_rep)

            t_fit = time.perf_counter()
            evaluate_individual(child, self.graph, self.lambda_val)
            self.profiler.runtime_fitness_diameter += (time.perf_counter() - t_fit)
            self.profiler.fitness_evaluations += 1

            offspring_list.append(child)

        survivor_selection(
            population=self.population,
            offspring=offspring_list,
            pop_size=self.config.pop_size,
            graph=self.graph,
            penalty_lambda=self.lambda_val
        )

        curr_best_f = self.population.best_fitness
        curr_feas_ratio = self.population.feasible_ratio
        curr_violation = self.population.mean_violation

        stagnated = True
        if curr_best_f < self.best_overall_fitness:
            self.best_overall_fitness = curr_best_f
            self.best_overall_individual = self.population.best_individual.copy()
            self.stagnation_count = 0
            stagnated = False
        else:
            self.stagnation_count += 1

        reward = compute_reward(
            prev_best_f=self.prev_best_f,
            curr_best_f=curr_best_f,
            prev_feas_ratio=self.prev_feas_ratio,
            curr_feas_ratio=curr_feas_ratio,
            prev_violation=self.prev_violation,
            curr_violation=curr_violation,
            stagnated=stagnated
        )

        self.prev_best_f = curr_best_f
        self.prev_feas_ratio = curr_feas_ratio
        self.prev_violation = curr_violation
        self.generation += 1

        done = (self.generation >= self.config.max_generations) or (self.stagnation_count >= self.config.stagnation_limit)

        next_state = extract_state(
            population=self.population,
            stagnation_count=self.stagnation_count,
            stagnation_limit=self.config.stagnation_limit,
            n_nodes=self.graph.n_nodes,
            s=self.config.s_club_threshold
        )

        cur_elapsed = time.perf_counter() - self.start_wall_time
        for b_sec in self.config.time_budgets_sec:
            if b_sec not in self.profiler.time_budget_snapshots and cur_elapsed >= b_sec:
                self.profiler.time_budget_snapshots[b_sec] = self.best_overall_individual.num_clubs

        self.profiler.update_memory_peak()

        info = {
            'best_k': self.best_overall_individual.num_clubs,
            'is_feasible': self.best_overall_individual.is_feasible,
            'generation': self.generation
        }
        return next_state, reward, done, info
