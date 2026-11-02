"""
check_env.py — Tự động kiểm tra tính sẵn sàng của môi trường EVO-RL MSCC.
"""
import sys
import os

# Đảm bảo UTF-8 cho Windows console
if sys.stdout is not None:
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

def check():
    print("=" * 70)
    print("        KIỂM TRA TỰ ĐỘNG MÔI TRƯỜNG EVO-RL MSCC (SELF-TEST)")
    print("=" * 70)
    print(f"[*] Trình thông dịch: {sys.executable}")
    print(f"[*] Phiên bản Python: {sys.version.split()[0]}")
    
    packages = [
        ('torch', 'PyTorch Tensor Cores Engine'),
        ('numpy', 'NumPy Matrix Processing'),
        ('networkx', 'NetworkX Graph Library'),
        ('matplotlib', 'Matplotlib Visualization'),
        ('pandas', 'Pandas Data Analysis'),
        ('psutil', 'PSUtil Hardware Monitor'),
        ('scipy', 'SciPy Statistical Engine'),
        ('igraph', 'C-Core igraph Graph Analytics')
    ]
    
    missing = []
    print("\n[*] [1] Kiểm tra các thư viện phụ thuộc:")
    for pkg, desc in packages:
        try:
            mod = __import__(pkg)
            ver = getattr(mod, '__version__', 'OK')
            print(f"  [+] {pkg:<12} : v{ver:<10} ({desc})")
        except ImportError as e:
            missing.append(pkg)
            print(f"  [X] {pkg:<12} : CHƯA CÀI ĐẶT ({e})")
            
    print("\n[*] [2] Kiểm tra tăng tốc phần cứng & thiết bị:")
    try:
        import torch
        if torch.cuda.is_available():
            dev_name = torch.cuda.get_device_name(0)
            vram = torch.cuda.get_device_properties(0).total_memory / (1024 ** 2)
            print(f"  [+] NVIDIA GPU   : {dev_name} ({vram:.0f} MB VRAM)")
            print(f"  [+] CUDA Version : {torch.version.cuda} (Tăng tốc Tensor Cores KÍCH HOẠT)")
        else:
            print("  [*] Chế độ       : CPU (Không tìm thấy GPU CUDA hoặc dùng PyTorch CPU)")
    except Exception as ex:
        print(f"  [!] Lỗi GPU: {ex}")

    cpu_cores = os.cpu_count() or 1
    print(f"  [+] CPU Cores    : {cpu_cores} nhân xử lý song song")

    print("\n[*] [3] Kiểm tra bộ dữ liệu thực nghiệm (Benchmark Datasets):")
    current_dir = os.path.dirname(os.path.abspath(__file__))
    candidates = [
        os.path.join(current_dir, "pbodulieu"),
        os.path.abspath(os.path.join(current_dir, "..", "pbodulieu")),
        os.path.join(current_dir, "dataset")
    ]
    
    found_dir = None
    for cand in candidates:
        if os.path.isdir(cand):
            found_dir = cand
            break
            
    if found_dir:
        try:
            from dataset.loader import discover_graph_files
            graphs = discover_graph_files(found_dir)
            print(f"  [+] Thư mục dữ liệu : {found_dir}")
            print(f"  [+] Số file đồ thị  : {len(graphs)} đồ thị (.clq, .gml, .graph)")
            sample = list(graphs.keys())[:5]
            print(f"      (Mẫu danh sách : {', '.join(sample)}...)")
        except Exception as e:
            print(f"  [!] Lỗi khi nạp dữ liệu: {e}")
    else:
        print("  [!] Cảnh báo: Chưa tìm thấy thư mục 'pbodulieu'.")

    print("=" * 70)
    if missing:
        print(f"[!] PHÁT HIỆN THIẾU {len(missing)} THƯ VIỆN: {', '.join(missing)}")
        return 1
    else:
        print("[V] TẤT CẢ CÁC THÀNH PHẦN ĐÃ SẴN SÀNG ĐỂ CHẠY THỰC NGHIỆM!")
        print("=" * 70)
        return 0

if __name__ == '__main__':
    sys.exit(check())
