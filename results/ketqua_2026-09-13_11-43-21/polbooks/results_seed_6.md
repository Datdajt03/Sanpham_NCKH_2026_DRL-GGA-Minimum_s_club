# Báo Cáo Kết Quả Thực Nghiệm: Seed #06 (Seed = `20260317`)

**Tập dữ liệu đồ thị:** `polbooks` ($|V| = 105$, $|E| = 441$, Density = $0.0808$, $s = 2$)  
**Hạt giống cố định (Seed Value):** `20260317` (Lần chạy 06/20 từ `seedun.md`)  
**Thời gian thực thi:** `2026-09-13 11:48:38`  
**Môi trường tính toán:** `Hybrid Co-Processing [CPU: 12 Cores song song (GA/C++ igraph) + GPU: NVIDIA GeForce RTX 3050 Laptop GPU (PPO Tensor Cores)]`  

---

## 1. Bảng Thống Kê Hiệu Năng Chi Tiết Các Thuật Toán (Seed #6)

| Chiến lược / Thuật toán | Best Cover (Min) | Best Fitness | Mean $\pm$ Std | Median | Vi phạm ($diam > s$) | Độ đa dạng | Khả thi ($100\%$) | Thời gian (s) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **PPO-AOS** | **13** | **13.00** | 13.61 $\pm$ 0.78 | 13.0 | 0.00 | 0.811 |  Đạt chuẩn | 11.04s |
| MAB-AOS | 13 | 13.00 | 13.49 $\pm$ 1.10 | 13.0 | 0.00 | 0.888 |  Đạt chuẩn | 5.79s |
| Greedy-AOS | 13 | 13.00 | 13.35 $\pm$ 0.84 | 13.0 | 0.00 | 0.865 |  Đạt chuẩn | 5.52s |
| I-MSM | 13 | 13.00 | 13.00 $\pm$ 0.00 | 13.0 | 0.00 | 0.000 |  Đạt chuẩn | 0.99s |
| CCA | 13 | 13.00 | 13.50 $\pm$ 0.82 | 13.0 | 0.00 | 0.000 |  Đạt chuẩn | 0.28s |
| No-RL | 13 | 13.00 | 13.40 $\pm$ 0.83 | 13.0 | 0.00 | 0.866 |  Đạt chuẩn | 5.91s |
| Fixed | 13 | 13.00 | 13.33 $\pm$ 0.81 | 13.0 | 0.00 | 0.840 |  Đạt chuẩn | 4.03s |
| Random | 13 | 13.00 | 13.40 $\pm$ 0.83 | 13.0 | 0.00 | 0.866 |  Đạt chuẩn | 6.27s |

---

## 2. Cấu Trúc Nghiệm Tốt Nhất Trong Lần Chạy (Best Solution Clusters)
- **Thuật toán đạt Best:** `PPO-AOS` (Cover = `13` clubs, Fitness = `13.00`)
- **Kích thước các cụm ($s$-clubs):** `[7, 18, 11, 9, 5, 7, 9, 9, 5, 6, 13, 3, 3]`
- **Số thế hệ tiến hóa:** `201` generations

### Chi tiết các cụm $s$-club thành phần:
- **Club 7** (Size = 7 đỉnh): `[0, 1, 2, 4, 5, 6, 29]`
- **Club 5** (Size = 18 đỉnh): `[3, 8, 9, 11, 12, 13, 14, 17, 18, 21, 22, 23, 24, 27, 32, 41, 46, 47]`
- **Club 1** (Size = 11 đỉnh): `[7, 50, 51, 52, 58, 64, 65, 68, 69, 77, 85]`
- **Club 8** (Size = 9 đỉnh): `[10, 15, 16, 19, 33, 37, 38, 39, 55]`
- **Club 3** (Size = 5 đỉnh): `[20, 48, 49, 56, 57]`
- **Club 9** (Size = 7 đỉnh): `[25, 26, 40, 42, 45, 53, 54]`
- **Club 4** (Size = 9 đỉnh): `[28, 70, 72, 75, 76, 80, 87, 90, 92]`
- **Club 6** (Size = 9 đỉnh): `[30, 31, 71, 74, 78, 79, 82, 91, 98]`
- **Club 10** (Size = 5 đỉnh): `[34, 35, 36, 43, 44]`
- **Club 2** (Size = 6 đỉnh): `[59, 60, 61, 62, 63, 99]`
- **Club 11** (Size = 13 đỉnh): `[66, 73, 81, 83, 84, 86, 88, 89, 94, 96, 97, 100, 101]`
- **Club 12** (Size = 3 đỉnh): `[67, 103, 104]`
- **Club 13** (Size = 3 đỉnh): `[93, 95, 102]`

---
*File được sinh tự động bởi hệ thống EVO-RL MSCC Research Framework.*
