# BÁO CÁO TỔNG HỢP SỐ LIỆU PHÂN TÍCH CHI PHÍ - LỢI ÍCH (BÀI BÁO 3)
## ĐỀ TÀI: COST-BENEFIT & BREAK-EVEN ANALYSIS OF DEEP RL IN COMBINATORIAL OPTIMIZATION

*Thời gian kết xuất:* `2026-11-01 20:47:44`  
*Tổng số đồ thị đã đánh giá chi phí:* `3` đồ thị  
*Thư mục chi tiết từng đồ thị:* [`chi_tiet_so_lieu_bai3/`](chi_tiet_so_lieu_bai3/)  

---

### 1. BẢNG ĐIỂM HÒA VỐN VÀ HIỆU QUẢ KINH TẾ/KỸ THUẬT (OVERALL SUMMARY)
> *Xem báo cáo đầy đủ: [`2_Phan_tich_diem_hoa_von_Pareto.md`](2_Phan_tich_diem_hoa_von_Pareto.md)*

| Đồ thị | Thuật toán | Nghiệm $|C|$ | Tổng TG (s) | Overhead vs No-RL (%) | RL Overhead (%) | $\Delta K$ vs No-RL | Tốc độ tối ưu (Gain/s) |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `football` | Fixed | 12.00 | 4.789s | +30.2% | 0.01% | **-2.00** | -0.418 |
| `football` | Greedy-AOS | 10.00 | 4.044s | +10.0% | 0.17% | **0.00** | 0.000 |
| `football` | MAB-AOS | 11.00 | 2.040s | -44.5% | 0.02% | **-1.00** | -0.490 |
| `football` | No-RL | 10.00 | 3.677s | +0.0% | 0.10% | **0.00** | 0.000 |
| `football` | **PPO-AOS** | 10.00 | 6.266s | +70.4% | 14.47% | **0.00** | 0.000 |
| `football` | Random | 10.00 | 3.827s | +4.1% | 0.06% | **0.00** | 0.000 |
| `johnson8-2-4` | Fixed | 1.00 | 0.706s | -8.3% | 0.01% | **0.00** | 0.000 |
| `johnson8-2-4` | Greedy-AOS | 1.00 | 0.934s | +21.4% | 0.61% | **0.00** | 0.000 |
| `johnson8-2-4` | MAB-AOS | 1.00 | 0.837s | +8.8% | 0.04% | **0.00** | 0.000 |
| `johnson8-2-4` | No-RL | 1.00 | 0.769s | +0.0% | 0.35% | **0.00** | 0.000 |
| `johnson8-2-4` | **PPO-AOS** | 1.00 | 1.274s | +65.6% | 35.96% | **0.00** | 0.000 |
| `johnson8-2-4` | Random | 1.00 | 0.805s | +4.7% | 0.17% | **0.00** | 0.000 |
| `karate` | Fixed | 4.00 | 1.796s | -14.7% | 0.01% | **0.00** | 0.000 |
| `karate` | Greedy-AOS | 4.00 | 1.918s | -8.9% | 0.25% | **0.00** | 0.000 |
| `karate` | MAB-AOS | 4.00 | 1.306s | -38.0% | 0.03% | **0.00** | 0.000 |
| `karate` | No-RL | 4.00 | 2.106s | +0.0% | 0.16% | **0.00** | 0.000 |
| `karate` | **PPO-AOS** | 4.00 | 2.559s | +21.5% | 18.92% | **0.00** | 0.000 |
| `karate` | Random | 4.00 | 1.472s | -30.1% | 0.09% | **0.00** | 0.000 |

---

### 2. LIÊN KẾT ĐẾN BÁO CÁO CHI TIẾT TỪNG ĐỒ THỊ
Nhấp vào tên đồ thị để kiểm tra toàn bộ dữ liệu bóc tách vi giây (microsecond), RAM đỉnh và bảng ngân sách thời gian riêng biệt:

- [`football`](chi_tiet_so_lieu_bai3/football.md)
- [`johnson8-2-4`](chi_tiet_so_lieu_bai3/johnson8-2-4.md)
- [`karate`](chi_tiet_so_lieu_bai3/karate.md)

---

### 3. CÁC BÁO CÁO CHUYÊN ĐỀ SỐ LIỆU TÁCH RIÊNG
1. [`1_Boc_tach_chi_phi_thoi_gian_PPO_Overhead.md`](1_Boc_tach_chi_phi_thoi_gian_PPO_Overhead.md): Bóc tách chi phí vi giây các module, % RL Overhead và RAM đỉnh.
2. [`2_Phan_tich_diem_hoa_von_Pareto.md`](2_Phan_tich_diem_hoa_von_Pareto.md): Điểm hòa vốn Pareto, Delta K và chi phí tối ưu hóa.
3. [`3_Doi_chuan_ngan_sach_thoi_gian_Time_Budget.md`](3_Doi_chuan_ngan_sach_thoi_gian_Time_Budget.md): Chất lượng nghiệm đạt được dưới các mốc ngân sách thời gian cố định.
