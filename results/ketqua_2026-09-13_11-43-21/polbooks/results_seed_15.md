# Báo Cáo Kết Quả Thực Nghiệm: Seed #15 (Seed = `31415926`)

**Tập dữ liệu đồ thị:** `polbooks` ($|V| = 105$, $|E| = 441$, Density = $0.0808$, $s = 2$)  
**Hạt giống cố định (Seed Value):** `31415926` (Lần chạy 15/20 từ `seedun.md`)  
**Thời gian thực thi:** `2026-09-13 11:49:10`  
**Môi trường tính toán:** `Hybrid Co-Processing [CPU: 12 Cores song song (GA/C++ igraph) + GPU: NVIDIA GeForce RTX 3050 Laptop GPU (PPO Tensor Cores)]`  

---

## 1. Bảng Thống Kê Hiệu Năng Chi Tiết Các Thuật Toán (Seed #15)

| Chiến lược / Thuật toán | Best Cover (Min) | Best Fitness | Mean $\pm$ Std | Median | Vi phạm ($diam > s$) | Độ đa dạng | Khả thi ($100\%$) | Thời gian (s) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **PPO-AOS** | **13** | **13.00** | 13.20 $\pm$ 0.61 | 13.0 | 0.00 | 0.866 |  Đạt chuẩn | 6.24s |
| MAB-AOS | 13 | 13.00 | 13.26 $\pm$ 0.68 | 13.0 | 0.00 | 0.872 |  Đạt chuẩn | 5.12s |
| Greedy-AOS | 13 | 13.00 | 13.28 $\pm$ 0.69 | 13.0 | 0.00 | 0.841 |  Đạt chuẩn | 5.13s |
| I-MSM | 13 | 13.00 | 13.39 $\pm$ 1.21 | 13.0 | 0.00 | 0.000 |  Đạt chuẩn | 1.18s |
| CCA | 14 | 14.00 | 14.45 $\pm$ 0.50 | 14.0 | 0.00 | 0.000 |  Đạt chuẩn | 0.35s |
| No-RL | 13 | 13.00 | 13.39 $\pm$ 0.75 | 13.0 | 0.00 | 0.924 |  Đạt chuẩn | 6.23s |
| Fixed | 13 | 13.00 | 13.25 $\pm$ 0.71 | 13.0 | 0.00 | 0.907 |  Đạt chuẩn | 4.00s |
| Random | 13 | 13.00 | 13.39 $\pm$ 0.75 | 13.0 | 0.00 | 0.924 |  Đạt chuẩn | 5.89s |

---

## 2. Cấu Trúc Nghiệm Tốt Nhất Trong Lần Chạy (Best Solution Clusters)
- **Thuật toán đạt Best:** `PPO-AOS` (Cover = `13` clubs, Fitness = `13.00`)
- **Kích thước các cụm ($s$-clubs):** `[8, 7, 22, 12, 3, 4, 6, 16, 6, 6, 3, 6, 6]`
- **Số thế hệ tiến hóa:** `114` generations

### Chi tiết các cụm $s$-club thành phần:
- **Club 4** (Size = 8 đỉnh): `[0, 1, 2, 4, 5, 6, 7, 29]`
- **Club 2** (Size = 7 đỉnh): `[3, 15, 16, 18, 21, 23, 25]`
- **Club 1** (Size = 22 đỉnh): `[8, 9, 10, 11, 12, 13, 17, 22, 24, 26, 27, 32, 33, 37, 40, 41, 42, 44, 45, 46, 47, 54]`
- **Club 3** (Size = 12 đỉnh): `[14, 49, 50, 51, 52, 58, 64, 65, 68, 69, 77, 85]`
- **Club 8** (Size = 3 đỉnh): `[19, 55, 56]`
- **Club 6** (Size = 4 đỉnh): `[20, 48, 53, 57]`
- **Club 9** (Size = 6 đỉnh): `[28, 66, 70, 90, 97, 99]`
- **Club 10** (Size = 16 đỉnh): `[30, 31, 72, 73, 74, 75, 82, 83, 84, 87, 88, 89, 91, 92, 98, 100]`
- **Club 11** (Size = 6 đỉnh): `[34, 35, 36, 38, 39, 43]`
- **Club 7** (Size = 6 đỉnh): `[59, 60, 61, 62, 63, 86]`
- **Club 12** (Size = 3 đỉnh): `[67, 103, 104]`
- **Club 13** (Size = 6 đỉnh): `[71, 76, 78, 79, 80, 81]`
- **Club 5** (Size = 6 đỉnh): `[93, 94, 95, 96, 101, 102]`

---
*File được sinh tự động bởi hệ thống EVO-RL MSCC Research Framework.*
