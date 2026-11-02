# Báo Cáo Kết Quả Thực Nghiệm: Seed #13 (Seed = `13572468`)

**Tập dữ liệu đồ thị:** `dolphins` ($|V| = 62$, $|E| = 159$, Density = $0.0841$, $s = 2$)  
**Hạt giống cố định (Seed Value):** `13572468` (Lần chạy 13/20 từ `seedun.md`)  
**Thời gian thực thi:** `2026-09-13 11:46:27`  
**Môi trường tính toán:** `Hybrid Co-Processing [CPU: 12 Cores song song (GA/C++ igraph) + GPU: NVIDIA GeForce RTX 3050 Laptop GPU (PPO Tensor Cores)]`  

---

## 1. Bảng Thống Kê Hiệu Năng Chi Tiết Các Thuật Toán (Seed #13)

| Chiến lược / Thuật toán | Best Cover (Min) | Best Fitness | Mean $\pm$ Std | Median | Vi phạm ($diam > s$) | Độ đa dạng | Khả thi ($100\%$) | Thời gian (s) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **PPO-AOS** | **14** | **14.00** | 14.09 $\pm$ 0.29 | 14.0 | 0.00 | 0.926 |  Đạt chuẩn | 4.64s |
| MAB-AOS | 13 | 13.00 | 13.15 $\pm$ 0.52 | 13.0 | 0.00 | 0.865 |  Đạt chuẩn | 3.55s |
| Greedy-AOS | 13 | 13.00 | 13.16 $\pm$ 0.43 | 13.0 | 0.00 | 0.904 |  Đạt chuẩn | 3.71s |
| I-MSM | 16 | 16.00 | 16.00 $\pm$ 0.00 | 16.0 | 0.00 | 0.000 |  Đạt chuẩn | 0.43s |
| CCA | 14 | 14.00 | 14.48 $\pm$ 0.70 | 14.0 | 0.00 | 0.000 |  Đạt chuẩn | 0.16s |
| No-RL | 13 | 13.00 | 13.27 $\pm$ 0.58 | 13.0 | 0.00 | 0.889 |  Đạt chuẩn | 3.87s |
| Fixed | 13 | 13.00 | 13.33 $\pm$ 0.62 | 13.0 | 0.00 | 0.903 |  Đạt chuẩn | 3.42s |
| Random | 13 | 13.00 | 13.27 $\pm$ 0.58 | 13.0 | 0.00 | 0.889 |  Đạt chuẩn | 3.94s |

---

## 2. Cấu Trúc Nghiệm Tốt Nhất Trong Lần Chạy (Best Solution Clusters)
- **Thuật toán đạt Best:** `MAB-AOS` (Cover = `13` clubs, Fitness = `13.00`)
- **Kích thước các cụm ($s$-clubs):** `[6, 6, 3, 5, 11, 7, 5, 8, 5, 2, 1, 2, 1]`
- **Số thế hệ tiến hóa:** `109` generations

### Chi tiết các cụm $s$-club thành phần:
- **Club 6** (Size = 6 đỉnh): `[0, 10, 28, 30, 42, 47]`
- **Club 3** (Size = 6 đỉnh): `[1, 7, 19, 26, 27, 54]`
- **Club 9** (Size = 3 đỉnh): `[2, 53, 61]`
- **Club 5** (Size = 5 đỉnh): `[3, 8, 15, 36, 59]`
- **Club 2** (Size = 11 đỉnh): `[4, 11, 18, 21, 23, 24, 29, 45, 50, 51, 55]`
- **Club 4** (Size = 7 đỉnh): `[5, 6, 13, 39, 41, 48, 57]`
- **Club 7** (Size = 5 đỉnh): `[9, 17, 22, 25, 31]`
- **Club 10** (Size = 8 đỉnh): `[12, 14, 16, 33, 34, 37, 40, 43]`
- **Club 11** (Size = 5 đỉnh): `[20, 38, 44, 52, 58]`
- **Club 1** (Size = 2 đỉnh): `[32, 60]`
- **Club 12** (Size = 1 đỉnh): `[35]`
- **Club 8** (Size = 2 đỉnh): `[46, 49]`
- **Club 13** (Size = 1 đỉnh): `[56]`

---
*File được sinh tự động bởi hệ thống EVO-RL MSCC Research Framework.*
