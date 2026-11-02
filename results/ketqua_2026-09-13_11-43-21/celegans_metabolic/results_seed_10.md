# Báo Cáo Kết Quả Thực Nghiệm: Seed #10 (Seed = `20260913`)

**Tập dữ liệu đồ thị:** `celegans_metabolic` ($|V| = 453$, $|E| = 2025$, Density = $0.0198$, $s = 2$)  
**Hạt giống cố định (Seed Value):** `20260913` (Lần chạy 10/20 từ `seedun.md`)  
**Thời gian thực thi:** `2026-09-13 13:25:59`  
**Môi trường tính toán:** `Hybrid Co-Processing [CPU: 12 Cores song song (GA/C++ igraph) + GPU: NVIDIA GeForce RTX 3050 Laptop GPU (PPO Tensor Cores)]`  

---

## 1. Bảng Thống Kê Hiệu Năng Chi Tiết Các Thuật Toán (Seed #10)

| Chiến lược / Thuật toán | Best Cover (Min) | Best Fitness | Mean $\pm$ Std | Median | Vi phạm ($diam > s$) | Độ đa dạng | Khả thi ($100\%$) | Thời gian (s) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **PPO-AOS** | **29** | **29.00** | 31.19 $\pm$ 3.87 | 30.0 | 0.00 | 0.885 |  Đạt chuẩn | 529.89s |
| MAB-AOS | 29 | 29.00 | 31.57 $\pm$ 4.49 | 29.0 | 0.00 | 0.983 |  Đạt chuẩn | 350.84s |
| Greedy-AOS | 29 | 29.00 | 31.02 $\pm$ 4.23 | 29.0 | 0.00 | 0.893 |  Đạt chuẩn | 338.65s |
| I-MSM | 31 | 31.00 | 31.43 $\pm$ 0.79 | 31.0 | 0.00 | 0.000 |  Đạt chuẩn | 225.95s |
| CCA | 29 | 29.00 | 29.18 $\pm$ 0.71 | 29.0 | 0.00 | 0.000 |  Đạt chuẩn | 22.05s |
| No-RL | 29 | 29.00 | 31.48 $\pm$ 3.99 | 30.0 | 0.00 | 0.977 |  Đạt chuẩn | 205.34s |
| Fixed | 29 | 29.00 | 30.66 $\pm$ 3.59 | 29.0 | 0.00 | 0.940 |  Đạt chuẩn | 251.37s |
| Random | 29 | 29.00 | 31.48 $\pm$ 3.99 | 30.0 | 0.00 | 0.977 |  Đạt chuẩn | 205.47s |

---

## 2. Cấu Trúc Nghiệm Tốt Nhất Trong Lần Chạy (Best Solution Clusters)
- **Thuật toán đạt Best:** `PPO-AOS` (Cover = `29` clubs, Fitness = `29.00`)
- **Kích thước các cụm ($s$-clubs):** `[138, 78, 13, 11, 9, 29, 18, 15, 23, 30, 2, 10, 20, 5, 14, 5, 7, 1, 2, 1, 4, 3, 1, 2, 5, 2, 3, 1, 1]`
- **Số thế hệ tiến hóa:** `201` generations

*(Có tổng cộng 29 cụm $s$-club hợp lệ, chi tiết toàn bộ đỉnh được lưu trong file `results_seed_10.json`)*

---
*File được sinh tự động bởi hệ thống EVO-RL MSCC Research Framework.*
