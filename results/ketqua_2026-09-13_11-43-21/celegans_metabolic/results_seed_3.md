# Báo Cáo Kết Quả Thực Nghiệm: Seed #03 (Seed = `23052026`)

**Tập dữ liệu đồ thị:** `celegans_metabolic` ($|V| = 453$, $|E| = 2025$, Density = $0.0198$, $s = 2$)  
**Hạt giống cố định (Seed Value):** `23052026` (Lần chạy 03/20 từ `seedun.md`)  
**Thời gian thực thi:** `2026-09-13 13:23:42`  
**Môi trường tính toán:** `Hybrid Co-Processing [CPU: 12 Cores song song (GA/C++ igraph) + GPU: NVIDIA GeForce RTX 3050 Laptop GPU (PPO Tensor Cores)]`  

---

## 1. Bảng Thống Kê Hiệu Năng Chi Tiết Các Thuật Toán (Seed #3)

| Chiến lược / Thuật toán | Best Cover (Min) | Best Fitness | Mean $\pm$ Std | Median | Vi phạm ($diam > s$) | Độ đa dạng | Khả thi ($100\%$) | Thời gian (s) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **PPO-AOS** | **29** | **29.00** | 31.28 $\pm$ 4.90 | 29.0 | 0.00 | 0.928 |  Đạt chuẩn | 238.74s |
| MAB-AOS | 29 | 29.00 | 31.32 $\pm$ 4.81 | 29.0 | 0.00 | 0.943 |  Đạt chuẩn | 306.92s |
| Greedy-AOS | 29 | 29.00 | 31.08 $\pm$ 4.46 | 29.0 | 0.00 | 0.958 |  Đạt chuẩn | 370.91s |
| I-MSM | 29 | 29.00 | 30.17 $\pm$ 3.62 | 29.0 | 0.00 | 0.000 |  Đạt chuẩn | 197.57s |
| CCA | 30 | 30.00 | 30.00 $\pm$ 0.00 | 30.0 | 0.00 | 0.000 |  Đạt chuẩn | 20.68s |
| No-RL | 29 | 29.00 | 31.99 $\pm$ 5.30 | 29.0 | 0.00 | 0.959 |  Đạt chuẩn | 238.22s |
| Fixed | 29 | 29.00 | 30.83 $\pm$ 4.38 | 29.0 | 0.00 | 0.965 |  Đạt chuẩn | 378.72s |
| Random | 29 | 29.00 | 31.99 $\pm$ 5.30 | 29.0 | 0.00 | 0.959 |  Đạt chuẩn | 240.99s |

---

## 2. Cấu Trúc Nghiệm Tốt Nhất Trong Lần Chạy (Best Solution Clusters)
- **Thuật toán đạt Best:** `PPO-AOS` (Cover = `29` clubs, Fitness = `29.00`)
- **Kích thước các cụm ($s$-clubs):** `[15, 33, 81, 102, 13, 11, 8, 19, 30, 18, 35, 3, 16, 5, 3, 8, 7, 15, 3, 3, 4, 1, 5, 1, 3, 5, 2, 3, 1]`
- **Số thế hệ tiến hóa:** `144` generations

*(Có tổng cộng 29 cụm $s$-club hợp lệ, chi tiết toàn bộ đỉnh được lưu trong file `results_seed_3.json`)*

---
*File được sinh tự động bởi hệ thống EVO-RL MSCC Research Framework.*
