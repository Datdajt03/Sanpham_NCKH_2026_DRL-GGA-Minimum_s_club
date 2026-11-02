# CHI TIẾT ĐỐI CHUẨN THỰC NGHIỆM BÀI 2 TRÊN ĐỒ THỊ `football`

* **Tập dữ liệu:** `football`
* **Giao thức:** Chạy độc lập qua 1 hạt giống (paired seeds).

## 1. BẢNG ĐỐI ĐẦU HIỆU NĂNG CÁC THUẬT TOÁN

| Thuật toán | Nghiệm tốt nhất $|C|_{\min}$ | Nghiệm Trung bình | Độ lệch SD | Khởi tạo $f_0$ | Số thế hệ $\bar{T}$ | Đánh giá $N_{\text{evals}}$ | Thời gian (s) | Khả thi (%) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| CCA | **14** | 14.00 | nan | 14.0 | 0 | 115 | 0.24s | 100.0% |
| Fixed | **12** | 12.00 | nan | 12.0 | 200 | 4100 | 5.18s | 100.0% |
| Greedy-AOS | **10** | 10.00 | nan | 10.0 | 128 | 2660 | 3.92s | 100.0% |
| I-MSM | **13** | 13.00 | nan | 13.0 | 0 | 100 | 0.80s | 100.0% |
| MAB-AOS | **11** | 11.00 | nan | 11.0 | 111 | 2320 | 2.33s | 100.0% |
| No-RL | **10** | 10.00 | nan | 10.0 | 123 | 2560 | 4.04s | 100.0% |
| **PPO-AOS** | **10** | 10.00 | nan | 10.0 | 128 | 2660 | 6.29s | 100.0% |
| Random | **10** | 10.00 | nan | 10.0 | 123 | 2560 | 4.16s | 100.0% |

## 2. ĐỘNG THÁI TOÁN TỬ VÀ PHẦN THƯỞNG TRÊN ĐỒ THỊ NÀY

| Thuật toán | Giai đoạn | Toán tử | Số lần chọn | Reward TB | Độ lệch SD |
| :--- | :---: | :--- | :---: | :---: | :---: |
| Fixed | Early | Op 3 | 66 | -0.2672 | 3.2398 |
| Fixed | Late | Op 3 | 68 | -1.0000 | 0.0000 |
| Fixed | Mid | Op 3 | 66 | -0.8217 | 1.4487 |
| Greedy-AOS | Early | Lai ghép cấu trúc (Crossover) | 24 | 0.4220 | 4.9545 |
| Greedy-AOS | Early | Đột biến sửa sai (Repair) | 28 | -0.1223 | 3.0874 |
| Greedy-AOS | Early | Đột biến đa dạng hóa (Diversify) | 14 | -0.8571 | 0.3631 |
| Greedy-AOS | Mid | Lai ghép cấu trúc (Crossover) | 17 | -1.0000 | 0.0000 |
| Greedy-AOS | Mid | Đột biến sửa sai (Repair) | 26 | -1.0000 | 0.0000 |
| Greedy-AOS | Mid | Đột biến đa dạng hóa (Diversify) | 19 | -1.0000 | 0.0000 |
| MAB-AOS | Early | Lai ghép cấu trúc (Crossover) | 66 | -0.1073 | 3.5527 |
| MAB-AOS | Mid | Lai ghép cấu trúc (Crossover) | 45 | -1.0000 | 0.0000 |
| No-RL | Early | Lai ghép cấu trúc (Crossover) | 24 | 1.8379 | 5.9061 |
| No-RL | Early | Đột biến sửa sai (Repair) | 20 | -0.3615 | 2.6294 |
| No-RL | Early | Đột biến đa dạng hóa (Diversify) | 22 | -0.8636 | 0.3513 |
| No-RL | Mid | Lai ghép cấu trúc (Crossover) | 16 | -1.0000 | 0.0000 |
| No-RL | Mid | Đột biến sửa sai (Repair) | 17 | -1.0000 | 0.0000 |
| No-RL | Mid | Đột biến đa dạng hóa (Diversify) | 24 | -1.0000 | 0.0000 |
| **PPO-AOS** | Early | Lai ghép cấu trúc (Crossover) | 18 | 1.0161 | 4.4918 |
| **PPO-AOS** | Early | Đột biến sửa sai (Repair) | 16 | 1.7867 | 6.2964 |
| **PPO-AOS** | Early | Đột biến đa dạng hóa (Diversify) | 32 | -0.9688 | 0.1768 |
| **PPO-AOS** | Mid | Lai ghép cấu trúc (Crossover) | 18 | -1.0000 | 0.0000 |
| **PPO-AOS** | Mid | Đột biến sửa sai (Repair) | 23 | -1.0000 | 0.0000 |
| **PPO-AOS** | Mid | Đột biến đa dạng hóa (Diversify) | 21 | -1.0000 | 0.0000 |
| Random | Early | Lai ghép cấu trúc (Crossover) | 24 | 1.8379 | 5.9061 |
| Random | Early | Đột biến sửa sai (Repair) | 20 | -0.3615 | 2.6294 |
| Random | Early | Đột biến đa dạng hóa (Diversify) | 22 | -0.8636 | 0.3513 |
| Random | Mid | Lai ghép cấu trúc (Crossover) | 16 | -1.0000 | 0.0000 |
| Random | Mid | Đột biến sửa sai (Repair) | 17 | -1.0000 | 0.0000 |
| Random | Mid | Đột biến đa dạng hóa (Diversify) | 24 | -1.0000 | 0.0000 |

---
*Quay lại [Báo cáo Tổng hợp Bài 2](../Tong_hop_so_lieu_Bai_2.md)*
