"""
operators/mutation.py — Các toán tử đột biến chuyên biệt cho bài toán Minimum s-Club Cover.
Bao gồm 3 toán tử chuẩn từ bài báo của Thầy, được tối ưu hóa thông minh:
  1. Tách club (Split club) — Ưu tiên sửa các club vi phạm đường kính.
  2. Gộp hai club (Merge clubs) — Ưu tiên gộp các cặp club kề nhau tạo thành s-club hợp lệ.
  3. Chuyển đỉnh (Transfer vertex) — Ưu tiên chuyển đỉnh từ club nhỏ để xóa sổ club dư thừa.
"""
import numpy as np
from problem.graph import SClubGraph
from problem.individual import Individual


def split_club_mutation(ind: Individual, graph: SClubGraph) -> Individual:
    """
    Toán tử Đột biến Tách club:
    Ưu tiên chọn club vi phạm đường kính để tách thành 2 club con,
    giúp phục hồi tính khả thi của s-club.
    """
    child = ind.copy()
    clubs = child.get_clubs()
    if not clubs:
        return child

    candidate_clubs = [c_id for c_id, nodes in clubs.items() if len(nodes) >= 3]
    if not candidate_clubs:
        # Nếu không có club nào >= 3 đỉnh, tìm các club vi phạm
        violating_clubs = [
            c_id for c_id, nodes in clubs.items()
            if len(nodes) > 1 and not graph.is_s_club(nodes)
        ]
        if not violating_clubs:
            return child
        chosen_c = np.random.choice(violating_clubs)
    else:
        # Ưu tiên chọn club vi phạm đường kính
        violating_clubs = [
            c_id for c_id in candidate_clubs 
            if not graph.is_s_club(clubs[c_id])
        ]
        if violating_clubs:
            chosen_c = np.random.choice(violating_clubs)
        else:
            # Nếu không có vi phạm, chọn các club có kích thước lớn
            max_size = max(len(clubs[c_id]) for c_id in candidate_clubs)
            large_clubs = [c_id for c_id in candidate_clubs if len(clubs[c_id]) == max_size]
            chosen_c = np.random.choice(large_clubs)

    nodes = clubs[chosen_c]
    np.random.shuffle(nodes)
    split_point = max(1, len(nodes) // 2)
    new_club_nodes = nodes[split_point:]

    new_label = int(np.max(child._x)) + 1 if len(child._x) > 0 else 1
    for v in new_club_nodes:
        child._x[v] = new_label

    child.relabel_compact()
    return child


def merge_clubs_mutation(ind: Individual, graph: SClubGraph) -> Individual:
    """
    Toán tử Đột biến Hợp nhất hai club:
    1. Ưu tiên tìm cặp club kề nhau mà khi gộp lại vẫn thỏa mãn diam <= s (Feasible Merge).
    2. Nếu không có, gộp 2 club có cạnh nối trực tiếp.
    3. Fallback: Gộp 2 club ngẫu nhiên.
    """
    child = ind.copy()
    clubs = child.get_clubs()
    c_ids = list(clubs.keys())
    if len(c_ids) < 2:
        return child

    n = graph.n_nodes
    sample_nodes = np.random.permutation(n)
    merged = False

    # 1. Tìm cặp club kề nhau mà khi gộp lại vẫn là s-club hoàn hảo (lấy mẫu nhanh 10 đỉnh)
    for u in sample_nodes[:min(n, 10)]:
        u_club = child._x[u]
        if u_club not in clubs:
            continue
        for v in graph.get_neighbors(u):
            v_club = child._x[v]
            if u_club != v_club and v_club in clubs:
                combined_nodes = clubs[u_club] + clubs[v_club]
                if graph.is_s_club(combined_nodes):
                    for node in clubs[v_club]:
                        child._x[node] = u_club
                    merged = True
                    break
        if merged:
            break

    # 2. Nếu không có cặp hoàn hảo, gộp 2 club có cạnh nối
    if not merged:
        for u in sample_nodes[:min(n, 8)]:
            u_club = child._x[u]
            if u_club not in clubs:
                continue
            for v in graph.get_neighbors(u):
                v_club = child._x[v]
                if u_club != v_club and v_club in clubs:
                    for node in clubs[v_club]:
                        child._x[node] = u_club
                    merged = True
                    break
            if merged:
                break

    # 3. Fallback gộp 2 club ngẫu nhiên
    if not merged:
        c1, c2 = np.random.choice(c_ids, size=2, replace=False)
        for v in clubs[c2]:
            child._x[v] = c1

    child.relabel_compact()
    return child


def transfer_vertex_mutation(ind: Individual, graph: SClubGraph) -> Individual:
    """
    Toán tử Đột biến Chuyển đỉnh:
    Ưu tiên chuyển đỉnh từ các club nhỏ (1-2 đỉnh) sang club láng giềng kề,
    giúp triệt tiêu các club thừa và giảm số lượng cover nhanh chóng.
    """
    child = ind.copy()
    n = graph.n_nodes
    if n == 0:
        return child

    clubs = child.get_clubs()
    # Ưu tiên chọn đỉnh từ club nhỏ nhất để xóa sổ club đó
    small_clubs = [c_id for c_id, nodes in clubs.items() if len(nodes) <= 2]
    if small_clubs and np.random.rand() < 0.7:
        c_target = np.random.choice(small_clubs)
        v = np.random.choice(clubs[c_target])
    else:
        v = np.random.randint(0, n)

    neighbors = graph.get_neighbors(v)
    if neighbors:
        diff_nbrs = [nbr for nbr in neighbors if child._x[nbr] != child._x[v]]
        if diff_nbrs:
            nbr = np.random.choice(diff_nbrs)
            child._x[v] = child._x[nbr]
        else:
            child._x[v] = child._x[np.random.choice(neighbors)]
    else:
        c_part = child.get_c_part()
        if c_part:
            child._x[v] = np.random.choice(c_part)

    child.relabel_compact()
    return child
