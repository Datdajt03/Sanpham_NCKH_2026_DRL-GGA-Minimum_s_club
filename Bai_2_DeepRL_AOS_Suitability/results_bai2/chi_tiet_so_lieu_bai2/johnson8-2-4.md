# CHI TIẾT ĐỐI CHUẨN THỰC NGHIỆM BÀI 2 TRÊN ĐỒ THỊ `johnson8-2-4`

* **Tập dữ liệu:** `johnson8-2-4`
* **Giao thức:** Chạy độc lập qua 1 hạt giống (paired seeds).

## 1. BẢNG ĐỐI ĐẦU HIỆU NĂNG CÁC THUẬT TOÁN

| Thuật toán | Nghiệm tốt nhất $|C|_{\min}$ | Nghiệm Trung bình | Độ lệch SD | Khởi tạo $f_0$ | Số thế hệ $\bar{T}$ | Đánh giá $N_{\text{evals}}$ | Thời gian (s) | Khả thi (%) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| CCA | **1** | 1.00 | nan | 1.0 | 0 | 28 | 0.01s | 100.0% |
| Fixed | **1** | 1.00 | nan | 1.0 | 109 | 2280 | 0.92s | 100.0% |
| Greedy-AOS | **1** | 1.00 | nan | 1.0 | 101 | 2120 | 0.90s | 100.0% |
| I-MSM | **1** | 1.00 | nan | 1.0 | 0 | 100 | 0.11s | 100.0% |
| MAB-AOS | **1** | 1.00 | nan | 1.0 | 102 | 2140 | 1.00s | 100.0% |
| No-RL | **1** | 1.00 | nan | 1.0 | 102 | 2140 | 0.88s | 100.0% |
| **PPO-AOS** | **1** | 1.00 | nan | 1.0 | 102 | 2140 | 1.34s | 100.0% |
| Random | **1** | 1.00 | nan | 1.0 | 102 | 2140 | 0.84s | 100.0% |

## 2. ĐỘNG THÁI TOÁN TỬ VÀ PHẦN THƯỞNG TRÊN ĐỒ THỊ NÀY

| Thuật toán | Giai đoạn | Toán tử | Số lần chọn | Reward TB | Độ lệch SD |
| :--- | :---: | :--- | :---: | :---: | :---: |
| Fixed | Early | Op 3 | 66 | 0.0236 | 4.6988 |
| Fixed | Mid | Op 3 | 43 | -1.0000 | 0.0000 |
| Greedy-AOS | Early | Lai ghép cấu trúc (Crossover) | 18 | 1.0578 | 8.2500 |
| Greedy-AOS | Early | Đột biến sửa sai (Repair) | 26 | -1.0000 | 0.0000 |
| Greedy-AOS | Early | Đột biến đa dạng hóa (Diversify) | 22 | -0.9091 | 0.2942 |
| Greedy-AOS | Mid | Lai ghép cấu trúc (Crossover) | 9 | -1.0000 | 0.0000 |
| Greedy-AOS | Mid | Đột biến sửa sai (Repair) | 8 | -1.0000 | 0.0000 |
| Greedy-AOS | Mid | Đột biến đa dạng hóa (Diversify) | 18 | -1.0000 | 0.0000 |
| MAB-AOS | Early | Lai ghép cấu trúc (Crossover) | 66 | -0.1950 | 4.4533 |
| MAB-AOS | Mid | Lai ghép cấu trúc (Crossover) | 36 | -1.0000 | 0.0000 |
| No-RL | Early | Lai ghép cấu trúc (Crossover) | 23 | 0.4203 | 6.8115 |
| No-RL | Early | Đột biến sửa sai (Repair) | 23 | -0.1208 | 3.8020 |
| No-RL | Early | Đột biến đa dạng hóa (Diversify) | 20 | -0.9500 | 0.2236 |
| No-RL | Mid | Lai ghép cấu trúc (Crossover) | 10 | -1.0000 | 0.0000 |
| No-RL | Mid | Đột biến sửa sai (Repair) | 12 | -1.0000 | 0.0000 |
| No-RL | Mid | Đột biến đa dạng hóa (Diversify) | 14 | -1.0000 | 0.0000 |
| **PPO-AOS** | Early | Lai ghép cấu trúc (Crossover) | 18 | 0.8306 | 7.2865 |
| **PPO-AOS** | Early | Đột biến sửa sai (Repair) | 16 | 0.1989 | 4.7955 |
| **PPO-AOS** | Early | Đột biến đa dạng hóa (Diversify) | 32 | -0.9688 | 0.1768 |
| **PPO-AOS** | Mid | Lai ghép cấu trúc (Crossover) | 10 | -1.0000 | 0.0000 |
| **PPO-AOS** | Mid | Đột biến sửa sai (Repair) | 13 | -1.0000 | 0.0000 |
| **PPO-AOS** | Mid | Đột biến đa dạng hóa (Diversify) | 13 | -1.0000 | 0.0000 |
| Random | Early | Lai ghép cấu trúc (Crossover) | 23 | 0.4203 | 6.8115 |
| Random | Early | Đột biến sửa sai (Repair) | 23 | -0.1208 | 3.8020 |
| Random | Early | Đột biến đa dạng hóa (Diversify) | 20 | -0.9500 | 0.2236 |
| Random | Mid | Lai ghép cấu trúc (Crossover) | 10 | -1.0000 | 0.0000 |
| Random | Mid | Đột biến sửa sai (Repair) | 12 | -1.0000 | 0.0000 |
| Random | Mid | Đột biến đa dạng hóa (Diversify) | 14 | -1.0000 | 0.0000 |

---
*Quay lại [Báo cáo Tổng hợp Bài 2](../Tong_hop_so_lieu_Bai_2.md)*
