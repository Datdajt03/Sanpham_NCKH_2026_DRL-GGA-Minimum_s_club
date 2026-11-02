# Báo Cáo Kết Quả Thực Nghiệm: Seed #14 (Seed = `24681357`)

**Tập dữ liệu đồ thị:** `adjnoun` ($|V| = 112$, $|E| = 425$, Density = $0.0684$, $s = 2$)  
**Hạt giống cố định (Seed Value):** `24681357` (Lần chạy 14/20 từ `seedun.md`)  
**Thời gian thực thi:** `2026-09-13 11:51:32`  
**Môi trường tính toán:** `Hybrid Co-Processing [CPU: 12 Cores song song (GA/C++ igraph) + GPU: NVIDIA GeForce RTX 3050 Laptop GPU (PPO Tensor Cores)]`  

---

## 1. Bảng Thống Kê Hiệu Năng Chi Tiết Các Thuật Toán (Seed #14)

| Chiến lược / Thuật toán | Best Cover (Min) | Best Fitness | Mean $\pm$ Std | Median | Vi phạm ($diam > s$) | Độ đa dạng | Khả thi ($100\%$) | Thời gian (s) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **PPO-AOS** | **19** | **19.00** | 19.78 $\pm$ 1.50 | 19.0 | 0.00 | 0.857 |  Đạt chuẩn | 11.71s |
| MAB-AOS | 18 | 18.00 | 19.12 $\pm$ 2.07 | 18.0 | 0.00 | 0.900 |  Đạt chuẩn | 10.16s |
| Greedy-AOS | 19 | 19.00 | 20.25 $\pm$ 1.88 | 19.0 | 0.00 | 0.768 |  Đạt chuẩn | 12.29s |
| I-MSM | 21 | 21.00 | 21.37 $\pm$ 0.93 | 21.0 | 0.00 | 0.000 |  Đạt chuẩn | 2.46s |
| CCA | 18 | 18.00 | 18.00 $\pm$ 0.00 | 18.0 | 0.00 | 0.000 |  Đạt chuẩn | 0.33s |
| No-RL | 19 | 19.00 | 19.68 $\pm$ 1.48 | 19.0 | 0.00 | 0.911 |  Đạt chuẩn | 8.66s |
| Fixed | 18 | 18.00 | 18.75 $\pm$ 1.66 | 18.0 | 0.00 | 0.915 |  Đạt chuẩn | 8.12s |
| Random | 19 | 19.00 | 19.68 $\pm$ 1.48 | 19.0 | 0.00 | 0.911 |  Đạt chuẩn | 7.47s |

---

## 2. Cấu Trúc Nghiệm Tốt Nhất Trong Lần Chạy (Best Solution Clusters)
- **Thuật toán đạt Best:** `MAB-AOS` (Cover = `18` clubs, Fitness = `18.00`)
- **Kích thước các cụm ($s$-clubs):** `[4, 11, 9, 3, 26, 11, 8, 4, 6, 6, 4, 3, 2, 3, 4, 1, 4, 3]`
- **Số thế hệ tiến hóa:** `154` generations

### Chi tiết các cụm $s$-club thành phần:
- **Club 11** (Size = 4 đỉnh): `[0, 1, 46, 91]`
- **Club 2** (Size = 11 đỉnh): `[2, 22, 34, 41, 45, 66, 73, 93, 97, 102, 111]`
- **Club 12** (Size = 9 đỉnh): `[3, 18, 21, 43, 44, 81, 98, 99, 100]`
- **Club 5** (Size = 3 đỉnh): `[4, 53, 89]`
- **Club 13** (Size = 26 đỉnh): `[5, 17, 24, 25, 26, 27, 28, 31, 32, 35, 36, 37, 52, 65, 67, 72, 77, 80, 82, 83, 84, 85, 86, 87, 103, 104]`
- **Club 7** (Size = 11 đỉnh): `[6, 7, 23, 30, 38, 49, 51, 57, 59, 101, 106]`
- **Club 14** (Size = 8 đỉnh): `[8, 9, 12, 39, 40, 60, 61, 62]`
- **Club 6** (Size = 4 đỉnh): `[10, 11, 63, 69]`
- **Club 3** (Size = 6 đỉnh): `[13, 14, 16, 68, 71, 105]`
- **Club 15** (Size = 6 đỉnh): `[15, 47, 48, 50, 76, 88]`
- **Club 16** (Size = 4 đỉnh): `[19, 20, 94, 108]`
- **Club 17** (Size = 3 đỉnh): `[29, 58, 74]`
- **Club 4** (Size = 2 đỉnh): `[33, 107]`
- **Club 18** (Size = 3 đỉnh): `[42, 56, 90]`
- **Club 1** (Size = 4 đỉnh): `[54, 55, 70, 75]`
- **Club 10** (Size = 1 đỉnh): `[64]`
- **Club 8** (Size = 4 đỉnh): `[78, 79, 109, 110]`
- **Club 9** (Size = 3 đỉnh): `[92, 95, 96]`

---
*File được sinh tự động bởi hệ thống EVO-RL MSCC Research Framework.*
