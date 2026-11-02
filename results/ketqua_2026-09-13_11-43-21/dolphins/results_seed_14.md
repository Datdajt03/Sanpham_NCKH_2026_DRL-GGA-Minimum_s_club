# Báo Cáo Kết Quả Thực Nghiệm: Seed #14 (Seed = `24681357`)

**Tập dữ liệu đồ thị:** `dolphins` ($|V| = 62$, $|E| = 159$, Density = $0.0841$, $s = 2$)  
**Hạt giống cố định (Seed Value):** `24681357` (Lần chạy 14/20 từ `seedun.md`)  
**Thời gian thực thi:** `2026-09-13 11:46:29`  
**Môi trường tính toán:** `Hybrid Co-Processing [CPU: 12 Cores song song (GA/C++ igraph) + GPU: NVIDIA GeForce RTX 3050 Laptop GPU (PPO Tensor Cores)]`  

---

## 1. Bảng Thống Kê Hiệu Năng Chi Tiết Các Thuật Toán (Seed #14)

| Chiến lược / Thuật toán | Best Cover (Min) | Best Fitness | Mean $\pm$ Std | Median | Vi phạm ($diam > s$) | Độ đa dạng | Khả thi ($100\%$) | Thời gian (s) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **PPO-AOS** | **13** | **13.00** | 13.43 $\pm$ 0.84 | 13.0 | 0.00 | 0.840 |  Đạt chuẩn | 5.46s |
| MAB-AOS | 13 | 13.00 | 13.57 $\pm$ 0.60 | 14.0 | 0.00 | 0.886 |  Đạt chuẩn | 6.48s |
| Greedy-AOS | 13 | 13.00 | 13.35 $\pm$ 0.67 | 13.0 | 0.00 | 0.849 |  Đạt chuẩn | 4.34s |
| I-MSM | 15 | 15.00 | 15.00 $\pm$ 0.00 | 15.0 | 0.00 | 0.000 |  Đạt chuẩn | 0.41s |
| CCA | 14 | 14.00 | 14.43 $\pm$ 0.49 | 14.0 | 0.00 | 0.000 |  Đạt chuẩn | 0.17s |
| No-RL | 14 | 14.00 | 14.08 $\pm$ 0.38 | 14.0 | 0.00 | 0.845 |  Đạt chuẩn | 3.50s |
| Fixed | 13 | 13.00 | 13.28 $\pm$ 0.76 | 13.0 | 0.00 | 0.902 |  Đạt chuẩn | 3.28s |
| Random | 14 | 14.00 | 14.08 $\pm$ 0.38 | 14.0 | 0.00 | 0.845 |  Đạt chuẩn | 2.16s |

---

## 2. Cấu Trúc Nghiệm Tốt Nhất Trong Lần Chạy (Best Solution Clusters)
- **Thuật toán đạt Best:** `PPO-AOS` (Cover = `13` clubs, Fitness = `13.00`)
- **Kích thước các cụm ($s$-clubs):** `[6, 5, 4, 5, 10, 2, 6, 8, 6, 5, 2, 1, 2]`
- **Số thế hệ tiến hóa:** `135` generations

### Chi tiết các cụm $s$-club thành phần:
- **Club 3** (Size = 6 đỉnh): `[0, 10, 28, 30, 42, 47]`
- **Club 6** (Size = 5 đỉnh): `[1, 7, 19, 26, 27]`
- **Club 7** (Size = 4 đỉnh): `[2, 37, 53, 61]`
- **Club 8** (Size = 5 đỉnh): `[3, 8, 15, 36, 59]`
- **Club 9** (Size = 10 đỉnh): `[4, 11, 18, 21, 23, 24, 29, 45, 51, 55]`
- **Club 2** (Size = 2 đỉnh): `[5, 56]`
- **Club 5** (Size = 6 đỉnh): `[6, 9, 17, 22, 25, 31]`
- **Club 4** (Size = 8 đỉnh): `[12, 14, 16, 33, 34, 40, 43, 50]`
- **Club 10** (Size = 6 đỉnh): `[13, 39, 41, 48, 54, 57]`
- **Club 11** (Size = 5 đỉnh): `[20, 38, 44, 52, 58]`
- **Club 1** (Size = 2 đỉnh): `[32, 60]`
- **Club 12** (Size = 1 đỉnh): `[35]`
- **Club 13** (Size = 2 đỉnh): `[46, 49]`

---
*File được sinh tự động bởi hệ thống EVO-RL MSCC Research Framework.*
