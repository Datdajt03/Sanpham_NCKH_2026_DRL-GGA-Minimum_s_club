# BÁO CÁO TỔNG HỢP SỐ LIỆU THỰC NGHIỆM BÀI BÁO 2
## ĐỀ TÀI: ĐÁNH GIÁ TÍNH PHÙ HỢP CỦA DEEP RL TRONG LỰA CHỌN TOÁN TỬ TIẾN HÓA (AOS SUITABILITY)

*Thời gian kết xuất:* `2026-11-01 18:07:51`  
*Tổng số đồ thị đã đối chuẩn:* `3` đồ thị  
*Thư mục chi tiết từng đồ thị:* [`chi_tiet_so_lieu_bai2/`](chi_tiet_so_lieu_bai2/)  

---

### 1. BẢNG ĐỐI CHUẨN ĐA TIÊU CHÍ VÀ XẾP HẠNG (SUMMARY RANKING)
> *Xem báo cáo đầy đủ: [`1_Bang_xep_hang_da_tieu_chi.md`](1_Bang_xep_hang_da_tieu_chi.md)*

| Thuật toán | Mean Rank | Thắng (W) | Hòa (T) | Thua (L) vs PPO | Thời gian trung vị | Fitness Evals | Gap to Best | Khả thi (%) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| MAB-AOS | **2.33** | 0 | 2 | 1 | 1.10s | 2193 | 0.33 | 100.0% |
| Greedy-AOS | **1.00** | 0 | 3 | 0 | 1.72s | 2300 | 0.00 | 100.0% |
| **PPO-AOS** | **1.00** | 0 | 0 | 0 | 4.67s | 2313 | 0.00 | 100.0% |
| No-RL | **1.00** | 0 | 3 | 0 | 2.14s | 2273 | 0.00 | 100.0% |
| Fixed | **2.67** | 0 | 2 | 1 | 1.92s | 2907 | 0.67 | 100.0% |
| I-MSM | **3.00** | 0 | 2 | 1 | 0.17s | 100 | 1.00 | 100.0% |
| CCA | **3.33** | 0 | 2 | 1 | 0.01s | 59 | 1.33 | 100.0% |
| Random | **1.00** | 0 | 3 | 0 | 2.01s | 2273 | 0.00 | 100.0% |

---

### 2. LIÊN KẾT ĐẾN BÁO CÁO CHI TIẾT TỪNG ĐỒ THỊ
Nhấp vào tên đồ thị để kiểm tra toàn bộ dữ liệu 20 hạt giống, phân bố toán tử và tiến trình hội tụ riêng biệt:

- [`football`](chi_tiet_so_lieu_bai2/football.md)
- [`johnson8-2-4`](chi_tiet_so_lieu_bai2/johnson8-2-4.md)
- [`karate`](chi_tiet_so_lieu_bai2/karate.md)

---

### 3. CÁC BÁO CÁO CHUYÊN ĐỀ SỐ LIỆU TÁCH RIÊNG
1. [`1_Bang_xep_hang_da_tieu_chi.md`](1_Bang_xep_hang_da_tieu_chi.md): Bảng phân tích thứ hạng, Gap-to-best và độ ổn định (SD, IQR).
2. [`2_Dong_thai_toan_tu_3_giai_doan.md`](2_Dong_thai_toan_tu_3_giai_doan.md): Bảng tỷ lệ chọn 3 toán tử và phần thưởng qua 3 giai đoạn Early, Mid, Late.
3. [`3_Tien_trinh_hoi_tu_anytime.md`](3_Tien_trinh_hoi_tu_anytime.md): Bảng tiến trình hội tụ theo từng mốc thế hệ.
