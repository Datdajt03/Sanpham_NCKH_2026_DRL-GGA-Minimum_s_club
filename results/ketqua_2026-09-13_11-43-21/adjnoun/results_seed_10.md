# Báo Cáo Kết Quả Thực Nghiệm: Seed #10 (Seed = `20260913`)

**Tập dữ liệu đồ thị:** `adjnoun` ($|V| = 112$, $|E| = 425$, Density = $0.0684$, $s = 2$)  
**Hạt giống cố định (Seed Value):** `20260913` (Lần chạy 10/20 từ `seedun.md`)  
**Thời gian thực thi:** `2026-09-13 11:50:36`  
**Môi trường tính toán:** `Hybrid Co-Processing [CPU: 12 Cores song song (GA/C++ igraph) + GPU: NVIDIA GeForce RTX 3050 Laptop GPU (PPO Tensor Cores)]`  

---

## 1. Bảng Thống Kê Hiệu Năng Chi Tiết Các Thuật Toán (Seed #10)

| Chiến lược / Thuật toán | Best Cover (Min) | Best Fitness | Mean $\pm$ Std | Median | Vi phạm ($diam > s$) | Độ đa dạng | Khả thi ($100\%$) | Thời gian (s) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **PPO-AOS** | **18** | **18.00** | 18.90 $\pm$ 1.55 | 18.0 | 0.00 | 0.920 |  Đạt chuẩn | 14.72s |
| MAB-AOS | 18 | 18.00 | 19.11 $\pm$ 1.64 | 18.0 | 0.00 | 0.859 |  Đạt chuẩn | 10.95s |
| Greedy-AOS | 18 | 18.00 | 18.97 $\pm$ 1.77 | 18.0 | 0.00 | 0.883 |  Đạt chuẩn | 9.95s |
| I-MSM | 19 | 19.00 | 19.65 $\pm$ 1.54 | 19.0 | 0.00 | 0.000 |  Đạt chuẩn | 3.27s |
| CCA | 18 | 18.00 | 18.90 $\pm$ 0.98 | 18.0 | 0.00 | 0.000 |  Đạt chuẩn | 0.61s |
| No-RL | 20 | 20.00 | 20.41 $\pm$ 0.93 | 20.0 | 0.00 | 0.846 |  Đạt chuẩn | 7.91s |
| Fixed | 18 | 18.00 | 18.91 $\pm$ 1.77 | 18.0 | 0.00 | 0.887 |  Đạt chuẩn | 7.97s |
| Random | 20 | 20.00 | 20.41 $\pm$ 0.93 | 20.0 | 0.00 | 0.846 |  Đạt chuẩn | 8.31s |

---

## 2. Cấu Trúc Nghiệm Tốt Nhất Trong Lần Chạy (Best Solution Clusters)
- **Thuật toán đạt Best:** `PPO-AOS` (Cover = `18` clubs, Fitness = `18.00`)
- **Kích thước các cụm ($s$-clubs):** `[12, 5, 4, 37, 5, 7, 4, 6, 3, 3, 4, 3, 3, 5, 1, 5, 1, 4]`
- **Số thế hệ tiến hóa:** `152` generations

### Chi tiết các cụm $s$-club thành phần:
- **Club 10** (Size = 12 đỉnh): `[0, 2, 3, 22, 23, 36, 41, 45, 93, 97, 105, 111]`
- **Club 11** (Size = 5 đỉnh): `[1, 18, 19, 46, 91]`
- **Club 9** (Size = 4 đỉnh): `[4, 53, 89, 99]`
- **Club 6** (Size = 37 đỉnh): `[5, 12, 13, 15, 17, 21, 24, 25, 26, 27, 28, 31, 32, 34, 35, 37, 38, 44, 50, 52, 54, 65, 66, 67, 72, 77, 80, 82, 83, 84, 85, 86, 87, 88, 102, 103, 104]`
- **Club 7** (Size = 5 đỉnh): `[6, 7, 55, 70, 75]`
- **Club 12** (Size = 7 đỉnh): `[8, 9, 39, 40, 60, 61, 62]`
- **Club 13** (Size = 4 đỉnh): `[10, 11, 63, 69]`
- **Club 1** (Size = 6 đỉnh): `[14, 16, 59, 68, 71, 73]`
- **Club 14** (Size = 3 đỉnh): `[20, 94, 108]`
- **Club 5** (Size = 3 đỉnh): `[29, 58, 74]`
- **Club 15** (Size = 4 đỉnh): `[30, 92, 95, 96]`
- **Club 4** (Size = 3 đỉnh): `[33, 76, 107]`
- **Club 16** (Size = 3 đỉnh): `[42, 56, 90]`
- **Club 17** (Size = 5 đỉnh): `[43, 48, 81, 98, 100]`
- **Club 18** (Size = 1 đỉnh): `[47]`
- **Club 3** (Size = 5 đỉnh): `[49, 51, 57, 101, 106]`
- **Club 8** (Size = 1 đỉnh): `[64]`
- **Club 2** (Size = 4 đỉnh): `[78, 79, 109, 110]`

---
*File được sinh tự động bởi hệ thống EVO-RL MSCC Research Framework.*
