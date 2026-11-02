# Báo Cáo Kết Quả Thực Nghiệm: Seed #11 (Seed = `11223344`)

**Tập dữ liệu đồ thị:** `dolphins` ($|V| = 62$, $|E| = 159$, Density = $0.0841$, $s = 2$)  
**Hạt giống cố định (Seed Value):** `11223344` (Lần chạy 11/20 từ `seedun.md`)  
**Thời gian thực thi:** `2026-09-13 11:46:27`  
**Môi trường tính toán:** `Hybrid Co-Processing [CPU: 12 Cores song song (GA/C++ igraph) + GPU: NVIDIA GeForce RTX 3050 Laptop GPU (PPO Tensor Cores)]`  

---

## 1. Bảng Thống Kê Hiệu Năng Chi Tiết Các Thuật Toán (Seed #11)

| Chiến lược / Thuật toán | Best Cover (Min) | Best Fitness | Mean $\pm$ Std | Median | Vi phạm ($diam > s$) | Độ đa dạng | Khả thi ($100\%$) | Thời gian (s) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **PPO-AOS** | **13** | **13.00** | 13.29 $\pm$ 0.70 | 13.0 | 0.00 | 0.895 |  Đạt chuẩn | 4.87s |
| MAB-AOS | 13 | 13.00 | 13.25 $\pm$ 0.66 | 13.0 | 0.00 | 0.769 |  Đạt chuẩn | 3.90s |
| Greedy-AOS | 13 | 13.00 | 13.12 $\pm$ 0.49 | 13.0 | 0.00 | 0.834 |  Đạt chuẩn | 3.35s |
| I-MSM | 14 | 14.00 | 14.27 $\pm$ 0.45 | 14.0 | 0.00 | 0.000 |  Đạt chuẩn | 0.57s |
| CCA | 14 | 14.00 | 14.16 $\pm$ 0.36 | 14.0 | 0.00 | 0.000 |  Đạt chuẩn | 0.12s |
| No-RL | 13 | 13.00 | 13.24 $\pm$ 0.58 | 13.0 | 0.00 | 0.863 |  Đạt chuẩn | 3.76s |
| Fixed | 13 | 13.00 | 13.37 $\pm$ 0.55 | 13.0 | 0.00 | 0.922 |  Đạt chuẩn | 3.99s |
| Random | 13 | 13.00 | 13.24 $\pm$ 0.58 | 13.0 | 0.00 | 0.863 |  Đạt chuẩn | 3.92s |

---

## 2. Cấu Trúc Nghiệm Tốt Nhất Trong Lần Chạy (Best Solution Clusters)
- **Thuật toán đạt Best:** `PPO-AOS` (Cover = `13` clubs, Fitness = `13.00`)
- **Kích thước các cụm ($s$-clubs):** `[6, 7, 3, 5, 5, 4, 5, 9, 7, 4, 2, 3, 2]`
- **Số thế hệ tiến hóa:** `122` generations

### Chi tiết các cụm $s$-club thành phần:
- **Club 5** (Size = 6 đỉnh): `[0, 10, 28, 30, 42, 47]`
- **Club 6** (Size = 7 đỉnh): `[1, 7, 19, 26, 27, 41, 54]`
- **Club 3** (Size = 3 đỉnh): `[2, 53, 61]`
- **Club 7** (Size = 5 đỉnh): `[3, 8, 15, 36, 59]`
- **Club 8** (Size = 5 đỉnh): `[4, 11, 23, 51, 55]`
- **Club 9** (Size = 4 đỉnh): `[5, 9, 13, 56]`
- **Club 10** (Size = 5 đỉnh): `[6, 17, 22, 25, 31]`
- **Club 11** (Size = 9 đỉnh): `[12, 14, 16, 33, 34, 37, 40, 43, 50]`
- **Club 12** (Size = 7 đỉnh): `[18, 21, 24, 29, 35, 45, 52]`
- **Club 4** (Size = 4 đỉnh): `[20, 38, 44, 58]`
- **Club 2** (Size = 2 đỉnh): `[32, 60]`
- **Club 13** (Size = 3 đỉnh): `[39, 48, 57]`
- **Club 1** (Size = 2 đỉnh): `[46, 49]`

---
*File được sinh tự động bởi hệ thống EVO-RL MSCC Research Framework.*
