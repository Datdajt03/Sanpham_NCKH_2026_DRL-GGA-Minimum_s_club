# Báo Cáo Kết Quả Thực Nghiệm: Seed #18 (Seed = `20252026`)

**Tập dữ liệu đồ thị:** `polbooks` ($|V| = 105$, $|E| = 441$, Density = $0.0808$, $s = 2$)  
**Hạt giống cố định (Seed Value):** `20252026` (Lần chạy 18/20 từ `seedun.md`)  
**Thời gian thực thi:** `2026-09-13 11:49:12`  
**Môi trường tính toán:** `Hybrid Co-Processing [CPU: 12 Cores song song (GA/C++ igraph) + GPU: NVIDIA GeForce RTX 3050 Laptop GPU (PPO Tensor Cores)]`  

---

## 1. Bảng Thống Kê Hiệu Năng Chi Tiết Các Thuật Toán (Seed #18)

| Chiến lược / Thuật toán | Best Cover (Min) | Best Fitness | Mean $\pm$ Std | Median | Vi phạm ($diam > s$) | Độ đa dạng | Khả thi ($100\%$) | Thời gian (s) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **PPO-AOS** | **13** | **13.00** | 13.28 $\pm$ 0.72 | 13.0 | 0.00 | 0.898 |  Đạt chuẩn | 6.40s |
| MAB-AOS | 13 | 13.00 | 13.41 $\pm$ 0.87 | 13.0 | 0.00 | 0.819 |  Đạt chuẩn | 5.81s |
| Greedy-AOS | 13 | 13.00 | 13.28 $\pm$ 0.74 | 13.0 | 0.00 | 0.812 |  Đạt chuẩn | 5.91s |
| I-MSM | 14 | 14.00 | 14.00 $\pm$ 0.00 | 14.0 | 0.00 | 0.000 |  Đạt chuẩn | 1.04s |
| CCA | 14 | 14.00 | 14.30 $\pm$ 0.71 | 14.0 | 0.00 | 0.000 |  Đạt chuẩn | 0.24s |
| No-RL | 13 | 13.00 | 13.39 $\pm$ 0.79 | 13.0 | 0.00 | 0.868 |  Đạt chuẩn | 6.00s |
| Fixed | 13 | 13.00 | 13.26 $\pm$ 0.74 | 13.0 | 0.00 | 0.848 |  Đạt chuẩn | 4.22s |
| Random | 13 | 13.00 | 13.39 $\pm$ 0.79 | 13.0 | 0.00 | 0.868 |  Đạt chuẩn | 4.10s |

---

## 2. Cấu Trúc Nghiệm Tốt Nhất Trong Lần Chạy (Best Solution Clusters)
- **Thuật toán đạt Best:** `PPO-AOS` (Cover = `13` clubs, Fitness = `13.00`)
- **Kích thước các cụm ($s$-clubs):** `[13, 6, 10, 12, 8, 9, 5, 19, 5, 3, 7, 4, 4]`
- **Số thế hệ tiến hóa:** `123` generations

### Chi tiết các cụm $s$-club thành phần:
- **Club 8** (Size = 13 đỉnh): `[0, 1, 3, 5, 15, 16, 18, 19, 21, 22, 23, 25, 27]`
- **Club 6** (Size = 6 đỉnh): `[2, 4, 6, 28, 29, 31]`
- **Club 9** (Size = 10 đỉnh): `[7, 50, 51, 52, 58, 64, 65, 68, 69, 85]`
- **Club 10** (Size = 12 đỉnh): `[8, 10, 33, 34, 35, 37, 38, 39, 40, 42, 43, 44]`
- **Club 4** (Size = 8 đỉnh): `[9, 11, 14, 24, 26, 45, 47, 53]`
- **Club 7** (Size = 9 đỉnh): `[12, 13, 17, 32, 36, 41, 46, 54, 55]`
- **Club 11** (Size = 5 đỉnh): `[20, 48, 49, 56, 57]`
- **Club 5** (Size = 19 đỉnh): `[30, 66, 70, 72, 73, 74, 76, 80, 82, 84, 86, 87, 88, 89, 90, 92, 96, 97, 99]`
- **Club 12** (Size = 5 đỉnh): `[59, 60, 61, 62, 63]`
- **Club 1** (Size = 3 đỉnh): `[67, 103, 104]`
- **Club 3** (Size = 7 đỉnh): `[71, 75, 77, 78, 79, 81, 83]`
- **Club 13** (Size = 4 đỉnh): `[91, 98, 100, 101]`
- **Club 2** (Size = 4 đỉnh): `[93, 94, 95, 102]`

---
*File được sinh tự động bởi hệ thống EVO-RL MSCC Research Framework.*
