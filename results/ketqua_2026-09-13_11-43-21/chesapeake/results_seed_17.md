# Báo Cáo Kết Quả Thực Nghiệm: Seed #17 (Seed = `52013140`)

**Tập dữ liệu đồ thị:** `chesapeake` ($|V| = 39$, $|E| = 170$, Density = $0.2294$, $s = 2$)  
**Hạt giống cố định (Seed Value):** `52013140` (Lần chạy 17/20 từ `seedun.md`)  
**Thời gian thực thi:** `2026-09-13 11:45:20`  
**Môi trường tính toán:** `Hybrid Co-Processing [CPU: 12 Cores song song (GA/C++ igraph) + GPU: NVIDIA GeForce RTX 3050 Laptop GPU (PPO Tensor Cores)]`  

---

## 1. Bảng Thống Kê Hiệu Năng Chi Tiết Các Thuật Toán (Seed #17)

| Chiến lược / Thuật toán | Best Cover (Min) | Best Fitness | Mean $\pm$ Std | Median | Vi phạm ($diam > s$) | Độ đa dạng | Khả thi ($100\%$) | Thời gian (s) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **PPO-AOS** | **3** | **3.00** | 3.00 $\pm$ 0.00 | 3.0 | 0.00 | 0.620 |  Đạt chuẩn | 4.29s |
| MAB-AOS | 3 | 3.00 | 3.00 $\pm$ 0.00 | 3.0 | 0.00 | 0.635 |  Đạt chuẩn | 3.76s |
| Greedy-AOS | 3 | 3.00 | 3.00 $\pm$ 0.00 | 3.0 | 0.00 | 0.548 |  Đạt chuẩn | 3.65s |
| I-MSM | 3 | 3.00 | 3.00 $\pm$ 0.00 | 3.0 | 0.00 | 0.000 |  Đạt chuẩn | 0.40s |
| CCA | 3 | 3.00 | 3.11 $\pm$ 0.31 | 3.0 | 0.00 | 0.000 |  Đạt chuẩn | 0.02s |
| No-RL | 3 | 3.00 | 3.00 $\pm$ 0.00 | 3.0 | 0.00 | 0.603 |  Đạt chuẩn | 3.52s |
| Fixed | 3 | 3.00 | 3.00 $\pm$ 0.00 | 3.0 | 0.00 | 0.578 |  Đạt chuẩn | 2.54s |
| Random | 3 | 3.00 | 3.00 $\pm$ 0.00 | 3.0 | 0.00 | 0.603 |  Đạt chuẩn | 3.41s |

---

## 2. Cấu Trúc Nghiệm Tốt Nhất Trong Lần Chạy (Best Solution Clusters)
- **Thuật toán đạt Best:** `PPO-AOS` (Cover = `3` clubs, Fitness = `3.00`)
- **Kích thước các cụm ($s$-clubs):** `[14, 11, 14]`
- **Số thế hệ tiến hóa:** `101` generations

### Chi tiết các cụm $s$-club thành phần:
- **Club 1** (Size = 14 đỉnh): `[0, 4, 5, 6, 7, 10, 11, 12, 21, 22, 33, 34, 36, 38]`
- **Club 3** (Size = 11 đỉnh): `[1, 2, 3, 8, 9, 13, 14, 15, 16, 17, 35]`
- **Club 2** (Size = 14 đỉnh): `[18, 19, 20, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 37]`

---
*File được sinh tự động bởi hệ thống EVO-RL MSCC Research Framework.*
