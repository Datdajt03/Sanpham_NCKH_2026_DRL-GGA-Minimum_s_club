# Báo Cáo Kết Quả Thực Nghiệm: Seed #18 (Seed = `20252026`)

**Tập dữ liệu đồ thị:** `lesmis` ($|V| = 77$, $|E| = 262$, Density = $0.0895$, $s = 2$)  
**Hạt giống cố định (Seed Value):** `20252026` (Lần chạy 18/20 từ `seedun.md`)  
**Thời gian thực thi:** `2026-09-13 11:47:41`  
**Môi trường tính toán:** `Hybrid Co-Processing [CPU: 12 Cores song song (GA/C++ igraph) + GPU: NVIDIA GeForce RTX 3050 Laptop GPU (PPO Tensor Cores)]`  

---

## 1. Bảng Thống Kê Hiệu Năng Chi Tiết Các Thuật Toán (Seed #18)

| Chiến lược / Thuật toán | Best Cover (Min) | Best Fitness | Mean $\pm$ Std | Median | Vi phạm ($diam > s$) | Độ đa dạng | Khả thi ($100\%$) | Thời gian (s) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **PPO-AOS** | **10** | **10.00** | 10.05 $\pm$ 0.21 | 10.0 | 0.00 | 0.775 |  Đạt chuẩn | 5.00s |
| MAB-AOS | 10 | 10.00 | 10.02 $\pm$ 0.14 | 10.0 | 0.00 | 0.865 |  Đạt chuẩn | 4.20s |
| Greedy-AOS | 10 | 10.00 | 10.03 $\pm$ 0.17 | 10.0 | 0.00 | 0.823 |  Đạt chuẩn | 3.69s |
| I-MSM | 10 | 10.00 | 10.24 $\pm$ 0.43 | 10.0 | 0.00 | 0.000 |  Đạt chuẩn | 0.94s |
| CCA | 10 | 10.00 | 10.00 $\pm$ 0.00 | 10.0 | 0.00 | 0.000 |  Đạt chuẩn | 0.09s |
| No-RL | 10 | 10.00 | 10.02 $\pm$ 0.14 | 10.0 | 0.00 | 0.858 |  Đạt chuẩn | 4.11s |
| Fixed | 10 | 10.00 | 10.01 $\pm$ 0.10 | 10.0 | 0.00 | 0.883 |  Đạt chuẩn | 2.71s |
| Random | 10 | 10.00 | 10.02 $\pm$ 0.14 | 10.0 | 0.00 | 0.858 |  Đạt chuẩn | 3.20s |

---

## 2. Cấu Trúc Nghiệm Tốt Nhất Trong Lần Chạy (Best Solution Clusters)
- **Thuật toán đạt Best:** `PPO-AOS` (Cover = `10` clubs, Fitness = `10.00`)
- **Kích thước các cụm ($s$-clubs):** `[10, 24, 8, 4, 5, 1, 2, 16, 3, 4]`
- **Số thế hệ tiến hóa:** `106` generations

### Chi tiết các cụm $s$-club thành phần:
- **Club 4** (Size = 10 đỉnh): `[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]`
- **Club 1** (Size = 24 đỉnh): `[10, 11, 12, 13, 14, 15, 23, 24, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 43, 44, 70, 72]`
- **Club 7** (Size = 8 đỉnh): `[16, 17, 18, 19, 20, 21, 22, 26]`
- **Club 5** (Size = 4 đỉnh): `[25, 39, 40, 42]`
- **Club 8** (Size = 5 đỉnh): `[41, 55, 57, 64, 67]`
- **Club 10** (Size = 1 đỉnh): `[45]`
- **Club 6** (Size = 2 đỉnh): `[46, 47]`
- **Club 9** (Size = 16 đỉnh): `[48, 58, 59, 60, 61, 62, 63, 65, 66, 68, 69, 71, 73, 74, 75, 76]`
- **Club 3** (Size = 3 đỉnh): `[49, 50, 56]`
- **Club 2** (Size = 4 đỉnh): `[51, 52, 53, 54]`

---
*File được sinh tự động bởi hệ thống EVO-RL MSCC Research Framework.*
