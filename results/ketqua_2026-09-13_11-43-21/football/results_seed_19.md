# Báo Cáo Kết Quả Thực Nghiệm: Seed #19 (Seed = `64086408`)

**Tập dữ liệu đồ thị:** `football` ($|V| = 115$, $|E| = 613$, Density = $0.0935$, $s = 2$)  
**Hạt giống cố định (Seed Value):** `64086408` (Lần chạy 19/20 từ `seedun.md`)  
**Thời gian thực thi:** `2026-09-13 11:53:02`  
**Môi trường tính toán:** `Hybrid Co-Processing [CPU: 12 Cores song song (GA/C++ igraph) + GPU: NVIDIA GeForce RTX 3050 Laptop GPU (PPO Tensor Cores)]`  

---

## 1. Bảng Thống Kê Hiệu Năng Chi Tiết Các Thuật Toán (Seed #19)

| Chiến lược / Thuật toán | Best Cover (Min) | Best Fitness | Mean $\pm$ Std | Median | Vi phạm ($diam > s$) | Độ đa dạng | Khả thi ($100\%$) | Thời gian (s) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **PPO-AOS** | **10** | **10.00** | 10.39 $\pm$ 0.77 | 10.0 | 0.00 | 0.733 |  Đạt chuẩn | 6.44s |
| MAB-AOS | 10 | 10.00 | 10.16 $\pm$ 0.56 | 10.0 | 0.00 | 0.870 |  Đạt chuẩn | 4.43s |
| Greedy-AOS | 10 | 10.00 | 10.31 $\pm$ 0.75 | 10.0 | 0.00 | 0.803 |  Đạt chuẩn | 5.26s |
| I-MSM | 12 | 12.00 | 12.38 $\pm$ 0.49 | 12.0 | 0.00 | 0.000 |  Đạt chuẩn | 1.12s |
| CCA | 14 | 14.00 | 14.20 $\pm$ 0.40 | 14.0 | 0.00 | 0.000 |  Đạt chuẩn | 0.17s |
| No-RL | 10 | 10.00 | 10.38 $\pm$ 0.86 | 10.0 | 0.00 | 0.809 |  Đạt chuẩn | 4.70s |
| Fixed | 10 | 10.00 | 10.32 $\pm$ 0.61 | 10.0 | 0.00 | 0.820 |  Đạt chuẩn | 3.79s |
| Random | 10 | 10.00 | 10.38 $\pm$ 0.86 | 10.0 | 0.00 | 0.809 |  Đạt chuẩn | 2.97s |

---

## 2. Cấu Trúc Nghiệm Tốt Nhất Trong Lần Chạy (Best Solution Clusters)
- **Thuật toán đạt Best:** `PPO-AOS` (Cover = `10` clubs, Fitness = `10.00`)
- **Kích thước các cụm ($s$-clubs):** `[10, 10, 10, 13, 12, 15, 11, 14, 10, 10]`
- **Số thế hệ tiến hóa:** `140` generations

### Chi tiết các cụm $s$-club thành phần:
- **Club 2** (Size = 10 đỉnh): `[0, 4, 9, 16, 28, 41, 69, 90, 93, 104]`
- **Club 8** (Size = 10 đỉnh): `[1, 24, 25, 33, 37, 45, 89, 103, 105, 109]`
- **Club 6** (Size = 10 đỉnh): `[2, 6, 32, 39, 47, 58, 60, 64, 100, 106]`
- **Club 4** (Size = 13 đỉnh): `[3, 5, 10, 11, 40, 52, 72, 74, 81, 84, 98, 102, 107]`
- **Club 3** (Size = 12 đỉnh): `[7, 8, 21, 22, 23, 50, 51, 68, 77, 78, 108, 111]`
- **Club 7** (Size = 15 đỉnh): `[12, 14, 18, 26, 31, 34, 36, 38, 42, 43, 54, 61, 71, 85, 99]`
- **Club 5** (Size = 11 đỉnh): `[13, 15, 46, 49, 53, 67, 73, 83, 88, 110, 114]`
- **Club 9** (Size = 14 đỉnh): `[17, 20, 27, 56, 59, 62, 63, 65, 70, 76, 87, 95, 96, 113]`
- **Club 1** (Size = 10 đỉnh): `[19, 29, 30, 35, 55, 79, 80, 82, 94, 101]`
- **Club 10** (Size = 10 đỉnh): `[44, 48, 57, 66, 75, 86, 91, 92, 97, 112]`

---
*File được sinh tự động bởi hệ thống EVO-RL MSCC Research Framework.*
