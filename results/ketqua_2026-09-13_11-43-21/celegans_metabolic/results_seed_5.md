# Báo Cáo Kết Quả Thực Nghiệm: Seed #05 (Seed = `13092026`)

**Tập dữ liệu đồ thị:** `celegans_metabolic` ($|V| = 453$, $|E| = 2025$, Density = $0.0198$, $s = 2$)  
**Hạt giống cố định (Seed Value):** `13092026` (Lần chạy 05/20 từ `seedun.md`)  
**Thời gian thực thi:** `2026-09-13 13:38:46`  
**Môi trường tính toán:** `Hybrid Co-Processing [CPU: 12 Cores song song (GA/C++ igraph) + GPU: NVIDIA GeForce RTX 3050 Laptop GPU (PPO Tensor Cores)]`  

---

## 1. Bảng Thống Kê Hiệu Năng Chi Tiết Các Thuật Toán (Seed #5)

| Chiến lược / Thuật toán | Best Cover (Min) | Best Fitness | Mean $\pm$ Std | Median | Vi phạm ($diam > s$) | Độ đa dạng | Khả thi ($100\%$) | Thời gian (s) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **PPO-AOS** | **29** | **29.00** | 31.45 $\pm$ 4.57 | 29.0 | 0.00 | 0.900 |  Đạt chuẩn | 235.54s |
| MAB-AOS | 29 | 29.00 | 31.30 $\pm$ 4.76 | 29.0 | 0.00 | 0.953 |  Đạt chuẩn | 275.82s |
| Greedy-AOS | 29 | 29.00 | 31.70 $\pm$ 5.06 | 29.0 | 0.00 | 0.970 |  Đạt chuẩn | 543.45s |
| I-MSM | 30 | 30.00 | 31.29 $\pm$ 1.56 | 31.0 | 0.00 | 0.000 |  Đạt chuẩn | 378.69s |
| CCA | 29 | 29.00 | 30.06 $\pm$ 1.74 | 30.0 | 0.00 | 0.000 |  Đạt chuẩn | 40.23s |
| No-RL | 29 | 29.00 | 32.07 $\pm$ 5.17 | 29.0 | 0.00 | 0.915 |  Đạt chuẩn | 351.59s |
| Fixed | 29 | 29.00 | 31.06 $\pm$ 4.05 | 29.0 | 0.00 | 0.903 |  Đạt chuẩn | 711.44s |
| Random | 29 | 29.00 | 32.07 $\pm$ 5.17 | 29.0 | 0.00 | 0.915 |  Đạt chuẩn | 359.47s |

---

## 2. Cấu Trúc Nghiệm Tốt Nhất Trong Lần Chạy (Best Solution Clusters)
- **Thuật toán đạt Best:** `PPO-AOS` (Cover = `29` clubs, Fitness = `29.00`)
- **Kích thước các cụm ($s$-clubs):** `[30, 125, 17, 12, 8, 31, 16, 69, 16, 1, 33, 16, 5, 9, 7, 5, 6, 12, 10, 3, 3, 1, 2, 4, 5, 2, 3, 1, 1]`
- **Số thế hệ tiến hóa:** `150` generations

*(Có tổng cộng 29 cụm $s$-club hợp lệ, chi tiết toàn bộ đỉnh được lưu trong file `results_seed_5.json`)*

---
*File được sinh tự động bởi hệ thống EVO-RL MSCC Research Framework.*
