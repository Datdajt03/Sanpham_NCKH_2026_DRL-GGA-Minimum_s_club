# Báo Cáo Kết Quả Thực Nghiệm: Seed #08 (Seed = `20260523`)

**Tập dữ liệu đồ thị:** `polbooks` ($|V| = 105$, $|E| = 441$, Density = $0.0808$, $s = 2$)  
**Hạt giống cố định (Seed Value):** `20260523` (Lần chạy 08/20 từ `seedun.md`)  
**Thời gian thực thi:** `2026-09-13 11:48:33`  
**Môi trường tính toán:** `Hybrid Co-Processing [CPU: 12 Cores song song (GA/C++ igraph) + GPU: NVIDIA GeForce RTX 3050 Laptop GPU (PPO Tensor Cores)]`  

---

## 1. Bảng Thống Kê Hiệu Năng Chi Tiết Các Thuật Toán (Seed #8)

| Chiến lược / Thuật toán | Best Cover (Min) | Best Fitness | Mean $\pm$ Std | Median | Vi phạm ($diam > s$) | Độ đa dạng | Khả thi ($100\%$) | Thời gian (s) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **PPO-AOS** | **13** | **13.00** | 13.24 $\pm$ 0.54 | 13.0 | 0.00 | 0.860 |  Đạt chuẩn | 8.19s |
| MAB-AOS | 14 | 14.00 | 14.02 $\pm$ 0.14 | 14.0 | 0.00 | 0.828 |  Đạt chuẩn | 4.60s |
| Greedy-AOS | 13 | 13.00 | 13.27 $\pm$ 0.54 | 13.0 | 0.00 | 0.864 |  Đạt chuẩn | 5.88s |
| I-MSM | 13 | 13.00 | 13.67 $\pm$ 0.91 | 13.0 | 0.00 | 0.000 |  Đạt chuẩn | 2.03s |
| CCA | 14 | 14.00 | 14.35 $\pm$ 0.56 | 14.0 | 0.00 | 0.000 |  Đạt chuẩn | 0.24s |
| No-RL | 14 | 14.00 | 14.05 $\pm$ 0.21 | 14.0 | 0.00 | 0.877 |  Đạt chuẩn | 4.58s |
| Fixed | 13 | 13.00 | 13.27 $\pm$ 0.60 | 13.0 | 0.00 | 0.900 |  Đạt chuẩn | 4.39s |
| Random | 14 | 14.00 | 14.05 $\pm$ 0.21 | 14.0 | 0.00 | 0.877 |  Đạt chuẩn | 4.68s |

---

## 2. Cấu Trúc Nghiệm Tốt Nhất Trong Lần Chạy (Best Solution Clusters)
- **Thuật toán đạt Best:** `PPO-AOS` (Cover = `13` clubs, Fitness = `13.00`)
- **Kích thước các cụm ($s$-clubs):** `[8, 7, 23, 4, 5, 11, 13, 6, 8, 6, 5, 3, 6]`
- **Số thế hệ tiến hóa:** `123` generations

### Chi tiết các cụm $s$-club thành phần:
- **Club 2** (Size = 8 đỉnh): `[0, 1, 2, 4, 5, 6, 7, 29]`
- **Club 9** (Size = 7 đỉnh): `[3, 15, 16, 18, 22, 25, 26]`
- **Club 8** (Size = 23 đỉnh): `[8, 9, 10, 11, 12, 13, 14, 17, 21, 23, 24, 27, 32, 33, 37, 39, 40, 41, 42, 45, 46, 47, 54]`
- **Club 5** (Size = 4 đỉnh): `[19, 55, 56, 77]`
- **Club 10** (Size = 5 đỉnh): `[20, 48, 49, 53, 57]`
- **Club 11** (Size = 11 đỉnh): `[28, 66, 70, 72, 76, 80, 85, 88, 89, 90, 92]`
- **Club 1** (Size = 13 đỉnh): `[30, 31, 71, 74, 75, 78, 79, 82, 83, 84, 87, 91, 98]`
- **Club 3** (Size = 6 đỉnh): `[34, 35, 36, 38, 43, 44]`
- **Club 13** (Size = 8 đỉnh): `[50, 51, 52, 58, 64, 65, 68, 69]`
- **Club 4** (Size = 6 đỉnh): `[59, 60, 62, 63, 99, 100]`
- **Club 7** (Size = 5 đỉnh): `[61, 81, 86, 97, 101]`
- **Club 12** (Size = 3 đỉnh): `[67, 103, 104]`
- **Club 6** (Size = 6 đỉnh): `[73, 93, 94, 95, 96, 102]`

---
*File được sinh tự động bởi hệ thống EVO-RL MSCC Research Framework.*
