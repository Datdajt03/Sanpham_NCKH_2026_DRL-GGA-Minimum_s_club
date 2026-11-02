# Báo Cáo Kết Quả Thực Nghiệm: Seed #17 (Seed = `52013140`)

**Tập dữ liệu đồ thị:** `karate` ($|V| = 34$, $|E| = 78$, Density = $0.1390$, $s = 2$)  
**Hạt giống cố định (Seed Value):** `52013140` (Lần chạy 17/20 từ `seedun.md`)  
**Thời gian thực thi:** `2026-09-13 11:44:14`  
**Môi trường tính toán:** `Hybrid Co-Processing [CPU: 12 Cores song song (GA/C++ igraph) + GPU: NVIDIA GeForce RTX 3050 Laptop GPU (PPO Tensor Cores)]`  

---

## 1. Bảng Thống Kê Hiệu Năng Chi Tiết Các Thuật Toán (Seed #17)

| Chiến lược / Thuật toán | Best Cover (Min) | Best Fitness | Mean $\pm$ Std | Median | Vi phạm ($diam > s$) | Độ đa dạng | Khả thi ($100\%$) | Thời gian (s) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **PPO-AOS** | **4** | **4.00** | 4.00 $\pm$ 0.00 | 4.0 | 0.00 | 0.795 |  Đạt chuẩn | 3.46s |
| MAB-AOS | 4 | 4.00 | 4.00 $\pm$ 0.00 | 4.0 | 0.00 | 0.689 |  Đạt chuẩn | 2.44s |
| Greedy-AOS | 4 | 4.00 | 4.00 $\pm$ 0.00 | 4.0 | 0.00 | 0.726 |  Đạt chuẩn | 2.45s |
| I-MSM | 4 | 4.00 | 4.00 $\pm$ 0.00 | 4.0 | 0.00 | 0.000 |  Đạt chuẩn | 0.18s |
| CCA | 4 | 4.00 | 4.00 $\pm$ 0.00 | 4.0 | 0.00 | 0.000 |  Đạt chuẩn | 0.02s |
| No-RL | 4 | 4.00 | 4.00 $\pm$ 0.00 | 4.0 | 0.00 | 0.733 |  Đạt chuẩn | 2.25s |
| Fixed | 4 | 4.00 | 4.00 $\pm$ 0.00 | 4.0 | 0.00 | 0.715 |  Đạt chuẩn | 1.58s |
| Random | 4 | 4.00 | 4.00 $\pm$ 0.00 | 4.0 | 0.00 | 0.733 |  Đạt chuẩn | 2.25s |

---

## 2. Cấu Trúc Nghiệm Tốt Nhất Trong Lần Chạy (Best Solution Clusters)
- **Thuật toán đạt Best:** `PPO-AOS` (Cover = `4` clubs, Fitness = `4.00`)
- **Kích thước các cụm ($s$-clubs):** `[11, 4, 15, 4]`
- **Số thế hệ tiến hóa:** `101` generations

### Chi tiết các cụm $s$-club thành phần:
- **Club 2** (Size = 11 đỉnh): `[0, 1, 2, 3, 7, 10, 11, 12, 13, 17, 21]`
- **Club 4** (Size = 4 đỉnh): `[4, 5, 6, 16]`
- **Club 1** (Size = 15 đỉnh): `[8, 9, 14, 15, 18, 19, 20, 22, 23, 26, 28, 29, 30, 32, 33]`
- **Club 3** (Size = 4 đỉnh): `[24, 25, 27, 31]`

---
*File được sinh tự động bởi hệ thống EVO-RL MSCC Research Framework.*
