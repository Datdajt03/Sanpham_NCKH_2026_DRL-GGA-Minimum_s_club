"""
dataset/selector.py — Giao diện tương tác điều hướng bằng phím (TUI Dataset Selector).

Tính năng:
  - Phím LÊN (▲) / XUỐNG (▼) hoặc W/S: Di chuyển con trỏ qua danh sách đồ thị benchmark.
  - Phím I (hoặc Phím Cách - Space): Chọn / Bỏ chọn đồ thị đang trỏ tới ([X] / [ ]).
  - Phím O (hoặc Phím Enter): Hoàn tất chọn và bắt đầu chạy thực nghiệm!
  - Phím A: Chọn tất cả (Select All) / Bỏ chọn tất cả.
  - Phím Q (hoặc Esc): Thoát chương trình.
  - Hỗ trợ cuộn phân trang mượt mà cho danh sách 80+ đồ thị trong pbodulieu.
"""
import os
import sys
from typing import List, Dict, Tuple


def _clear_screen():
    """Xóa màn hình console tương thích Windows / Linux."""
    os.system('cls' if os.name == 'nt' else 'clear')


def interactive_dataset_selector(graph_files: Dict[str, str]) -> List[str]:
    """
    Menu tương tác trực quan chọn đồ thị bằng phím mũi tên [▲/▼], phím [I] để chọn và [O] để hoàn tất.
    """
    graph_names = list(graph_files.keys())
    if not graph_names:
        return []

    # Kiểm tra xem môi trường có hỗ trợ nhập ký tự trực tiếp không (msvcrt trên Windows)
    is_windows = (os.name == 'nt')
    has_msvcrt = False
    if is_windows:
        try:
            import msvcrt
            has_msvcrt = True
        except ImportError:
            has_msvcrt = False

    # Nếu không có msvcrt (ví dụ chạy qua pipe hoặc terminal không hỗ trợ), fallback sang nhập text
    if not has_msvcrt or not sys.stdin.isatty():
        return _fallback_text_menu(graph_names, graph_files)

    import msvcrt

    selected_indices = set()
    cursor_idx = 0
    page_size = 18  # Số lượng đồ thị hiển thị trên một trang
    filter_keyword = ""

    while True:
        # Lọc danh sách nếu có từ khóa tìm kiếm
        if filter_keyword:
            filtered_indices = [idx for idx, name in enumerate(graph_names) if filter_keyword.lower() in name.lower()]
        else:
            filtered_indices = list(range(len(graph_names)))

        if not filtered_indices:
            filtered_indices = list(range(len(graph_names)))
            filter_keyword = ""

        # Đảm bảo con trỏ nằm trong phạm vi hiển thị
        if cursor_idx >= len(filtered_indices):
            cursor_idx = len(filtered_indices) - 1
        if cursor_idx < 0:
            cursor_idx = 0

        # Tính toán trang hiển thị
        start_idx = (cursor_idx // page_size) * page_size
        end_idx = min(start_idx + page_size, len(filtered_indices))

        _clear_screen()
        print("=" * 82)
        print("      🚀 EVO-RL: BẢNG ĐIỀU KHIỂN CHỌN BỘ DỮ LIỆU THỰC NGHIỆM ĐỒ THỊ")
        print("=" * 82)
        print(f" Tìm thấy: {len(graph_names)} đồ thị trong pbodulieu | Đã chọn: {len(selected_indices)} đồ thị")
        if filter_keyword:
            print(f" 🔍 Bộ lọc tìm kiếm: '{filter_keyword}' (Nhấn Backspace để xóa)")
        print("-" * 82)
        print(f" {'Trạng thái':<12} | {'STT':<4} | {'Tên bộ dữ liệu đồ thị':<35} | {'Dung lượng':<12}")
        print("-" * 82)

        for pos in range(start_idx, end_idx):
            real_idx = filtered_indices[pos]
            name = graph_names[real_idx]
            fpath = graph_files[name]
            
            try:
                sz_kb = os.path.getsize(fpath) / 1024
                sz_str = f"{sz_kb:>7.1f} KB" if sz_kb < 1024 else f"{sz_kb/1024:>6.2f} MB"
            except Exception:
                sz_str = "    N/A   "

            is_sel = real_idx in selected_indices
            is_cur = (pos == cursor_idx)

            check_mark = "[X]" if is_sel else "[ ]"
            pointer = "👉 " if is_cur else "   "

            # Format dòng hiển thị
            line_str = f"{pointer}{check_mark}        | {real_idx + 1:>3d}  | {name:<35} | {sz_str}"
            print(line_str)

        # Hiển thị thanh cuộn và hướng dẫn phím tắt
        print("-" * 82)
        page_curr = (cursor_idx // page_size) + 1
        page_total = max(1, (len(filtered_indices) + page_size - 1) // page_size)
        print(f" [Trang {page_curr}/{page_total}] (Hiển thị {start_idx + 1} - {end_idx} / tổng {len(filtered_indices)} đồ thị)")
        print("=" * 82)
        print(" 🎮 HƯỚNG DẪN ĐIỀU KHIỂN:")
        print("   * [▲ / ▼] hoặc [W / S]   : Di chuyển con trỏ lên / xuống")
        print("   * [I] hoặc [Phím Cách]    : CHỌN / BỎ CHỌN đồ thị hiện tại ([X] / [ ])")
        print("   * [O] hoặc [Phím Enter]   : HOÀN TẤT VÀ BẮT ĐẦU CHẠY THỰC NGHIỆM")
        print("   * [A]                     : Chọn TẤT CẢ / Bỏ chọn tất cả")
        print("   * [Q] hoặc [Esc]          : Thoát chương trình")
        print("=" * 82)

        # Đọc phím nhấn từ bàn phím qua msvcrt
        key = msvcrt.getch()

        # Xử lý phím đặc biệt (Phím mũi tên, PageUp, PageDown)
        if key in (b'\x00', b'\xe0'):
            sub_key = msvcrt.getch()
            if sub_key == b'H':  # Mũi tên Lên
                cursor_idx = (cursor_idx - 1) % len(filtered_indices)
            elif sub_key == b'P':  # Mũi tên Xuống
                cursor_idx = (cursor_idx + 1) % len(filtered_indices)
            elif sub_key == b'I':  # Page Up
                cursor_idx = max(0, cursor_idx - page_size)
            elif sub_key == b'Q':  # Page Down
                cursor_idx = min(len(filtered_indices) - 1, cursor_idx + page_size)
            elif sub_key == b'G':  # Home
                cursor_idx = 0
            elif sub_key == b'O':  # End
                cursor_idx = len(filtered_indices) - 1
            continue

        # Xử lý các phím ký tự thông thường
        if key in (b'i', b'I', b' '):
            # Phím I hoặc Space: Toggle chọn
            cur_real = filtered_indices[cursor_idx]
            if cur_real in selected_indices:
                selected_indices.remove(cur_real)
            else:
                selected_indices.add(cur_real)
            # Tự động di chuyển xuống 1 dòng cho tiện thao tác
            cursor_idx = (cursor_idx + 1) % len(filtered_indices)

        elif key in (b'o', b'O', b'\r'):
            # Phím O hoặc Enter: Hoàn tất
            if not selected_indices:
                # Nếu chưa chọn gì, tự động chọn đồ thị đang được trỏ
                selected_indices.add(filtered_indices[cursor_idx])
            break

        elif key in (b'w', b'W', b'k', b'K'):
            # W hoặc K: Di chuyển lên
            cursor_idx = (cursor_idx - 1) % len(filtered_indices)

        elif key in (b's', b'S', b'j', b'J'):
            # S hoặc J: Di chuyển xuống
            cursor_idx = (cursor_idx + 1) % len(filtered_indices)

        elif key in (b'a', b'A'):
            # Phím A: Chọn tất cả hoặc bỏ chọn tất cả
            if len(selected_indices) == len(graph_names):
                selected_indices.clear()
            else:
                selected_indices = set(range(len(graph_names)))

        elif key in (b'q', b'Q', b'\x1b'):
            # Phím Q hoặc Esc: Thoát
            print("\n[!] Đã thoát chương trình.")
            sys.exit(0)

        elif key == b'\x08':  # Backspace (xóa từ khóa tìm kiếm)
            if filter_keyword:
                filter_keyword = filter_keyword[:-1]
                cursor_idx = 0

    selected_names = [graph_names[idx] for idx in sorted(list(selected_indices))]
    _clear_screen()
    print("=" * 82)
    print(f" [+] ĐÃ CHỌN {len(selected_names)} ĐỒ THỊ ĐỂ CHẠY THỰC NGHIỆM:")
    for i, name in enumerate(selected_names, 1):
        print(f"     {i:>2d}. {name}")
    print("=" * 82)
    return selected_names


def _fallback_text_menu(graph_names: List[str], graph_files: Dict[str, str]) -> List[str]:
    """Fallback cho terminal không hỗ trợ msvcrt hoặc chế độ dòng lệnh."""
    print("\n" + "=" * 80)
    print("      CHƯƠNG TRÌNH THỰC NGHIỆM TIẾN HÓA HỌC TĂNG CƯỜNG (EVO-RL)")
    print("=" * 80)
    print(f"Tìm thấy {len(graph_names)} đồ thị trong pbodulieu:")
    print("  [ 0] Chạy TẤT CẢ đồ thị")
    for idx, name in enumerate(graph_names):
        print(f"  [{idx + 1:2d}] {name}")
    print("-" * 80)
    choice = input(">> Nhập lựa chọn (vd: 1,3,5 hoặc 1-5 hoặc tên đồ thị): ").strip()
    if not choice or choice == '0' or choice.lower() in ('all', 'tat ca'):
        return list(graph_names)
    
    selected = []
    tokens = [t.strip() for t in choice.replace(',', ' ').split() if t.strip()]
    for token in tokens:
        if '-' in token:
            parts = token.split('-')
            if parts[0].isdigit() and parts[1].isdigit():
                for idx in range(int(parts[0]), int(parts[1]) + 1):
                    if 1 <= idx <= len(graph_names):
                        selected.append(graph_names[idx - 1])
                continue
        if token.isdigit():
            idx = int(token)
            if 1 <= idx <= len(graph_names):
                selected.append(graph_names[idx - 1])
            continue
        for name in graph_names:
            if token.lower() in name.lower():
                if name not in selected:
                    selected.append(name)
    return selected if selected else [graph_names[0]]
