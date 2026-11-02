# Báo Cáo Kết Quả Thực Nghiệm: Seed #07 (Seed = `20260421`)

**Tập dữ liệu đồ thị:** `adjnoun` ($|V| = 112$, $|E| = 425$, Density = $0.0684$, $s = 2$)  
**Hạt giống cố định (Seed Value):** `20260421` (Lần chạy 07/20 từ `seedun.md`)  
**Thời gian thực thi:** `2026-09-13 11:50:37`  
**Môi trường tính toán:** `Hybrid Co-Processing [CPU: 12 Cores song song (GA/C++ igraph) + GPU: NVIDIA GeForce RTX 3050 Laptop GPU (PPO Tensor Cores)]`  

---

## 1. Bảng Thống Kê Hiệu Năng Chi Tiết Các Thuật Toán (Seed #7)

| Chiến lược / Thuật toán | Best Cover (Min) | Best Fitness | Mean $\pm$ Std | Median | Vi phạm ($diam > s$) | Độ đa dạng | Khả thi ($100\%$) | Thời gian (s) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **PPO-AOS** | **19** | **19.00** | 19.54 $\pm$ 1.41 | 19.0 | 0.00 | 0.872 |  Đạt chuẩn | 11.18s |
| MAB-AOS | 19 | 19.00 | 19.79 $\pm$ 1.69 | 19.0 | 0.00 | 0.888 |  Đạt chuẩn | 8.03s |
| Greedy-AOS | 18 | 18.00 | 18.79 $\pm$ 1.67 | 18.0 | 0.00 | 0.916 |  Đạt chuẩn | 9.65s |
| I-MSM | 19 | 19.00 | 19.83 $\pm$ 1.37 | 19.0 | 0.00 | 0.000 |  Đạt chuẩn | 3.20s |
| CCA | 18 | 18.00 | 18.00 $\pm$ 0.00 | 18.0 | 0.00 | 0.000 |  Đạt chuẩn | 0.32s |
| No-RL | 19 | 19.00 | 19.89 $\pm$ 1.59 | 19.0 | 0.00 | 0.869 |  Đạt chuẩn | 11.03s |
| Fixed | 19 | 19.00 | 19.74 $\pm$ 1.55 | 19.0 | 0.00 | 0.916 |  Đạt chuẩn | 9.53s |
| Random | 19 | 19.00 | 19.89 $\pm$ 1.59 | 19.0 | 0.00 | 0.869 |  Đạt chuẩn | 11.73s |

---

## 2. Cấu Trúc Nghiệm Tốt Nhất Trong Lần Chạy (Best Solution Clusters)
- **Thuật toán đạt Best:** `Greedy-AOS` (Cover = `18` clubs, Fitness = `18.00`)
- **Kích thước các cụm ($s$-clubs):** `[6, 8, 12, 3, 5, 25, 7, 3, 5, 6, 9, 9, 3, 3, 3, 1, 3, 1]`
- **Số thế hệ tiến hóa:** `142` generations

### Chi tiết các cụm $s$-club thành phần:
- **Club 1** (Size = 6 đỉnh): `[0, 1, 19, 45, 46, 91]`
- **Club 12** (Size = 8 đỉnh): `[2, 22, 41, 83, 93, 97, 105, 111]`
- **Club 5** (Size = 12 đỉnh): `[3, 18, 27, 43, 48, 63, 70, 80, 81, 98, 99, 100]`
- **Club 8** (Size = 3 đỉnh): `[4, 53, 89]`
- **Club 6** (Size = 5 đỉnh): `[5, 6, 32, 52, 55]`
- **Club 13** (Size = 25 đỉnh): `[7, 12, 13, 17, 21, 25, 26, 28, 31, 34, 35, 37, 38, 44, 65, 66, 67, 72, 77, 82, 84, 85, 86, 88, 102]`
- **Club 11** (Size = 7 đỉnh): `[8, 9, 39, 40, 60, 61, 62]`
- **Club 14** (Size = 3 đỉnh): `[10, 11, 69]`
- **Club 2** (Size = 5 đỉnh): `[14, 16, 68, 71, 73]`
- **Club 7** (Size = 6 đỉnh): `[15, 20, 78, 79, 109, 110]`
- **Club 4** (Size = 9 đỉnh): `[23, 30, 50, 51, 54, 57, 59, 101, 106]`
- **Club 10** (Size = 9 đỉnh): `[24, 36, 47, 49, 75, 76, 87, 103, 108]`
- **Club 15** (Size = 3 đỉnh): `[29, 58, 74]`
- **Club 16** (Size = 3 đỉnh): `[33, 104, 107]`
- **Club 17** (Size = 3 đỉnh): `[42, 56, 90]`
- **Club 9** (Size = 1 đỉnh): `[64]`
- **Club 3** (Size = 3 đỉnh): `[92, 95, 96]`
- **Club 18** (Size = 1 đỉnh): `[94]`

---
*File được sinh tự động bởi hệ thống EVO-RL MSCC Research Framework.*
