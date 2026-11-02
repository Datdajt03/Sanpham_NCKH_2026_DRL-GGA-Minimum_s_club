# Báo Cáo Kết Quả Thực Nghiệm: Seed #10 (Seed = `20260913`)

**Tập dữ liệu đồ thị:** `chesapeake` ($|V| = 39$, $|E| = 170$, Density = $0.2294$, $s = 2$)  
**Hạt giống cố định (Seed Value):** `20260913` (Lần chạy 10/20 từ `seedun.md`)  
**Thời gian thực thi:** `2026-09-13 11:44:58`  
**Môi trường tính toán:** `Hybrid Co-Processing [CPU: 12 Cores song song (GA/C++ igraph) + GPU: NVIDIA GeForce RTX 3050 Laptop GPU (PPO Tensor Cores)]`  

---

## 1. Bảng Thống Kê Hiệu Năng Chi Tiết Các Thuật Toán (Seed #10)

| Chiến lược / Thuật toán | Best Cover (Min) | Best Fitness | Mean $\pm$ Std | Median | Vi phạm ($diam > s$) | Độ đa dạng | Khả thi ($100\%$) | Thời gian (s) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **PPO-AOS** | **3** | **3.00** | 3.00 $\pm$ 0.00 | 3.0 | 0.00 | 0.521 |  Đạt chuẩn | 8.20s |
| MAB-AOS | 3 | 3.00 | 3.00 $\pm$ 0.00 | 3.0 | 0.00 | 0.675 |  Đạt chuẩn | 3.60s |
| Greedy-AOS | 3 | 3.00 | 3.00 $\pm$ 0.00 | 3.0 | 0.00 | 0.483 |  Đạt chuẩn | 3.80s |
| I-MSM | 3 | 3.00 | 3.00 $\pm$ 0.00 | 3.0 | 0.00 | 0.000 |  Đạt chuẩn | 0.40s |
| CCA | 3 | 3.00 | 3.06 $\pm$ 0.24 | 3.0 | 0.00 | 0.000 |  Đạt chuẩn | 0.02s |
| No-RL | 3 | 3.00 | 3.00 $\pm$ 0.00 | 3.0 | 0.00 | 0.609 |  Đạt chuẩn | 3.81s |
| Fixed | 3 | 3.00 | 3.00 $\pm$ 0.00 | 3.0 | 0.00 | 0.687 |  Đạt chuẩn | 2.49s |
| Random | 3 | 3.00 | 3.00 $\pm$ 0.00 | 3.0 | 0.00 | 0.609 |  Đạt chuẩn | 3.87s |

---

## 2. Cấu Trúc Nghiệm Tốt Nhất Trong Lần Chạy (Best Solution Clusters)
- **Thuật toán đạt Best:** `PPO-AOS` (Cover = `3` clubs, Fitness = `3.00`)
- **Kích thước các cụm ($s$-clubs):** `[26, 5, 8]`
- **Số thế hệ tiến hóa:** `101` generations

### Chi tiết các cụm $s$-club thành phần:
- **Club 2** (Size = 26 đỉnh): `[0, 1, 2, 3, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 21, 22, 24, 25, 26, 28, 29, 30, 31, 38]`
- **Club 1** (Size = 5 đỉnh): `[4, 5, 33, 34, 36]`
- **Club 3** (Size = 8 đỉnh): `[18, 19, 20, 23, 27, 32, 35, 37]`

---
*File được sinh tự động bởi hệ thống EVO-RL MSCC Research Framework.*
