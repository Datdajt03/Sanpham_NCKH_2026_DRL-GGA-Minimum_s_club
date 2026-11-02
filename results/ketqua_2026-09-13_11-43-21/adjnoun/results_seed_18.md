# Báo Cáo Kết Quả Thực Nghiệm: Seed #18 (Seed = `20252026`)

**Tập dữ liệu đồ thị:** `adjnoun` ($|V| = 112$, $|E| = 425$, Density = $0.0684$, $s = 2$)  
**Hạt giống cố định (Seed Value):** `20252026` (Lần chạy 18/20 từ `seedun.md`)  
**Thời gian thực thi:** `2026-09-13 11:51:40`  
**Môi trường tính toán:** `Hybrid Co-Processing [CPU: 12 Cores song song (GA/C++ igraph) + GPU: NVIDIA GeForce RTX 3050 Laptop GPU (PPO Tensor Cores)]`  

---

## 1. Bảng Thống Kê Hiệu Năng Chi Tiết Các Thuật Toán (Seed #18)

| Chiến lược / Thuật toán | Best Cover (Min) | Best Fitness | Mean $\pm$ Std | Median | Vi phạm ($diam > s$) | Độ đa dạng | Khả thi ($100\%$) | Thời gian (s) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **PPO-AOS** | **18** | **18.00** | 19.10 $\pm$ 1.39 | 19.0 | 0.00 | 0.796 |  Đạt chuẩn | 14.98s |
| MAB-AOS | 18 | 18.00 | 18.95 $\pm$ 1.73 | 18.0 | 0.00 | 0.925 |  Đạt chuẩn | 10.67s |
| Greedy-AOS | 19 | 19.00 | 19.48 $\pm$ 1.15 | 19.0 | 0.00 | 0.921 |  Đạt chuẩn | 9.21s |
| I-MSM | 21 | 21.00 | 21.40 $\pm$ 0.80 | 21.0 | 0.00 | 0.000 |  Đạt chuẩn | 2.43s |
| CCA | 18 | 18.00 | 18.27 $\pm$ 0.45 | 18.0 | 0.00 | 0.000 |  Đạt chuẩn | 0.44s |
| No-RL | 19 | 19.00 | 19.61 $\pm$ 1.19 | 19.0 | 0.00 | 0.926 |  Đạt chuẩn | 9.08s |
| Fixed | 19 | 19.00 | 19.45 $\pm$ 1.14 | 19.0 | 0.00 | 0.871 |  Đạt chuẩn | 5.82s |
| Random | 19 | 19.00 | 19.61 $\pm$ 1.19 | 19.0 | 0.00 | 0.926 |  Đạt chuẩn | 4.94s |

---

## 2. Cấu Trúc Nghiệm Tốt Nhất Trong Lần Chạy (Best Solution Clusters)
- **Thuật toán đạt Best:** `PPO-AOS` (Cover = `18` clubs, Fitness = `18.00`)
- **Kích thước các cụm ($s$-clubs):** `[13, 5, 4, 28, 10, 7, 4, 7, 3, 3, 4, 3, 4, 3, 5, 1, 5, 3]`
- **Số thế hệ tiến hóa:** `201` generations

### Chi tiết các cụm $s$-club thành phần:
- **Club 5** (Size = 13 đỉnh): `[0, 2, 3, 22, 23, 41, 45, 73, 83, 93, 97, 105, 111]`
- **Club 9** (Size = 5 đỉnh): `[1, 19, 28, 46, 91]`
- **Club 1** (Size = 4 đỉnh): `[4, 53, 89, 99]`
- **Club 17** (Size = 28 đỉnh): `[5, 12, 15, 17, 24, 26, 27, 32, 34, 36, 37, 38, 44, 50, 52, 54, 65, 66, 67, 72, 77, 80, 82, 84, 85, 86, 88, 103]`
- **Club 11** (Size = 10 đỉnh): `[6, 7, 18, 21, 30, 49, 51, 57, 101, 106]`
- **Club 2** (Size = 7 đỉnh): `[8, 9, 39, 40, 60, 61, 62]`
- **Club 3** (Size = 4 đỉnh): `[10, 11, 63, 69]`
- **Club 12** (Size = 7 đỉnh): `[13, 14, 16, 25, 59, 68, 71]`
- **Club 4** (Size = 3 đỉnh): `[20, 94, 108]`
- **Club 13** (Size = 3 đỉnh): `[29, 58, 74]`
- **Club 10** (Size = 4 đỉnh): `[31, 43, 98, 100]`
- **Club 6** (Size = 3 đỉnh): `[33, 76, 107]`
- **Club 7** (Size = 4 đỉnh): `[35, 47, 48, 104]`
- **Club 14** (Size = 3 đỉnh): `[42, 56, 90]`
- **Club 15** (Size = 5 đỉnh): `[55, 70, 75, 87, 102]`
- **Club 18** (Size = 1 đỉnh): `[64]`
- **Club 8** (Size = 5 đỉnh): `[78, 79, 81, 109, 110]`
- **Club 16** (Size = 3 đỉnh): `[92, 95, 96]`

---
*File được sinh tự động bởi hệ thống EVO-RL MSCC Research Framework.*
