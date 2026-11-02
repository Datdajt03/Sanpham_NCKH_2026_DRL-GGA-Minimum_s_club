# Báo Cáo Kết Quả Thực Nghiệm: Seed #02 (Seed = `21042026`)

**Tập dữ liệu đồ thị:** `celegans_metabolic` ($|V| = 453$, $|E| = 2025$, Density = $0.0198$, $s = 2$)  
**Hạt giống cố định (Seed Value):** `21042026` (Lần chạy 02/20 từ `seedun.md`)  
**Thời gian thực thi:** `2026-09-13 13:29:28`  
**Môi trường tính toán:** `Hybrid Co-Processing [CPU: 12 Cores song song (GA/C++ igraph) + GPU: NVIDIA GeForce RTX 3050 Laptop GPU (PPO Tensor Cores)]`  

---

## 1. Bảng Thống Kê Hiệu Năng Chi Tiết Các Thuật Toán (Seed #2)

| Chiến lược / Thuật toán | Best Cover (Min) | Best Fitness | Mean $\pm$ Std | Median | Vi phạm ($diam > s$) | Độ đa dạng | Khả thi ($100\%$) | Thời gian (s) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **PPO-AOS** | **29** | **29.00** | 31.10 $\pm$ 4.14 | 29.0 | 0.00 | 0.957 |  Đạt chuẩn | 440.45s |
| MAB-AOS | 29 | 29.00 | 31.65 $\pm$ 4.80 | 29.0 | 0.00 | 0.931 |  Đạt chuẩn | 420.74s |
| Greedy-AOS | 30 | 30.00 | 32.46 $\pm$ 3.95 | 30.0 | 0.00 | 0.933 |  Đạt chuẩn | 488.45s |
| I-MSM | 29 | 29.00 | 30.05 $\pm$ 2.18 | 29.0 | 0.00 | 0.000 |  Đạt chuẩn | 215.54s |
| CCA | 29 | 29.00 | 29.47 $\pm$ 1.57 | 29.0 | 0.00 | 0.000 |  Đạt chuẩn | 22.01s |
| No-RL | 29 | 29.00 | 30.77 $\pm$ 3.98 | 29.0 | 0.00 | 0.962 |  Đạt chuẩn | 277.55s |
| Fixed | 29 | 29.00 | 31.18 $\pm$ 3.72 | 29.0 | 0.00 | 0.918 |  Đạt chuẩn | 194.85s |
| Random | 29 | 29.00 | 30.77 $\pm$ 3.98 | 29.0 | 0.00 | 0.962 |  Đạt chuẩn | 279.07s |

---

## 2. Cấu Trúc Nghiệm Tốt Nhất Trong Lần Chạy (Best Solution Clusters)
- **Thuật toán đạt Best:** `PPO-AOS` (Cover = `29` clubs, Fitness = `29.00`)
- **Kích thước các cụm ($s$-clubs):** `[138, 76, 10, 19, 11, 9, 20, 22, 14, 37, 2, 19, 5, 9, 3, 8, 3, 8, 12, 3, 2, 3, 5, 1, 3, 5, 2, 3, 1]`
- **Số thế hệ tiến hóa:** `150` generations

*(Có tổng cộng 29 cụm $s$-club hợp lệ, chi tiết toàn bộ đỉnh được lưu trong file `results_seed_2.json`)*

---
*File được sinh tự động bởi hệ thống EVO-RL MSCC Research Framework.*
