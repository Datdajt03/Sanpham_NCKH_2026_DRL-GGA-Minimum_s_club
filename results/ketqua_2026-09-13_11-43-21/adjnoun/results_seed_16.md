# Báo Cáo Kết Quả Thực Nghiệm: Seed #16 (Seed = `27182818`)

**Tập dữ liệu đồ thị:** `adjnoun` ($|V| = 112$, $|E| = 425$, Density = $0.0684$, $s = 2$)  
**Hạt giống cố định (Seed Value):** `27182818` (Lần chạy 16/20 từ `seedun.md`)  
**Thời gian thực thi:** `2026-09-13 11:51:37`  
**Môi trường tính toán:** `Hybrid Co-Processing [CPU: 12 Cores song song (GA/C++ igraph) + GPU: NVIDIA GeForce RTX 3050 Laptop GPU (PPO Tensor Cores)]`  

---

## 1. Bảng Thống Kê Hiệu Năng Chi Tiết Các Thuật Toán (Seed #16)

| Chiến lược / Thuật toán | Best Cover (Min) | Best Fitness | Mean $\pm$ Std | Median | Vi phạm ($diam > s$) | Độ đa dạng | Khả thi ($100\%$) | Thời gian (s) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **PPO-AOS** | **20** | **20.00** | 20.74 $\pm$ 1.50 | 20.0 | 0.00 | 0.894 |  Đạt chuẩn | 11.97s |
| MAB-AOS | 20 | 20.00 | 20.88 $\pm$ 1.41 | 20.0 | 0.00 | 0.910 |  Đạt chuẩn | 12.56s |
| Greedy-AOS | 20 | 20.00 | 20.50 $\pm$ 1.31 | 20.0 | 0.00 | 0.815 |  Đạt chuẩn | 9.46s |
| I-MSM | 21 | 21.00 | 21.33 $\pm$ 1.15 | 21.0 | 0.00 | 0.000 |  Đạt chuẩn | 2.39s |
| CCA | 19 | 19.00 | 19.06 $\pm$ 0.24 | 19.0 | 0.00 | 0.000 |  Đạt chuẩn | 0.36s |
| No-RL | 19 | 19.00 | 19.49 $\pm$ 1.25 | 19.0 | 0.00 | 0.913 |  Đạt chuẩn | 8.45s |
| Fixed | 18 | 18.00 | 18.96 $\pm$ 1.96 | 18.0 | 0.00 | 0.938 |  Đạt chuẩn | 10.30s |
| Random | 19 | 19.00 | 19.49 $\pm$ 1.25 | 19.0 | 0.00 | 0.913 |  Đạt chuẩn | 5.73s |

---

## 2. Cấu Trúc Nghiệm Tốt Nhất Trong Lần Chạy (Best Solution Clusters)
- **Thuật toán đạt Best:** `Fixed` (Cover = `18` clubs, Fitness = `18.00`)
- **Kích thước các cụm ($s$-clubs):** `[6, 9, 4, 40, 5, 7, 4, 6, 4, 3, 6, 3, 3, 2, 1, 5, 3, 1]`
- **Số thế hệ tiến hóa:** `139` generations

### Chi tiết các cụm $s$-club thành phần:
- **Club 7** (Size = 6 đỉnh): `[0, 1, 18, 45, 46, 91]`
- **Club 9** (Size = 9 đỉnh): `[2, 3, 22, 23, 41, 93, 97, 105, 111]`
- **Club 10** (Size = 4 đỉnh): `[4, 53, 89, 99]`
- **Club 11** (Size = 40 đỉnh): `[5, 12, 13, 15, 17, 21, 24, 25, 26, 27, 28, 31, 32, 34, 35, 36, 37, 38, 43, 44, 50, 52, 54, 65, 66, 67, 72, 77, 80, 82, 83, 84, 85, 86, 87, 88, 98, 102, 103, 104]`
- **Club 12** (Size = 5 đỉnh): `[6, 7, 55, 70, 75]`
- **Club 2** (Size = 7 đỉnh): `[8, 9, 39, 40, 60, 61, 62]`
- **Club 3** (Size = 4 đỉnh): `[10, 11, 63, 69]`
- **Club 6** (Size = 6 đỉnh): `[14, 16, 59, 68, 71, 73]`
- **Club 13** (Size = 4 đỉnh): `[19, 20, 94, 108]`
- **Club 14** (Size = 3 đỉnh): `[29, 58, 74]`
- **Club 1** (Size = 6 đỉnh): `[30, 49, 51, 57, 101, 106]`
- **Club 8** (Size = 3 đỉnh): `[33, 76, 107]`
- **Club 5** (Size = 3 đỉnh): `[42, 56, 90]`
- **Club 15** (Size = 2 đỉnh): `[47, 48]`
- **Club 4** (Size = 1 đỉnh): `[64]`
- **Club 16** (Size = 5 đỉnh): `[78, 79, 81, 109, 110]`
- **Club 17** (Size = 3 đỉnh): `[92, 95, 96]`
- **Club 18** (Size = 1 đỉnh): `[100]`

---
*File được sinh tự động bởi hệ thống EVO-RL MSCC Research Framework.*
