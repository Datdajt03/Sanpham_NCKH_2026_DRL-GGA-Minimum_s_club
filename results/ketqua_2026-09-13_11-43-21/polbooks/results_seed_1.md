# Báo Cáo Kết Quả Thực Nghiệm: Seed #01 (Seed = `17032026`)

**Tập dữ liệu đồ thị:** `polbooks` ($|V| = 105$, $|E| = 441$, Density = $0.0808$, $s = 2$)  
**Hạt giống cố định (Seed Value):** `17032026` (Lần chạy 01/20 từ `seedun.md`)  
**Thời gian thực thi:** `2026-09-13 11:48:33`  
**Môi trường tính toán:** `Hybrid Co-Processing [CPU: 12 Cores song song (GA/C++ igraph) + GPU: NVIDIA GeForce RTX 3050 Laptop GPU (PPO Tensor Cores)]`  

---

## 1. Bảng Thống Kê Hiệu Năng Chi Tiết Các Thuật Toán (Seed #1)

| Chiến lược / Thuật toán | Best Cover (Min) | Best Fitness | Mean $\pm$ Std | Median | Vi phạm ($diam > s$) | Độ đa dạng | Khả thi ($100\%$) | Thời gian (s) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **PPO-AOS** | **14** | **14.00** | 14.16 $\pm$ 0.49 | 14.0 | 0.00 | 0.935 |  Đạt chuẩn | 7.85s |
| MAB-AOS | 13 | 13.00 | 13.25 $\pm$ 0.59 | 13.0 | 0.00 | 0.897 |  Đạt chuẩn | 5.37s |
| Greedy-AOS | 13 | 13.00 | 13.32 $\pm$ 0.79 | 13.0 | 0.00 | 0.842 |  Đạt chuẩn | 5.10s |
| I-MSM | 13 | 13.00 | 13.36 $\pm$ 0.48 | 13.0 | 0.00 | 0.000 |  Đạt chuẩn | 1.56s |
| CCA | 14 | 14.00 | 14.29 $\pm$ 0.55 | 14.0 | 0.00 | 0.000 |  Đạt chuẩn | 0.22s |
| No-RL | 13 | 13.00 | 13.39 $\pm$ 0.79 | 13.0 | 0.00 | 0.917 |  Đạt chuẩn | 5.39s |
| Fixed | 13 | 13.00 | 13.30 $\pm$ 0.77 | 13.0 | 0.00 | 0.914 |  Đạt chuẩn | 4.02s |
| Random | 13 | 13.00 | 13.39 $\pm$ 0.79 | 13.0 | 0.00 | 0.917 |  Đạt chuẩn | 5.56s |

---

## 2. Cấu Trúc Nghiệm Tốt Nhất Trong Lần Chạy (Best Solution Clusters)
- **Thuật toán đạt Best:** `MAB-AOS` (Cover = `13` clubs, Fitness = `13.00`)
- **Kích thước các cụm ($s$-clubs):** `[12, 5, 12, 10, 6, 7, 12, 7, 6, 3, 4, 17, 4]`
- **Số thế hệ tiến hóa:** `124` generations

### Chi tiết các cụm $s$-club thành phần:
- **Club 7** (Size = 12 đỉnh): `[0, 1, 3, 5, 16, 18, 19, 21, 22, 23, 24, 25]`
- **Club 8** (Size = 5 đỉnh): `[2, 4, 6, 28, 29]`
- **Club 4** (Size = 12 đỉnh): `[7, 30, 50, 51, 52, 58, 64, 65, 68, 69, 77, 85]`
- **Club 6** (Size = 10 đỉnh): `[8, 11, 14, 26, 27, 42, 43, 45, 47, 56]`
- **Club 9** (Size = 6 đỉnh): `[9, 20, 48, 49, 53, 57]`
- **Club 10** (Size = 7 đỉnh): `[10, 33, 34, 35, 37, 39, 40]`
- **Club 11** (Size = 12 đỉnh): `[12, 13, 15, 17, 32, 36, 38, 41, 44, 46, 54, 55]`
- **Club 3** (Size = 7 đỉnh): `[31, 73, 93, 94, 96, 97, 98]`
- **Club 12** (Size = 6 đỉnh): `[59, 60, 62, 63, 90, 99]`
- **Club 2** (Size = 3 đỉnh): `[61, 95, 102]`
- **Club 5** (Size = 4 đỉnh): `[66, 67, 103, 104]`
- **Club 1** (Size = 17 đỉnh): `[70, 71, 72, 74, 75, 76, 78, 79, 80, 82, 83, 84, 87, 88, 89, 91, 92]`
- **Club 13** (Size = 4 đỉnh): `[81, 86, 100, 101]`

---
*File được sinh tự động bởi hệ thống EVO-RL MSCC Research Framework.*
