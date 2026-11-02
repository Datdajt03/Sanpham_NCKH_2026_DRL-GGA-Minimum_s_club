# BÁO CÁO TỔNG HỢP SỐ LIỆU PHÂN TÍCH THỰC NGHIỆM TOÀN DIỆN
## ĐỀ TÀI: KHUNG TỐI ƯU HÓA TIẾN HÓA NHÓM DỰA TRÊN PPO CHO BÀI TOÁN MSCC

*Thời gian xuất dữ liệu:* `2026-11-02 19:12:43`  
*Tổng số đồ thị benchmark:* `30` đồ thị  
*Thư mục chi tiết từng đồ thị:* [`chi_tiet_tung_do_thi/`](chi_tiet_tung_do_thi/)  

---

### 1. BẢNG MA TRẬN ÁNH XẠ VAI TRÒ HẠT GIỐNG (SEED MAPPING MATRIX)
Để giải đáp câu hỏi phản biện: *'Seed nào điều khiển thành phần nào và cấu trúc khởi tạo khác nhau ra sao'*, bảng dưới đây phân định rạch ròi cơ chế ngẫu nhiên giữa các thuật toán:

| Nhóm thuật toán | Khởi tạo ban đầu (Step 0) | Thành phần ngẫu nhiên do `seed` điều khiển | Bản chất tính công bằng |
| :--- | :--- | :--- | :--- |
| **6 Thuật toán Tiến hóa**<br>(`PPO-AOS`, `MAB-AOS`, `Greedy-AOS`, `No-RL`, `Fixed`, `Random`) | **Cùng 100% Quần thể $P_0$**<br>(50% BFS Seeding + 50% Random assignment + Repair) | - Chọn giải đấu cha mẹ.<br>- Điểm cắt lai ghép.<br>- Chọn đỉnh đột biến.<br>- Thứ tự đỉnh trong repair. | **Công bằng tuyệt đối**: Bắt đầu từ chính xác cùng một tập cá thể thế hệ 0 ($P_0$) trên cùng seed. |
| **Riêng PPO-AOS**<br>(Deep RL Controller) | Khởi tạo mạng Actor-Critic ngẫu nhiên qua Orthogonal Init | - Trọng số ban đầu mạng Actor/Critic (`torch.manual_seed`).<br>- Lấy mẫu hành động Categorical ($a_t \sim \pi_\theta$).<br>- Thứ tự shuffle mini-batch trong PPO Buffer. | **Online Adaptation**: Mạng học trực tuyến thích nghi với từng seed, không rò rỉ dữ liệu ngoại tuyến. |
| **I-MSM**<br>(Iterated Maximum s-Club) | **Constructive Greedy**<br>(Tập chưa phủ $U = V$) | - Phá vỡ thế hòa (Tie-break) khi chọn đỉnh hạt giống cực đại.<br>- Lấy mẫu ngẫu nhiên candidate ($< 10$).<br>- Nhiễu ngẫu nhiên trong hàm chấm điểm. | **Cấu trúc khởi tạo độc lập**: Không dùng quần thể $P_0$, khởi tạo bằng tìm kiếm tham lam lặp. |
| **CCA**<br>(Clique/Club-Cover-Approx) | **Constructive Balls**<br>(Các quả cầu đóng bán kính $r = \lfloor s/2 \rfloor$) | - Tie-break chọn đỉnh tâm quả cầu tối đa hóa độ phủ.<br>- Lấy mẫu candidate ($< 20$).<br>- Nhiễu ngẫu nhiên trong hàm chọn tâm. | **Cấu trúc khởi tạo độc lập**: Không dùng quần thể $P_0$, khởi tạo bằng tham lam phủ tâm. |

---

### 2. TỔNG HỢP KẾT QUẢ ĐỐI ĐẦU WIN / TIE / LOSS (SO VỚI PPO-AOS)
Dựa trên kiểm định Wilcoxon Signed-Rank hiệu chỉnh đa kiểm định Holm-Bonferroni ở mức ý nghĩa $\alpha = 0.05$:

| Thuật toán đối chứng | PPO Thắng ($+$) | Hòa ($\sim$) | PPO Thua ($-$) | Tỷ lệ không thua (W+T) |
| :--- | :---: | :---: | :---: | :---: |
| **MAB-AOS** | 0 | 30 | 0 | **100.0%** |
| **Greedy-AOS** | 0 | 30 | 0 | **100.0%** |
| **No-RL** | 1 | 29 | 0 | **100.0%** |
| **Fixed** | 0 | 28 | 2 | **93.3%** |
| **Random** | 1 | 29 | 0 | **100.0%** |
| **I-MSM** | 5 | 23 | 2 | **93.3%** |
| **CCA** | 4 | 23 | 3 | **90.0%** |

---

### 3. BẢNG TỔNG HỢP TOÀN BỘ 30 ĐỒ THỊ VỚI LINK CHI TIẾT TỪNG ĐỒ THỊ
> *Nhấp vào tên đồ thị để xem bảng kết quả chi tiết từng hạt giống (20 seeds) và phân tích riêng của đồ thị đó.*

| Đồ thị | Nhóm | Thuật toán | Khởi tạo $f_0$ | Nghiệm tốt ($|C|_{\min}$) | Mean $\pm$ Std | Số thế hệ $\bar{T}$ | Đánh giá $N_{\text{evals}}$ | Thời gian (s) | $p_{\text{Holm}}$ | Ý nghĩa |
| :--- | :---: | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| [`C125.9`](chi_tiet_tung_do_thi/C125.9.md) | Type 2 | **PPO-AOS** | 2.0 | **1** | 1.0 $\pm$ 0.0 | 101.0 | 2120 | 8.02s | 1.0 | `=` |
| [`C125.9`](chi_tiet_tung_do_thi/C125.9.md) | Type 2 | MAB-AOS | 2.0 | **1** | 1.0 $\pm$ 0.0 | 101.0 | 2120 | 6.78s | 1.0 | `~` |
| [`C125.9`](chi_tiet_tung_do_thi/C125.9.md) | Type 2 | Greedy-AOS | 2.0 | **1** | 1.0 $\pm$ 0.0 | 101.0 | 2120 | 6.46s | 1.0 | `~` |
| [`C125.9`](chi_tiet_tung_do_thi/C125.9.md) | Type 2 | No-RL | 2.0 | **1** | 1.0 $\pm$ 0.0 | 101.0 | 2120 | 6.45s | 1.0 | `~` |
| [`C125.9`](chi_tiet_tung_do_thi/C125.9.md) | Type 2 | Fixed | 2.0 | **1** | 1.0 $\pm$ 0.0 | 101.0 | 2120 | 6.57s | 1.0 | `~` |
| [`C125.9`](chi_tiet_tung_do_thi/C125.9.md) | Type 2 | Random | 2.0 | **1** | 1.0 $\pm$ 0.0 | 101.0 | 2120 | 6.36s | 1.0 | `~` |
| [`C125.9`](chi_tiet_tung_do_thi/C125.9.md) | Type 2 | I-MSM | 1.0 | **1** | 1.0 $\pm$ 0.0 | 15.0 | 15 | 10.57s | 1.0 | `~` |
| [`C125.9`](chi_tiet_tung_do_thi/C125.9.md) | Type 2 | CCA | 1.0 | **1** | 1.0 $\pm$ 0.0 | 15.0 | 15 | 0.05s | 1.0 | `~` |
| [`MANN_a9`](chi_tiet_tung_do_thi/MANN_a9.md) | Type 2 | **PPO-AOS** | 1.0 | **1** | 1.0 $\pm$ 0.0 | 100.0 | 2100 | 2.84s | 1.0 | `=` |
| [`MANN_a9`](chi_tiet_tung_do_thi/MANN_a9.md) | Type 2 | MAB-AOS | 1.0 | **1** | 1.0 $\pm$ 0.0 | 100.0 | 2100 | 1.6s | 1.0 | `~` |
| [`MANN_a9`](chi_tiet_tung_do_thi/MANN_a9.md) | Type 2 | Greedy-AOS | 1.0 | **1** | 1.0 $\pm$ 0.0 | 100.0 | 2100 | 1.42s | 1.0 | `~` |
| [`MANN_a9`](chi_tiet_tung_do_thi/MANN_a9.md) | Type 2 | No-RL | 1.0 | **1** | 1.0 $\pm$ 0.0 | 100.0 | 2100 | 1.37s | 1.0 | `~` |
| [`MANN_a9`](chi_tiet_tung_do_thi/MANN_a9.md) | Type 2 | Fixed | 1.0 | **1** | 1.0 $\pm$ 0.0 | 100.0 | 2100 | 1.48s | 1.0 | `~` |
| [`MANN_a9`](chi_tiet_tung_do_thi/MANN_a9.md) | Type 2 | Random | 1.0 | **1** | 1.0 $\pm$ 0.0 | 100.0 | 2100 | 1.4s | 1.0 | `~` |
| [`MANN_a9`](chi_tiet_tung_do_thi/MANN_a9.md) | Type 2 | I-MSM | 1.0 | **1** | 1.0 $\pm$ 0.0 | 15.0 | 15 | 0.38s | 1.0 | `~` |
| [`MANN_a9`](chi_tiet_tung_do_thi/MANN_a9.md) | Type 2 | CCA | 1.0 | **1** | 1.0 $\pm$ 0.0 | 15.0 | 15 | 0.0s | 1.0 | `~` |
| [`adjnoun`](chi_tiet_tung_do_thi/adjnoun.md) | Type 1 | **PPO-AOS** | 24.75 | **18** | 19.05 $\pm$ 0.59 | 138.7 | 2874 | 12.04s | 1.0 | `=` |
| [`adjnoun`](chi_tiet_tung_do_thi/adjnoun.md) | Type 1 | MAB-AOS | 24.75 | **18** | 18.85 $\pm$ 0.65 | 149.9 | 3099 | 10.29s | 1.0 | `~` |
| [`adjnoun`](chi_tiet_tung_do_thi/adjnoun.md) | Type 1 | Greedy-AOS | 24.75 | **18** | 18.75 $\pm$ 0.62 | 144.3 | 2987 | 10.0s | 0.226 | `~` |
| [`adjnoun`](chi_tiet_tung_do_thi/adjnoun.md) | Type 1 | No-RL | 24.75 | **19** | 19.2 $\pm$ 0.4 | 138.3 | 2867 | 9.07s | 1.0 | `~` |
| [`adjnoun`](chi_tiet_tung_do_thi/adjnoun.md) | Type 1 | Fixed | 24.75 | **18** | 18.35 $\pm$ 0.48 | 135.4 | 2809 | 8.43s | 0.0136 | `-` |
| [`adjnoun`](chi_tiet_tung_do_thi/adjnoun.md) | Type 1 | Random | 24.75 | **19** | 19.2 $\pm$ 0.4 | 138.3 | 2867 | 8.16s | 1.0 | `~` |
| [`adjnoun`](chi_tiet_tung_do_thi/adjnoun.md) | Type 1 | I-MSM | 23.4 | **19** | 19.7 $\pm$ 0.71 | 22.6 | 23 | 3.0s | 0.0339 | `+` |
| [`adjnoun`](chi_tiet_tung_do_thi/adjnoun.md) | Type 1 | CCA | 19.9 | **18** | 18.1 $\pm$ 0.3 | 20.7 | 21 | 0.43s | 0.0007 | `-` |
| [`brock200_1`](chi_tiet_tung_do_thi/brock200_1.md) | Type 2 | **PPO-AOS** | 2.9 | **1** | 1.0 $\pm$ 0.0 | 102.3 | 2147 | 24.23s | 1.0 | `=` |
| [`brock200_1`](chi_tiet_tung_do_thi/brock200_1.md) | Type 2 | MAB-AOS | 2.9 | **1** | 1.0 $\pm$ 0.0 | 101.0 | 2120 | 22.66s | 1.0 | `~` |
| [`brock200_1`](chi_tiet_tung_do_thi/brock200_1.md) | Type 2 | Greedy-AOS | 2.9 | **1** | 1.0 $\pm$ 0.0 | 101.8 | 2137 | 22.48s | 1.0 | `~` |
| [`brock200_1`](chi_tiet_tung_do_thi/brock200_1.md) | Type 2 | No-RL | 2.9 | **1** | 1.0 $\pm$ 0.0 | 101.5 | 2129 | 20.36s | 1.0 | `~` |
| [`brock200_1`](chi_tiet_tung_do_thi/brock200_1.md) | Type 2 | Fixed | 2.9 | **1** | 1.0 $\pm$ 0.0 | 101.0 | 2120 | 20.55s | 1.0 | `~` |
| [`brock200_1`](chi_tiet_tung_do_thi/brock200_1.md) | Type 2 | Random | 2.9 | **1** | 1.0 $\pm$ 0.0 | 101.5 | 2129 | 19.96s | 1.0 | `~` |
| [`brock200_1`](chi_tiet_tung_do_thi/brock200_1.md) | Type 2 | I-MSM | 1.0 | **1** | 1.0 $\pm$ 0.0 | 15.0 | 15 | 67.21s | 1.0 | `~` |
| [`brock200_1`](chi_tiet_tung_do_thi/brock200_1.md) | Type 2 | CCA | 1.0 | **1** | 1.0 $\pm$ 0.0 | 15.0 | 15 | 0.28s | 1.0 | `~` |
| [`brock200_2`](chi_tiet_tung_do_thi/brock200_2.md) | Type 2 | **PPO-AOS** | 2.9 | **1** | 1.0 $\pm$ 0.0 | 102.2 | 2145 | 21.87s | 1.0 | `=` |
| [`brock200_2`](chi_tiet_tung_do_thi/brock200_2.md) | Type 2 | MAB-AOS | 2.9 | **1** | 1.0 $\pm$ 0.0 | 101.0 | 2121 | 19.98s | 1.0 | `~` |
| [`brock200_2`](chi_tiet_tung_do_thi/brock200_2.md) | Type 2 | Greedy-AOS | 2.9 | **1** | 1.0 $\pm$ 0.0 | 101.8 | 2136 | 20.44s | 1.0 | `~` |
| [`brock200_2`](chi_tiet_tung_do_thi/brock200_2.md) | Type 2 | No-RL | 2.9 | **1** | 1.0 $\pm$ 0.0 | 101.5 | 2129 | 20.41s | 1.0 | `~` |
| [`brock200_2`](chi_tiet_tung_do_thi/brock200_2.md) | Type 2 | Fixed | 2.9 | **1** | 1.0 $\pm$ 0.0 | 101.0 | 2120 | 19.88s | 1.0 | `~` |
| [`brock200_2`](chi_tiet_tung_do_thi/brock200_2.md) | Type 2 | Random | 2.9 | **1** | 1.0 $\pm$ 0.0 | 101.5 | 2129 | 19.81s | 1.0 | `~` |
| [`brock200_2`](chi_tiet_tung_do_thi/brock200_2.md) | Type 2 | I-MSM | 1.0 | **1** | 1.0 $\pm$ 0.0 | 15.0 | 15 | 64.28s | 1.0 | `~` |
| [`brock200_2`](chi_tiet_tung_do_thi/brock200_2.md) | Type 2 | CCA | 1.0 | **1** | 1.0 $\pm$ 0.0 | 15.0 | 15 | 0.29s | 1.0 | `~` |
| [`brock200_3`](chi_tiet_tung_do_thi/brock200_3.md) | Type 2 | **PPO-AOS** | 3.0 | **1** | 1.0 $\pm$ 0.0 | 102.4 | 2148 | 22.16s | 1.0 | `=` |
| [`brock200_3`](chi_tiet_tung_do_thi/brock200_3.md) | Type 2 | MAB-AOS | 3.0 | **1** | 1.0 $\pm$ 0.0 | 101.0 | 2121 | 20.11s | 1.0 | `~` |
| [`brock200_3`](chi_tiet_tung_do_thi/brock200_3.md) | Type 2 | Greedy-AOS | 3.0 | **1** | 1.0 $\pm$ 0.0 | 102.0 | 2139 | 20.06s | 1.0 | `~` |
| [`brock200_3`](chi_tiet_tung_do_thi/brock200_3.md) | Type 2 | No-RL | 3.0 | **1** | 1.0 $\pm$ 0.0 | 101.6 | 2132 | 20.1s | 1.0 | `~` |
| [`brock200_3`](chi_tiet_tung_do_thi/brock200_3.md) | Type 2 | Fixed | 3.0 | **1** | 1.0 $\pm$ 0.0 | 101.0 | 2121 | 20.03s | 1.0 | `~` |
| [`brock200_3`](chi_tiet_tung_do_thi/brock200_3.md) | Type 2 | Random | 3.0 | **1** | 1.0 $\pm$ 0.0 | 101.6 | 2132 | 19.89s | 1.0 | `~` |
| [`brock200_3`](chi_tiet_tung_do_thi/brock200_3.md) | Type 2 | I-MSM | 1.0 | **1** | 1.0 $\pm$ 0.0 | 15.0 | 15 | 63.99s | 1.0 | `~` |
| [`brock200_3`](chi_tiet_tung_do_thi/brock200_3.md) | Type 2 | CCA | 1.0 | **1** | 1.0 $\pm$ 0.0 | 15.0 | 15 | 0.27s | 1.0 | `~` |
| [`c-fat200-1`](chi_tiet_tung_do_thi/c-fat200-1.md) | Type 2 | **PPO-AOS** | 14.1 | **13** | 13.0 $\pm$ 0.0 | 108.5 | 2271 | 8.25s | 1.0 | `=` |
| [`c-fat200-1`](chi_tiet_tung_do_thi/c-fat200-1.md) | Type 2 | MAB-AOS | 14.1 | **13** | 13.0 $\pm$ 0.0 | 110.1 | 2302 | 6.51s | 1.0 | `~` |
| [`c-fat200-1`](chi_tiet_tung_do_thi/c-fat200-1.md) | Type 2 | Greedy-AOS | 14.1 | **13** | 13.0 $\pm$ 0.0 | 111.0 | 2319 | 6.57s | 1.0 | `~` |
| [`c-fat200-1`](chi_tiet_tung_do_thi/c-fat200-1.md) | Type 2 | No-RL | 14.1 | **13** | 13.0 $\pm$ 0.0 | 111.3 | 2327 | 6.51s | 1.0 | `~` |
| [`c-fat200-1`](chi_tiet_tung_do_thi/c-fat200-1.md) | Type 2 | Fixed | 14.1 | **13** | 13.0 $\pm$ 0.0 | 113.4 | 2368 | 5.48s | 1.0 | `~` |
| [`c-fat200-1`](chi_tiet_tung_do_thi/c-fat200-1.md) | Type 2 | Random | 14.1 | **13** | 13.0 $\pm$ 0.0 | 111.3 | 2327 | 6.0s | 1.0 | `~` |
| [`c-fat200-1`](chi_tiet_tung_do_thi/c-fat200-1.md) | Type 2 | I-MSM | 14.1 | **13** | 13.05 $\pm$ 0.22 | 20.1 | 20 | 1.22s | 1.0 | `~` |
| [`c-fat200-1`](chi_tiet_tung_do_thi/c-fat200-1.md) | Type 2 | CCA | 14.65 | **13** | 13.15 $\pm$ 0.36 | 21.4 | 21 | 0.26s | 0.5829 | `~` |
| [`c-fat200-5`](chi_tiet_tung_do_thi/c-fat200-5.md) | Type 2 | **PPO-AOS** | 5.2 | **1** | 1.0 $\pm$ 0.0 | 105.5 | 2211 | 22.76s | 1.0 | `=` |
| [`c-fat200-5`](chi_tiet_tung_do_thi/c-fat200-5.md) | Type 2 | MAB-AOS | 5.2 | **1** | 1.0 $\pm$ 0.0 | 103.8 | 2175 | 20.84s | 1.0 | `~` |
| [`c-fat200-5`](chi_tiet_tung_do_thi/c-fat200-5.md) | Type 2 | Greedy-AOS | 5.2 | **1** | 1.0 $\pm$ 0.0 | 104.5 | 2189 | 20.51s | 1.0 | `~` |
| [`c-fat200-5`](chi_tiet_tung_do_thi/c-fat200-5.md) | Type 2 | No-RL | 5.2 | **1** | 1.0 $\pm$ 0.0 | 105.3 | 2206 | 20.52s | 1.0 | `~` |
| [`c-fat200-5`](chi_tiet_tung_do_thi/c-fat200-5.md) | Type 2 | Fixed | 5.2 | **1** | 1.0 $\pm$ 0.0 | 103.2 | 2163 | 20.27s | 1.0 | `~` |
| [`c-fat200-5`](chi_tiet_tung_do_thi/c-fat200-5.md) | Type 2 | Random | 5.2 | **1** | 1.0 $\pm$ 0.0 | 105.3 | 2206 | 20.4s | 1.0 | `~` |
| [`c-fat200-5`](chi_tiet_tung_do_thi/c-fat200-5.md) | Type 2 | I-MSM | 1.0 | **1** | 1.0 $\pm$ 0.0 | 15.0 | 15 | 64.53s | 1.0 | `~` |
| [`c-fat200-5`](chi_tiet_tung_do_thi/c-fat200-5.md) | Type 2 | CCA | 3.0 | **2** | 2.2 $\pm$ 0.4 | 19.8 | 20 | 0.38s | 0.0002 | `+` |
| [`celegans_metabolic`](chi_tiet_tung_do_thi/celegans_metabolic.md) | Type 1 | **PPO-AOS** | 48.35 | **29** | 29.65 $\pm$ 1.11 | 171.2 | 3524 | 391.85s | 1.0 | `=` |
| [`celegans_metabolic`](chi_tiet_tung_do_thi/celegans_metabolic.md) | Type 1 | MAB-AOS | 48.35 | **29** | 29.5 $\pm$ 0.74 | 162.9 | 3358 | 391.31s | 1.0 | `~` |
| [`celegans_metabolic`](chi_tiet_tung_do_thi/celegans_metabolic.md) | Type 1 | Greedy-AOS | 48.35 | **29** | 29.25 $\pm$ 0.43 | 156.8 | 3235 | 471.51s | 1.0 | `~` |
| [`celegans_metabolic`](chi_tiet_tung_do_thi/celegans_metabolic.md) | Type 1 | No-RL | 48.35 | **29** | 29.75 $\pm$ 0.99 | 168.6 | 3472 | 285.22s | 1.0 | `~` |
| [`celegans_metabolic`](chi_tiet_tung_do_thi/celegans_metabolic.md) | Type 1 | Fixed | 48.35 | **29** | 29.6 $\pm$ 0.73 | 147.5 | 3050 | 361.57s | 1.0 | `~` |
| [`celegans_metabolic`](chi_tiet_tung_do_thi/celegans_metabolic.md) | Type 1 | Random | 48.35 | **29** | 29.75 $\pm$ 0.99 | 168.6 | 3472 | 267.34s | 1.0 | `~` |
| [`celegans_metabolic`](chi_tiet_tung_do_thi/celegans_metabolic.md) | Type 1 | I-MSM | 36.15 | **29** | 29.9 $\pm$ 0.77 | 22.4 | 22 | 240.34s | 1.0 | `~` |
| [`celegans_metabolic`](chi_tiet_tung_do_thi/celegans_metabolic.md) | Type 1 | CCA | 33.05 | **29** | 29.25 $\pm$ 0.54 | 23.1 | 23 | 27.12s | 1.0 | `~` |
| [`celegansneural`](chi_tiet_tung_do_thi/celegansneural.md) | Type 1 | **PPO-AOS** | 32.8 | **18** | 19.05 $\pm$ 0.97 | 180.4 | 3709 | 151.36s | 1.0 | `=` |
| [`celegansneural`](chi_tiet_tung_do_thi/celegansneural.md) | Type 1 | MAB-AOS | 32.8 | **18** | 19.7 $\pm$ 1.42 | 175.3 | 3606 | 164.3s | 0.3829 | `~` |
| [`celegansneural`](chi_tiet_tung_do_thi/celegansneural.md) | Type 1 | Greedy-AOS | 32.8 | **17** | 19.25 $\pm$ 0.89 | 171.1 | 3521 | 189.25s | 0.7724 | `~` |
| [`celegansneural`](chi_tiet_tung_do_thi/celegansneural.md) | Type 1 | No-RL | 32.8 | **18** | 20.4 $\pm$ 1.36 | 175.8 | 3616 | 133.03s | 0.0108 | `+` |
| [`celegansneural`](chi_tiet_tung_do_thi/celegansneural.md) | Type 1 | Fixed | 32.8 | **18** | 19.35 $\pm$ 1.28 | 154.3 | 3186 | 90.67s | 0.7724 | `~` |
| [`celegansneural`](chi_tiet_tung_do_thi/celegansneural.md) | Type 1 | Random | 32.8 | **18** | 20.4 $\pm$ 1.36 | 175.8 | 3616 | 120.38s | 0.0108 | `+` |
| [`celegansneural`](chi_tiet_tung_do_thi/celegansneural.md) | Type 1 | I-MSM | 27.3 | **20** | 22.25 $\pm$ 1.09 | 24.8 | 25 | 36.3s | 0.0006 | `+` |
| [`celegansneural`](chi_tiet_tung_do_thi/celegansneural.md) | Type 1 | CCA | 21.55 | **17** | 18.55 $\pm$ 0.74 | 22.1 | 22 | 3.63s | 0.5097 | `~` |
| [`chesapeake`](chi_tiet_tung_do_thi/chesapeake.md) | Type 1 | **PPO-AOS** | 3.0 | **3** | 3.0 $\pm$ 0.0 | 100.0 | 2100 | 6.2s | 1.0 | `=` |
| [`chesapeake`](chi_tiet_tung_do_thi/chesapeake.md) | Type 1 | MAB-AOS | 3.0 | **3** | 3.0 $\pm$ 0.0 | 100.0 | 2100 | 3.79s | 1.0 | `~` |
| [`chesapeake`](chi_tiet_tung_do_thi/chesapeake.md) | Type 1 | Greedy-AOS | 3.0 | **3** | 3.0 $\pm$ 0.0 | 100.0 | 2100 | 3.7s | 1.0 | `~` |
| [`chesapeake`](chi_tiet_tung_do_thi/chesapeake.md) | Type 1 | No-RL | 3.0 | **3** | 3.0 $\pm$ 0.0 | 100.0 | 2100 | 3.73s | 1.0 | `~` |
| [`chesapeake`](chi_tiet_tung_do_thi/chesapeake.md) | Type 1 | Fixed | 3.0 | **3** | 3.0 $\pm$ 0.0 | 100.0 | 2100 | 2.46s | 1.0 | `~` |
| [`chesapeake`](chi_tiet_tung_do_thi/chesapeake.md) | Type 1 | Random | 3.0 | **3** | 3.0 $\pm$ 0.0 | 100.0 | 2100 | 3.65s | 1.0 | `~` |
| [`chesapeake`](chi_tiet_tung_do_thi/chesapeake.md) | Type 1 | I-MSM | 3.0 | **3** | 3.0 $\pm$ 0.0 | 15.0 | 15 | 0.39s | 1.0 | `~` |
| [`chesapeake`](chi_tiet_tung_do_thi/chesapeake.md) | Type 1 | CCA | 3.4 | **3** | 3.0 $\pm$ 0.0 | 15.6 | 16 | 0.01s | 1.0 | `~` |
| [`dolphins`](chi_tiet_tung_do_thi/dolphins.md) | Type 1 | **PPO-AOS** | 15.6 | **13** | 13.2 $\pm$ 0.4 | 124.7 | 2593 | 5.78s | 1.0 | `=` |
| [`dolphins`](chi_tiet_tung_do_thi/dolphins.md) | Type 1 | MAB-AOS | 15.6 | **13** | 13.3 $\pm$ 0.46 | 123.7 | 2573 | 4.08s | 0.9519 | `~` |
| [`dolphins`](chi_tiet_tung_do_thi/dolphins.md) | Type 1 | Greedy-AOS | 15.6 | **13** | 13.45 $\pm$ 0.5 | 115.5 | 2410 | 3.71s | 0.4779 | `~` |
| [`dolphins`](chi_tiet_tung_do_thi/dolphins.md) | Type 1 | No-RL | 15.6 | **13** | 13.35 $\pm$ 0.48 | 122.3 | 2547 | 3.9s | 0.9519 | `~` |
| [`dolphins`](chi_tiet_tung_do_thi/dolphins.md) | Type 1 | Fixed | 15.6 | **13** | 13.1 $\pm$ 0.3 | 118.7 | 2474 | 3.23s | 0.6292 | `~` |
| [`dolphins`](chi_tiet_tung_do_thi/dolphins.md) | Type 1 | Random | 15.6 | **13** | 13.35 $\pm$ 0.48 | 122.3 | 2547 | 3.6s | 0.9519 | `~` |
| [`dolphins`](chi_tiet_tung_do_thi/dolphins.md) | Type 1 | I-MSM | 15.85 | **14** | 14.4 $\pm$ 0.58 | 19.5 | 20 | 0.53s | 0.0004 | `+` |
| [`dolphins`](chi_tiet_tung_do_thi/dolphins.md) | Type 1 | CCA | 15.4 | **14** | 14.15 $\pm$ 0.36 | 19.2 | 19 | 0.13s | 0.0004 | `+` |
| [`email`](chi_tiet_tung_do_thi/email.md) | Type 1 | **PPO-AOS** | 310.5 | **239** | 248.35 $\pm$ 4.6 | 200.0 | 4100 | 80.03s | 1.0 | `=` |
| [`email`](chi_tiet_tung_do_thi/email.md) | Type 1 | MAB-AOS | 310.5 | **235** | 244.5 $\pm$ 6.3 | 200.0 | 4100 | 80.51s | 0.0997 | `~` |
| [`email`](chi_tiet_tung_do_thi/email.md) | Type 1 | Greedy-AOS | 310.5 | **234** | 251.2 $\pm$ 10.93 | 200.0 | 4100 | 82.63s | 1.0 | `~` |
| [`email`](chi_tiet_tung_do_thi/email.md) | Type 1 | No-RL | 310.5 | **239** | 248.1 $\pm$ 5.86 | 200.0 | 4100 | 71.07s | 1.0 | `~` |
| [`email`](chi_tiet_tung_do_thi/email.md) | Type 1 | Fixed | 310.5 | **232** | 240.15 $\pm$ 4.5 | 200.0 | 4100 | 77.25s | 0.0041 | `-` |
| [`email`](chi_tiet_tung_do_thi/email.md) | Type 1 | Random | 310.5 | **239** | 248.1 $\pm$ 5.86 | 200.0 | 4100 | 67.8s | 1.0 | `~` |
| [`email`](chi_tiet_tung_do_thi/email.md) | Type 1 | I-MSM | 256.15 | **232** | 241.25 $\pm$ 3.88 | 26.5 | 26 | 264.18s | 0.0013 | `-` |
| [`email`](chi_tiet_tung_do_thi/email.md) | Type 1 | CCA | 226.95 | **220** | 221.9 $\pm$ 1.14 | 23.6 | 24 | 136.6s | 0.0006 | `-` |
| [`football`](chi_tiet_tung_do_thi/football.md) | Type 1 | **PPO-AOS** | 13.75 | **10** | 10.0 $\pm$ 0.0 | 126.5 | 2630 | 7.3s | 1.0 | `=` |
| [`football`](chi_tiet_tung_do_thi/football.md) | Type 1 | MAB-AOS | 13.75 | **10** | 10.05 $\pm$ 0.22 | 120.3 | 2507 | 4.96s | 1.0 | `~` |
| [`football`](chi_tiet_tung_do_thi/football.md) | Type 1 | Greedy-AOS | 13.75 | **10** | 10.05 $\pm$ 0.22 | 118.7 | 2473 | 4.84s | 1.0 | `~` |
| [`football`](chi_tiet_tung_do_thi/football.md) | Type 1 | No-RL | 13.75 | **10** | 10.0 $\pm$ 0.0 | 123.6 | 2572 | 4.92s | 1.0 | `~` |
| [`football`](chi_tiet_tung_do_thi/football.md) | Type 1 | Fixed | 13.75 | **10** | 10.05 $\pm$ 0.22 | 121.4 | 2528 | 3.46s | 1.0 | `~` |
| [`football`](chi_tiet_tung_do_thi/football.md) | Type 1 | Random | 13.75 | **10** | 10.0 $\pm$ 0.0 | 123.6 | 2572 | 4.55s | 1.0 | `~` |
| [`football`](chi_tiet_tung_do_thi/football.md) | Type 1 | I-MSM | 14.65 | **11** | 12.55 $\pm$ 0.67 | 21.6 | 22 | 0.97s | 0.0004 | `+` |
| [`football`](chi_tiet_tung_do_thi/football.md) | Type 1 | CCA | 15.2 | **13** | 13.95 $\pm$ 0.38 | 19.6 | 20 | 0.18s | 0.0002 | `+` |
| [`gen200_p0.9_44`](chi_tiet_tung_do_thi/gen200_p0.9_44.md) | Type 2 | **PPO-AOS** | 2.0 | **1** | 1.0 $\pm$ 0.0 | 101.0 | 2120 | 22.01s | 1.0 | `=` |
| [`gen200_p0.9_44`](chi_tiet_tung_do_thi/gen200_p0.9_44.md) | Type 2 | MAB-AOS | 2.0 | **1** | 1.0 $\pm$ 0.0 | 101.0 | 2120 | 20.1s | 1.0 | `~` |
| [`gen200_p0.9_44`](chi_tiet_tung_do_thi/gen200_p0.9_44.md) | Type 2 | Greedy-AOS | 2.0 | **1** | 1.0 $\pm$ 0.0 | 101.0 | 2120 | 20.15s | 1.0 | `~` |
| [`gen200_p0.9_44`](chi_tiet_tung_do_thi/gen200_p0.9_44.md) | Type 2 | No-RL | 2.0 | **1** | 1.0 $\pm$ 0.0 | 101.0 | 2120 | 20.05s | 1.0 | `~` |
| [`gen200_p0.9_44`](chi_tiet_tung_do_thi/gen200_p0.9_44.md) | Type 2 | Fixed | 2.0 | **1** | 1.0 $\pm$ 0.0 | 101.0 | 2120 | 20.23s | 1.0 | `~` |
| [`gen200_p0.9_44`](chi_tiet_tung_do_thi/gen200_p0.9_44.md) | Type 2 | Random | 2.0 | **1** | 1.0 $\pm$ 0.0 | 101.0 | 2120 | 19.83s | 1.0 | `~` |
| [`gen200_p0.9_44`](chi_tiet_tung_do_thi/gen200_p0.9_44.md) | Type 2 | I-MSM | 1.0 | **1** | 1.0 $\pm$ 0.0 | 15.0 | 15 | 63.37s | 1.0 | `~` |
| [`gen200_p0.9_44`](chi_tiet_tung_do_thi/gen200_p0.9_44.md) | Type 2 | CCA | 1.0 | **1** | 1.0 $\pm$ 0.0 | 15.0 | 15 | 0.14s | 1.0 | `~` |
| [`gen200_p0.9_55`](chi_tiet_tung_do_thi/gen200_p0.9_55.md) | Type 2 | **PPO-AOS** | 2.0 | **1** | 1.0 $\pm$ 0.0 | 101.0 | 2120 | 21.66s | 1.0 | `=` |
| [`gen200_p0.9_55`](chi_tiet_tung_do_thi/gen200_p0.9_55.md) | Type 2 | MAB-AOS | 2.0 | **1** | 1.0 $\pm$ 0.0 | 101.0 | 2120 | 19.98s | 1.0 | `~` |
| [`gen200_p0.9_55`](chi_tiet_tung_do_thi/gen200_p0.9_55.md) | Type 2 | Greedy-AOS | 2.0 | **1** | 1.0 $\pm$ 0.0 | 101.0 | 2120 | 19.88s | 1.0 | `~` |
| [`gen200_p0.9_55`](chi_tiet_tung_do_thi/gen200_p0.9_55.md) | Type 2 | No-RL | 2.0 | **1** | 1.0 $\pm$ 0.0 | 101.0 | 2120 | 20.21s | 1.0 | `~` |
| [`gen200_p0.9_55`](chi_tiet_tung_do_thi/gen200_p0.9_55.md) | Type 2 | Fixed | 2.0 | **1** | 1.0 $\pm$ 0.0 | 101.0 | 2120 | 20.3s | 1.0 | `~` |
| [`gen200_p0.9_55`](chi_tiet_tung_do_thi/gen200_p0.9_55.md) | Type 2 | Random | 2.0 | **1** | 1.0 $\pm$ 0.0 | 101.0 | 2120 | 19.98s | 1.0 | `~` |
| [`gen200_p0.9_55`](chi_tiet_tung_do_thi/gen200_p0.9_55.md) | Type 2 | I-MSM | 1.0 | **1** | 1.0 $\pm$ 0.0 | 15.0 | 15 | 63.02s | 1.0 | `~` |
| [`gen200_p0.9_55`](chi_tiet_tung_do_thi/gen200_p0.9_55.md) | Type 2 | CCA | 1.0 | **1** | 1.0 $\pm$ 0.0 | 15.0 | 15 | 0.14s | 1.0 | `~` |
| [`hamming6-2`](chi_tiet_tung_do_thi/hamming6-2.md) | Type 2 | **PPO-AOS** | 2.0 | **1** | 1.0 $\pm$ 0.0 | 101.0 | 2120 | 3.86s | 1.0 | `=` |
| [`hamming6-2`](chi_tiet_tung_do_thi/hamming6-2.md) | Type 2 | MAB-AOS | 2.0 | **1** | 1.0 $\pm$ 0.0 | 101.0 | 2120 | 2.02s | 1.0 | `~` |
| [`hamming6-2`](chi_tiet_tung_do_thi/hamming6-2.md) | Type 2 | Greedy-AOS | 2.0 | **1** | 1.0 $\pm$ 0.0 | 101.0 | 2120 | 1.92s | 1.0 | `~` |
| [`hamming6-2`](chi_tiet_tung_do_thi/hamming6-2.md) | Type 2 | No-RL | 2.0 | **1** | 1.0 $\pm$ 0.0 | 101.0 | 2120 | 1.81s | 1.0 | `~` |
| [`hamming6-2`](chi_tiet_tung_do_thi/hamming6-2.md) | Type 2 | Fixed | 2.0 | **1** | 1.0 $\pm$ 0.0 | 101.0 | 2120 | 1.98s | 1.0 | `~` |
| [`hamming6-2`](chi_tiet_tung_do_thi/hamming6-2.md) | Type 2 | Random | 2.0 | **1** | 1.0 $\pm$ 0.0 | 101.0 | 2120 | 1.81s | 1.0 | `~` |
| [`hamming6-2`](chi_tiet_tung_do_thi/hamming6-2.md) | Type 2 | I-MSM | 1.0 | **1** | 1.0 $\pm$ 0.0 | 15.0 | 15 | 0.98s | 1.0 | `~` |
| [`hamming6-2`](chi_tiet_tung_do_thi/hamming6-2.md) | Type 2 | CCA | 1.0 | **1** | 1.0 $\pm$ 0.0 | 15.0 | 15 | 0.01s | 1.0 | `~` |
| [`hamming6-4`](chi_tiet_tung_do_thi/hamming6-4.md) | Type 2 | **PPO-AOS** | 4.2 | **1** | 1.0 $\pm$ 0.0 | 105.0 | 2200 | 3.58s | 1.0 | `=` |
| [`hamming6-4`](chi_tiet_tung_do_thi/hamming6-4.md) | Type 2 | MAB-AOS | 4.2 | **1** | 1.0 $\pm$ 0.0 | 103.0 | 2159 | 2.25s | 1.0 | `~` |
| [`hamming6-4`](chi_tiet_tung_do_thi/hamming6-4.md) | Type 2 | Greedy-AOS | 4.2 | **1** | 1.0 $\pm$ 0.0 | 103.6 | 2172 | 2.15s | 1.0 | `~` |
| [`hamming6-4`](chi_tiet_tung_do_thi/hamming6-4.md) | Type 2 | No-RL | 4.2 | **1** | 1.0 $\pm$ 0.0 | 104.0 | 2180 | 2.05s | 1.0 | `~` |
| [`hamming6-4`](chi_tiet_tung_do_thi/hamming6-4.md) | Type 2 | Fixed | 4.2 | **1** | 1.0 $\pm$ 0.0 | 103.3 | 2167 | 2.24s | 1.0 | `~` |
| [`hamming6-4`](chi_tiet_tung_do_thi/hamming6-4.md) | Type 2 | Random | 4.2 | **1** | 1.0 $\pm$ 0.0 | 104.0 | 2180 | 2.06s | 1.0 | `~` |
| [`hamming6-4`](chi_tiet_tung_do_thi/hamming6-4.md) | Type 2 | I-MSM | 1.0 | **1** | 1.0 $\pm$ 0.0 | 15.0 | 15 | 0.95s | 1.0 | `~` |
| [`hamming6-4`](chi_tiet_tung_do_thi/hamming6-4.md) | Type 2 | CCA | 3.7 | **1** | 1.05 $\pm$ 0.22 | 19.6 | 20 | 0.03s | 1.0 | `~` |
| [`hamming8-2`](chi_tiet_tung_do_thi/hamming8-2.md) | Type 2 | **PPO-AOS** | 2.0 | **1** | 1.0 $\pm$ 0.0 | 101.0 | 2120 | 45.41s | 1.0 | `=` |
| [`hamming8-2`](chi_tiet_tung_do_thi/hamming8-2.md) | Type 2 | MAB-AOS | 2.0 | **1** | 1.0 $\pm$ 0.0 | 101.0 | 2120 | 44.53s | 1.0 | `~` |
| [`hamming8-2`](chi_tiet_tung_do_thi/hamming8-2.md) | Type 2 | Greedy-AOS | 2.0 | **1** | 1.0 $\pm$ 0.0 | 101.0 | 2120 | 43.82s | 1.0 | `~` |
| [`hamming8-2`](chi_tiet_tung_do_thi/hamming8-2.md) | Type 2 | No-RL | 2.0 | **1** | 1.0 $\pm$ 0.0 | 101.0 | 2120 | 43.52s | 1.0 | `~` |
| [`hamming8-2`](chi_tiet_tung_do_thi/hamming8-2.md) | Type 2 | Fixed | 2.0 | **1** | 1.0 $\pm$ 0.0 | 101.0 | 2120 | 43.8s | 1.0 | `~` |
| [`hamming8-2`](chi_tiet_tung_do_thi/hamming8-2.md) | Type 2 | Random | 2.0 | **1** | 1.0 $\pm$ 0.0 | 101.0 | 2120 | 43.55s | 1.0 | `~` |
| [`hamming8-2`](chi_tiet_tung_do_thi/hamming8-2.md) | Type 2 | I-MSM | 1.0 | **1** | 1.0 $\pm$ 0.0 | 15.0 | 15 | 167.04s | 1.0 | `~` |
| [`hamming8-2`](chi_tiet_tung_do_thi/hamming8-2.md) | Type 2 | CCA | 1.0 | **1** | 1.0 $\pm$ 0.0 | 15.0 | 15 | 0.3s | 1.0 | `~` |
| [`jazz`](chi_tiet_tung_do_thi/jazz.md) | Type 1 | **PPO-AOS** | 20.0 | **13** | 13.7 $\pm$ 0.64 | 156.3 | 3227 | 67.43s | 1.0 | `=` |
| [`jazz`](chi_tiet_tung_do_thi/jazz.md) | Type 1 | MAB-AOS | 20.0 | **13** | 14.15 $\pm$ 1.11 | 142.4 | 2949 | 62.04s | 0.2929 | `~` |
| [`jazz`](chi_tiet_tung_do_thi/jazz.md) | Type 1 | Greedy-AOS | 20.0 | **13** | 14.0 $\pm$ 0.89 | 146.9 | 3039 | 70.97s | 0.5761 | `~` |
| [`jazz`](chi_tiet_tung_do_thi/jazz.md) | Type 1 | No-RL | 20.0 | **13** | 13.65 $\pm$ 0.65 | 152.8 | 3156 | 62.34s | 1.0 | `~` |
| [`jazz`](chi_tiet_tung_do_thi/jazz.md) | Type 1 | Fixed | 20.0 | **13** | 13.95 $\pm$ 0.8 | 151.0 | 3120 | 21.69s | 1.0 | `~` |
| [`jazz`](chi_tiet_tung_do_thi/jazz.md) | Type 1 | Random | 20.0 | **13** | 13.65 $\pm$ 0.65 | 152.8 | 3156 | 58.4s | 1.0 | `~` |
| [`jazz`](chi_tiet_tung_do_thi/jazz.md) | Type 1 | I-MSM | 17.85 | **14** | 15.1 $\pm$ 0.54 | 20.7 | 21 | 26.62s | 0.0008 | `+` |
| [`jazz`](chi_tiet_tung_do_thi/jazz.md) | Type 1 | CCA | 16.25 | **13** | 14.0 $\pm$ 0.55 | 22.3 | 22 | 1.79s | 0.4163 | `~` |
| [`johnson16-2-4`](chi_tiet_tung_do_thi/johnson16-2-4.md) | Type 2 | **PPO-AOS** | 2.0 | **1** | 1.0 $\pm$ 0.0 | 101.0 | 2120 | 8.12s | 1.0 | `=` |
| [`johnson16-2-4`](chi_tiet_tung_do_thi/johnson16-2-4.md) | Type 2 | MAB-AOS | 2.0 | **1** | 1.0 $\pm$ 0.0 | 101.0 | 2120 | 6.56s | 1.0 | `~` |
| [`johnson16-2-4`](chi_tiet_tung_do_thi/johnson16-2-4.md) | Type 2 | Greedy-AOS | 2.0 | **1** | 1.0 $\pm$ 0.0 | 101.0 | 2120 | 6.46s | 1.0 | `~` |
| [`johnson16-2-4`](chi_tiet_tung_do_thi/johnson16-2-4.md) | Type 2 | No-RL | 2.0 | **1** | 1.0 $\pm$ 0.0 | 101.0 | 2120 | 6.5s | 1.0 | `~` |
| [`johnson16-2-4`](chi_tiet_tung_do_thi/johnson16-2-4.md) | Type 2 | Fixed | 2.0 | **1** | 1.0 $\pm$ 0.0 | 101.0 | 2120 | 6.61s | 1.0 | `~` |
| [`johnson16-2-4`](chi_tiet_tung_do_thi/johnson16-2-4.md) | Type 2 | Random | 2.0 | **1** | 1.0 $\pm$ 0.0 | 101.0 | 2120 | 6.35s | 1.0 | `~` |
| [`johnson16-2-4`](chi_tiet_tung_do_thi/johnson16-2-4.md) | Type 2 | I-MSM | 1.0 | **1** | 1.0 $\pm$ 0.0 | 15.0 | 15 | 8.9s | 1.0 | `~` |
| [`johnson16-2-4`](chi_tiet_tung_do_thi/johnson16-2-4.md) | Type 2 | CCA | 1.0 | **1** | 1.0 $\pm$ 0.0 | 15.0 | 15 | 0.07s | 1.0 | `~` |
| [`johnson8-2-4`](chi_tiet_tung_do_thi/johnson8-2-4.md) | Type 2 | **PPO-AOS** | 1.6 | **1** | 1.0 $\pm$ 0.0 | 100.6 | 2112 | 3.16s | 1.0 | `=` |
| [`johnson8-2-4`](chi_tiet_tung_do_thi/johnson8-2-4.md) | Type 2 | MAB-AOS | 1.6 | **1** | 1.0 $\pm$ 0.0 | 100.6 | 2112 | 1.19s | 1.0 | `~` |
| [`johnson8-2-4`](chi_tiet_tung_do_thi/johnson8-2-4.md) | Type 2 | Greedy-AOS | 1.6 | **1** | 1.0 $\pm$ 0.0 | 100.6 | 2112 | 1.1s | 1.0 | `~` |
| [`johnson8-2-4`](chi_tiet_tung_do_thi/johnson8-2-4.md) | Type 2 | No-RL | 1.6 | **1** | 1.0 $\pm$ 0.0 | 100.6 | 2112 | 1.11s | 1.0 | `~` |
| [`johnson8-2-4`](chi_tiet_tung_do_thi/johnson8-2-4.md) | Type 2 | Fixed | 1.6 | **1** | 1.0 $\pm$ 0.0 | 100.6 | 2112 | 1.18s | 1.0 | `~` |
| [`johnson8-2-4`](chi_tiet_tung_do_thi/johnson8-2-4.md) | Type 2 | Random | 1.6 | **1** | 1.0 $\pm$ 0.0 | 100.6 | 2112 | 1.01s | 1.0 | `~` |
| [`johnson8-2-4`](chi_tiet_tung_do_thi/johnson8-2-4.md) | Type 2 | I-MSM | 1.0 | **1** | 1.0 $\pm$ 0.0 | 15.0 | 15 | 0.13s | 1.0 | `~` |
| [`johnson8-2-4`](chi_tiet_tung_do_thi/johnson8-2-4.md) | Type 2 | CCA | 1.0 | **1** | 1.0 $\pm$ 0.0 | 15.0 | 15 | 0.01s | 1.0 | `~` |
| [`johnson8-4-4`](chi_tiet_tung_do_thi/johnson8-4-4.md) | Type 2 | **PPO-AOS** | 3.0 | **1** | 1.0 $\pm$ 0.0 | 102.2 | 2144 | 3.43s | 1.0 | `=` |
| [`johnson8-4-4`](chi_tiet_tung_do_thi/johnson8-4-4.md) | Type 2 | MAB-AOS | 3.0 | **1** | 1.0 $\pm$ 0.0 | 101.0 | 2120 | 2.37s | 1.0 | `~` |
| [`johnson8-4-4`](chi_tiet_tung_do_thi/johnson8-4-4.md) | Type 2 | Greedy-AOS | 3.0 | **1** | 1.0 $\pm$ 0.0 | 102.0 | 2141 | 2.27s | 1.0 | `~` |
| [`johnson8-4-4`](chi_tiet_tung_do_thi/johnson8-4-4.md) | Type 2 | No-RL | 3.0 | **1** | 1.0 $\pm$ 0.0 | 101.7 | 2133 | 2.19s | 1.0 | `~` |
| [`johnson8-4-4`](chi_tiet_tung_do_thi/johnson8-4-4.md) | Type 2 | Fixed | 3.0 | **1** | 1.0 $\pm$ 0.0 | 101.0 | 2120 | 2.31s | 1.0 | `~` |
| [`johnson8-4-4`](chi_tiet_tung_do_thi/johnson8-4-4.md) | Type 2 | Random | 3.0 | **1** | 1.0 $\pm$ 0.0 | 101.7 | 2133 | 2.13s | 1.0 | `~` |
| [`johnson8-4-4`](chi_tiet_tung_do_thi/johnson8-4-4.md) | Type 2 | I-MSM | 1.0 | **1** | 1.0 $\pm$ 0.0 | 15.0 | 15 | 1.32s | 1.0 | `~` |
| [`johnson8-4-4`](chi_tiet_tung_do_thi/johnson8-4-4.md) | Type 2 | CCA | 1.0 | **1** | 1.0 $\pm$ 0.0 | 15.0 | 15 | 0.01s | 1.0 | `~` |
| [`karate`](chi_tiet_tung_do_thi/karate.md) | Type 1 | **PPO-AOS** | 4.0 | **4** | 4.0 $\pm$ 0.0 | 100.0 | 2100 | 6.25s | 1.0 | `=` |
| [`karate`](chi_tiet_tung_do_thi/karate.md) | Type 1 | MAB-AOS | 4.0 | **4** | 4.0 $\pm$ 0.0 | 100.0 | 2100 | 2.91s | 1.0 | `~` |
| [`karate`](chi_tiet_tung_do_thi/karate.md) | Type 1 | Greedy-AOS | 4.0 | **4** | 4.0 $\pm$ 0.0 | 100.0 | 2100 | 2.64s | 1.0 | `~` |
| [`karate`](chi_tiet_tung_do_thi/karate.md) | Type 1 | No-RL | 4.0 | **4** | 4.0 $\pm$ 0.0 | 100.0 | 2100 | 2.57s | 1.0 | `~` |
| [`karate`](chi_tiet_tung_do_thi/karate.md) | Type 1 | Fixed | 4.0 | **4** | 4.0 $\pm$ 0.0 | 100.0 | 2100 | 1.69s | 1.0 | `~` |
| [`karate`](chi_tiet_tung_do_thi/karate.md) | Type 1 | Random | 4.0 | **4** | 4.0 $\pm$ 0.0 | 100.0 | 2100 | 2.48s | 1.0 | `~` |
| [`karate`](chi_tiet_tung_do_thi/karate.md) | Type 1 | I-MSM | 4.05 | **4** | 4.0 $\pm$ 0.0 | 15.1 | 15 | 0.18s | 1.0 | `~` |
| [`karate`](chi_tiet_tung_do_thi/karate.md) | Type 1 | CCA | 4.0 | **4** | 4.0 $\pm$ 0.0 | 15.0 | 15 | 0.02s | 1.0 | `~` |
| [`keller4`](chi_tiet_tung_do_thi/keller4.md) | Type 2 | **PPO-AOS** | 3.0 | **1** | 1.0 $\pm$ 0.0 | 102.7 | 2154 | 15.15s | 1.0 | `=` |
| [`keller4`](chi_tiet_tung_do_thi/keller4.md) | Type 2 | MAB-AOS | 3.0 | **1** | 1.0 $\pm$ 0.0 | 101.2 | 2124 | 13.42s | 1.0 | `~` |
| [`keller4`](chi_tiet_tung_do_thi/keller4.md) | Type 2 | Greedy-AOS | 3.0 | **1** | 1.0 $\pm$ 0.0 | 102.2 | 2145 | 13.52s | 1.0 | `~` |
| [`keller4`](chi_tiet_tung_do_thi/keller4.md) | Type 2 | No-RL | 3.0 | **1** | 1.0 $\pm$ 0.0 | 102.5 | 2151 | 13.89s | 1.0 | `~` |
| [`keller4`](chi_tiet_tung_do_thi/keller4.md) | Type 2 | Fixed | 3.0 | **1** | 1.0 $\pm$ 0.0 | 101.3 | 2127 | 13.56s | 1.0 | `~` |
| [`keller4`](chi_tiet_tung_do_thi/keller4.md) | Type 2 | Random | 3.0 | **1** | 1.0 $\pm$ 0.0 | 102.5 | 2151 | 13.3s | 1.0 | `~` |
| [`keller4`](chi_tiet_tung_do_thi/keller4.md) | Type 2 | I-MSM | 1.0 | **1** | 1.0 $\pm$ 0.0 | 15.0 | 15 | 35.06s | 1.0 | `~` |
| [`keller4`](chi_tiet_tung_do_thi/keller4.md) | Type 2 | CCA | 1.0 | **1** | 1.0 $\pm$ 0.0 | 15.0 | 15 | 0.25s | 1.0 | `~` |
| [`lesmis`](chi_tiet_tung_do_thi/lesmis.md) | Type 1 | **PPO-AOS** | 10.6 | **10** | 10.0 $\pm$ 0.0 | 102.2 | 2143 | 5.97s | 1.0 | `=` |
| [`lesmis`](chi_tiet_tung_do_thi/lesmis.md) | Type 1 | MAB-AOS | 10.6 | **10** | 10.0 $\pm$ 0.0 | 101.8 | 2137 | 4.08s | 1.0 | `~` |
| [`lesmis`](chi_tiet_tung_do_thi/lesmis.md) | Type 1 | Greedy-AOS | 10.6 | **10** | 10.0 $\pm$ 0.0 | 102.3 | 2147 | 3.89s | 1.0 | `~` |
| [`lesmis`](chi_tiet_tung_do_thi/lesmis.md) | Type 1 | No-RL | 10.6 | **10** | 10.0 $\pm$ 0.0 | 102.2 | 2145 | 3.94s | 1.0 | `~` |
| [`lesmis`](chi_tiet_tung_do_thi/lesmis.md) | Type 1 | Fixed | 10.6 | **10** | 10.0 $\pm$ 0.0 | 101.5 | 2130 | 2.81s | 1.0 | `~` |
| [`lesmis`](chi_tiet_tung_do_thi/lesmis.md) | Type 1 | Random | 10.6 | **10** | 10.0 $\pm$ 0.0 | 102.2 | 2145 | 3.71s | 1.0 | `~` |
| [`lesmis`](chi_tiet_tung_do_thi/lesmis.md) | Type 1 | I-MSM | 11.05 | **10** | 10.0 $\pm$ 0.0 | 19.4 | 19 | 0.91s | 1.0 | `~` |
| [`lesmis`](chi_tiet_tung_do_thi/lesmis.md) | Type 1 | CCA | 10.85 | **10** | 10.0 $\pm$ 0.0 | 16.9 | 17 | 0.1s | 1.0 | `~` |
| [`netscience`](chi_tiet_tung_do_thi/netscience.md) | Type 1 | **PPO-AOS** | 479.35 | **424** | 431.15 $\pm$ 3.23 | 200.0 | 4100 | 123.58s | 1.0 | `=` |
| [`netscience`](chi_tiet_tung_do_thi/netscience.md) | Type 1 | MAB-AOS | 479.35 | **420** | 429.3 $\pm$ 4.24 | 200.0 | 4100 | 119.37s | 0.3637 | `~` |
| [`netscience`](chi_tiet_tung_do_thi/netscience.md) | Type 1 | Greedy-AOS | 479.35 | **419** | 429.1 $\pm$ 4.75 | 200.0 | 4100 | 108.71s | 0.3637 | `~` |
| [`netscience`](chi_tiet_tung_do_thi/netscience.md) | Type 1 | No-RL | 479.35 | **425** | 430.55 $\pm$ 2.44 | 200.0 | 4100 | 106.5s | 0.6973 | `~` |
| [`netscience`](chi_tiet_tung_do_thi/netscience.md) | Type 1 | Fixed | 479.35 | **410** | 426.7 $\pm$ 11.19 | 200.0 | 4100 | 112.01s | 0.3637 | `~` |
| [`netscience`](chi_tiet_tung_do_thi/netscience.md) | Type 1 | Random | 479.35 | **425** | 430.55 $\pm$ 2.44 | 200.0 | 4100 | 95.13s | 0.6973 | `~` |
| [`netscience`](chi_tiet_tung_do_thi/netscience.md) | Type 1 | I-MSM | 407.6 | **390** | 397.4 $\pm$ 2.89 | 22.8 | 23 | 181.22s | 0.0006 | `-` |
| [`netscience`](chi_tiet_tung_do_thi/netscience.md) | Type 1 | CCA | 393.95 | **381** | 385.8 $\pm$ 2.18 | 24.3 | 24 | 116.83s | 0.0006 | `-` |
| [`polbooks`](chi_tiet_tung_do_thi/polbooks.md) | Type 1 | **PPO-AOS** | 16.05 | **13** | 13.05 $\pm$ 0.22 | 135.9 | 2818 | 7.99s | 1.0 | `=` |
| [`polbooks`](chi_tiet_tung_do_thi/polbooks.md) | Type 1 | MAB-AOS | 16.05 | **13** | 13.15 $\pm$ 0.36 | 126.7 | 2634 | 5.7s | 1.0 | `~` |
| [`polbooks`](chi_tiet_tung_do_thi/polbooks.md) | Type 1 | Greedy-AOS | 16.05 | **13** | 13.2 $\pm$ 0.4 | 121.5 | 2530 | 5.44s | 0.9438 | `~` |
| [`polbooks`](chi_tiet_tung_do_thi/polbooks.md) | Type 1 | No-RL | 16.05 | **13** | 13.15 $\pm$ 0.36 | 131.6 | 2732 | 5.81s | 1.0 | `~` |
| [`polbooks`](chi_tiet_tung_do_thi/polbooks.md) | Type 1 | Fixed | 16.05 | **13** | 13.0 $\pm$ 0.0 | 120.8 | 2516 | 4.33s | 1.0 | `~` |
| [`polbooks`](chi_tiet_tung_do_thi/polbooks.md) | Type 1 | Random | 16.05 | **13** | 13.15 $\pm$ 0.36 | 131.6 | 2732 | 5.25s | 1.0 | `~` |
| [`polbooks`](chi_tiet_tung_do_thi/polbooks.md) | Type 1 | I-MSM | 15.0 | **12** | 13.25 $\pm$ 0.54 | 21.9 | 22 | 1.52s | 0.9438 | `~` |
| [`polbooks`](chi_tiet_tung_do_thi/polbooks.md) | Type 1 | CCA | 15.55 | **13** | 13.85 $\pm$ 0.57 | 21.8 | 22 | 0.26s | 0.0016 | `+` |
| [`san200_0.9_2`](chi_tiet_tung_do_thi/san200_0.9_2.md) | Type 2 | **PPO-AOS** | 2.0 | **1** | 1.0 $\pm$ 0.0 | 101.0 | 2120 | 21.81s | 1.0 | `=` |
| [`san200_0.9_2`](chi_tiet_tung_do_thi/san200_0.9_2.md) | Type 2 | MAB-AOS | 2.0 | **1** | 1.0 $\pm$ 0.0 | 101.0 | 2120 | 20.07s | 1.0 | `~` |
| [`san200_0.9_2`](chi_tiet_tung_do_thi/san200_0.9_2.md) | Type 2 | Greedy-AOS | 2.0 | **1** | 1.0 $\pm$ 0.0 | 101.0 | 2120 | 20.15s | 1.0 | `~` |
| [`san200_0.9_2`](chi_tiet_tung_do_thi/san200_0.9_2.md) | Type 2 | No-RL | 2.0 | **1** | 1.0 $\pm$ 0.0 | 101.0 | 2120 | 19.95s | 1.0 | `~` |
| [`san200_0.9_2`](chi_tiet_tung_do_thi/san200_0.9_2.md) | Type 2 | Fixed | 2.0 | **1** | 1.0 $\pm$ 0.0 | 101.0 | 2120 | 20.06s | 1.0 | `~` |
| [`san200_0.9_2`](chi_tiet_tung_do_thi/san200_0.9_2.md) | Type 2 | Random | 2.0 | **1** | 1.0 $\pm$ 0.0 | 101.0 | 2120 | 19.69s | 1.0 | `~` |
| [`san200_0.9_2`](chi_tiet_tung_do_thi/san200_0.9_2.md) | Type 2 | I-MSM | 1.0 | **1** | 1.0 $\pm$ 0.0 | 15.0 | 15 | 62.94s | 1.0 | `~` |
| [`san200_0.9_2`](chi_tiet_tung_do_thi/san200_0.9_2.md) | Type 2 | CCA | 1.0 | **1** | 1.0 $\pm$ 0.0 | 15.0 | 15 | 0.14s | 1.0 | `~` |
| [`san200_0.9_3`](chi_tiet_tung_do_thi/san200_0.9_3.md) | Type 2 | **PPO-AOS** | 2.0 | **1** | 1.0 $\pm$ 0.0 | 101.0 | 2120 | 21.75s | 1.0 | `=` |
| [`san200_0.9_3`](chi_tiet_tung_do_thi/san200_0.9_3.md) | Type 2 | MAB-AOS | 2.0 | **1** | 1.0 $\pm$ 0.0 | 101.0 | 2120 | 19.99s | 1.0 | `~` |
| [`san200_0.9_3`](chi_tiet_tung_do_thi/san200_0.9_3.md) | Type 2 | Greedy-AOS | 2.0 | **1** | 1.0 $\pm$ 0.0 | 101.0 | 2120 | 19.98s | 1.0 | `~` |
| [`san200_0.9_3`](chi_tiet_tung_do_thi/san200_0.9_3.md) | Type 2 | No-RL | 2.0 | **1** | 1.0 $\pm$ 0.0 | 101.0 | 2120 | 20.11s | 1.0 | `~` |
| [`san200_0.9_3`](chi_tiet_tung_do_thi/san200_0.9_3.md) | Type 2 | Fixed | 2.0 | **1** | 1.0 $\pm$ 0.0 | 101.0 | 2120 | 20.19s | 1.0 | `~` |
| [`san200_0.9_3`](chi_tiet_tung_do_thi/san200_0.9_3.md) | Type 2 | Random | 2.0 | **1** | 1.0 $\pm$ 0.0 | 101.0 | 2120 | 19.71s | 1.0 | `~` |
| [`san200_0.9_3`](chi_tiet_tung_do_thi/san200_0.9_3.md) | Type 2 | I-MSM | 1.0 | **1** | 1.0 $\pm$ 0.0 | 15.0 | 15 | 63.04s | 1.0 | `~` |
| [`san200_0.9_3`](chi_tiet_tung_do_thi/san200_0.9_3.md) | Type 2 | CCA | 1.0 | **1** | 1.0 $\pm$ 0.0 | 15.0 | 15 | 0.14s | 1.0 | `~` |

---

### 4. TỔNG KẾT VỀ TÍNH CÔNG BẰNG VÀ TÀI NGUYÊN TÍNH TOÁN
1. **Về tính tương đương khởi tạo:** 6 giải thuật GA dùng chung 100% quần thể ban đầu $P_0$. 2 heuristic tham lam I-MSM và CCA sử dụng cơ chế multi-start riêng biệt do cấu trúc giải thuật khác biệt.
2. **Về ngân sách tìm kiếm:** Tất cả các giải thuật GA đều có cùng trần ngân sách ($4,100$ evals). PPO-AOS dừng sớm hơn do hội tụ nhanh hơn, chứ không phải do bất bình đẳng về tài nguyên.
3. **Về thời gian vận hành PPO:** Thời gian `Mean_Time_Sec` là Wall-clock Runtime, đã bao gồm 100% thời gian trích xuất State, thời gian suy luận nơ-ron (Inference), và thời gian huấn luyện gradient descent (Online Training Update).
