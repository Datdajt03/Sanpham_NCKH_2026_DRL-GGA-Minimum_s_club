# Báo Cáo Kết Quả Thực Nghiệm: Seed #18 (Seed = `20252026`)

**Tập dữ liệu đồ thị:** `dolphins` ($|V| = 62$, $|E| = 159$, Density = $0.0841$, $s = 2$)  
**Hạt giống cố định (Seed Value):** `20252026` (Lần chạy 18/20 từ `seedun.md`)  
**Thời gian thực thi:** `2026-09-13 11:46:28`  
**Môi trường tính toán:** `Hybrid Co-Processing [CPU: 12 Cores song song (GA/C++ igraph) + GPU: NVIDIA GeForce RTX 3050 Laptop GPU (PPO Tensor Cores)]`  

---

## 1. Bảng Thống Kê Hiệu Năng Chi Tiết Các Thuật Toán (Seed #18)

| Chiến lược / Thuật toán | Best Cover (Min) | Best Fitness | Mean $\pm$ Std | Median | Vi phạm ($diam > s$) | Độ đa dạng | Khả thi ($100\%$) | Thời gian (s) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **PPO-AOS** | **13** | **13.00** | 13.28 $\pm$ 0.68 | 13.0 | 0.00 | 0.852 |  Đạt chuẩn | 4.73s |
| MAB-AOS | 13 | 13.00 | 13.34 $\pm$ 0.67 | 13.0 | 0.00 | 0.838 |  Đạt chuẩn | 4.37s |
| Greedy-AOS | 13 | 13.00 | 13.25 $\pm$ 0.67 | 13.0 | 0.00 | 0.911 |  Đạt chuẩn | 3.62s |
| I-MSM | 15 | 15.00 | 15.00 $\pm$ 0.00 | 15.0 | 0.00 | 0.000 |  Đạt chuẩn | 0.43s |
| CCA | 14 | 14.00 | 14.27 $\pm$ 0.45 | 14.0 | 0.00 | 0.000 |  Đạt chuẩn | 0.13s |
| No-RL | 14 | 14.00 | 14.09 $\pm$ 0.37 | 14.0 | 0.00 | 0.823 |  Đạt chuẩn | 3.62s |
| Fixed | 13 | 13.00 | 13.18 $\pm$ 0.57 | 13.0 | 0.00 | 0.876 |  Đạt chuẩn | 3.02s |
| Random | 14 | 14.00 | 14.09 $\pm$ 0.37 | 14.0 | 0.00 | 0.823 |  Đạt chuẩn | 3.26s |

---

## 2. Cấu Trúc Nghiệm Tốt Nhất Trong Lần Chạy (Best Solution Clusters)
- **Thuật toán đạt Best:** `PPO-AOS` (Cover = `13` clubs, Fitness = `13.00`)
- **Kích thước các cụm ($s$-clubs):** `[6, 7, 3, 6, 6, 3, 5, 8, 3, 4, 5, 3, 3]`
- **Số thế hệ tiến hóa:** `123` generations

### Chi tiết các cụm $s$-club thành phần:
- **Club 7** (Size = 6 đỉnh): `[0, 10, 28, 30, 42, 47]`
- **Club 6** (Size = 7 đỉnh): `[1, 7, 19, 26, 27, 41, 54]`
- **Club 2** (Size = 3 đỉnh): `[2, 53, 61]`
- **Club 4** (Size = 6 đỉnh): `[3, 8, 15, 36, 45, 59]`
- **Club 8** (Size = 6 đỉnh): `[4, 11, 21, 23, 51, 55]`
- **Club 9** (Size = 3 đỉnh): `[5, 6, 56]`
- **Club 3** (Size = 5 đỉnh): `[9, 17, 22, 25, 31]`
- **Club 11** (Size = 8 đỉnh): `[12, 14, 16, 33, 34, 37, 40, 50]`
- **Club 10** (Size = 3 đỉnh): `[13, 32, 60]`
- **Club 1** (Size = 4 đỉnh): `[18, 24, 29, 35]`
- **Club 5** (Size = 5 đỉnh): `[20, 38, 44, 52, 58]`
- **Club 12** (Size = 3 đỉnh): `[39, 48, 57]`
- **Club 13** (Size = 3 đỉnh): `[43, 46, 49]`

---
*File được sinh tự động bởi hệ thống EVO-RL MSCC Research Framework.*
