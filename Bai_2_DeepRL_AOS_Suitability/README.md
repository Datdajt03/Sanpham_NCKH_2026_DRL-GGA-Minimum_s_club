# Bài Báo 2: Deep RL có thực sự phù hợp cho Adaptive Operator Selection (AOS)?

## 1. Trọng tâm Nghiên cứu
Module này phục vụ việc trả lời câu hỏi khoa học: **"Deep RL có tạo ra lợi ích thuật toán độc lập, cải thiện tốc độ hội tụ và độ ổn định cho AOS trong bài toán Minimum s-Club Cover hay không?"**

## 2. Các tệp dữ liệu xuất ra (Output Data)
1. `results_bai2_runs.csv`: Dữ liệu từng lượt chạy `dataset × method × seed` gồm đầy đủ 22 trường:
   - `dataset, graph_type, n, m, density, s, method, seed, best_k, final_k, mean_k, median_k, worst_k, feasible_rate, best_violation, mean_violation, fitness_evaluations, generations, runtime, time_to_first_feasible, time_to_best, status`
2. `results_bai2_anytime.csv`: Đường cong hội tụ chi tiết theo số lượng đánh giá thể lực (`evaluations`) và thời gian thực (`time_elapsed`).
3. `results_bai2_operator_stats.csv`: Phân bố tỷ lệ chọn toán tử và phản hồi phần thưởng (`mean_reward`, `median_reward`) theo 3 giai đoạn (Early $0-33\%$, Mid $33-66\%$, Late $66-100\%$).
4. `results_bai2_summary.csv`: Bảng tổng hợp đa chiều gồm Mean rank, Win/Tie/Loss đối đầu với PPO, Median runtime, Mean evaluations, Gap-to-best, Feasible rate, SD, và IQR.

## 3. Cách chạy
```bash
# Chạy demo kiểm tra nhanh (2 đồ thị, 3 seeds)
python run_bai2.py --datasets demo --seeds 3 --workers 2

# Chạy toàn bộ nhóm Type 1 (9 mạng, 20 seeds)
python run_bai2.py --datasets Type1 --seeds 20 --workers 4

# Chạy toàn bộ 28 đồ thị chuẩn (20 seeds)
python run_bai2.py --datasets all --seeds 20 --workers 5
```
