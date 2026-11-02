# Báo Cáo Kết Quả Thực Nghiệm: Seed #12 (Seed = `12344321`)

**Tập dữ liệu đồ thị:** `hamming6-2` ($|V| = 64$, $|E| = 1824$, Density = $0.9048$, $s = 2$)  
**Hạt giống cố định (Seed Value):** `12344321` (Lần chạy 12/20 từ `seedun.md`)  
**Thời gian thực thi:** `2026-09-13 14:54:23`  
**Môi trường tính toán:** `Hybrid Co-Processing [CPU: 12 Cores song song (GA/C++ igraph) + GPU: NVIDIA GeForce RTX 3050 Laptop GPU (PPO Tensor Cores)]`  

---

## 1. Bảng Thống Kê Hiệu Năng Chi Tiết Các Thuật Toán (Seed #12)

| Chiến lược / Thuật toán | Best Cover (Min) | Best Fitness | Mean $\pm$ Std | Median | Vi phạm ($diam > s$) | Độ đa dạng | Khả thi ($100\%$) | Thời gian (s) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **PPO-AOS** | **1** | **1.00** | 1.01 $\pm$ 0.10 | 1.0 | 0.00 | 0.000 |  Đạt chuẩn | 2.77s |
| MAB-AOS | 1 | 1.00 | 1.01 $\pm$ 0.10 | 1.0 | 0.00 | 0.000 |  Đạt chuẩn | 1.85s |
| Greedy-AOS | 1 | 1.00 | 1.01 $\pm$ 0.10 | 1.0 | 0.00 | 0.000 |  Đạt chuẩn | 1.81s |
| I-MSM | 1 | 1.00 | 1.00 $\pm$ 0.00 | 1.0 | 0.00 | 0.000 |  Đạt chuẩn | 0.95s |
| CCA | 1 | 1.00 | 1.00 $\pm$ 0.00 | 1.0 | 0.00 | 0.000 |  Đạt chuẩn | 0.01s |
| No-RL | 1 | 1.00 | 1.01 $\pm$ 0.10 | 1.0 | 0.00 | 0.000 |  Đạt chuẩn | 1.81s |
| Fixed | 1 | 1.00 | 1.01 $\pm$ 0.10 | 1.0 | 0.00 | 0.000 |  Đạt chuẩn | 1.81s |
| Random | 1 | 1.00 | 1.01 $\pm$ 0.10 | 1.0 | 0.00 | 0.000 |  Đạt chuẩn | 1.79s |

---

## 2. Cấu Trúc Nghiệm Tốt Nhất Trong Lần Chạy (Best Solution Clusters)
- **Thuật toán đạt Best:** `PPO-AOS` (Cover = `1` clubs, Fitness = `1.00`)
- **Kích thước các cụm ($s$-clubs):** `[64]`
- **Số thế hệ tiến hóa:** `102` generations

### Chi tiết các cụm $s$-club thành phần:
- **Club 1** (Size = 64 đỉnh): `[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63]`

---
*File được sinh tự động bởi hệ thống EVO-RL MSCC Research Framework.*
