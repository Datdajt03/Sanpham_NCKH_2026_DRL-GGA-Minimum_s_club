# Báo Cáo Kết Quả Thực Nghiệm: Seed #11 (Seed = `11223344`)

**Tập dữ liệu đồ thị:** `celegans_metabolic` ($|V| = 453$, $|E| = 2025$, Density = $0.0198$, $s = 2$)  
**Hạt giống cố định (Seed Value):** `11223344` (Lần chạy 11/20 từ `seedun.md`)  
**Thời gian thực thi:** `2026-09-13 14:01:34`  
**Môi trường tính toán:** `Hybrid Co-Processing [CPU: 12 Cores song song (GA/C++ igraph) + GPU: NVIDIA GeForce RTX 3050 Laptop GPU (PPO Tensor Cores)]`  

---

## 1. Bảng Thống Kê Hiệu Năng Chi Tiết Các Thuật Toán (Seed #11)

| Chiến lược / Thuật toán | Best Cover (Min) | Best Fitness | Mean $\pm$ Std | Median | Vi phạm ($diam > s$) | Độ đa dạng | Khả thi ($100\%$) | Thời gian (s) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **PPO-AOS** | **30** | **30.00** | 32.47 $\pm$ 4.49 | 30.0 | 0.00 | 0.970 |  Đạt chuẩn | 258.24s |
| MAB-AOS | 29 | 29.00 | 31.33 $\pm$ 4.58 | 29.0 | 0.00 | 0.888 |  Đạt chuẩn | 285.82s |
| Greedy-AOS | 29 | 29.00 | 31.39 $\pm$ 4.94 | 29.0 | 0.00 | 0.947 |  Đạt chuẩn | 238.56s |
| I-MSM | 31 | 31.00 | 32.08 $\pm$ 1.63 | 31.0 | 0.00 | 0.000 |  Đạt chuẩn | 256.88s |
| CCA | 31 | 31.00 | 31.22 $\pm$ 0.63 | 31.0 | 0.00 | 0.000 |  Đạt chuẩn | 26.31s |
| No-RL | 29 | 29.00 | 31.60 $\pm$ 5.14 | 29.0 | 0.00 | 0.959 |  Đạt chuẩn | 315.41s |
| Fixed | 30 | 30.00 | 31.76 $\pm$ 4.27 | 30.0 | 0.00 | 0.946 |  Đạt chuẩn | 673.87s |
| Random | 29 | 29.00 | 31.60 $\pm$ 5.14 | 29.0 | 0.00 | 0.959 |  Đạt chuẩn | 312.70s |

---

## 2. Cấu Trúc Nghiệm Tốt Nhất Trong Lần Chạy (Best Solution Clusters)
- **Thuật toán đạt Best:** `MAB-AOS` (Cover = `29` clubs, Fitness = `29.00`)
- **Kích thước các cụm ($s$-clubs):** `[29, 122, 14, 71, 11, 8, 13, 18, 23, 13, 3, 3, 13, 34, 21, 5, 11, 8, 10, 2, 1, 3, 5, 1, 2, 3, 2, 3, 1]`
- **Số thế hệ tiến hóa:** `173` generations

*(Có tổng cộng 29 cụm $s$-club hợp lệ, chi tiết toàn bộ đỉnh được lưu trong file `results_seed_11.json`)*

---
*File được sinh tự động bởi hệ thống EVO-RL MSCC Research Framework.*
