# Báo Cáo Kết Quả Thực Nghiệm: Seed #19 (Seed = `64086408`)

**Tập dữ liệu đồ thị:** `adjnoun` ($|V| = 112$, $|E| = 425$, Density = $0.0684$, $s = 2$)  
**Hạt giống cố định (Seed Value):** `64086408` (Lần chạy 19/20 từ `seedun.md`)  
**Thời gian thực thi:** `2026-09-13 11:51:38`  
**Môi trường tính toán:** `Hybrid Co-Processing [CPU: 12 Cores song song (GA/C++ igraph) + GPU: NVIDIA GeForce RTX 3050 Laptop GPU (PPO Tensor Cores)]`  

---

## 1. Bảng Thống Kê Hiệu Năng Chi Tiết Các Thuật Toán (Seed #19)

| Chiến lược / Thuật toán | Best Cover (Min) | Best Fitness | Mean $\pm$ Std | Median | Vi phạm ($diam > s$) | Độ đa dạng | Khả thi ($100\%$) | Thời gian (s) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **PPO-AOS** | **19** | **19.00** | 19.65 $\pm$ 1.44 | 19.0 | 0.00 | 0.867 |  Đạt chuẩn | 10.04s |
| MAB-AOS | 19 | 19.00 | 19.71 $\pm$ 1.48 | 19.0 | 0.00 | 0.893 |  Đạt chuẩn | 8.61s |
| Greedy-AOS | 18 | 18.00 | 18.81 $\pm$ 1.67 | 18.0 | 0.00 | 0.932 |  Đạt chuẩn | 9.10s |
| I-MSM | 19 | 19.00 | 20.24 $\pm$ 1.21 | 21.0 | 0.00 | 0.000 |  Đạt chuẩn | 4.69s |
| CCA | 18 | 18.00 | 18.81 $\pm$ 0.93 | 18.0 | 0.00 | 0.000 |  Đạt chuẩn | 0.70s |
| No-RL | 19 | 19.00 | 19.77 $\pm$ 1.50 | 19.0 | 0.00 | 0.907 |  Đạt chuẩn | 8.30s |
| Fixed | 18 | 18.00 | 18.66 $\pm$ 1.49 | 18.0 | 0.00 | 0.921 |  Đạt chuẩn | 7.59s |
| Random | 19 | 19.00 | 19.77 $\pm$ 1.50 | 19.0 | 0.00 | 0.907 |  Đạt chuẩn | 5.83s |

---

## 2. Cấu Trúc Nghiệm Tốt Nhất Trong Lần Chạy (Best Solution Clusters)
- **Thuật toán đạt Best:** `Greedy-AOS` (Cover = `18` clubs, Fitness = `18.00`)
- **Kích thước các cụm ($s$-clubs):** `[5, 13, 3, 29, 7, 7, 7, 5, 5, 4, 3, 3, 4, 3, 3, 5, 2, 4]`
- **Số thế hệ tiến hóa:** `137` generations

### Chi tiết các cụm $s$-club thành phần:
- **Club 11** (Size = 5 đỉnh): `[0, 1, 46, 91, 102]`
- **Club 8** (Size = 13 đỉnh): `[2, 3, 11, 22, 24, 36, 41, 45, 73, 93, 97, 98, 111]`
- **Club 7** (Size = 3 đỉnh): `[4, 89, 99]`
- **Club 12** (Size = 29 đỉnh): `[5, 17, 25, 26, 27, 28, 31, 32, 34, 35, 37, 38, 44, 52, 54, 65, 66, 67, 72, 77, 80, 82, 84, 85, 86, 87, 88, 103, 104]`
- **Club 13** (Size = 7 đỉnh): `[6, 7, 49, 51, 57, 101, 106]`
- **Club 1** (Size = 7 đỉnh): `[8, 9, 39, 40, 60, 61, 62]`
- **Club 14** (Size = 7 đỉnh): `[10, 12, 18, 21, 50, 53, 78]`
- **Club 5** (Size = 5 đỉnh): `[13, 14, 16, 59, 71]`
- **Club 2** (Size = 5 đỉnh): `[15, 43, 48, 83, 100]`
- **Club 6** (Size = 4 đỉnh): `[19, 23, 47, 69]`
- **Club 15** (Size = 3 đỉnh): `[20, 94, 108]`
- **Club 16** (Size = 3 đỉnh): `[29, 58, 74]`
- **Club 3** (Size = 4 đỉnh): `[30, 92, 95, 96]`
- **Club 4** (Size = 3 đỉnh): `[33, 76, 107]`
- **Club 17** (Size = 3 đỉnh): `[42, 56, 90]`
- **Club 10** (Size = 5 đỉnh): `[55, 68, 70, 75, 105]`
- **Club 18** (Size = 2 đỉnh): `[63, 64]`
- **Club 9** (Size = 4 đỉnh): `[79, 81, 109, 110]`

---
*File được sinh tự động bởi hệ thống EVO-RL MSCC Research Framework.*
