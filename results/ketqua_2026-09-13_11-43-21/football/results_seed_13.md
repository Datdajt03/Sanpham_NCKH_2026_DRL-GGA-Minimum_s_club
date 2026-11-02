# Báo Cáo Kết Quả Thực Nghiệm: Seed #13 (Seed = `13572468`)

**Tập dữ liệu đồ thị:** `football` ($|V| = 115$, $|E| = 613$, Density = $0.0935$, $s = 2$)  
**Hạt giống cố định (Seed Value):** `13572468` (Lần chạy 13/20 từ `seedun.md`)  
**Thời gian thực thi:** `2026-09-13 11:52:59`  
**Môi trường tính toán:** `Hybrid Co-Processing [CPU: 12 Cores song song (GA/C++ igraph) + GPU: NVIDIA GeForce RTX 3050 Laptop GPU (PPO Tensor Cores)]`  

---

## 1. Bảng Thống Kê Hiệu Năng Chi Tiết Các Thuật Toán (Seed #13)

| Chiến lược / Thuật toán | Best Cover (Min) | Best Fitness | Mean $\pm$ Std | Median | Vi phạm ($diam > s$) | Độ đa dạng | Khả thi ($100\%$) | Thời gian (s) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **PPO-AOS** | **10** | **10.00** | 10.42 $\pm$ 0.76 | 10.0 | 0.00 | 0.792 |  Đạt chuẩn | 7.32s |
| MAB-AOS | 10 | 10.00 | 10.17 $\pm$ 0.57 | 10.0 | 0.00 | 0.862 |  Đạt chuẩn | 4.65s |
| Greedy-AOS | 10 | 10.00 | 10.26 $\pm$ 0.62 | 10.0 | 0.00 | 0.828 |  Đạt chuẩn | 5.03s |
| I-MSM | 13 | 13.00 | 13.12 $\pm$ 0.47 | 13.0 | 0.00 | 0.000 |  Đạt chuẩn | 0.69s |
| CCA | 14 | 14.00 | 14.20 $\pm$ 0.40 | 14.0 | 0.00 | 0.000 |  Đạt chuẩn | 0.16s |
| No-RL | 10 | 10.00 | 10.29 $\pm$ 0.74 | 10.0 | 0.00 | 0.773 |  Đạt chuẩn | 4.53s |
| Fixed | 10 | 10.00 | 10.17 $\pm$ 0.52 | 10.0 | 0.00 | 0.825 |  Đạt chuẩn | 3.19s |
| Random | 10 | 10.00 | 10.29 $\pm$ 0.74 | 10.0 | 0.00 | 0.773 |  Đạt chuẩn | 4.34s |

---

## 2. Cấu Trúc Nghiệm Tốt Nhất Trong Lần Chạy (Best Solution Clusters)
- **Thuật toán đạt Best:** `PPO-AOS` (Cover = `10` clubs, Fitness = `10.00`)
- **Kích thước các cụm ($s$-clubs):** `[12, 10, 11, 13, 11, 15, 15, 10, 8, 10]`
- **Số thế hệ tiến hóa:** `146` generations

### Chi tiết các cụm $s$-club thành phần:
- **Club 2** (Size = 12 đỉnh): `[0, 4, 9, 16, 23, 28, 41, 69, 90, 91, 93, 104]`
- **Club 7** (Size = 10 đỉnh): `[1, 24, 25, 33, 37, 45, 89, 103, 105, 109]`
- **Club 1** (Size = 11 đỉnh): `[2, 6, 13, 15, 32, 39, 47, 60, 64, 100, 106]`
- **Club 5** (Size = 13 đỉnh): `[3, 5, 10, 11, 40, 52, 72, 74, 81, 84, 98, 102, 107]`
- **Club 6** (Size = 11 đỉnh): `[7, 8, 21, 22, 50, 51, 68, 77, 78, 108, 111]`
- **Club 4** (Size = 15 đỉnh): `[12, 14, 18, 26, 31, 34, 36, 38, 42, 43, 54, 61, 71, 85, 99]`
- **Club 8** (Size = 15 đỉnh): `[17, 20, 27, 56, 59, 62, 63, 65, 66, 70, 76, 87, 95, 96, 113]`
- **Club 9** (Size = 10 đỉnh): `[19, 29, 30, 35, 55, 79, 80, 82, 94, 101]`
- **Club 10** (Size = 8 đỉnh): `[44, 48, 57, 75, 86, 92, 97, 112]`
- **Club 3** (Size = 10 đỉnh): `[46, 49, 53, 58, 67, 73, 83, 88, 110, 114]`

---
*File được sinh tự động bởi hệ thống EVO-RL MSCC Research Framework.*
