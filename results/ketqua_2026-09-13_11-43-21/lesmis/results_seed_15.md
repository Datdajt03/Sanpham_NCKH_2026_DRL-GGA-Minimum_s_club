# Báo Cáo Kết Quả Thực Nghiệm: Seed #15 (Seed = `31415926`)

**Tập dữ liệu đồ thị:** `lesmis` ($|V| = 77$, $|E| = 262$, Density = $0.0895$, $s = 2$)  
**Hạt giống cố định (Seed Value):** `31415926` (Lần chạy 15/20 từ `seedun.md`)  
**Thời gian thực thi:** `2026-09-13 11:47:40`  
**Môi trường tính toán:** `Hybrid Co-Processing [CPU: 12 Cores song song (GA/C++ igraph) + GPU: NVIDIA GeForce RTX 3050 Laptop GPU (PPO Tensor Cores)]`  

---

## 1. Bảng Thống Kê Hiệu Năng Chi Tiết Các Thuật Toán (Seed #15)

| Chiến lược / Thuật toán | Best Cover (Min) | Best Fitness | Mean $\pm$ Std | Median | Vi phạm ($diam > s$) | Độ đa dạng | Khả thi ($100\%$) | Thời gian (s) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **PPO-AOS** | **10** | **10.00** | 10.00 $\pm$ 0.00 | 10.0 | 0.00 | 0.842 |  Đạt chuẩn | 4.54s |
| MAB-AOS | 10 | 10.00 | 10.00 $\pm$ 0.00 | 10.0 | 0.00 | 0.900 |  Đạt chuẩn | 4.02s |
| Greedy-AOS | 10 | 10.00 | 10.00 $\pm$ 0.00 | 10.0 | 0.00 | 0.895 |  Đạt chuẩn | 3.98s |
| I-MSM | 10 | 10.00 | 10.50 $\pm$ 0.56 | 10.0 | 0.00 | 0.000 |  Đạt chuẩn | 1.39s |
| CCA | 10 | 10.00 | 10.06 $\pm$ 0.24 | 10.0 | 0.00 | 0.000 |  Đạt chuẩn | 0.10s |
| No-RL | 10 | 10.00 | 10.00 $\pm$ 0.00 | 10.0 | 0.00 | 0.853 |  Đạt chuẩn | 3.95s |
| Fixed | 10 | 10.00 | 10.00 $\pm$ 0.00 | 10.0 | 0.00 | 0.847 |  Đạt chuẩn | 2.87s |
| Random | 10 | 10.00 | 10.00 $\pm$ 0.00 | 10.0 | 0.00 | 0.853 |  Đạt chuẩn | 3.42s |

---

## 2. Cấu Trúc Nghiệm Tốt Nhất Trong Lần Chạy (Best Solution Clusters)
- **Thuật toán đạt Best:** `PPO-AOS` (Cover = `10` clubs, Fitness = `10.00`)
- **Kích thước các cụm ($s$-clubs):** `[10, 22, 7, 10, 5, 2, 2, 15, 3, 1]`
- **Số thế hệ tiến hóa:** `101` generations

### Chi tiết các cụm $s$-club thành phần:
- **Club 6** (Size = 10 đỉnh): `[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]`
- **Club 2** (Size = 22 đỉnh): `[10, 11, 12, 13, 14, 15, 23, 27, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 43, 44, 70, 72]`
- **Club 5** (Size = 7 đỉnh): `[16, 17, 18, 19, 20, 21, 22]`
- **Club 4** (Size = 10 đỉnh): `[24, 25, 39, 40, 41, 42, 68, 69, 71, 75]`
- **Club 3** (Size = 5 đỉnh): `[26, 49, 50, 54, 56]`
- **Club 10** (Size = 2 đỉnh): `[28, 45]`
- **Club 7** (Size = 2 đỉnh): `[46, 47]`
- **Club 9** (Size = 15 đỉnh): `[48, 55, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 73, 74, 76]`
- **Club 8** (Size = 3 đỉnh): `[51, 52, 53]`
- **Club 1** (Size = 1 đỉnh): `[67]`

---
*File được sinh tự động bởi hệ thống EVO-RL MSCC Research Framework.*
