# Báo Cáo Kết Quả Thực Nghiệm: Seed #08 (Seed = `20260523`)

**Tập dữ liệu đồ thị:** `dolphins` ($|V| = 62$, $|E| = 159$, Density = $0.0841$, $s = 2$)  
**Hạt giống cố định (Seed Value):** `20260523` (Lần chạy 08/20 từ `seedun.md`)  
**Thời gian thực thi:** `2026-09-13 11:46:05`  
**Môi trường tính toán:** `Hybrid Co-Processing [CPU: 12 Cores song song (GA/C++ igraph) + GPU: NVIDIA GeForce RTX 3050 Laptop GPU (PPO Tensor Cores)]`  

---

## 1. Bảng Thống Kê Hiệu Năng Chi Tiết Các Thuật Toán (Seed #8)

| Chiến lược / Thuật toán | Best Cover (Min) | Best Fitness | Mean $\pm$ Std | Median | Vi phạm ($diam > s$) | Độ đa dạng | Khả thi ($100\%$) | Thời gian (s) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **PPO-AOS** | **13** | **13.00** | 13.23 $\pm$ 0.58 | 13.0 | 0.00 | 0.895 |  Đạt chuẩn | 6.57s |
| MAB-AOS | 13 | 13.00 | 13.46 $\pm$ 0.71 | 13.0 | 0.00 | 0.889 |  Đạt chuẩn | 5.25s |
| Greedy-AOS | 13 | 13.00 | 13.26 $\pm$ 0.55 | 13.0 | 0.00 | 0.912 |  Đạt chuẩn | 3.91s |
| I-MSM | 14 | 14.00 | 14.38 $\pm$ 0.72 | 14.0 | 0.00 | 0.000 |  Đạt chuẩn | 0.55s |
| CCA | 14 | 14.00 | 14.00 $\pm$ 0.00 | 14.0 | 0.00 | 0.000 |  Đạt chuẩn | 0.10s |
| No-RL | 13 | 13.00 | 13.21 $\pm$ 0.66 | 13.0 | 0.00 | 0.898 |  Đạt chuẩn | 3.53s |
| Fixed | 13 | 13.00 | 13.19 $\pm$ 0.59 | 13.0 | 0.00 | 0.899 |  Đạt chuẩn | 3.21s |
| Random | 13 | 13.00 | 13.21 $\pm$ 0.66 | 13.0 | 0.00 | 0.898 |  Đạt chuẩn | 3.60s |

---

## 2. Cấu Trúc Nghiệm Tốt Nhất Trong Lần Chạy (Best Solution Clusters)
- **Thuật toán đạt Best:** `PPO-AOS` (Cover = `13` clubs, Fitness = `13.00`)
- **Kích thước các cụm ($s$-clubs):** `[5, 7, 3, 5, 6, 5, 5, 10, 4, 5, 2, 3, 2]`
- **Số thế hệ tiến hóa:** `122` generations

### Chi tiết các cụm $s$-club thành phần:
- **Club 8** (Size = 5 đỉnh): `[0, 28, 30, 42, 47]`
- **Club 9** (Size = 7 đỉnh): `[1, 7, 19, 26, 27, 41, 54]`
- **Club 1** (Size = 3 đỉnh): `[2, 53, 61]`
- **Club 7** (Size = 5 đỉnh): `[3, 8, 15, 36, 59]`
- **Club 10** (Size = 6 đỉnh): `[4, 11, 23, 24, 51, 55]`
- **Club 5** (Size = 5 đỉnh): `[5, 6, 9, 13, 56]`
- **Club 11** (Size = 5 đỉnh): `[10, 18, 29, 35, 45]`
- **Club 6** (Size = 10 đỉnh): `[12, 14, 16, 21, 33, 34, 37, 40, 43, 50]`
- **Club 3** (Size = 4 đỉnh): `[17, 22, 25, 31]`
- **Club 4** (Size = 5 đỉnh): `[20, 38, 44, 52, 58]`
- **Club 12** (Size = 2 đỉnh): `[32, 60]`
- **Club 2** (Size = 3 đỉnh): `[39, 48, 57]`
- **Club 13** (Size = 2 đỉnh): `[46, 49]`

---
*File được sinh tự động bởi hệ thống EVO-RL MSCC Research Framework.*
