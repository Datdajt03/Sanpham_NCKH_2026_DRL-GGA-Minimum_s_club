# Báo Cáo Kết Quả Thực Nghiệm: Seed #19 (Seed = `64086408`)

**Tập dữ liệu đồ thị:** `polbooks` ($|V| = 105$, $|E| = 441$, Density = $0.0808$, $s = 2$)  
**Hạt giống cố định (Seed Value):** `64086408` (Lần chạy 19/20 từ `seedun.md`)  
**Thời gian thực thi:** `2026-09-13 11:49:11`  
**Môi trường tính toán:** `Hybrid Co-Processing [CPU: 12 Cores song song (GA/C++ igraph) + GPU: NVIDIA GeForce RTX 3050 Laptop GPU (PPO Tensor Cores)]`  

---

## 1. Bảng Thống Kê Hiệu Năng Chi Tiết Các Thuật Toán (Seed #19)

| Chiến lược / Thuật toán | Best Cover (Min) | Best Fitness | Mean $\pm$ Std | Median | Vi phạm ($diam > s$) | Độ đa dạng | Khả thi ($100\%$) | Thời gian (s) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **PPO-AOS** | **13** | **13.00** | 13.34 $\pm$ 0.83 | 13.0 | 0.00 | 0.794 |  Đạt chuẩn | 6.35s |
| MAB-AOS | 13 | 13.00 | 13.34 $\pm$ 0.96 | 13.0 | 0.00 | 0.843 |  Đạt chuẩn | 5.92s |
| Greedy-AOS | 14 | 14.00 | 14.17 $\pm$ 0.57 | 14.0 | 0.00 | 0.890 |  Đạt chuẩn | 4.76s |
| I-MSM | 13 | 13.00 | 13.21 $\pm$ 0.52 | 13.0 | 0.00 | 0.000 |  Đạt chuẩn | 1.25s |
| CCA | 13 | 13.00 | 13.58 $\pm$ 0.66 | 13.0 | 0.00 | 0.000 |  Đạt chuẩn | 0.32s |
| No-RL | 13 | 13.00 | 13.30 $\pm$ 0.91 | 13.0 | 0.00 | 0.855 |  Đạt chuẩn | 5.21s |
| Fixed | 13 | 13.00 | 13.26 $\pm$ 0.72 | 13.0 | 0.00 | 0.897 |  Đạt chuẩn | 4.26s |
| Random | 13 | 13.00 | 13.30 $\pm$ 0.91 | 13.0 | 0.00 | 0.855 |  Đạt chuẩn | 4.25s |

---

## 2. Cấu Trúc Nghiệm Tốt Nhất Trong Lần Chạy (Best Solution Clusters)
- **Thuật toán đạt Best:** `PPO-AOS` (Cover = `13` clubs, Fitness = `13.00`)
- **Kích thước các cụm ($s$-clubs):** `[22, 5, 10, 10, 5, 4, 16, 5, 5, 5, 5, 4, 9]`
- **Số thế hệ tiến hóa:** `125` generations

### Chi tiết các cụm $s$-club thành phần:
- **Club 7** (Size = 22 đỉnh): `[0, 1, 3, 5, 8, 9, 10, 11, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27]`
- **Club 13** (Size = 5 đỉnh): `[2, 4, 6, 28, 29]`
- **Club 8** (Size = 10 đỉnh): `[7, 50, 51, 52, 58, 64, 65, 69, 77, 85]`
- **Club 9** (Size = 10 đỉnh): `[12, 32, 33, 36, 41, 44, 46, 47, 54, 55]`
- **Club 6** (Size = 5 đỉnh): `[13, 48, 49, 56, 57]`
- **Club 1** (Size = 4 đỉnh): `[30, 67, 103, 104]`
- **Club 2** (Size = 16 đỉnh): `[31, 66, 70, 73, 75, 76, 82, 83, 84, 86, 89, 92, 93, 96, 97, 100]`
- **Club 10** (Size = 5 đỉnh): `[34, 35, 37, 38, 43]`
- **Club 11** (Size = 5 đỉnh): `[39, 40, 42, 45, 53]`
- **Club 12** (Size = 5 đỉnh): `[59, 60, 62, 63, 99]`
- **Club 3** (Size = 5 đỉnh): `[61, 94, 95, 101, 102]`
- **Club 5** (Size = 4 đỉnh): `[68, 71, 80, 81]`
- **Club 4** (Size = 9 đỉnh): `[72, 74, 78, 79, 87, 88, 90, 91, 98]`

---
*File được sinh tự động bởi hệ thống EVO-RL MSCC Research Framework.*
