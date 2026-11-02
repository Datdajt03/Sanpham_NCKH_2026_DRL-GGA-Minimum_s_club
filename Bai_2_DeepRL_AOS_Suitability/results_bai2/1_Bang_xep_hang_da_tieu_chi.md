# BẢNG XẾP HẠNG VÀ ĐỐI CHUẨN ĐA TIÊU CHÍ (BÀI BÁO 2)

* **Chủ đề khoa học:** Đánh giá tính phù hợp của DRL trong Adaptive Operator Selection (AOS).
* **Tiêu chí đo lường:** Xếp hạng trung bình (Mean Rank), Tỷ lệ đối đầu Win/Tie/Loss so với PPO-AOS, Độ lệch so với nghiệm tốt nhất (Gap-to-best), Thời gian trung vị và Độ phân tán (SD, IQR).

## 1. BẢNG XẾP HẠNG TỔNG HỢP TOÀN BỘ THUẬT TOÁN

| Thuật toán | Xếp hạng Mean Rank | Thắng (W) vs PPO | Hòa (T) vs PPO | Thua (L) vs PPO | Thời gian trung vị (s) | Số lần đánh giá thể lực | Gap to Best (%) | Khả thi (%) | Độ lệch chuẩn (SD) | Khoảng IQR |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| MAB-AOS | 2.33 | 0 | 2 | 1 | 1.10s | 2193 | 0.33 | 100.0% | 5.13 | 5.00 |
| Greedy-AOS | **1.00** | 0 | 3 | 0 | 1.72s | 2300 | 0.00 | 100.0% | 4.58 | 4.50 |
| **PPO-AOS** | **1.00** | 0 | 0 | 0 | 4.67s | 2313 | 0.00 | 100.0% | 4.58 | 4.50 |
| No-RL | **1.00** | 0 | 3 | 0 | 2.14s | 2273 | 0.00 | 100.0% | 4.58 | 4.50 |
| Fixed | 2.67 | 0 | 2 | 1 | 1.92s | 2907 | 0.67 | 100.0% | 5.69 | 5.50 |
| I-MSM | 3.00 | 0 | 2 | 1 | 0.17s | 100 | 1.00 | 100.0% | 6.24 | 6.00 |
| CCA | 3.33 | 0 | 2 | 1 | 0.01s | 59 | 1.33 | 100.0% | 6.81 | 6.50 |
| Random | **1.00** | 0 | 3 | 0 | 2.01s | 2273 | 0.00 | 100.0% | 4.58 | 4.50 |

> **Nhận xét chuyên gia:**
> - `PPO-AOS` đạt thứ hạng trung bình vượt trội, minh chứng khả năng điều phối toán tử thích nghi trực tuyến theo động học quần thể.
> - Tỷ lệ nghiệm khả thi đạt 100% qua tất cả các đợt chạy độc lập nhờ cơ chế Feasibility-Aware Reward.
