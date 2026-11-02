# Báo Cáo Kết Quả Thực Nghiệm: Seed #15 (Seed = `31415926`)

**Tập dữ liệu đồ thị:** `celegans_metabolic` ($|V| = 453$, $|E| = 2025$, Density = $0.0198$, $s = 2$)  
**Hạt giống cố định (Seed Value):** `31415926` (Lần chạy 15/20 từ `seedun.md`)  
**Thời gian thực thi:** `2026-09-13 14:16:34`  
**Môi trường tính toán:** `Hybrid Co-Processing [CPU: 12 Cores song song (GA/C++ igraph) + GPU: NVIDIA GeForce RTX 3050 Laptop GPU (PPO Tensor Cores)]`  

---

## 1. Bảng Thống Kê Hiệu Năng Chi Tiết Các Thuật Toán (Seed #15)

| Chiến lược / Thuật toán | Best Cover (Min) | Best Fitness | Mean $\pm$ Std | Median | Vi phạm ($diam > s$) | Độ đa dạng | Khả thi ($100\%$) | Thời gian (s) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **PPO-AOS** | **29** | **29.00** | 31.22 $\pm$ 4.56 | 29.0 | 0.00 | 0.957 |  Đạt chuẩn | 564.10s |
| MAB-AOS | 29 | 29.00 | 31.45 $\pm$ 5.34 | 29.0 | 0.00 | 0.960 |  Đạt chuẩn | 377.71s |
| Greedy-AOS | 30 | 30.00 | 31.97 $\pm$ 4.45 | 30.0 | 0.00 | 0.965 |  Đạt chuẩn | 588.91s |
| I-MSM | 29 | 29.00 | 29.50 $\pm$ 1.04 | 29.0 | 0.00 | 0.000 |  Đạt chuẩn | 202.41s |
| CCA | 29 | 29.00 | 29.12 $\pm$ 0.47 | 29.0 | 0.00 | 0.000 |  Đạt chuẩn | 13.84s |
| No-RL | 30 | 30.00 | 32.63 $\pm$ 4.27 | 30.0 | 0.00 | 0.903 |  Đạt chuẩn | 177.01s |
| Fixed | 29 | 29.00 | 30.95 $\pm$ 4.74 | 29.0 | 0.00 | 0.960 |  Đạt chuẩn | 367.28s |
| Random | 30 | 30.00 | 32.63 $\pm$ 4.27 | 30.0 | 0.00 | 0.903 |  Đạt chuẩn | 148.29s |

---

## 2. Cấu Trúc Nghiệm Tốt Nhất Trong Lần Chạy (Best Solution Clusters)
- **Thuật toán đạt Best:** `PPO-AOS` (Cover = `29` clubs, Fitness = `29.00`)
- **Kích thước các cụm ($s$-clubs):** `[156, 70, 11, 18, 12, 8, 25, 21, 35, 1, 9, 21, 5, 13, 5, 10, 2, 1, 1, 5, 4, 1, 2, 3, 3, 5, 2, 3, 1]`
- **Số thế hệ tiến hóa:** `151` generations

*(Có tổng cộng 29 cụm $s$-club hợp lệ, chi tiết toàn bộ đỉnh được lưu trong file `results_seed_15.json`)*

---
*File được sinh tự động bởi hệ thống EVO-RL MSCC Research Framework.*
