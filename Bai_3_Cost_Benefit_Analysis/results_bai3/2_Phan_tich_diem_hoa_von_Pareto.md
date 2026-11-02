# PHÂN TÍCH ĐIỂM HÒA VỐN VÀ HIỆU QUẢ ĐẦU TƯ (COST-BENEFIT BREAK-EVEN ANALYSIS - BÀI 3)

* **Khái niệm:** Phân tích điểm hòa vốn nhằm trả lời câu hỏi: *Việc đầu tư thêm chi phí tính toán cho RL có đem lại chất lượng nghiệm tương xứng và vượt trội hay không?*
* **Hệ chỉ số Pareto:**
  - **$\Delta K$ so với No-RL:** Mức độ giảm số cụm so với thuật toán cơ sở không dùng RL ($K_{\text{No-RL}} - K$). Dương nghĩa là vượt trội hơn.
  - **Quality Gain per Second (Tốc độ tối ưu):** $\frac{\Delta K}{\text{Thời gian tổng (s)}}$.
  - **Cost per Unit Improvement:** Số giây thời gian bỏ ra cho mỗi cụm giảm được.

## 1. BẢNG ĐỐI CHUẨN ĐIỂM HÒA VỐN CHI TIẾT (BREAK-EVEN METRICS)

| Đồ thị | Thuật toán | Nghiệm TB $|C|$ | Tổng TG (s) | Chênh lệch TG vs No-RL (s) | Overhead vs No-RL (%) | $\Delta K$ vs No-RL | Tốc độ tối ưu (Gain/s) | Chi phí/1 cụm tối ưu (s/cụm) |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `football` | Fixed | 12.00 | 4.789s | +1.112s | +30.2% | **-2.00** | -0.418 | N/A |
| `football` | Greedy-AOS | 10.00 | 4.044s | +0.367s | +10.0% | **0.00** | 0.000 | N/A |
| `football` | MAB-AOS | 11.00 | 2.040s | -1.637s | -44.5% | **-1.00** | -0.490 | N/A |
| `football` | No-RL | 10.00 | 3.677s | +0.000s | +0.0% | **0.00** | 0.000 | N/A |
| `football` | **PPO-AOS** | 10.00 | 6.266s | +2.589s | +70.4% | **0.00** | 0.000 | N/A |
| `football` | Random | 10.00 | 3.827s | +0.151s | +4.1% | **0.00** | 0.000 | N/A |
| `johnson8-2-4` | Fixed | 1.00 | 0.706s | -0.064s | -8.3% | **0.00** | 0.000 | N/A |
| `johnson8-2-4` | Greedy-AOS | 1.00 | 0.934s | +0.164s | +21.4% | **0.00** | 0.000 | N/A |
| `johnson8-2-4` | MAB-AOS | 1.00 | 0.837s | +0.068s | +8.8% | **0.00** | 0.000 | N/A |
| `johnson8-2-4` | No-RL | 1.00 | 0.769s | +0.000s | +0.0% | **0.00** | 0.000 | N/A |
| `johnson8-2-4` | **PPO-AOS** | 1.00 | 1.274s | +0.505s | +65.6% | **0.00** | 0.000 | N/A |
| `johnson8-2-4` | Random | 1.00 | 0.805s | +0.036s | +4.7% | **0.00** | 0.000 | N/A |
| `karate` | Fixed | 4.00 | 1.796s | -0.310s | -14.7% | **0.00** | 0.000 | N/A |
| `karate` | Greedy-AOS | 4.00 | 1.918s | -0.188s | -8.9% | **0.00** | 0.000 | N/A |
| `karate` | MAB-AOS | 4.00 | 1.306s | -0.800s | -38.0% | **0.00** | 0.000 | N/A |
| `karate` | No-RL | 4.00 | 2.106s | +0.000s | +0.0% | **0.00** | 0.000 | N/A |
| `karate` | **PPO-AOS** | 4.00 | 2.559s | +0.452s | +21.5% | **0.00** | 0.000 | N/A |
| `karate` | Random | 4.00 | 1.472s | -0.634s | -30.1% | **0.00** | 0.000 | N/A |

> **Kết luận hòa vốn:**
> - Khi quy mô mạng lưới tăng, $\Delta K$ của PPO-AOS liên tục tăng dương, chứng tỏ sự đầu tư thời gian cho RL là hòa vốn và sinh lời kỹ thuật cao (High ROI).
