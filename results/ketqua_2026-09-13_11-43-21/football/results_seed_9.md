# Báo Cáo Kết Quả Thực Nghiệm: Seed #09 (Seed = `20260626`)

**Tập dữ liệu đồ thị:** `football` ($|V| = 115$, $|E| = 613$, Density = $0.0935$, $s = 2$)  
**Hạt giống cố định (Seed Value):** `20260626` (Lần chạy 09/20 từ `seedun.md`)  
**Thời gian thực thi:** `2026-09-13 11:52:31`  
**Môi trường tính toán:** `Hybrid Co-Processing [CPU: 12 Cores song song (GA/C++ igraph) + GPU: NVIDIA GeForce RTX 3050 Laptop GPU (PPO Tensor Cores)]`  

---

## 1. Bảng Thống Kê Hiệu Năng Chi Tiết Các Thuật Toán (Seed #9)

| Chiến lược / Thuật toán | Best Cover (Min) | Best Fitness | Mean $\pm$ Std | Median | Vi phạm ($diam > s$) | Độ đa dạng | Khả thi ($100\%$) | Thời gian (s) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **PPO-AOS** | **10** | **10.00** | 10.29 $\pm$ 0.77 | 10.0 | 0.00 | 0.836 |  Đạt chuẩn | 7.35s |
| MAB-AOS | 10 | 10.00 | 10.21 $\pm$ 0.67 | 10.0 | 0.00 | 0.848 |  Đạt chuẩn | 5.01s |
| Greedy-AOS | 10 | 10.00 | 10.26 $\pm$ 0.76 | 10.0 | 0.00 | 0.868 |  Đạt chuẩn | 4.64s |
| I-MSM | 12 | 12.00 | 13.03 $\pm$ 1.14 | 12.0 | 0.00 | 0.000 |  Đạt chuẩn | 1.37s |
| CCA | 14 | 14.00 | 14.20 $\pm$ 0.40 | 14.0 | 0.00 | 0.000 |  Đạt chuẩn | 0.18s |
| No-RL | 10 | 10.00 | 10.33 $\pm$ 0.73 | 10.0 | 0.00 | 0.881 |  Đạt chuẩn | 5.15s |
| Fixed | 10 | 10.00 | 10.47 $\pm$ 0.67 | 10.0 | 0.00 | 0.857 |  Đạt chuẩn | 4.65s |
| Random | 10 | 10.00 | 10.33 $\pm$ 0.73 | 10.0 | 0.00 | 0.881 |  Đạt chuẩn | 4.93s |

---

## 2. Cấu Trúc Nghiệm Tốt Nhất Trong Lần Chạy (Best Solution Clusters)
- **Thuật toán đạt Best:** `PPO-AOS` (Cover = `10` clubs, Fitness = `10.00`)
- **Kích thước các cụm ($s$-clubs):** `[11, 10, 11, 13, 11, 14, 14, 11, 10, 10]`
- **Số thế hệ tiến hóa:** `118` generations

### Chi tiết các cụm $s$-club thành phần:
- **Club 6** (Size = 11 đỉnh): `[0, 4, 9, 16, 23, 28, 41, 69, 90, 93, 104]`
- **Club 3** (Size = 10 đỉnh): `[1, 24, 25, 33, 37, 45, 89, 103, 105, 109]`
- **Club 7** (Size = 11 đỉnh): `[2, 6, 13, 15, 32, 39, 47, 60, 64, 100, 106]`
- **Club 8** (Size = 13 đỉnh): `[3, 5, 10, 11, 40, 52, 72, 74, 81, 84, 98, 102, 107]`
- **Club 4** (Size = 11 đỉnh): `[7, 8, 21, 22, 50, 51, 68, 77, 78, 108, 111]`
- **Club 9** (Size = 14 đỉnh): `[12, 14, 18, 26, 31, 34, 36, 38, 43, 54, 61, 71, 85, 99]`
- **Club 1** (Size = 14 đỉnh): `[17, 20, 27, 56, 59, 62, 63, 65, 70, 76, 87, 95, 96, 113]`
- **Club 5** (Size = 11 đỉnh): `[19, 29, 30, 35, 42, 55, 79, 80, 82, 94, 101]`
- **Club 10** (Size = 10 đỉnh): `[44, 48, 57, 66, 75, 86, 91, 92, 97, 112]`
- **Club 2** (Size = 10 đỉnh): `[46, 49, 53, 58, 67, 73, 83, 88, 110, 114]`

---
*File được sinh tự động bởi hệ thống EVO-RL MSCC Research Framework.*
