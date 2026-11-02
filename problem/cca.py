r"""
problem/cca.py — Cài đặt thuật toán Club-Cover-Approx (CCA).

Định vị khoa học:
  Baseline đối chứng văn hiến kinh điển trong bài báo gốc của R. Dondi et al. (2019) và bài báo của Thầy:
  "Covering a graph with clubs" (Journal of Graph Algorithms and Applications 2019).

Cơ chế hoạt động:
  1. Với s = 2r (đặc biệt s = 2, r = 1):
     Một hình cầu tâm v bán kính r (Closed r-hop Ball) B_r(v) = {u in V | d_G[B_r(v)](u, v) <= r}
     luôn thỏa mãn diam(G[B_r(v)]) <= 2r = s.
  2. Giai đoạn 1 (Greedy Dominating Center Selection):
     - Tập đỉnh chưa phủ ban đầu: U = V.
     - Trong khi U != rỗng: Chọn đỉnh tâm v tối đa hóa số lượng đỉnh chưa phủ bao bọc bởi B_r(v):
       v = argmax_v |B_r(v) \cap U|.
     - Bổ sung club B_r(v) vào tập phủ và cập nhật U <- U \ B_r(v).
  3. Giai đoạn 2 (Local Refinement & Redundant Pruning):
     - Loại bỏ các club dư thừa (Redundant Clubs) nếu mọi đỉnh của nó đã được phủ bởi các club khác.
     - Thử gộp các cặp club lân cận nếu hợp của chúng vẫn là 1 s-club hợp lệ.
  4. Cơ chế Đa khởi tạo (Multi-start Restarts) có Early Stopping:
     - Phá vỡ liên kết ngẫu nhiên dựa trên seed để khảo sát phân phối thống kê chuẩn xác qua 20 seeds.
"""
import time
import random
import numpy as np
from typing import List, Set, Dict, Any, Optional
from configs.config import ExperimentConfig
from problem.graph import SClubGraph


class CCASolver:
    """
    Bộ giải Club-Cover-Approx (CCA) tối ưu hóa tốc độ cao với tiền tính toán bán kính s/2.
    """
    def __init__(self, graph: SClubGraph, config: ExperimentConfig):
        self.graph = graph
        self.config = config
        self.s = config.s_club_threshold
        self.n_nodes = graph.n_nodes
        self.radius = max(1, self.s // 2)

        # Tiền tính toán các quả cầu bán kính r quanh từng đỉnh (r-hop ball)
        self.balls: List[List[int]] = []
        for v in range(self.n_nodes):
            # BFS tìm các đỉnh trong bán kính r từ v
            ball = self._get_r_ball(v, self.radius)
            self.balls.append(ball)

        self.degrees = np.array(graph.raw_graph.degree(), dtype=np.int32)

    def _get_r_ball(self, center: int, r: int) -> List[int]:
        """Tìm quả cầu cảm sinh bán kính r quanh đỉnh center luôn đảm bảo diam <= 2r <= s."""
        visited = {center}
        queue = [(center, 0)]
        while queue:
            curr, depth = queue.pop(0)
            if depth >= r:
                continue
            for nbr in self.graph.get_neighbors(curr):
                if nbr not in visited:
                    visited.add(nbr)
                    queue.append((nbr, depth + 1))
        return list(visited)

    def _prune_redundant_clubs(self, clubs: List[List[int]]) -> List[List[int]]:
        """Loại bỏ các club dư thừa nếu mọi đỉnh của nó đã được phủ bởi các club khác."""
        pruned = list(clubs)
        changed = True
        while changed:
            changed = False
            for i in range(len(pruned) - 1, -1, -1):
                other_nodes = set()
                for j in range(len(pruned)):
                    if j != i:
                        other_nodes.update(pruned[j])
                if set(pruned[i]).issubset(other_nodes):
                    pruned.pop(i)
                    changed = True
                    break
        return pruned

    def _merge_adjacent_clubs(self, clubs: List[List[int]]) -> List[List[int]]:
        """Thử gộp các cặp club nếu hợp của chúng vẫn là một s-club hợp lệ."""
        merged = list(clubs)
        changed = True
        passes = 0
        while changed and passes < 3:
            passes += 1
            changed = False
            n = len(merged)
            for i in range(n):
                for j in range(i + 1, n):
                    c1, c2 = merged[i], merged[j]
                    has_edge = any(self.graph.adj_matrix[u, v] for u in c1 for v in c2)
                    if not has_edge:
                        continue

                    combined = list(set(c1 + c2))
                    if self.graph.is_s_club(combined):
                        merged[i] = combined
                        merged.pop(j)
                        changed = True
                        break
                if changed:
                    break
        return merged

    def solve_single_iteration(self) -> List[List[int]]:
        """Thực hiện một lượt giải CCA kết hợp tham lam bao phủ và tìm kiếm cục bộ."""
        uncovered = set(range(self.n_nodes))
        clubs = []

        remaining_candidates = set(range(self.n_nodes))

        while uncovered and remaining_candidates:
            # Chọn tâm v tối đa hóa |Ball(v) \cap uncovered|
            best_v = None
            max_gain = -1.0

            cand_list = list(remaining_candidates)
            if len(cand_list) > 20:
                cand_list = random.sample(cand_list, 20)

            for v in cand_list:
                ball_v = self.balls[v]
                gain = sum(1 for u in ball_v if u in uncovered)
                # Thêm chút nhiễu ngẫu nhiên để đa dạng hóa nghiệm qua các lượt chạy
                score = float(gain) + (self.degrees[v] * 0.01) + random.uniform(0.0, 0.1)
                if score > max_gain:
                    max_gain = score
                    best_v = v

            if best_v is None or max_gain <= 0.0:
                # Nếu không tâm nào phủ thêm được, gán từng đỉnh còn lại vào chính nó
                for u in list(uncovered):
                    clubs.append([u])
                break

            chosen_club = list(self.balls[best_v])
            clubs.append(chosen_club)
            uncovered.difference_update(chosen_club)
            remaining_candidates.discard(best_v)

        # Tinh chỉnh cục bộ
        clubs = self._prune_redundant_clubs(clubs)
        clubs = self._merge_adjacent_clubs(clubs)
        clubs = self._prune_redundant_clubs(clubs)
        return clubs

    def run(self, max_iterations: int = 200) -> Dict[str, Any]:
        """Thực thi CCA qua nhiều lượt multi-start có Early Stopping."""
        start_time = time.time()
        best_cover_size = self.n_nodes
        best_clubs = []

        convergence_curve = []
        cover_sizes = []
        stagnant_count = 0
        limit_iter = min(max_iterations, 50)

        for it in range(1, limit_iter + 1):
            clubs = self.solve_single_iteration()
            cover_sz = len(clubs)

            if cover_sz < best_cover_size:
                best_cover_size = cover_sz
                best_clubs = clubs
                stagnant_count = 0
            else:
                stagnant_count += 1

            convergence_curve.append(float(best_cover_size))
            cover_sizes.append(int(best_cover_size))

            if stagnant_count >= 15:
                break

        runtime = time.time() - start_time

        # Kiểm tra tính khả thi
        covered_all = set()
        for c in best_clubs:
            covered_all.update(c)
        is_feasible = (len(covered_all) == self.n_nodes) and all(self.graph.is_s_club(c) for c in best_clubs)

        return {
            'best_cover': int(best_cover_size),
            'best_fitness': float(best_cover_size),
            'avg_fitness': float(best_cover_size),
            'mean_violation': 0.0,
            'diversity': 0.0,
            'is_feasible': bool(is_feasible),
            'runtime': float(runtime),
            'best_solution_clubs': {int(i): [int(v) for v in c] for i, c in enumerate(best_clubs)},
            'club_sizes': [len(c) for c in best_clubs],
            'history': {
                'convergence_curve': convergence_curve,
                'cover_sizes': cover_sizes,
                'action_probs': [[1.0 / self.config.num_operators] * self.config.num_operators] * len(convergence_curve)
            }
        }


def run_cca(graph: SClubGraph, config: ExperimentConfig, seed: Optional[int] = None) -> Dict[str, Any]:
    """Hàm giao diện thực thi thuật toán Club-Cover-Approx (CCA) trên một seed cụ thể."""
    if seed is not None:
        random.seed(seed)
        np.random.seed(seed)
    solver = CCASolver(graph, config)
    return solver.run(max_iterations=config.max_generations)
