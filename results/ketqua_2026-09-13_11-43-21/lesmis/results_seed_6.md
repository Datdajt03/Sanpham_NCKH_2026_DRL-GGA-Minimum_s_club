# Báo Cáo Kết Quả Thực Nghiệm: Seed #06 (Seed = `20260317`)

**Tập dữ liệu đồ thị:** `lesmis` ($|V| = 77$, $|E| = 262$, Density = $0.0895$, $s = 2$)  
**Hạt giống cố định (Seed Value):** `20260317` (Lần chạy 06/20 từ `seedun.md`)  
**Thời gian thực thi:** `2026-09-13 11:47:14`  
**Môi trường tính toán:** `Hybrid Co-Processing [CPU: 12 Cores song song (GA/C++ igraph) + GPU: NVIDIA GeForce RTX 3050 Laptop GPU (PPO Tensor Cores)]`  

---

## 1. Bảng Thống Kê Hiệu Năng Chi Tiết Các Thuật Toán (Seed #6)

| Chiến lược / Thuật toán | Best Cover (Min) | Best Fitness | Mean $\pm$ Std | Median | Vi phạm ($diam > s$) | Độ đa dạng | Khả thi ($100\%$) | Thời gian (s) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **PPO-AOS** | **10** | **10.00** | 10.05 $\pm$ 0.21 | 10.0 | 0.00 | 0.822 |  Đạt chuẩn | 6.33s |
| MAB-AOS | 10 | 10.00 | 10.06 $\pm$ 0.23 | 10.0 | 0.00 | 0.861 |  Đạt chuẩn | 4.13s |
| Greedy-AOS | 10 | 10.00 | 10.02 $\pm$ 0.14 | 10.0 | 0.00 | 0.832 |  Đạt chuẩn | 3.60s |
| I-MSM | 10 | 10.00 | 10.20 $\pm$ 0.40 | 10.0 | 0.00 | 0.000 |  Đạt chuẩn | 0.90s |
| CCA | 10 | 10.00 | 10.17 $\pm$ 0.50 | 10.0 | 0.00 | 0.000 |  Đạt chuẩn | 0.11s |
| No-RL | 10 | 10.00 | 10.03 $\pm$ 0.17 | 10.0 | 0.00 | 0.772 |  Đạt chuẩn | 3.53s |
| Fixed | 10 | 10.00 | 10.04 $\pm$ 0.19 | 10.0 | 0.00 | 0.877 |  Đạt chuẩn | 2.69s |
| Random | 10 | 10.00 | 10.03 $\pm$ 0.17 | 10.0 | 0.00 | 0.772 |  Đạt chuẩn | 3.80s |

---

## 2. Cấu Trúc Nghiệm Tốt Nhất Trong Lần Chạy (Best Solution Clusters)
- **Thuật toán đạt Best:** `PPO-AOS` (Cover = `10` clubs, Fitness = `10.00`)
- **Kích thước các cụm ($s$-clubs):** `[10, 19, 9, 11, 3, 2, 15, 4, 3, 1]`
- **Số thế hệ tiến hóa:** `106` generations

### Chi tiết các cụm $s$-club thành phần:
- **Club 7** (Size = 10 đỉnh): `[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]`
- **Club 5** (Size = 19 đỉnh): `[10, 11, 12, 13, 14, 15, 27, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 43, 72]`
- **Club 3** (Size = 9 đỉnh): `[16, 17, 18, 19, 20, 21, 22, 23, 26]`
- **Club 2** (Size = 11 đỉnh): `[24, 25, 39, 40, 41, 42, 68, 69, 70, 71, 75]`
- **Club 10** (Size = 3 đỉnh): `[28, 44, 45]`
- **Club 6** (Size = 2 đỉnh): `[46, 47]`
- **Club 1** (Size = 15 đỉnh): `[48, 55, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 73, 74, 76]`
- **Club 9** (Size = 4 đỉnh): `[49, 50, 54, 56]`
- **Club 4** (Size = 3 đỉnh): `[51, 52, 53]`
- **Club 8** (Size = 1 đỉnh): `[67]`

---
*File được sinh tự động bởi hệ thống EVO-RL MSCC Research Framework.*
