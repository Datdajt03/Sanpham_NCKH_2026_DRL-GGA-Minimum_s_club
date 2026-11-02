# ĐỘNG THÁI LỰA CHỌN TOÁN TỬ VÀ PHẦN THƯỞNG QUA 3 GIAI ĐOẠN TIẾN HÓA (BÀI 2)

* **3 Giai đoạn tiến hóa được phân định:**
  - **Giai đoạn sớm (Early - 0% đến 30% thế hệ):** Thăm dò không gian tìm kiếm (Exploration).
  - **Giai đoạn giữa (Mid - 30% đến 70% thế hệ):** Cân bằng giữa khai thác và đa dạng hóa.
  - **Giai đoạn muộn (Late - 70% đến 100% thế hệ):** Tinh chỉnh cục bộ và phục hồi tính khả thi (Exploitation & Repair).

## 1. BẢNG PHÂN BỔ TẦN SUẤT CHỌN VÀ REWARD THEO TOÁN TỬ

| Đồ thị | Thuật toán | Giai đoạn | Toán tử | Số lần chọn | Tỷ lệ chọn (%) | Reward Trung bình | Reward Trung vị | Độ lệch SD |
| :--- | :--- | :---: | :--- | :---: | :---: | :---: | :---: | :---: |
| `football` | Fixed | Early | Toán tử 3 | 66 | 100.0% | -0.2672 | -1.0000 | 3.2398 |
| `football` | Fixed | Late | Toán tử 3 | 68 | 100.0% | -1.0000 | -1.0000 | 0.0000 |
| `football` | Fixed | Mid | Toán tử 3 | 66 | 100.0% | -0.8217 | -1.0000 | 1.4487 |
| `football` | Greedy-AOS | Early | Lai ghép cấu trúc (Crossover) | 24 | 36.4% | 0.4220 | -1.0000 | 4.9545 |
| `football` | Greedy-AOS | Early | Đột biến sửa sai (Repair) | 28 | 42.4% | -0.1223 | -1.0000 | 3.0874 |
| `football` | Greedy-AOS | Early | Đột biến đa dạng hóa (Diversify) | 14 | 21.2% | -0.8571 | -1.0000 | 0.3631 |
| `football` | Greedy-AOS | Mid | Lai ghép cấu trúc (Crossover) | 17 | 27.4% | -1.0000 | -1.0000 | 0.0000 |
| `football` | Greedy-AOS | Mid | Đột biến sửa sai (Repair) | 26 | 41.9% | -1.0000 | -1.0000 | 0.0000 |
| `football` | Greedy-AOS | Mid | Đột biến đa dạng hóa (Diversify) | 19 | 30.6% | -1.0000 | -1.0000 | 0.0000 |
| `football` | MAB-AOS | Early | Lai ghép cấu trúc (Crossover) | 66 | 100.0% | -0.1073 | -1.0000 | 3.5527 |
| `football` | MAB-AOS | Mid | Lai ghép cấu trúc (Crossover) | 45 | 100.0% | -1.0000 | -1.0000 | 0.0000 |
| `football` | No-RL | Early | Lai ghép cấu trúc (Crossover) | 24 | 36.4% | 1.8379 | -1.0000 | 5.9061 |
| `football` | No-RL | Early | Đột biến sửa sai (Repair) | 20 | 30.3% | -0.3615 | -1.0000 | 2.6294 |
| `football` | No-RL | Early | Đột biến đa dạng hóa (Diversify) | 22 | 33.3% | -0.8636 | -1.0000 | 0.3513 |
| `football` | No-RL | Mid | Lai ghép cấu trúc (Crossover) | 16 | 28.1% | -1.0000 | -1.0000 | 0.0000 |
| `football` | No-RL | Mid | Đột biến sửa sai (Repair) | 17 | 29.8% | -1.0000 | -1.0000 | 0.0000 |
| `football` | No-RL | Mid | Đột biến đa dạng hóa (Diversify) | 24 | 42.1% | -1.0000 | -1.0000 | 0.0000 |
| `football` | **PPO-AOS** | Early | Lai ghép cấu trúc (Crossover) | 18 | 27.3% | 1.0161 | -1.0000 | 4.4918 |
| `football` | **PPO-AOS** | Early | Đột biến sửa sai (Repair) | 16 | 24.2% | 1.7867 | -1.0000 | 6.2964 |
| `football` | **PPO-AOS** | Early | Đột biến đa dạng hóa (Diversify) | 32 | 48.5% | -0.9688 | -1.0000 | 0.1768 |
| `football` | **PPO-AOS** | Mid | Lai ghép cấu trúc (Crossover) | 18 | 29.0% | -1.0000 | -1.0000 | 0.0000 |
| `football` | **PPO-AOS** | Mid | Đột biến sửa sai (Repair) | 23 | 37.1% | -1.0000 | -1.0000 | 0.0000 |
| `football` | **PPO-AOS** | Mid | Đột biến đa dạng hóa (Diversify) | 21 | 33.9% | -1.0000 | -1.0000 | 0.0000 |
| `football` | Random | Early | Lai ghép cấu trúc (Crossover) | 24 | 36.4% | 1.8379 | -1.0000 | 5.9061 |
| `football` | Random | Early | Đột biến sửa sai (Repair) | 20 | 30.3% | -0.3615 | -1.0000 | 2.6294 |
| `football` | Random | Early | Đột biến đa dạng hóa (Diversify) | 22 | 33.3% | -0.8636 | -1.0000 | 0.3513 |
| `football` | Random | Mid | Lai ghép cấu trúc (Crossover) | 16 | 28.1% | -1.0000 | -1.0000 | 0.0000 |
| `football` | Random | Mid | Đột biến sửa sai (Repair) | 17 | 29.8% | -1.0000 | -1.0000 | 0.0000 |
| `football` | Random | Mid | Đột biến đa dạng hóa (Diversify) | 24 | 42.1% | -1.0000 | -1.0000 | 0.0000 |
| `johnson8-2-4` | Fixed | Early | Toán tử 3 | 66 | 100.0% | 0.0236 | -1.0000 | 4.6988 |
| `johnson8-2-4` | Fixed | Mid | Toán tử 3 | 43 | 100.0% | -1.0000 | -1.0000 | 0.0000 |
| `johnson8-2-4` | Greedy-AOS | Early | Lai ghép cấu trúc (Crossover) | 18 | 27.3% | 1.0578 | -1.0000 | 8.2500 |
| `johnson8-2-4` | Greedy-AOS | Early | Đột biến sửa sai (Repair) | 26 | 39.4% | -1.0000 | -1.0000 | 0.0000 |
| `johnson8-2-4` | Greedy-AOS | Early | Đột biến đa dạng hóa (Diversify) | 22 | 33.3% | -0.9091 | -1.0000 | 0.2942 |
| `johnson8-2-4` | Greedy-AOS | Mid | Lai ghép cấu trúc (Crossover) | 9 | 25.7% | -1.0000 | -1.0000 | 0.0000 |
| `johnson8-2-4` | Greedy-AOS | Mid | Đột biến sửa sai (Repair) | 8 | 22.9% | -1.0000 | -1.0000 | 0.0000 |
| `johnson8-2-4` | Greedy-AOS | Mid | Đột biến đa dạng hóa (Diversify) | 18 | 51.4% | -1.0000 | -1.0000 | 0.0000 |
| `johnson8-2-4` | MAB-AOS | Early | Lai ghép cấu trúc (Crossover) | 66 | 100.0% | -0.1950 | -1.0000 | 4.4533 |
| `johnson8-2-4` | MAB-AOS | Mid | Lai ghép cấu trúc (Crossover) | 36 | 100.0% | -1.0000 | -1.0000 | 0.0000 |
| `johnson8-2-4` | No-RL | Early | Lai ghép cấu trúc (Crossover) | 23 | 34.8% | 0.4203 | -1.0000 | 6.8115 |
| `johnson8-2-4` | No-RL | Early | Đột biến sửa sai (Repair) | 23 | 34.8% | -0.1208 | -1.0000 | 3.8020 |
| `johnson8-2-4` | No-RL | Early | Đột biến đa dạng hóa (Diversify) | 20 | 30.3% | -0.9500 | -1.0000 | 0.2236 |
| `johnson8-2-4` | No-RL | Mid | Lai ghép cấu trúc (Crossover) | 10 | 27.8% | -1.0000 | -1.0000 | 0.0000 |
| `johnson8-2-4` | No-RL | Mid | Đột biến sửa sai (Repair) | 12 | 33.3% | -1.0000 | -1.0000 | 0.0000 |
| `johnson8-2-4` | No-RL | Mid | Đột biến đa dạng hóa (Diversify) | 14 | 38.9% | -1.0000 | -1.0000 | 0.0000 |
| `johnson8-2-4` | **PPO-AOS** | Early | Lai ghép cấu trúc (Crossover) | 18 | 27.3% | 0.8306 | -1.0000 | 7.2865 |
| `johnson8-2-4` | **PPO-AOS** | Early | Đột biến sửa sai (Repair) | 16 | 24.2% | 0.1989 | -1.0000 | 4.7955 |
| `johnson8-2-4` | **PPO-AOS** | Early | Đột biến đa dạng hóa (Diversify) | 32 | 48.5% | -0.9688 | -1.0000 | 0.1768 |
| `johnson8-2-4` | **PPO-AOS** | Mid | Lai ghép cấu trúc (Crossover) | 10 | 27.8% | -1.0000 | -1.0000 | 0.0000 |
| `johnson8-2-4` | **PPO-AOS** | Mid | Đột biến sửa sai (Repair) | 13 | 36.1% | -1.0000 | -1.0000 | 0.0000 |
| `johnson8-2-4` | **PPO-AOS** | Mid | Đột biến đa dạng hóa (Diversify) | 13 | 36.1% | -1.0000 | -1.0000 | 0.0000 |
| `johnson8-2-4` | Random | Early | Lai ghép cấu trúc (Crossover) | 23 | 34.8% | 0.4203 | -1.0000 | 6.8115 |
| `johnson8-2-4` | Random | Early | Đột biến sửa sai (Repair) | 23 | 34.8% | -0.1208 | -1.0000 | 3.8020 |
| `johnson8-2-4` | Random | Early | Đột biến đa dạng hóa (Diversify) | 20 | 30.3% | -0.9500 | -1.0000 | 0.2236 |
| `johnson8-2-4` | Random | Mid | Lai ghép cấu trúc (Crossover) | 10 | 27.8% | -1.0000 | -1.0000 | 0.0000 |
| `johnson8-2-4` | Random | Mid | Đột biến sửa sai (Repair) | 12 | 33.3% | -1.0000 | -1.0000 | 0.0000 |
| `johnson8-2-4` | Random | Mid | Đột biến đa dạng hóa (Diversify) | 14 | 38.9% | -1.0000 | -1.0000 | 0.0000 |
| `karate` | Fixed | Early | Toán tử 3 | 66 | 100.0% | -0.4254 | -1.0000 | 3.0102 |
| `karate` | Fixed | Mid | Toán tử 3 | 46 | 100.0% | -1.0000 | -1.0000 | 0.0000 |
| `karate` | Greedy-AOS | Early | Lai ghép cấu trúc (Crossover) | 23 | 34.8% | -0.0896 | -1.0000 | 4.3659 |
| `karate` | Greedy-AOS | Early | Đột biến sửa sai (Repair) | 11 | 16.7% | -1.0000 | -1.0000 | 0.0000 |
| `karate` | Greedy-AOS | Early | Đột biến đa dạng hóa (Diversify) | 32 | 48.5% | -0.8750 | -1.0000 | 0.3360 |
| `karate` | Greedy-AOS | Mid | Lai ghép cấu trúc (Crossover) | 13 | 37.1% | -1.0000 | -1.0000 | 0.0000 |
| `karate` | Greedy-AOS | Mid | Đột biến sửa sai (Repair) | 14 | 40.0% | -1.0000 | -1.0000 | 0.0000 |
| `karate` | Greedy-AOS | Mid | Đột biến đa dạng hóa (Diversify) | 8 | 22.9% | -1.0000 | -1.0000 | 0.0000 |
| `karate` | MAB-AOS | Early | Lai ghép cấu trúc (Crossover) | 66 | 100.0% | -0.6222 | -1.0000 | 2.5809 |
| `karate` | MAB-AOS | Mid | Lai ghép cấu trúc (Crossover) | 35 | 100.0% | -1.0000 | -1.0000 | 0.0000 |
| `karate` | No-RL | Early | Lai ghép cấu trúc (Crossover) | 28 | 42.4% | -0.1808 | -1.0000 | 3.9516 |
| `karate` | No-RL | Early | Đột biến sửa sai (Repair) | 25 | 37.9% | -0.9200 | -1.0000 | 0.2769 |
| `karate` | No-RL | Early | Đột biến đa dạng hóa (Diversify) | 13 | 19.7% | -1.0000 | -1.0000 | 0.0000 |
| `karate` | No-RL | Mid | Lai ghép cấu trúc (Crossover) | 15 | 42.9% | -1.0000 | -1.0000 | 0.0000 |
| `karate` | No-RL | Mid | Đột biến sửa sai (Repair) | 8 | 22.9% | -1.0000 | -1.0000 | 0.0000 |
| `karate` | No-RL | Mid | Đột biến đa dạng hóa (Diversify) | 12 | 34.3% | -1.0000 | -1.0000 | 0.0000 |
| `karate` | **PPO-AOS** | Early | Lai ghép cấu trúc (Crossover) | 18 | 27.3% | -0.1667 | -1.0000 | 3.0534 |
| `karate` | **PPO-AOS** | Early | Đột biến sửa sai (Repair) | 16 | 24.2% | 0.3077 | -1.0000 | 5.2307 |
| `karate` | **PPO-AOS** | Early | Đột biến đa dạng hóa (Diversify) | 32 | 48.5% | -0.9688 | -1.0000 | 0.1768 |
| `karate` | **PPO-AOS** | Mid | Lai ghép cấu trúc (Crossover) | 10 | 27.8% | -1.0000 | -1.0000 | 0.0000 |
| `karate` | **PPO-AOS** | Mid | Đột biến sửa sai (Repair) | 13 | 36.1% | -1.0000 | -1.0000 | 0.0000 |
| `karate` | **PPO-AOS** | Mid | Đột biến đa dạng hóa (Diversify) | 13 | 36.1% | -1.0000 | -1.0000 | 0.0000 |
| `karate` | Random | Early | Lai ghép cấu trúc (Crossover) | 28 | 42.4% | -0.1808 | -1.0000 | 3.9516 |
| `karate` | Random | Early | Đột biến sửa sai (Repair) | 25 | 37.9% | -0.9200 | -1.0000 | 0.2769 |
| `karate` | Random | Early | Đột biến đa dạng hóa (Diversify) | 13 | 19.7% | -1.0000 | -1.0000 | 0.0000 |
| `karate` | Random | Mid | Lai ghép cấu trúc (Crossover) | 15 | 42.9% | -1.0000 | -1.0000 | 0.0000 |
| `karate` | Random | Mid | Đột biến sửa sai (Repair) | 8 | 22.9% | -1.0000 | -1.0000 | 0.0000 |
| `karate` | Random | Mid | Đột biến đa dạng hóa (Diversify) | 12 | 34.3% | -1.0000 | -1.0000 | 0.0000 |
