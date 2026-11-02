# Báo Cáo Kết Quả Thực Nghiệm: Seed #14 (Seed = `24681357`)

**Tập dữ liệu đồ thị:** `celegans_metabolic` ($|V| = 453$, $|E| = 2025$, Density = $0.0198$, $s = 2$)  
**Hạt giống cố định (Seed Value):** `24681357` (Lần chạy 14/20 từ `seedun.md`)  
**Thời gian thực thi:** `2026-09-13 14:00:48`  
**Môi trường tính toán:** `Hybrid Co-Processing [CPU: 12 Cores song song (GA/C++ igraph) + GPU: NVIDIA GeForce RTX 3050 Laptop GPU (PPO Tensor Cores)]`  

---

## 1. Bảng Thống Kê Hiệu Năng Chi Tiết Các Thuật Toán (Seed #14)

| Chiến lược / Thuật toán | Best Cover (Min) | Best Fitness | Mean $\pm$ Std | Median | Vi phạm ($diam > s$) | Độ đa dạng | Khả thi ($100\%$) | Thời gian (s) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **PPO-AOS** | **29** | **29.00** | 32.18 $\pm$ 5.51 | 29.0 | 0.00 | 0.863 |  Đạt chuẩn | 353.86s |
| MAB-AOS | 29 | 29.00 | 31.57 $\pm$ 5.03 | 29.0 | 0.00 | 0.909 |  Đạt chuẩn | 297.76s |
| Greedy-AOS | 29 | 29.00 | 31.18 $\pm$ 4.40 | 29.0 | 0.00 | 0.955 |  Đạt chuẩn | 393.42s |
| I-MSM | 29 | 29.00 | 29.00 $\pm$ 0.00 | 29.0 | 0.00 | 0.000 |  Đạt chuẩn | 172.76s |
| CCA | 29 | 29.00 | 29.63 $\pm$ 0.95 | 29.0 | 0.00 | 0.000 |  Đạt chuẩn | 33.65s |
| No-RL | 30 | 30.00 | 32.22 $\pm$ 4.83 | 30.0 | 0.00 | 0.942 |  Đạt chuẩn | 224.36s |
| Fixed | 31 | 31.00 | 32.69 $\pm$ 4.17 | 31.0 | 0.00 | 0.963 |  Đạt chuẩn | 180.46s |
| Random | 30 | 30.00 | 32.22 $\pm$ 4.83 | 30.0 | 0.00 | 0.942 |  Đạt chuẩn | 223.53s |

---

## 2. Cấu Trúc Nghiệm Tốt Nhất Trong Lần Chạy (Best Solution Clusters)
- **Thuật toán đạt Best:** `PPO-AOS` (Cover = `29` clubs, Fitness = `29.00`)
- **Kích thước các cụm ($s$-clubs):** `[136, 14, 35, 11, 8, 19, 20, 6, 21, 71, 2, 12, 26, 5, 8, 14, 4, 8, 3, 3, 7, 4, 1, 2, 5, 2, 2, 3, 1]`
- **Số thế hệ tiến hóa:** `168` generations

*(Có tổng cộng 29 cụm $s$-club hợp lệ, chi tiết toàn bộ đỉnh được lưu trong file `results_seed_14.json`)*

---
*File được sinh tự động bởi hệ thống EVO-RL MSCC Research Framework.*
