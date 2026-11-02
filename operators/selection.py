"""
operators/selection.py — Các toán tử chọn lọc cha mẹ và chọn lọc sống sót (Survivor selection).
"""
import numpy as np
from typing import List
from problem.graph import SClubGraph
from problem.individual import Individual
from problem.population import Population
from problem.fitness import evaluate_individual


def tournament_selection(population: Population, k: int = 3) -> Individual:
    """
    Chọn lọc giải đấu (Tournament Selection):
    Chọn ngẫu nhiên k cá thể từ quần thể và trả về cá thể có fitness tốt nhất.
    """
    indices = np.random.choice(population.size, size=k, replace=False)
    best_ind = population.individuals[indices[0]]
    best_f = best_ind.fitness

    for idx in indices[1:]:
        cand = population.individuals[idx]
        if cand.fitness < best_f:
            best_f = cand.fitness
            best_ind = cand

    return best_ind


def survivor_selection(
    population: Population, 
    offspring: List[Individual], 
    pop_size: int, 
    graph: SClubGraph, 
    penalty_lambda: float = 10.0
):
    """
    Chọn lọc cá thể sống sót (Elitism / (μ + λ) Selection):
    Gộp quần thể hiện tại và thế hệ con, đánh giá và giữ lại 'pop_size' cá thể tốt nhất.
    """
    all_candidates = population.individuals + offspring
    
    for ind in all_candidates:
        if ind.fitness == float('inf'):
            evaluate_individual(ind, graph, penalty_lambda)

    # Sắp xếp theo fitness tăng dần (nhỏ = tốt hơn)
    all_candidates.sort(key=lambda x: (x.fitness, not x.is_feasible, x.num_clubs))
    
    # Cắt lấy pop_size cá thể tốt nhất và cập nhật thống kê siêu tốc
    population.individuals = [ind.copy() for ind in all_candidates[:pop_size]]
    population.update_statistics()

