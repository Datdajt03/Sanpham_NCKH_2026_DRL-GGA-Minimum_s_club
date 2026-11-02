# Báo Cáo Kết Quả Thực Nghiệm: Seed #01 (Seed = `17032026`)

**Tập dữ liệu đồ thị:** `dolphins` ($|V| = 62$, $|E| = 159$, Density = $0.0841$, $s = 2$)  
**Hạt giống cố định (Seed Value):** `17032026` (Lần chạy 01/20 từ `seedun.md`)  
**Thời gian thực thi:** `2026-09-13 11:46:06`  
**Môi trường tính toán:** `Hybrid Co-Processing [CPU: 12 Cores song song (GA/C++ igraph) + GPU: NVIDIA GeForce RTX 3050 Laptop GPU (PPO Tensor Cores)]`  

---

## 1. Bảng Thống Kê Hiệu Năng Chi Tiết Các Thuật Toán (Seed #1)

| Chiến lược / Thuật toán | Best Cover (Min) | Best Fitness | Mean $\pm$ Std | Median | Vi phạm ($diam > s$) | Độ đa dạng | Khả thi ($100\%$) | Thời gian (s) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **PPO-AOS** | **13** | **13.00** | 13.49 $\pm$ 0.53 | 13.0 | 0.00 | 0.807 |  Đạt chuẩn | 9.00s |
| MAB-AOS | 13 | 13.00 | 13.21 $\pm$ 0.53 | 13.0 | 0.00 | 0.850 |  Đạt chuẩn | 3.77s |
| Greedy-AOS | 13 | 13.00 | 13.20 $\pm$ 0.53 | 13.0 | 0.00 | 0.851 |  Đạt chuẩn | 3.65s |
| I-MSM | 15 | 15.00 | 15.11 $\pm$ 0.31 | 15.0 | 0.00 | 0.000 |  Đạt chuẩn | 0.45s |
| CCA | 14 | 14.00 | 14.42 $\pm$ 1.04 | 14.0 | 0.00 | 0.000 |  Đạt chuẩn | 0.12s |
| No-RL | 13 | 13.00 | 13.25 $\pm$ 0.59 | 13.0 | 0.00 | 0.873 |  Đạt chuẩn | 3.76s |
| Fixed | 13 | 13.00 | 13.25 $\pm$ 0.59 | 13.0 | 0.00 | 0.903 |  Đạt chuẩn | 3.32s |
| Random | 13 | 13.00 | 13.25 $\pm$ 0.59 | 13.0 | 0.00 | 0.873 |  Đạt chuẩn | 3.83s |

---

## 2. Cấu Trúc Nghiệm Tốt Nhất Trong Lần Chạy (Best Solution Clusters)
- **Thuật toán đạt Best:** `PPO-AOS` (Cover = `13` clubs, Fitness = `13.00`)
- **Kích thước các cụm ($s$-clubs):** `[6, 5, 4, 5, 9, 5, 4, 6, 4, 4, 2, 3, 5]`
- **Số thế hệ tiến hóa:** `191` generations

### Chi tiết các cụm $s$-club thành phần:
- **Club 3** (Size = 6 đỉnh): `[0, 10, 28, 30, 42, 47]`
- **Club 12** (Size = 5 đỉnh): `[1, 7, 19, 26, 27]`
- **Club 4** (Size = 4 đỉnh): `[2, 37, 53, 61]`
- **Club 13** (Size = 5 đỉnh): `[3, 8, 15, 36, 59]`
- **Club 5** (Size = 9 đỉnh): `[4, 11, 18, 21, 23, 45, 50, 51, 55]`
- **Club 6** (Size = 5 đỉnh): `[5, 6, 9, 13, 56]`
- **Club 7** (Size = 4 đỉnh): `[12, 33, 40, 43]`
- **Club 8** (Size = 6 đỉnh): `[14, 16, 20, 38, 44, 58]`
- **Club 9** (Size = 4 đỉnh): `[17, 22, 25, 31]`
- **Club 10** (Size = 4 đỉnh): `[24, 29, 35, 52]`
- **Club 11** (Size = 2 đỉnh): `[32, 60]`
- **Club 2** (Size = 3 đỉnh): `[34, 46, 49]`
- **Club 1** (Size = 5 đỉnh): `[39, 41, 48, 54, 57]`

---
*File được sinh tự động bởi hệ thống EVO-RL MSCC Research Framework.*
