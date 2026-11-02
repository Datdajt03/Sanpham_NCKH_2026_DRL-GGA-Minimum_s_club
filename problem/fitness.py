"""
problem/fitness.py — Đánh giá hàm thích nghi (Fitness) và ràng buộc s-club tốc độ cao.
"""
from typing import Tuple
from .graph import SClubGraph
from .individual import Individual


def evaluate_individual(
    ind: Individual, 
    graph: SClubGraph, 
    penalty_lambda: float = 10.0
) -> Tuple[float, bool, int, float]:
    """
    Đánh giá một cá thể theo công thức:
      Fitness(I) = |Clubs(I)| + λ * Total_Violation(I)
      
    Tối ưu hóa:
      - Fast-Path: Nếu cá thể đã được đánh giá hoặc đã repair hợp lệ -> Bỏ qua lập tức O(1).
      - Kiểm tra nhanh is_s_club: nếu thỏa mãn -> Violation = 0.0.
      - Chỉ khi không thỏa mãn mới tính chính xác mức độ vi phạm để áp dụng điểm phạt λ.
    """
    if ind.fitness != float('inf'):
        return ind.fitness, ind.is_feasible, ind.num_clubs, ind.diameter_violation

    clubs = ind.get_clubs()
    num_clubs = len(clubs)
    total_violation = 0.0

    for c_id, nodes in clubs.items():
        if graph.is_s_club(nodes):
            continue
            
        d = graph.get_subgraph_diameter(nodes)
        if d == -1:
            # Đồ thị con không liên thông → Phạt nặng theo số đỉnh
            total_violation += float(len(nodes))
        elif d > graph.s:
            # Đồ thị con liên thông nhưng vượt quá ngưỡng đường kính s
            total_violation += float(d - graph.s)

    is_feasible = (total_violation == 0.0)
    fitness = float(num_clubs) + penalty_lambda * total_violation

    # Cập nhật trực tiếp vào thuộc tính của cá thể
    ind.fitness = fitness
    ind.is_feasible = is_feasible
    ind.num_clubs = num_clubs
    ind.diameter_violation = total_violation

    return fitness, is_feasible, num_clubs, total_violation

