# Báo Cáo Kết Quả Thực Nghiệm: Seed #15 (Seed = `31415926`)

**Tập dữ liệu đồ thị:** `dolphins` ($|V| = 62$, $|E| = 159$, Density = $0.0841$, $s = 2$)  
**Hạt giống cố định (Seed Value):** `31415926` (Lần chạy 15/20 từ `seedun.md`)  
**Thời gian thực thi:** `2026-09-13 11:46:28`  
**Môi trường tính toán:** `Hybrid Co-Processing [CPU: 12 Cores song song (GA/C++ igraph) + GPU: NVIDIA GeForce RTX 3050 Laptop GPU (PPO Tensor Cores)]`  

---

## 1. Bảng Thống Kê Hiệu Năng Chi Tiết Các Thuật Toán (Seed #15)

| Chiến lược / Thuật toán | Best Cover (Min) | Best Fitness | Mean $\pm$ Std | Median | Vi phạm ($diam > s$) | Độ đa dạng | Khả thi ($100\%$) | Thời gian (s) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **PPO-AOS** | **13** | **13.00** | 13.28 $\pm$ 0.72 | 13.0 | 0.00 | 0.866 |  Đạt chuẩn | 4.60s |
| MAB-AOS | 13 | 13.00 | 13.29 $\pm$ 0.68 | 13.0 | 0.00 | 0.917 |  Đạt chuẩn | 4.13s |
| Greedy-AOS | 14 | 14.00 | 14.06 $\pm$ 0.30 | 14.0 | 0.00 | 0.884 |  Đạt chuẩn | 3.34s |
| I-MSM | 14 | 14.00 | 14.65 $\pm$ 0.74 | 14.0 | 0.00 | 0.000 |  Đạt chuẩn | 0.78s |
| CCA | 14 | 14.00 | 14.11 $\pm$ 0.31 | 14.0 | 0.00 | 0.000 |  Đạt chuẩn | 0.11s |
| No-RL | 13 | 13.00 | 13.35 $\pm$ 0.72 | 13.0 | 0.00 | 0.812 |  Đạt chuẩn | 4.11s |
| Fixed | 13 | 13.00 | 13.18 $\pm$ 0.59 | 13.0 | 0.00 | 0.869 |  Đạt chuẩn | 2.93s |
| Random | 13 | 13.00 | 13.35 $\pm$ 0.72 | 13.0 | 0.00 | 0.812 |  Đạt chuẩn | 3.87s |

---

## 2. Cấu Trúc Nghiệm Tốt Nhất Trong Lần Chạy (Best Solution Clusters)
- **Thuật toán đạt Best:** `PPO-AOS` (Cover = `13` clubs, Fitness = `13.00`)
- **Kích thước các cụm ($s$-clubs):** `[6, 7, 3, 6, 5, 4, 5, 9, 5, 5, 2, 3, 2]`
- **Số thế hệ tiến hóa:** `121` generations

### Chi tiết các cụm $s$-club thành phần:
- **Club 7** (Size = 6 đỉnh): `[0, 10, 28, 30, 42, 47]`
- **Club 2** (Size = 7 đỉnh): `[1, 7, 19, 26, 27, 41, 54]`
- **Club 6** (Size = 3 đỉnh): `[2, 53, 61]`
- **Club 5** (Size = 6 đỉnh): `[3, 8, 15, 36, 45, 59]`
- **Club 4** (Size = 5 đỉnh): `[4, 11, 23, 51, 55]`
- **Club 8** (Size = 4 đỉnh): `[5, 9, 13, 56]`
- **Club 9** (Size = 5 đỉnh): `[6, 17, 22, 25, 31]`
- **Club 3** (Size = 9 đỉnh): `[12, 14, 16, 33, 34, 37, 40, 43, 50]`
- **Club 10** (Size = 5 đỉnh): `[18, 21, 24, 29, 35]`
- **Club 1** (Size = 5 đỉnh): `[20, 38, 44, 52, 58]`
- **Club 11** (Size = 2 đỉnh): `[32, 60]`
- **Club 12** (Size = 3 đỉnh): `[39, 48, 57]`
- **Club 13** (Size = 2 đỉnh): `[46, 49]`

---
*File được sinh tự động bởi hệ thống EVO-RL MSCC Research Framework.*
