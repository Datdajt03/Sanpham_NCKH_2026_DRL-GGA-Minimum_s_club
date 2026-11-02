# Báo Cáo Kết Quả Thực Nghiệm: Seed #04 (Seed = `26062026`)

**Tập dữ liệu đồ thị:** `celegans_metabolic` ($|V| = 453$, $|E| = 2025$, Density = $0.0198$, $s = 2$)  
**Hạt giống cố định (Seed Value):** `26062026` (Lần chạy 04/20 từ `seedun.md`)  
**Thời gian thực thi:** `2026-09-13 13:43:08`  
**Môi trường tính toán:** `Hybrid Co-Processing [CPU: 12 Cores song song (GA/C++ igraph) + GPU: NVIDIA GeForce RTX 3050 Laptop GPU (PPO Tensor Cores)]`  

---

## 1. Bảng Thống Kê Hiệu Năng Chi Tiết Các Thuật Toán (Seed #4)

| Chiến lược / Thuật toán | Best Cover (Min) | Best Fitness | Mean $\pm$ Std | Median | Vi phạm ($diam > s$) | Độ đa dạng | Khả thi ($100\%$) | Thời gian (s) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **PPO-AOS** | **29** | **29.00** | 32.46 $\pm$ 4.93 | 31.0 | 0.00 | 0.891 |  Đạt chuẩn | 564.66s |
| MAB-AOS | 30 | 30.00 | 32.04 $\pm$ 4.16 | 30.0 | 0.00 | 0.940 |  Đạt chuẩn | 407.58s |
| Greedy-AOS | 30 | 30.00 | 32.12 $\pm$ 5.06 | 30.0 | 0.00 | 0.862 |  Đạt chuẩn | 583.15s |
| I-MSM | 29 | 29.00 | 30.59 $\pm$ 1.67 | 30.5 | 0.00 | 0.000 |  Đạt chuẩn | 352.70s |
| CCA | 29 | 29.00 | 30.32 $\pm$ 3.39 | 29.0 | 0.00 | 0.000 |  Đạt chuẩn | 31.78s |
| No-RL | 30 | 30.00 | 32.06 $\pm$ 3.99 | 30.0 | 0.00 | 0.882 |  Đạt chuẩn | 373.79s |
| Fixed | 31 | 31.00 | 32.89 $\pm$ 4.25 | 31.0 | 0.00 | 0.908 |  Đạt chuẩn | 470.46s |
| Random | 30 | 30.00 | 32.06 $\pm$ 3.99 | 30.0 | 0.00 | 0.882 |  Đạt chuẩn | 374.29s |

---

## 2. Cấu Trúc Nghiệm Tốt Nhất Trong Lần Chạy (Best Solution Clusters)
- **Thuật toán đạt Best:** `PPO-AOS` (Cover = `29` clubs, Fitness = `29.00`)
- **Kích thước các cụm ($s$-clubs):** `[138, 16, 77, 11, 8, 14, 19, 15, 16, 37, 2, 10, 22, 5, 8, 7, 9, 9, 7, 2, 1, 6, 3, 1, 2, 2, 2, 3, 1]`
- **Số thế hệ tiến hóa:** `201` generations

*(Có tổng cộng 29 cụm $s$-club hợp lệ, chi tiết toàn bộ đỉnh được lưu trong file `results_seed_4.json`)*

---
*File được sinh tự động bởi hệ thống EVO-RL MSCC Research Framework.*
