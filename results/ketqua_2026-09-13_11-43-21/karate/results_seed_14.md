# Báo Cáo Kết Quả Thực Nghiệm: Seed #14 (Seed = `24681357`)

**Tập dữ liệu đồ thị:** `karate` ($|V| = 34$, $|E| = 78$, Density = $0.1390$, $s = 2$)  
**Hạt giống cố định (Seed Value):** `24681357` (Lần chạy 14/20 từ `seedun.md`)  
**Thời gian thực thi:** `2026-09-13 11:44:14`  
**Môi trường tính toán:** `Hybrid Co-Processing [CPU: 12 Cores song song (GA/C++ igraph) + GPU: NVIDIA GeForce RTX 3050 Laptop GPU (PPO Tensor Cores)]`  

---

## 1. Bảng Thống Kê Hiệu Năng Chi Tiết Các Thuật Toán (Seed #14)

| Chiến lược / Thuật toán | Best Cover (Min) | Best Fitness | Mean $\pm$ Std | Median | Vi phạm ($diam > s$) | Độ đa dạng | Khả thi ($100\%$) | Thời gian (s) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **PPO-AOS** | **4** | **4.00** | 4.00 $\pm$ 0.00 | 4.0 | 0.00 | 0.701 |  Đạt chuẩn | 3.55s |
| MAB-AOS | 4 | 4.00 | 4.00 $\pm$ 0.00 | 4.0 | 0.00 | 0.715 |  Đạt chuẩn | 2.52s |
| Greedy-AOS | 4 | 4.00 | 4.00 $\pm$ 0.00 | 4.0 | 0.00 | 0.649 |  Đạt chuẩn | 2.33s |
| I-MSM | 4 | 4.00 | 4.00 $\pm$ 0.00 | 4.0 | 0.00 | 0.000 |  Đạt chuẩn | 0.20s |
| CCA | 4 | 4.00 | 4.00 $\pm$ 0.00 | 4.0 | 0.00 | 0.000 |  Đạt chuẩn | 0.01s |
| No-RL | 4 | 4.00 | 4.00 $\pm$ 0.00 | 4.0 | 0.00 | 0.598 |  Đạt chuẩn | 2.39s |
| Fixed | 4 | 4.00 | 4.00 $\pm$ 0.00 | 4.0 | 0.00 | 0.684 |  Đạt chuẩn | 1.69s |
| Random | 4 | 4.00 | 4.00 $\pm$ 0.00 | 4.0 | 0.00 | 0.598 |  Đạt chuẩn | 2.38s |

---

## 2. Cấu Trúc Nghiệm Tốt Nhất Trong Lần Chạy (Best Solution Clusters)
- **Thuật toán đạt Best:** `PPO-AOS` (Cover = `4` clubs, Fitness = `4.00`)
- **Kích thước các cụm ($s$-clubs):** `[11, 4, 14, 5]`
- **Số thế hệ tiến hóa:** `101` generations

### Chi tiết các cụm $s$-club thành phần:
- **Club 1** (Size = 11 đỉnh): `[0, 1, 2, 3, 4, 7, 11, 12, 17, 19, 21]`
- **Club 4** (Size = 4 đỉnh): `[5, 6, 10, 16]`
- **Club 3** (Size = 14 đỉnh): `[8, 9, 13, 14, 15, 18, 20, 22, 26, 28, 29, 30, 32, 33]`
- **Club 2** (Size = 5 đỉnh): `[23, 24, 25, 27, 31]`

---
*File được sinh tự động bởi hệ thống EVO-RL MSCC Research Framework.*
