# TIẾN TRÌNH HỘI TỤ THEO THỜI GIAN THỰC (ANYTIME PERFORMANCE - BÀI 2)

* **Mục đích khoa học:** Đánh giá chất lượng nghiệm tại từng mốc thế hệ độc lập. Chứng minh PPO-AOS tìm thấy nghiệm chất lượng cao nhanh hơn các thuật toán đối chứng.

## 1. BẢNG MẪU TIẾN TRÌNH HỘI TỤ THEO CÁC MỐC THẾ HỆ CHÍNH

| Đồ thị | Thuật toán | Thế hệ 1 | Thế hệ 20 | Thế hệ 50 | Thế hệ 100 | Thế hệ 150 | Thế hệ 200 (Cuối) |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `football` | Fixed | 15.00 | 14.00 | 14.00 | 13.00 | 12.00 | 12.00 |
| `football` | Greedy-AOS | 15.00 | 11.00 | 10.00 | 10.00 | - | - |
| `football` | MAB-AOS | 15.00 | 11.00 | 11.00 | 11.00 | - | - |
| `football` | No-RL | 15.00 | 11.00 | 10.00 | 10.00 | - | - |
| `football` | **PPO-AOS** | 15.00 | 11.00 | 10.00 | 10.00 | - | - |
| `football` | Random | 15.00 | 11.00 | 10.00 | 10.00 | - | - |
| `johnson8-2-4` | Fixed | 3.00 | 1.00 | 1.00 | 1.00 | - | - |
| `johnson8-2-4` | Greedy-AOS | 1.00 | 1.00 | 1.00 | 1.00 | - | - |
| `johnson8-2-4` | MAB-AOS | 2.00 | 1.00 | 1.00 | 1.00 | - | - |
| `johnson8-2-4` | No-RL | 3.00 | 1.00 | 1.00 | 1.00 | - | - |
| `johnson8-2-4` | **PPO-AOS** | 2.00 | 1.00 | 1.00 | 1.00 | - | - |
| `johnson8-2-4` | Random | 3.00 | 1.00 | 1.00 | 1.00 | - | - |
| `karate` | Fixed | 5.00 | 4.00 | 4.00 | 4.00 | - | - |
| `karate` | Greedy-AOS | 4.00 | 4.00 | 4.00 | 4.00 | - | - |
| `karate` | MAB-AOS | 4.00 | 4.00 | 4.00 | 4.00 | - | - |
| `karate` | No-RL | 4.00 | 4.00 | 4.00 | 4.00 | - | - |
| `karate` | **PPO-AOS** | 5.00 | 4.00 | 4.00 | 4.00 | - | - |
| `karate` | Random | 4.00 | 4.00 | 4.00 | 4.00 | - | - |
