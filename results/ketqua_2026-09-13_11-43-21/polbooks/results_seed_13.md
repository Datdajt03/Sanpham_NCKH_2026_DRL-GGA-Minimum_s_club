# Báo Cáo Kết Quả Thực Nghiệm: Seed #13 (Seed = `13572468`)

**Tập dữ liệu đồ thị:** `polbooks` ($|V| = 105$, $|E| = 441$, Density = $0.0808$, $s = 2$)  
**Hạt giống cố định (Seed Value):** `13572468` (Lần chạy 13/20 từ `seedun.md`)  
**Thời gian thực thi:** `2026-09-13 11:49:08`  
**Môi trường tính toán:** `Hybrid Co-Processing [CPU: 12 Cores song song (GA/C++ igraph) + GPU: NVIDIA GeForce RTX 3050 Laptop GPU (PPO Tensor Cores)]`  

---

## 1. Bảng Thống Kê Hiệu Năng Chi Tiết Các Thuật Toán (Seed #13)

| Chiến lược / Thuật toán | Best Cover (Min) | Best Fitness | Mean $\pm$ Std | Median | Vi phạm ($diam > s$) | Độ đa dạng | Khả thi ($100\%$) | Thời gian (s) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **PPO-AOS** | **13** | **13.00** | 13.46 $\pm$ 0.81 | 13.0 | 0.00 | 0.837 |  Đạt chuẩn | 7.45s |
| MAB-AOS | 13 | 13.00 | 13.50 $\pm$ 0.83 | 13.0 | 0.00 | 0.875 |  Đạt chuẩn | 6.45s |
| Greedy-AOS | 14 | 14.00 | 14.07 $\pm$ 0.33 | 14.0 | 0.00 | 0.929 |  Đạt chuẩn | 4.53s |
| I-MSM | 13 | 13.00 | 13.68 $\pm$ 0.93 | 13.0 | 0.00 | 0.000 |  Đạt chuẩn | 1.65s |
| CCA | 14 | 14.00 | 14.00 $\pm$ 0.00 | 14.0 | 0.00 | 0.000 |  Đạt chuẩn | 0.20s |
| No-RL | 14 | 14.00 | 14.12 $\pm$ 0.35 | 14.0 | 0.00 | 0.890 |  Đạt chuẩn | 4.84s |
| Fixed | 13 | 13.00 | 13.33 $\pm$ 0.82 | 13.0 | 0.00 | 0.896 |  Đạt chuẩn | 4.29s |
| Random | 14 | 14.00 | 14.12 $\pm$ 0.35 | 14.0 | 0.00 | 0.890 |  Đạt chuẩn | 4.75s |

---

## 2. Cấu Trúc Nghiệm Tốt Nhất Trong Lần Chạy (Best Solution Clusters)
- **Thuật toán đạt Best:** `PPO-AOS` (Cover = `13` clubs, Fitness = `13.00`)
- **Kích thước các cụm ($s$-clubs):** `[8, 10, 19, 10, 4, 5, 9, 12, 6, 5, 3, 9, 5]`
- **Số thế hệ tiến hóa:** `143` generations

### Chi tiết các cụm $s$-club thành phần:
- **Club 5** (Size = 8 đỉnh): `[0, 1, 2, 4, 5, 6, 7, 29]`
- **Club 8** (Size = 10 đỉnh): `[3, 11, 13, 15, 16, 17, 18, 21, 22, 25]`
- **Club 9** (Size = 19 đỉnh): `[8, 9, 10, 12, 23, 24, 26, 27, 32, 33, 36, 39, 40, 41, 42, 45, 46, 47, 54]`
- **Club 10** (Size = 10 đỉnh): `[14, 50, 51, 52, 58, 64, 65, 68, 69, 85]`
- **Club 2** (Size = 4 đỉnh): `[19, 55, 56, 77]`
- **Club 11** (Size = 5 đỉnh): `[20, 48, 49, 53, 57]`
- **Club 12** (Size = 9 đỉnh): `[28, 70, 72, 78, 80, 87, 90, 91, 92]`
- **Club 6** (Size = 12 đỉnh): `[30, 31, 66, 73, 74, 86, 88, 89, 96, 97, 98, 99]`
- **Club 3** (Size = 6 đỉnh): `[34, 35, 37, 38, 43, 44]`
- **Club 13** (Size = 5 đỉnh): `[59, 60, 61, 62, 63]`
- **Club 1** (Size = 3 đỉnh): `[67, 103, 104]`
- **Club 7** (Size = 9 đỉnh): `[71, 75, 76, 79, 81, 82, 83, 84, 100]`
- **Club 4** (Size = 5 đỉnh): `[93, 94, 95, 101, 102]`

---
*File được sinh tự động bởi hệ thống EVO-RL MSCC Research Framework.*
