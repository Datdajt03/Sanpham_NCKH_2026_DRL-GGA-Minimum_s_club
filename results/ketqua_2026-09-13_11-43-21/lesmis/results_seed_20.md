# Báo Cáo Kết Quả Thực Nghiệm: Seed #20 (Seed = `86088608`)

**Tập dữ liệu đồ thị:** `lesmis` ($|V| = 77$, $|E| = 262$, Density = $0.0895$, $s = 2$)  
**Hạt giống cố định (Seed Value):** `86088608` (Lần chạy 20/20 từ `seedun.md`)  
**Thời gian thực thi:** `2026-09-13 11:47:40`  
**Môi trường tính toán:** `Hybrid Co-Processing [CPU: 12 Cores song song (GA/C++ igraph) + GPU: NVIDIA GeForce RTX 3050 Laptop GPU (PPO Tensor Cores)]`  

---

## 1. Bảng Thống Kê Hiệu Năng Chi Tiết Các Thuật Toán (Seed #20)

| Chiến lược / Thuật toán | Best Cover (Min) | Best Fitness | Mean $\pm$ Std | Median | Vi phạm ($diam > s$) | Độ đa dạng | Khả thi ($100\%$) | Thời gian (s) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **PPO-AOS** | **10** | **10.00** | 10.00 $\pm$ 0.00 | 10.0 | 0.00 | 0.813 |  Đạt chuẩn | 4.45s |
| MAB-AOS | 10 | 10.00 | 10.00 $\pm$ 0.00 | 10.0 | 0.00 | 0.795 |  Đạt chuẩn | 3.89s |
| Greedy-AOS | 10 | 10.00 | 10.00 $\pm$ 0.00 | 10.0 | 0.00 | 0.867 |  Đạt chuẩn | 3.76s |
| I-MSM | 10 | 10.00 | 10.20 $\pm$ 0.40 | 10.0 | 0.00 | 0.000 |  Đạt chuẩn | 0.92s |
| CCA | 10 | 10.00 | 10.06 $\pm$ 0.24 | 10.0 | 0.00 | 0.000 |  Đạt chuẩn | 0.10s |
| No-RL | 10 | 10.00 | 10.00 $\pm$ 0.00 | 10.0 | 0.00 | 0.807 |  Đạt chuẩn | 3.77s |
| Fixed | 10 | 10.00 | 10.00 $\pm$ 0.00 | 10.0 | 0.00 | 0.888 |  Đạt chuẩn | 2.81s |
| Random | 10 | 10.00 | 10.00 $\pm$ 0.00 | 10.0 | 0.00 | 0.807 |  Đạt chuẩn | 3.22s |

---

## 2. Cấu Trúc Nghiệm Tốt Nhất Trong Lần Chạy (Best Solution Clusters)
- **Thuật toán đạt Best:** `PPO-AOS` (Cover = `10` clubs, Fitness = `10.00`)
- **Kích thước các cụm ($s$-clubs):** `[9, 26, 8, 7, 3, 2, 12, 4, 3, 3]`
- **Số thế hệ tiến hóa:** `101` generations

### Chi tiết các cụm $s$-club thành phần:
- **Club 2** (Size = 9 đỉnh): `[0, 1, 3, 4, 5, 6, 7, 8, 9]`
- **Club 6** (Size = 26 đỉnh): `[2, 10, 11, 12, 13, 14, 15, 23, 24, 27, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 43, 68, 69, 70, 71, 72]`
- **Club 10** (Size = 8 đỉnh): `[16, 17, 18, 19, 20, 21, 22, 26]`
- **Club 8** (Size = 7 đỉnh): `[25, 39, 40, 41, 42, 55, 75]`
- **Club 3** (Size = 3 đỉnh): `[28, 44, 45]`
- **Club 5** (Size = 2 đỉnh): `[46, 47]`
- **Club 1** (Size = 12 đỉnh): `[48, 58, 59, 60, 61, 62, 63, 64, 66, 73, 74, 76]`
- **Club 4** (Size = 4 đỉnh): `[49, 50, 54, 56]`
- **Club 7** (Size = 3 đỉnh): `[51, 52, 53]`
- **Club 9** (Size = 3 đỉnh): `[57, 65, 67]`

---
*File được sinh tự động bởi hệ thống EVO-RL MSCC Research Framework.*
