# Báo Cáo Kết Quả Thực Nghiệm: Seed #14 (Seed = `24681357`)

**Tập dữ liệu đồ thị:** `chesapeake` ($|V| = 39$, $|E| = 170$, Density = $0.2294$, $s = 2$)  
**Hạt giống cố định (Seed Value):** `24681357` (Lần chạy 14/20 từ `seedun.md`)  
**Thời gian thực thi:** `2026-09-13 11:45:20`  
**Môi trường tính toán:** `Hybrid Co-Processing [CPU: 12 Cores song song (GA/C++ igraph) + GPU: NVIDIA GeForce RTX 3050 Laptop GPU (PPO Tensor Cores)]`  

---

## 1. Bảng Thống Kê Hiệu Năng Chi Tiết Các Thuật Toán (Seed #14)

| Chiến lược / Thuật toán | Best Cover (Min) | Best Fitness | Mean $\pm$ Std | Median | Vi phạm ($diam > s$) | Độ đa dạng | Khả thi ($100\%$) | Thời gian (s) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **PPO-AOS** | **3** | **3.00** | 3.00 $\pm$ 0.00 | 3.0 | 0.00 | 0.544 |  Đạt chuẩn | 4.42s |
| MAB-AOS | 3 | 3.00 | 3.00 $\pm$ 0.00 | 3.0 | 0.00 | 0.599 |  Đạt chuẩn | 3.64s |
| Greedy-AOS | 3 | 3.00 | 3.00 $\pm$ 0.00 | 3.0 | 0.00 | 0.675 |  Đạt chuẩn | 3.73s |
| I-MSM | 3 | 3.00 | 3.00 $\pm$ 0.00 | 3.0 | 0.00 | 0.000 |  Đạt chuẩn | 0.42s |
| CCA | 3 | 3.00 | 3.00 $\pm$ 0.00 | 3.0 | 0.00 | 0.000 |  Đạt chuẩn | 0.01s |
| No-RL | 3 | 3.00 | 3.00 $\pm$ 0.00 | 3.0 | 0.00 | 0.655 |  Đạt chuẩn | 3.55s |
| Fixed | 3 | 3.00 | 3.00 $\pm$ 0.00 | 3.0 | 0.00 | 0.571 |  Đạt chuẩn | 2.47s |
| Random | 3 | 3.00 | 3.00 $\pm$ 0.00 | 3.0 | 0.00 | 0.655 |  Đạt chuẩn | 3.46s |

---

## 2. Cấu Trúc Nghiệm Tốt Nhất Trong Lần Chạy (Best Solution Clusters)
- **Thuật toán đạt Best:** `PPO-AOS` (Cover = `3` clubs, Fitness = `3.00`)
- **Kích thước các cụm ($s$-clubs):** `[18, 3, 18]`
- **Số thế hệ tiến hóa:** `101` generations

### Chi tiết các cụm $s$-club thành phần:
- **Club 1** (Size = 18 đỉnh): `[0, 1, 2, 3, 5, 6, 8, 9, 10, 13, 14, 15, 16, 17, 18, 34, 35, 38]`
- **Club 3** (Size = 3 đỉnh): `[4, 33, 36]`
- **Club 2** (Size = 18 đỉnh): `[7, 11, 12, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 37]`

---
*File được sinh tự động bởi hệ thống EVO-RL MSCC Research Framework.*
