# Báo Cáo Kết Quả Thực Nghiệm: Seed #19 (Seed = `64086408`)

**Tập dữ liệu đồ thị:** `dolphins` ($|V| = 62$, $|E| = 159$, Density = $0.0841$, $s = 2$)  
**Hạt giống cố định (Seed Value):** `64086408` (Lần chạy 19/20 từ `seedun.md`)  
**Thời gian thực thi:** `2026-09-13 11:46:29`  
**Môi trường tính toán:** `Hybrid Co-Processing [CPU: 12 Cores song song (GA/C++ igraph) + GPU: NVIDIA GeForce RTX 3050 Laptop GPU (PPO Tensor Cores)]`  

---

## 1. Bảng Thống Kê Hiệu Năng Chi Tiết Các Thuật Toán (Seed #19)

| Chiến lược / Thuật toán | Best Cover (Min) | Best Fitness | Mean $\pm$ Std | Median | Vi phạm ($diam > s$) | Độ đa dạng | Khả thi ($100\%$) | Thời gian (s) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **PPO-AOS** | **13** | **13.00** | 13.23 $\pm$ 0.67 | 13.0 | 0.00 | 0.872 |  Đạt chuẩn | 4.49s |
| MAB-AOS | 13 | 13.00 | 13.24 $\pm$ 0.65 | 13.0 | 0.00 | 0.898 |  Đạt chuẩn | 3.91s |
| Greedy-AOS | 13 | 13.00 | 13.27 $\pm$ 0.74 | 13.0 | 0.00 | 0.780 |  Đạt chuẩn | 3.66s |
| I-MSM | 14 | 14.00 | 14.81 $\pm$ 0.98 | 14.5 | 0.00 | 0.000 |  Đạt chuẩn | 0.86s |
| CCA | 14 | 14.00 | 14.60 $\pm$ 0.71 | 14.0 | 0.00 | 0.000 |  Đạt chuẩn | 0.21s |
| No-RL | 13 | 13.00 | 13.32 $\pm$ 0.76 | 13.0 | 0.00 | 0.944 |  Đạt chuẩn | 3.95s |
| Fixed | 13 | 13.00 | 13.34 $\pm$ 0.83 | 13.0 | 0.00 | 0.903 |  Đạt chuẩn | 3.44s |
| Random | 13 | 13.00 | 13.32 $\pm$ 0.76 | 13.0 | 0.00 | 0.944 |  Đạt chuẩn | 2.59s |

---

## 2. Cấu Trúc Nghiệm Tốt Nhất Trong Lần Chạy (Best Solution Clusters)
- **Thuật toán đạt Best:** `PPO-AOS` (Cover = `13` clubs, Fitness = `13.00`)
- **Kích thước các cụm ($s$-clubs):** `[6, 7, 3, 6, 8, 7, 8, 6, 4, 2, 3, 1, 1]`
- **Số thế hệ tiến hóa:** `116` generations

### Chi tiết các cụm $s$-club thành phần:
- **Club 9** (Size = 6 đỉnh): `[0, 10, 28, 30, 42, 47]`
- **Club 12** (Size = 7 đỉnh): `[1, 7, 19, 26, 27, 41, 54]`
- **Club 4** (Size = 3 đỉnh): `[2, 53, 61]`
- **Club 10** (Size = 6 đỉnh): `[3, 8, 15, 36, 45, 59]`
- **Club 11** (Size = 8 đỉnh): `[4, 11, 18, 23, 24, 29, 51, 55]`
- **Club 5** (Size = 7 đỉnh): `[5, 6, 9, 13, 39, 48, 57]`
- **Club 13** (Size = 8 đỉnh): `[12, 14, 21, 33, 37, 40, 43, 50]`
- **Club 6** (Size = 6 đỉnh): `[16, 20, 38, 44, 52, 58]`
- **Club 7** (Size = 4 đỉnh): `[17, 22, 25, 31]`
- **Club 2** (Size = 2 đỉnh): `[32, 60]`
- **Club 8** (Size = 3 đỉnh): `[34, 46, 49]`
- **Club 1** (Size = 1 đỉnh): `[35]`
- **Club 3** (Size = 1 đỉnh): `[56]`

---
*File được sinh tự động bởi hệ thống EVO-RL MSCC Research Framework.*
