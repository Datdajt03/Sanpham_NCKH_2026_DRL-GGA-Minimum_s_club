# EVO-RL MSCC Framework
## Khung Tối Ưu Hóa Tiến Hóa Kết Hợp Học Tăng Cường Sâu (PPO-AOS) Cho Bài Toán Minimum s-Club Cover
**Gói sản phẩm:** `Sanpham_nckh` | **Nghiệm thu Đề tài NCKH**

---

### 1. GIỚI THIỆU TỔNG QUAN
Hệ thống **EVO-RL MSCC** là giải pháp phần mềm nghiên cứu khoa học giải bài toán **Phủ s-Club Tối thiểu (Minimum s-Club Cover - MSCC)** trên đồ thị phức, tích hợp giải thuật di truyền nhóm (Grouping GA) và mạng học tăng cường sâu PPO (Proximal Policy Optimization) để lựa chọn toán tử thích nghi trực tuyến (Adaptive Operator Selection - AOS).

* **Đóng góp khoa học cốt lõi:**
  * Giải quyết bài toán mở về hạn chế của tỷ lệ đột biến tĩnh 33% (TS. Phạm Đình Thành, 2024).
  * Biểu diễn không gian quan sát qua vector 5 chiều nén $S_t$ kết hợp chuẩn hóa Welford 5D.
  * Hàm phần thưởng Feasibility-Aware 4 thành phần giúp định hướng cân bằng giữa tối ưu tập phủ và sửa sai.
  * Tối ưu hóa tính toán: Tăng tốc GPU NVIDIA CUDA cho mạng Actor-Critic, CPU đa luồng (10 workers song song).
  * Khả chuyển 100%: Tích hợp sẵn 30 đồ thị benchmark chuẩn quốc tế (12 mạng thực tế + 18 DIMACS).

---

### 2. CẤU TRÚC GÓI SẢN PHẨM TINH GỌN

```text
Sanpham_nckh/
├── CHAY_CHUONG_TRINH_TONG.bat   # [1-CLICK] Menu chính điều hành tất cả tính năng sản phẩm
├── CHAY.bat                    # [1-CLICK] Phím tắt nhanh khởi chạy Menu Tổng
├── setup.bat                    # [1-CLICK] Cài đặt môi trường tự động (Python, CUDA, thư viện)
│
├── Run.bat/                     # THƯ MỤC CHỨA CÁC RUNNER THỰC NGHIỆM CHI TIẾT
│   ├── run.bat                  # Thực nghiệm EVO-RL MSCC (30 đồ thị benchmark)
│   ├── runbieudo.bat            # Xuất biểu đồ chuẩn 600 DPI (PNG) và vector PDF
│   ├── run_tong_hop_so_lieu.bat # Tổng hợp số liệu phân tích và đóng gói báo cáo
│   ├── verify_all.bat           # Bộ kiểm chứng tự động 9 giai đoạn (< 5 giây)
│   └── RUN_ALL.bat              # Phím tắt chuyển tiếp tới CHAY_CHUONG_TRINH_TONG.bat
│
├── configs/                     # Cấu hình siêu tham số giải thuật (khóa cứng chuẩn đối chuẩn)
├── dataset/ & problem/          # Nạp đồ thị, mô hình hóa SClubGraph, Individual, Fitness
├── operators/                   # Toán tử di truyền Crossover, Mutation (Split/Merge/Transfer), Repair
├── rl/ & environment/           # Não bộ Deep RL: Mạng Actor-Critic MLP, MDP Gym Environment, Reward
├── trainer/ & analysis/         # Vòng lặp tiến hóa lai (GGA + PPO), vẽ biểu đồ 600 DPI
│
├── pbodulieu/                   # Bộ 30 đồ thị benchmark chuẩn (12 mạng thực tế + 18 DIMACS)
├── results/                     # Kết quả thực nghiệm (30 đồ thị x 20 seeds x 8 thuật toán)
└── Tong_hop_so_lieu_phan_bien/  # Kết quả tổng hợp đối chuẩn 30 đồ thị & báo cáo Markdown
```

---

### 3. CÀI ĐẶT MÔI TRƯỜNG (SETUP)

Chỉ cần thực hiện 1 lần duy nhất nếu máy tính chưa cài đặt thư viện:
* **Tự động 1-Click (Khuyến nghị trên Windows):** Nhấp đúp vào:
  ```cmd
  setup.bat
  ```
* **Hoặc thủ công bằng pip:**
  ```bash
  pip install -r requirements.txt
  ```

---

### 4. HƯỚNG DẪN KHỞI CHẠY (QUICK START)

#### Cách 1: Sử dụng Menu Chương trình Tổng (Khuyến nghị)
Nhấp đúp chuột vào tệp:
```cmd
CHAY_CHUONG_TRINH_TONG.bat
```
*(hoặc phím tắt `CHAY.bat`)*

Giao diện hiển thị Menu trực quan, rõ ràng gồm 11 chức năng (từ 0 đến 11):
- `[1]` Chạy Test Nhanh (Demo 4 đồ thị)
- `[2]` Chạy Nhóm 1 - 12 Mạng Thực Tế
- `[3]` Chạy Nhóm 2 - 18 Đồ Thị DIMACS
- `[4]` Chạy Toàn Bộ 30 Đồ Thị Benchmark Chuẩn Quốc Tế
- `[5]` Điền Tên Hoặc Dán Danh Sách Đồ Thị Tùy Chọn
- `[6]` Chế Độ Chọn Đồ Thị Tương Tác TUI (Phím mũi tên, Space, Enter)
- `[7]` Tùy Chỉnh Siêu Tham Số Nâng Cao (s, seeds, workers, epochs, pop_size)
- `[8]` Xuất Biểu Đồ Phân Tích & Hội Tụ (600 DPI PNG & Vector PDF)
- `[9]` Tổng Hợp Bảng Số Liệu Báo Cáo & Kiểm Định Wilcoxon
- `[10]` Kiểm Tra Toàn Diện Hệ Thống (9 giai đoạn kiểm chứng)
- `[11]` Thiết Lập Môi Trường & GPU (CUDA)
- `[0]` Thoát chương trình

#### Cách 2: Khởi chạy trực tiếp bằng Python
Chạy trực tiếp từ dòng lệnh:
```bash
python main.py
```
Hệ thống sẽ hiển thị Master Console Menu tương tác trực quan ngay trên terminal. Hoặc truyền tham số trực tiếp:
```bash
# Chạy demo 4 đồ thị
python main.py --graph "karate,chesapeake,dolphins,johnson8-2-4"

# Chạy toàn bộ 30 đồ thị
python main.py --all

# Mở giao diện TUI chọn đồ thị
python main.py --tui
```

#### Cách 3: Kiểm chứng nhanh hệ thống trong 5 giây
Nhấp đúp `Run.bat\verify_all.bat` hoặc chạy lệnh:
```bash
python verify_system.py
```
Hệ thống tự động thực hiện 9 giai đoạn kiểm tra độc lập (phần cứng GPU CUDA, thư viện, nạp đồ thị, toán tử di truyền, mạng PPO, chạy mini smoke test 2 thế hệ, kiểm định thống kê Wilcoxon/Holm-Bonferroni).

---

### 5. TÀI LIỆU KÈM THEO
* **Sổ tay hướng dẫn chi tiết dành cho Hội đồng Khoa học:** [HUONG_DAN_HOI_DONG.md](file:///c:/Users/DD03/Downloads/Baocaotongket/Sanpham_nckh/HUONG_DAN_HOI_DONG.md)
* **Danh sách 20 Hạt giống ngẫu nhiên chuẩn quốc tế:** [seedun.md](file:///c:/Users/DD03/Downloads/Baocaotongket/Sanpham_nckh/seedun.md)
