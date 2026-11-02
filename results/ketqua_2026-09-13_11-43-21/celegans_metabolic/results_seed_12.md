# Báo Cáo Kết Quả Thực Nghiệm: Seed #12 (Seed = `12344321`)

**Tập dữ liệu đồ thị:** `celegans_metabolic` ($|V| = 453$, $|E| = 2025$, Density = $0.0198$, $s = 2$)  
**Hạt giống cố định (Seed Value):** `12344321` (Lần chạy 12/20 từ `seedun.md`)  
**Thời gian thực thi:** `2026-09-13 14:01:21`  
**Môi trường tính toán:** `Hybrid Co-Processing [CPU: 12 Cores song song (GA/C++ igraph) + GPU: NVIDIA GeForce RTX 3050 Laptop GPU (PPO Tensor Cores)]`  

---

## 1. Bảng Thống Kê Hiệu Năng Chi Tiết Các Thuật Toán (Seed #12)

| Chiến lược / Thuật toán | Best Cover (Min) | Best Fitness | Mean $\pm$ Std | Median | Vi phạm ($diam > s$) | Độ đa dạng | Khả thi ($100\%$) | Thời gian (s) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **PPO-AOS** | **31** | **31.00** | 32.79 $\pm$ 3.90 | 31.0 | 0.00 | 0.955 |  Đạt chuẩn | 329.76s |
| MAB-AOS | 29 | 29.00 | 31.35 $\pm$ 4.42 | 29.0 | 0.00 | 0.889 |  Đạt chuẩn | 380.41s |
| Greedy-AOS | 29 | 29.00 | 31.62 $\pm$ 4.65 | 30.0 | 0.00 | 0.533 |  Đạt chuẩn | 325.30s |
| I-MSM | 29 | 29.00 | 30.71 $\pm$ 1.93 | 30.0 | 0.00 | 0.000 |  Đạt chuẩn | 416.34s |
| CCA | 29 | 29.00 | 29.50 $\pm$ 0.63 | 29.0 | 0.00 | 0.000 |  Đạt chuẩn | 30.42s |
| No-RL | 29 | 29.00 | 31.48 $\pm$ 4.74 | 29.0 | 0.00 | 0.911 |  Đạt chuẩn | 203.08s |
| Fixed | 29 | 29.00 | 31.25 $\pm$ 4.62 | 29.0 | 0.00 | 0.896 |  Đạt chuẩn | 372.02s |
| Random | 29 | 29.00 | 31.48 $\pm$ 4.74 | 29.0 | 0.00 | 0.911 |  Đạt chuẩn | 201.36s |

---

## 2. Cấu Trúc Nghiệm Tốt Nhất Trong Lần Chạy (Best Solution Clusters)
- **Thuật toán đạt Best:** `MAB-AOS` (Cover = `29` clubs, Fitness = `29.00`)
- **Kích thước các cụm ($s$-clubs):** `[133, 14, 29, 12, 9, 13, 84, 15, 2, 23, 22, 5, 15, 19, 4, 10, 11, 9, 2, 1, 3, 3, 2, 1, 3, 3, 2, 3, 1]`
- **Số thế hệ tiến hóa:** `164` generations

*(Có tổng cộng 29 cụm $s$-club hợp lệ, chi tiết toàn bộ đỉnh được lưu trong file `results_seed_12.json`)*

---
*File được sinh tự động bởi hệ thống EVO-RL MSCC Research Framework.*
