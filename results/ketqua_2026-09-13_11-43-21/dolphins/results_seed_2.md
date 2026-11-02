# Báo Cáo Kết Quả Thực Nghiệm: Seed #02 (Seed = `21042026`)

**Tập dữ liệu đồ thị:** `dolphins` ($|V| = 62$, $|E| = 159$, Density = $0.0841$, $s = 2$)  
**Hạt giống cố định (Seed Value):** `21042026` (Lần chạy 02/20 từ `seedun.md`)  
**Thời gian thực thi:** `2026-09-13 11:46:03`  
**Môi trường tính toán:** `Hybrid Co-Processing [CPU: 12 Cores song song (GA/C++ igraph) + GPU: NVIDIA GeForce RTX 3050 Laptop GPU (PPO Tensor Cores)]`  

---

## 1. Bảng Thống Kê Hiệu Năng Chi Tiết Các Thuật Toán (Seed #2)

| Chiến lược / Thuật toán | Best Cover (Min) | Best Fitness | Mean $\pm$ Std | Median | Vi phạm ($diam > s$) | Độ đa dạng | Khả thi ($100\%$) | Thời gian (s) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **PPO-AOS** | **13** | **13.00** | 13.10 $\pm$ 0.41 | 13.0 | 0.00 | 0.876 |  Đạt chuẩn | 5.77s |
| MAB-AOS | 13 | 13.00 | 13.15 $\pm$ 0.49 | 13.0 | 0.00 | 0.892 |  Đạt chuẩn | 3.69s |
| Greedy-AOS | 14 | 14.00 | 14.04 $\pm$ 0.19 | 14.0 | 0.00 | 0.883 |  Đạt chuẩn | 3.43s |
| I-MSM | 15 | 15.00 | 15.16 $\pm$ 0.36 | 15.0 | 0.00 | 0.000 |  Đạt chuẩn | 0.48s |
| CCA | 14 | 14.00 | 14.45 $\pm$ 0.92 | 14.0 | 0.00 | 0.000 |  Đạt chuẩn | 0.13s |
| No-RL | 13 | 13.00 | 13.31 $\pm$ 0.53 | 13.0 | 0.00 | 0.653 |  Đạt chuẩn | 4.31s |
| Fixed | 13 | 13.00 | 13.11 $\pm$ 0.34 | 13.0 | 0.00 | 0.928 |  Đạt chuẩn | 2.92s |
| Random | 13 | 13.00 | 13.31 $\pm$ 0.53 | 13.0 | 0.00 | 0.653 |  Đạt chuẩn | 4.31s |

---

## 2. Cấu Trúc Nghiệm Tốt Nhất Trong Lần Chạy (Best Solution Clusters)
- **Thuật toán đạt Best:** `PPO-AOS` (Cover = `13` clubs, Fitness = `13.00`)
- **Kích thước các cụm ($s$-clubs):** `[6, 6, 4, 4, 7, 3, 7, 7, 2, 7, 4, 2, 3]`
- **Số thế hệ tiến hóa:** `108` generations

### Chi tiết các cụm $s$-club thành phần:
- **Club 6** (Size = 6 đỉnh): `[0, 7, 30, 40, 42, 47]`
- **Club 2** (Size = 6 đỉnh): `[1, 19, 26, 27, 28, 36]`
- **Club 7** (Size = 4 đỉnh): `[2, 37, 53, 61]`
- **Club 8** (Size = 4 đỉnh): `[3, 8, 15, 59]`
- **Club 5** (Size = 7 đỉnh): `[4, 11, 23, 45, 50, 51, 55]`
- **Club 9** (Size = 3 đỉnh): `[5, 6, 56]`
- **Club 10** (Size = 7 đỉnh): `[9, 13, 39, 41, 48, 54, 57]`
- **Club 3** (Size = 7 đỉnh): `[10, 18, 21, 24, 29, 35, 43]`
- **Club 11** (Size = 2 đỉnh): `[12, 33]`
- **Club 1** (Size = 7 đỉnh): `[14, 16, 20, 38, 44, 52, 58]`
- **Club 4** (Size = 4 đỉnh): `[17, 22, 25, 31]`
- **Club 12** (Size = 2 đỉnh): `[32, 60]`
- **Club 13** (Size = 3 đỉnh): `[34, 46, 49]`

---
*File được sinh tự động bởi hệ thống EVO-RL MSCC Research Framework.*
