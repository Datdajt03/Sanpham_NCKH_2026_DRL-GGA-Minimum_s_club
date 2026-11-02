"""
problem/individual.py — Lớp đại diện cho một cá thể (nghiệm) theo mã hóa GGA.
"""
import numpy as np
from typing import Dict, List, Set


class Individual:
    """
    Một cá thể biểu diễn phân hoạch các đỉnh của đồ thị vào các s-club.
    Kế thừa mô hình mã hóa Grouping Genetic Algorithm (GGA):
      - _x: Vector gán nhãn đỉnh [v] -> club_id (V-part)
      - c_part: Danh sách các club_id hoạt động (C-part)
    """
    def __init__(self, n_nodes: int, k_max: int = None, assignment: np.ndarray = None):
        self.n_nodes = n_nodes
        self.k_max = k_max if k_max is not None else max(1, n_nodes // 2)
        
        if n_nodes <= 0:
            self._x = np.array([], dtype=np.int32)
            self.fitness: float = float('inf')
            self.is_feasible: bool = False
            self.num_clubs: int = 0
            self.diameter_violation: float = 0.0
            return

        if assignment is not None:
            self._x = np.array(assignment, dtype=np.int32)
        else:
            # Khởi tạo ngẫu nhiên
            self._x = np.random.randint(0, self.k_max, size=n_nodes, dtype=np.int32)

        self.fitness: float = float('inf')
        self.is_feasible: bool = False
        self.num_clubs: int = len(np.unique(self._x)) if len(self._x) > 0 else 0
        self.diameter_violation: float = float('inf')

        self.relabel_compact()

    def get_clubs(self) -> Dict[int, List[int]]:
        """Trả về dictionary ánh xạ: club_id -> danh sách đỉnh thuộc club."""
        clubs = {}
        for v in range(self.n_nodes):
            c_id = int(self._x[v])
            if c_id not in clubs:
                clubs[c_id] = []
            clubs[c_id].append(v)
        return clubs

    def get_c_part(self) -> List[int]:
        """Trả về danh sách các nhãn club hoạt động (C-part)."""
        if len(self._x) == 0:
            return []
        return sorted(list(set(self._x.tolist())))

    def relabel_compact(self):
        """
        Chuẩn hóa đánh số các club từ 0 đến m - 1 liên tục.
        Giúp cấu trúc nghiệm dạng nhóm luôn ở dạng chính tắc (canonical).
        """
        if len(self._x) == 0:
            self.num_clubs = 0
            return
        unique_labels = np.unique(self._x)
        mapping = {old_lbl: new_lbl for new_lbl, old_lbl in enumerate(unique_labels)}
        self._x = np.array([mapping[val] for val in self._x], dtype=np.int32)
        self.num_clubs = len(unique_labels)

    def copy(self) -> 'Individual':
        """Tạo bản sao sâu (deep copy) của cá thể."""
        clone = Individual(self.n_nodes, self.k_max, assignment=self._x.copy())
        clone.fitness = self.fitness
        clone.is_feasible = self.is_feasible
        clone.num_clubs = self.num_clubs
        clone.diameter_violation = self.diameter_violation
        return clone

    def __repr__(self) -> str:
        return f"<Individual n={self.n_nodes}, clubs={self.num_clubs}, fitness={self.fitness:.2f}, feasible={self.is_feasible}>"


def create_greedy_bfs_individual(graph, s: int) -> Individual:
    """
    Khởi tạo cá thể chất lượng cao bằng thuật toán gom cụm BFS ngẫu nhiên (Randomized BFS Seeding):
    Xuất phát từ các đỉnh gốc ngẫu nhiên và mở rộng quả cầu cảm sinh B_r(root) với r = max(1, s // 2).
    Theo định lý Dondi (2019), mọi quả cầu bán kính r <= s//2 luôn đảm bảo 100% diam(G[B_r]) <= 2r <= s.
    Tốc độ khởi tạo O(|V| + |E|) tính bằng mili-giây mà không cần nhân ma trận.
    """
    n = graph.n_nodes
    if n <= 0:
        return Individual(0)

    unvisited = set(range(n))
    assignment = np.full(n, -1, dtype=np.int32)
    club_id = 0
    radius = max(1, s // 2)

    while unvisited:
        root = np.random.choice(list(unvisited))
        current_cluster = [int(root)]
        unvisited.remove(root)

        queue = [(int(root), 0)]
        visited_in_step = {int(root)}

        while queue:
            curr, depth = queue.pop(0)
            if depth >= radius:
                continue
            for nbr in graph.get_neighbors(curr):
                if nbr in unvisited and nbr not in visited_in_step:
                    visited_in_step.add(nbr)
                    current_cluster.append(nbr)
                    unvisited.remove(nbr)
                    queue.append((nbr, depth + 1))

        for v in current_cluster:
            assignment[v] = club_id
        club_id += 1

    ind = Individual(n, assignment=assignment)
    ind.relabel_compact()
    return ind
