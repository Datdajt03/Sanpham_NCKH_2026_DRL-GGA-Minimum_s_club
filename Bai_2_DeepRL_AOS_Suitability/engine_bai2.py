"""
Bai_2_DeepRL_AOS_Suitability/engine_bai2.py — Thu thập dữ liệu chi tiết cho Bài 2.
Theo dõi Anytime convergence curve, Operator distribution theo giai đoạn và Reward response.
"""
import time
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
from .config_bai2 import Bai2Config


class DetailedTrackerBai2:
    """Theo dõi quỹ đạo chi tiết từng thế hệ cho Bài 2."""
    def __init__(self, dataset_name: str, method: str, seed: int, total_nodes: int):
        self.dataset_name = dataset_name
        self.method = method
        self.seed = seed
        self.total_nodes = total_nodes
        
        self.anytime_logs = []
        self.op_history = []
        self.eval_count = 0
        self.time_to_first_feasible = None
        self.time_to_best = None
        self.best_k_overall = float('inf')
        self.start_time = 0.0

    def start(self):
        self.start_time = time.perf_counter()

    def record_step(
        self, 
        gen: int, 
        evals_added: int, 
        best_k: int, 
        feas_ratio: float, 
        violation: float,
        op_idx: int, 
        reward: float, 
        state_vec: np.ndarray,
        max_gen: int
    ):
        elapsed = time.perf_counter() - self.start_time
        self.eval_count += evals_added

        if feas_ratio >= 1.0 and self.time_to_first_feasible is None:
            self.time_to_first_feasible = elapsed

        if best_k < self.best_k_overall:
            self.best_k_overall = best_k
            self.time_to_best = elapsed

        stage_ratio = gen / max(1, max_gen)
        if stage_ratio <= 0.33:
            stage = "Early"
        elif stage_ratio <= 0.66:
            stage = "Mid"
        else:
            stage = "Late"

        self.op_history.append({
            'gen': gen,
            'op_idx': op_idx,
            'reward': reward,
            'stage': stage
        })

        self.anytime_logs.append({
            'dataset': self.dataset_name,
            'method': self.method,
            'seed': self.seed,
            'generation': gen,
            'evaluations': self.eval_count,
            'time_elapsed': elapsed,
            'best_so_far_k': best_k,
            'feas_ratio': feas_ratio,
            'violation': violation,
            'operator_chosen': op_idx,
            'reward': reward,
            'state_fmin': float(state_vec[0]),
            'state_favg': float(state_vec[1]),
            'state_rho': float(state_vec[2]),
            'state_phi': float(state_vec[3]),
            'state_tau': float(state_vec[4])
        })


class SClubEnvironmentBai2:
    """Môi trường mở rộng có tracker chi tiết cho Bài 2."""
    def __init__(self, graph: SClubGraph, config: Bai2Config, tracker: DetailedTrackerBai2):
        self.graph = graph
        self.config = config
        self.tracker = tracker
        
        self.lambda_val = config.penalty_lambda if config.penalty_lambda > 0 else (graph.n_nodes + 1)
        self.population = None
        self.generation = 0
        self.stagnation_count = 0
        
        self.best_overall_individual = None
        self.best_overall_fitness = float('inf')
        
        self.prev_best_f = float('inf')
        self.prev_feas_ratio = 0.0
        self.prev_violation = float('inf')

    def reset(self) -> np.ndarray:
        self.population = Population(size=self.config.pop_size, n_nodes=self.graph.n_nodes)
        
        # Đánh giá fitness ban đầu
        for ind in self.population.individuals:
            evaluate_individual(ind, self.graph, self.lambda_val)
            self.tracker.eval_count += 1

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

            child = repair_individual(child, self.graph, self.config.s_club_threshold)
            evaluate_individual(child, self.graph, self.lambda_val)
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
            stagnated=stagnated,
            alpha1=self.config.alpha1,
            alpha2=self.config.alpha2,
            alpha3=self.config.alpha3,
            alpha4=self.config.alpha4
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

        self.tracker.record_step(
            gen=self.generation,
            evals_added=n_offspring,
            best_k=self.best_overall_individual.num_clubs,
            feas_ratio=curr_feas_ratio,
            violation=curr_violation,
            op_idx=action,
            reward=reward,
            state_vec=next_state,
            max_gen=self.config.max_generations
        )

        info = {
            'best_k': self.best_overall_individual.num_clubs,
            'is_feasible': self.best_overall_individual.is_feasible,
            'generation': self.generation,
            'evaluations': self.tracker.eval_count
        }
        return next_state, reward, done, info
