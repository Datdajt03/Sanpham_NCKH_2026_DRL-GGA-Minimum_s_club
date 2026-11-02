"""
problem/population.py — Quản lý quần thể và các chỉ số thống kê vĩ mô.
"""
import numpy as np
from typing import List, Dict, Any
from .graph import SClubGraph
from .individual import Individual
from .fitness import evaluate_individual


class Population:
    """
    Quản lý tập hợp các cá thể trong một thế hệ tiến hóa.
    Tính toán các chỉ số vĩ mô phục vụ cho RL State Vector.
    """
    def __init__(self, size: int, n_nodes: int, k_max: int = None):
        self.size = size
        self.n_nodes = n_nodes
        self.k_max = k_max if k_max is not None else max(1, n_nodes // 2)
        
        self.individuals: List[Individual] = [
            Individual(n_nodes, self.k_max) for _ in range(size)
        ]
        
        self.best_individual: Individual = None
        self.best_fitness: float = float('inf')
        self.avg_fitness: float = float('inf')
        self.feasible_ratio: float = 0.0
        self.mean_violation: float = 0.0
        self.diversity: float = 0.0

    def evaluate_all(self, graph: SClubGraph, penalty_lambda: float = 10.0):
        """Đánh giá toàn bộ cá thể chưa được đánh giá trong quần thể và cập nhật các chỉ số thống kê."""
        for ind in self.individuals:
            if ind.fitness == float('inf'):
                evaluate_individual(ind, graph, penalty_lambda)
        self.update_statistics()

    def update_statistics(self):
        """Cập nhật các chỉ số thống kê vĩ mô từ các cá thể đã được đánh giá (không tính lại đồ thị)."""
        fitnesses = [ind.fitness for ind in self.individuals]
        violations = [ind.diameter_violation for ind in self.individuals]
        feasible_count = sum(1 for ind in self.individuals if ind.is_feasible)

        self.best_individual = self.individuals[0].copy()
        self.best_fitness = self.individuals[0].fitness

        for ind in self.individuals[1:]:
            f = ind.fitness
            is_feas = ind.is_feasible
            if f < self.best_fitness:
                self.best_individual = ind.copy()
                self.best_fitness = f
            elif f == self.best_fitness and is_feas and not self.best_individual.is_feasible:
                self.best_individual = ind.copy()
                self.best_fitness = f

        self.avg_fitness = float(np.mean(fitnesses)) if fitnesses else float('inf')
        self.feasible_ratio = float(feasible_count / self.size) if self.size > 0 else 0.0
        self.mean_violation = float(np.mean(violations)) if violations else 0.0
        self.diversity = self.compute_diversity()


    def compute_diversity(self, sample_pairs: int = 30) -> float:
        """
        Tính độ đa dạng của quần thể dựa trên khoảng cách Hamming trung bình
        giữa các cặp cá thể ngẫu nhiên.
        """
        if self.size < 2:
            return 0.0

        diff_fractions = []
        n_pairs = min(sample_pairs, self.size * (self.size - 1) // 2)
        
        for _ in range(n_pairs):
            i, j = np.random.choice(self.size, size=2, replace=False)
            ind1, ind2 = self.individuals[i], self.individuals[j]
            # Tỷ lệ đỉnh có nhãn khác nhau
            diff = np.mean(ind1._x != ind2._x)
            diff_fractions.append(diff)

        return float(np.mean(diff_fractions)) if diff_fractions else 0.0

    def get_summary(self) -> Dict[str, Any]:
        """Trả về tóm tắt trạng thái của quần thể."""
        return {
            'best_fitness': self.best_fitness,
            'avg_fitness': self.avg_fitness,
            'feasible_ratio': self.feasible_ratio,
            'mean_violation': self.mean_violation,
            'diversity': self.diversity,
            'best_num_clubs': self.best_individual.num_clubs if self.best_individual else self.k_max,
            'best_is_feasible': self.best_individual.is_feasible if self.best_individual else False,
        }
