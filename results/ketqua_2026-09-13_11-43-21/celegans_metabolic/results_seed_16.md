# Báo Cáo Kết Quả Thực Nghiệm: Seed #16 (Seed = `27182818`)

**Tập dữ liệu đồ thị:** `celegans_metabolic` ($|V| = 453$, $|E| = 2025$, Density = $0.0198$, $s = 2$)  
**Hạt giống cố định (Seed Value):** `27182818` (Lần chạy 16/20 từ `seedun.md`)  
**Thời gian thực thi:** `2026-09-13 14:18:21`  
**Môi trường tính toán:** `Hybrid Co-Processing [CPU: 12 Cores song song (GA/C++ igraph) + GPU: NVIDIA GeForce RTX 3050 Laptop GPU (PPO Tensor Cores)]`  

---

## 1. Bảng Thống Kê Hiệu Năng Chi Tiết Các Thuật Toán (Seed #16)

| Chiến lược / Thuật toán | Best Cover (Min) | Best Fitness | Mean $\pm$ Std | Median | Vi phạm ($diam > s$) | Độ đa dạng | Khả thi ($100\%$) | Thời gian (s) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **PPO-AOS** | **29** | **29.00** | 31.91 $\pm$ 4.95 | 30.0 | 0.00 | 0.947 |  Đạt chuẩn | 797.71s |
| MAB-AOS | 31 | 31.00 | 33.39 $\pm$ 4.03 | 32.0 | 0.00 | 0.874 |  Đạt chuẩn | 379.38s |
| Greedy-AOS | 29 | 29.00 | 30.95 $\pm$ 4.36 | 29.0 | 0.00 | 0.882 |  Đạt chuẩn | 374.87s |
| I-MSM | 30 | 30.00 | 30.80 $\pm$ 0.91 | 30.0 | 0.00 | 0.000 |  Đạt chuẩn | 255.70s |
| CCA | 29 | 29.00 | 29.36 $\pm$ 0.48 | 29.0 | 0.00 | 0.000 |  Đạt chuẩn | 23.66s |
| No-RL | 30 | 30.00 | 33.09 $\pm$ 4.79 | 30.0 | 0.00 | 0.938 |  Đạt chuẩn | 289.19s |
| Fixed | 30 | 30.00 | 32.27 $\pm$ 4.76 | 30.0 | 0.00 | 0.938 |  Đạt chuẩn | 145.55s |
| Random | 30 | 30.00 | 33.09 $\pm$ 4.79 | 30.0 | 0.00 | 0.938 |  Đạt chuẩn | 250.21s |

---

## 2. Cấu Trúc Nghiệm Tốt Nhất Trong Lần Chạy (Best Solution Clusters)
- **Thuật toán đạt Best:** `PPO-AOS` (Cover = `29` clubs, Fitness = `29.00`)
- **Kích thước các cụm ($s$-clubs):** `[150, 17, 12, 6, 23, 14, 51, 21, 41, 3, 15, 23, 5, 8, 4, 6, 5, 12, 9, 2, 2, 5, 6, 1, 2, 2, 3, 2, 3]`
- **Số thế hệ tiến hóa:** `201` generations

*(Có tổng cộng 29 cụm $s$-club hợp lệ, chi tiết toàn bộ đỉnh được lưu trong file `results_seed_16.json`)*

---
*File được sinh tự động bởi hệ thống EVO-RL MSCC Research Framework.*
