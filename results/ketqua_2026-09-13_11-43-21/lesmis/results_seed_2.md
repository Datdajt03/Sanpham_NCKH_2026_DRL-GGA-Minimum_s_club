# Báo Cáo Kết Quả Thực Nghiệm: Seed #02 (Seed = `21042026`)

**Tập dữ liệu đồ thị:** `lesmis` ($|V| = 77$, $|E| = 262$, Density = $0.0895$, $s = 2$)  
**Hạt giống cố định (Seed Value):** `21042026` (Lần chạy 02/20 từ `seedun.md`)  
**Thời gian thực thi:** `2026-09-13 11:47:17`  
**Môi trường tính toán:** `Hybrid Co-Processing [CPU: 12 Cores song song (GA/C++ igraph) + GPU: NVIDIA GeForce RTX 3050 Laptop GPU (PPO Tensor Cores)]`  

---

## 1. Bảng Thống Kê Hiệu Năng Chi Tiết Các Thuật Toán (Seed #2)

| Chiến lược / Thuật toán | Best Cover (Min) | Best Fitness | Mean $\pm$ Std | Median | Vi phạm ($diam > s$) | Độ đa dạng | Khả thi ($100\%$) | Thời gian (s) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **PPO-AOS** | **10** | **10.00** | 10.02 $\pm$ 0.14 | 10.0 | 0.00 | 0.881 |  Đạt chuẩn | 6.63s |
| MAB-AOS | 10 | 10.00 | 10.06 $\pm$ 0.25 | 10.0 | 0.00 | 0.825 |  Đạt chuẩn | 4.53s |
| Greedy-AOS | 10 | 10.00 | 10.07 $\pm$ 0.26 | 10.0 | 0.00 | 0.890 |  Đạt chuẩn | 4.18s |
| I-MSM | 10 | 10.00 | 10.00 $\pm$ 0.00 | 10.0 | 0.00 | 0.000 |  Đạt chuẩn | 0.77s |
| CCA | 10 | 10.00 | 10.38 $\pm$ 0.56 | 10.0 | 0.00 | 0.000 |  Đạt chuẩn | 0.13s |
| No-RL | 10 | 10.00 | 10.03 $\pm$ 0.17 | 10.0 | 0.00 | 0.849 |  Đạt chuẩn | 4.44s |
| Fixed | 10 | 10.00 | 10.01 $\pm$ 0.10 | 10.0 | 0.00 | 0.862 |  Đạt chuẩn | 2.78s |
| Random | 10 | 10.00 | 10.03 $\pm$ 0.17 | 10.0 | 0.00 | 0.849 |  Đạt chuẩn | 4.31s |

---

## 2. Cấu Trúc Nghiệm Tốt Nhất Trong Lần Chạy (Best Solution Clusters)
- **Thuật toán đạt Best:** `PPO-AOS` (Cover = `10` clubs, Fitness = `10.00`)
- **Kích thước các cụm ($s$-clubs):** `[10, 21, 7, 11, 3, 2, 15, 4, 3, 1]`
- **Số thế hệ tiến hóa:** `103` generations

### Chi tiết các cụm $s$-club thành phần:
- **Club 4** (Size = 10 đỉnh): `[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]`
- **Club 9** (Size = 21 đỉnh): `[10, 11, 12, 13, 14, 15, 24, 27, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 43, 70, 72]`
- **Club 3** (Size = 7 đỉnh): `[16, 17, 18, 19, 20, 21, 22]`
- **Club 2** (Size = 11 đỉnh): `[23, 25, 26, 39, 40, 41, 42, 68, 69, 71, 75]`
- **Club 6** (Size = 3 đỉnh): `[28, 44, 45]`
- **Club 7** (Size = 2 đỉnh): `[46, 47]`
- **Club 1** (Size = 15 đỉnh): `[48, 55, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 73, 74, 76]`
- **Club 8** (Size = 4 đỉnh): `[49, 50, 54, 56]`
- **Club 10** (Size = 3 đỉnh): `[51, 52, 53]`
- **Club 5** (Size = 1 đỉnh): `[67]`

---
*File được sinh tự động bởi hệ thống EVO-RL MSCC Research Framework.*
