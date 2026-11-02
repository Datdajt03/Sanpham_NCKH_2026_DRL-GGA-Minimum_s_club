"""
operators/repair.py — Toán tử sửa nghiệm thông minh bảo toàn cấu trúc s-club với tốc độ cao.
"""
import numpy as np
from problem.graph import SClubGraph
from problem.individual import Individual


def repair_individual(ind: Individual, graph: SClubGraph, s: int) -> Individual:
    """
    Toán tử sửa nghiệm thông minh Greedy Reassignment Repair:
    1. Kiểm tra từng club xem có vi phạm tính liên thông hoặc đường kính > s.
    2. Nếu vi phạm: Lần lượt bóc đỉnh có bậc nội bộ nhỏ nhất (min internal degree).
    3. Với mỗi đỉnh bị bóc ra:
       - Thử tham lam gán vào các club láng giềng đã có mà khi thêm đỉnh vào vẫn thỏa mãn s-club.
       - Chỉ khi không thể ghép vào bất kỳ club láng giềng nào mới tạo club mới.
    4. Quét co cụm (Compaction pass): Thử gộp các club đơn/nhỏ vào các club lớn tương thích.
    5. Đảm bảo 100% nghiệm sau khi sửa đều khả thi (feasible, diam <= s).
    """
    if ind.n_nodes <= 0:
        return ind

    child = ind.copy()
    clubs = child.get_clubs()
    next_label = int(np.max(child._x)) + 1 if len(child._x) > 0 else 0
    popped_vertices = []

    for c_id, nodes in list(clubs.items()):
        k = len(nodes)
        if k <= 1:
            continue

        if k == 2:
            if not graph.adj_matrix[nodes[0], nodes[1]]:
                popped_v = nodes[1]
                popped_vertices.append((popped_v, c_id))
                clubs[c_id].remove(popped_v)
            continue

        idx = np.array(nodes, dtype=np.intp)
        A_S = graph.adj_matrix[idx[:, None], idx]
        M = A_S.copy()
        np.fill_diagonal(M, 1)

        # Kiểm tra nhanh s-club
        if s == 2 and np.all((M @ M) > 0):
            continue
        elif s != 2 and np.all(np.linalg.matrix_power(M, s) > 0):
            continue

        curr_nodes = list(nodes)
        while len(curr_nodes) > 1:
            M = A_S.copy()
            np.fill_diagonal(M, 1)
            if s == 2 and np.all((M @ M) > 0):
                break
            elif s != 2 and np.all(np.linalg.matrix_power(M, s) > 0):
                break

            degs = A_S.sum(axis=1)
            min_idx = int(np.argmin(degs))
            popped_v = curr_nodes.pop(min_idx)
            popped_vertices.append((popped_v, c_id))
            A_S = np.delete(np.delete(A_S, min_idx, axis=0), min_idx, axis=1)

        clubs[c_id] = curr_nodes
        for v in curr_nodes:
            child._x[v] = c_id

    # Gán tham lam các đỉnh bị bóc ra vào các club hợp lệ hiện có
    for popped_v, orig_cid in popped_vertices:
        neighbors = graph.get_neighbors(popped_v)
        assigned = False

        # Ưu tiên các club láng giềng kề có nhiều kết nối nhất với popped_v
        neighbor_club_counts = {}
        for nbr in neighbors:
            nbr_cid = int(child._x[nbr])
            if nbr_cid != -1 and nbr_cid in clubs and len(clubs[nbr_cid]) > 0:
                neighbor_club_counts[nbr_cid] = neighbor_club_counts.get(nbr_cid, 0) + 1

        sorted_cand_clubs = sorted(neighbor_club_counts.keys(), key=lambda c: neighbor_club_counts[c], reverse=True)

        for cand_cid in sorted_cand_clubs:
            candidate_members = clubs[cand_cid] + [popped_v]
            if graph.is_s_club(candidate_members):
                child._x[popped_v] = cand_cid
                clubs[cand_cid].append(popped_v)
                assigned = True
                break

        if not assigned:
            # Nếu không ghép được vào club láng giềng nào, mở club mới
            child._x[popped_v] = next_label
            clubs[next_label] = [popped_v]
            next_label += 1

    # Quét co cụm nhanh (Fast Compaction Pass cho các club nhỏ <= 2 đỉnh)
    # Tối ưu hóa cực đại: CHỈ duyệt các club láng giềng có kết nối cạnh thực tế thay vì O(K^2)
    current_c_ids = [c for c, members in clubs.items() if 0 < len(members) <= 2]
    for small_cid in current_c_ids:
        small_members = clubs.get(small_cid, [])
        if not small_members:
            continue

        # Tìm các club láng giềng kề có kết nối trực tiếp với ít nhất 1 đỉnh trong small_members
        cand_target_cids = set()
        for v in small_members:
            for nbr in graph.get_neighbors(v):
                nbr_cid = int(child._x[nbr])
                if nbr_cid != -1 and nbr_cid != small_cid and nbr_cid in clubs and len(clubs[nbr_cid]) > 0:
                    cand_target_cids.add(nbr_cid)

        # Thử ghép toàn bộ small_members vào các club láng giềng kề
        for target_cid in cand_target_cids:
            target_members = clubs.get(target_cid, [])
            if not target_members:
                continue
            combined = target_members + small_members
            if graph.is_s_club(combined):
                for v in small_members:
                    child._x[v] = target_cid
                target_members.extend(small_members)
                clubs[small_cid] = []
                break

    child.relabel_compact()
    child.is_feasible = True
    child.diameter_violation = 0.0
    child.fitness = float(child.num_clubs)
    return child

