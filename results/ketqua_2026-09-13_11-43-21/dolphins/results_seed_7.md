# Báo Cáo Kết Quả Thực Nghiệm: Seed #07 (Seed = `20260421`)

**Tập dữ liệu đồ thị:** `dolphins` ($|V| = 62$, $|E| = 159$, Density = $0.0841$, $s = 2$)  
**Hạt giống cố định (Seed Value):** `20260421` (Lần chạy 07/20 từ `seedun.md`)  
**Thời gian thực thi:** `2026-09-13 11:46:05`  
**Môi trường tính toán:** `Hybrid Co-Processing [CPU: 12 Cores song song (GA/C++ igraph) + GPU: NVIDIA GeForce RTX 3050 Laptop GPU (PPO Tensor Cores)]`  

---

## 1. Bảng Thống Kê Hiệu Năng Chi Tiết Các Thuật Toán (Seed #7)

| Chiến lược / Thuật toán | Best Cover (Min) | Best Fitness | Mean $\pm$ Std | Median | Vi phạm ($diam > s$) | Độ đa dạng | Khả thi ($100\%$) | Thời gian (s) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **PPO-AOS** | **13** | **13.00** | 13.38 $\pm$ 0.77 | 13.0 | 0.00 | 0.860 |  Đạt chuẩn | 6.83s |
| MAB-AOS | 14 | 14.00 | 14.10 $\pm$ 0.36 | 14.0 | 0.00 | 0.888 |  Đạt chuẩn | 3.68s |
| Greedy-AOS | 13 | 13.00 | 13.39 $\pm$ 0.77 | 13.0 | 0.00 | 0.911 |  Đạt chuẩn | 4.23s |
| I-MSM | 14 | 14.00 | 14.22 $\pm$ 0.63 | 14.0 | 0.00 | 0.000 |  Đạt chuẩn | 0.45s |
| CCA | 15 | 15.00 | 15.06 $\pm$ 0.24 | 15.0 | 0.00 | 0.000 |  Đạt chuẩn | 0.10s |
| No-RL | 13 | 13.00 | 13.34 $\pm$ 0.80 | 13.0 | 0.00 | 0.916 |  Đạt chuẩn | 3.84s |
| Fixed | 13 | 13.00 | 13.32 $\pm$ 0.59 | 13.0 | 0.00 | 0.911 |  Đạt chuẩn | 3.52s |
| Random | 13 | 13.00 | 13.34 $\pm$ 0.80 | 13.0 | 0.00 | 0.916 |  Đạt chuẩn | 3.85s |

---

## 2. Cấu Trúc Nghiệm Tốt Nhất Trong Lần Chạy (Best Solution Clusters)
- **Thuật toán đạt Best:** `PPO-AOS` (Cover = `13` clubs, Fitness = `13.00`)
- **Kích thước các cụm ($s$-clubs):** `[6, 6, 3, 5, 5, 5, 9, 4, 7, 4, 2, 4, 2]`
- **Số thế hệ tiến hóa:** `134` generations

### Chi tiết các cụm $s$-club thành phần:
- **Club 5** (Size = 6 đỉnh): `[0, 10, 28, 30, 42, 47]`
- **Club 6** (Size = 6 đỉnh): `[1, 7, 19, 26, 27, 54]`
- **Club 2** (Size = 3 đỉnh): `[2, 53, 61]`
- **Club 7** (Size = 5 đỉnh): `[3, 8, 15, 36, 59]`
- **Club 8** (Size = 5 đỉnh): `[4, 11, 23, 51, 55]`
- **Club 9** (Size = 5 đỉnh): `[5, 6, 9, 13, 56]`
- **Club 10** (Size = 9 đỉnh): `[12, 14, 16, 33, 34, 37, 40, 43, 50]`
- **Club 11** (Size = 4 đỉnh): `[17, 22, 25, 31]`
- **Club 1** (Size = 7 đỉnh): `[18, 21, 24, 29, 35, 45, 52]`
- **Club 3** (Size = 4 đỉnh): `[20, 38, 44, 58]`
- **Club 12** (Size = 2 đỉnh): `[32, 60]`
- **Club 4** (Size = 4 đỉnh): `[39, 41, 48, 57]`
- **Club 13** (Size = 2 đỉnh): `[46, 49]`

---
*File được sinh tự động bởi hệ thống EVO-RL MSCC Research Framework.*
