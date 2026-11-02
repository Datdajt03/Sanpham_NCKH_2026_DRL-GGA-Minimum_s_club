# Báo Cáo Kết Quả Thực Nghiệm: Seed #01 (Seed = `17032026`)

**Tập dữ liệu đồ thị:** `celegans_metabolic` ($|V| = 453$, $|E| = 2025$, Density = $0.0198$, $s = 2$)  
**Hạt giống cố định (Seed Value):** `17032026` (Lần chạy 01/20 từ `seedun.md`)  
**Thời gian thực thi:** `2026-09-13 13:35:54`  
**Môi trường tính toán:** `Hybrid Co-Processing [CPU: 12 Cores song song (GA/C++ igraph) + GPU: NVIDIA GeForce RTX 3050 Laptop GPU (PPO Tensor Cores)]`  

---

## 1. Bảng Thống Kê Hiệu Năng Chi Tiết Các Thuật Toán (Seed #1)

| Chiến lược / Thuật toán | Best Cover (Min) | Best Fitness | Mean $\pm$ Std | Median | Vi phạm ($diam > s$) | Độ đa dạng | Khả thi ($100\%$) | Thời gian (s) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **PPO-AOS** | **29** | **29.00** | 31.62 $\pm$ 4.91 | 29.0 | 0.00 | 0.897 |  Đạt chuẩn | 333.28s |
| MAB-AOS | 31 | 31.00 | 33.19 $\pm$ 4.40 | 31.0 | 0.00 | 0.940 |  Đạt chuẩn | 482.80s |
| Greedy-AOS | 30 | 30.00 | 32.08 $\pm$ 3.89 | 31.0 | 0.00 | 0.307 |  Đạt chuẩn | 574.19s |
| I-MSM | 30 | 30.00 | 30.62 $\pm$ 0.93 | 30.5 | 0.00 | 0.000 |  Đạt chuẩn | 342.54s |
| CCA | 29 | 29.00 | 29.75 $\pm$ 0.83 | 29.5 | 0.00 | 0.000 |  Đạt chuẩn | 36.91s |
| No-RL | 31 | 31.00 | 33.43 $\pm$ 4.16 | 31.0 | 0.00 | 0.968 |  Đạt chuẩn | 345.36s |
| Fixed | 31 | 31.00 | 32.88 $\pm$ 3.92 | 31.0 | 0.00 | 0.956 |  Đạt chuẩn | 263.12s |
| Random | 31 | 31.00 | 33.43 $\pm$ 4.16 | 31.0 | 0.00 | 0.968 |  Đạt chuẩn | 346.15s |

---

## 2. Cấu Trúc Nghiệm Tốt Nhất Trong Lần Chạy (Best Solution Clusters)
- **Thuật toán đạt Best:** `PPO-AOS` (Cover = `29` clubs, Fitness = `29.00`)
- **Kích thước các cụm ($s$-clubs):** `[11, 128, 79, 15, 11, 9, 18, 15, 26, 20, 2, 29, 22, 5, 11, 8, 7, 7, 4, 2, 1, 9, 4, 1, 2, 2, 3, 1, 1]`
- **Số thế hệ tiến hóa:** `164` generations

*(Có tổng cộng 29 cụm $s$-club hợp lệ, chi tiết toàn bộ đỉnh được lưu trong file `results_seed_1.json`)*

---
*File được sinh tự động bởi hệ thống EVO-RL MSCC Research Framework.*
