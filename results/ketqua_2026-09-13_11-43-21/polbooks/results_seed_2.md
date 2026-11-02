# Báo Cáo Kết Quả Thực Nghiệm: Seed #02 (Seed = `21042026`)

**Tập dữ liệu đồ thị:** `polbooks` ($|V| = 105$, $|E| = 441$, Density = $0.0808$, $s = 2$)  
**Hạt giống cố định (Seed Value):** `21042026` (Lần chạy 02/20 từ `seedun.md`)  
**Thời gian thực thi:** `2026-09-13 11:48:36`  
**Môi trường tính toán:** `Hybrid Co-Processing [CPU: 12 Cores song song (GA/C++ igraph) + GPU: NVIDIA GeForce RTX 3050 Laptop GPU (PPO Tensor Cores)]`  

---

## 1. Bảng Thống Kê Hiệu Năng Chi Tiết Các Thuật Toán (Seed #2)

| Chiến lược / Thuật toán | Best Cover (Min) | Best Fitness | Mean $\pm$ Std | Median | Vi phạm ($diam > s$) | Độ đa dạng | Khả thi ($100\%$) | Thời gian (s) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **PPO-AOS** | **13** | **13.00** | 13.30 $\pm$ 0.73 | 13.0 | 0.00 | 0.864 |  Đạt chuẩn | 8.13s |
| MAB-AOS | 13 | 13.00 | 13.38 $\pm$ 0.78 | 13.0 | 0.00 | 0.919 |  Đạt chuẩn | 5.95s |
| Greedy-AOS | 13 | 13.00 | 13.34 $\pm$ 0.83 | 13.0 | 0.00 | 0.880 |  Đạt chuẩn | 5.21s |
| I-MSM | 14 | 14.00 | 14.12 $\pm$ 0.47 | 14.0 | 0.00 | 0.000 |  Đạt chuẩn | 1.11s |
| CCA | 14 | 14.00 | 14.06 $\pm$ 0.24 | 14.0 | 0.00 | 0.000 |  Đạt chuẩn | 0.19s |
| No-RL | 13 | 13.00 | 13.42 $\pm$ 0.72 | 13.0 | 0.00 | 0.874 |  Đạt chuẩn | 6.32s |
| Fixed | 13 | 13.00 | 13.26 $\pm$ 0.71 | 13.0 | 0.00 | 0.880 |  Đạt chuẩn | 4.22s |
| Random | 13 | 13.00 | 13.42 $\pm$ 0.72 | 13.0 | 0.00 | 0.874 |  Đạt chuẩn | 6.32s |

---

## 2. Cấu Trúc Nghiệm Tốt Nhất Trong Lần Chạy (Best Solution Clusters)
- **Thuật toán đạt Best:** `PPO-AOS` (Cover = `13` clubs, Fitness = `13.00`)
- **Kích thước các cụm ($s$-clubs):** `[8, 16, 11, 7, 13, 5, 6, 4, 10, 4, 4, 14, 3]`
- **Số thế hệ tiến hóa:** `121` generations

### Chi tiết các cụm $s$-club thành phần:
- **Club 7** (Size = 8 đỉnh): `[0, 1, 2, 4, 5, 6, 7, 29]`
- **Club 8** (Size = 16 đỉnh): `[3, 8, 9, 10, 11, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 25]`
- **Club 9** (Size = 11 đỉnh): `[12, 23, 32, 33, 39, 41, 44, 46, 47, 54, 55]`
- **Club 10** (Size = 7 đỉnh): `[24, 26, 27, 40, 42, 45, 53]`
- **Club 1** (Size = 13 đỉnh): `[28, 70, 71, 72, 75, 76, 78, 79, 80, 87, 90, 91, 92]`
- **Club 11** (Size = 5 đỉnh): `[30, 31, 74, 82, 98]`
- **Club 6** (Size = 6 đỉnh): `[34, 35, 36, 37, 38, 43]`
- **Club 3** (Size = 4 đỉnh): `[48, 49, 56, 57]`
- **Club 5** (Size = 10 đỉnh): `[50, 51, 52, 58, 64, 65, 68, 69, 77, 85]`
- **Club 2** (Size = 4 đỉnh): `[59, 60, 62, 63]`
- **Club 12** (Size = 4 đỉnh): `[61, 94, 95, 102]`
- **Club 13** (Size = 14 đỉnh): `[66, 73, 81, 83, 84, 86, 88, 89, 93, 96, 97, 99, 100, 101]`
- **Club 4** (Size = 3 đỉnh): `[67, 103, 104]`

---
*File được sinh tự động bởi hệ thống EVO-RL MSCC Research Framework.*
