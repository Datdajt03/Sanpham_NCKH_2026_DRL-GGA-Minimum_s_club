# Báo Cáo Kết Quả Thực Nghiệm: Seed #09 (Seed = `20260626`)

**Tập dữ liệu đồ thị:** `lesmis` ($|V| = 77$, $|E| = 262$, Density = $0.0895$, $s = 2$)  
**Hạt giống cố định (Seed Value):** `20260626` (Lần chạy 09/20 từ `seedun.md`)  
**Thời gian thực thi:** `2026-09-13 11:47:16`  
**Môi trường tính toán:** `Hybrid Co-Processing [CPU: 12 Cores song song (GA/C++ igraph) + GPU: NVIDIA GeForce RTX 3050 Laptop GPU (PPO Tensor Cores)]`  

---

## 1. Bảng Thống Kê Hiệu Năng Chi Tiết Các Thuật Toán (Seed #9)

| Chiến lược / Thuật toán | Best Cover (Min) | Best Fitness | Mean $\pm$ Std | Median | Vi phạm ($diam > s$) | Độ đa dạng | Khả thi ($100\%$) | Thời gian (s) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **PPO-AOS** | **10** | **10.00** | 10.00 $\pm$ 0.00 | 10.0 | 0.00 | 0.735 |  Đạt chuẩn | 7.03s |
| MAB-AOS | 10 | 10.00 | 10.00 $\pm$ 0.00 | 10.0 | 0.00 | 0.884 |  Đạt chuẩn | 4.16s |
| Greedy-AOS | 10 | 10.00 | 10.00 $\pm$ 0.00 | 10.0 | 0.00 | 0.847 |  Đạt chuẩn | 3.83s |
| I-MSM | 10 | 10.00 | 10.24 $\pm$ 0.43 | 10.0 | 0.00 | 0.000 |  Đạt chuẩn | 0.90s |
| CCA | 10 | 10.00 | 10.06 $\pm$ 0.24 | 10.0 | 0.00 | 0.000 |  Đạt chuẩn | 0.10s |
| No-RL | 10 | 10.00 | 10.00 $\pm$ 0.00 | 10.0 | 0.00 | 0.903 |  Đạt chuẩn | 3.91s |
| Fixed | 10 | 10.00 | 10.00 $\pm$ 0.00 | 10.0 | 0.00 | 0.839 |  Đạt chuẩn | 2.84s |
| Random | 10 | 10.00 | 10.00 $\pm$ 0.00 | 10.0 | 0.00 | 0.903 |  Đạt chuẩn | 3.96s |

---

## 2. Cấu Trúc Nghiệm Tốt Nhất Trong Lần Chạy (Best Solution Clusters)
- **Thuật toán đạt Best:** `PPO-AOS` (Cover = `10` clubs, Fitness = `10.00`)
- **Kích thước các cụm ($s$-clubs):** `[10, 24, 7, 8, 5, 7, 1, 2, 10, 3]`
- **Số thế hệ tiến hóa:** `101` generations

### Chi tiết các cụm $s$-club thành phần:
- **Club 4** (Size = 10 đỉnh): `[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]`
- **Club 8** (Size = 24 đỉnh): `[10, 11, 12, 13, 14, 15, 18, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 43, 44, 68, 71, 72]`
- **Club 6** (Size = 7 đỉnh): `[16, 17, 19, 20, 21, 22, 23]`
- **Club 5** (Size = 8 đỉnh): `[24, 25, 39, 40, 42, 69, 70, 75]`
- **Club 3** (Size = 5 đỉnh): `[26, 49, 50, 54, 56]`
- **Club 2** (Size = 7 đỉnh): `[41, 55, 57, 62, 63, 65, 67]`
- **Club 10** (Size = 1 đỉnh): `[45]`
- **Club 9** (Size = 2 đỉnh): `[46, 47]`
- **Club 1** (Size = 10 đỉnh): `[48, 58, 59, 60, 61, 64, 66, 73, 74, 76]`
- **Club 7** (Size = 3 đỉnh): `[51, 52, 53]`

---
*File được sinh tự động bởi hệ thống EVO-RL MSCC Research Framework.*
