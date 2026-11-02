# Báo Cáo Kết Quả Thực Nghiệm: Seed #10 (Seed = `20260913`)

**Tập dữ liệu đồ thị:** `polbooks` ($|V| = 105$, $|E| = 441$, Density = $0.0808$, $s = 2$)  
**Hạt giống cố định (Seed Value):** `20260913` (Lần chạy 10/20 từ `seedun.md`)  
**Thời gian thực thi:** `2026-09-13 11:48:39`  
**Môi trường tính toán:** `Hybrid Co-Processing [CPU: 12 Cores song song (GA/C++ igraph) + GPU: NVIDIA GeForce RTX 3050 Laptop GPU (PPO Tensor Cores)]`  

---

## 1. Bảng Thống Kê Hiệu Năng Chi Tiết Các Thuật Toán (Seed #10)

| Chiến lược / Thuật toán | Best Cover (Min) | Best Fitness | Mean $\pm$ Std | Median | Vi phạm ($diam > s$) | Độ đa dạng | Khả thi ($100\%$) | Thời gian (s) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **PPO-AOS** | **13** | **13.00** | 13.35 $\pm$ 0.76 | 13.0 | 0.00 | 0.862 |  Đạt chuẩn | 8.55s |
| MAB-AOS | 14 | 14.00 | 14.17 $\pm$ 0.51 | 14.0 | 0.00 | 0.893 |  Đạt chuẩn | 5.35s |
| Greedy-AOS | 13 | 13.00 | 13.30 $\pm$ 0.72 | 13.0 | 0.00 | 0.907 |  Đạt chuẩn | 5.36s |
| I-MSM | 14 | 14.00 | 14.11 $\pm$ 0.31 | 14.0 | 0.00 | 0.000 |  Đạt chuẩn | 1.20s |
| CCA | 13 | 13.00 | 13.97 $\pm$ 1.05 | 14.0 | 0.00 | 0.000 |  Đạt chuẩn | 0.44s |
| No-RL | 13 | 13.00 | 13.52 $\pm$ 0.76 | 13.0 | 0.00 | 0.670 |  Đạt chuẩn | 7.62s |
| Fixed | 13 | 13.00 | 13.30 $\pm$ 0.66 | 13.0 | 0.00 | 0.870 |  Đạt chuẩn | 4.33s |
| Random | 13 | 13.00 | 13.52 $\pm$ 0.76 | 13.0 | 0.00 | 0.670 |  Đạt chuẩn | 7.85s |

---

## 2. Cấu Trúc Nghiệm Tốt Nhất Trong Lần Chạy (Best Solution Clusters)
- **Thuật toán đạt Best:** `PPO-AOS` (Cover = `13` clubs, Fitness = `13.00`)
- **Kích thước các cụm ($s$-clubs):** `[7, 17, 8, 9, 19, 6, 6, 5, 4, 10, 6, 3, 5]`
- **Số thế hệ tiến hóa:** `127` generations

### Chi tiết các cụm $s$-club thành phần:
- **Club 7** (Size = 7 đỉnh): `[0, 1, 2, 4, 6, 7, 29]`
- **Club 8** (Size = 17 đỉnh): `[3, 5, 8, 9, 10, 11, 14, 15, 16, 17, 19, 20, 21, 22, 23, 25, 27]`
- **Club 9** (Size = 8 đỉnh): `[12, 13, 18, 32, 33, 38, 44, 55]`
- **Club 3** (Size = 9 đỉnh): `[24, 26, 40, 41, 42, 45, 47, 53, 54]`
- **Club 10** (Size = 19 đỉnh): `[28, 30, 66, 70, 71, 72, 74, 75, 76, 78, 79, 80, 82, 86, 87, 88, 89, 90, 92]`
- **Club 6** (Size = 6 đỉnh): `[31, 73, 83, 91, 98, 100]`
- **Club 11** (Size = 6 đỉnh): `[34, 35, 36, 37, 39, 43]`
- **Club 12** (Size = 5 đỉnh): `[46, 93, 94, 95, 102]`
- **Club 13** (Size = 4 đỉnh): `[48, 49, 56, 57]`
- **Club 5** (Size = 10 đỉnh): `[50, 51, 52, 58, 64, 65, 68, 69, 77, 85]`
- **Club 1** (Size = 6 đỉnh): `[59, 60, 61, 62, 63, 99]`
- **Club 2** (Size = 3 đỉnh): `[67, 103, 104]`
- **Club 4** (Size = 5 đỉnh): `[81, 84, 96, 97, 101]`

---
*File được sinh tự động bởi hệ thống EVO-RL MSCC Research Framework.*
