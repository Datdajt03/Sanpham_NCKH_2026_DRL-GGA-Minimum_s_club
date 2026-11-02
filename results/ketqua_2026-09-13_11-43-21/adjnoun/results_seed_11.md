# Báo Cáo Kết Quả Thực Nghiệm: Seed #11 (Seed = `11223344`)

**Tập dữ liệu đồ thị:** `adjnoun` ($|V| = 112$, $|E| = 425$, Density = $0.0684$, $s = 2$)  
**Hạt giống cố định (Seed Value):** `11223344` (Lần chạy 11/20 từ `seedun.md`)  
**Thời gian thực thi:** `2026-09-13 11:51:29`  
**Môi trường tính toán:** `Hybrid Co-Processing [CPU: 12 Cores song song (GA/C++ igraph) + GPU: NVIDIA GeForce RTX 3050 Laptop GPU (PPO Tensor Cores)]`  

---

## 1. Bảng Thống Kê Hiệu Năng Chi Tiết Các Thuật Toán (Seed #11)

| Chiến lược / Thuật toán | Best Cover (Min) | Best Fitness | Mean $\pm$ Std | Median | Vi phạm ($diam > s$) | Độ đa dạng | Khả thi ($100\%$) | Thời gian (s) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **PPO-AOS** | **18** | **18.00** | 18.72 $\pm$ 1.19 | 18.0 | 0.00 | 0.817 |  Đạt chuẩn | 11.02s |
| MAB-AOS | 18 | 18.00 | 18.63 $\pm$ 1.52 | 18.0 | 0.00 | 0.943 |  Đạt chuẩn | 8.65s |
| Greedy-AOS | 18 | 18.00 | 18.64 $\pm$ 1.08 | 18.0 | 0.00 | 0.904 |  Đạt chuẩn | 12.50s |
| I-MSM | 19 | 19.00 | 19.57 $\pm$ 1.09 | 19.0 | 0.00 | 0.000 |  Đạt chuẩn | 2.73s |
| CCA | 18 | 18.00 | 18.18 $\pm$ 0.71 | 18.0 | 0.00 | 0.000 |  Đạt chuẩn | 0.32s |
| No-RL | 19 | 19.00 | 19.52 $\pm$ 1.13 | 19.0 | 0.00 | 0.924 |  Đạt chuẩn | 8.65s |
| Fixed | 18 | 18.00 | 18.65 $\pm$ 1.30 | 18.0 | 0.00 | 0.935 |  Đạt chuẩn | 7.74s |
| Random | 19 | 19.00 | 19.52 $\pm$ 1.13 | 19.0 | 0.00 | 0.924 |  Đạt chuẩn | 8.38s |

---

## 2. Cấu Trúc Nghiệm Tốt Nhất Trong Lần Chạy (Best Solution Clusters)
- **Thuật toán đạt Best:** `PPO-AOS` (Cover = `18` clubs, Fitness = `18.00`)
- **Kích thước các cụm ($s$-clubs):** `[17, 5, 3, 9, 9, 9, 5, 17, 3, 3, 3, 4, 3, 5, 4, 5, 3, 5]`
- **Số thế hệ tiến hóa:** `171` generations

### Chi tiết các cụm $s$-club thành phần:
- **Club 14** (Size = 17 đỉnh): `[0, 2, 3, 11, 22, 24, 36, 41, 45, 73, 83, 93, 97, 98, 104, 105, 111]`
- **Club 8** (Size = 5 đỉnh): `[1, 19, 46, 91, 102]`
- **Club 9** (Size = 3 đỉnh): `[4, 5, 89]`
- **Club 10** (Size = 9 đỉnh): `[6, 7, 38, 49, 51, 57, 67, 101, 106]`
- **Club 11** (Size = 9 đỉnh): `[8, 9, 25, 39, 40, 59, 60, 61, 62]`
- **Club 12** (Size = 9 đỉnh): `[10, 12, 18, 21, 44, 48, 50, 53, 54]`
- **Club 13** (Size = 5 đỉnh): `[13, 14, 16, 68, 71]`
- **Club 15** (Size = 17 đỉnh): `[15, 17, 26, 35, 37, 52, 65, 66, 72, 77, 80, 82, 84, 85, 86, 88, 103]`
- **Club 16** (Size = 3 đỉnh): `[20, 94, 108]`
- **Club 5** (Size = 3 đỉnh): `[23, 47, 69]`
- **Club 2** (Size = 3 đỉnh): `[27, 63, 64]`
- **Club 3** (Size = 4 đỉnh): `[28, 33, 34, 107]`
- **Club 1** (Size = 3 đỉnh): `[29, 58, 74]`
- **Club 7** (Size = 5 đỉnh): `[30, 76, 92, 95, 96]`
- **Club 17** (Size = 4 đỉnh): `[31, 43, 99, 100]`
- **Club 18** (Size = 5 đỉnh): `[32, 55, 70, 75, 87]`
- **Club 6** (Size = 3 đỉnh): `[42, 56, 90]`
- **Club 4** (Size = 5 đỉnh): `[78, 79, 81, 109, 110]`

---
*File được sinh tự động bởi hệ thống EVO-RL MSCC Research Framework.*
