"""
environment/env.py — Môi trường tương tác chuẩn Gym kết nối EA và PPO.
"""
import numpy as np
from typing import Tuple, Dict, Any, List

from configs.config import ExperimentConfig
from problem.graph import SClubGraph
from problem.individual import Individual, create_greedy_bfs_individual
from problem.population import Population
from operators.crossover import structural_crossover
from operators.mutation import split_club_mutation, merge_clubs_mutation, transfer_vertex_mutation
from operators.repair import repair_individual
from operators.selection import tournament_selection, survivor_selection
from rl.state import extract_state
from rl.reward import compute_reward


class SClubEnvironment:
    """
    Môi trường tiến hóa giải bài toán Minimum s-Club Cover (Gym-compatible interface).
    Mỗi bước step(action) là 1 thế hệ tiến hóa áp dụng toán tử do PPO lựa chọn.
    """
    def __init__(self, graph: SClubGraph, config: ExperimentConfig):
        self.graph = graph
        self.config = config
        
        self.population: Population = None
        self.generation: int = 0
        self.stagnation_count: int = 0
        
        self.best_overall_individual: Individual = None
        self.best_overall_fitness: float = float('inf')
        
        self.prev_best_f: float = float('inf')
        self.prev_feas_ratio: float = 0.0
        self.prev_violation: float = float('inf')

    def reset(self) -> np.ndarray:
        """Khởi tạo lại môi trường cho một Episode mới (Đảm bảo 100% cá thể hợp lệ ngay từ gen 0)."""
        self.population = Population(
            size=self.config.pop_size, 
            n_nodes=self.graph.n_nodes
        )
        # Khởi tạo 50% cá thể bằng Randomized BFS Seeding chất lượng cao
        n_greedy = max(1, self.config.pop_size // 2)
        for i in range(n_greedy):
            self.population.individuals[i] = create_greedy_bfs_individual(
                self.graph, self.config.s_club_threshold
            )

        for i in range(len(self.population.individuals)):
            self.population.individuals[i] = repair_individual(
                self.population.individuals[i], 
                self.graph, 
                self.config.s_club_threshold
            )
        self.population.update_statistics()

        self.generation = 0
        self.stagnation_count = 0
        self.best_overall_individual = self.population.best_individual.copy()
        self.best_overall_fitness = self.population.best_fitness

        self.prev_best_f = self.population.best_fitness
        self.prev_feas_ratio = self.population.feasible_ratio
        self.prev_violation = self.population.mean_violation

        state = extract_state(
            population=self.population,
            stagnation_count=self.stagnation_count,
            stagnation_limit=self.config.stagnation_limit,
            n_nodes=self.graph.n_nodes,
            s=self.config.s_club_threshold
        )
        return state

    def step(self, action: int) -> Tuple[np.ndarray, float, bool, Dict[str, Any]]:
        """
        Thực hiện một bước tiến hóa theo toán tử được chọn:
          action = 0: Structural Crossover
          action = 1: Feasibility-preserving Mutation (Merge clubs / Transfer vertex)
          action = 2: Diversification Mutation (Split clubs / Transfer vertex)
          action = 3: Standard Fixed GGA (Thuật toán di truyền nhóm chuẩn bài báo của Thầy: pc=0.90, pm=0.05)
        """
        offspring_list: List[Individual] = []
        n_offspring = self.config.offspring_size

        for _ in range(n_offspring):
            if action == 0:
                # 1. Structural Crossover
                p1 = tournament_selection(self.population, self.config.tournament_size)
                p2 = tournament_selection(self.population, self.config.tournament_size)
                child = structural_crossover(p1, p2, self.graph)
            elif action == 1:
                # 2. Feasibility-preserving Mutation
                p = tournament_selection(self.population, self.config.tournament_size)
                if np.random.rand() < 0.6:
                    child = merge_clubs_mutation(p, self.graph)
                else:
                    child = transfer_vertex_mutation(p, self.graph)
            elif action == 2:
                # 3. Diversification Mutation
                p = tournament_selection(self.population, self.config.tournament_size)
                if self.population.feasible_ratio >= 0.99 and self.population.best_fitness <= 2.0:
                    child = merge_clubs_mutation(p, self.graph)
                elif np.random.rand() < 0.6:
                    child = split_club_mutation(p, self.graph)
                else:
                    child = transfer_vertex_mutation(p, self.graph)
            else:
                # 4. Standard Fixed GGA (Chuẩn bài báo của Thầy: pc = 0.90, pm = 0.05)
                p1 = tournament_selection(self.population, self.config.tournament_size)
                if np.random.rand() < self.config.crossover_rate:
                    p2 = tournament_selection(self.population, self.config.tournament_size)
                    child = structural_crossover(p1, p2, self.graph)
                else:
                    child = p1.copy()

                if np.random.rand() < self.config.mutation_rate:
                    m_type = np.random.randint(0, 3)
                    if m_type == 0:
                        child = split_club_mutation(child, self.graph)
                    elif m_type == 1:
                        child = merge_clubs_mutation(child, self.graph)
                    else:
                        child = transfer_vertex_mutation(child, self.graph)

            # Sửa nghiệm để đảm bảo 100% hợp lệ tính khả thi s-club
            child = repair_individual(child, self.graph, self.config.s_club_threshold)
            offspring_list.append(child)

        # Chọn lọc cá thể sống sót (Survivor Selection)
        survivor_selection(
            population=self.population,
            offspring=offspring_list,
            pop_size=self.config.pop_size,
            graph=self.graph,
            penalty_lambda=self.config.penalty_lambda
        )

        curr_best_f = self.population.best_fitness
        curr_feas_ratio = self.population.feasible_ratio
        curr_violation = self.population.mean_violation

        # Cập nhật trì trệ (Stagnation)
        stagnated = True
        if curr_best_f < self.best_overall_fitness:
            self.best_overall_fitness = curr_best_f
            self.best_overall_individual = self.population.best_individual.copy()
            self.stagnation_count = 0
            stagnated = False
        else:
            self.stagnation_count += 1

        # Tính phần thưởng (Reward)
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

        # Kiểm tra điều kiện kết thúc Episode
        done = (self.generation >= self.config.max_generations) or \
               (self.stagnation_count >= self.config.stagnation_limit)

        next_state = extract_state(
            population=self.population,
            stagnation_count=self.stagnation_count,
            stagnation_limit=self.config.stagnation_limit,
            n_nodes=self.graph.n_nodes,
            s=self.config.s_club_threshold
        )

        info = {
            'generation': self.generation,
            'best_fitness': self.best_overall_fitness,
            'cover_size': self.get_cover_size(),
            'is_feasible': self.best_overall_individual.is_feasible if self.best_overall_individual else False,
            'stagnation': self.stagnation_count
        }

        return next_state, reward, done, info

    def get_cover_size(self) -> int:
        """Trả về số lượng s-club của nghiệm tốt nhất toàn cục."""
        if self.best_overall_individual is not None:
            return self.best_overall_individual.num_clubs
        return self.graph.n_nodes

    def is_fully_covered(self) -> bool:
        """Kiểm tra nghiệm tốt nhất có bao phủ 100% đỉnh và hợp lệ không."""
        if self.best_overall_individual is None:
            return False
        return self.best_overall_individual.is_feasible

    def validate_solution(self) -> bool:
        """Xác thực nghiêm ngặt từng club trong nghiệm tốt nhất có phải là s-club hợp lệ không."""
        if self.best_overall_individual is None:
            return False
        clubs = self.best_overall_individual.get_clubs()
        all_nodes = set()
        for nodes in clubs.values():
            all_nodes.update(nodes)
            if not self.graph.is_s_club(nodes):
                return False
        return len(all_nodes) == self.graph.n_nodes