# Báo Cáo Kết Quả Thực Nghiệm: Seed #16 (Seed = `27182818`)

**Tập dữ liệu đồ thị:** `keller4` ($|V| = 171$, $|E| = 9435$, Density = $0.6491$, $s = 2$)  
**Hạt giống cố định (Seed Value):** `27182818` (Lần chạy 16/20 từ `seedun.md`)  
**Thời gian thực thi:** `2026-09-13 15:04:58`  
**Môi trường tính toán:** `Hybrid Co-Processing [CPU: 12 Cores song song (GA/C++ igraph) + GPU: NVIDIA GeForce RTX 3050 Laptop GPU (PPO Tensor Cores)]`  

---

## 1. Bảng Thống Kê Hiệu Năng Chi Tiết Các Thuật Toán (Seed #16)

| Chiến lược / Thuật toán | Best Cover (Min) | Best Fitness | Mean $\pm$ Std | Median | Vi phạm ($diam > s$) | Độ đa dạng | Khả thi ($100\%$) | Thời gian (s) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **PPO-AOS** | **1** | **1.00** | 1.07 $\pm$ 0.35 | 1.0 | 0.00 | 0.000 |  Đạt chuẩn | 14.59s |
| MAB-AOS | 1 | 1.00 | 1.02 $\pm$ 0.20 | 1.0 | 0.00 | 0.000 |  Đạt chuẩn | 13.37s |
| Greedy-AOS | 1 | 1.00 | 1.03 $\pm$ 0.22 | 1.0 | 0.00 | 0.000 |  Đạt chuẩn | 13.60s |
| I-MSM | 1 | 1.00 | 1.00 $\pm$ 0.00 | 1.0 | 0.00 | 0.000 |  Đạt chuẩn | 35.36s |
| CCA | 1 | 1.00 | 1.00 $\pm$ 0.00 | 1.0 | 0.00 | 0.000 |  Đạt chuẩn | 0.29s |
| No-RL | 1 | 1.00 | 1.02 $\pm$ 0.20 | 1.0 | 0.00 | 0.000 |  Đạt chuẩn | 13.25s |
| Fixed | 1 | 1.00 | 1.02 $\pm$ 0.20 | 1.0 | 0.00 | 0.000 |  Đạt chuẩn | 13.56s |
| Random | 1 | 1.00 | 1.02 $\pm$ 0.20 | 1.0 | 0.00 | 0.000 |  Đạt chuẩn | 12.94s |

---

## 2. Cấu Trúc Nghiệm Tốt Nhất Trong Lần Chạy (Best Solution Clusters)
- **Thuật toán đạt Best:** `PPO-AOS` (Cover = `1` clubs, Fitness = `1.00`)
- **Kích thước các cụm ($s$-clubs):** `[171]`
- **Số thế hệ tiến hóa:** `105` generations

### Chi tiết các cụm $s$-club thành phần:
- **Club 1** (Size = 171 đỉnh): `[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170]`

---
*File được sinh tự động bởi hệ thống EVO-RL MSCC Research Framework.*
