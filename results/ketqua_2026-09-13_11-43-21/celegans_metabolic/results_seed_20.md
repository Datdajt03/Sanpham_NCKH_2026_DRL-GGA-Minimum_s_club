# Báo Cáo Kết Quả Thực Nghiệm: Seed #20 (Seed = `86088608`)

**Tập dữ liệu đồ thị:** `celegans_metabolic` ($|V| = 453$, $|E| = 2025$, Density = $0.0198$, $s = 2$)  
**Hạt giống cố định (Seed Value):** `86088608` (Lần chạy 20/20 từ `seedun.md`)  
**Thời gian thực thi:** `2026-09-13 14:12:26`  
**Môi trường tính toán:** `Hybrid Co-Processing [CPU: 12 Cores song song (GA/C++ igraph) + GPU: NVIDIA GeForce RTX 3050 Laptop GPU (PPO Tensor Cores)]`  

---

## 1. Bảng Thống Kê Hiệu Năng Chi Tiết Các Thuật Toán (Seed #20)

| Chiến lược / Thuật toán | Best Cover (Min) | Best Fitness | Mean $\pm$ Std | Median | Vi phạm ($diam > s$) | Độ đa dạng | Khả thi ($100\%$) | Thời gian (s) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **PPO-AOS** | **31** | **31.00** | 33.64 $\pm$ 4.61 | 31.0 | 0.00 | 0.930 |  Đạt chuẩn | 312.41s |
| MAB-AOS | 29 | 29.00 | 31.76 $\pm$ 5.19 | 29.0 | 0.00 | 0.919 |  Đạt chuẩn | 435.91s |
| Greedy-AOS | 29 | 29.00 | 31.31 $\pm$ 4.91 | 29.0 | 0.00 | 0.943 |  Đạt chuẩn | 287.17s |
| I-MSM | 31 | 31.00 | 31.00 $\pm$ 0.00 | 31.0 | 0.00 | 0.000 |  Đạt chuẩn | 147.10s |
| CCA | 29 | 29.00 | 29.73 $\pm$ 1.16 | 29.0 | 0.00 | 0.000 |  Đạt chuẩn | 24.19s |
| No-RL | 30 | 30.00 | 32.60 $\pm$ 4.90 | 30.0 | 0.00 | 0.955 |  Đạt chuẩn | 175.27s |
| Fixed | 29 | 29.00 | 31.24 $\pm$ 4.47 | 29.0 | 0.00 | 0.972 |  Đạt chuẩn | 215.61s |
| Random | 30 | 30.00 | 32.60 $\pm$ 4.90 | 30.0 | 0.00 | 0.955 |  Đạt chuẩn | 160.04s |

---

## 2. Cấu Trúc Nghiệm Tốt Nhất Trong Lần Chạy (Best Solution Clusters)
- **Thuật toán đạt Best:** `MAB-AOS` (Cover = `29` clubs, Fitness = `29.00`)
- **Kích thước các cụm ($s$-clubs):** `[139, 85, 12, 20, 14, 8, 18, 17, 38, 2, 7, 21, 5, 6, 14, 7, 7, 2, 4, 9, 3, 1, 2, 3, 2, 2, 3, 1, 1]`
- **Số thế hệ tiến hóa:** `160` generations

*(Có tổng cộng 29 cụm $s$-club hợp lệ, chi tiết toàn bộ đỉnh được lưu trong file `results_seed_20.json`)*

---
*File được sinh tự động bởi hệ thống EVO-RL MSCC Research Framework.*
