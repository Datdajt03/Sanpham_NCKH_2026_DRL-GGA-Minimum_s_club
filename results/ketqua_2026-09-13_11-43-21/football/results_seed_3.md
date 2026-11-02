# Báo Cáo Kết Quả Thực Nghiệm: Seed #03 (Seed = `23052026`)

**Tập dữ liệu đồ thị:** `football` ($|V| = 115$, $|E| = 613$, Density = $0.0935$, $s = 2$)  
**Hạt giống cố định (Seed Value):** `23052026` (Lần chạy 03/20 từ `seedun.md`)  
**Thời gian thực thi:** `2026-09-13 11:52:33`  
**Môi trường tính toán:** `Hybrid Co-Processing [CPU: 12 Cores song song (GA/C++ igraph) + GPU: NVIDIA GeForce RTX 3050 Laptop GPU (PPO Tensor Cores)]`  

---

## 1. Bảng Thống Kê Hiệu Năng Chi Tiết Các Thuật Toán (Seed #3)

| Chiến lược / Thuật toán | Best Cover (Min) | Best Fitness | Mean $\pm$ Std | Median | Vi phạm ($diam > s$) | Độ đa dạng | Khả thi ($100\%$) | Thời gian (s) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **PPO-AOS** | **10** | **10.00** | 10.29 $\pm$ 0.73 | 10.0 | 0.00 | 0.845 |  Đạt chuẩn | 8.25s |
| MAB-AOS | 10 | 10.00 | 10.45 $\pm$ 0.68 | 10.0 | 0.00 | 0.848 |  Đạt chuẩn | 6.48s |
| Greedy-AOS | 10 | 10.00 | 10.22 $\pm$ 0.63 | 10.0 | 0.00 | 0.749 |  Đạt chuẩn | 4.82s |
| I-MSM | 12 | 12.00 | 12.46 $\pm$ 0.57 | 12.0 | 0.00 | 0.000 |  Đạt chuẩn | 1.27s |
| CCA | 14 | 14.00 | 14.38 $\pm$ 0.49 | 14.0 | 0.00 | 0.000 |  Đạt chuẩn | 0.25s |
| No-RL | 10 | 10.00 | 10.31 $\pm$ 0.78 | 10.0 | 0.00 | 0.870 |  Đạt chuẩn | 5.39s |
| Fixed | 10 | 10.00 | 10.26 $\pm$ 0.66 | 10.0 | 0.00 | 0.878 |  Đạt chuẩn | 3.27s |
| Random | 10 | 10.00 | 10.31 $\pm$ 0.78 | 10.0 | 0.00 | 0.870 |  Đạt chuẩn | 5.36s |

---

## 2. Cấu Trúc Nghiệm Tốt Nhất Trong Lần Chạy (Best Solution Clusters)
- **Thuật toán đạt Best:** `PPO-AOS` (Cover = `10` clubs, Fitness = `10.00`)
- **Kích thước các cụm ($s$-clubs):** `[10, 12, 11, 12, 9, 14, 14, 13, 10, 10]`
- **Số thế hệ tiến hóa:** `126` generations

### Chi tiết các cụm $s$-club thành phần:
- **Club 7** (Size = 10 đỉnh): `[0, 8, 11, 23, 24, 28, 50, 69, 78, 90]`
- **Club 8** (Size = 12 đỉnh): `[1, 25, 33, 36, 37, 45, 80, 89, 95, 103, 105, 109]`
- **Club 4** (Size = 11 đỉnh): `[2, 6, 13, 15, 32, 39, 47, 60, 82, 100, 106]`
- **Club 6** (Size = 12 đỉnh): `[3, 5, 10, 40, 52, 72, 74, 81, 84, 98, 102, 107]`
- **Club 1** (Size = 9 đỉnh): `[4, 9, 16, 22, 41, 64, 93, 104, 108]`
- **Club 3** (Size = 14 đỉnh): `[7, 21, 46, 49, 53, 67, 68, 73, 77, 83, 88, 110, 111, 114]`
- **Club 5** (Size = 14 đỉnh): `[12, 14, 18, 26, 31, 34, 38, 42, 43, 54, 61, 71, 85, 99]`
- **Club 9** (Size = 13 đỉnh): `[17, 20, 27, 56, 59, 62, 63, 65, 70, 76, 87, 96, 113]`
- **Club 2** (Size = 10 đỉnh): `[19, 29, 30, 35, 51, 55, 58, 79, 94, 101]`
- **Club 10** (Size = 10 đỉnh): `[44, 48, 57, 66, 75, 86, 91, 92, 97, 112]`

---
*File được sinh tự động bởi hệ thống EVO-RL MSCC Research Framework.*
