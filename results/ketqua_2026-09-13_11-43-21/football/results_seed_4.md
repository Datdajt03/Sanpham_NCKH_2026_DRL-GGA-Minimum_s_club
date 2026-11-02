# Báo Cáo Kết Quả Thực Nghiệm: Seed #04 (Seed = `26062026`)

**Tập dữ liệu đồ thị:** `football` ($|V| = 115$, $|E| = 613$, Density = $0.0935$, $s = 2$)  
**Hạt giống cố định (Seed Value):** `26062026` (Lần chạy 04/20 từ `seedun.md`)  
**Thời gian thực thi:** `2026-09-13 11:52:31`  
**Môi trường tính toán:** `Hybrid Co-Processing [CPU: 12 Cores song song (GA/C++ igraph) + GPU: NVIDIA GeForce RTX 3050 Laptop GPU (PPO Tensor Cores)]`  

---

## 1. Bảng Thống Kê Hiệu Năng Chi Tiết Các Thuật Toán (Seed #4)

| Chiến lược / Thuật toán | Best Cover (Min) | Best Fitness | Mean $\pm$ Std | Median | Vi phạm ($diam > s$) | Độ đa dạng | Khả thi ($100\%$) | Thời gian (s) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **PPO-AOS** | **10** | **10.00** | 10.34 $\pm$ 0.81 | 10.0 | 0.00 | 0.817 |  Đạt chuẩn | 8.42s |
| MAB-AOS | 10 | 10.00 | 10.32 $\pm$ 0.81 | 10.0 | 0.00 | 0.777 |  Đạt chuẩn | 4.99s |
| Greedy-AOS | 11 | 11.00 | 11.14 $\pm$ 0.53 | 11.0 | 0.00 | 0.870 |  Đạt chuẩn | 4.30s |
| I-MSM | 12 | 12.00 | 12.12 $\pm$ 0.47 | 12.0 | 0.00 | 0.000 |  Đạt chuẩn | 0.74s |
| CCA | 13 | 13.00 | 13.53 $\pm$ 0.62 | 13.0 | 0.00 | 0.000 |  Đạt chuẩn | 0.25s |
| No-RL | 10 | 10.00 | 10.42 $\pm$ 0.88 | 10.0 | 0.00 | 0.888 |  Đạt chuẩn | 5.68s |
| Fixed | 10 | 10.00 | 10.17 $\pm$ 0.54 | 10.0 | 0.00 | 0.880 |  Đạt chuẩn | 3.29s |
| Random | 10 | 10.00 | 10.42 $\pm$ 0.88 | 10.0 | 0.00 | 0.888 |  Đạt chuẩn | 5.37s |

---

## 2. Cấu Trúc Nghiệm Tốt Nhất Trong Lần Chạy (Best Solution Clusters)
- **Thuật toán đạt Best:** `PPO-AOS` (Cover = `10` clubs, Fitness = `10.00`)
- **Kích thước các cụm ($s$-clubs):** `[13, 10, 11, 9, 12, 15, 14, 10, 11, 10]`
- **Số thế hệ tiến hóa:** `128` generations

### Chi tiết các cụm $s$-club thành phần:
- **Club 2** (Size = 13 đỉnh): `[0, 4, 5, 9, 11, 16, 23, 28, 41, 69, 90, 93, 104]`
- **Club 5** (Size = 10 đỉnh): `[1, 24, 25, 33, 37, 45, 89, 103, 105, 109]`
- **Club 6** (Size = 11 đỉnh): `[2, 6, 13, 15, 32, 39, 47, 60, 64, 100, 106]`
- **Club 7** (Size = 9 đỉnh): `[3, 10, 52, 72, 74, 81, 84, 102, 107]`
- **Club 8** (Size = 12 đỉnh): `[7, 8, 21, 22, 40, 50, 51, 68, 77, 78, 108, 111]`
- **Club 9** (Size = 15 đỉnh): `[12, 14, 18, 26, 31, 34, 36, 38, 42, 43, 54, 61, 71, 85, 99]`
- **Club 4** (Size = 14 đỉnh): `[17, 20, 27, 56, 59, 62, 63, 65, 70, 76, 87, 95, 96, 113]`
- **Club 3** (Size = 10 đỉnh): `[19, 29, 30, 35, 55, 79, 80, 82, 94, 101]`
- **Club 1** (Size = 11 đỉnh): `[44, 48, 57, 66, 75, 86, 91, 92, 97, 98, 112]`
- **Club 10** (Size = 10 đỉnh): `[46, 49, 53, 58, 67, 73, 83, 88, 110, 114]`

---
*File được sinh tự động bởi hệ thống EVO-RL MSCC Research Framework.*
