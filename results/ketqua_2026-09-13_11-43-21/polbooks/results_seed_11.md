# Báo Cáo Kết Quả Thực Nghiệm: Seed #11 (Seed = `11223344`)

**Tập dữ liệu đồ thị:** `polbooks` ($|V| = 105$, $|E| = 441$, Density = $0.0808$, $s = 2$)  
**Hạt giống cố định (Seed Value):** `11223344` (Lần chạy 11/20 từ `seedun.md`)  
**Thời gian thực thi:** `2026-09-13 11:49:12`  
**Môi trường tính toán:** `Hybrid Co-Processing [CPU: 12 Cores song song (GA/C++ igraph) + GPU: NVIDIA GeForce RTX 3050 Laptop GPU (PPO Tensor Cores)]`  

---

## 1. Bảng Thống Kê Hiệu Năng Chi Tiết Các Thuật Toán (Seed #11)

| Chiến lược / Thuật toán | Best Cover (Min) | Best Fitness | Mean $\pm$ Std | Median | Vi phạm ($diam > s$) | Độ đa dạng | Khả thi ($100\%$) | Thời gian (s) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **PPO-AOS** | **13** | **13.00** | 13.40 $\pm$ 0.56 | 13.0 | 0.00 | 0.671 |  Đạt chuẩn | 8.48s |
| MAB-AOS | 13 | 13.00 | 13.24 $\pm$ 0.51 | 13.0 | 0.00 | 0.816 |  Đạt chuẩn | 5.50s |
| Greedy-AOS | 14 | 14.00 | 14.05 $\pm$ 0.21 | 14.0 | 0.00 | 0.912 |  Đạt chuẩn | 5.04s |
| I-MSM | 13 | 13.00 | 13.38 $\pm$ 0.49 | 13.0 | 0.00 | 0.000 |  Đạt chuẩn | 1.79s |
| CCA | 14 | 14.00 | 14.43 $\pm$ 0.49 | 14.0 | 0.00 | 0.000 |  Đạt chuẩn | 0.32s |
| No-RL | 13 | 13.00 | 13.39 $\pm$ 0.59 | 13.0 | 0.00 | 0.901 |  Đạt chuẩn | 7.26s |
| Fixed | 13 | 13.00 | 13.29 $\pm$ 0.59 | 13.0 | 0.00 | 0.858 |  Đạt chuẩn | 4.92s |
| Random | 13 | 13.00 | 13.39 $\pm$ 0.59 | 13.0 | 0.00 | 0.901 |  Đạt chuẩn | 5.65s |

---

## 2. Cấu Trúc Nghiệm Tốt Nhất Trong Lần Chạy (Best Solution Clusters)
- **Thuật toán đạt Best:** `PPO-AOS` (Cover = `13` clubs, Fitness = `13.00`)
- **Kích thước các cụm ($s$-clubs):** `[15, 7, 17, 5, 5, 12, 6, 9, 6, 11, 3, 4, 5]`
- **Số thế hệ tiến hóa:** `159` generations

### Chi tiết các cụm $s$-club thành phần:
- **Club 6** (Size = 15 đỉnh): `[0, 1, 3, 5, 11, 14, 15, 16, 18, 21, 22, 23, 25, 26, 27]`
- **Club 9** (Size = 7 đỉnh): `[2, 4, 6, 7, 29, 30, 31]`
- **Club 4** (Size = 17 đỉnh): `[8, 9, 12, 13, 17, 24, 32, 33, 39, 40, 41, 42, 44, 45, 46, 47, 54]`
- **Club 5** (Size = 5 đỉnh): `[10, 19, 55, 56, 77]`
- **Club 3** (Size = 5 đỉnh): `[20, 48, 49, 53, 57]`
- **Club 7** (Size = 12 đỉnh): `[28, 70, 71, 72, 74, 76, 78, 80, 87, 90, 91, 92]`
- **Club 10** (Size = 6 đỉnh): `[34, 35, 36, 37, 38, 43]`
- **Club 11** (Size = 9 đỉnh): `[50, 51, 52, 58, 64, 65, 68, 69, 85]`
- **Club 12** (Size = 6 đỉnh): `[59, 60, 61, 62, 63, 99]`
- **Club 8** (Size = 11 đỉnh): `[66, 75, 79, 81, 82, 83, 84, 86, 88, 89, 100]`
- **Club 1** (Size = 3 đỉnh): `[67, 103, 104]`
- **Club 13** (Size = 4 đỉnh): `[73, 96, 97, 98]`
- **Club 2** (Size = 5 đỉnh): `[93, 94, 95, 101, 102]`

---
*File được sinh tự động bởi hệ thống EVO-RL MSCC Research Framework.*
