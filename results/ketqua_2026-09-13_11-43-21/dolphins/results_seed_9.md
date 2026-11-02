# Báo Cáo Kết Quả Thực Nghiệm: Seed #09 (Seed = `20260626`)

**Tập dữ liệu đồ thị:** `dolphins` ($|V| = 62$, $|E| = 159$, Density = $0.0841$, $s = 2$)  
**Hạt giống cố định (Seed Value):** `20260626` (Lần chạy 09/20 từ `seedun.md`)  
**Thời gian thực thi:** `2026-09-13 11:46:04`  
**Môi trường tính toán:** `Hybrid Co-Processing [CPU: 12 Cores song song (GA/C++ igraph) + GPU: NVIDIA GeForce RTX 3050 Laptop GPU (PPO Tensor Cores)]`  

---

## 1. Bảng Thống Kê Hiệu Năng Chi Tiết Các Thuật Toán (Seed #9)

| Chiến lược / Thuật toán | Best Cover (Min) | Best Fitness | Mean $\pm$ Std | Median | Vi phạm ($diam > s$) | Độ đa dạng | Khả thi ($100\%$) | Thời gian (s) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **PPO-AOS** | **14** | **14.00** | 14.16 $\pm$ 0.43 | 14.0 | 0.00 | 0.886 |  Đạt chuẩn | 6.60s |
| MAB-AOS | 13 | 13.00 | 13.27 $\pm$ 0.65 | 13.0 | 0.00 | 0.880 |  Đạt chuẩn | 4.00s |
| Greedy-AOS | 13 | 13.00 | 13.25 $\pm$ 0.74 | 13.0 | 0.00 | 0.852 |  Đạt chuẩn | 3.58s |
| I-MSM | 14 | 14.00 | 14.52 $\pm$ 0.88 | 14.0 | 0.00 | 0.000 |  Đạt chuẩn | 0.58s |
| CCA | 15 | 15.00 | 15.00 $\pm$ 0.00 | 15.0 | 0.00 | 0.000 |  Đạt chuẩn | 0.10s |
| No-RL | 13 | 13.00 | 13.37 $\pm$ 0.79 | 13.0 | 0.00 | 0.889 |  Đạt chuẩn | 3.81s |
| Fixed | 13 | 13.00 | 13.24 $\pm$ 0.63 | 13.0 | 0.00 | 0.871 |  Đạt chuẩn | 3.24s |
| Random | 13 | 13.00 | 13.37 $\pm$ 0.79 | 13.0 | 0.00 | 0.889 |  Đạt chuẩn | 3.79s |

---

## 2. Cấu Trúc Nghiệm Tốt Nhất Trong Lần Chạy (Best Solution Clusters)
- **Thuật toán đạt Best:** `MAB-AOS` (Cover = `13` clubs, Fitness = `13.00`)
- **Kích thước các cụm ($s$-clubs):** `[6, 7, 3, 5, 8, 4, 7, 3, 4, 5, 5, 3, 2]`
- **Số thế hệ tiến hóa:** `122` generations

### Chi tiết các cụm $s$-club thành phần:
- **Club 1** (Size = 6 đỉnh): `[0, 10, 28, 30, 42, 47]`
- **Club 10** (Size = 7 đỉnh): `[1, 7, 19, 26, 27, 41, 54]`
- **Club 6** (Size = 3 đỉnh): `[2, 53, 61]`
- **Club 11** (Size = 5 đỉnh): `[3, 8, 15, 36, 59]`
- **Club 5** (Size = 8 đỉnh): `[4, 11, 23, 24, 45, 50, 51, 55]`
- **Club 2** (Size = 4 đỉnh): `[5, 6, 9, 56]`
- **Club 9** (Size = 7 đỉnh): `[12, 14, 16, 33, 34, 37, 40]`
- **Club 7** (Size = 3 đỉnh): `[13, 32, 60]`
- **Club 3** (Size = 4 đỉnh): `[17, 22, 25, 31]`
- **Club 4** (Size = 5 đỉnh): `[18, 21, 29, 35, 43]`
- **Club 12** (Size = 5 đỉnh): `[20, 38, 44, 52, 58]`
- **Club 13** (Size = 3 đỉnh): `[39, 48, 57]`
- **Club 8** (Size = 2 đỉnh): `[46, 49]`

---
*File được sinh tự động bởi hệ thống EVO-RL MSCC Research Framework.*
