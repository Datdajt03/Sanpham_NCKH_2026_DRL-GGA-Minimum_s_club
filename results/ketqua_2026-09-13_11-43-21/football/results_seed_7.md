# Báo Cáo Kết Quả Thực Nghiệm: Seed #07 (Seed = `20260421`)

**Tập dữ liệu đồ thị:** `football` ($|V| = 115$, $|E| = 613$, Density = $0.0935$, $s = 2$)  
**Hạt giống cố định (Seed Value):** `20260421` (Lần chạy 07/20 từ `seedun.md`)  
**Thời gian thực thi:** `2026-09-13 11:52:28`  
**Môi trường tính toán:** `Hybrid Co-Processing [CPU: 12 Cores song song (GA/C++ igraph) + GPU: NVIDIA GeForce RTX 3050 Laptop GPU (PPO Tensor Cores)]`  

---

## 1. Bảng Thống Kê Hiệu Năng Chi Tiết Các Thuật Toán (Seed #7)

| Chiến lược / Thuật toán | Best Cover (Min) | Best Fitness | Mean $\pm$ Std | Median | Vi phạm ($diam > s$) | Độ đa dạng | Khả thi ($100\%$) | Thời gian (s) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **PPO-AOS** | **10** | **10.00** | 10.21 $\pm$ 0.66 | 10.0 | 0.00 | 0.868 |  Đạt chuẩn | 8.05s |
| MAB-AOS | 10 | 10.00 | 10.27 $\pm$ 0.72 | 10.0 | 0.00 | 0.790 |  Đạt chuẩn | 4.83s |
| Greedy-AOS | 10 | 10.00 | 10.21 $\pm$ 0.75 | 10.0 | 0.00 | 0.851 |  Đạt chuẩn | 4.44s |
| I-MSM | 11 | 11.00 | 12.05 $\pm$ 1.72 | 11.0 | 0.00 | 0.000 |  Đạt chuẩn | 0.90s |
| CCA | 15 | 15.00 | 15.00 $\pm$ 0.00 | 15.0 | 0.00 | 0.000 |  Đạt chuẩn | 0.13s |
| No-RL | 10 | 10.00 | 10.20 $\pm$ 0.68 | 10.0 | 0.00 | 0.846 |  Đạt chuẩn | 4.38s |
| Fixed | 10 | 10.00 | 10.14 $\pm$ 0.57 | 10.0 | 0.00 | 0.836 |  Đạt chuẩn | 3.14s |
| Random | 10 | 10.00 | 10.20 $\pm$ 0.68 | 10.0 | 0.00 | 0.846 |  Đạt chuẩn | 4.24s |

---

## 2. Cấu Trúc Nghiệm Tốt Nhất Trong Lần Chạy (Best Solution Clusters)
- **Thuật toán đạt Best:** `PPO-AOS` (Cover = `10` clubs, Fitness = `10.00`)
- **Kích thước các cụm ($s$-clubs):** `[12, 10, 11, 12, 10, 15, 14, 10, 11, 10]`
- **Số thế hệ tiến hóa:** `116` generations

### Chi tiết các cụm $s$-club thành phần:
- **Club 5** (Size = 12 đỉnh): `[0, 4, 9, 11, 16, 23, 28, 41, 69, 90, 93, 104]`
- **Club 2** (Size = 10 đỉnh): `[1, 24, 25, 33, 37, 45, 89, 103, 105, 109]`
- **Club 4** (Size = 11 đỉnh): `[2, 6, 13, 15, 32, 39, 47, 60, 64, 100, 106]`
- **Club 7** (Size = 12 đỉnh): `[3, 5, 10, 40, 52, 72, 74, 81, 84, 98, 102, 107]`
- **Club 6** (Size = 10 đỉnh): `[7, 8, 21, 22, 68, 77, 78, 82, 108, 111]`
- **Club 8** (Size = 15 đỉnh): `[12, 14, 18, 26, 31, 34, 36, 38, 42, 43, 54, 61, 71, 85, 99]`
- **Club 3** (Size = 14 đỉnh): `[17, 20, 27, 56, 59, 62, 63, 65, 70, 76, 87, 95, 96, 113]`
- **Club 9** (Size = 10 đỉnh): `[19, 29, 30, 35, 50, 51, 55, 79, 94, 101]`
- **Club 1** (Size = 11 đỉnh): `[44, 48, 57, 66, 75, 80, 86, 91, 92, 97, 112]`
- **Club 10** (Size = 10 đỉnh): `[46, 49, 53, 58, 67, 73, 83, 88, 110, 114]`

---
*File được sinh tự động bởi hệ thống EVO-RL MSCC Research Framework.*
