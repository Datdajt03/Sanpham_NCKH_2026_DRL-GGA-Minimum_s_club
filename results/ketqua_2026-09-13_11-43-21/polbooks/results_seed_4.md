# Báo Cáo Kết Quả Thực Nghiệm: Seed #04 (Seed = `26062026`)

**Tập dữ liệu đồ thị:** `polbooks` ($|V| = 105$, $|E| = 441$, Density = $0.0808$, $s = 2$)  
**Hạt giống cố định (Seed Value):** `26062026` (Lần chạy 04/20 từ `seedun.md`)  
**Thời gian thực thi:** `2026-09-13 11:48:39`  
**Môi trường tính toán:** `Hybrid Co-Processing [CPU: 12 Cores song song (GA/C++ igraph) + GPU: NVIDIA GeForce RTX 3050 Laptop GPU (PPO Tensor Cores)]`  

---

## 1. Bảng Thống Kê Hiệu Năng Chi Tiết Các Thuật Toán (Seed #4)

| Chiến lược / Thuật toán | Best Cover (Min) | Best Fitness | Mean $\pm$ Std | Median | Vi phạm ($diam > s$) | Độ đa dạng | Khả thi ($100\%$) | Thời gian (s) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **PPO-AOS** | **13** | **13.00** | 13.53 $\pm$ 0.77 | 13.0 | 0.00 | 0.865 |  Đạt chuẩn | 10.57s |
| MAB-AOS | 13 | 13.00 | 13.44 $\pm$ 0.81 | 13.0 | 0.00 | 0.764 |  Đạt chuẩn | 6.03s |
| Greedy-AOS | 13 | 13.00 | 13.39 $\pm$ 0.78 | 13.0 | 0.00 | 0.700 |  Đạt chuẩn | 6.10s |
| I-MSM | 13 | 13.00 | 13.58 $\pm$ 0.66 | 13.0 | 0.00 | 0.000 |  Đạt chuẩn | 1.99s |
| CCA | 15 | 15.00 | 15.12 $\pm$ 0.47 | 15.0 | 0.00 | 0.000 |  Đạt chuẩn | 0.18s |
| No-RL | 13 | 13.00 | 13.41 $\pm$ 0.80 | 13.0 | 0.00 | 0.889 |  Đạt chuẩn | 5.33s |
| Fixed | 13 | 13.00 | 13.22 $\pm$ 0.57 | 13.0 | 0.00 | 0.899 |  Đạt chuẩn | 4.78s |
| Random | 13 | 13.00 | 13.41 $\pm$ 0.80 | 13.0 | 0.00 | 0.889 |  Đạt chuẩn | 5.54s |

---

## 2. Cấu Trúc Nghiệm Tốt Nhất Trong Lần Chạy (Best Solution Clusters)
- **Thuật toán đạt Best:** `PPO-AOS` (Cover = `13` clubs, Fitness = `13.00`)
- **Kích thước các cụm ($s$-clubs):** `[7, 12, 10, 9, 9, 5, 12, 11, 5, 9, 7, 5, 4]`
- **Số thế hệ tiến hóa:** `171` generations

### Chi tiết các cụm $s$-club thành phần:
- **Club 9** (Size = 7 đỉnh): `[0, 2, 4, 5, 6, 7, 29]`
- **Club 5** (Size = 12 đỉnh): `[1, 3, 10, 11, 14, 15, 16, 18, 19, 21, 22, 25]`
- **Club 8** (Size = 10 đỉnh): `[8, 33, 34, 35, 37, 38, 39, 42, 43, 44]`
- **Club 1** (Size = 9 đỉnh): `[9, 20, 24, 26, 27, 40, 41, 45, 53]`
- **Club 4** (Size = 9 đỉnh): `[12, 17, 23, 32, 36, 46, 47, 54, 55]`
- **Club 10** (Size = 5 đỉnh): `[13, 48, 49, 56, 57]`
- **Club 7** (Size = 12 đỉnh): `[28, 70, 71, 72, 79, 80, 82, 87, 88, 89, 90, 92]`
- **Club 6** (Size = 11 đỉnh): `[30, 66, 75, 76, 81, 83, 84, 86, 96, 97, 100]`
- **Club 3** (Size = 5 đỉnh): `[31, 74, 78, 91, 98]`
- **Club 11** (Size = 9 đỉnh): `[50, 51, 52, 58, 64, 65, 68, 77, 85]`
- **Club 12** (Size = 7 đỉnh): `[59, 60, 62, 63, 73, 93, 99]`
- **Club 2** (Size = 5 đỉnh): `[61, 94, 95, 101, 102]`
- **Club 13** (Size = 4 đỉnh): `[67, 69, 103, 104]`

---
*File được sinh tự động bởi hệ thống EVO-RL MSCC Research Framework.*
