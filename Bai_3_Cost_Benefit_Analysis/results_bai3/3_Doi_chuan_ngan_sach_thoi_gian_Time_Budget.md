# ĐỐI CHUẨN NGHIỆM DƯỚI NGÂN SÁCH THỜI GIAN CỐ ĐỊNH (TIME-BUDGET SNAPSHOTS - BÀI 3)

* **Ý nghĩa ứng dụng:** Trong các hệ thống điều khiển mạng lưới viễn thông, logistics hoặc định tuyến xe cứu hỏa/cứu nạn, thời gian tính toán bị giới hạn ngặt nghèo (Deadline-constrained). Bảng này chỉ rõ chất lượng nghiệm $|C|$ mà mỗi thuật toán đạt được khi bị cưỡng chế dừng tại các mốc thời gian cố định.

## 1. BẢNG ĐỐI ĐẦU THEO CÁC MỐC THỜI GIAN CỐ ĐỊNH

| Đồ thị | Thuật toán | T = 0.5s | T = 1.0s | T = 2.0s | T = 5.0s | T = 10.0s | T = 30.0s | T = 60.0s |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `football` | Fixed | 15.00 | 14.00 | 13.00 | 12.00 | 12.00 | 12.00 | 12.00 |
| `football` | Greedy-AOS | 14.00 | 10.00 | 10.00 | 10.00 | 10.00 | 10.00 | 10.00 |
| `football` | MAB-AOS | 12.00 | 11.00 | 11.00 | 11.00 | 11.00 | 11.00 | 11.00 |
| `football` | No-RL | 15.00 | 11.00 | 10.00 | 10.00 | 10.00 | 10.00 | 10.00 |
| `football` | **PPO-AOS** | **14.00** | **12.00** | **10.00** | **10.00** | **10.00** | **10.00** | **10.00** |
| `football` | Random | 15.00 | 11.00 | 10.00 | 10.00 | 10.00 | 10.00 | 10.00 |
| `johnson8-2-4` | Fixed | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 |
| `johnson8-2-4` | Greedy-AOS | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 |
| `johnson8-2-4` | MAB-AOS | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 |
| `johnson8-2-4` | No-RL | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 |
| `johnson8-2-4` | **PPO-AOS** | **1.00** | **1.00** | **1.00** | **1.00** | **1.00** | **1.00** | **1.00** |
| `johnson8-2-4` | Random | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 |
| `karate` | Fixed | 4.00 | 4.00 | 4.00 | 4.00 | 4.00 | 4.00 | 4.00 |
| `karate` | Greedy-AOS | 4.00 | 4.00 | 4.00 | 4.00 | 4.00 | 4.00 | 4.00 |
| `karate` | MAB-AOS | 4.00 | 4.00 | 4.00 | 4.00 | 4.00 | 4.00 | 4.00 |
| `karate` | No-RL | 4.00 | 4.00 | 4.00 | 4.00 | 4.00 | 4.00 | 4.00 |
| `karate` | **PPO-AOS** | **4.00** | **4.00** | **4.00** | **4.00** | **4.00** | **4.00** | **4.00** |
| `karate` | Random | 4.00 | 4.00 | 4.00 | 4.00 | 4.00 | 4.00 | 4.00 |
