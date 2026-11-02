# Báo Cáo Kết Quả Thực Nghiệm: Seed #08 (Seed = `20260523`)

**Tập dữ liệu đồ thị:** `lesmis` ($|V| = 77$, $|E| = 262$, Density = $0.0895$, $s = 2$)  
**Hạt giống cố định (Seed Value):** `20260523` (Lần chạy 08/20 từ `seedun.md`)  
**Thời gian thực thi:** `2026-09-13 11:47:17`  
**Môi trường tính toán:** `Hybrid Co-Processing [CPU: 12 Cores song song (GA/C++ igraph) + GPU: NVIDIA GeForce RTX 3050 Laptop GPU (PPO Tensor Cores)]`  

---

## 1. Bảng Thống Kê Hiệu Năng Chi Tiết Các Thuật Toán (Seed #8)

| Chiến lược / Thuật toán | Best Cover (Min) | Best Fitness | Mean $\pm$ Std | Median | Vi phạm ($diam > s$) | Độ đa dạng | Khả thi ($100\%$) | Thời gian (s) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **PPO-AOS** | **10** | **10.00** | 10.06 $\pm$ 0.23 | 10.0 | 0.00 | 0.648 |  Đạt chuẩn | 8.15s |
| MAB-AOS | 10 | 10.00 | 10.01 $\pm$ 0.10 | 10.0 | 0.00 | 0.828 |  Đạt chuẩn | 4.16s |
| Greedy-AOS | 10 | 10.00 | 10.07 $\pm$ 0.26 | 10.0 | 0.00 | 0.806 |  Đạt chuẩn | 4.29s |
| I-MSM | 10 | 10.00 | 10.12 $\pm$ 0.47 | 10.0 | 0.00 | 0.000 |  Đạt chuẩn | 0.78s |
| CCA | 10 | 10.00 | 10.16 $\pm$ 0.36 | 10.0 | 0.00 | 0.000 |  Đạt chuẩn | 0.11s |
| No-RL | 10 | 10.00 | 10.06 $\pm$ 0.23 | 10.0 | 0.00 | 0.851 |  Đạt chuẩn | 3.80s |
| Fixed | 10 | 10.00 | 10.04 $\pm$ 0.19 | 10.0 | 0.00 | 0.847 |  Đạt chuẩn | 2.88s |
| Random | 10 | 10.00 | 10.06 $\pm$ 0.23 | 10.0 | 0.00 | 0.851 |  Đạt chuẩn | 3.82s |

---

## 2. Cấu Trúc Nghiệm Tốt Nhất Trong Lần Chạy (Best Solution Clusters)
- **Thuật toán đạt Best:** `PPO-AOS` (Cover = `10` clubs, Fitness = `10.00`)
- **Kích thước các cụm ($s$-clubs):** `[10, 26, 5, 10, 1, 2, 13, 4, 4, 2]`
- **Số thế hệ tiến hóa:** `107` generations

### Chi tiết các cụm $s$-club thành phần:
- **Club 5** (Size = 10 đỉnh): `[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]`
- **Club 6** (Size = 26 đỉnh): `[10, 11, 12, 13, 14, 15, 16, 18, 23, 24, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 43, 44, 72]`
- **Club 7** (Size = 5 đỉnh): `[17, 19, 20, 21, 22]`
- **Club 3** (Size = 10 đỉnh): `[25, 39, 40, 41, 42, 68, 69, 70, 71, 75]`
- **Club 8** (Size = 1 đỉnh): `[45]`
- **Club 9** (Size = 2 đỉnh): `[46, 47]`
- **Club 2** (Size = 13 đỉnh): `[48, 58, 59, 60, 61, 62, 63, 64, 65, 66, 73, 74, 76]`
- **Club 10** (Size = 4 đỉnh): `[49, 50, 55, 56]`
- **Club 4** (Size = 4 đỉnh): `[51, 52, 53, 54]`
- **Club 1** (Size = 2 đỉnh): `[57, 67]`

---
*File được sinh tự động bởi hệ thống EVO-RL MSCC Research Framework.*
