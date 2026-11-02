# Báo Cáo Kết Quả Thực Nghiệm: Seed #17 (Seed = `52013140`)

**Tập dữ liệu đồ thị:** `dolphins` ($|V| = 62$, $|E| = 159$, Density = $0.0841$, $s = 2$)  
**Hạt giống cố định (Seed Value):** `52013140` (Lần chạy 17/20 từ `seedun.md`)  
**Thời gian thực thi:** `2026-09-13 11:46:27`  
**Môi trường tính toán:** `Hybrid Co-Processing [CPU: 12 Cores song song (GA/C++ igraph) + GPU: NVIDIA GeForce RTX 3050 Laptop GPU (PPO Tensor Cores)]`  

---

## 1. Bảng Thống Kê Hiệu Năng Chi Tiết Các Thuật Toán (Seed #17)

| Chiến lược / Thuật toán | Best Cover (Min) | Best Fitness | Mean $\pm$ Std | Median | Vi phạm ($diam > s$) | Độ đa dạng | Khả thi ($100\%$) | Thời gian (s) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **PPO-AOS** | **14** | **14.00** | 14.08 $\pm$ 0.27 | 14.0 | 0.00 | 0.891 |  Đạt chuẩn | 4.51s |
| MAB-AOS | 14 | 14.00 | 14.05 $\pm$ 0.21 | 14.0 | 0.00 | 0.804 |  Đạt chuẩn | 3.43s |
| Greedy-AOS | 14 | 14.00 | 14.06 $\pm$ 0.23 | 14.0 | 0.00 | 0.877 |  Đạt chuẩn | 3.52s |
| I-MSM | 14 | 14.00 | 14.62 $\pm$ 0.76 | 14.0 | 0.00 | 0.000 |  Đạt chuẩn | 0.76s |
| CCA | 14 | 14.00 | 14.37 $\pm$ 0.87 | 14.0 | 0.00 | 0.000 |  Đạt chuẩn | 0.12s |
| No-RL | 14 | 14.00 | 14.03 $\pm$ 0.17 | 14.0 | 0.00 | 0.868 |  Đạt chuẩn | 3.41s |
| Fixed | 14 | 14.00 | 14.08 $\pm$ 0.27 | 14.0 | 0.00 | 0.923 |  Đạt chuẩn | 3.21s |
| Random | 14 | 14.00 | 14.03 $\pm$ 0.17 | 14.0 | 0.00 | 0.868 |  Đạt chuẩn | 3.39s |

---

## 2. Cấu Trúc Nghiệm Tốt Nhất Trong Lần Chạy (Best Solution Clusters)
- **Thuật toán đạt Best:** `PPO-AOS` (Cover = `14` clubs, Fitness = `14.00`)
- **Kích thước các cụm ($s$-clubs):** `[6, 5, 3, 6, 10, 7, 2, 3, 6, 5, 5, 2, 1, 1]`
- **Số thế hệ tiến hóa:** `110` generations

### Chi tiết các cụm $s$-club thành phần:
- **Club 8** (Size = 6 đỉnh): `[0, 10, 15, 40, 42, 47]`
- **Club 3** (Size = 5 đỉnh): `[1, 19, 26, 41, 54]`
- **Club 1** (Size = 3 đỉnh): `[2, 53, 61]`
- **Club 6** (Size = 6 đỉnh): `[3, 8, 20, 28, 36, 59]`
- **Club 2** (Size = 10 đỉnh): `[4, 11, 18, 23, 24, 29, 45, 50, 51, 55]`
- **Club 9** (Size = 7 đỉnh): `[5, 6, 9, 13, 39, 48, 57]`
- **Club 12** (Size = 2 đỉnh): `[7, 30]`
- **Club 7** (Size = 3 đỉnh): `[12, 21, 33]`
- **Club 5** (Size = 6 đỉnh): `[14, 34, 37, 43, 46, 49]`
- **Club 13** (Size = 5 đỉnh): `[16, 38, 44, 52, 58]`
- **Club 10** (Size = 5 đỉnh): `[17, 22, 25, 27, 31]`
- **Club 11** (Size = 2 đỉnh): `[32, 60]`
- **Club 4** (Size = 1 đỉnh): `[35]`
- **Club 14** (Size = 1 đỉnh): `[56]`

---
*File được sinh tự động bởi hệ thống EVO-RL MSCC Research Framework.*
