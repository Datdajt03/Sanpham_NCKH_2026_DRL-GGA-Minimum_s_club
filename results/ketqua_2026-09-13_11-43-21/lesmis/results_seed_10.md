# Báo Cáo Kết Quả Thực Nghiệm: Seed #10 (Seed = `20260913`)

**Tập dữ liệu đồ thị:** `lesmis` ($|V| = 77$, $|E| = 262$, Density = $0.0895$, $s = 2$)  
**Hạt giống cố định (Seed Value):** `20260913` (Lần chạy 10/20 từ `seedun.md`)  
**Thời gian thực thi:** `2026-09-13 11:47:16`  
**Môi trường tính toán:** `Hybrid Co-Processing [CPU: 12 Cores song song (GA/C++ igraph) + GPU: NVIDIA GeForce RTX 3050 Laptop GPU (PPO Tensor Cores)]`  

---

## 1. Bảng Thống Kê Hiệu Năng Chi Tiết Các Thuật Toán (Seed #10)

| Chiến lược / Thuật toán | Best Cover (Min) | Best Fitness | Mean $\pm$ Std | Median | Vi phạm ($diam > s$) | Độ đa dạng | Khả thi ($100\%$) | Thời gian (s) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **PPO-AOS** | **10** | **10.00** | 10.09 $\pm$ 0.29 | 10.0 | 0.00 | 0.857 |  Đạt chuẩn | 8.10s |
| MAB-AOS | 10 | 10.00 | 10.02 $\pm$ 0.14 | 10.0 | 0.00 | 0.864 |  Đạt chuẩn | 3.85s |
| Greedy-AOS | 10 | 10.00 | 10.08 $\pm$ 0.27 | 10.0 | 0.00 | 0.843 |  Đạt chuẩn | 3.81s |
| I-MSM | 10 | 10.00 | 10.16 $\pm$ 0.36 | 10.0 | 0.00 | 0.000 |  Đạt chuẩn | 0.83s |
| CCA | 10 | 10.00 | 10.00 $\pm$ 0.00 | 10.0 | 0.00 | 0.000 |  Đạt chuẩn | 0.09s |
| No-RL | 10 | 10.00 | 10.04 $\pm$ 0.19 | 10.0 | 0.00 | 0.818 |  Đạt chuẩn | 3.70s |
| Fixed | 10 | 10.00 | 10.05 $\pm$ 0.21 | 10.0 | 0.00 | 0.869 |  Đạt chuẩn | 2.76s |
| Random | 10 | 10.00 | 10.04 $\pm$ 0.19 | 10.0 | 0.00 | 0.818 |  Đạt chuẩn | 3.67s |

---

## 2. Cấu Trúc Nghiệm Tốt Nhất Trong Lần Chạy (Best Solution Clusters)
- **Thuật toán đạt Best:** `PPO-AOS` (Cover = `10` clubs, Fitness = `10.00`)
- **Kích thước các cụm ($s$-clubs):** `[10, 21, 7, 11, 5, 2, 5, 2, 11, 3]`
- **Số thế hệ tiến hóa:** `111` generations

### Chi tiết các cụm $s$-club thành phần:
- **Club 6** (Size = 10 đỉnh): `[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]`
- **Club 4** (Size = 21 đỉnh): `[10, 11, 12, 13, 14, 15, 23, 27, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 43, 44, 72]`
- **Club 7** (Size = 7 đỉnh): `[16, 17, 18, 19, 20, 21, 22]`
- **Club 8** (Size = 11 đỉnh): `[24, 25, 39, 40, 42, 55, 68, 69, 70, 71, 75]`
- **Club 9** (Size = 5 đỉnh): `[26, 49, 50, 54, 56]`
- **Club 2** (Size = 2 đỉnh): `[28, 45]`
- **Club 10** (Size = 5 đỉnh): `[41, 57, 61, 65, 67]`
- **Club 1** (Size = 2 đỉnh): `[46, 47]`
- **Club 5** (Size = 11 đỉnh): `[48, 58, 59, 60, 62, 63, 64, 66, 73, 74, 76]`
- **Club 3** (Size = 3 đỉnh): `[51, 52, 53]`

---
*File được sinh tự động bởi hệ thống EVO-RL MSCC Research Framework.*
