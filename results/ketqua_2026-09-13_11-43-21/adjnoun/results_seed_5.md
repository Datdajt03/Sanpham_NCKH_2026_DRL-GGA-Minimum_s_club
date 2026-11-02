# Báo Cáo Kết Quả Thực Nghiệm: Seed #05 (Seed = `13092026`)

**Tập dữ liệu đồ thị:** `adjnoun` ($|V| = 112$, $|E| = 425$, Density = $0.0684$, $s = 2$)  
**Hạt giống cố định (Seed Value):** `13092026` (Lần chạy 05/20 từ `seedun.md`)  
**Thời gian thực thi:** `2026-09-13 11:50:29`  
**Môi trường tính toán:** `Hybrid Co-Processing [CPU: 12 Cores song song (GA/C++ igraph) + GPU: NVIDIA GeForce RTX 3050 Laptop GPU (PPO Tensor Cores)]`  

---

## 1. Bảng Thống Kê Hiệu Năng Chi Tiết Các Thuật Toán (Seed #5)

| Chiến lược / Thuật toán | Best Cover (Min) | Best Fitness | Mean $\pm$ Std | Median | Vi phạm ($diam > s$) | Độ đa dạng | Khả thi ($100\%$) | Thời gian (s) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **PPO-AOS** | **20** | **20.00** | 20.48 $\pm$ 1.23 | 20.0 | 0.00 | 0.946 |  Đạt chuẩn | 11.35s |
| MAB-AOS | 19 | 19.00 | 19.86 $\pm$ 1.71 | 19.0 | 0.00 | 0.804 |  Đạt chuẩn | 10.02s |
| Greedy-AOS | 18 | 18.00 | 18.81 $\pm$ 1.80 | 18.0 | 0.00 | 0.854 |  Đạt chuẩn | 9.66s |
| I-MSM | 19 | 19.00 | 19.00 $\pm$ 0.00 | 19.0 | 0.00 | 0.000 |  Đạt chuẩn | 1.96s |
| CCA | 18 | 18.00 | 18.18 $\pm$ 0.71 | 18.0 | 0.00 | 0.000 |  Đạt chuẩn | 0.33s |
| No-RL | 19 | 19.00 | 19.59 $\pm$ 1.54 | 19.0 | 0.00 | 0.885 |  Đạt chuẩn | 7.78s |
| Fixed | 18 | 18.00 | 18.89 $\pm$ 2.05 | 18.0 | 0.00 | 0.933 |  Đạt chuẩn | 8.12s |
| Random | 19 | 19.00 | 19.59 $\pm$ 1.54 | 19.0 | 0.00 | 0.885 |  Đạt chuẩn | 7.69s |

---

## 2. Cấu Trúc Nghiệm Tốt Nhất Trong Lần Chạy (Best Solution Clusters)
- **Thuật toán đạt Best:** `Greedy-AOS` (Cover = `18` clubs, Fitness = `18.00`)
- **Kích thước các cụm ($s$-clubs):** `[14, 5, 4, 4, 34, 7, 4, 4, 4, 5, 8, 4, 2, 3, 4, 4, 1, 1]`
- **Số thế hệ tiến hóa:** `133` generations

### Chi tiết các cụm $s$-club thành phần:
- **Club 1** (Size = 14 đỉnh): `[0, 2, 3, 22, 23, 41, 66, 73, 83, 93, 97, 98, 105, 111]`
- **Club 8** (Size = 5 đỉnh): `[1, 19, 45, 46, 91]`
- **Club 9** (Size = 4 đỉnh): `[4, 53, 89, 99]`
- **Club 10** (Size = 4 đỉnh): `[5, 6, 32, 55]`
- **Club 3** (Size = 34 đỉnh): `[7, 12, 13, 15, 17, 21, 25, 26, 27, 28, 31, 34, 35, 37, 38, 44, 50, 52, 54, 65, 67, 70, 72, 77, 80, 82, 84, 85, 86, 87, 88, 102, 103, 104]`
- **Club 6** (Size = 7 đỉnh): `[8, 9, 39, 40, 60, 61, 62]`
- **Club 11** (Size = 4 đỉnh): `[10, 11, 63, 69]`
- **Club 12** (Size = 4 đỉnh): `[14, 16, 59, 71]`
- **Club 13** (Size = 4 đỉnh): `[18, 29, 58, 74]`
- **Club 5** (Size = 5 đỉnh): `[20, 78, 79, 109, 110]`
- **Club 7** (Size = 8 đỉnh): `[24, 36, 47, 49, 68, 75, 76, 108]`
- **Club 16** (Size = 4 đỉnh): `[30, 92, 95, 96]`
- **Club 4** (Size = 2 đỉnh): `[33, 107]`
- **Club 17** (Size = 3 đỉnh): `[42, 56, 90]`
- **Club 14** (Size = 4 đỉnh): `[43, 48, 81, 100]`
- **Club 18** (Size = 4 đỉnh): `[51, 57, 101, 106]`
- **Club 2** (Size = 1 đỉnh): `[64]`
- **Club 15** (Size = 1 đỉnh): `[94]`

---
*File được sinh tự động bởi hệ thống EVO-RL MSCC Research Framework.*
