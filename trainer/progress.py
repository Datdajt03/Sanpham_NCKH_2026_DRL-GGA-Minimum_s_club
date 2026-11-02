"""
trainer/progress.py — Module giám sát tiến trình đa tiến trình thời gian thực (Live Multi-Worker Dashboard).
Hiển thị đồng thời trạng thái của tất cả các Seed đang chạy song song trên console.
Hỗ trợ đa nền tảng Windows CMD / PowerShell với cơ chế an toàn bộ nhớ và không làm nghẽn luồng.
"""
import os
import sys
import time
import threading
from typing import Dict, Any, Optional, List


def format_progress_bar(current: int, total: int, length: int = 15) -> str:
    """Tạo thanh tiến độ đồ họa ASCII dạng [██████░░░░] %."""
    if total <= 0:
        return "[" + " " * length + "]   0.0%"
    ratio = min(1.0, max(0.0, current / total))
    filled_len = int(length * ratio)
    bar = "█" * filled_len + "░" * (length - filled_len)
    percent = ratio * 100.0
    return f"[{bar}] {percent:>5.1f}%"


class LiveParallelDashboard:
    """
    Bảng điều khiển trực quan cập nhật liên tục trạng thái của N workers chạy song song.
    Hoạt động trong một luồng riêng biệt (Daemon Thread) ở tiến trình chính.
    """
    def __init__(
        self, 
        shared_status_dict: Dict[int, Any], 
        num_workers: int = 5, 
        total_seeds: int = 20,
        conditions: Optional[List[str]] = None,
        refresh_interval: float = 1.0
    ):
        self.shared_status = shared_status_dict
        self.num_workers = num_workers
        self.total_seeds = total_seeds
        self.conditions = conditions or ["PPO-AOS", "MAB-AOS", "Greedy-AOS", "No-RL", "Fixed", "Random", "I-MSM", "CCA"]
        self.refresh_interval = refresh_interval
        self.running = False
        self.thread: Optional[threading.Thread] = None
        self._lock = threading.Lock()

    def start(self):
        """Khởi động luồng hiển thị Dashboard thời gian thực."""
        self.running = True
        self.thread = threading.Thread(target=self._render_loop, daemon=True)
        self.thread.start()

    def stop(self):
        """Dừng bảng điều khiển an toàn và giải phóng màn hình."""
        self.running = False
        if self.thread and self.thread.is_alive():
            self.thread.join(timeout=1.5)
        print("", flush=True)

    def _render_loop(self):
        """Vòng lặp vẽ lại dashboard theo chu kỳ."""
        time.sleep(0.5)
        while self.running:
            try:
                self._draw_dashboard()
            except Exception:
                pass
            time.sleep(self.refresh_interval)

    def _draw_dashboard(self):
        """Kết xuất thông tin của tất cả các worker đang hoạt động."""
        if not self.running:
            return

        with self._lock:
            try:
                status_keys = list(self.shared_status.keys())
            except Exception:
                return

            if not status_keys:
                return

            # Lấy các slot đang chạy
            active_slots = []
            for s_idx in sorted(status_keys):
                info = self.shared_status.get(s_idx, {})
                if info and info.get('status') == 'RUNNING':
                    active_slots.append(info)

            if not active_slots:
                return

            header = f"\n>>> [LIVE PARALLEL DASHBOARD | {len(active_slots)}/{self.num_workers} SEEDS SONG SONG] <<<"
            lines = [header]
            lines.append("=" * 95)

            for slot in active_slots:
                w_id = slot.get('worker_id', 1)
                s_idx = slot.get('seed_idx', 1)
                s_val = slot.get('seed_val', '------')
                cond = slot.get('condition', 'PPO-AOS')
                cond_idx = slot.get('cond_idx', 1)
                total_conds = slot.get('total_conds', len(self.conditions))
                gen = slot.get('gen', 0)
                max_gen = slot.get('max_gen', 200)
                cover = slot.get('best_cover', '--')
                feas = "Feas:OK" if slot.get('is_feasible', True) else "Feas:NO"
                elapsed = slot.get('elapsed', 0.0)
                
                pbar = format_progress_bar(gen, max_gen, length=10)
                
                line = (
                    f"  Worker #{w_id:02d} | Seed {s_idx:02d}/{self.total_seeds:02d} ({s_val}) | "
                    f"[{cond:<10}] ({cond_idx}/{total_conds}) | "
                    f"Gen {gen:>3}/{max_gen} {pbar} | Cover={cover:<3} ({feas}) | {elapsed:>5.1f}s"
                )
                lines.append(line)

            lines.append("=" * 95)
            output_str = "\n".join(lines)
            print(output_str, flush=True)


def update_worker_status(
    shared_status: Optional[Dict[int, Any]],
    seed_idx: int,
    seed_val: int,
    worker_id: int,
    condition: str,
    cond_idx: int,
    total_conds: int,
    gen: int,
    max_gen: int,
    best_cover: int,
    is_feasible: bool,
    elapsed: float,
    status: str = "RUNNING"
):
    """
    Cập nhật nhanh trạng thái của một worker vào shared_dict.
    Hoạt động cực nhanh (Sub-millisecond), không gây nghẽn tiến trình tính toán.
    """
    if shared_status is None:
        return
    try:
        shared_status[seed_idx] = {
            'worker_id': worker_id,
            'seed_idx': seed_idx,
            'seed_val': seed_val,
            'condition': condition,
            'cond_idx': cond_idx,
            'total_conds': total_conds,
            'gen': gen,
            'max_gen': max_gen,
            'best_cover': best_cover,
            'is_feasible': is_feasible,
            'elapsed': float(elapsed),
            'status': status,
            'updated_at': time.time()
        }
    except Exception:
        pass
