# Báo Cáo Kết Quả Thực Nghiệm: Seed #11 (Seed = `11223344`)

**Tập dữ liệu đồ thị:** `chesapeake` ($|V| = 39$, $|E| = 170$, Density = $0.2294$, $s = 2$)  
**Hạt giống cố định (Seed Value):** `11223344` (Lần chạy 11/20 từ `seedun.md`)  
**Thời gian thực thi:** `2026-09-13 11:45:17`  
**Môi trường tính toán:** `Hybrid Co-Processing [CPU: 12 Cores song song (GA/C++ igraph) + GPU: NVIDIA GeForce RTX 3050 Laptop GPU (PPO Tensor Cores)]`  

---

## 1. Bảng Thống Kê Hiệu Năng Chi Tiết Các Thuật Toán (Seed #11)

| Chiến lược / Thuật toán | Best Cover (Min) | Best Fitness | Mean $\pm$ Std | Median | Vi phạm ($diam > s$) | Độ đa dạng | Khả thi ($100\%$) | Thời gian (s) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **PPO-AOS** | **3** | **3.00** | 3.00 $\pm$ 0.00 | 3.0 | 0.00 | 0.621 |  Đạt chuẩn | 4.68s |
| MAB-AOS | 3 | 3.00 | 3.00 $\pm$ 0.00 | 3.0 | 0.00 | 0.655 |  Đạt chuẩn | 3.58s |
| Greedy-AOS | 3 | 3.00 | 3.00 $\pm$ 0.00 | 3.0 | 0.00 | 0.697 |  Đạt chuẩn | 3.36s |
| I-MSM | 3 | 3.00 | 3.00 $\pm$ 0.00 | 3.0 | 0.00 | 0.000 |  Đạt chuẩn | 0.38s |
| CCA | 3 | 3.00 | 3.11 $\pm$ 0.31 | 3.0 | 0.00 | 0.000 |  Đạt chuẩn | 0.02s |
| No-RL | 3 | 3.00 | 3.00 $\pm$ 0.00 | 3.0 | 0.00 | 0.550 |  Đạt chuẩn | 3.67s |
| Fixed | 3 | 3.00 | 3.00 $\pm$ 0.00 | 3.0 | 0.00 | 0.616 |  Đạt chuẩn | 2.37s |
| Random | 3 | 3.00 | 3.00 $\pm$ 0.00 | 3.0 | 0.00 | 0.550 |  Đạt chuẩn | 3.74s |

---

## 2. Cấu Trúc Nghiệm Tốt Nhất Trong Lần Chạy (Best Solution Clusters)
- **Thuật toán đạt Best:** `PPO-AOS` (Cover = `3` clubs, Fitness = `3.00`)
- **Kích thước các cụm ($s$-clubs):** `[12, 18, 9]`
- **Số thế hệ tiến hóa:** `101` generations

### Chi tiết các cụm $s$-club thành phần:
- **Club 3** (Size = 12 đỉnh): `[0, 4, 5, 6, 7, 10, 11, 12, 21, 33, 34, 36]`
- **Club 1** (Size = 18 đỉnh): `[1, 2, 3, 8, 9, 15, 16, 17, 18, 19, 20, 22, 23, 24, 27, 29, 32, 35]`
- **Club 2** (Size = 9 đỉnh): `[13, 14, 25, 26, 28, 30, 31, 37, 38]`

---
*File được sinh tự động bởi hệ thống EVO-RL MSCC Research Framework.*
