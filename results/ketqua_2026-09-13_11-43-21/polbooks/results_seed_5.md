# Báo Cáo Kết Quả Thực Nghiệm: Seed #05 (Seed = `13092026`)

**Tập dữ liệu đồ thị:** `polbooks` ($|V| = 105$, $|E| = 441$, Density = $0.0808$, $s = 2$)  
**Hạt giống cố định (Seed Value):** `13092026` (Lần chạy 05/20 từ `seedun.md`)  
**Thời gian thực thi:** `2026-09-13 11:48:38`  
**Môi trường tính toán:** `Hybrid Co-Processing [CPU: 12 Cores song song (GA/C++ igraph) + GPU: NVIDIA GeForce RTX 3050 Laptop GPU (PPO Tensor Cores)]`  

---

## 1. Bảng Thống Kê Hiệu Năng Chi Tiết Các Thuật Toán (Seed #5)

| Chiến lược / Thuật toán | Best Cover (Min) | Best Fitness | Mean $\pm$ Std | Median | Vi phạm ($diam > s$) | Độ đa dạng | Khả thi ($100\%$) | Thời gian (s) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **PPO-AOS** | **13** | **13.00** | 13.33 $\pm$ 0.77 | 13.0 | 0.00 | 0.866 |  Đạt chuẩn | 8.79s |
| MAB-AOS | 13 | 13.00 | 13.44 $\pm$ 0.81 | 13.0 | 0.00 | 0.832 |  Đạt chuẩn | 5.92s |
| Greedy-AOS | 13 | 13.00 | 13.28 $\pm$ 0.74 | 13.0 | 0.00 | 0.926 |  Đạt chuẩn | 5.28s |
| I-MSM | 14 | 14.00 | 14.22 $\pm$ 0.63 | 14.0 | 0.00 | 0.000 |  Đạt chuẩn | 1.26s |
| CCA | 14 | 14.00 | 14.00 $\pm$ 0.00 | 14.0 | 0.00 | 0.000 |  Đạt chuẩn | 0.20s |
| No-RL | 13 | 13.00 | 13.44 $\pm$ 0.74 | 13.0 | 0.00 | 0.914 |  Đạt chuẩn | 6.52s |
| Fixed | 13 | 13.00 | 13.35 $\pm$ 0.76 | 13.0 | 0.00 | 0.902 |  Đạt chuẩn | 4.85s |
| Random | 13 | 13.00 | 13.44 $\pm$ 0.74 | 13.0 | 0.00 | 0.914 |  Đạt chuẩn | 6.58s |

---

## 2. Cấu Trúc Nghiệm Tốt Nhất Trong Lần Chạy (Best Solution Clusters)
- **Thuật toán đạt Best:** `PPO-AOS` (Cover = `13` clubs, Fitness = `13.00`)
- **Kích thước các cụm ($s$-clubs):** `[7, 16, 11, 7, 10, 13, 12, 7, 2, 4, 5, 3, 8]`
- **Số thế hệ tiến hóa:** `124` generations

### Chi tiết các cụm $s$-club thành phần:
- **Club 4** (Size = 7 đỉnh): `[0, 2, 4, 5, 6, 28, 29]`
- **Club 3** (Size = 16 đỉnh): `[1, 3, 9, 10, 11, 13, 15, 16, 17, 18, 19, 20, 21, 22, 25, 27]`
- **Club 2** (Size = 11 đỉnh): `[7, 50, 51, 52, 58, 64, 65, 68, 69, 77, 85]`
- **Club 13** (Size = 7 đỉnh): `[8, 12, 14, 23, 32, 33, 55]`
- **Club 8** (Size = 10 đỉnh): `[24, 26, 40, 41, 42, 44, 45, 47, 53, 54]`
- **Club 5** (Size = 13 đỉnh): `[30, 66, 74, 76, 79, 81, 83, 84, 86, 87, 88, 89, 101]`
- **Club 6** (Size = 12 đỉnh): `[31, 73, 75, 82, 93, 94, 95, 96, 97, 98, 99, 100]`
- **Club 9** (Size = 7 đỉnh): `[34, 35, 36, 37, 38, 39, 43]`
- **Club 10** (Size = 2 đỉnh): `[46, 102]`
- **Club 1** (Size = 4 đỉnh): `[48, 49, 56, 57]`
- **Club 7** (Size = 5 đỉnh): `[59, 60, 61, 62, 63]`
- **Club 11** (Size = 3 đỉnh): `[67, 103, 104]`
- **Club 12** (Size = 8 đỉnh): `[70, 71, 72, 78, 80, 90, 91, 92]`

---
*File được sinh tự động bởi hệ thống EVO-RL MSCC Research Framework.*
