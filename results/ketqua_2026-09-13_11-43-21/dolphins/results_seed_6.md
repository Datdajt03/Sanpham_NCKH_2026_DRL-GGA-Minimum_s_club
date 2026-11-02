# Báo Cáo Kết Quả Thực Nghiệm: Seed #06 (Seed = `20260317`)

**Tập dữ liệu đồ thị:** `dolphins` ($|V| = 62$, $|E| = 159$, Density = $0.0841$, $s = 2$)  
**Hạt giống cố định (Seed Value):** `20260317` (Lần chạy 06/20 từ `seedun.md`)  
**Thời gian thực thi:** `2026-09-13 11:46:03`  
**Môi trường tính toán:** `Hybrid Co-Processing [CPU: 12 Cores song song (GA/C++ igraph) + GPU: NVIDIA GeForce RTX 3050 Laptop GPU (PPO Tensor Cores)]`  

---

## 1. Bảng Thống Kê Hiệu Năng Chi Tiết Các Thuật Toán (Seed #6)

| Chiến lược / Thuật toán | Best Cover (Min) | Best Fitness | Mean $\pm$ Std | Median | Vi phạm ($diam > s$) | Độ đa dạng | Khả thi ($100\%$) | Thời gian (s) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **PPO-AOS** | **13** | **13.00** | 13.29 $\pm$ 0.77 | 13.0 | 0.00 | 0.841 |  Đạt chuẩn | 6.32s |
| MAB-AOS | 14 | 14.00 | 14.18 $\pm$ 0.50 | 14.0 | 0.00 | 0.890 |  Đạt chuẩn | 4.00s |
| Greedy-AOS | 14 | 14.00 | 14.07 $\pm$ 0.35 | 14.0 | 0.00 | 0.929 |  Đạt chuẩn | 3.46s |
| I-MSM | 14 | 14.00 | 14.44 $\pm$ 0.64 | 14.0 | 0.00 | 0.000 |  Đạt chuẩn | 0.63s |
| CCA | 14 | 14.00 | 14.45 $\pm$ 0.78 | 14.0 | 0.00 | 0.000 |  Đạt chuẩn | 0.14s |
| No-RL | 14 | 14.00 | 14.15 $\pm$ 0.51 | 14.0 | 0.00 | 0.885 |  Đạt chuẩn | 3.71s |
| Fixed | 13 | 13.00 | 13.20 $\pm$ 0.67 | 13.0 | 0.00 | 0.906 |  Đạt chuẩn | 3.09s |
| Random | 14 | 14.00 | 14.15 $\pm$ 0.51 | 14.0 | 0.00 | 0.885 |  Đạt chuẩn | 3.73s |

---

## 2. Cấu Trúc Nghiệm Tốt Nhất Trong Lần Chạy (Best Solution Clusters)
- **Thuật toán đạt Best:** `PPO-AOS` (Cover = `13` clubs, Fitness = `13.00`)
- **Kích thước các cụm ($s$-clubs):** `[6, 7, 3, 5, 10, 5, 2, 9, 5, 5, 2, 1, 2]`
- **Số thế hệ tiến hóa:** `117` generations

### Chi tiết các cụm $s$-club thành phần:
- **Club 10** (Size = 6 đỉnh): `[0, 10, 28, 30, 42, 47]`
- **Club 9** (Size = 7 đỉnh): `[1, 7, 19, 26, 27, 41, 54]`
- **Club 2** (Size = 3 đỉnh): `[2, 53, 61]`
- **Club 6** (Size = 5 đỉnh): `[3, 8, 15, 36, 59]`
- **Club 3** (Size = 10 đỉnh): `[4, 11, 18, 21, 23, 24, 29, 45, 51, 55]`
- **Club 5** (Size = 5 đỉnh): `[5, 9, 39, 48, 57]`
- **Club 11** (Size = 2 đỉnh): `[6, 56]`
- **Club 7** (Size = 9 đỉnh): `[12, 14, 16, 33, 34, 37, 40, 43, 50]`
- **Club 12** (Size = 5 đỉnh): `[13, 17, 22, 25, 31]`
- **Club 1** (Size = 5 đỉnh): `[20, 38, 44, 52, 58]`
- **Club 8** (Size = 2 đỉnh): `[32, 60]`
- **Club 4** (Size = 1 đỉnh): `[35]`
- **Club 13** (Size = 2 đỉnh): `[46, 49]`

---
*File được sinh tự động bởi hệ thống EVO-RL MSCC Research Framework.*
