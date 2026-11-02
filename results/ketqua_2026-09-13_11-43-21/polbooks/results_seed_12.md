# Báo Cáo Kết Quả Thực Nghiệm: Seed #12 (Seed = `12344321`)

**Tập dữ liệu đồ thị:** `polbooks` ($|V| = 105$, $|E| = 441$, Density = $0.0808$, $s = 2$)  
**Hạt giống cố định (Seed Value):** `12344321` (Lần chạy 12/20 từ `seedun.md`)  
**Thời gian thực thi:** `2026-09-13 11:49:09`  
**Môi trường tính toán:** `Hybrid Co-Processing [CPU: 12 Cores song song (GA/C++ igraph) + GPU: NVIDIA GeForce RTX 3050 Laptop GPU (PPO Tensor Cores)]`  

---

## 1. Bảng Thống Kê Hiệu Năng Chi Tiết Các Thuật Toán (Seed #12)

| Chiến lược / Thuật toán | Best Cover (Min) | Best Fitness | Mean $\pm$ Std | Median | Vi phạm ($diam > s$) | Độ đa dạng | Khả thi ($100\%$) | Thời gian (s) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **PPO-AOS** | **13** | **13.00** | 13.33 $\pm$ 0.82 | 13.0 | 0.00 | 0.906 |  Đạt chuẩn | 6.58s |
| MAB-AOS | 13 | 13.00 | 13.36 $\pm$ 0.75 | 13.0 | 0.00 | 0.807 |  Đạt chuẩn | 5.91s |
| Greedy-AOS | 13 | 13.00 | 13.34 $\pm$ 0.88 | 13.0 | 0.00 | 0.857 |  Đạt chuẩn | 5.21s |
| I-MSM | 14 | 14.00 | 14.40 $\pm$ 0.80 | 14.0 | 0.00 | 0.000 |  Đạt chuẩn | 1.43s |
| CCA | 14 | 14.00 | 14.30 $\pm$ 0.46 | 14.0 | 0.00 | 0.000 |  Đạt chuẩn | 0.24s |
| No-RL | 13 | 13.00 | 13.48 $\pm$ 0.93 | 13.0 | 0.00 | 0.901 |  Đạt chuẩn | 5.96s |
| Fixed | 13 | 13.00 | 13.08 $\pm$ 0.45 | 13.0 | 0.00 | 0.850 |  Đạt chuẩn | 4.05s |
| Random | 13 | 13.00 | 13.48 $\pm$ 0.93 | 13.0 | 0.00 | 0.901 |  Đạt chuẩn | 5.81s |

---

## 2. Cấu Trúc Nghiệm Tốt Nhất Trong Lần Chạy (Best Solution Clusters)
- **Thuật toán đạt Best:** `PPO-AOS` (Cover = `13` clubs, Fitness = `13.00`)
- **Kích thước các cụm ($s$-clubs):** `[8, 12, 17, 4, 5, 8, 17, 9, 7, 8, 5, 3, 2]`
- **Số thế hệ tiến hóa:** `120` generations

### Chi tiết các cụm $s$-club thành phần:
- **Club 5** (Size = 8 đỉnh): `[0, 1, 2, 4, 5, 6, 7, 29]`
- **Club 6** (Size = 12 đỉnh): `[3, 10, 11, 14, 15, 16, 17, 18, 21, 22, 25, 26]`
- **Club 4** (Size = 17 đỉnh): `[8, 9, 12, 13, 23, 24, 27, 32, 33, 40, 41, 42, 44, 45, 46, 47, 54]`
- **Club 2** (Size = 4 đỉnh): `[19, 55, 56, 77]`
- **Club 7** (Size = 5 đỉnh): `[20, 48, 49, 53, 57]`
- **Club 8** (Size = 8 đỉnh): `[28, 70, 72, 80, 85, 88, 90, 92]`
- **Club 1** (Size = 17 đỉnh): `[30, 66, 73, 76, 81, 82, 83, 84, 86, 89, 93, 94, 96, 97, 99, 100, 101]`
- **Club 3** (Size = 9 đỉnh): `[31, 71, 74, 75, 78, 79, 87, 91, 98]`
- **Club 9** (Size = 7 đỉnh): `[34, 35, 36, 37, 38, 39, 43]`
- **Club 10** (Size = 8 đỉnh): `[50, 51, 52, 58, 64, 65, 68, 69]`
- **Club 11** (Size = 5 đỉnh): `[59, 60, 61, 62, 63]`
- **Club 12** (Size = 3 đỉnh): `[67, 103, 104]`
- **Club 13** (Size = 2 đỉnh): `[95, 102]`

---
*File được sinh tự động bởi hệ thống EVO-RL MSCC Research Framework.*
