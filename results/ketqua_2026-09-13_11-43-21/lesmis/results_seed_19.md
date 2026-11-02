# Báo Cáo Kết Quả Thực Nghiệm: Seed #19 (Seed = `64086408`)

**Tập dữ liệu đồ thị:** `lesmis` ($|V| = 77$, $|E| = 262$, Density = $0.0895$, $s = 2$)  
**Hạt giống cố định (Seed Value):** `64086408` (Lần chạy 19/20 từ `seedun.md`)  
**Thời gian thực thi:** `2026-09-13 11:47:40`  
**Môi trường tính toán:** `Hybrid Co-Processing [CPU: 12 Cores song song (GA/C++ igraph) + GPU: NVIDIA GeForce RTX 3050 Laptop GPU (PPO Tensor Cores)]`  

---

## 1. Bảng Thống Kê Hiệu Năng Chi Tiết Các Thuật Toán (Seed #19)

| Chiến lược / Thuật toán | Best Cover (Min) | Best Fitness | Mean $\pm$ Std | Median | Vi phạm ($diam > s$) | Độ đa dạng | Khả thi ($100\%$) | Thời gian (s) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **PPO-AOS** | **10** | **10.00** | 10.00 $\pm$ 0.00 | 10.0 | 0.00 | 0.885 |  Đạt chuẩn | 4.72s |
| MAB-AOS | 10 | 10.00 | 10.00 $\pm$ 0.00 | 10.0 | 0.00 | 0.865 |  Đạt chuẩn | 3.65s |
| Greedy-AOS | 10 | 10.00 | 10.00 $\pm$ 0.00 | 10.0 | 0.00 | 0.870 |  Đạt chuẩn | 3.94s |
| I-MSM | 10 | 10.00 | 10.00 $\pm$ 0.00 | 10.0 | 0.00 | 0.000 |  Đạt chuẩn | 0.71s |
| CCA | 10 | 10.00 | 10.11 $\pm$ 0.31 | 10.0 | 0.00 | 0.000 |  Đạt chuẩn | 0.09s |
| No-RL | 10 | 10.00 | 10.00 $\pm$ 0.00 | 10.0 | 0.00 | 0.871 |  Đạt chuẩn | 3.82s |
| Fixed | 10 | 10.00 | 10.00 $\pm$ 0.00 | 10.0 | 0.00 | 0.851 |  Đạt chuẩn | 2.91s |
| Random | 10 | 10.00 | 10.00 $\pm$ 0.00 | 10.0 | 0.00 | 0.871 |  Đạt chuẩn | 3.28s |

---

## 2. Cấu Trúc Nghiệm Tốt Nhất Trong Lần Chạy (Best Solution Clusters)
- **Thuật toán đạt Best:** `PPO-AOS` (Cover = `10` clubs, Fitness = `10.00`)
- **Kích thước các cụm ($s$-clubs):** `[10, 19, 9, 14, 1, 2, 6, 4, 3, 9]`
- **Số thế hệ tiến hóa:** `101` generations

### Chi tiết các cụm $s$-club thành phần:
- **Club 8** (Size = 10 đỉnh): `[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]`
- **Club 6** (Size = 19 đỉnh): `[10, 11, 13, 14, 15, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 43, 44, 72]`
- **Club 1** (Size = 9 đỉnh): `[12, 16, 17, 18, 19, 20, 21, 22, 23]`
- **Club 3** (Size = 14 đỉnh): `[24, 25, 26, 27, 39, 40, 41, 42, 55, 68, 69, 70, 71, 75]`
- **Club 7** (Size = 1 đỉnh): `[45]`
- **Club 10** (Size = 2 đỉnh): `[46, 47]`
- **Club 2** (Size = 6 đỉnh): `[48, 60, 66, 73, 74, 76]`
- **Club 5** (Size = 4 đỉnh): `[49, 50, 54, 56]`
- **Club 9** (Size = 3 đỉnh): `[51, 52, 53]`
- **Club 4** (Size = 9 đỉnh): `[57, 58, 59, 61, 62, 63, 64, 65, 67]`

---
*File được sinh tự động bởi hệ thống EVO-RL MSCC Research Framework.*
