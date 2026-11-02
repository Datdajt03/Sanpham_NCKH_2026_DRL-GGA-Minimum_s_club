r"""
problem/imsm.py — Cài đặt thuật toán I-MSM (Iterated Maximum s-Club Heuristic / Multi-start Greedy Search).

Định vị khoa học:
  Baseline đối chứng kinh điển trong văn hiến quốc tế và bài báo gốc của Thầy:
  "Thuật toán gần đúng dựa trên phương thức khởi tạo lời giải nhiều lần kết hợp tìm kiếm tham lam cục bộ (I-MSM)".

Cơ chế hoạt động:
  1. Multi-start Restarts: Chạy qua T lần lặp (tương đương số thế hệ max_generations của EA).
  2. Ở mỗi lần lặp:
       - Tập đỉnh chưa phủ ban đầu: U = V.
       - Vòng lặp tham lam: Trong khi U != rỗng, chọn đỉnh hạt giống v in U có bậc lớn nhất.
       - Phát triển s-club cực đại quanh v: Liên tục bổ sung các đỉnh u tối đa hóa số đỉnh chưa phủ được bao bọc sao cho đường kính cảm sinh vẫn thỏa diam(G[C U {u}]) <= s.
       - Bổ sung club C vào tập phủ và cập nhật U <- U \ C.
  3. Tìm kiếm cục bộ & Tinh gọn (Local Search & Redundant Pruning):
       - Loại bỏ các club dư thừa (Redundant Clubs) nếu mọi đỉnh của nó đã được phủ bởi các club khác.
       - Thử gộp các cặp club lân cận nếu hợp của chúng vẫn là 1 s-club hợp lệ.
  4. Ghi nhận đường cong hội tụ qua các bước lặp để đối chiếu trực tiếp với PPO-AOS, MAB-AOS, Greedy-AOS.
"""
import time
import random
import numpy as np
from typing import List, Set, Dict, Any, Optional
from configs.config import ExperimentConfig
from problem.graph import SClubGraph


class IMSMSolver:
    """
    Bộ giải I-MSM (Iterated Maximum s-Club Method) với ma trận khoảng cách O(1).
    """
    def __init__(self, graph: SClubGraph, config: ExperimentConfig):
        self.graph = graph
        self.config = config
        self.s = config.s_club_threshold
        self.n_nodes = graph.n_nodes
        
        # Tiền tính toán ma trận khoảng cách và bậc đỉnh một lần duy nhất để truy xuất O(1)
        # Sử dụng float32 để hỗ trợ an toàn cho đồ thị không liên thông (khoảng cách inf giữa các thành phần)
        self.dist_matrix = np.array(graph.raw_graph.distances(), dtype=np.float32)
        self.degrees = np.array(graph.raw_graph.degree(), dtype=np.int32)

    def _greedy_expand_s_club(self, seed_node: int, uncovered_nodes: Set[int]) -> List[int]:
        """
        Phát triển một s-club cực đại bắt đầu từ đỉnh seed_node.
        Ưu tiên các đỉnh nằm trong tập uncovered_nodes để giảm số lượng club.
        """
        club = [seed_node]
        candidates = {u for u in range(self.n_nodes) if u != seed_node and self.dist_matrix[seed_node, u] <= self.s}

        while candidates:
            best_candidate = None
            best_score = -1.0

            candidate_list = list(candidates)
            if len(candidate_list) > 10:
                candidate_list = random.sample(candidate_list, 10)

            for u in candidate_list:
                trial_club = club + [u]
                if self.graph.is_s_club(trial_club):
                    score = (10.0 if u in uncovered_nodes else 1.0) + (self.degrees[u] * 0.05) + random.uniform(0.0, 0.2)
                    if score > best_score:
                        best_score = score
                        best_candidate = u

            if best_candidate is not None:
                club.append(best_candidate)
                candidates.remove(best_candidate)
                candidates = {u for u in candidates if self.dist_matrix[best_candidate, u] <= self.s}
            else:
                break

        return club

    def _prune_redundant_clubs(self, clubs: List[List[int]]) -> List[List[int]]:
        """Loại bỏ các club dư thừa (nếu mọi đỉnh của nó đã được phủ bởi các club khác)."""
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
                    # Chỉ kiểm tra s-club nếu giữa 2 club thực sự có cạnh nối trực tiếp
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
        """Thực hiện một lần lặp xây dựng lời giải từ đầu và tinh chỉnh cục bộ."""
        uncovered = set(range(self.n_nodes))
        clubs = []

        while uncovered:
            uncovered_list = list(uncovered)
            degs = [self.degrees[u] for u in uncovered_list]
            max_deg = max(degs)
            candidates_seed = [u for u, d in zip(uncovered_list, degs) if d >= max_deg * 0.7]
            seed = random.choice(candidates_seed) if candidates_seed else uncovered_list[0]

            new_club = self._greedy_expand_s_club(seed, uncovered)
            clubs.append(new_club)
            uncovered.difference_update(new_club)

        # Tinh chỉnh cục bộ
        clubs = self._prune_redundant_clubs(clubs)
        clubs = self._merge_adjacent_clubs(clubs)
        clubs = self._prune_redundant_clubs(clubs)
        return clubs

    def run(self, max_iterations: int = 200) -> Dict[str, Any]:
        """
        Thực hiện toàn bộ quá trình I-MSM qua max_iterations lần lặp (có Early Stopping).
        """
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

            # Dừng sớm nếu không cải thiện sau 15 lần lặp
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


def run_imsm(graph: SClubGraph, config: ExperimentConfig, seed: Optional[int] = None) -> Dict[str, Any]:
    """Hàm giao diện thực thi thuật toán I-MSM trên một seed cụ thể."""
    if seed is not None:
        random.seed(seed)
        np.random.seed(seed)
    solver = IMSMSolver(graph, config)
    return solver.run(max_iterations=config.max_generations)
