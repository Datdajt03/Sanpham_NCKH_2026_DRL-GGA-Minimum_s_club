# Báo Cáo Kết Quả Thực Nghiệm: Seed #20 (Seed = `86088608`)

**Tập dữ liệu đồ thị:** `polbooks` ($|V| = 105$, $|E| = 441$, Density = $0.0808$, $s = 2$)  
**Hạt giống cố định (Seed Value):** `86088608` (Lần chạy 20/20 từ `seedun.md`)  
**Thời gian thực thi:** `2026-09-13 11:49:14`  
**Môi trường tính toán:** `Hybrid Co-Processing [CPU: 12 Cores song song (GA/C++ igraph) + GPU: NVIDIA GeForce RTX 3050 Laptop GPU (PPO Tensor Cores)]`  

---

## 1. Bảng Thống Kê Hiệu Năng Chi Tiết Các Thuật Toán (Seed #20)

| Chiến lược / Thuật toán | Best Cover (Min) | Best Fitness | Mean $\pm$ Std | Median | Vi phạm ($diam > s$) | Độ đa dạng | Khả thi ($100\%$) | Thời gian (s) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **PPO-AOS** | **13** | **13.00** | 13.75 $\pm$ 0.96 | 13.0 | 0.00 | 0.835 |  Đạt chuẩn | 8.32s |
| MAB-AOS | 13 | 13.00 | 13.49 $\pm$ 0.83 | 13.0 | 0.00 | 0.848 |  Đạt chuẩn | 6.62s |
| Greedy-AOS | 14 | 14.00 | 14.26 $\pm$ 0.56 | 14.0 | 0.00 | 0.865 |  Đạt chuẩn | 6.27s |
| I-MSM | 14 | 14.00 | 14.00 $\pm$ 0.00 | 14.0 | 0.00 | 0.000 |  Đạt chuẩn | 1.08s |
| CCA | 14 | 14.00 | 14.52 $\pm$ 0.56 | 14.0 | 0.00 | 0.000 |  Đạt chuẩn | 0.32s |
| No-RL | 13 | 13.00 | 13.49 $\pm$ 0.83 | 13.0 | 0.00 | 0.861 |  Đạt chuẩn | 6.05s |
| Fixed | 13 | 13.00 | 13.26 $\pm$ 0.75 | 13.0 | 0.00 | 0.933 |  Đạt chuẩn | 3.31s |
| Random | 13 | 13.00 | 13.49 $\pm$ 0.83 | 13.0 | 0.00 | 0.861 |  Đạt chuẩn | 3.03s |

---

## 2. Cấu Trúc Nghiệm Tốt Nhất Trong Lần Chạy (Best Solution Clusters)
- **Thuật toán đạt Best:** `PPO-AOS` (Cover = `13` clubs, Fitness = `13.00`)
- **Kích thước các cụm ($s$-clubs):** `[12, 6, 9, 9, 12, 5, 11, 9, 8, 6, 3, 5, 10]`
- **Số thế hệ tiến hóa:** `174` generations

### Chi tiết các cụm $s$-club thành phần:
- **Club 5** (Size = 12 đỉnh): `[0, 3, 9, 10, 14, 16, 19, 21, 22, 23, 25, 27]`
- **Club 6** (Size = 6 đỉnh): `[1, 2, 4, 5, 6, 7]`
- **Club 3** (Size = 9 đỉnh): `[8, 33, 34, 35, 37, 38, 39, 42, 43]`
- **Club 4** (Size = 9 đỉnh): `[11, 13, 17, 26, 29, 45, 47, 50, 56]`
- **Club 7** (Size = 12 đỉnh): `[12, 15, 18, 24, 32, 36, 40, 41, 44, 46, 54, 55]`
- **Club 2** (Size = 5 đỉnh): `[20, 48, 49, 53, 57]`
- **Club 1** (Size = 11 đỉnh): `[28, 66, 70, 71, 72, 80, 85, 88, 89, 90, 92]`
- **Club 8** (Size = 9 đỉnh): `[30, 31, 74, 78, 79, 82, 87, 91, 98]`
- **Club 9** (Size = 8 đỉnh): `[51, 52, 58, 64, 65, 68, 69, 77]`
- **Club 10** (Size = 6 đỉnh): `[59, 60, 61, 62, 63, 99]`
- **Club 11** (Size = 3 đỉnh): `[67, 103, 104]`
- **Club 12** (Size = 5 đỉnh): `[73, 93, 94, 95, 102]`
- **Club 13** (Size = 10 đỉnh): `[75, 76, 81, 83, 84, 86, 96, 97, 100, 101]`

---
*File được sinh tự động bởi hệ thống EVO-RL MSCC Research Framework.*
