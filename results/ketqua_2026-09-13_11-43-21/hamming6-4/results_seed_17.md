# Báo Cáo Kết Quả Thực Nghiệm: Seed #17 (Seed = `52013140`)

**Tập dữ liệu đồ thị:** `hamming6-4` ($|V| = 64$, $|E| = 704$, Density = $0.3492$, $s = 2$)  
**Hạt giống cố định (Seed Value):** `52013140` (Lần chạy 17/20 từ `seedun.md`)  
**Thời gian thực thi:** `2026-09-13 14:55:22`  
**Môi trường tính toán:** `Hybrid Co-Processing [CPU: 12 Cores song song (GA/C++ igraph) + GPU: NVIDIA GeForce RTX 3050 Laptop GPU (PPO Tensor Cores)]`  

---

## 1. Bảng Thống Kê Hiệu Năng Chi Tiết Các Thuật Toán (Seed #17)

| Chiến lược / Thuật toán | Best Cover (Min) | Best Fitness | Mean $\pm$ Std | Median | Vi phạm ($diam > s$) | Độ đa dạng | Khả thi ($100\%$) | Thời gian (s) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **PPO-AOS** | **1** | **1.00** | 1.12 $\pm$ 0.58 | 1.0 | 0.00 | 0.000 |  Đạt chuẩn | 3.05s |
| MAB-AOS | 1 | 1.00 | 1.06 $\pm$ 0.33 | 1.0 | 0.00 | 0.000 |  Đạt chuẩn | 2.15s |
| Greedy-AOS | 1 | 1.00 | 1.04 $\pm$ 0.31 | 1.0 | 0.00 | 0.000 |  Đạt chuẩn | 2.14s |
| I-MSM | 1 | 1.00 | 1.00 $\pm$ 0.00 | 1.0 | 0.00 | 0.000 |  Đạt chuẩn | 0.97s |
| CCA | 1 | 1.00 | 1.00 $\pm$ 0.00 | 1.0 | 0.00 | 0.000 |  Đạt chuẩn | 0.03s |
| No-RL | 1 | 1.00 | 1.13 $\pm$ 0.57 | 1.0 | 0.00 | 0.000 |  Đạt chuẩn | 2.11s |
| Fixed | 1 | 1.00 | 1.07 $\pm$ 0.34 | 1.0 | 0.00 | 0.000 |  Đạt chuẩn | 2.34s |
| Random | 1 | 1.00 | 1.13 $\pm$ 0.57 | 1.0 | 0.00 | 0.000 |  Đạt chuẩn | 2.04s |

---

## 2. Cấu Trúc Nghiệm Tốt Nhất Trong Lần Chạy (Best Solution Clusters)
- **Thuật toán đạt Best:** `PPO-AOS` (Cover = `1` clubs, Fitness = `1.00`)
- **Kích thước các cụm ($s$-clubs):** `[64]`
- **Số thế hệ tiến hóa:** `106` generations

### Chi tiết các cụm $s$-club thành phần:
- **Club 1** (Size = 64 đỉnh): `[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63]`

---
*File được sinh tự động bởi hệ thống EVO-RL MSCC Research Framework.*
