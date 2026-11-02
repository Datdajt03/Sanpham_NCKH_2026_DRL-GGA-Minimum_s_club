# Báo Cáo Kết Quả Thực Nghiệm: Seed #13 (Seed = `13572468`)

**Tập dữ liệu đồ thị:** `celegans_metabolic` ($|V| = 453$, $|E| = 2025$, Density = $0.0198$, $s = 2$)  
**Hạt giống cố định (Seed Value):** `13572468` (Lần chạy 13/20 từ `seedun.md`)  
**Thời gian thực thi:** `2026-09-13 14:07:48`  
**Môi trường tính toán:** `Hybrid Co-Processing [CPU: 12 Cores song song (GA/C++ igraph) + GPU: NVIDIA GeForce RTX 3050 Laptop GPU (PPO Tensor Cores)]`  

---

## 1. Bảng Thống Kê Hiệu Năng Chi Tiết Các Thuật Toán (Seed #13)

| Chiến lược / Thuật toán | Best Cover (Min) | Best Fitness | Mean $\pm$ Std | Median | Vi phạm ($diam > s$) | Độ đa dạng | Khả thi ($100\%$) | Thời gian (s) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **PPO-AOS** | **33** | **33.00** | 34.82 $\pm$ 3.45 | 33.0 | 0.00 | 0.951 |  Đạt chuẩn | 349.52s |
| MAB-AOS | 30 | 30.00 | 31.98 $\pm$ 4.19 | 30.0 | 0.00 | 0.952 |  Đạt chuẩn | 432.28s |
| Greedy-AOS | 29 | 29.00 | 31.25 $\pm$ 5.18 | 29.0 | 0.00 | 0.890 |  Đạt chuẩn | 500.32s |
| I-MSM | 30 | 30.00 | 30.53 $\pm$ 2.12 | 30.0 | 0.00 | 0.000 |  Đạt chuẩn | 184.27s |
| CCA | 29 | 29.00 | 29.67 $\pm$ 0.94 | 29.0 | 0.00 | 0.000 |  Đạt chuẩn | 29.76s |
| No-RL | 29 | 29.00 | 31.97 $\pm$ 5.37 | 29.0 | 0.00 | 0.838 |  Đạt chuẩn | 355.42s |
| Fixed | 29 | 29.00 | 30.86 $\pm$ 4.34 | 29.0 | 0.00 | 0.926 |  Đạt chuẩn | 385.38s |
| Random | 29 | 29.00 | 31.97 $\pm$ 5.37 | 29.0 | 0.00 | 0.838 |  Đạt chuẩn | 271.92s |

---

## 2. Cấu Trúc Nghiệm Tốt Nhất Trong Lần Chạy (Best Solution Clusters)
- **Thuật toán đạt Best:** `Greedy-AOS` (Cover = `29` clubs, Fitness = `29.00`)
- **Kích thước các cụm ($s$-clubs):** `[39, 155, 60, 14, 11, 9, 12, 20, 2, 7, 29, 19, 5, 15, 8, 10, 2, 8, 1, 3, 1, 5, 1, 4, 2, 5, 2, 3, 1]`
- **Số thế hệ tiến hóa:** `142` generations

*(Có tổng cộng 29 cụm $s$-club hợp lệ, chi tiết toàn bộ đỉnh được lưu trong file `results_seed_13.json`)*

---
*File được sinh tự động bởi hệ thống EVO-RL MSCC Research Framework.*
