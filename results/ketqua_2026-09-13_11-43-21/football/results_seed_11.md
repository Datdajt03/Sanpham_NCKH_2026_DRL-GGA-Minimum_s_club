# Báo Cáo Kết Quả Thực Nghiệm: Seed #11 (Seed = `11223344`)

**Tập dữ liệu đồ thị:** `football` ($|V| = 115$, $|E| = 613$, Density = $0.0935$, $s = 2$)  
**Hạt giống cố định (Seed Value):** `11223344` (Lần chạy 11/20 từ `seedun.md`)  
**Thời gian thực thi:** `2026-09-13 11:52:59`  
**Môi trường tính toán:** `Hybrid Co-Processing [CPU: 12 Cores song song (GA/C++ igraph) + GPU: NVIDIA GeForce RTX 3050 Laptop GPU (PPO Tensor Cores)]`  

---

## 1. Bảng Thống Kê Hiệu Năng Chi Tiết Các Thuật Toán (Seed #11)

| Chiến lược / Thuật toán | Best Cover (Min) | Best Fitness | Mean $\pm$ Std | Median | Vi phạm ($diam > s$) | Độ đa dạng | Khả thi ($100\%$) | Thời gian (s) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **PPO-AOS** | **10** | **10.00** | 10.26 $\pm$ 0.66 | 10.0 | 0.00 | 0.805 |  Đạt chuẩn | 6.11s |
| MAB-AOS | 10 | 10.00 | 10.26 $\pm$ 0.62 | 10.0 | 0.00 | 0.786 |  Đạt chuẩn | 5.00s |
| Greedy-AOS | 10 | 10.00 | 10.34 $\pm$ 0.80 | 10.0 | 0.00 | 0.791 |  Đạt chuẩn | 5.44s |
| I-MSM | 13 | 13.00 | 13.40 $\pm$ 0.86 | 13.0 | 0.00 | 0.000 |  Đạt chuẩn | 0.90s |
| CCA | 14 | 14.00 | 14.41 $\pm$ 0.49 | 14.0 | 0.00 | 0.000 |  Đạt chuẩn | 0.24s |
| No-RL | 10 | 10.00 | 10.28 $\pm$ 0.72 | 10.0 | 0.00 | 0.848 |  Đạt chuẩn | 5.05s |
| Fixed | 10 | 10.00 | 10.19 $\pm$ 0.62 | 10.0 | 0.00 | 0.835 |  Đạt chuẩn | 3.29s |
| Random | 10 | 10.00 | 10.28 $\pm$ 0.72 | 10.0 | 0.00 | 0.848 |  Đạt chuẩn | 4.78s |

---

## 2. Cấu Trúc Nghiệm Tốt Nhất Trong Lần Chạy (Best Solution Clusters)
- **Thuật toán đạt Best:** `PPO-AOS` (Cover = `10` clubs, Fitness = `10.00`)
- **Kích thước các cụm ($s$-clubs):** `[12, 12, 10, 13, 11, 15, 12, 8, 9, 13]`
- **Số thế hệ tiến hóa:** `122` generations

### Chi tiết các cụm $s$-club thành phần:
- **Club 9** (Size = 12 đỉnh): `[0, 4, 9, 16, 23, 28, 41, 69, 78, 90, 93, 104]`
- **Club 3** (Size = 12 đỉnh): `[1, 25, 33, 37, 45, 62, 70, 89, 95, 103, 105, 109]`
- **Club 8** (Size = 10 đỉnh): `[2, 6, 15, 39, 47, 60, 64, 82, 100, 106]`
- **Club 5** (Size = 13 đỉnh): `[3, 5, 10, 11, 40, 52, 72, 74, 81, 84, 98, 102, 107]`
- **Club 6** (Size = 11 đỉnh): `[7, 8, 20, 21, 22, 32, 51, 68, 77, 108, 111]`
- **Club 2** (Size = 15 đỉnh): `[12, 14, 18, 26, 31, 34, 36, 38, 42, 43, 54, 61, 71, 85, 99]`
- **Club 7** (Size = 12 đỉnh): `[13, 24, 46, 49, 53, 67, 73, 80, 83, 88, 110, 114]`
- **Club 1** (Size = 8 đỉnh): `[17, 27, 58, 59, 63, 65, 97, 113]`
- **Club 10** (Size = 9 đỉnh): `[19, 29, 30, 35, 50, 55, 79, 94, 101]`
- **Club 4** (Size = 13 đỉnh): `[44, 48, 56, 57, 66, 75, 76, 86, 87, 91, 92, 96, 112]`

---
*File được sinh tự động bởi hệ thống EVO-RL MSCC Research Framework.*
