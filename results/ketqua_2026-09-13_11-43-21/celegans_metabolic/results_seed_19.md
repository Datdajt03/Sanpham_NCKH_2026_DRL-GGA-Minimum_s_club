# Báo Cáo Kết Quả Thực Nghiệm: Seed #19 (Seed = `64086408`)

**Tập dữ liệu đồ thị:** `celegans_metabolic` ($|V| = 453$, $|E| = 2025$, Density = $0.0198$, $s = 2$)  
**Hạt giống cố định (Seed Value):** `64086408` (Lần chạy 19/20 từ `seedun.md`)  
**Thời gian thực thi:** `2026-09-13 14:21:53`  
**Môi trường tính toán:** `Hybrid Co-Processing [CPU: 12 Cores song song (GA/C++ igraph) + GPU: NVIDIA GeForce RTX 3050 Laptop GPU (PPO Tensor Cores)]`  

---

## 1. Bảng Thống Kê Hiệu Năng Chi Tiết Các Thuật Toán (Seed #19)

| Chiến lược / Thuật toán | Best Cover (Min) | Best Fitness | Mean $\pm$ Std | Median | Vi phạm ($diam > s$) | Độ đa dạng | Khả thi ($100\%$) | Thời gian (s) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **PPO-AOS** | **29** | **29.00** | 31.52 $\pm$ 4.34 | 29.0 | 0.00 | 0.969 |  Đạt chuẩn | 411.68s |
| MAB-AOS | 30 | 30.00 | 32.74 $\pm$ 4.76 | 30.0 | 0.00 | 0.941 |  Đạt chuẩn | 495.00s |
| Greedy-AOS | 29 | 29.00 | 31.05 $\pm$ 4.87 | 29.0 | 0.00 | 0.961 |  Đạt chuẩn | 490.10s |
| I-MSM | 30 | 30.00 | 30.56 $\pm$ 0.74 | 30.0 | 0.00 | 0.000 |  Đạt chuẩn | 223.30s |
| CCA | 30 | 30.00 | 30.06 $\pm$ 0.24 | 30.0 | 0.00 | 0.000 |  Đạt chuẩn | 14.81s |
| No-RL | 29 | 29.00 | 31.55 $\pm$ 4.15 | 30.0 | 0.00 | 0.955 |  Đạt chuẩn | 434.15s |
| Fixed | 29 | 29.00 | 30.78 $\pm$ 3.51 | 30.0 | 0.00 | 0.961 |  Đạt chuẩn | 192.90s |
| Random | 29 | 29.00 | 31.55 $\pm$ 4.15 | 30.0 | 0.00 | 0.955 |  Đạt chuẩn | 325.61s |

---

## 2. Cấu Trúc Nghiệm Tốt Nhất Trong Lần Chạy (Best Solution Clusters)
- **Thuật toán đạt Best:** `PPO-AOS` (Cover = `29` clubs, Fitness = `29.00`)
- **Kích thước các cụm ($s$-clubs):** `[21, 136, 14, 11, 9, 28, 73, 15, 36, 3, 11, 21, 5, 12, 13, 9, 10, 2, 1, 3, 3, 4, 1, 2, 1, 2, 2, 2, 3]`
- **Số thế hệ tiến hóa:** `175` generations

*(Có tổng cộng 29 cụm $s$-club hợp lệ, chi tiết toàn bộ đỉnh được lưu trong file `results_seed_19.json`)*

---
*File được sinh tự động bởi hệ thống EVO-RL MSCC Research Framework.*
