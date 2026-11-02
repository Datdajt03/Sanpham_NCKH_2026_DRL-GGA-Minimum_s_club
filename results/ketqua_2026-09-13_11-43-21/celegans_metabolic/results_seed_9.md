# Báo Cáo Kết Quả Thực Nghiệm: Seed #09 (Seed = `20260626`)

**Tập dữ liệu đồ thị:** `celegans_metabolic` ($|V| = 453$, $|E| = 2025$, Density = $0.0198$, $s = 2$)  
**Hạt giống cố định (Seed Value):** `20260626` (Lần chạy 09/20 từ `seedun.md`)  
**Thời gian thực thi:** `2026-09-13 13:37:32`  
**Môi trường tính toán:** `Hybrid Co-Processing [CPU: 12 Cores song song (GA/C++ igraph) + GPU: NVIDIA GeForce RTX 3050 Laptop GPU (PPO Tensor Cores)]`  

---

## 1. Bảng Thống Kê Hiệu Năng Chi Tiết Các Thuật Toán (Seed #9)

| Chiến lược / Thuật toán | Best Cover (Min) | Best Fitness | Mean $\pm$ Std | Median | Vi phạm ($diam > s$) | Độ đa dạng | Khả thi ($100\%$) | Thời gian (s) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **PPO-AOS** | **31** | **31.00** | 33.35 $\pm$ 4.02 | 31.0 | 0.00 | 0.897 |  Đạt chuẩn | 220.55s |
| MAB-AOS | 29 | 29.00 | 31.48 $\pm$ 4.31 | 30.0 | 0.00 | 0.924 |  Đạt chuẩn | 561.01s |
| Greedy-AOS | 29 | 29.00 | 31.25 $\pm$ 4.60 | 29.0 | 0.00 | 0.822 |  Đạt chuẩn | 708.30s |
| I-MSM | 30 | 30.00 | 30.65 $\pm$ 2.59 | 30.0 | 0.00 | 0.000 |  Đạt chuẩn | 181.32s |
| CCA | 30 | 30.00 | 30.20 $\pm$ 0.40 | 30.0 | 0.00 | 0.000 |  Đạt chuẩn | 25.79s |
| No-RL | 29 | 29.00 | 32.11 $\pm$ 5.81 | 29.0 | 0.00 | 0.951 |  Đạt chuẩn | 233.51s |
| Fixed | 30 | 30.00 | 31.86 $\pm$ 4.03 | 30.0 | 0.00 | 0.939 |  Đạt chuẩn | 655.66s |
| Random | 29 | 29.00 | 32.11 $\pm$ 5.81 | 29.0 | 0.00 | 0.951 |  Đạt chuẩn | 236.37s |

---

## 2. Cấu Trúc Nghiệm Tốt Nhất Trong Lần Chạy (Best Solution Clusters)
- **Thuật toán đạt Best:** `MAB-AOS` (Cover = `29` clubs, Fitness = `29.00`)
- **Kích thước các cụm ($s$-clubs):** `[22, 139, 16, 12, 7, 11, 68, 13, 17, 40, 3, 23, 5, 11, 3, 6, 16, 10, 2, 9, 3, 2, 4, 1, 2, 2, 2, 3, 1]`
- **Số thế hệ tiến hóa:** `201` generations

*(Có tổng cộng 29 cụm $s$-club hợp lệ, chi tiết toàn bộ đỉnh được lưu trong file `results_seed_9.json`)*

---
*File được sinh tự động bởi hệ thống EVO-RL MSCC Research Framework.*
