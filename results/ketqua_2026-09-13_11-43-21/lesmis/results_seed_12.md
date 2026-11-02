# Báo Cáo Kết Quả Thực Nghiệm: Seed #12 (Seed = `12344321`)

**Tập dữ liệu đồ thị:** `lesmis` ($|V| = 77$, $|E| = 262$, Density = $0.0895$, $s = 2$)  
**Hạt giống cố định (Seed Value):** `12344321` (Lần chạy 12/20 từ `seedun.md`)  
**Thời gian thực thi:** `2026-09-13 11:47:38`  
**Môi trường tính toán:** `Hybrid Co-Processing [CPU: 12 Cores song song (GA/C++ igraph) + GPU: NVIDIA GeForce RTX 3050 Laptop GPU (PPO Tensor Cores)]`  

---

## 1. Bảng Thống Kê Hiệu Năng Chi Tiết Các Thuật Toán (Seed #12)

| Chiến lược / Thuật toán | Best Cover (Min) | Best Fitness | Mean $\pm$ Std | Median | Vi phạm ($diam > s$) | Độ đa dạng | Khả thi ($100\%$) | Thời gian (s) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **PPO-AOS** | **10** | **10.00** | 10.00 $\pm$ 0.00 | 10.0 | 0.00 | 0.884 |  Đạt chuẩn | 4.82s |
| MAB-AOS | 10 | 10.00 | 10.00 $\pm$ 0.00 | 10.0 | 0.00 | 0.882 |  Đạt chuẩn | 3.94s |
| Greedy-AOS | 10 | 10.00 | 10.00 $\pm$ 0.00 | 10.0 | 0.00 | 0.907 |  Đạt chuẩn | 3.99s |
| I-MSM | 10 | 10.00 | 10.17 $\pm$ 0.50 | 10.0 | 0.00 | 0.000 |  Đạt chuẩn | 0.77s |
| CCA | 10 | 10.00 | 10.16 $\pm$ 0.36 | 10.0 | 0.00 | 0.000 |  Đạt chuẩn | 0.09s |
| No-RL | 10 | 10.00 | 10.00 $\pm$ 0.00 | 10.0 | 0.00 | 0.855 |  Đạt chuẩn | 3.37s |
| Fixed | 10 | 10.00 | 10.00 $\pm$ 0.00 | 10.0 | 0.00 | 0.851 |  Đạt chuẩn | 2.80s |
| Random | 10 | 10.00 | 10.00 $\pm$ 0.00 | 10.0 | 0.00 | 0.855 |  Đạt chuẩn | 3.58s |

---

## 2. Cấu Trúc Nghiệm Tốt Nhất Trong Lần Chạy (Best Solution Clusters)
- **Thuật toán đạt Best:** `PPO-AOS` (Cover = `10` clubs, Fitness = `10.00`)
- **Kích thước các cụm ($s$-clubs):** `[10, 23, 6, 7, 6, 12, 2, 2, 3, 6]`
- **Số thế hệ tiến hóa:** `101` generations

### Chi tiết các cụm $s$-club thành phần:
- **Club 10** (Size = 10 đỉnh): `[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]`
- **Club 3** (Size = 23 đỉnh): `[10, 11, 12, 13, 14, 15, 16, 23, 24, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 43, 44, 71, 72]`
- **Club 5** (Size = 6 đỉnh): `[17, 18, 19, 20, 21, 22]`
- **Club 9** (Size = 7 đỉnh): `[25, 39, 40, 41, 42, 70, 75]`
- **Club 6** (Size = 6 đỉnh): `[26, 51, 52, 53, 54, 55]`
- **Club 8** (Size = 12 đỉnh): `[27, 48, 58, 59, 60, 63, 66, 68, 69, 73, 74, 76]`
- **Club 4** (Size = 2 đỉnh): `[28, 45]`
- **Club 7** (Size = 2 đỉnh): `[46, 47]`
- **Club 1** (Size = 3 đỉnh): `[49, 50, 56]`
- **Club 2** (Size = 6 đỉnh): `[57, 61, 62, 64, 65, 67]`

---
*File được sinh tự động bởi hệ thống EVO-RL MSCC Research Framework.*
