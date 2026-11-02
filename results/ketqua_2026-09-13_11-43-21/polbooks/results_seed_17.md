# Báo Cáo Kết Quả Thực Nghiệm: Seed #17 (Seed = `52013140`)

**Tập dữ liệu đồ thị:** `polbooks` ($|V| = 105$, $|E| = 441$, Density = $0.0808$, $s = 2$)  
**Hạt giống cố định (Seed Value):** `52013140` (Lần chạy 17/20 từ `seedun.md`)  
**Thời gian thực thi:** `2026-09-13 11:49:12`  
**Môi trường tính toán:** `Hybrid Co-Processing [CPU: 12 Cores song song (GA/C++ igraph) + GPU: NVIDIA GeForce RTX 3050 Laptop GPU (PPO Tensor Cores)]`  

---

## 1. Bảng Thống Kê Hiệu Năng Chi Tiết Các Thuật Toán (Seed #17)

| Chiến lược / Thuật toán | Best Cover (Min) | Best Fitness | Mean $\pm$ Std | Median | Vi phạm ($diam > s$) | Độ đa dạng | Khả thi ($100\%$) | Thời gian (s) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **PPO-AOS** | **13** | **13.00** | 13.38 $\pm$ 0.77 | 13.0 | 0.00 | 0.823 |  Đạt chuẩn | 6.96s |
| MAB-AOS | 14 | 14.00 | 14.24 $\pm$ 0.54 | 14.0 | 0.00 | 0.852 |  Đạt chuẩn | 5.73s |
| Greedy-AOS | 13 | 13.00 | 13.29 $\pm$ 0.72 | 13.0 | 0.00 | 0.842 |  Đạt chuẩn | 5.28s |
| I-MSM | 13 | 13.00 | 13.62 $\pm$ 0.76 | 13.0 | 0.00 | 0.000 |  Đạt chuẩn | 1.96s |
| CCA | 14 | 14.00 | 14.22 $\pm$ 0.63 | 14.0 | 0.00 | 0.000 |  Đạt chuẩn | 0.22s |
| No-RL | 13 | 13.00 | 13.37 $\pm$ 0.79 | 13.0 | 0.00 | 0.813 |  Đạt chuẩn | 5.95s |
| Fixed | 13 | 13.00 | 13.30 $\pm$ 0.67 | 13.0 | 0.00 | 0.870 |  Đạt chuẩn | 4.19s |
| Random | 13 | 13.00 | 13.37 $\pm$ 0.79 | 13.0 | 0.00 | 0.813 |  Đạt chuẩn | 4.05s |

---

## 2. Cấu Trúc Nghiệm Tốt Nhất Trong Lần Chạy (Best Solution Clusters)
- **Thuật toán đạt Best:** `PPO-AOS` (Cover = `13` clubs, Fitness = `13.00`)
- **Kích thước các cụm ($s$-clubs):** `[7, 9, 10, 11, 7, 12, 6, 10, 14, 5, 3, 8, 3]`
- **Số thế hệ tiến hóa:** `136` generations

### Chi tiết các cụm $s$-club thành phần:
- **Club 3** (Size = 7 đỉnh): `[0, 2, 4, 5, 6, 28, 29]`
- **Club 7** (Size = 9 đỉnh): `[1, 3, 15, 16, 18, 19, 21, 22, 25]`
- **Club 9** (Size = 10 đỉnh): `[7, 50, 51, 52, 58, 65, 68, 69, 77, 85]`
- **Club 5** (Size = 11 đỉnh): `[8, 9, 11, 13, 14, 26, 27, 42, 43, 45, 56]`
- **Club 1** (Size = 7 đỉnh): `[10, 33, 34, 35, 37, 38, 39]`
- **Club 10** (Size = 12 đỉnh): `[12, 17, 23, 32, 36, 40, 41, 44, 46, 47, 54, 55]`
- **Club 6** (Size = 6 đỉnh): `[20, 24, 48, 49, 53, 57]`
- **Club 11** (Size = 10 đỉnh): `[30, 64, 66, 70, 80, 88, 89, 90, 93, 99]`
- **Club 12** (Size = 14 đỉnh): `[31, 71, 72, 73, 74, 75, 78, 79, 82, 83, 87, 91, 92, 98]`
- **Club 13** (Size = 5 đỉnh): `[59, 60, 61, 62, 63]`
- **Club 2** (Size = 3 đỉnh): `[67, 103, 104]`
- **Club 4** (Size = 8 đỉnh): `[76, 81, 84, 86, 96, 97, 100, 101]`
- **Club 8** (Size = 3 đỉnh): `[94, 95, 102]`

---
*File được sinh tự động bởi hệ thống EVO-RL MSCC Research Framework.*
