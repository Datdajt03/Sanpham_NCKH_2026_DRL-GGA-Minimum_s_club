# Báo Cáo Kết Quả Thực Nghiệm: Seed #17 (Seed = `52013140`)

**Tập dữ liệu đồ thị:** `celegans_metabolic` ($|V| = 453$, $|E| = 2025$, Density = $0.0198$, $s = 2$)  
**Hạt giống cố định (Seed Value):** `52013140` (Lần chạy 17/20 từ `seedun.md`)  
**Thời gian thực thi:** `2026-09-13 14:18:53`  
**Môi trường tính toán:** `Hybrid Co-Processing [CPU: 12 Cores song song (GA/C++ igraph) + GPU: NVIDIA GeForce RTX 3050 Laptop GPU (PPO Tensor Cores)]`  

---

## 1. Bảng Thống Kê Hiệu Năng Chi Tiết Các Thuật Toán (Seed #17)

| Chiến lược / Thuật toán | Best Cover (Min) | Best Fitness | Mean $\pm$ Std | Median | Vi phạm ($diam > s$) | Độ đa dạng | Khả thi ($100\%$) | Thời gian (s) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **PPO-AOS** | **29** | **29.00** | 30.27 $\pm$ 3.11 | 29.0 | 0.00 | 0.936 |  Đạt chuẩn | 491.84s |
| MAB-AOS | 29 | 29.00 | 30.49 $\pm$ 3.54 | 29.0 | 0.00 | 0.962 |  Đạt chuẩn | 325.12s |
| Greedy-AOS | 29 | 29.00 | 30.38 $\pm$ 3.21 | 29.0 | 0.00 | 0.965 |  Đạt chuẩn | 785.18s |
| I-MSM | 31 | 31.00 | 32.28 $\pm$ 4.59 | 31.0 | 0.00 | 0.000 |  Đạt chuẩn | 151.90s |
| CCA | 29 | 29.00 | 29.72 $\pm$ 1.37 | 29.0 | 0.00 | 0.000 |  Đạt chuẩn | 23.13s |
| No-RL | 33 | 33.00 | 34.41 $\pm$ 2.45 | 33.0 | 0.00 | 0.925 |  Đạt chuẩn | 112.45s |
| Fixed | 29 | 29.00 | 30.50 $\pm$ 3.40 | 29.0 | 0.00 | 0.963 |  Đạt chuẩn | 575.44s |
| Random | 33 | 33.00 | 34.41 $\pm$ 2.45 | 33.0 | 0.00 | 0.925 |  Đạt chuẩn | 81.74s |

---

## 2. Cấu Trúc Nghiệm Tốt Nhất Trong Lần Chạy (Best Solution Clusters)
- **Thuật toán đạt Best:** `PPO-AOS` (Cover = `29` clubs, Fitness = `29.00`)
- **Kích thước các cụm ($s$-clubs):** `[162, 15, 14, 11, 9, 18, 56, 24, 34, 2, 26, 9, 15, 11, 7, 4, 2, 1, 3, 3, 7, 4, 1, 4, 2, 3, 2, 3, 1]`
- **Số thế hệ tiến hóa:** `132` generations

*(Có tổng cộng 29 cụm $s$-club hợp lệ, chi tiết toàn bộ đỉnh được lưu trong file `results_seed_17.json`)*

---
*File được sinh tự động bởi hệ thống EVO-RL MSCC Research Framework.*
