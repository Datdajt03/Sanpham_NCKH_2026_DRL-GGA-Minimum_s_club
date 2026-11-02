# Báo Cáo Kết Quả Thực Nghiệm: Seed #03 (Seed = `23052026`)

**Tập dữ liệu đồ thị:** `polbooks` ($|V| = 105$, $|E| = 441$, Density = $0.0808$, $s = 2$)  
**Hạt giống cố định (Seed Value):** `23052026` (Lần chạy 03/20 từ `seedun.md`)  
**Thời gian thực thi:** `2026-09-13 11:48:37`  
**Môi trường tính toán:** `Hybrid Co-Processing [CPU: 12 Cores song song (GA/C++ igraph) + GPU: NVIDIA GeForce RTX 3050 Laptop GPU (PPO Tensor Cores)]`  

---

## 1. Bảng Thống Kê Hiệu Năng Chi Tiết Các Thuật Toán (Seed #3)

| Chiến lược / Thuật toán | Best Cover (Min) | Best Fitness | Mean $\pm$ Std | Median | Vi phạm ($diam > s$) | Độ đa dạng | Khả thi ($100\%$) | Thời gian (s) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **PPO-AOS** | **13** | **13.00** | 13.48 $\pm$ 0.92 | 13.0 | 0.00 | 0.870 |  Đạt chuẩn | 9.46s |
| MAB-AOS | 13 | 13.00 | 13.35 $\pm$ 0.86 | 13.0 | 0.00 | 0.912 |  Đạt chuẩn | 5.52s |
| Greedy-AOS | 13 | 13.00 | 13.41 $\pm$ 0.87 | 13.0 | 0.00 | 0.857 |  Đạt chuẩn | 6.16s |
| I-MSM | 13 | 13.00 | 13.50 $\pm$ 0.68 | 13.0 | 0.00 | 0.000 |  Đạt chuẩn | 1.92s |
| CCA | 14 | 14.00 | 14.33 $\pm$ 0.71 | 14.0 | 0.00 | 0.000 |  Đạt chuẩn | 0.21s |
| No-RL | 14 | 14.00 | 14.13 $\pm$ 0.49 | 14.0 | 0.00 | 0.786 |  Đạt chuẩn | 5.36s |
| Fixed | 13 | 13.00 | 13.42 $\pm$ 0.96 | 13.0 | 0.00 | 0.829 |  Đạt chuẩn | 4.54s |
| Random | 14 | 14.00 | 14.13 $\pm$ 0.49 | 14.0 | 0.00 | 0.786 |  Đạt chuẩn | 5.55s |

---

## 2. Cấu Trúc Nghiệm Tốt Nhất Trong Lần Chạy (Best Solution Clusters)
- **Thuật toán đạt Best:** `PPO-AOS` (Cover = `13` clubs, Fitness = `13.00`)
- **Kích thước các cụm ($s$-clubs):** `[8, 9, 13, 13, 12, 15, 5, 3, 9, 5, 4, 8, 1]`
- **Số thế hệ tiến hóa:** `140` generations

### Chi tiết các cụm $s$-club thành phần:
- **Club 7** (Size = 8 đỉnh): `[0, 1, 2, 4, 5, 6, 7, 29]`
- **Club 6** (Size = 9 đỉnh): `[3, 8, 14, 16, 18, 19, 21, 22, 25]`
- **Club 5** (Size = 13 đỉnh): `[9, 11, 20, 24, 26, 27, 40, 41, 42, 45, 47, 53, 54]`
- **Club 1** (Size = 13 đỉnh): `[10, 12, 13, 15, 17, 23, 32, 33, 36, 39, 44, 46, 55]`
- **Club 9** (Size = 12 đỉnh): `[28, 49, 70, 71, 72, 78, 79, 80, 88, 90, 91, 92]`
- **Club 2** (Size = 15 đỉnh): `[30, 31, 66, 73, 74, 82, 86, 89, 93, 94, 95, 96, 98, 99, 100]`
- **Club 10** (Size = 5 đỉnh): `[34, 35, 37, 38, 43]`
- **Club 8** (Size = 3 đỉnh): `[48, 56, 57]`
- **Club 3** (Size = 9 đỉnh): `[50, 51, 52, 58, 65, 68, 69, 77, 85]`
- **Club 11** (Size = 5 đỉnh): `[59, 60, 61, 62, 63]`
- **Club 12** (Size = 4 đỉnh): `[64, 67, 103, 104]`
- **Club 4** (Size = 8 đỉnh): `[75, 76, 81, 83, 84, 87, 97, 101]`
- **Club 13** (Size = 1 đỉnh): `[102]`

---
*File được sinh tự động bởi hệ thống EVO-RL MSCC Research Framework.*
