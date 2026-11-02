# CHI TIẾT ĐỐI CHUẨN THỰC NGHIỆM BÀI 2 TRÊN ĐỒ THỊ `karate`

* **Tập dữ liệu:** `karate`
* **Giao thức:** Chạy độc lập qua 1 hạt giống (paired seeds).

## 1. BẢNG ĐỐI ĐẦU HIỆU NĂNG CÁC THUẬT TOÁN

| Thuật toán | Nghiệm tốt nhất $|C|_{\min}$ | Nghiệm Trung bình | Độ lệch SD | Khởi tạo $f_0$ | Số thế hệ $\bar{T}$ | Đánh giá $N_{\text{evals}}$ | Thời gian (s) | Khả thi (%) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| CCA | **4** | 4.00 | nan | 4.0 | 0 | 34 | 0.01s | 100.0% |
| Fixed | **4** | 4.00 | nan | 4.0 | 112 | 2340 | 1.92s | 100.0% |
| Greedy-AOS | **4** | 4.00 | nan | 4.0 | 101 | 2120 | 1.72s | 100.0% |
| I-MSM | **4** | 4.00 | nan | 4.0 | 0 | 100 | 0.17s | 100.0% |
| MAB-AOS | **4** | 4.00 | nan | 4.0 | 101 | 2120 | 1.10s | 100.0% |
| No-RL | **4** | 4.00 | nan | 4.0 | 101 | 2120 | 2.14s | 100.0% |
| **PPO-AOS** | **4** | 4.00 | nan | 4.0 | 102 | 2140 | 4.67s | 100.0% |
| Random | **4** | 4.00 | nan | 4.0 | 101 | 2120 | 2.01s | 100.0% |

## 2. ĐỘNG THÁI TOÁN TỬ VÀ PHẦN THƯỞNG TRÊN ĐỒ THỊ NÀY

| Thuật toán | Giai đoạn | Toán tử | Số lần chọn | Reward TB | Độ lệch SD |
| :--- | :---: | :--- | :---: | :---: | :---: |
| Fixed | Early | Op 3 | 66 | -0.4254 | 3.0102 |
| Fixed | Mid | Op 3 | 46 | -1.0000 | 0.0000 |
| Greedy-AOS | Early | Lai ghép cấu trúc (Crossover) | 23 | -0.0896 | 4.3659 |
| Greedy-AOS | Early | Đột biến sửa sai (Repair) | 11 | -1.0000 | 0.0000 |
| Greedy-AOS | Early | Đột biến đa dạng hóa (Diversify) | 32 | -0.8750 | 0.3360 |
| Greedy-AOS | Mid | Lai ghép cấu trúc (Crossover) | 13 | -1.0000 | 0.0000 |
| Greedy-AOS | Mid | Đột biến sửa sai (Repair) | 14 | -1.0000 | 0.0000 |
| Greedy-AOS | Mid | Đột biến đa dạng hóa (Diversify) | 8 | -1.0000 | 0.0000 |
| MAB-AOS | Early | Lai ghép cấu trúc (Crossover) | 66 | -0.6222 | 2.5809 |
| MAB-AOS | Mid | Lai ghép cấu trúc (Crossover) | 35 | -1.0000 | 0.0000 |
| No-RL | Early | Lai ghép cấu trúc (Crossover) | 28 | -0.1808 | 3.9516 |
| No-RL | Early | Đột biến sửa sai (Repair) | 25 | -0.9200 | 0.2769 |
| No-RL | Early | Đột biến đa dạng hóa (Diversify) | 13 | -1.0000 | 0.0000 |
| No-RL | Mid | Lai ghép cấu trúc (Crossover) | 15 | -1.0000 | 0.0000 |
| No-RL | Mid | Đột biến sửa sai (Repair) | 8 | -1.0000 | 0.0000 |
| No-RL | Mid | Đột biến đa dạng hóa (Diversify) | 12 | -1.0000 | 0.0000 |
| **PPO-AOS** | Early | Lai ghép cấu trúc (Crossover) | 18 | -0.1667 | 3.0534 |
| **PPO-AOS** | Early | Đột biến sửa sai (Repair) | 16 | 0.3077 | 5.2307 |
| **PPO-AOS** | Early | Đột biến đa dạng hóa (Diversify) | 32 | -0.9688 | 0.1768 |
| **PPO-AOS** | Mid | Lai ghép cấu trúc (Crossover) | 10 | -1.0000 | 0.0000 |
| **PPO-AOS** | Mid | Đột biến sửa sai (Repair) | 13 | -1.0000 | 0.0000 |
| **PPO-AOS** | Mid | Đột biến đa dạng hóa (Diversify) | 13 | -1.0000 | 0.0000 |
| Random | Early | Lai ghép cấu trúc (Crossover) | 28 | -0.1808 | 3.9516 |
| Random | Early | Đột biến sửa sai (Repair) | 25 | -0.9200 | 0.2769 |
| Random | Early | Đột biến đa dạng hóa (Diversify) | 13 | -1.0000 | 0.0000 |
| Random | Mid | Lai ghép cấu trúc (Crossover) | 15 | -1.0000 | 0.0000 |
| Random | Mid | Đột biến sửa sai (Repair) | 8 | -1.0000 | 0.0000 |
| Random | Mid | Đột biến đa dạng hóa (Diversify) | 12 | -1.0000 | 0.0000 |

---
*Quay lại [Báo cáo Tổng hợp Bài 2](../Tong_hop_so_lieu_Bai_2.md)*
