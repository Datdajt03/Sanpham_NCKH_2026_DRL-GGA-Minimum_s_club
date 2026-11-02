# Báo Cáo Kết Quả Thực Nghiệm: Seed #07 (Seed = `20260421`)

**Tập dữ liệu đồ thị:** `lesmis` ($|V| = 77$, $|E| = 262$, Density = $0.0895$, $s = 2$)  
**Hạt giống cố định (Seed Value):** `20260421` (Lần chạy 07/20 từ `seedun.md`)  
**Thời gian thực thi:** `2026-09-13 11:47:17`  
**Môi trường tính toán:** `Hybrid Co-Processing [CPU: 12 Cores song song (GA/C++ igraph) + GPU: NVIDIA GeForce RTX 3050 Laptop GPU (PPO Tensor Cores)]`  

---

## 1. Bảng Thống Kê Hiệu Năng Chi Tiết Các Thuật Toán (Seed #7)

| Chiến lược / Thuật toán | Best Cover (Min) | Best Fitness | Mean $\pm$ Std | Median | Vi phạm ($diam > s$) | Độ đa dạng | Khả thi ($100\%$) | Thời gian (s) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **PPO-AOS** | **10** | **10.00** | 10.03 $\pm$ 0.17 | 10.0 | 0.00 | 0.884 |  Đạt chuẩn | 7.22s |
| MAB-AOS | 10 | 10.00 | 10.04 $\pm$ 0.19 | 10.0 | 0.00 | 0.868 |  Đạt chuẩn | 4.35s |
| Greedy-AOS | 10 | 10.00 | 10.05 $\pm$ 0.21 | 10.0 | 0.00 | 0.817 |  Đạt chuẩn | 3.96s |
| I-MSM | 10 | 10.00 | 10.29 $\pm$ 0.55 | 10.0 | 0.00 | 0.000 |  Đạt chuẩn | 0.93s |
| CCA | 10 | 10.00 | 10.00 $\pm$ 0.00 | 10.0 | 0.00 | 0.000 |  Đạt chuẩn | 0.10s |
| No-RL | 10 | 10.00 | 10.07 $\pm$ 0.26 | 10.0 | 0.00 | 0.900 |  Đạt chuẩn | 4.31s |
| Fixed | 10 | 10.00 | 10.02 $\pm$ 0.14 | 10.0 | 0.00 | 0.874 |  Đạt chuẩn | 2.79s |
| Random | 10 | 10.00 | 10.07 $\pm$ 0.26 | 10.0 | 0.00 | 0.900 |  Đạt chuẩn | 4.24s |

---

## 2. Cấu Trúc Nghiệm Tốt Nhất Trong Lần Chạy (Best Solution Clusters)
- **Thuật toán đạt Best:** `PPO-AOS` (Cover = `10` clubs, Fitness = `10.00`)
- **Kích thước các cụm ($s$-clubs):** `[10, 19, 8, 11, 5, 3, 2, 12, 3, 4]`
- **Số thế hệ tiến hóa:** `104` generations

### Chi tiết các cụm $s$-club thành phần:
- **Club 7** (Size = 10 đỉnh): `[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]`
- **Club 8** (Size = 19 đỉnh): `[10, 11, 12, 13, 14, 15, 27, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 43, 72]`
- **Club 3** (Size = 8 đỉnh): `[16, 17, 18, 19, 20, 21, 22, 23]`
- **Club 9** (Size = 11 đỉnh): `[24, 25, 39, 40, 41, 42, 68, 69, 70, 71, 75]`
- **Club 1** (Size = 5 đỉnh): `[26, 51, 52, 53, 54]`
- **Club 10** (Size = 3 đỉnh): `[28, 44, 45]`
- **Club 4** (Size = 2 đỉnh): `[46, 47]`
- **Club 6** (Size = 12 đỉnh): `[48, 55, 58, 59, 60, 61, 62, 64, 66, 73, 74, 76]`
- **Club 5** (Size = 3 đỉnh): `[49, 50, 56]`
- **Club 2** (Size = 4 đỉnh): `[57, 63, 65, 67]`

---
*File được sinh tự động bởi hệ thống EVO-RL MSCC Research Framework.*
