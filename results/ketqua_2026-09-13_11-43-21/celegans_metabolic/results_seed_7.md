# Báo Cáo Kết Quả Thực Nghiệm: Seed #07 (Seed = `20260421`)

**Tập dữ liệu đồ thị:** `celegans_metabolic` ($|V| = 453$, $|E| = 2025$, Density = $0.0198$, $s = 2$)  
**Hạt giống cố định (Seed Value):** `20260421` (Lần chạy 07/20 từ `seedun.md`)  
**Thời gian thực thi:** `2026-09-13 13:22:06`  
**Môi trường tính toán:** `Hybrid Co-Processing [CPU: 12 Cores song song (GA/C++ igraph) + GPU: NVIDIA GeForce RTX 3050 Laptop GPU (PPO Tensor Cores)]`  

---

## 1. Bảng Thống Kê Hiệu Năng Chi Tiết Các Thuật Toán (Seed #7)

| Chiến lược / Thuật toán | Best Cover (Min) | Best Fitness | Mean $\pm$ Std | Median | Vi phạm ($diam > s$) | Độ đa dạng | Khả thi ($100\%$) | Thời gian (s) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **PPO-AOS** | **29** | **29.00** | 31.85 $\pm$ 5.20 | 29.0 | 0.00 | 0.884 |  Đạt chuẩn | 294.79s |
| MAB-AOS | 30 | 30.00 | 32.48 $\pm$ 4.40 | 30.0 | 0.00 | 0.934 |  Đạt chuẩn | 454.22s |
| Greedy-AOS | 29 | 29.00 | 31.86 $\pm$ 4.93 | 29.0 | 0.00 | 0.858 |  Đạt chuẩn | 279.84s |
| I-MSM | 30 | 30.00 | 30.00 $\pm$ 0.00 | 30.0 | 0.00 | 0.000 |  Đạt chuẩn | 177.57s |
| CCA | 29 | 29.00 | 29.20 $\pm$ 0.40 | 29.0 | 0.00 | 0.000 |  Đạt chuẩn | 27.37s |
| No-RL | 30 | 30.00 | 32.19 $\pm$ 4.39 | 30.0 | 0.00 | 0.905 |  Đạt chuẩn | 230.07s |
| Fixed | 29 | 29.00 | 31.22 $\pm$ 4.53 | 29.0 | 0.00 | 0.976 |  Đạt chuẩn | 198.75s |
| Random | 30 | 30.00 | 32.19 $\pm$ 4.39 | 30.0 | 0.00 | 0.905 |  Đạt chuẩn | 233.82s |

---

## 2. Cấu Trúc Nghiệm Tốt Nhất Trong Lần Chạy (Best Solution Clusters)
- **Thuật toán đạt Best:** `PPO-AOS` (Cover = `29` clubs, Fitness = `29.00`)
- **Kích thước các cụm ($s$-clubs):** `[15, 121, 13, 44, 11, 7, 30, 20, 54, 31, 2, 17, 20, 5, 8, 8, 7, 8, 2, 7, 3, 1, 5, 1, 2, 5, 2, 3, 1]`
- **Số thế hệ tiến hóa:** `179` generations

*(Có tổng cộng 29 cụm $s$-club hợp lệ, chi tiết toàn bộ đỉnh được lưu trong file `results_seed_7.json`)*

---
*File được sinh tự động bởi hệ thống EVO-RL MSCC Research Framework.*
