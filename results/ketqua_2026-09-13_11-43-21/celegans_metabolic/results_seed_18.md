# Báo Cáo Kết Quả Thực Nghiệm: Seed #18 (Seed = `20252026`)

**Tập dữ liệu đồ thị:** `celegans_metabolic` ($|V| = 453$, $|E| = 2025$, Density = $0.0198$, $s = 2$)  
**Hạt giống cố định (Seed Value):** `20252026` (Lần chạy 18/20 từ `seedun.md`)  
**Thời gian thực thi:** `2026-09-13 14:17:24`  
**Môi trường tính toán:** `Hybrid Co-Processing [CPU: 12 Cores song song (GA/C++ igraph) + GPU: NVIDIA GeForce RTX 3050 Laptop GPU (PPO Tensor Cores)]`  

---

## 1. Bảng Thống Kê Hiệu Năng Chi Tiết Các Thuật Toán (Seed #18)

| Chiến lược / Thuật toán | Best Cover (Min) | Best Fitness | Mean $\pm$ Std | Median | Vi phạm ($diam > s$) | Độ đa dạng | Khả thi ($100\%$) | Thời gian (s) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **PPO-AOS** | **29** | **29.00** | 31.86 $\pm$ 4.01 | 30.0 | 0.00 | 0.891 |  Đạt chuẩn | 235.92s |
| MAB-AOS | 29 | 29.00 | 31.44 $\pm$ 4.65 | 29.0 | 0.00 | 0.972 |  Đạt chuẩn | 296.50s |
| Greedy-AOS | 30 | 30.00 | 31.63 $\pm$ 3.86 | 30.0 | 0.00 | 0.920 |  Đạt chuẩn | 507.58s |
| I-MSM | 30 | 30.00 | 31.82 $\pm$ 2.45 | 30.0 | 0.00 | 0.000 |  Đạt chuẩn | 306.03s |
| CCA | 29 | 29.00 | 29.79 $\pm$ 1.12 | 30.0 | 0.00 | 0.000 |  Đạt chuẩn | 36.59s |
| No-RL | 30 | 30.00 | 32.40 $\pm$ 4.08 | 30.0 | 0.00 | 0.932 |  Đạt chuẩn | 447.68s |
| Fixed | 30 | 30.00 | 32.01 $\pm$ 4.29 | 30.0 | 0.00 | 0.952 |  Đạt chuẩn | 193.24s |
| Random | 30 | 30.00 | 32.40 $\pm$ 4.08 | 30.0 | 0.00 | 0.932 |  Đạt chuẩn | 368.28s |

---

## 2. Cấu Trúc Nghiệm Tốt Nhất Trong Lần Chạy (Best Solution Clusters)
- **Thuật toán đạt Best:** `PPO-AOS` (Cover = `29` clubs, Fitness = `29.00`)
- **Kích thước các cụm ($s$-clubs):** `[32, 28, 10, 91, 42, 11, 9, 17, 80, 2, 24, 19, 18, 5, 14, 5, 11, 2, 3, 3, 3, 1, 11, 3, 1, 2, 2, 3, 1]`
- **Số thế hệ tiến hóa:** `201` generations

*(Có tổng cộng 29 cụm $s$-club hợp lệ, chi tiết toàn bộ đỉnh được lưu trong file `results_seed_18.json`)*

---
*File được sinh tự động bởi hệ thống EVO-RL MSCC Research Framework.*
