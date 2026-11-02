"""
operators/crossover.py — Toán tử lai ghép cấu trúc (Structural / Falkenauer Grouping Crossover).
Kế thừa trực tiếp từ bài báo của Thầy và Falkenauer (1994).
"""
import numpy as np
from problem.graph import SClubGraph
from problem.individual import Individual


def structural_crossover(parent1: Individual, parent2: Individual, graph: SClubGraph) -> Individual:
    """
    Toán tử lai ghép nhóm Falkenauer Grouping Crossover (Chuẩn bài báo của Thầy):
    1. Chọn ngẫu nhiên một tập các club từ Cha mẹ 1 và truyền nguyên vẹn sang Con.
    2. Bổ sung các club từ Cha mẹ 2 cho các đỉnh chưa được gán.
    3. Gán tham lam các đỉnh còn sót lại vào các club láng giềng phù hợp.
    """
    n = graph.n_nodes
    if n <= 0:
        return parent1.copy()

    child_x = np.full(n, -1, dtype=np.int32)
    clubs1 = parent1.get_clubs()
    c_keys1 = list(clubs1.keys())

    if len(c_keys1) > 1:
        # Chọn ngẫu nhiên một tập các club từ cha mẹ 1
        n_select = max(1, int(len(c_keys1) * np.random.uniform(0.3, 0.7)))
        selected_clubs1 = np.random.choice(c_keys1, size=n_select, replace=False)
        for new_label, c_id in enumerate(selected_clubs1):
            for v in clubs1[c_id]:
                child_x[v] = new_label
        next_label = n_select
    else:
        child_x = parent1._x.copy()
        next_label = len(np.unique(child_x))

    # Bổ sung từ Cha mẹ 2 cho các đỉnh chưa được gán
    clubs2 = parent2.get_clubs()
    for c_id, nodes in clubs2.items():
        unassigned_in_c = [v for v in nodes if child_x[v] == -1]
        if len(unassigned_in_c) > 0:
            # Nếu đa số đỉnh trong club này chưa gán, tạo club mới cho chúng
            if len(unassigned_in_c) >= len(nodes) * 0.5:
                for v in unassigned_in_c:
                    child_x[v] = next_label
                next_label += 1

    # Xử lý các đỉnh còn sót lại chưa gán vào club nào
    unassigned_nodes = np.where(child_x == -1)[0]
    for v in unassigned_nodes:
        neighbors = graph.get_neighbors(v)
        assigned_nbr_clubs = [int(child_x[nbr]) for nbr in neighbors if child_x[nbr] != -1]
        if assigned_nbr_clubs:
            # Chọn club xuất hiện nhiều nhất trong số các đỉnh láng giềng kề
            unique_c, counts = np.unique(assigned_nbr_clubs, return_counts=True)
            best_c = unique_c[np.argmax(counts)]
            child_x[v] = best_c
        else:
            # Nếu không có láng giềng nào đã gán, mở club mới
            child_x[v] = next_label
            next_label += 1

    child = Individual(n, parent1.k_max, assignment=child_x)
    child.relabel_compact()
    return child
