# Báo Cáo Kết Quả Thực Nghiệm: Seed #16 (Seed = `27182818`)

**Tập dữ liệu đồ thị:** `dolphins` ($|V| = 62$, $|E| = 159$, Density = $0.0841$, $s = 2$)  
**Hạt giống cố định (Seed Value):** `27182818` (Lần chạy 16/20 từ `seedun.md`)  
**Thời gian thực thi:** `2026-09-13 11:46:29`  
**Môi trường tính toán:** `Hybrid Co-Processing [CPU: 12 Cores song song (GA/C++ igraph) + GPU: NVIDIA GeForce RTX 3050 Laptop GPU (PPO Tensor Cores)]`  

---

## 1. Bảng Thống Kê Hiệu Năng Chi Tiết Các Thuật Toán (Seed #16)

| Chiến lược / Thuật toán | Best Cover (Min) | Best Fitness | Mean $\pm$ Std | Median | Vi phạm ($diam > s$) | Độ đa dạng | Khả thi ($100\%$) | Thời gian (s) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **PPO-AOS** | **13** | **13.00** | 13.47 $\pm$ 0.85 | 13.0 | 0.00 | 0.877 |  Đạt chuẩn | 5.54s |
| MAB-AOS | 13 | 13.00 | 13.23 $\pm$ 0.52 | 13.0 | 0.00 | 0.855 |  Đạt chuẩn | 3.84s |
| Greedy-AOS | 14 | 14.00 | 14.15 $\pm$ 0.49 | 14.0 | 0.00 | 0.775 |  Đạt chuẩn | 3.55s |
| I-MSM | 14 | 14.00 | 14.21 $\pm$ 0.52 | 14.0 | 0.00 | 0.000 |  Đạt chuẩn | 0.50s |
| CCA | 14 | 14.00 | 14.16 $\pm$ 0.36 | 14.0 | 0.00 | 0.000 |  Đạt chuẩn | 0.12s |
| No-RL | 13 | 13.00 | 13.31 $\pm$ 0.65 | 13.0 | 0.00 | 0.731 |  Đạt chuẩn | 4.24s |
| Fixed | 13 | 13.00 | 13.21 $\pm$ 0.58 | 13.0 | 0.00 | 0.904 |  Đạt chuẩn | 3.40s |
| Random | 13 | 13.00 | 13.31 $\pm$ 0.65 | 13.0 | 0.00 | 0.731 |  Đạt chuẩn | 3.07s |

---

## 2. Cấu Trúc Nghiệm Tốt Nhất Trong Lần Chạy (Best Solution Clusters)
- **Thuật toán đạt Best:** `PPO-AOS` (Cover = `13` clubs, Fitness = `13.00`)
- **Kích thước các cụm ($s$-clubs):** `[6, 6, 3, 5, 8, 4, 5, 7, 4, 4, 6, 2, 2]`
- **Số thế hệ tiến hóa:** `143` generations

### Chi tiết các cụm $s$-club thành phần:
- **Club 7** (Size = 6 đỉnh): `[0, 10, 28, 30, 42, 47]`
- **Club 4** (Size = 6 đỉnh): `[1, 7, 19, 26, 27, 54]`
- **Club 6** (Size = 3 đỉnh): `[2, 53, 61]`
- **Club 3** (Size = 5 đỉnh): `[3, 8, 15, 36, 59]`
- **Club 9** (Size = 8 đỉnh): `[4, 11, 18, 23, 45, 50, 51, 55]`
- **Club 11** (Size = 4 đỉnh): `[5, 9, 13, 56]`
- **Club 10** (Size = 5 đỉnh): `[6, 39, 41, 48, 57]`
- **Club 5** (Size = 7 đỉnh): `[12, 14, 16, 33, 34, 37, 40]`
- **Club 12** (Size = 4 đỉnh): `[17, 22, 25, 31]`
- **Club 8** (Size = 4 đỉnh): `[20, 38, 44, 58]`
- **Club 1** (Size = 6 đỉnh): `[21, 24, 29, 35, 43, 52]`
- **Club 2** (Size = 2 đỉnh): `[32, 60]`
- **Club 13** (Size = 2 đỉnh): `[46, 49]`

---
*File được sinh tự động bởi hệ thống EVO-RL MSCC Research Framework.*
