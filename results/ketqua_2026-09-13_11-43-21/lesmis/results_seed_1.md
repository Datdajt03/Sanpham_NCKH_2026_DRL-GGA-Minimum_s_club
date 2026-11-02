# Báo Cáo Kết Quả Thực Nghiệm: Seed #01 (Seed = `17032026`)

**Tập dữ liệu đồ thị:** `lesmis` ($|V| = 77$, $|E| = 262$, Density = $0.0895$, $s = 2$)  
**Hạt giống cố định (Seed Value):** `17032026` (Lần chạy 01/20 từ `seedun.md`)  
**Thời gian thực thi:** `2026-09-13 11:47:14`  
**Môi trường tính toán:** `Hybrid Co-Processing [CPU: 12 Cores song song (GA/C++ igraph) + GPU: NVIDIA GeForce RTX 3050 Laptop GPU (PPO Tensor Cores)]`  

---

## 1. Bảng Thống Kê Hiệu Năng Chi Tiết Các Thuật Toán (Seed #1)

| Chiến lược / Thuật toán | Best Cover (Min) | Best Fitness | Mean $\pm$ Std | Median | Vi phạm ($diam > s$) | Độ đa dạng | Khả thi ($100\%$) | Thời gian (s) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **PPO-AOS** | **10** | **10.00** | 10.00 $\pm$ 0.00 | 10.0 | 0.00 | 0.839 |  Đạt chuẩn | 7.11s |
| MAB-AOS | 10 | 10.00 | 10.00 $\pm$ 0.00 | 10.0 | 0.00 | 0.818 |  Đạt chuẩn | 3.91s |
| Greedy-AOS | 10 | 10.00 | 10.00 $\pm$ 0.00 | 10.0 | 0.00 | 0.866 |  Đạt chuẩn | 3.70s |
| I-MSM | 10 | 10.00 | 10.00 $\pm$ 0.00 | 10.0 | 0.00 | 0.000 |  Đạt chuẩn | 0.68s |
| CCA | 10 | 10.00 | 10.11 $\pm$ 0.31 | 10.0 | 0.00 | 0.000 |  Đạt chuẩn | 0.08s |
| No-RL | 10 | 10.00 | 10.00 $\pm$ 0.00 | 10.0 | 0.00 | 0.808 |  Đạt chuẩn | 3.62s |
| Fixed | 10 | 10.00 | 10.00 $\pm$ 0.00 | 10.0 | 0.00 | 0.868 |  Đạt chuẩn | 2.63s |
| Random | 10 | 10.00 | 10.00 $\pm$ 0.00 | 10.0 | 0.00 | 0.808 |  Đạt chuẩn | 3.60s |

---

## 2. Cấu Trúc Nghiệm Tốt Nhất Trong Lần Chạy (Best Solution Clusters)
- **Thuật toán đạt Best:** `PPO-AOS` (Cover = `10` clubs, Fitness = `10.00`)
- **Kích thước các cụm ($s$-clubs):** `[9, 18, 10, 11, 5, 3, 2, 12, 4, 3]`
- **Số thế hệ tiến hóa:** `101` generations

### Chi tiết các cụm $s$-club thành phần:
- **Club 2** (Size = 9 đỉnh): `[0, 1, 2, 4, 5, 6, 7, 8, 9]`
- **Club 3** (Size = 18 đỉnh): `[3, 10, 11, 12, 13, 14, 15, 18, 30, 32, 33, 34, 35, 36, 37, 38, 43, 72]`
- **Club 9** (Size = 10 đỉnh): `[16, 17, 19, 20, 21, 22, 23, 27, 29, 31]`
- **Club 4** (Size = 11 đỉnh): `[24, 25, 39, 40, 41, 42, 68, 69, 70, 71, 75]`
- **Club 1** (Size = 5 đỉnh): `[26, 49, 50, 54, 56]`
- **Club 8** (Size = 3 đỉnh): `[28, 44, 45]`
- **Club 6** (Size = 2 đỉnh): `[46, 47]`
- **Club 5** (Size = 12 đỉnh): `[48, 59, 60, 61, 62, 63, 64, 65, 66, 73, 74, 76]`
- **Club 10** (Size = 4 đỉnh): `[51, 52, 53, 55]`
- **Club 7** (Size = 3 đỉnh): `[57, 58, 67]`

---
*File được sinh tự động bởi hệ thống EVO-RL MSCC Research Framework.*
