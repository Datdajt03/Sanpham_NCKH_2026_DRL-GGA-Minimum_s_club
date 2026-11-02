# Báo Cáo Kết Quả Thực Nghiệm: Seed #06 (Seed = `20260317`)

**Tập dữ liệu đồ thị:** `celegans_metabolic` ($|V| = 453$, $|E| = 2025$, Density = $0.0198$, $s = 2$)  
**Hạt giống cố định (Seed Value):** `20260317` (Lần chạy 06/20 từ `seedun.md`)  
**Thời gian thực thi:** `2026-09-13 13:36:25`  
**Môi trường tính toán:** `Hybrid Co-Processing [CPU: 12 Cores song song (GA/C++ igraph) + GPU: NVIDIA GeForce RTX 3050 Laptop GPU (PPO Tensor Cores)]`  

---

## 1. Bảng Thống Kê Hiệu Năng Chi Tiết Các Thuật Toán (Seed #6)

| Chiến lược / Thuật toán | Best Cover (Min) | Best Fitness | Mean $\pm$ Std | Median | Vi phạm ($diam > s$) | Độ đa dạng | Khả thi ($100\%$) | Thời gian (s) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **PPO-AOS** | **29** | **29.00** | 31.47 $\pm$ 3.96 | 30.0 | 0.00 | 0.943 |  Đạt chuẩn | 634.68s |
| MAB-AOS | 29 | 29.00 | 31.38 $\pm$ 4.55 | 29.0 | 0.00 | 0.928 |  Đạt chuẩn | 536.98s |
| Greedy-AOS | 29 | 29.00 | 31.24 $\pm$ 4.33 | 29.0 | 0.00 | 0.928 |  Đạt chuẩn | 623.40s |
| I-MSM | 31 | 31.00 | 31.16 $\pm$ 0.36 | 31.0 | 0.00 | 0.000 |  Đạt chuẩn | 213.45s |
| CCA | 29 | 29.00 | 29.57 $\pm$ 0.82 | 29.0 | 0.00 | 0.000 |  Đạt chuẩn | 30.15s |
| No-RL | 31 | 31.00 | 33.27 $\pm$ 4.18 | 31.0 | 0.00 | 0.921 |  Đạt chuẩn | 237.44s |
| Fixed | 30 | 30.00 | 31.77 $\pm$ 4.03 | 30.0 | 0.00 | 0.960 |  Đạt chuẩn | 240.42s |
| Random | 31 | 31.00 | 33.27 $\pm$ 4.18 | 31.0 | 0.00 | 0.921 |  Đạt chuẩn | 238.95s |

---

## 2. Cấu Trúc Nghiệm Tốt Nhất Trong Lần Chạy (Best Solution Clusters)
- **Thuật toán đạt Best:** `PPO-AOS` (Cover = `29` clubs, Fitness = `29.00`)
- **Kích thước các cụm ($s$-clubs):** `[145, 84, 12, 12, 7, 18, 18, 11, 21, 32, 3, 20, 5, 14, 5, 6, 3, 2, 1, 4, 3, 1, 13, 4, 1, 2, 2, 3, 1]`
- **Số thế hệ tiến hóa:** `201` generations

*(Có tổng cộng 29 cụm $s$-club hợp lệ, chi tiết toàn bộ đỉnh được lưu trong file `results_seed_6.json`)*

---
*File được sinh tự động bởi hệ thống EVO-RL MSCC Research Framework.*
