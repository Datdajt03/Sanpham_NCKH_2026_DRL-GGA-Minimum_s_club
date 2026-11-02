# Báo Cáo Kết Quả Thực Nghiệm: Seed #11 (Seed = `11223344`)

**Tập dữ liệu đồ thị:** `lesmis` ($|V| = 77$, $|E| = 262$, Density = $0.0895$, $s = 2$)  
**Hạt giống cố định (Seed Value):** `11223344` (Lần chạy 11/20 từ `seedun.md`)  
**Thời gian thực thi:** `2026-09-13 11:47:40`  
**Môi trường tính toán:** `Hybrid Co-Processing [CPU: 12 Cores song song (GA/C++ igraph) + GPU: NVIDIA GeForce RTX 3050 Laptop GPU (PPO Tensor Cores)]`  

---

## 1. Bảng Thống Kê Hiệu Năng Chi Tiết Các Thuật Toán (Seed #11)

| Chiến lược / Thuật toán | Best Cover (Min) | Best Fitness | Mean $\pm$ Std | Median | Vi phạm ($diam > s$) | Độ đa dạng | Khả thi ($100\%$) | Thời gian (s) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **PPO-AOS** | **10** | **10.00** | 10.01 $\pm$ 0.10 | 10.0 | 0.00 | 0.865 |  Đạt chuẩn | 4.94s |
| MAB-AOS | 10 | 10.00 | 10.04 $\pm$ 0.19 | 10.0 | 0.00 | 0.831 |  Đạt chuẩn | 4.24s |
| Greedy-AOS | 10 | 10.00 | 10.01 $\pm$ 0.10 | 10.0 | 0.00 | 0.832 |  Đạt chuẩn | 4.01s |
| I-MSM | 10 | 10.00 | 10.16 $\pm$ 0.36 | 10.0 | 0.00 | 0.000 |  Đạt chuẩn | 0.89s |
| CCA | 10 | 10.00 | 10.00 $\pm$ 0.00 | 10.0 | 0.00 | 0.000 |  Đạt chuẩn | 0.10s |
| No-RL | 10 | 10.00 | 10.01 $\pm$ 0.10 | 10.0 | 0.00 | 0.819 |  Đạt chuẩn | 4.37s |
| Fixed | 10 | 10.00 | 10.02 $\pm$ 0.14 | 10.0 | 0.00 | 0.873 |  Đạt chuẩn | 2.93s |
| Random | 10 | 10.00 | 10.01 $\pm$ 0.10 | 10.0 | 0.00 | 0.819 |  Đạt chuẩn | 4.22s |

---

## 2. Cấu Trúc Nghiệm Tốt Nhất Trong Lần Chạy (Best Solution Clusters)
- **Thuật toán đạt Best:** `PPO-AOS` (Cover = `10` clubs, Fitness = `10.00`)
- **Kích thước các cụm ($s$-clubs):** `[9, 24, 8, 6, 19, 1, 2, 4, 3, 1]`
- **Số thế hệ tiến hóa:** `102` generations

### Chi tiết các cụm $s$-club thành phần:
- **Club 8** (Size = 9 đỉnh): `[0, 1, 2, 4, 5, 6, 7, 8, 9]`
- **Club 2** (Size = 24 đỉnh): `[3, 10, 11, 12, 13, 14, 15, 24, 26, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 43, 44, 70, 72]`
- **Club 5** (Size = 8 đỉnh): `[16, 17, 18, 19, 20, 21, 22, 23]`
- **Club 3** (Size = 6 đỉnh): `[25, 39, 40, 41, 42, 55]`
- **Club 1** (Size = 19 đỉnh): `[27, 48, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 68, 69, 71, 73, 74, 75, 76]`
- **Club 9** (Size = 1 đỉnh): `[45]`
- **Club 7** (Size = 2 đỉnh): `[46, 47]`
- **Club 6** (Size = 4 đỉnh): `[49, 50, 54, 56]`
- **Club 4** (Size = 3 đỉnh): `[51, 52, 53]`
- **Club 10** (Size = 1 đỉnh): `[67]`

---
*File được sinh tự động bởi hệ thống EVO-RL MSCC Research Framework.*
