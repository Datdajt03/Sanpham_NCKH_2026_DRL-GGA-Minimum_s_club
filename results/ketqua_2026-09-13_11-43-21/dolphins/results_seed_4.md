# Báo Cáo Kết Quả Thực Nghiệm: Seed #04 (Seed = `26062026`)

**Tập dữ liệu đồ thị:** `dolphins` ($|V| = 62$, $|E| = 159$, Density = $0.0841$, $s = 2$)  
**Hạt giống cố định (Seed Value):** `26062026` (Lần chạy 04/20 từ `seedun.md`)  
**Thời gian thực thi:** `2026-09-13 11:46:08`  
**Môi trường tính toán:** `Hybrid Co-Processing [CPU: 12 Cores song song (GA/C++ igraph) + GPU: NVIDIA GeForce RTX 3050 Laptop GPU (PPO Tensor Cores)]`  

---

## 1. Bảng Thống Kê Hiệu Năng Chi Tiết Các Thuật Toán (Seed #4)

| Chiến lược / Thuật toán | Best Cover (Min) | Best Fitness | Mean $\pm$ Std | Median | Vi phạm ($diam > s$) | Độ đa dạng | Khả thi ($100\%$) | Thời gian (s) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **PPO-AOS** | **14** | **14.00** | 14.06 $\pm$ 0.25 | 14.0 | 0.00 | 0.845 |  Đạt chuẩn | 6.08s |
| MAB-AOS | 14 | 14.00 | 14.16 $\pm$ 0.37 | 14.0 | 0.00 | 0.846 |  Đạt chuẩn | 4.02s |
| Greedy-AOS | 14 | 14.00 | 14.07 $\pm$ 0.26 | 14.0 | 0.00 | 0.896 |  Đạt chuẩn | 3.61s |
| I-MSM | 15 | 15.00 | 15.12 $\pm$ 0.47 | 15.0 | 0.00 | 0.000 |  Đạt chuẩn | 0.45s |
| CCA | 14 | 14.00 | 14.00 $\pm$ 0.00 | 14.0 | 0.00 | 0.000 |  Đạt chuẩn | 0.09s |
| No-RL | 13 | 13.00 | 13.55 $\pm$ 0.61 | 13.0 | 0.00 | 0.856 |  Đạt chuẩn | 6.22s |
| Fixed | 14 | 14.00 | 14.06 $\pm$ 0.25 | 14.0 | 0.00 | 0.912 |  Đạt chuẩn | 3.07s |
| Random | 13 | 13.00 | 13.55 $\pm$ 0.61 | 13.0 | 0.00 | 0.856 |  Đạt chuẩn | 6.34s |

---

## 2. Cấu Trúc Nghiệm Tốt Nhất Trong Lần Chạy (Best Solution Clusters)
- **Thuật toán đạt Best:** `No-RL` (Cover = `13` clubs, Fitness = `13.00`)
- **Kích thước các cụm ($s$-clubs):** `[6, 6, 3, 5, 5, 5, 9, 7, 5, 4, 2, 3, 2]`
- **Số thế hệ tiến hóa:** `200` generations

### Chi tiết các cụm $s$-club thành phần:
- **Club 2** (Size = 6 đỉnh): `[0, 7, 30, 40, 42, 47]`
- **Club 6** (Size = 6 đỉnh): `[1, 19, 26, 28, 41, 54]`
- **Club 4** (Size = 3 đỉnh): `[2, 53, 61]`
- **Club 5** (Size = 5 đỉnh): `[3, 8, 15, 36, 59]`
- **Club 7** (Size = 5 đỉnh): `[4, 11, 23, 51, 55]`
- **Club 8** (Size = 5 đỉnh): `[5, 6, 9, 13, 56]`
- **Club 1** (Size = 9 đỉnh): `[10, 18, 21, 24, 29, 35, 43, 45, 52]`
- **Club 3** (Size = 7 đỉnh): `[12, 14, 16, 33, 34, 37, 50]`
- **Club 9** (Size = 5 đỉnh): `[17, 22, 25, 27, 31]`
- **Club 11** (Size = 4 đỉnh): `[20, 38, 44, 58]`
- **Club 10** (Size = 2 đỉnh): `[32, 60]`
- **Club 12** (Size = 3 đỉnh): `[39, 48, 57]`
- **Club 13** (Size = 2 đỉnh): `[46, 49]`

---
*File được sinh tự động bởi hệ thống EVO-RL MSCC Research Framework.*
