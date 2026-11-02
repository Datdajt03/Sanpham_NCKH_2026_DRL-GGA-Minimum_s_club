# Bài Báo 3: Phân tích Chi phí - Lợi ích của Deep RL trong Adaptive Operator Selection

## 1. Trọng tâm Nghiên cứu
Module này phục vụ việc trả lời câu hỏi khoa học: **"PPO-AOS có tạo ra mức cải thiện chất lượng hoặc khả năng hội tụ đủ lớn để bù đắp chi phí tính toán (overhead) và độ phức tạp triển khai so với các cơ chế AOS nhẹ hơn hay không?"**

## 2. Các tệp dữ liệu xuất ra (Output Data)
1. `results_bai3_cost_profile.csv`: Bóc tách chi tiết từng micro-giây của runtime:
   - `runtime_total, runtime_fitness_diameter, runtime_repair, runtime_operator, runtime_ppo_inference, runtime_ppo_update, number_of_ppo_updates, number_of_operator_calls, fitness_evaluations, memory_peak_mb`
2. `results_bai3_time_budget.csv`: Hiệu năng chuẩn hóa theo ngân sách thời gian cố định ($0.5	ext{s}, 1	ext{s}, 2	ext{s}, 5	ext{s}, 10	ext{s}, 30	ext{s}, 60	ext{s}$).
3. `results_bai3_pareto_breakeven.csv`: Phân tích điểm hòa vốn (Break-even), tỷ lệ overhead (\%) so với No-RL, chất lượng tăng thêm trên mỗi giây (`quality_gain_per_sec`) và Pareto frontier.

## 3. Cách chạy
```bash
# Chạy demo kiểm tra nhanh (2 đồ thị, 3 seeds)
python run_bai3.py --datasets demo --seeds 3 --workers 2

# Chạy toàn bộ nhóm Type 1 (9 mạng, 20 seeds)
python run_bai3.py --datasets Type1 --seeds 20 --workers 4

# Chạy toàn bộ 28 đồ thị chuẩn (20 seeds)
python run_bai3.py --datasets all --seeds 20 --workers 5
```
