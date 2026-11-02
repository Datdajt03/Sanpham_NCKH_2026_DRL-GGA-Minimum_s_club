"""
dataset/parser.py — Xử lý định dạng đồ thị DIMACS (.clq), Metis (.graph), GML và chuẩn hóa dữ liệu.
"""
import re
import igraph as ig
from typing import Tuple, List


def parse_dimacs_clq(content: str) -> Tuple[int, List[Tuple[int, int]]]:
    """
    Parse nội dung file DIMACS (.clq) thành số đỉnh và danh sách cạnh 0-indexed.
    Định dạng DIMACS Clique/Coloring:
      c Comment lines...
      p edge <n_nodes> <n_edges>
      e <u> <v>
    """
    edges = []
    n_nodes = 0

    for line in content.splitlines():
        line = line.strip()
        if not line or line.startswith('c') or line.startswith('#'):
            continue
        parts = line.split()
        if parts[0] == 'p':
            n_nodes = int(parts[2])
        elif parts[0] == 'e':
            u = int(parts[1]) - 1  # Chuyển sang 0-indexed
            v = int(parts[2]) - 1
            if u != v:
                edges.append((min(u, v), max(u, v)))

    # Loại bỏ cạnh trùng lặp
    edges = list(set(edges))
    return n_nodes, edges


def parse_metis_graph(content: str) -> Tuple[int, List[Tuple[int, int]]]:
    """
    Parse định dạng Metis Graph (.graph) từ DIMACS 10th Challenge:
      % Comment lines
      <n_nodes> <n_edges> [fmt]
      neighbor_1 neighbor_2 ... (cho đỉnh 1)
      neighbor_1 neighbor_2 ... (cho đỉnh 2)
    """
    lines = [
        line.strip() for line in content.splitlines() 
        if line.strip() and not line.strip().startswith(('%', '#', 'c'))
    ]
    if not lines:
        return 0, []

    first_line = lines[0].split()
    n_nodes = int(first_line[0])
    
    edges = []
    for u_idx, line in enumerate(lines[1:n_nodes + 1]):
        u = u_idx  # 0-indexed
        tokens = line.split()
        for token in tokens:
            try:
                v = int(token) - 1  # 0-indexed
                if u < v and v < n_nodes:
                    edges.append((u, v))
            except ValueError:
                continue

    return n_nodes, list(set(edges))


def parse_gml_text(content: str) -> Tuple[int, List[Tuple[int, int]]]:
    """
    Parse nội dung file GML bằng Regex khi parser mặc định gặp lỗi.
    """
    nodes = re.findall(r'id\s+(\d+)', content)
    node_ids = sorted(list(set(int(n) for n in nodes)))
    n_nodes = len(node_ids)

    id_map = {orig_id: idx for idx, orig_id in enumerate(node_ids)}
    edges_raw = re.findall(r'source\s+(\d+)\s+target\s+(\d+)', content)
    
    edges = []
    for u, v in edges_raw:
        u_idx, v_idx = id_map[int(u)], id_map[int(v)]
        if u_idx != v_idx:
            edges.append((min(u_idx, v_idx), max(u_idx, v_idx)))

    edges = list(set(edges))
    return n_nodes, edges


def clean_graph(G: ig.Graph) -> ig.Graph:
    """Loại bỏ khuyên (self-loops) và đa cạnh (multi-edges)."""
    G.simplify(multiple=True, loops=True)
    return G
