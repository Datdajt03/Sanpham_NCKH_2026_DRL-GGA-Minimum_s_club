# Báo Cáo Kết Quả Thực Nghiệm: Seed #16 (Seed = `27182818`)

**Tập dữ liệu đồ thị:** `polbooks` ($|V| = 105$, $|E| = 441$, Density = $0.0808$, $s = 2$)  
**Hạt giống cố định (Seed Value):** `27182818` (Lần chạy 16/20 từ `seedun.md`)  
**Thời gian thực thi:** `2026-09-13 11:49:09`  
**Môi trường tính toán:** `Hybrid Co-Processing [CPU: 12 Cores song song (GA/C++ igraph) + GPU: NVIDIA GeForce RTX 3050 Laptop GPU (PPO Tensor Cores)]`  

---

## 1. Bảng Thống Kê Hiệu Năng Chi Tiết Các Thuật Toán (Seed #16)

| Chiến lược / Thuật toán | Best Cover (Min) | Best Fitness | Mean $\pm$ Std | Median | Vi phạm ($diam > s$) | Độ đa dạng | Khả thi ($100\%$) | Thời gian (s) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **PPO-AOS** | **13** | **13.00** | 13.31 $\pm$ 0.78 | 13.0 | 0.00 | 0.907 |  Đạt chuẩn | 5.81s |
| MAB-AOS | 13 | 13.00 | 13.30 $\pm$ 0.86 | 13.0 | 0.00 | 0.915 |  Đạt chuẩn | 5.15s |
| Greedy-AOS | 13 | 13.00 | 13.42 $\pm$ 0.93 | 13.0 | 0.00 | 0.860 |  Đạt chuẩn | 5.54s |
| I-MSM | 12 | 12.00 | 12.40 $\pm$ 0.80 | 12.0 | 0.00 | 0.000 |  Đạt chuẩn | 1.38s |
| CCA | 15 | 15.00 | 15.00 $\pm$ 0.00 | 15.0 | 0.00 | 0.000 |  Đạt chuẩn | 0.18s |
| No-RL | 13 | 13.00 | 13.40 $\pm$ 0.99 | 13.0 | 0.00 | 0.860 |  Đạt chuẩn | 5.31s |
| Fixed | 13 | 13.00 | 13.35 $\pm$ 0.90 | 13.0 | 0.00 | 0.886 |  Đạt chuẩn | 4.12s |
| Random | 13 | 13.00 | 13.40 $\pm$ 0.99 | 13.0 | 0.00 | 0.860 |  Đạt chuẩn | 4.86s |

---

## 2. Cấu Trúc Nghiệm Tốt Nhất Trong Lần Chạy (Best Solution Clusters)
- **Thuật toán đạt Best:** `I-MSM` (Cover = `12` clubs, Fitness = `12.00`)
- **Kích thước các cụm ($s$-clubs):** `[26, 14, 23, 7, 9, 21, 23, 7, 16, 14, 12, 24]`
- **Số thế hệ tiến hóa:** `20` generations

### Chi tiết các cụm $s$-club thành phần:
- **Club 1** (Size = 26 đỉnh): `[3, 8, 40, 10, 12, 9, 47, 11, 24, 13, 6, 35, 33, 14, 23, 41, 39, 38, 54, 37, 15, 36, 44, 32, 55, 46]`
- **Club 2** (Size = 14 đỉnh): `[58, 69, 64, 49, 7, 77, 65, 51, 52, 85, 68, 50, 30, 14]`
- **Club 3** (Size = 23 đỉnh): `[20, 53, 26, 8, 3, 45, 9, 40, 27, 22, 25, 12, 42, 11, 47, 13, 41, 35, 24, 39, 14, 54, 44]`
- **Club 4** (Size = 7 đỉnh): `[67, 104, 103, 66, 30, 65, 64]`
- **Club 5** (Size = 9 đỉnh): `[5, 4, 2, 0, 29, 28, 30, 6, 31]`
- **Club 6** (Size = 21 đỉnh): `[91, 98, 90, 72, 73, 87, 66, 86, 84, 71, 74, 78, 30, 75, 99, 31, 82, 79, 88, 89, 92]`
- **Club 7** (Size = 23 đỉnh): `[70, 66, 80, 84, 30, 72, 75, 86, 73, 71, 100, 81, 74, 99, 76, 82, 83, 79, 87, 96, 97, 89, 88]`
- **Club 8** (Size = 7 đỉnh): `[95, 102, 61, 73, 94, 101, 84]`
- **Club 9** (Size = 16 đỉnh): `[34, 39, 12, 40, 10, 38, 35, 8, 33, 37, 47, 44, 36, 41, 42, 43]`
- **Club 10** (Size = 14 đỉnh): `[59, 63, 99, 66, 84, 30, 73, 74, 100, 60, 86, 93, 90, 62]`
- **Club 11** (Size = 12 đỉnh): `[57, 13, 48, 56, 20, 11, 8, 3, 9, 12, 47, 49]`
- **Club 12** (Size = 24 đỉnh): `[1, 0, 3, 18, 16, 8, 11, 19, 13, 10, 12, 9, 24, 20, 14, 26, 27, 23, 22, 5, 17, 15, 21, 25]`

---
*File được sinh tự động bởi hệ thống EVO-RL MSCC Research Framework.*
