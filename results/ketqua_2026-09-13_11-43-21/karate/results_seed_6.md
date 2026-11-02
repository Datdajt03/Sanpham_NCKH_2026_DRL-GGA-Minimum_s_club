# Báo Cáo Kết Quả Thực Nghiệm: Seed #06 (Seed = `20260317`)

**Tập dữ liệu đồ thị:** `karate` ($|V| = 34$, $|E| = 78$, Density = $0.1390$, $s = 2$)  
**Hạt giống cố định (Seed Value):** `20260317` (Lần chạy 06/20 từ `seedun.md`)  
**Thời gian thực thi:** `2026-09-13 11:43:59`  
**Môi trường tính toán:** `Hybrid Co-Processing [CPU: 12 Cores song song (GA/C++ igraph) + GPU: NVIDIA GeForce RTX 3050 Laptop GPU (PPO Tensor Cores)]`  

---

## 1. Bảng Thống Kê Hiệu Năng Chi Tiết Các Thuật Toán (Seed #6)

| Chiến lược / Thuật toán | Best Cover (Min) | Best Fitness | Mean $\pm$ Std | Median | Vi phạm ($diam > s$) | Độ đa dạng | Khả thi ($100\%$) | Thời gian (s) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **PPO-AOS** | **4** | **4.00** | 4.00 $\pm$ 0.00 | 4.0 | 0.00 | 0.737 |  Đạt chuẩn | 9.64s |
| MAB-AOS | 4 | 4.00 | 4.00 $\pm$ 0.00 | 4.0 | 0.00 | 0.614 |  Đạt chuẩn | 3.30s |
| Greedy-AOS | 4 | 4.00 | 4.00 $\pm$ 0.00 | 4.0 | 0.00 | 0.718 |  Đạt chuẩn | 2.83s |
| I-MSM | 4 | 4.00 | 4.00 $\pm$ 0.00 | 4.0 | 0.00 | 0.000 |  Đạt chuẩn | 0.18s |
| CCA | 4 | 4.00 | 4.00 $\pm$ 0.00 | 4.0 | 0.00 | 0.000 |  Đạt chuẩn | 0.02s |
| No-RL | 4 | 4.00 | 4.00 $\pm$ 0.00 | 4.0 | 0.00 | 0.723 |  Đạt chuẩn | 2.48s |
| Fixed | 4 | 4.00 | 4.00 $\pm$ 0.00 | 4.0 | 0.00 | 0.722 |  Đạt chuẩn | 1.79s |
| Random | 4 | 4.00 | 4.00 $\pm$ 0.00 | 4.0 | 0.00 | 0.723 |  Đạt chuẩn | 2.36s |

---

## 2. Cấu Trúc Nghiệm Tốt Nhất Trong Lần Chạy (Best Solution Clusters)
- **Thuật toán đạt Best:** `PPO-AOS` (Cover = `4` clubs, Fitness = `4.00`)
- **Kích thước các cụm ($s$-clubs):** `[11, 4, 15, 4]`
- **Số thế hệ tiến hóa:** `101` generations

### Chi tiết các cụm $s$-club thành phần:
- **Club 2** (Size = 11 đỉnh): `[0, 1, 2, 3, 4, 7, 11, 12, 13, 17, 21]`
- **Club 3** (Size = 4 đỉnh): `[5, 6, 10, 16]`
- **Club 1** (Size = 15 đỉnh): `[8, 9, 14, 15, 18, 19, 20, 22, 23, 26, 27, 29, 30, 32, 33]`
- **Club 4** (Size = 4 đỉnh): `[24, 25, 28, 31]`

---
*File được sinh tự động bởi hệ thống EVO-RL MSCC Research Framework.*
