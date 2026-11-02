# Báo Cáo Kết Quả Thực Nghiệm: Seed #03 (Seed = `23052026`)

**Tập dữ liệu đồ thị:** `dolphins` ($|V| = 62$, $|E| = 159$, Density = $0.0841$, $s = 2$)  
**Hạt giống cố định (Seed Value):** `23052026` (Lần chạy 03/20 từ `seedun.md`)  
**Thời gian thực thi:** `2026-09-13 11:46:05`  
**Môi trường tính toán:** `Hybrid Co-Processing [CPU: 12 Cores song song (GA/C++ igraph) + GPU: NVIDIA GeForce RTX 3050 Laptop GPU (PPO Tensor Cores)]`  

---

## 1. Bảng Thống Kê Hiệu Năng Chi Tiết Các Thuật Toán (Seed #3)

| Chiến lược / Thuật toán | Best Cover (Min) | Best Fitness | Mean $\pm$ Std | Median | Vi phạm ($diam > s$) | Độ đa dạng | Khả thi ($100\%$) | Thời gian (s) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **PPO-AOS** | **13** | **13.00** | 13.16 $\pm$ 0.45 | 13.0 | 0.00 | 0.907 |  Đạt chuẩn | 5.85s |
| MAB-AOS | 13 | 13.00 | 13.34 $\pm$ 0.57 | 13.0 | 0.00 | 0.872 |  Đạt chuẩn | 4.59s |
| Greedy-AOS | 13 | 13.00 | 13.41 $\pm$ 0.62 | 13.0 | 0.00 | 0.502 |  Đạt chuẩn | 4.66s |
| I-MSM | 14 | 14.00 | 14.17 $\pm$ 0.50 | 14.0 | 0.00 | 0.000 |  Đạt chuẩn | 0.45s |
| CCA | 14 | 14.00 | 14.30 $\pm$ 0.46 | 14.0 | 0.00 | 0.000 |  Đạt chuẩn | 0.16s |
| No-RL | 13 | 13.00 | 13.30 $\pm$ 0.66 | 13.0 | 0.00 | 0.817 |  Đạt chuẩn | 3.82s |
| Fixed | 13 | 13.00 | 13.13 $\pm$ 0.41 | 13.0 | 0.00 | 0.897 |  Đạt chuẩn | 3.01s |
| Random | 13 | 13.00 | 13.30 $\pm$ 0.66 | 13.0 | 0.00 | 0.817 |  Đạt chuẩn | 3.93s |

---

## 2. Cấu Trúc Nghiệm Tốt Nhất Trong Lần Chạy (Best Solution Clusters)
- **Thuật toán đạt Best:** `PPO-AOS` (Cover = `13` clubs, Fitness = `13.00`)
- **Kích thước các cụm ($s$-clubs):** `[7, 5, 3, 5, 6, 7, 2, 3, 8, 4, 7, 3, 2]`
- **Số thế hệ tiến hóa:** `115` generations

### Chi tiết các cụm $s$-club thành phần:
- **Club 5** (Size = 7 đỉnh): `[0, 10, 20, 28, 30, 42, 47]`
- **Club 3** (Size = 5 đỉnh): `[1, 7, 19, 26, 27]`
- **Club 6** (Size = 3 đỉnh): `[2, 53, 61]`
- **Club 7** (Size = 5 đỉnh): `[3, 8, 15, 36, 59]`
- **Club 8** (Size = 6 đỉnh): `[4, 11, 23, 45, 51, 55]`
- **Club 9** (Size = 7 đỉnh): `[5, 13, 39, 41, 48, 54, 57]`
- **Club 10** (Size = 2 đỉnh): `[6, 56]`
- **Club 4** (Size = 3 đỉnh): `[9, 32, 60]`
- **Club 11** (Size = 8 đỉnh): `[12, 14, 16, 33, 34, 37, 40, 50]`
- **Club 12** (Size = 4 đỉnh): `[17, 22, 25, 31]`
- **Club 2** (Size = 7 đỉnh): `[18, 21, 24, 29, 35, 43, 52]`
- **Club 13** (Size = 3 đỉnh): `[38, 44, 58]`
- **Club 1** (Size = 2 đỉnh): `[46, 49]`

---
*File được sinh tự động bởi hệ thống EVO-RL MSCC Research Framework.*
