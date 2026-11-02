# Báo Cáo Kết Quả Thực Nghiệm: Seed #17 (Seed = `52013140`)

**Tập dữ liệu đồ thị:** `lesmis` ($|V| = 77$, $|E| = 262$, Density = $0.0895$, $s = 2$)  
**Hạt giống cố định (Seed Value):** `52013140` (Lần chạy 17/20 từ `seedun.md`)  
**Thời gian thực thi:** `2026-09-13 11:47:41`  
**Môi trường tính toán:** `Hybrid Co-Processing [CPU: 12 Cores song song (GA/C++ igraph) + GPU: NVIDIA GeForce RTX 3050 Laptop GPU (PPO Tensor Cores)]`  

---

## 1. Bảng Thống Kê Hiệu Năng Chi Tiết Các Thuật Toán (Seed #17)

| Chiến lược / Thuật toán | Best Cover (Min) | Best Fitness | Mean $\pm$ Std | Median | Vi phạm ($diam > s$) | Độ đa dạng | Khả thi ($100\%$) | Thời gian (s) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **PPO-AOS** | **10** | **10.00** | 10.02 $\pm$ 0.14 | 10.0 | 0.00 | 0.855 |  Đạt chuẩn | 4.73s |
| MAB-AOS | 10 | 10.00 | 10.05 $\pm$ 0.21 | 10.0 | 0.00 | 0.879 |  Đạt chuẩn | 3.94s |
| Greedy-AOS | 10 | 10.00 | 10.03 $\pm$ 0.17 | 10.0 | 0.00 | 0.786 |  Đạt chuẩn | 3.85s |
| I-MSM | 10 | 10.00 | 10.30 $\pm$ 0.46 | 10.0 | 0.00 | 0.000 |  Đạt chuẩn | 1.09s |
| CCA | 10 | 10.00 | 10.11 $\pm$ 0.31 | 10.0 | 0.00 | 0.000 |  Đạt chuẩn | 0.12s |
| No-RL | 10 | 10.00 | 10.06 $\pm$ 0.23 | 10.0 | 0.00 | 0.855 |  Đạt chuẩn | 4.62s |
| Fixed | 10 | 10.00 | 10.02 $\pm$ 0.14 | 10.0 | 0.00 | 0.870 |  Đạt chuẩn | 3.00s |
| Random | 10 | 10.00 | 10.06 $\pm$ 0.23 | 10.0 | 0.00 | 0.855 |  Đạt chuẩn | 3.48s |

---

## 2. Cấu Trúc Nghiệm Tốt Nhất Trong Lần Chạy (Best Solution Clusters)
- **Thuật toán đạt Best:** `PPO-AOS` (Cover = `10` clubs, Fitness = `10.00`)
- **Kích thước các cụm ($s$-clubs):** `[10, 23, 7, 10, 5, 1, 1, 14, 3, 3]`
- **Số thế hệ tiến hóa:** `103` generations

### Chi tiết các cụm $s$-club thành phần:
- **Club 8** (Size = 10 đỉnh): `[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]`
- **Club 6** (Size = 23 đỉnh): `[10, 11, 12, 13, 14, 15, 18, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 43, 44, 68, 69, 72]`
- **Club 5** (Size = 7 đỉnh): `[16, 17, 19, 20, 21, 22, 23]`
- **Club 1** (Size = 10 đỉnh): `[24, 25, 27, 39, 40, 41, 42, 70, 71, 75]`
- **Club 7** (Size = 5 đỉnh): `[26, 49, 50, 54, 56]`
- **Club 9** (Size = 1 đỉnh): `[45]`
- **Club 10** (Size = 1 đỉnh): `[46]`
- **Club 3** (Size = 14 đỉnh): `[47, 48, 55, 58, 60, 61, 62, 63, 64, 65, 66, 73, 74, 76]`
- **Club 2** (Size = 3 đỉnh): `[51, 52, 53]`
- **Club 4** (Size = 3 đỉnh): `[57, 59, 67]`

---
*File được sinh tự động bởi hệ thống EVO-RL MSCC Research Framework.*
