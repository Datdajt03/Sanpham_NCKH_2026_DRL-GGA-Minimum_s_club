# Báo Cáo Kết Quả Thực Nghiệm: Seed #01 (Seed = `17032026`)

**Tập dữ liệu đồ thị:** `football` ($|V| = 115$, $|E| = 613$, Density = $0.0935$, $s = 2$)  
**Hạt giống cố định (Seed Value):** `17032026` (Lần chạy 01/20 từ `seedun.md`)  
**Thời gian thực thi:** `2026-09-13 11:52:29`  
**Môi trường tính toán:** `Hybrid Co-Processing [CPU: 12 Cores song song (GA/C++ igraph) + GPU: NVIDIA GeForce RTX 3050 Laptop GPU (PPO Tensor Cores)]`  

---

## 1. Bảng Thống Kê Hiệu Năng Chi Tiết Các Thuật Toán (Seed #1)

| Chiến lược / Thuật toán | Best Cover (Min) | Best Fitness | Mean $\pm$ Std | Median | Vi phạm ($diam > s$) | Độ đa dạng | Khả thi ($100\%$) | Thời gian (s) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **PPO-AOS** | **10** | **10.00** | 10.34 $\pm$ 0.89 | 10.0 | 0.00 | 0.857 |  Đạt chuẩn | 8.14s |
| MAB-AOS | 10 | 10.00 | 10.21 $\pm$ 0.65 | 10.0 | 0.00 | 0.885 |  Đạt chuẩn | 4.90s |
| Greedy-AOS | 10 | 10.00 | 10.44 $\pm$ 1.04 | 10.0 | 0.00 | 0.817 |  Đạt chuẩn | 4.91s |
| I-MSM | 13 | 13.00 | 13.12 $\pm$ 0.47 | 13.0 | 0.00 | 0.000 |  Đạt chuẩn | 0.69s |
| CCA | 14 | 14.00 | 14.11 $\pm$ 0.31 | 14.0 | 0.00 | 0.000 |  Đạt chuẩn | 0.17s |
| No-RL | 10 | 10.00 | 10.27 $\pm$ 0.77 | 10.0 | 0.00 | 0.858 |  Đạt chuẩn | 4.86s |
| Fixed | 10 | 10.00 | 10.18 $\pm$ 0.61 | 10.0 | 0.00 | 0.838 |  Đạt chuẩn | 3.33s |
| Random | 10 | 10.00 | 10.27 $\pm$ 0.77 | 10.0 | 0.00 | 0.858 |  Đạt chuẩn | 4.59s |

---

## 2. Cấu Trúc Nghiệm Tốt Nhất Trong Lần Chạy (Best Solution Clusters)
- **Thuật toán đạt Best:** `PPO-AOS` (Cover = `10` clubs, Fitness = `10.00`)
- **Kích thước các cụm ($s$-clubs):** `[10, 10, 11, 13, 11, 13, 14, 12, 10, 11]`
- **Số thế hệ tiến hóa:** `121` generations

### Chi tiết các cụm $s$-club thành phần:
- **Club 5** (Size = 10 đỉnh): `[0, 4, 9, 16, 23, 28, 41, 90, 93, 104]`
- **Club 2** (Size = 10 đỉnh): `[1, 24, 25, 33, 37, 45, 89, 103, 105, 109]`
- **Club 6** (Size = 11 đỉnh): `[2, 6, 13, 15, 32, 39, 47, 60, 64, 100, 106]`
- **Club 1** (Size = 13 đỉnh): `[3, 5, 10, 11, 40, 52, 72, 74, 81, 84, 98, 102, 107]`
- **Club 4** (Size = 11 đỉnh): `[7, 8, 21, 22, 50, 51, 68, 77, 78, 108, 111]`
- **Club 7** (Size = 13 đỉnh): `[12, 14, 18, 26, 31, 36, 38, 43, 54, 61, 71, 85, 99]`
- **Club 8** (Size = 14 đỉnh): `[17, 20, 27, 56, 59, 62, 63, 65, 70, 76, 87, 95, 96, 113]`
- **Club 3** (Size = 12 đỉnh): `[19, 29, 30, 34, 35, 42, 55, 79, 80, 82, 94, 101]`
- **Club 10** (Size = 10 đỉnh): `[44, 48, 57, 66, 75, 86, 91, 92, 97, 112]`
- **Club 9** (Size = 11 đỉnh): `[46, 49, 53, 58, 67, 69, 73, 83, 88, 110, 114]`

---
*File được sinh tự động bởi hệ thống EVO-RL MSCC Research Framework.*
