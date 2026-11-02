# Báo Cáo Kết Quả Thực Nghiệm: Seed #04 (Seed = `26062026`)

**Tập dữ liệu đồ thị:** `lesmis` ($|V| = 77$, $|E| = 262$, Density = $0.0895$, $s = 2$)  
**Hạt giống cố định (Seed Value):** `26062026` (Lần chạy 04/20 từ `seedun.md`)  
**Thời gian thực thi:** `2026-09-13 11:47:16`  
**Môi trường tính toán:** `Hybrid Co-Processing [CPU: 12 Cores song song (GA/C++ igraph) + GPU: NVIDIA GeForce RTX 3050 Laptop GPU (PPO Tensor Cores)]`  

---

## 1. Bảng Thống Kê Hiệu Năng Chi Tiết Các Thuật Toán (Seed #4)

| Chiến lược / Thuật toán | Best Cover (Min) | Best Fitness | Mean $\pm$ Std | Median | Vi phạm ($diam > s$) | Độ đa dạng | Khả thi ($100\%$) | Thời gian (s) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **PPO-AOS** | **10** | **10.00** | 10.04 $\pm$ 0.19 | 10.0 | 0.00 | 0.806 |  Đạt chuẩn | 7.07s |
| MAB-AOS | 10 | 10.00 | 10.02 $\pm$ 0.14 | 10.0 | 0.00 | 0.880 |  Đạt chuẩn | 4.30s |
| Greedy-AOS | 10 | 10.00 | 10.02 $\pm$ 0.14 | 10.0 | 0.00 | 0.839 |  Đạt chuẩn | 3.84s |
| I-MSM | 10 | 10.00 | 10.06 $\pm$ 0.24 | 10.0 | 0.00 | 0.000 |  Đạt chuẩn | 0.70s |
| CCA | 10 | 10.00 | 10.33 $\pm$ 0.47 | 10.0 | 0.00 | 0.000 |  Đạt chuẩn | 0.12s |
| No-RL | 10 | 10.00 | 10.02 $\pm$ 0.14 | 10.0 | 0.00 | 0.889 |  Đạt chuẩn | 4.11s |
| Fixed | 10 | 10.00 | 10.03 $\pm$ 0.17 | 10.0 | 0.00 | 0.882 |  Đạt chuẩn | 2.77s |
| Random | 10 | 10.00 | 10.02 $\pm$ 0.14 | 10.0 | 0.00 | 0.889 |  Đạt chuẩn | 4.06s |

---

## 2. Cấu Trúc Nghiệm Tốt Nhất Trong Lần Chạy (Best Solution Clusters)
- **Thuật toán đạt Best:** `PPO-AOS` (Cover = `10` clubs, Fitness = `10.00`)
- **Kích thước các cụm ($s$-clubs):** `[10, 23, 7, 11, 2, 2, 14, 3, 4, 1]`
- **Số thế hệ tiến hóa:** `105` generations

### Chi tiết các cụm $s$-club thành phần:
- **Club 1** (Size = 10 đỉnh): `[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]`
- **Club 3** (Size = 23 đỉnh): `[10, 11, 12, 13, 14, 15, 26, 27, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 43, 44, 69, 70, 72]`
- **Club 6** (Size = 7 đỉnh): `[16, 17, 18, 19, 20, 21, 22]`
- **Club 2** (Size = 11 đỉnh): `[23, 24, 25, 39, 40, 41, 42, 55, 68, 71, 75]`
- **Club 7** (Size = 2 đỉnh): `[28, 45]`
- **Club 4** (Size = 2 đỉnh): `[46, 47]`
- **Club 5** (Size = 14 đỉnh): `[48, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 73, 74, 76]`
- **Club 8** (Size = 3 đỉnh): `[49, 50, 56]`
- **Club 9** (Size = 4 đỉnh): `[51, 52, 53, 54]`
- **Club 10** (Size = 1 đỉnh): `[67]`

---
*File được sinh tự động bởi hệ thống EVO-RL MSCC Research Framework.*
