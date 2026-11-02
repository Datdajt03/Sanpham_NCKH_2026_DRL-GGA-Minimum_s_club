# Báo Cáo Kết Quả Thực Nghiệm: Seed #14 (Seed = `24681357`)

**Tập dữ liệu đồ thị:** `polbooks` ($|V| = 105$, $|E| = 441$, Density = $0.0808$, $s = 2$)  
**Hạt giống cố định (Seed Value):** `24681357` (Lần chạy 14/20 từ `seedun.md`)  
**Thời gian thực thi:** `2026-09-13 11:49:13`  
**Môi trường tính toán:** `Hybrid Co-Processing [CPU: 12 Cores song song (GA/C++ igraph) + GPU: NVIDIA GeForce RTX 3050 Laptop GPU (PPO Tensor Cores)]`  

---

## 1. Bảng Thống Kê Hiệu Năng Chi Tiết Các Thuật Toán (Seed #14)

| Chiến lược / Thuật toán | Best Cover (Min) | Best Fitness | Mean $\pm$ Std | Median | Vi phạm ($diam > s$) | Độ đa dạng | Khả thi ($100\%$) | Thời gian (s) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **PPO-AOS** | **13** | **13.00** | 13.44 $\pm$ 0.76 | 13.0 | 0.00 | 0.862 |  Đạt chuẩn | 7.37s |
| MAB-AOS | 13 | 13.00 | 13.39 $\pm$ 0.72 | 13.0 | 0.00 | 0.878 |  Đạt chuẩn | 5.91s |
| Greedy-AOS | 13 | 13.00 | 13.25 $\pm$ 0.57 | 13.0 | 0.00 | 0.894 |  Đạt chuẩn | 5.52s |
| I-MSM | 13 | 13.00 | 13.71 $\pm$ 0.88 | 13.0 | 0.00 | 0.000 |  Đạt chuẩn | 1.93s |
| CCA | 13 | 13.00 | 13.52 $\pm$ 0.62 | 13.0 | 0.00 | 0.000 |  Đạt chuẩn | 0.32s |
| No-RL | 13 | 13.00 | 13.48 $\pm$ 0.78 | 13.0 | 0.00 | 0.861 |  Đạt chuẩn | 6.60s |
| Fixed | 13 | 13.00 | 13.33 $\pm$ 0.62 | 13.0 | 0.00 | 0.871 |  Đạt chuẩn | 4.73s |
| Random | 13 | 13.00 | 13.48 $\pm$ 0.78 | 13.0 | 0.00 | 0.861 |  Đạt chuẩn | 4.39s |

---

## 2. Cấu Trúc Nghiệm Tốt Nhất Trong Lần Chạy (Best Solution Clusters)
- **Thuật toán đạt Best:** `PPO-AOS` (Cover = `13` clubs, Fitness = `13.00`)
- **Kích thước các cụm ($s$-clubs):** `[7, 12, 10, 14, 10, 16, 12, 4, 4, 6, 4, 1, 5]`
- **Số thế hệ tiến hóa:** `142` generations

### Chi tiết các cụm $s$-club thành phần:
- **Club 9** (Size = 7 đỉnh): `[0, 1, 2, 4, 5, 6, 29]`
- **Club 10** (Size = 12 đỉnh): `[3, 8, 10, 11, 13, 15, 16, 17, 18, 19, 21, 23]`
- **Club 7** (Size = 10 đỉnh): `[7, 50, 51, 52, 58, 64, 65, 68, 77, 85]`
- **Club 11** (Size = 14 đỉnh): `[9, 12, 14, 24, 32, 33, 36, 38, 39, 41, 44, 46, 47, 55]`
- **Club 1** (Size = 10 đỉnh): `[20, 22, 25, 26, 27, 40, 42, 45, 53, 54]`
- **Club 4** (Size = 16 đỉnh): `[28, 66, 70, 72, 73, 76, 80, 88, 89, 90, 92, 93, 96, 97, 99, 100]`
- **Club 5** (Size = 12 đỉnh): `[30, 31, 71, 74, 75, 78, 79, 82, 83, 87, 91, 98]`
- **Club 6** (Size = 4 đỉnh): `[34, 35, 37, 43]`
- **Club 12** (Size = 4 đỉnh): `[48, 49, 56, 57]`
- **Club 3** (Size = 6 đỉnh): `[59, 60, 61, 62, 63, 86]`
- **Club 13** (Size = 4 đỉnh): `[67, 69, 103, 104]`
- **Club 8** (Size = 1 đỉnh): `[81]`
- **Club 2** (Size = 5 đỉnh): `[84, 94, 95, 101, 102]`

---
*File được sinh tự động bởi hệ thống EVO-RL MSCC Research Framework.*
