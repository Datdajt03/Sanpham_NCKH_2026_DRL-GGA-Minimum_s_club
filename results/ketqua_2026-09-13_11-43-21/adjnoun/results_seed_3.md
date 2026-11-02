# Báo Cáo Kết Quả Thực Nghiệm: Seed #03 (Seed = `23052026`)

**Tập dữ liệu đồ thị:** `adjnoun` ($|V| = 112$, $|E| = 425$, Density = $0.0684$, $s = 2$)  
**Hạt giống cố định (Seed Value):** `23052026` (Lần chạy 03/20 từ `seedun.md`)  
**Thời gian thực thi:** `2026-09-13 11:50:31`  
**Môi trường tính toán:** `Hybrid Co-Processing [CPU: 12 Cores song song (GA/C++ igraph) + GPU: NVIDIA GeForce RTX 3050 Laptop GPU (PPO Tensor Cores)]`  

---

## 1. Bảng Thống Kê Hiệu Năng Chi Tiết Các Thuật Toán (Seed #3)

| Chiến lược / Thuật toán | Best Cover (Min) | Best Fitness | Mean $\pm$ Std | Median | Vi phạm ($diam > s$) | Độ đa dạng | Khả thi ($100\%$) | Thời gian (s) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **PPO-AOS** | **20** | **20.00** | 20.53 $\pm$ 1.27 | 20.0 | 0.00 | 0.891 |  Đạt chuẩn | 13.11s |
| MAB-AOS | 18 | 18.00 | 18.89 $\pm$ 1.72 | 18.0 | 0.00 | 0.852 |  Đạt chuẩn | 8.71s |
| Greedy-AOS | 19 | 19.00 | 19.37 $\pm$ 1.23 | 19.0 | 0.00 | 0.851 |  Đạt chuẩn | 9.05s |
| I-MSM | 20 | 20.00 | 20.00 $\pm$ 0.00 | 20.0 | 0.00 | 0.000 |  Đạt chuẩn | 1.89s |
| CCA | 18 | 18.00 | 18.52 $\pm$ 0.83 | 18.0 | 0.00 | 0.000 |  Đạt chuẩn | 0.42s |
| No-RL | 19 | 19.00 | 19.70 $\pm$ 1.48 | 19.0 | 0.00 | 0.881 |  Đạt chuẩn | 8.33s |
| Fixed | 19 | 19.00 | 19.42 $\pm$ 1.18 | 19.0 | 0.00 | 0.929 |  Đạt chuẩn | 8.52s |
| Random | 19 | 19.00 | 19.70 $\pm$ 1.48 | 19.0 | 0.00 | 0.881 |  Đạt chuẩn | 8.72s |

---

## 2. Cấu Trúc Nghiệm Tốt Nhất Trong Lần Chạy (Best Solution Clusters)
- **Thuật toán đạt Best:** `MAB-AOS` (Cover = `18` clubs, Fitness = `18.00`)
- **Kích thước các cụm ($s$-clubs):** `[17, 6, 4, 26, 9, 7, 5, 5, 3, 7, 6, 3, 3, 3, 3, 1, 3, 1]`
- **Số thế hệ tiến hóa:** `141` generations

### Chi tiết các cụm $s$-club thành phần:
- **Club 3** (Size = 17 đỉnh): `[0, 2, 3, 22, 23, 27, 31, 34, 41, 45, 54, 73, 83, 93, 97, 105, 111]`
- **Club 10** (Size = 6 đỉnh): `[1, 18, 19, 46, 91, 102]`
- **Club 11** (Size = 4 đỉnh): `[4, 53, 89, 99]`
- **Club 12** (Size = 26 đỉnh): `[5, 12, 13, 15, 17, 21, 25, 35, 37, 44, 50, 52, 65, 66, 67, 72, 77, 80, 82, 84, 85, 86, 87, 88, 103, 104]`
- **Club 13** (Size = 9 đỉnh): `[6, 7, 30, 32, 38, 51, 57, 101, 106]`
- **Club 9** (Size = 7 đỉnh): `[8, 9, 39, 40, 60, 61, 62]`
- **Club 5** (Size = 5 đỉnh): `[10, 11, 63, 69, 98]`
- **Club 14** (Size = 5 đỉnh): `[14, 16, 59, 68, 71]`
- **Club 15** (Size = 3 đỉnh): `[20, 94, 108]`
- **Club 16** (Size = 7 đỉnh): `[24, 36, 43, 47, 48, 49, 76]`
- **Club 17** (Size = 6 đỉnh): `[26, 78, 79, 81, 109, 110]`
- **Club 18** (Size = 3 đỉnh): `[28, 33, 107]`
- **Club 6** (Size = 3 đỉnh): `[29, 58, 74]`
- **Club 1** (Size = 3 đỉnh): `[42, 56, 90]`
- **Club 7** (Size = 3 đỉnh): `[55, 70, 75]`
- **Club 2** (Size = 1 đỉnh): `[64]`
- **Club 4** (Size = 3 đỉnh): `[92, 95, 96]`
- **Club 8** (Size = 1 đỉnh): `[100]`

---
*File được sinh tự động bởi hệ thống EVO-RL MSCC Research Framework.*
