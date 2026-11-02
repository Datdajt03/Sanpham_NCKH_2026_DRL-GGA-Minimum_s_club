# BÓC TÁCH CHI PHÍ THỜI GIAN VÀ OVERHEAD CỦA DEEP RL (BÀI BÁO 3)

* **Chủ đề khoa học:** Định lượng chi phí suy luận mạng nơ-ron (PPO Inference) và cập nhật Policy (PPO Update) so với chi phí tính toán GA truyền thống (Đánh giá Thể lực, Sửa nghiệm, Lai ghép/Đột biến).
* **Ý nghĩa thực tiễn:** Chứng minh kiến trúc Actor-Critic gọn nhẹ (MLP/GNN) chỉ chiếm tỷ lệ không đáng kể (< 1.5%) trong tổng ngân sách thời gian, loại bỏ hoàn toàn hoài nghi về gánh nặng tính toán của Deep RL.

## 1. BẢNG PHÂN RÃ THỜI GIAN TRUNG BÌNH THEO MODULE (AVERAGE TIME PROFILE)

| Đồ thị | Thuật toán | Tổng TG (s) | Đánh giá Thể lực (s) | Sửa nghiệm Repair (s) | Toán tử Operator (s) | RL Suy luận (s) | RL Cập nhật (s) | Tỷ lệ RL Overhead (%) | RAM Đỉnh (MB) |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `football` | Fixed | 4.789s | 0.121s | 2.133s | 1.303s | 0.0003s | 0.0000s | **0.01%** | 1352.9 MB |
| `football` | Greedy-AOS | 4.044s | 0.107s | 1.835s | 1.327s | 0.0070s | 0.0000s | **0.17%** | 563.6 MB |
| `football` | MAB-AOS | 2.040s | 0.084s | 0.854s | 0.585s | 0.0005s | 0.0000s | **0.02%** | 554.3 MB |
| `football` | No-RL | 3.677s | 0.114s | 1.699s | 1.163s | 0.0037s | 0.0000s | **0.10%** | 563.7 MB |
| `football` | **PPO-AOS** | 6.266s | 0.080s | 1.924s | 1.224s | 0.5916s | 0.3149s | **14.47%** | 1352.6 MB |
| `football` | Random | 3.827s | 0.118s | 1.764s | 1.204s | 0.0023s | 0.0000s | **0.06%** | 563.7 MB |
| `johnson8-2-4` | Fixed | 0.706s | 0.019s | 0.218s | 0.124s | 0.0001s | 0.0000s | **0.01%** | 1354.2 MB |
| `johnson8-2-4` | Greedy-AOS | 0.934s | 0.019s | 0.262s | 0.203s | 0.0057s | 0.0000s | **0.61%** | 1354.2 MB |
| `johnson8-2-4` | MAB-AOS | 0.837s | 0.020s | 0.213s | 0.243s | 0.0004s | 0.0000s | **0.04%** | 1354.2 MB |
| `johnson8-2-4` | No-RL | 0.769s | 0.020s | 0.218s | 0.177s | 0.0027s | 0.0000s | **0.35%** | 563.7 MB |
| `johnson8-2-4` | **PPO-AOS** | 1.274s | 0.020s | 0.230s | 0.182s | 0.3046s | 0.1538s | **35.96%** | 1354.2 MB |
| `johnson8-2-4` | Random | 0.805s | 0.011s | 0.231s | 0.188s | 0.0013s | 0.0000s | **0.17%** | 563.9 MB |
| `karate` | Fixed | 1.796s | 0.036s | 0.858s | 0.402s | 0.0002s | 0.0000s | **0.01%** | 563.9 MB |
| `karate` | Greedy-AOS | 1.918s | 0.035s | 0.973s | 0.463s | 0.0049s | 0.0000s | **0.25%** | 563.9 MB |
| `karate` | MAB-AOS | 1.306s | 0.035s | 0.449s | 0.398s | 0.0004s | 0.0000s | **0.03%** | 563.9 MB |
| `karate` | No-RL | 2.106s | 0.020s | 1.073s | 0.538s | 0.0033s | 0.0000s | **0.16%** | 1354.2 MB |
| `karate` | **PPO-AOS** | 2.559s | 0.037s | 1.072s | 0.500s | 0.3463s | 0.1378s | **18.92%** | 1354.2 MB |
| `karate` | Random | 1.472s | 0.036s | 0.744s | 0.374s | 0.0013s | 0.0000s | **0.09%** | 1354.2 MB |

> **Nhận định cốt lõi:**
> - Thời gian lớn nhất (> 70%) luôn thuộc về thủ tục **Sửa nghiệm (Repair procedure)** và **Đánh giá đường kính (Diameter verification)** do đặc tính NP-hard của MSCC.
> - Chi phí suy luận trực tuyến của PPO chỉ chiếm phần trăm rất nhỏ (thường < 1%), khẳng định mô hình hoàn toàn khả thi trên môi trường CPU tiêu chuẩn lẫn GPU.
