# Báo Cáo Kết Quả Thực Nghiệm: Seed #07 (Seed = `20260421`)

**Tập dữ liệu đồ thị:** `polbooks` ($|V| = 105$, $|E| = 441$, Density = $0.0808$, $s = 2$)  
**Hạt giống cố định (Seed Value):** `20260421` (Lần chạy 07/20 từ `seedun.md`)  
**Thời gian thực thi:** `2026-09-13 11:48:33`  
**Môi trường tính toán:** `Hybrid Co-Processing [CPU: 12 Cores song song (GA/C++ igraph) + GPU: NVIDIA GeForce RTX 3050 Laptop GPU (PPO Tensor Cores)]`  

---

## 1. Bảng Thống Kê Hiệu Năng Chi Tiết Các Thuật Toán (Seed #7)

| Chiến lược / Thuật toán | Best Cover (Min) | Best Fitness | Mean $\pm$ Std | Median | Vi phạm ($diam > s$) | Độ đa dạng | Khả thi ($100\%$) | Thời gian (s) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **PPO-AOS** | **13** | **13.00** | 13.23 $\pm$ 0.51 | 13.0 | 0.00 | 0.879 |  Đạt chuẩn | 8.46s |
| MAB-AOS | 13 | 13.00 | 13.21 $\pm$ 0.50 | 13.0 | 0.00 | 0.771 |  Đạt chuẩn | 5.38s |
| Greedy-AOS | 13 | 13.00 | 13.22 $\pm$ 0.55 | 13.0 | 0.00 | 0.784 |  Đạt chuẩn | 5.37s |
| I-MSM | 13 | 13.00 | 13.43 $\pm$ 0.49 | 13.0 | 0.00 | 0.000 |  Đạt chuẩn | 1.85s |
| CCA | 14 | 14.00 | 14.22 $\pm$ 0.63 | 14.0 | 0.00 | 0.000 |  Đạt chuẩn | 0.24s |
| No-RL | 13 | 13.00 | 13.18 $\pm$ 0.52 | 13.0 | 0.00 | 0.884 |  Đạt chuẩn | 4.68s |
| Fixed | 13 | 13.00 | 13.29 $\pm$ 0.63 | 13.0 | 0.00 | 0.883 |  Đạt chuẩn | 4.53s |
| Random | 13 | 13.00 | 13.18 $\pm$ 0.52 | 13.0 | 0.00 | 0.884 |  Đạt chuẩn | 4.66s |

---

## 2. Cấu Trúc Nghiệm Tốt Nhất Trong Lần Chạy (Best Solution Clusters)
- **Thuật toán đạt Best:** `PPO-AOS` (Cover = `13` clubs, Fitness = `13.00`)
- **Kích thước các cụm ($s$-clubs):** `[7, 13, 12, 13, 6, 8, 6, 8, 14, 3, 5, 8, 2]`
- **Số thế hệ tiến hóa:** `124` generations

### Chi tiết các cụm $s$-club thành phần:
- **Club 7** (Size = 7 đỉnh): `[0, 2, 4, 6, 28, 29, 31]`
- **Club 3** (Size = 13 đỉnh): `[1, 3, 5, 15, 16, 17, 18, 19, 21, 22, 23, 25, 26]`
- **Club 10** (Size = 12 đỉnh): `[7, 30, 50, 51, 52, 58, 64, 65, 68, 69, 77, 85]`
- **Club 1** (Size = 13 đỉnh): `[8, 9, 10, 11, 12, 14, 32, 33, 36, 41, 44, 46, 55]`
- **Club 8** (Size = 6 đỉnh): `[13, 20, 48, 49, 56, 57]`
- **Club 9** (Size = 8 đỉnh): `[24, 27, 40, 42, 45, 47, 53, 54]`
- **Club 11** (Size = 6 đỉnh): `[34, 35, 37, 38, 39, 43]`
- **Club 2** (Size = 8 đỉnh): `[59, 60, 61, 62, 63, 86, 93, 99]`
- **Club 12** (Size = 14 đỉnh): `[66, 70, 71, 72, 73, 74, 75, 76, 78, 80, 82, 87, 90, 92]`
- **Club 6** (Size = 3 đỉnh): `[67, 103, 104]`
- **Club 5** (Size = 5 đỉnh): `[79, 91, 96, 98, 100]`
- **Club 13** (Size = 8 đỉnh): `[81, 83, 84, 88, 89, 94, 97, 101]`
- **Club 4** (Size = 2 đỉnh): `[95, 102]`

---
*File được sinh tự động bởi hệ thống EVO-RL MSCC Research Framework.*
