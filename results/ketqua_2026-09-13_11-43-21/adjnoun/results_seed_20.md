# Báo Cáo Kết Quả Thực Nghiệm: Seed #20 (Seed = `86088608`)

**Tập dữ liệu đồ thị:** `adjnoun` ($|V| = 112$, $|E| = 425$, Density = $0.0684$, $s = 2$)  
**Hạt giống cố định (Seed Value):** `86088608` (Lần chạy 20/20 từ `seedun.md`)  
**Thời gian thực thi:** `2026-09-13 11:51:41`  
**Môi trường tính toán:** `Hybrid Co-Processing [CPU: 12 Cores song song (GA/C++ igraph) + GPU: NVIDIA GeForce RTX 3050 Laptop GPU (PPO Tensor Cores)]`  

---

## 1. Bảng Thống Kê Hiệu Năng Chi Tiết Các Thuật Toán (Seed #20)

| Chiến lược / Thuật toán | Best Cover (Min) | Best Fitness | Mean $\pm$ Std | Median | Vi phạm ($diam > s$) | Độ đa dạng | Khả thi ($100\%$) | Thời gian (s) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **PPO-AOS** | **19** | **19.00** | 19.78 $\pm$ 1.64 | 19.0 | 0.00 | 0.909 |  Đạt chuẩn | 8.99s |
| MAB-AOS | 19 | 19.00 | 20.04 $\pm$ 1.68 | 19.0 | 0.00 | 0.886 |  Đạt chuẩn | 10.24s |
| Greedy-AOS | 18 | 18.00 | 18.98 $\pm$ 2.03 | 18.0 | 0.00 | 0.919 |  Đạt chuẩn | 11.14s |
| I-MSM | 20 | 20.00 | 20.50 $\pm$ 1.64 | 20.0 | 0.00 | 0.000 |  Đạt chuẩn | 2.24s |
| CCA | 18 | 18.00 | 18.00 $\pm$ 0.00 | 18.0 | 0.00 | 0.000 |  Đạt chuẩn | 0.31s |
| No-RL | 19 | 19.00 | 20.21 $\pm$ 1.89 | 19.0 | 0.00 | 0.906 |  Đạt chuẩn | 9.67s |
| Fixed | 18 | 18.00 | 18.84 $\pm$ 1.79 | 18.0 | 0.00 | 0.907 |  Đạt chuẩn | 6.69s |
| Random | 19 | 19.00 | 20.21 $\pm$ 1.89 | 19.0 | 0.00 | 0.906 |  Đạt chuẩn | 5.22s |

---

## 2. Cấu Trúc Nghiệm Tốt Nhất Trong Lần Chạy (Best Solution Clusters)
- **Thuật toán đạt Best:** `Greedy-AOS` (Cover = `18` clubs, Fitness = `18.00`)
- **Kích thước các cụm ($s$-clubs):** `[6, 10, 11, 3, 32, 7, 7, 4, 5, 2, 8, 3, 2, 3, 1, 1, 4, 3]`
- **Số thế hệ tiến hóa:** `135` generations

### Chi tiết các cụm $s$-club thành phần:
- **Club 5** (Size = 6 đỉnh): `[0, 1, 19, 45, 46, 91]`
- **Club 8** (Size = 10 đỉnh): `[2, 22, 23, 34, 66, 93, 97, 102, 105, 111]`
- **Club 9** (Size = 11 đỉnh): `[3, 12, 18, 41, 43, 48, 59, 81, 98, 99, 100]`
- **Club 10** (Size = 3 đỉnh): `[4, 53, 89]`
- **Club 11** (Size = 32 đỉnh): `[5, 7, 13, 15, 17, 21, 26, 27, 28, 31, 32, 35, 36, 37, 38, 44, 50, 52, 54, 65, 67, 70, 72, 77, 80, 82, 83, 84, 85, 86, 87, 88]`
- **Club 12** (Size = 7 đỉnh): `[6, 25, 30, 51, 57, 101, 106]`
- **Club 13** (Size = 7 đỉnh): `[8, 9, 39, 40, 60, 61, 62]`
- **Club 4** (Size = 4 đỉnh): `[10, 11, 63, 69]`
- **Club 14** (Size = 5 đỉnh): `[14, 16, 68, 71, 73]`
- **Club 15** (Size = 2 đỉnh): `[20, 94]`
- **Club 7** (Size = 8 đỉnh): `[24, 47, 49, 75, 76, 103, 104, 108]`
- **Club 16** (Size = 3 đỉnh): `[29, 58, 74]`
- **Club 17** (Size = 2 đỉnh): `[33, 107]`
- **Club 2** (Size = 3 đỉnh): `[42, 56, 90]`
- **Club 1** (Size = 1 đỉnh): `[55]`
- **Club 18** (Size = 1 đỉnh): `[64]`
- **Club 6** (Size = 4 đỉnh): `[78, 79, 109, 110]`
- **Club 3** (Size = 3 đỉnh): `[92, 95, 96]`

---
*File được sinh tự động bởi hệ thống EVO-RL MSCC Research Framework.*
