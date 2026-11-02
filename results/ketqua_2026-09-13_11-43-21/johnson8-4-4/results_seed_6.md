# Báo Cáo Kết Quả Thực Nghiệm: Seed #06 (Seed = `20260317`)

**Tập dữ liệu đồ thị:** `johnson8-4-4` ($|V| = 70$, $|E| = 1855$, Density = $0.7681$, $s = 2$)  
**Hạt giống cố định (Seed Value):** `20260317` (Lần chạy 06/20 từ `seedun.md`)  
**Thời gian thực thi:** `2026-09-13 14:55:54`  
**Môi trường tính toán:** `Hybrid Co-Processing [CPU: 12 Cores song song (GA/C++ igraph) + GPU: NVIDIA GeForce RTX 3050 Laptop GPU (PPO Tensor Cores)]`  

---

## 1. Bảng Thống Kê Hiệu Năng Chi Tiết Các Thuật Toán (Seed #6)

| Chiến lược / Thuật toán | Best Cover (Min) | Best Fitness | Mean $\pm$ Std | Median | Vi phạm ($diam > s$) | Độ đa dạng | Khả thi ($100\%$) | Thời gian (s) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **PPO-AOS** | **1** | **1.00** | 1.05 $\pm$ 0.29 | 1.0 | 0.00 | 0.000 |  Đạt chuẩn | 3.85s |
| MAB-AOS | 1 | 1.00 | 1.02 $\pm$ 0.20 | 1.0 | 0.00 | 0.000 |  Đạt chuẩn | 2.60s |
| Greedy-AOS | 1 | 1.00 | 1.02 $\pm$ 0.20 | 1.0 | 0.00 | 0.000 |  Đạt chuẩn | 2.40s |
| I-MSM | 1 | 1.00 | 1.00 $\pm$ 0.00 | 1.0 | 0.00 | 0.000 |  Đạt chuẩn | 1.24s |
| CCA | 1 | 1.00 | 1.00 $\pm$ 0.00 | 1.0 | 0.00 | 0.000 |  Đạt chuẩn | 0.02s |
| No-RL | 1 | 1.00 | 1.05 $\pm$ 0.29 | 1.0 | 0.00 | 0.000 |  Đạt chuẩn | 2.21s |
| Fixed | 1 | 1.00 | 1.02 $\pm$ 0.20 | 1.0 | 0.00 | 0.000 |  Đạt chuẩn | 2.27s |
| Random | 1 | 1.00 | 1.05 $\pm$ 0.29 | 1.0 | 0.00 | 0.000 |  Đạt chuẩn | 2.22s |

---

## 2. Cấu Trúc Nghiệm Tốt Nhất Trong Lần Chạy (Best Solution Clusters)
- **Thuật toán đạt Best:** `PPO-AOS` (Cover = `1` clubs, Fitness = `1.00`)
- **Kích thước các cụm ($s$-clubs):** `[70]`
- **Số thế hệ tiến hóa:** `104` generations

### Chi tiết các cụm $s$-club thành phần:
- **Club 1** (Size = 70 đỉnh): `[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69]`

---
*File được sinh tự động bởi hệ thống EVO-RL MSCC Research Framework.*
