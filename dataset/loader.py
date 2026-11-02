"""
dataset/loader.py — Đọc và tải đồ thị từ ổ đĩa vào đối tượng igraph.Graph.
"""
import os
import bz2
import igraph as ig
from typing import Dict, List, Tuple
from .parser import parse_dimacs_clq, parse_metis_graph, parse_gml_text, clean_graph


def load_graph(filepath: str) -> ig.Graph:
    """
    Tự động nhận diện định dạng file và trả về đối tượng igraph.Graph.
    Hỗ trợ: .clq, .gml, .graph, .graph.bz2, .txt
    """
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"Không tìm thấy file đồ thị: {filepath}")

    ext = os.path.splitext(filepath)[1].lower()
    content = ""
    
    if filepath.endswith('.graph.bz2') or filepath.endswith('.bz2'):
        try:
            with bz2.open(filepath, 'rt', encoding='utf-8', errors='ignore') as f:
                content = f.read()
        except Exception:
            with bz2.open(filepath, 'rt', encoding='latin1', errors='ignore') as f:
                content = f.read()
    else:
        try:
            with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()
        except Exception:
            with open(filepath, 'r', encoding='latin1', errors='ignore') as f:
                content = f.read()

    # Nhận diện định dạng từ nội dung
    if ext == '.gml':
        try:
            G = ig.Graph.Read_GML(filepath)
            G.to_undirected()
            return clean_graph(G)
        except Exception:
            n_nodes, edges = parse_gml_text(content)
            G = ig.Graph(n=n_nodes, edges=edges, directed=False)
            return clean_graph(G)

    # Kiểm tra nếu là DIMACS .clq format (có 'p edge')
    if 'p edge' in content or ext == '.clq':
        n_nodes, edges = parse_dimacs_clq(content)
    else:
        # Mặc định là Metis .graph format
        n_nodes, edges = parse_metis_graph(content)

    if n_nodes <= 0:
        raise ValueError(f"Đồ thị rỗng hoặc không thể parse được từ: {filepath}")

    G = ig.Graph(n=n_nodes, edges=edges, directed=False)
    return clean_graph(G)


def discover_graph_files(data_dir: str) -> Dict[str, str]:
    """
    Quét và tìm tất cả các file đồ thị hợp lệ trong thư mục.
    Ưu tiên các file benchmark .clq ở thư mục gốc trước.
    """
    graph_files = {}
    if not os.path.exists(data_dir):
        return graph_files

    # 1. Quét các file ở thư mục gốc trước
    for fname in sorted(os.listdir(data_dir)):
        fpath = os.path.join(data_dir, fname)
        if os.path.isfile(fpath):
            ext = os.path.splitext(fname)[1].lower()
            if ext in ('.clq', '.gml', '.graph') or fname.endswith('.graph.bz2'):
                name = os.path.splitext(fname)[0]
                if name.endswith('.graph'):
                    name = os.path.splitext(name)[0]
                graph_files[name] = fpath

    # 2. Quét tiếp các thư mục con
    for root, _, files in os.walk(data_dir):
        if root == data_dir:
            continue
        for fname in sorted(files):
            ext = os.path.splitext(fname)[1].lower()
            if ext in ('.clq', '.gml', '.graph') or fname.endswith('.graph.bz2'):
                name = os.path.splitext(fname)[0]
                if name.endswith('.graph'):
                    name = os.path.splitext(name)[0]
                if name not in graph_files:
                    graph_files[name] = os.path.join(root, fname)

    return graph_files


def load_all_graphs(data_dir: str) -> Dict[str, ig.Graph]:
    """
    Đọc tất cả các file đồ thị hợp lệ trong thư mục.
    Trả về dictionary {graph_name: igraph.Graph}.
    """
    graphs = {}
    graph_files = discover_graph_files(data_dir)
    for name, fpath in graph_files.items():
        try:
            G = load_graph(fpath)
            graphs[name] = G
        except Exception as ex:
            print(f"[Dataset] Warning: Không thể đọc file {name} ({fpath}): {ex}")

    return graphs
