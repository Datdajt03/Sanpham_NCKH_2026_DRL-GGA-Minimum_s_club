# Báo Cáo Kết Quả Thực Nghiệm: Seed #05 (Seed = `13092026`)

**Tập dữ liệu đồ thị:** `karate` ($|V| = 34$, $|E| = 78$, Density = $0.1390$, $s = 2$)  
**Hạt giống cố định (Seed Value):** `13092026` (Lần chạy 05/20 từ `seedun.md`)  
**Thời gian thực thi:** `2026-09-13 11:43:58`  
**Môi trường tính toán:** `Hybrid Co-Processing [CPU: 12 Cores song song (GA/C++ igraph) + GPU: NVIDIA GeForce RTX 3050 Laptop GPU (PPO Tensor Cores)]`  

---

## 1. Bảng Thống Kê Hiệu Năng Chi Tiết Các Thuật Toán (Seed #5)

| Chiến lược / Thuật toán | Best Cover (Min) | Best Fitness | Mean $\pm$ Std | Median | Vi phạm ($diam > s$) | Độ đa dạng | Khả thi ($100\%$) | Thời gian (s) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **PPO-AOS** | **4** | **4.00** | 4.00 $\pm$ 0.00 | 4.0 | 0.00 | 0.741 |  Đạt chuẩn | 8.67s |
| MAB-AOS | 4 | 4.00 | 4.00 $\pm$ 0.00 | 4.0 | 0.00 | 0.725 |  Đạt chuẩn | 3.02s |
| Greedy-AOS | 4 | 4.00 | 4.00 $\pm$ 0.00 | 4.0 | 0.00 | 0.756 |  Đạt chuẩn | 2.73s |
| I-MSM | 4 | 4.00 | 4.00 $\pm$ 0.00 | 4.0 | 0.00 | 0.000 |  Đạt chuẩn | 0.19s |
| CCA | 4 | 4.00 | 4.00 $\pm$ 0.00 | 4.0 | 0.00 | 0.000 |  Đạt chuẩn | 0.02s |
| No-RL | 4 | 4.00 | 4.00 $\pm$ 0.00 | 4.0 | 0.00 | 0.714 |  Đạt chuẩn | 2.61s |
| Fixed | 4 | 4.00 | 4.00 $\pm$ 0.00 | 4.0 | 0.00 | 0.750 |  Đạt chuẩn | 1.71s |
| Random | 4 | 4.00 | 4.00 $\pm$ 0.00 | 4.0 | 0.00 | 0.714 |  Đạt chuẩn | 2.52s |

---

## 2. Cấu Trúc Nghiệm Tốt Nhất Trong Lần Chạy (Best Solution Clusters)
- **Thuật toán đạt Best:** `PPO-AOS` (Cover = `4` clubs, Fitness = `4.00`)
- **Kích thước các cụm ($s$-clubs):** `[10, 4, 18, 2]`
- **Số thế hệ tiến hóa:** `101` generations

### Chi tiết các cụm $s$-club thành phần:
- **Club 2** (Size = 10 đỉnh): `[0, 1, 2, 3, 7, 10, 11, 12, 17, 21]`
- **Club 3** (Size = 4 đỉnh): `[4, 5, 6, 16]`
- **Club 1** (Size = 18 đỉnh): `[8, 9, 13, 14, 15, 18, 19, 20, 22, 23, 26, 27, 28, 29, 30, 31, 32, 33]`
- **Club 4** (Size = 2 đỉnh): `[24, 25]`

---
*File được sinh tự động bởi hệ thống EVO-RL MSCC Research Framework.*
