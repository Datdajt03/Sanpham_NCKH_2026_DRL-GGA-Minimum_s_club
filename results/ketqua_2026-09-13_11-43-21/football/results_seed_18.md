# Báo Cáo Kết Quả Thực Nghiệm: Seed #18 (Seed = `20252026`)

**Tập dữ liệu đồ thị:** `football` ($|V| = 115$, $|E| = 613$, Density = $0.0935$, $s = 2$)  
**Hạt giống cố định (Seed Value):** `20252026` (Lần chạy 18/20 từ `seedun.md`)  
**Thời gian thực thi:** `2026-09-13 11:53:01`  
**Môi trường tính toán:** `Hybrid Co-Processing [CPU: 12 Cores song song (GA/C++ igraph) + GPU: NVIDIA GeForce RTX 3050 Laptop GPU (PPO Tensor Cores)]`  

---

## 1. Bảng Thống Kê Hiệu Năng Chi Tiết Các Thuật Toán (Seed #18)

| Chiến lược / Thuật toán | Best Cover (Min) | Best Fitness | Mean $\pm$ Std | Median | Vi phạm ($diam > s$) | Độ đa dạng | Khả thi ($100\%$) | Thời gian (s) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **PPO-AOS** | **10** | **10.00** | 10.28 $\pm$ 0.73 | 10.0 | 0.00 | 0.767 |  Đạt chuẩn | 5.95s |
| MAB-AOS | 10 | 10.00 | 10.40 $\pm$ 0.87 | 10.0 | 0.00 | 0.832 |  Đạt chuẩn | 5.31s |
| Greedy-AOS | 10 | 10.00 | 10.32 $\pm$ 0.85 | 10.0 | 0.00 | 0.863 |  Đạt chuẩn | 4.88s |
| I-MSM | 12 | 12.00 | 12.82 $\pm$ 0.90 | 13.0 | 0.00 | 0.000 |  Đạt chuẩn | 1.32s |
| CCA | 14 | 14.00 | 14.06 $\pm$ 0.24 | 14.0 | 0.00 | 0.000 |  Đạt chuẩn | 0.15s |
| No-RL | 10 | 10.00 | 10.28 $\pm$ 0.88 | 10.0 | 0.00 | 0.792 |  Đạt chuẩn | 4.87s |
| Fixed | 10 | 10.00 | 10.19 $\pm$ 0.64 | 10.0 | 0.00 | 0.847 |  Đạt chuẩn | 3.34s |
| Random | 10 | 10.00 | 10.28 $\pm$ 0.88 | 10.0 | 0.00 | 0.792 |  Đạt chuẩn | 3.77s |

---

## 2. Cấu Trúc Nghiệm Tốt Nhất Trong Lần Chạy (Best Solution Clusters)
- **Thuật toán đạt Best:** `PPO-AOS` (Cover = `10` clubs, Fitness = `10.00`)
- **Kích thước các cụm ($s$-clubs):** `[12, 10, 11, 11, 12, 15, 14, 9, 11, 10]`
- **Số thế hệ tiến hóa:** `122` generations

### Chi tiết các cụm $s$-club thành phần:
- **Club 1** (Size = 12 đỉnh): `[0, 4, 9, 11, 16, 23, 28, 41, 69, 90, 93, 104]`
- **Club 8** (Size = 10 đỉnh): `[1, 24, 25, 33, 37, 45, 89, 103, 105, 109]`
- **Club 4** (Size = 11 đỉnh): `[2, 6, 13, 15, 32, 39, 47, 60, 64, 100, 106]`
- **Club 9** (Size = 11 đỉnh): `[3, 5, 10, 52, 72, 74, 81, 84, 98, 102, 107]`
- **Club 6** (Size = 12 đỉnh): `[7, 8, 21, 22, 40, 50, 51, 68, 77, 78, 108, 111]`
- **Club 5** (Size = 15 đỉnh): `[12, 14, 18, 26, 31, 34, 36, 38, 42, 43, 54, 61, 71, 85, 99]`
- **Club 2** (Size = 14 đỉnh): `[17, 20, 27, 56, 59, 62, 63, 65, 70, 76, 87, 95, 96, 113]`
- **Club 7** (Size = 9 đỉnh): `[19, 29, 30, 35, 55, 79, 82, 94, 101]`
- **Club 10** (Size = 11 đỉnh): `[44, 48, 57, 66, 75, 80, 86, 91, 92, 97, 112]`
- **Club 3** (Size = 10 đỉnh): `[46, 49, 53, 58, 67, 73, 83, 88, 110, 114]`

---
*File được sinh tự động bởi hệ thống EVO-RL MSCC Research Framework.*
