# Báo Cáo Kết Quả Thực Nghiệm: Seed #09 (Seed = `20260626`)

**Tập dữ liệu đồ thị:** `adjnoun` ($|V| = 112$, $|E| = 425$, Density = $0.0684$, $s = 2$)  
**Hạt giống cố định (Seed Value):** `20260626` (Lần chạy 09/20 từ `seedun.md`)  
**Thời gian thực thi:** `2026-09-13 11:50:46`  
**Môi trường tính toán:** `Hybrid Co-Processing [CPU: 12 Cores song song (GA/C++ igraph) + GPU: NVIDIA GeForce RTX 3050 Laptop GPU (PPO Tensor Cores)]`  

---

## 1. Bảng Thống Kê Hiệu Năng Chi Tiết Các Thuật Toán (Seed #9)

| Chiến lược / Thuật toán | Best Cover (Min) | Best Fitness | Mean $\pm$ Std | Median | Vi phạm ($diam > s$) | Độ đa dạng | Khả thi ($100\%$) | Thời gian (s) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **PPO-AOS** | **20** | **20.00** | 20.48 $\pm$ 1.19 | 20.0 | 0.00 | 0.852 |  Đạt chuẩn | 12.84s |
| MAB-AOS | 18 | 18.00 | 19.22 $\pm$ 2.08 | 18.0 | 0.00 | 0.870 |  Đạt chuẩn | 12.68s |
| Greedy-AOS | 20 | 20.00 | 20.82 $\pm$ 1.15 | 21.0 | 0.00 | 0.915 |  Đạt chuẩn | 12.60s |
| I-MSM | 19 | 19.00 | 19.12 $\pm$ 0.47 | 19.0 | 0.00 | 0.000 |  Đạt chuẩn | 2.10s |
| CCA | 18 | 18.00 | 18.47 $\pm$ 0.50 | 18.0 | 0.00 | 0.000 |  Đạt chuẩn | 0.61s |
| No-RL | 19 | 19.00 | 20.19 $\pm$ 1.89 | 19.0 | 0.00 | 0.877 |  Đạt chuẩn | 11.40s |
| Fixed | 18 | 18.00 | 18.99 $\pm$ 1.68 | 18.0 | 0.00 | 0.905 |  Đạt chuẩn | 9.81s |
| Random | 19 | 19.00 | 20.19 $\pm$ 1.89 | 19.0 | 0.00 | 0.877 |  Đạt chuẩn | 12.02s |

---

## 2. Cấu Trúc Nghiệm Tốt Nhất Trong Lần Chạy (Best Solution Clusters)
- **Thuật toán đạt Best:** `MAB-AOS` (Cover = `18` clubs, Fitness = `18.00`)
- **Kích thước các cụm ($s$-clubs):** `[7, 11, 4, 37, 7, 7, 4, 6, 4, 5, 4, 2, 3, 1, 1, 5, 3, 1]`
- **Số thế hệ tiến hóa:** `156` generations

### Chi tiết các cụm $s$-club thành phần:
- **Club 6** (Size = 7 đỉnh): `[0, 1, 18, 41, 45, 46, 91]`
- **Club 4** (Size = 11 đỉnh): `[2, 3, 21, 22, 23, 34, 73, 93, 97, 105, 111]`
- **Club 7** (Size = 4 đỉnh): `[4, 53, 89, 99]`
- **Club 8** (Size = 37 đỉnh): `[5, 7, 12, 15, 17, 25, 26, 27, 31, 32, 35, 36, 37, 38, 43, 44, 50, 52, 54, 65, 66, 67, 70, 72, 77, 80, 82, 83, 84, 85, 86, 87, 88, 98, 102, 103, 104]`
- **Club 9** (Size = 7 đỉnh): `[6, 30, 49, 51, 57, 101, 106]`
- **Club 2** (Size = 7 đỉnh): `[8, 9, 39, 40, 60, 61, 62]`
- **Club 10** (Size = 4 đỉnh): `[10, 11, 63, 69]`
- **Club 11** (Size = 6 đỉnh): `[13, 14, 16, 59, 68, 71]`
- **Club 12** (Size = 4 đỉnh): `[19, 20, 94, 108]`
- **Club 13** (Size = 5 đỉnh): `[24, 47, 48, 75, 76]`
- **Club 14** (Size = 4 đỉnh): `[28, 29, 58, 74]`
- **Club 15** (Size = 2 đỉnh): `[33, 107]`
- **Club 5** (Size = 3 đỉnh): `[42, 56, 90]`
- **Club 16** (Size = 1 đỉnh): `[55]`
- **Club 17** (Size = 1 đỉnh): `[64]`
- **Club 1** (Size = 5 đỉnh): `[78, 79, 81, 109, 110]`
- **Club 18** (Size = 3 đỉnh): `[92, 95, 96]`
- **Club 3** (Size = 1 đỉnh): `[100]`

---
*File được sinh tự động bởi hệ thống EVO-RL MSCC Research Framework.*
