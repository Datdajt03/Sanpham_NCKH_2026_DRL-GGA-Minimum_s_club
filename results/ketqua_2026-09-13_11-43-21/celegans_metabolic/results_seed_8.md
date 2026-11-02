# Báo Cáo Kết Quả Thực Nghiệm: Seed #08 (Seed = `20260523`)

**Tập dữ liệu đồ thị:** `celegans_metabolic` ($|V| = 453$, $|E| = 2025$, Density = $0.0198$, $s = 2$)  
**Hạt giống cố định (Seed Value):** `20260523` (Lần chạy 08/20 từ `seedun.md`)  
**Thời gian thực thi:** `2026-09-13 13:36:26`  
**Môi trường tính toán:** `Hybrid Co-Processing [CPU: 12 Cores song song (GA/C++ igraph) + GPU: NVIDIA GeForce RTX 3050 Laptop GPU (PPO Tensor Cores)]`  

---

## 1. Bảng Thống Kê Hiệu Năng Chi Tiết Các Thuật Toán (Seed #8)

| Chiến lược / Thuật toán | Best Cover (Min) | Best Fitness | Mean $\pm$ Std | Median | Vi phạm ($diam > s$) | Độ đa dạng | Khả thi ($100\%$) | Thời gian (s) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **PPO-AOS** | **31** | **31.00** | 33.30 $\pm$ 4.28 | 31.0 | 0.00 | 0.926 |  Đạt chuẩn | 239.47s |
| MAB-AOS | 31 | 31.00 | 32.76 $\pm$ 3.46 | 31.0 | 0.00 | 0.947 |  Đạt chuẩn | 323.31s |
| Greedy-AOS | 29 | 29.00 | 30.84 $\pm$ 3.84 | 29.0 | 0.00 | 0.915 |  Đạt chuẩn | 428.52s |
| I-MSM | 29 | 29.00 | 30.16 $\pm$ 3.26 | 29.0 | 0.00 | 0.000 |  Đạt chuẩn | 204.78s |
| CCA | 29 | 29.00 | 29.78 $\pm$ 1.13 | 29.0 | 0.00 | 0.000 |  Đạt chuẩn | 29.15s |
| No-RL | 29 | 29.00 | 31.31 $\pm$ 4.50 | 29.0 | 0.00 | 0.969 |  Đạt chuẩn | 477.54s |
| Fixed | 30 | 30.00 | 32.12 $\pm$ 4.47 | 30.0 | 0.00 | 0.961 |  Đạt chuẩn | 564.87s |
| Random | 29 | 29.00 | 31.31 $\pm$ 4.50 | 29.0 | 0.00 | 0.969 |  Đạt chuẩn | 488.49s |

---

## 2. Cấu Trúc Nghiệm Tốt Nhất Trong Lần Chạy (Best Solution Clusters)
- **Thuật toán đạt Best:** `Greedy-AOS` (Cover = `29` clubs, Fitness = `29.00`)
- **Kích thước các cụm ($s$-clubs):** `[14, 144, 92, 12, 11, 9, 14, 21, 16, 37, 1, 10, 18, 5, 6, 5, 8, 7, 2, 2, 3, 1, 3, 1, 2, 3, 2, 3, 1]`
- **Số thế hệ tiến hóa:** `156` generations

*(Có tổng cộng 29 cụm $s$-club hợp lệ, chi tiết toàn bộ đỉnh được lưu trong file `results_seed_8.json`)*

---
*File được sinh tự động bởi hệ thống EVO-RL MSCC Research Framework.*
