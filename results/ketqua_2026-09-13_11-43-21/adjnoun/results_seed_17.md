# Báo Cáo Kết Quả Thực Nghiệm: Seed #17 (Seed = `52013140`)

**Tập dữ liệu đồ thị:** `adjnoun` ($|V| = 112$, $|E| = 425$, Density = $0.0684$, $s = 2$)  
**Hạt giống cố định (Seed Value):** `52013140` (Lần chạy 17/20 từ `seedun.md`)  
**Thời gian thực thi:** `2026-09-13 11:51:37`  
**Môi trường tính toán:** `Hybrid Co-Processing [CPU: 12 Cores song song (GA/C++ igraph) + GPU: NVIDIA GeForce RTX 3050 Laptop GPU (PPO Tensor Cores)]`  

---

## 1. Bảng Thống Kê Hiệu Năng Chi Tiết Các Thuật Toán (Seed #17)

| Chiến lược / Thuật toán | Best Cover (Min) | Best Fitness | Mean $\pm$ Std | Median | Vi phạm ($diam > s$) | Độ đa dạng | Khả thi ($100\%$) | Thời gian (s) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **PPO-AOS** | **19** | **19.00** | 19.64 $\pm$ 1.36 | 19.0 | 0.00 | 0.874 |  Đạt chuẩn | 11.03s |
| MAB-AOS | 19 | 19.00 | 19.88 $\pm$ 1.38 | 19.0 | 0.00 | 0.916 |  Đạt chuẩn | 13.40s |
| Greedy-AOS | 18 | 18.00 | 18.79 $\pm$ 1.42 | 18.0 | 0.00 | 0.803 |  Đạt chuẩn | 9.12s |
| I-MSM | 19 | 19.00 | 19.29 $\pm$ 1.18 | 19.0 | 0.00 | 0.000 |  Đạt chuẩn | 2.21s |
| CCA | 18 | 18.00 | 18.18 $\pm$ 0.71 | 18.0 | 0.00 | 0.000 |  Đạt chuẩn | 0.36s |
| No-RL | 19 | 19.00 | 19.78 $\pm$ 1.63 | 19.0 | 0.00 | 0.848 |  Đạt chuẩn | 9.35s |
| Fixed | 19 | 19.00 | 19.54 $\pm$ 1.22 | 19.0 | 0.00 | 0.880 |  Đạt chuẩn | 8.30s |
| Random | 19 | 19.00 | 19.78 $\pm$ 1.63 | 19.0 | 0.00 | 0.848 |  Đạt chuẩn | 6.35s |

---

## 2. Cấu Trúc Nghiệm Tốt Nhất Trong Lần Chạy (Best Solution Clusters)
- **Thuật toán đạt Best:** `Greedy-AOS` (Cover = `18` clubs, Fitness = `18.00`)
- **Kích thước các cụm ($s$-clubs):** `[5, 18, 4, 5, 22, 9, 4, 5, 5, 4, 3, 4, 7, 3, 5, 4, 1, 4]`
- **Số thế hệ tiến hóa:** `159` generations

### Chi tiết các cụm $s$-club thành phần:
- **Club 7** (Size = 5 đỉnh): `[0, 1, 19, 46, 91]`
- **Club 9** (Size = 18 đỉnh): `[2, 3, 22, 23, 24, 25, 31, 36, 41, 45, 50, 54, 73, 93, 97, 102, 104, 111]`
- **Club 6** (Size = 4 đỉnh): `[4, 53, 89, 99]`
- **Club 10** (Size = 5 đỉnh): `[5, 6, 32, 52, 100]`
- **Club 11** (Size = 22 đỉnh): `[7, 17, 21, 26, 27, 37, 38, 43, 44, 65, 66, 67, 72, 77, 80, 82, 84, 85, 86, 87, 98, 103]`
- **Club 12** (Size = 9 đỉnh): `[8, 9, 12, 39, 40, 59, 60, 61, 62]`
- **Club 13** (Size = 4 đỉnh): `[10, 11, 63, 69]`
- **Club 5** (Size = 5 đỉnh): `[13, 14, 16, 71, 105]`
- **Club 14** (Size = 5 đỉnh): `[15, 35, 47, 48, 88]`
- **Club 3** (Size = 4 đỉnh): `[18, 29, 58, 74]`
- **Club 4** (Size = 3 đỉnh): `[20, 94, 108]`
- **Club 1** (Size = 4 đỉnh): `[28, 33, 34, 107]`
- **Club 15** (Size = 7 đỉnh): `[30, 78, 79, 81, 83, 109, 110]`
- **Club 16** (Size = 3 đỉnh): `[42, 56, 90]`
- **Club 17** (Size = 5 đỉnh): `[49, 51, 57, 101, 106]`
- **Club 18** (Size = 4 đỉnh): `[55, 68, 70, 75]`
- **Club 2** (Size = 1 đỉnh): `[64]`
- **Club 8** (Size = 4 đỉnh): `[76, 92, 95, 96]`

---
*File được sinh tự động bởi hệ thống EVO-RL MSCC Research Framework.*
