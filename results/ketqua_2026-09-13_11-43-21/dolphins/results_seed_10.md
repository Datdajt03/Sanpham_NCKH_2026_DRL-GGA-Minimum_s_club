# Báo Cáo Kết Quả Thực Nghiệm: Seed #10 (Seed = `20260913`)

**Tập dữ liệu đồ thị:** `dolphins` ($|V| = 62$, $|E| = 159$, Density = $0.0841$, $s = 2$)  
**Hạt giống cố định (Seed Value):** `20260913` (Lần chạy 10/20 từ `seedun.md`)  
**Thời gian thực thi:** `2026-09-13 11:46:02`  
**Môi trường tính toán:** `Hybrid Co-Processing [CPU: 12 Cores song song (GA/C++ igraph) + GPU: NVIDIA GeForce RTX 3050 Laptop GPU (PPO Tensor Cores)]`  

---

## 1. Bảng Thống Kê Hiệu Năng Chi Tiết Các Thuật Toán (Seed #10)

| Chiến lược / Thuật toán | Best Cover (Min) | Best Fitness | Mean $\pm$ Std | Median | Vi phạm ($diam > s$) | Độ đa dạng | Khả thi ($100\%$) | Thời gian (s) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **PPO-AOS** | **13** | **13.00** | 13.27 $\pm$ 0.67 | 13.0 | 0.00 | 0.811 |  Đạt chuẩn | 6.44s |
| MAB-AOS | 13 | 13.00 | 13.25 $\pm$ 0.73 | 13.0 | 0.00 | 0.829 |  Đạt chuẩn | 3.71s |
| Greedy-AOS | 14 | 14.00 | 14.04 $\pm$ 0.28 | 14.0 | 0.00 | 0.867 |  Đạt chuẩn | 3.31s |
| I-MSM | 14 | 14.00 | 14.00 $\pm$ 0.00 | 14.0 | 0.00 | 0.000 |  Đạt chuẩn | 0.42s |
| CCA | 15 | 15.00 | 15.00 $\pm$ 0.00 | 15.0 | 0.00 | 0.000 |  Đạt chuẩn | 0.10s |
| No-RL | 14 | 14.00 | 14.04 $\pm$ 0.28 | 14.0 | 0.00 | 0.845 |  Đạt chuẩn | 3.26s |
| Fixed | 13 | 13.00 | 13.29 $\pm$ 0.66 | 13.0 | 0.00 | 0.886 |  Đạt chuẩn | 3.27s |
| Random | 14 | 14.00 | 14.04 $\pm$ 0.28 | 14.0 | 0.00 | 0.845 |  Đạt chuẩn | 3.23s |

---

## 2. Cấu Trúc Nghiệm Tốt Nhất Trong Lần Chạy (Best Solution Clusters)
- **Thuật toán đạt Best:** `PPO-AOS` (Cover = `13` clubs, Fitness = `13.00`)
- **Kích thước các cụm ($s$-clubs):** `[6, 7, 3, 5, 8, 7, 9, 4, 5, 3, 2, 2, 1]`
- **Số thế hệ tiến hóa:** `121` generations

### Chi tiết các cụm $s$-club thành phần:
- **Club 5** (Size = 6 đỉnh): `[0, 10, 28, 30, 42, 47]`
- **Club 1** (Size = 7 đỉnh): `[1, 7, 19, 26, 27, 41, 54]`
- **Club 7** (Size = 3 đỉnh): `[2, 53, 61]`
- **Club 8** (Size = 5 đỉnh): `[3, 8, 15, 36, 59]`
- **Club 9** (Size = 8 đỉnh): `[4, 11, 18, 23, 24, 45, 51, 55]`
- **Club 10** (Size = 7 đỉnh): `[5, 6, 9, 13, 39, 48, 57]`
- **Club 11** (Size = 9 đỉnh): `[12, 14, 16, 33, 34, 37, 40, 43, 50]`
- **Club 6** (Size = 4 đỉnh): `[17, 22, 25, 31]`
- **Club 3** (Size = 5 đỉnh): `[20, 38, 44, 52, 58]`
- **Club 4** (Size = 3 đỉnh): `[21, 29, 35]`
- **Club 2** (Size = 2 đỉnh): `[32, 60]`
- **Club 12** (Size = 2 đỉnh): `[46, 49]`
- **Club 13** (Size = 1 đỉnh): `[56]`

---
*File được sinh tự động bởi hệ thống EVO-RL MSCC Research Framework.*
