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
  * Tối ưu hóa tính toán: PPO Overhead chiếm < 1.5% tổng thời gian thực thi, RAM đỉnh < 600 MB.
  * Khả chuyển 100%: Tích hợp sẵn 30 đồ thị benchmark chuẩn quốc tế (2.03 MB), không dùng NTFS Junction.

---

### 2. CẤU TRÚC GÓI SẢN PHẨM TINH GỌN

```text
Sanpham_nckh/
├── CHAY_CHUONG_TRINH_TONG.bat   # [1-CLICK] Menu chính điều hành tất cả tính năng sản phẩm
├── setup.bat                    # [1-CLICK] Cài đặt môi trường tự động (Python, CUDA, thư viện)
│
├── Run.bat/                     # THƯ MỤC CHỨA TOÀN BỘ CÁC RUNNER THỰC NGHIỆM CHI TIẾT
│   ├── run.bat                  # Thực nghiệm Bài 1 (Khung thuật toán EVO-RL MSCC)
│   ├── run_bai2.bat             # Thực nghiệm Bài 2 (Đánh giá tính phù hợp DRL)
│   ├── run_bai3.bat             # Thực nghiệm Bài 3 (Phân tích chi phí & Overhead)
│   ├── run_both_bai2_and_bai3.bat # Chạy song song độc lập cả Bài 2 và Bài 3
│   ├── runbieudo.bat            # Xuất biểu đồ chuẩn báo cáo 300 DPI và vector PDF
│   ├── run_tong_hop_so_lieu.bat # Tổng hợp số liệu phân tích và đóng gói báo cáo
│   ├── verify_all.bat           # Bộ kiểm chứng tự động 9 giai đoạn (< 6 giây)
│   └── RUN_ALL.bat              # Phím tắt chuyển tiếp tới CHAY_CHUONG_TRINH_TONG.bat
│
├── configs/                     # Cấu hình siêu tham số giải thuật (khóa cứng chuẩn đối chuẩn)
├── dataset/ & problem/          # Nạp đồ thị, mô hình hóa SClubGraph, Individual, Fitness
├── operators/                   # Toán tử di truyền Crossover, Mutation (Split/Merge/Transfer), Repair
├── rl/ & environment/           # Não bộ Deep RL: Mạng Actor-Critic MLP, MDP Gym Environment, Reward
├── trainer/ & analysis/         # Vòng lặp tiến hóa lai (GGA + PPO), kiểm định thống kê Wilcoxon/Holm
│
├── pbodulieu/                   # Bộ 30 đồ thị benchmark chuẩn (12 mạng thực tế + 18 DIMACS)
├── results/                     # Kết quả Bài 1 (30 đồ thị x 20 seeds x 8 thuật toán)
├── Bai_2_DeepRL_AOS_Suitability/# Kết quả Bài 2 (DRL Suitability & Operator Dynamics)
├── Bai_3_Cost_Benefit_Analysis/ # Kết quả Bài 3 (Cost-Benefit, Breakeven, Time-Budget)
└── Tong_hop_so_lieu_phan_bien/  # Kết quả tổng hợp phản biện Mục 4.4
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
Giao diện hiển thị Menu 10 chức năng (từ 0 đến 9). Quý Thầy/Cô và người dùng chỉ cần nhập số chức năng mong muốn để thực thi (Chạy Bài 1, Bài 2, Bài 3, Xuất biểu đồ, Tổng hợp số liệu, Kiểm chứng...).

#### Cách 2: Kiểm chứng nhanh hệ thống trong 6 giây
Nhấp đúp `Run.bat\verify_all.bat` hoặc chạy lệnh:
```bash
python verify_system.py
```
Hệ thống tự động thực hiện 9 giai đoạn kiểm tra độc lập (phần cứng GPU CUDA, thư viện, nạp đồ thị, toán tử di truyền, mạng PPO, chạy mini test 2 thế hệ).

---

### 5. TÀI LIỆU KÈM THEO
* **Sổ tay hướng dẫn chi tiết dành cho Hội đồng Khoa học:** [HUONG_DAN_HOI_DONG.md](file:///A:/autorc/pcode/Sanpham_nckh/HUONG_DAN_HOI_DONG.md)
* **Danh sách 20 Hạt giống ngẫu nhiên chuẩn quốc tế:** [seedun.md](file:///A:/autorc\pcode\Sanpham_nckh\seedun.md)
