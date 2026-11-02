# Báo Cáo Kết Quả Thực Nghiệm: Seed #12 (Seed = `12344321`)

**Tập dữ liệu đồ thị:** `chesapeake` ($|V| = 39$, $|E| = 170$, Density = $0.2294$, $s = 2$)  
**Hạt giống cố định (Seed Value):** `12344321` (Lần chạy 12/20 từ `seedun.md`)  
**Thời gian thực thi:** `2026-09-13 11:45:20`  
**Môi trường tính toán:** `Hybrid Co-Processing [CPU: 12 Cores song song (GA/C++ igraph) + GPU: NVIDIA GeForce RTX 3050 Laptop GPU (PPO Tensor Cores)]`  

---

## 1. Bảng Thống Kê Hiệu Năng Chi Tiết Các Thuật Toán (Seed #12)

| Chiến lược / Thuật toán | Best Cover (Min) | Best Fitness | Mean $\pm$ Std | Median | Vi phạm ($diam > s$) | Độ đa dạng | Khả thi ($100\%$) | Thời gian (s) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **PPO-AOS** | **3** | **3.00** | 3.00 $\pm$ 0.00 | 3.0 | 0.00 | 0.672 |  Đạt chuẩn | 4.44s |
| MAB-AOS | 3 | 3.00 | 3.00 $\pm$ 0.00 | 3.0 | 0.00 | 0.567 |  Đạt chuẩn | 3.55s |
| Greedy-AOS | 3 | 3.00 | 3.00 $\pm$ 0.00 | 3.0 | 0.00 | 0.631 |  Đạt chuẩn | 3.81s |
| I-MSM | 3 | 3.00 | 3.00 $\pm$ 0.00 | 3.0 | 0.00 | 0.000 |  Đạt chuẩn | 0.38s |
| CCA | 3 | 3.00 | 3.00 $\pm$ 0.00 | 3.0 | 0.00 | 0.000 |  Đạt chuẩn | 0.01s |
| No-RL | 3 | 3.00 | 3.00 $\pm$ 0.00 | 3.0 | 0.00 | 0.624 |  Đạt chuẩn | 4.20s |
| Fixed | 3 | 3.00 | 3.00 $\pm$ 0.00 | 3.0 | 0.00 | 0.497 |  Đạt chuẩn | 2.28s |
| Random | 3 | 3.00 | 3.00 $\pm$ 0.00 | 3.0 | 0.00 | 0.624 |  Đạt chuẩn | 3.94s |

---

## 2. Cấu Trúc Nghiệm Tốt Nhất Trong Lần Chạy (Best Solution Clusters)
- **Thuật toán đạt Best:** `PPO-AOS` (Cover = `3` clubs, Fitness = `3.00`)
- **Kích thước các cụm ($s$-clubs):** `[14, 24, 1]`
- **Số thế hệ tiến hóa:** `101` generations

### Chi tiết các cụm $s$-club thành phần:
- **Club 1** (Size = 14 đỉnh): `[0, 4, 5, 6, 7, 10, 11, 12, 21, 22, 33, 34, 36, 38]`
- **Club 2** (Size = 24 đỉnh): `[1, 2, 3, 8, 9, 13, 14, 15, 16, 17, 18, 19, 20, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 35]`
- **Club 3** (Size = 1 đỉnh): `[37]`

---
*File được sinh tự động bởi hệ thống EVO-RL MSCC Research Framework.*
