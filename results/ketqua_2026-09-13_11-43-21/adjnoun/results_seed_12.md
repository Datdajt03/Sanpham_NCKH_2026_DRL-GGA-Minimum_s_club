# Báo Cáo Kết Quả Thực Nghiệm: Seed #12 (Seed = `12344321`)

**Tập dữ liệu đồ thị:** `adjnoun` ($|V| = 112$, $|E| = 425$, Density = $0.0684$, $s = 2$)  
**Hạt giống cố định (Seed Value):** `12344321` (Lần chạy 12/20 từ `seedun.md`)  
**Thời gian thực thi:** `2026-09-13 11:51:33`  
**Môi trường tính toán:** `Hybrid Co-Processing [CPU: 12 Cores song song (GA/C++ igraph) + GPU: NVIDIA GeForce RTX 3050 Laptop GPU (PPO Tensor Cores)]`  

---

## 1. Bảng Thống Kê Hiệu Năng Chi Tiết Các Thuật Toán (Seed #12)

| Chiến lược / Thuật toán | Best Cover (Min) | Best Fitness | Mean $\pm$ Std | Median | Vi phạm ($diam > s$) | Độ đa dạng | Khả thi ($100\%$) | Thời gian (s) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **PPO-AOS** | **19** | **19.00** | 19.70 $\pm$ 1.31 | 19.0 | 0.00 | 0.847 |  Đạt chuẩn | 13.33s |
| MAB-AOS | 19 | 19.00 | 19.81 $\pm$ 1.75 | 19.0 | 0.00 | 0.905 |  Đạt chuẩn | 9.71s |
| Greedy-AOS | 19 | 19.00 | 19.78 $\pm$ 1.62 | 19.0 | 0.00 | 0.946 |  Đạt chuẩn | 10.24s |
| I-MSM | 20 | 20.00 | 20.61 $\pm$ 0.65 | 21.0 | 0.00 | 0.000 |  Đạt chuẩn | 4.10s |
| CCA | 19 | 19.00 | 19.30 $\pm$ 0.64 | 19.0 | 0.00 | 0.000 |  Đạt chuẩn | 0.40s |
| No-RL | 20 | 20.00 | 20.49 $\pm$ 1.11 | 20.0 | 0.00 | 0.918 |  Đạt chuẩn | 9.85s |
| Fixed | 18 | 18.00 | 18.93 $\pm$ 1.99 | 18.0 | 0.00 | 0.871 |  Đạt chuẩn | 8.47s |
| Random | 20 | 20.00 | 20.49 $\pm$ 1.11 | 20.0 | 0.00 | 0.918 |  Đạt chuẩn | 7.85s |

---

## 2. Cấu Trúc Nghiệm Tốt Nhất Trong Lần Chạy (Best Solution Clusters)
- **Thuật toán đạt Best:** `Fixed` (Cover = `18` clubs, Fitness = `18.00`)
- **Kích thước các cụm ($s$-clubs):** `[5, 11, 4, 8, 2, 36, 6, 4, 5, 4, 6, 6, 5, 2, 3, 1, 3, 1]`
- **Số thế hệ tiến hóa:** `134` generations

### Chi tiết các cụm $s$-club thành phần:
- **Club 2** (Size = 5 đỉnh): `[0, 1, 19, 46, 91]`
- **Club 9** (Size = 11 đỉnh): `[2, 3, 22, 23, 41, 45, 73, 93, 97, 105, 111]`
- **Club 6** (Size = 4 đỉnh): `[4, 53, 89, 99]`
- **Club 7** (Size = 8 đỉnh): `[5, 26, 39, 43, 48, 80, 98, 100]`
- **Club 10** (Size = 2 đỉnh): `[6, 55]`
- **Club 8** (Size = 36 đỉnh): `[7, 12, 13, 15, 17, 21, 25, 27, 28, 31, 32, 34, 35, 36, 37, 38, 44, 50, 52, 54, 65, 66, 67, 70, 72, 77, 82, 83, 84, 85, 86, 87, 88, 102, 103, 104]`
- **Club 11** (Size = 6 đỉnh): `[8, 9, 40, 60, 61, 62]`
- **Club 12** (Size = 4 đỉnh): `[10, 11, 63, 69]`
- **Club 13** (Size = 5 đỉnh): `[14, 16, 59, 68, 71]`
- **Club 14** (Size = 4 đỉnh): `[18, 29, 58, 74]`
- **Club 5** (Size = 6 đỉnh): `[20, 78, 79, 81, 109, 110]`
- **Club 15** (Size = 6 đỉnh): `[24, 47, 49, 75, 76, 108]`
- **Club 17** (Size = 5 đỉnh): `[30, 51, 57, 101, 106]`
- **Club 4** (Size = 2 đỉnh): `[33, 107]`
- **Club 16** (Size = 3 đỉnh): `[42, 56, 90]`
- **Club 1** (Size = 1 đỉnh): `[64]`
- **Club 3** (Size = 3 đỉnh): `[92, 95, 96]`
- **Club 18** (Size = 1 đỉnh): `[94]`

---
*File được sinh tự động bởi hệ thống EVO-RL MSCC Research Framework.*
