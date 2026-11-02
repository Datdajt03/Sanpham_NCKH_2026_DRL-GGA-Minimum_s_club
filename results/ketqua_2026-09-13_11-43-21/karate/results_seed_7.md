# Báo Cáo Kết Quả Thực Nghiệm: Seed #07 (Seed = `20260421`)

**Tập dữ liệu đồ thị:** `karate` ($|V| = 34$, $|E| = 78$, Density = $0.1390$, $s = 2$)  
**Hạt giống cố định (Seed Value):** `20260421` (Lần chạy 07/20 từ `seedun.md`)  
**Thời gian thực thi:** `2026-09-13 11:44:00`  
**Môi trường tính toán:** `Hybrid Co-Processing [CPU: 12 Cores song song (GA/C++ igraph) + GPU: NVIDIA GeForce RTX 3050 Laptop GPU (PPO Tensor Cores)]`  

---

## 1. Bảng Thống Kê Hiệu Năng Chi Tiết Các Thuật Toán (Seed #7)

| Chiến lược / Thuật toán | Best Cover (Min) | Best Fitness | Mean $\pm$ Std | Median | Vi phạm ($diam > s$) | Độ đa dạng | Khả thi ($100\%$) | Thời gian (s) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **PPO-AOS** | **4** | **4.00** | 4.00 $\pm$ 0.00 | 4.0 | 0.00 | 0.694 |  Đạt chuẩn | 9.33s |
| MAB-AOS | 4 | 4.00 | 4.00 $\pm$ 0.00 | 4.0 | 0.00 | 0.764 |  Đạt chuẩn | 3.38s |
| Greedy-AOS | 4 | 4.00 | 4.00 $\pm$ 0.00 | 4.0 | 0.00 | 0.773 |  Đạt chuẩn | 2.80s |
| I-MSM | 4 | 4.00 | 4.00 $\pm$ 0.00 | 4.0 | 0.00 | 0.000 |  Đạt chuẩn | 0.18s |
| CCA | 4 | 4.00 | 4.00 $\pm$ 0.00 | 4.0 | 0.00 | 0.000 |  Đạt chuẩn | 0.02s |
| No-RL | 4 | 4.00 | 4.00 $\pm$ 0.00 | 4.0 | 0.00 | 0.788 |  Đạt chuẩn | 2.97s |
| Fixed | 4 | 4.00 | 4.00 $\pm$ 0.00 | 4.0 | 0.00 | 0.739 |  Đạt chuẩn | 1.76s |
| Random | 4 | 4.00 | 4.00 $\pm$ 0.00 | 4.0 | 0.00 | 0.788 |  Đạt chuẩn | 2.85s |

---

## 2. Cấu Trúc Nghiệm Tốt Nhất Trong Lần Chạy (Best Solution Clusters)
- **Thuật toán đạt Best:** `PPO-AOS` (Cover = `4` clubs, Fitness = `4.00`)
- **Kích thước các cụm ($s$-clubs):** `[13, 3, 14, 4]`
- **Số thế hệ tiến hóa:** `101` generations

### Chi tiết các cụm $s$-club thành phần:
- **Club 1** (Size = 13 đỉnh): `[0, 1, 2, 3, 4, 7, 10, 11, 12, 13, 17, 19, 21]`
- **Club 3** (Size = 3 đỉnh): `[5, 6, 16]`
- **Club 2** (Size = 14 đỉnh): `[8, 9, 14, 15, 18, 20, 22, 26, 28, 29, 30, 31, 32, 33]`
- **Club 4** (Size = 4 đỉnh): `[23, 24, 25, 27]`

---
*File được sinh tự động bởi hệ thống EVO-RL MSCC Research Framework.*
