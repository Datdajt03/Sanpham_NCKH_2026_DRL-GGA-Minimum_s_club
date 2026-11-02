# Báo Cáo Kết Quả Thực Nghiệm: Seed #16 (Seed = `27182818`)

**Tập dữ liệu đồ thị:** `football` ($|V| = 115$, $|E| = 613$, Density = $0.0935$, $s = 2$)  
**Hạt giống cố định (Seed Value):** `27182818` (Lần chạy 16/20 từ `seedun.md`)  
**Thời gian thực thi:** `2026-09-13 11:53:00`  
**Môi trường tính toán:** `Hybrid Co-Processing [CPU: 12 Cores song song (GA/C++ igraph) + GPU: NVIDIA GeForce RTX 3050 Laptop GPU (PPO Tensor Cores)]`  

---

## 1. Bảng Thống Kê Hiệu Năng Chi Tiết Các Thuật Toán (Seed #16)

| Chiến lược / Thuật toán | Best Cover (Min) | Best Fitness | Mean $\pm$ Std | Median | Vi phạm ($diam > s$) | Độ đa dạng | Khả thi ($100\%$) | Thời gian (s) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **PPO-AOS** | **10** | **10.00** | 10.31 $\pm$ 0.87 | 10.0 | 0.00 | 0.860 |  Đạt chuẩn | 5.70s |
| MAB-AOS | 10 | 10.00 | 10.26 $\pm$ 0.72 | 10.0 | 0.00 | 0.862 |  Đạt chuẩn | 4.68s |
| Greedy-AOS | 10 | 10.00 | 10.18 $\pm$ 0.63 | 10.0 | 0.00 | 0.879 |  Đạt chuẩn | 4.51s |
| I-MSM | 13 | 13.00 | 13.27 $\pm$ 0.45 | 13.0 | 0.00 | 0.000 |  Đạt chuẩn | 0.97s |
| CCA | 14 | 14.00 | 14.18 $\pm$ 0.71 | 14.0 | 0.00 | 0.000 |  Đạt chuẩn | 0.14s |
| No-RL | 10 | 10.00 | 10.40 $\pm$ 1.01 | 10.0 | 0.00 | 0.888 |  Đạt chuẩn | 4.83s |
| Fixed | 10 | 10.00 | 10.18 $\pm$ 0.59 | 10.0 | 0.00 | 0.839 |  Đạt chuẩn | 3.47s |
| Random | 10 | 10.00 | 10.40 $\pm$ 1.01 | 10.0 | 0.00 | 0.888 |  Đạt chuẩn | 4.72s |

---

## 2. Cấu Trúc Nghiệm Tốt Nhất Trong Lần Chạy (Best Solution Clusters)
- **Thuật toán đạt Best:** `PPO-AOS` (Cover = `10` clubs, Fitness = `10.00`)
- **Kích thước các cụm ($s$-clubs):** `[13, 11, 12, 10, 12, 12, 14, 12, 10, 9]`
- **Số thế hệ tiến hóa:** `118` generations

### Chi tiết các cụm $s$-club thành phần:
- **Club 5** (Size = 13 đỉnh): `[0, 4, 5, 9, 11, 16, 23, 28, 41, 69, 90, 93, 104]`
- **Club 3** (Size = 11 đỉnh): `[1, 24, 25, 33, 37, 45, 53, 89, 103, 105, 109]`
- **Club 4** (Size = 12 đỉnh): `[2, 6, 13, 14, 15, 32, 39, 47, 60, 64, 100, 106]`
- **Club 2** (Size = 10 đỉnh): `[3, 10, 52, 72, 74, 81, 84, 98, 102, 107]`
- **Club 1** (Size = 12 đỉnh): `[7, 8, 21, 22, 40, 50, 51, 68, 77, 78, 108, 111]`
- **Club 8** (Size = 12 đỉnh): `[12, 18, 26, 31, 36, 38, 43, 54, 61, 71, 85, 99]`
- **Club 6** (Size = 14 đỉnh): `[17, 20, 27, 56, 59, 62, 63, 65, 70, 76, 87, 95, 96, 113]`
- **Club 10** (Size = 12 đỉnh): `[19, 29, 30, 34, 35, 42, 55, 79, 80, 82, 94, 101]`
- **Club 7** (Size = 10 đỉnh): `[44, 48, 57, 66, 75, 86, 91, 92, 97, 112]`
- **Club 9** (Size = 9 đỉnh): `[46, 49, 58, 67, 73, 83, 88, 110, 114]`

---
*File được sinh tự động bởi hệ thống EVO-RL MSCC Research Framework.*
