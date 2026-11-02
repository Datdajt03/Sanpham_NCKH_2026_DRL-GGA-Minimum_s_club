# Báo Cáo Kết Quả Thực Nghiệm: Seed #05 (Seed = `13092026`)

**Tập dữ liệu đồ thị:** `dolphins` ($|V| = 62$, $|E| = 159$, Density = $0.0841$, $s = 2$)  
**Hạt giống cố định (Seed Value):** `13092026` (Lần chạy 05/20 từ `seedun.md`)  
**Thời gian thực thi:** `2026-09-13 11:46:03`  
**Môi trường tính toán:** `Hybrid Co-Processing [CPU: 12 Cores song song (GA/C++ igraph) + GPU: NVIDIA GeForce RTX 3050 Laptop GPU (PPO Tensor Cores)]`  

---

## 1. Bảng Thống Kê Hiệu Năng Chi Tiết Các Thuật Toán (Seed #5)

| Chiến lược / Thuật toán | Best Cover (Min) | Best Fitness | Mean $\pm$ Std | Median | Vi phạm ($diam > s$) | Độ đa dạng | Khả thi ($100\%$) | Thời gian (s) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **PPO-AOS** | **13** | **13.00** | 13.31 $\pm$ 0.69 | 13.0 | 0.00 | 0.886 |  Đạt chuẩn | 6.40s |
| MAB-AOS | 14 | 14.00 | 14.15 $\pm$ 0.36 | 14.0 | 0.00 | 0.816 |  Đạt chuẩn | 3.95s |
| Greedy-AOS | 14 | 14.00 | 14.07 $\pm$ 0.26 | 14.0 | 0.00 | 0.875 |  Đạt chuẩn | 3.52s |
| I-MSM | 15 | 15.00 | 15.16 $\pm$ 0.36 | 15.0 | 0.00 | 0.000 |  Đạt chuẩn | 0.52s |
| CCA | 14 | 14.00 | 14.06 $\pm$ 0.24 | 14.0 | 0.00 | 0.000 |  Đạt chuẩn | 0.10s |
| No-RL | 14 | 14.00 | 14.05 $\pm$ 0.21 | 14.0 | 0.00 | 0.867 |  Đạt chuẩn | 3.37s |
| Fixed | 13 | 13.00 | 13.14 $\pm$ 0.37 | 13.0 | 0.00 | 0.913 |  Đạt chuẩn | 3.08s |
| Random | 14 | 14.00 | 14.05 $\pm$ 0.21 | 14.0 | 0.00 | 0.867 |  Đạt chuẩn | 3.41s |

---

## 2. Cấu Trúc Nghiệm Tốt Nhất Trong Lần Chạy (Best Solution Clusters)
- **Thuật toán đạt Best:** `PPO-AOS` (Cover = `13` clubs, Fitness = `13.00`)
- **Kích thước các cụm ($s$-clubs):** `[6, 7, 4, 5, 6, 3, 5, 7, 4, 5, 5, 2, 3]`
- **Số thế hệ tiến hóa:** `123` generations

### Chi tiết các cụm $s$-club thành phần:
- **Club 6** (Size = 6 đỉnh): `[0, 10, 28, 30, 42, 47]`
- **Club 4** (Size = 7 đỉnh): `[1, 7, 19, 26, 27, 41, 54]`
- **Club 1** (Size = 4 đỉnh): `[2, 37, 53, 61]`
- **Club 8** (Size = 5 đỉnh): `[3, 8, 15, 36, 59]`
- **Club 13** (Size = 6 đỉnh): `[4, 11, 18, 23, 51, 55]`
- **Club 9** (Size = 3 đỉnh): `[5, 6, 56]`
- **Club 7** (Size = 5 đỉnh): `[9, 13, 39, 48, 57]`
- **Club 10** (Size = 7 đỉnh): `[12, 14, 16, 33, 40, 43, 50]`
- **Club 2** (Size = 4 đỉnh): `[17, 22, 25, 31]`
- **Club 5** (Size = 5 đỉnh): `[20, 38, 44, 52, 58]`
- **Club 11** (Size = 5 đỉnh): `[21, 24, 29, 35, 45]`
- **Club 3** (Size = 2 đỉnh): `[32, 60]`
- **Club 12** (Size = 3 đỉnh): `[34, 46, 49]`

---
*File được sinh tự động bởi hệ thống EVO-RL MSCC Research Framework.*
