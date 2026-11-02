# Báo Cáo Kết Quả Thực Nghiệm: Seed #12 (Seed = `12344321`)

**Tập dữ liệu đồ thị:** `dolphins` ($|V| = 62$, $|E| = 159$, Density = $0.0841$, $s = 2$)  
**Hạt giống cố định (Seed Value):** `12344321` (Lần chạy 12/20 từ `seedun.md`)  
**Thời gian thực thi:** `2026-09-13 11:46:27`  
**Môi trường tính toán:** `Hybrid Co-Processing [CPU: 12 Cores song song (GA/C++ igraph) + GPU: NVIDIA GeForce RTX 3050 Laptop GPU (PPO Tensor Cores)]`  

---

## 1. Bảng Thống Kê Hiệu Năng Chi Tiết Các Thuật Toán (Seed #12)

| Chiến lược / Thuật toán | Best Cover (Min) | Best Fitness | Mean $\pm$ Std | Median | Vi phạm ($diam > s$) | Độ đa dạng | Khả thi ($100\%$) | Thời gian (s) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **PPO-AOS** | **13** | **13.00** | 13.34 $\pm$ 0.53 | 13.0 | 0.00 | 0.716 |  Đạt chuẩn | 6.00s |
| MAB-AOS | 14 | 14.00 | 14.06 $\pm$ 0.23 | 14.0 | 0.00 | 0.844 |  Đạt chuẩn | 3.54s |
| Greedy-AOS | 14 | 14.00 | 14.09 $\pm$ 0.29 | 14.0 | 0.00 | 0.822 |  Đạt chuẩn | 3.76s |
| I-MSM | 14 | 14.00 | 14.11 $\pm$ 0.31 | 14.0 | 0.00 | 0.000 |  Đạt chuẩn | 0.47s |
| CCA | 14 | 14.00 | 14.41 $\pm$ 0.49 | 14.0 | 0.00 | 0.000 |  Đạt chuẩn | 0.17s |
| No-RL | 14 | 14.00 | 14.11 $\pm$ 0.31 | 14.0 | 0.00 | 0.925 |  Đạt chuẩn | 3.75s |
| Fixed | 13 | 13.00 | 13.20 $\pm$ 0.49 | 13.0 | 0.00 | 0.848 |  Đạt chuẩn | 3.16s |
| Random | 14 | 14.00 | 14.11 $\pm$ 0.31 | 14.0 | 0.00 | 0.925 |  Đạt chuẩn | 3.67s |

---

## 2. Cấu Trúc Nghiệm Tốt Nhất Trong Lần Chạy (Best Solution Clusters)
- **Thuật toán đạt Best:** `PPO-AOS` (Cover = `13` clubs, Fitness = `13.00`)
- **Kích thước các cụm ($s$-clubs):** `[6, 6, 3, 8, 7, 3, 7, 5, 4, 5, 4, 2, 2]`
- **Số thế hệ tiến hóa:** `147` generations

### Chi tiết các cụm $s$-club thành phần:
- **Club 1** (Size = 6 đỉnh): `[0, 7, 30, 40, 42, 47]`
- **Club 5** (Size = 6 đỉnh): `[1, 19, 26, 27, 28, 36]`
- **Club 6** (Size = 3 đỉnh): `[2, 53, 61]`
- **Club 7** (Size = 8 đỉnh): `[3, 8, 14, 15, 24, 45, 50, 59]`
- **Club 8** (Size = 7 đỉnh): `[4, 11, 18, 21, 23, 51, 55]`
- **Club 4** (Size = 3 đỉnh): `[5, 13, 56]`
- **Club 9** (Size = 7 đỉnh): `[6, 9, 39, 41, 48, 54, 57]`
- **Club 2** (Size = 5 đỉnh): `[10, 29, 35, 43, 52]`
- **Club 10** (Size = 4 đỉnh): `[12, 33, 34, 37]`
- **Club 3** (Size = 5 đỉnh): `[16, 20, 38, 44, 58]`
- **Club 11** (Size = 4 đỉnh): `[17, 22, 25, 31]`
- **Club 12** (Size = 2 đỉnh): `[32, 60]`
- **Club 13** (Size = 2 đỉnh): `[46, 49]`

---
*File được sinh tự động bởi hệ thống EVO-RL MSCC Research Framework.*
