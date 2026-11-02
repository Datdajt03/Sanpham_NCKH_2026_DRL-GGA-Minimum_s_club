# Báo Cáo Kết Quả Thực Nghiệm: Seed #20 (Seed = `86088608`)

**Tập dữ liệu đồ thị:** `dolphins` ($|V| = 62$, $|E| = 159$, Density = $0.0841$, $s = 2$)  
**Hạt giống cố định (Seed Value):** `86088608` (Lần chạy 20/20 từ `seedun.md`)  
**Thời gian thực thi:** `2026-09-13 11:46:30`  
**Môi trường tính toán:** `Hybrid Co-Processing [CPU: 12 Cores song song (GA/C++ igraph) + GPU: NVIDIA GeForce RTX 3050 Laptop GPU (PPO Tensor Cores)]`  

---

## 1. Bảng Thống Kê Hiệu Năng Chi Tiết Các Thuật Toán (Seed #20)

| Chiến lược / Thuật toán | Best Cover (Min) | Best Fitness | Mean $\pm$ Std | Median | Vi phạm ($diam > s$) | Độ đa dạng | Khả thi ($100\%$) | Thời gian (s) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **PPO-AOS** | **13** | **13.00** | 13.39 $\pm$ 0.80 | 13.0 | 0.00 | 0.850 |  Đạt chuẩn | 4.81s |
| MAB-AOS | 13 | 13.00 | 13.29 $\pm$ 0.76 | 13.0 | 0.00 | 0.876 |  Đạt chuẩn | 3.69s |
| Greedy-AOS | 13 | 13.00 | 13.32 $\pm$ 0.77 | 13.0 | 0.00 | 0.901 |  Đạt chuẩn | 3.89s |
| I-MSM | 14 | 14.00 | 14.12 $\pm$ 0.47 | 14.0 | 0.00 | 0.000 |  Đạt chuẩn | 0.46s |
| CCA | 14 | 14.00 | 14.00 $\pm$ 0.00 | 14.0 | 0.00 | 0.000 |  Đạt chuẩn | 0.10s |
| No-RL | 13 | 13.00 | 13.32 $\pm$ 0.72 | 13.0 | 0.00 | 0.680 |  Đạt chuẩn | 4.07s |
| Fixed | 13 | 13.00 | 13.30 $\pm$ 0.74 | 13.0 | 0.00 | 0.899 |  Đạt chuẩn | 2.94s |
| Random | 13 | 13.00 | 13.32 $\pm$ 0.72 | 13.0 | 0.00 | 0.680 |  Đạt chuẩn | 2.08s |

---

## 2. Cấu Trúc Nghiệm Tốt Nhất Trong Lần Chạy (Best Solution Clusters)
- **Thuật toán đạt Best:** `PPO-AOS` (Cover = `13` clubs, Fitness = `13.00`)
- **Kích thước các cụm ($s$-clubs):** `[7, 5, 3, 5, 10, 2, 8, 8, 5, 4, 2, 1, 2]`
- **Số thế hệ tiến hóa:** `130` generations

### Chi tiết các cụm $s$-club thành phần:
- **Club 8** (Size = 7 đỉnh): `[0, 10, 20, 28, 30, 42, 47]`
- **Club 9** (Size = 5 đỉnh): `[1, 7, 19, 26, 27]`
- **Club 10** (Size = 3 đỉnh): `[2, 53, 61]`
- **Club 12** (Size = 5 đỉnh): `[3, 8, 15, 36, 59]`
- **Club 2** (Size = 10 đỉnh): `[4, 11, 18, 21, 23, 24, 29, 45, 51, 55]`
- **Club 3** (Size = 2 đỉnh): `[5, 56]`
- **Club 4** (Size = 8 đỉnh): `[6, 9, 13, 39, 41, 48, 54, 57]`
- **Club 7** (Size = 8 đỉnh): `[12, 14, 33, 34, 37, 40, 43, 50]`
- **Club 11** (Size = 5 đỉnh): `[16, 38, 44, 52, 58]`
- **Club 5** (Size = 4 đỉnh): `[17, 22, 25, 31]`
- **Club 6** (Size = 2 đỉnh): `[32, 60]`
- **Club 13** (Size = 1 đỉnh): `[35]`
- **Club 1** (Size = 2 đỉnh): `[46, 49]`

---
*File được sinh tự động bởi hệ thống EVO-RL MSCC Research Framework.*
