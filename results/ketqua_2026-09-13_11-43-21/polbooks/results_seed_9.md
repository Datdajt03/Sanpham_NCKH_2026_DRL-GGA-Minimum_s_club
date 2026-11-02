# Báo Cáo Kết Quả Thực Nghiệm: Seed #09 (Seed = `20260626`)

**Tập dữ liệu đồ thị:** `polbooks` ($|V| = 105$, $|E| = 441$, Density = $0.0808$, $s = 2$)  
**Hạt giống cố định (Seed Value):** `20260626` (Lần chạy 09/20 từ `seedun.md`)  
**Thời gian thực thi:** `2026-09-13 11:48:36`  
**Môi trường tính toán:** `Hybrid Co-Processing [CPU: 12 Cores song song (GA/C++ igraph) + GPU: NVIDIA GeForce RTX 3050 Laptop GPU (PPO Tensor Cores)]`  

---

## 1. Bảng Thống Kê Hiệu Năng Chi Tiết Các Thuật Toán (Seed #9)

| Chiến lược / Thuật toán | Best Cover (Min) | Best Fitness | Mean $\pm$ Std | Median | Vi phạm ($diam > s$) | Độ đa dạng | Khả thi ($100\%$) | Thời gian (s) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **PPO-AOS** | **13** | **13.00** | 13.45 $\pm$ 0.83 | 13.0 | 0.00 | 0.846 |  Đạt chuẩn | 8.74s |
| MAB-AOS | 13 | 13.00 | 13.38 $\pm$ 0.82 | 13.0 | 0.00 | 0.891 |  Đạt chuẩn | 5.91s |
| Greedy-AOS | 13 | 13.00 | 13.32 $\pm$ 0.73 | 13.0 | 0.00 | 0.884 |  Đạt chuẩn | 5.55s |
| I-MSM | 13 | 13.00 | 13.52 $\pm$ 0.62 | 13.0 | 0.00 | 0.000 |  Đạt chuẩn | 1.81s |
| CCA | 13 | 13.00 | 13.22 $\pm$ 0.63 | 13.0 | 0.00 | 0.000 |  Đạt chuẩn | 0.20s |
| No-RL | 13 | 13.00 | 13.26 $\pm$ 0.59 | 13.0 | 0.00 | 0.833 |  Đạt chuẩn | 5.09s |
| Fixed | 13 | 13.00 | 13.35 $\pm$ 0.78 | 13.0 | 0.00 | 0.904 |  Đạt chuẩn | 4.84s |
| Random | 13 | 13.00 | 13.26 $\pm$ 0.59 | 13.0 | 0.00 | 0.833 |  Đạt chuẩn | 5.25s |

---

## 2. Cấu Trúc Nghiệm Tốt Nhất Trong Lần Chạy (Best Solution Clusters)
- **Thuật toán đạt Best:** `PPO-AOS` (Cover = `13` clubs, Fitness = `13.00`)
- **Kích thước các cụm ($s$-clubs):** `[8, 16, 12, 6, 10, 13, 6, 4, 10, 4, 7, 3, 6]`
- **Số thế hệ tiến hóa:** `137` generations

### Chi tiết các cụm $s$-club thành phần:
- **Club 8** (Size = 8 đỉnh): `[0, 1, 2, 4, 5, 6, 7, 29]`
- **Club 7** (Size = 16 đỉnh): `[3, 8, 9, 10, 11, 14, 16, 19, 20, 21, 22, 23, 26, 27, 33, 37]`
- **Club 9** (Size = 12 đỉnh): `[12, 13, 15, 17, 18, 24, 32, 36, 41, 46, 54, 55]`
- **Club 11** (Size = 6 đỉnh): `[25, 40, 42, 45, 47, 53]`
- **Club 5** (Size = 10 đỉnh): `[28, 70, 71, 72, 75, 76, 78, 80, 90, 92]`
- **Club 3** (Size = 13 đỉnh): `[30, 31, 66, 73, 74, 79, 82, 83, 87, 91, 98, 99, 100]`
- **Club 12** (Size = 6 đỉnh): `[34, 35, 38, 39, 43, 44]`
- **Club 10** (Size = 4 đỉnh): `[48, 49, 56, 57]`
- **Club 1** (Size = 10 đỉnh): `[50, 51, 52, 58, 64, 65, 68, 69, 77, 85]`
- **Club 13** (Size = 4 đỉnh): `[59, 60, 62, 63]`
- **Club 4** (Size = 7 đỉnh): `[61, 86, 93, 94, 95, 101, 102]`
- **Club 6** (Size = 3 đỉnh): `[67, 103, 104]`
- **Club 2** (Size = 6 đỉnh): `[81, 84, 88, 89, 96, 97]`

---
*File được sinh tự động bởi hệ thống EVO-RL MSCC Research Framework.*
