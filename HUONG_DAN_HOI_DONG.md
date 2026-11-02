# HƯỚNG DẪN NGHIỆM THU DÀNH CHO HỘI ĐỒNG KHOA HỌC
## ĐỀ TÀI: KHUNG TỐI ƯU HÓA TIẾN HÓA KẾT HỢP HỌC TĂNG CƯỜNG SÂU (EVO-RL / PPO-AOS) CHO BÀI TOÁN MINIMUM s-CLUB COVER
**Gói sản phẩm:** `Sanpham_nckh` | **Phiên bản:** Hoàn thiện nghiệm thu | **Độc lập & Khả chuyển 100%**

---

### KÍNH GỬI QUÝ THẦY CÔ VÀ CÁC THÀNH VIÊN HỘI ĐỒNG ĐÁNH GIÁ

Nhóm nghiên cứu trân trọng gửi tới Quý Hội đồng toàn bộ gói sản phẩm phần mềm, cơ sở dữ liệu thực nghiệm, mã nguồn và tài liệu học thuật hoàn chỉnh của đề tài. Gói sản phẩm được tổ chức tinh gọn, khả chuyển và sẵn sàng thực thi 1-Click trên mọi máy tính Windows mà không cần cấu hình phức tạp.

---

### 1. BẮT ĐẦU NHANH (QUICK START - 1 CLICK)

> [!IMPORTANT]
> **Điểm khởi chạy duy nhất:** Quý Thầy/Cô chỉ cần nhấp đúp vào:
> ```cmd
> CHAY_CHUONG_TRINH_TONG.bat
> ```
> *(Nếu máy tính mới chưa cài đặt môi trường Python/CUDA, vui lòng nhấp đúp `setup.bat` ở thư mục gốc trước).*

#### Giao diện Menu Tổng hợp (`CHAY_CHUONG_TRINH_TONG.bat`):
* **`[1]` Chạy thực nghiệm Bài 1:** Giải bài toán MSCC với EVO-RL trên 30 đồ thị benchmark.
* **`[2]` Chạy thực nghiệm Bài 2:** Đánh giá tính phù hợp DRL (PPO vs MAB, Greedy, Random).
* **`[3]` Chạy thực nghiệm Bài 3:** Phân tích chi phí vi giây, Overhead và điểm hòa vốn DRL.
* **`[4]` Chạy đồng thời Bài 2 & Bài 3:** Kích hoạt song song 2 bài báo để tiết kiệm thời gian.
* **`[5]` Xuất biểu đồ phân tích:** Tự động vẽ 7 dạng biểu đồ 300 DPI và vector PDF vào `Chart_seed/`.
* **`[6]` Tổng hợp số liệu phân tích:** Trích xuất tự động ma trận kết quả 28 đồ thị, CSV và Markdown.
* **`[7]` Tái xuất báo cáo Markdown:** Kết xuất lại file `.md` cho Bài 2 & Bài 3 từ CSV có sẵn.
* **`[8]` Kiểm tra toàn diện hệ thống:** Chạy tự động 9 giai đoạn kiểm chứng (< 6 giây).
* **`[9]` Thiết lập môi trường & GPU:** Cài đặt thư viện và kiểm tra card đồ họa NVIDIA CUDA.
* **`[0]` Thoát chương trình.**

---

### 2. KIỂM CHỨNG NHANH TOÀN HỆ THỐNG TRONG 6 GIÂY

Để đánh giá nhanh tính toàn vẹn của mã nguồn, thư viện và dữ liệu trước khi nghiệm thu:
* **Cách 1:** Chọn phím **`[8]`** trong `CHAY_CHUONG_TRINH_TONG.bat`.
* **Cách 2:** Mở thư mục **`Run.bat/`** và nhấp đúp `verify_all.bat`.
* **Cách 3:** Chạy lệnh Terminal: `python verify_system.py`.

*Kết quả kiểm chứng chuẩn khi đạt:*
```text
[✓] TẤT CẢ 9/9 GIAI ĐOẠN ĐÃ VƯỢT QUA XUẤT SẮC! (~5.9s)
Hệ thống 'Sanpham_nckh' đạt chuẩn 100% tính độc lập, khả chuyển và sẵn sàng nộp Hội đồng!
```

---

### 3. CẤU TRÚC GÓI SẢN PHẨM & CÁC TỆP RUNNER

Toàn bộ các tệp thực thi chi tiết đã được gom gọn gàng vào thư mục `Run.bat/`, ở thư mục gốc chỉ để lại **Chương trình Tổng** và tệp **cài đặt môi trường**:

```text
Sanpham_nckh/
├── CHAY_CHUONG_TRINH_TONG.bat   <-- [CHÍNH] Menu tổng điều khiển tất cả tính năng
├── setup.bat                    <-- Cài đặt môi trường tự động (chạy 1 lần khi sang máy mới)
│
├── Run.bat/                     <-- THƯ MỤC CHỨA CÁC RUNNER CHI TIẾT:
│   ├── run.bat                  <-- Runner Bài 1 (Menu thuật toán EVO-RL, 30 đồ thị)
│   ├── run_bai2.bat             <-- Runner Bài 2 (Đánh giá tính phù hợp DRL)
│   ├── run_bai3.bat             <-- Runner Bài 3 (Phân tích chi phí & Overhead)
│   ├── run_both_bai2_and_bai3.bat <-- Runner chạy song song độc lập cả Bài 2 & Bài 3
│   ├── runbieudo.bat            <-- Xuất biểu đồ chuẩn 300 DPI & Vector PDF
│   ├── run_tong_hop_so_lieu.bat <-- Trích xuất và tổng hợp báo cáo số liệu
│   ├── verify_all.bat           <-- Kiểm chứng tự động 9 giai đoạn mã nguồn
│   └── RUN_ALL.bat              <-- Phím tắt chuyển tiếp tới CHAY_CHUONG_TRINH_TONG
│
├── pbodulieu/                   <-- Bộ 30 đồ thị benchmark chuẩn (2.03 MB, độc lập 100%)
├── results/                     <-- Cơ sở dữ liệu kết quả Bài 1 (30 đồ thị x 20 seeds x 8 thuật toán)
├── Bai_2_DeepRL_AOS_Suitability/<-- Mã nguồn & cơ sở dữ liệu kết quả Bài báo 2 (results_bai2/)
├── Bai_3_Cost_Benefit_Analysis/ <-- Mã nguồn & cơ sở dữ liệu kết quả Bài báo 3 (results_bai3/)
└── Tong_hop_so_lieu_phan_bien/  <-- Bộ công cụ tổng hợp số liệu phản biện & đối chuẩn Mục 4.4
```

---

### 4. BẢN ĐỒ DỮ LIỆU KẾT QUẢ THỰC NGHIỆM

Toàn bộ kết quả thực nghiệm chính thức đã được chạy sẵn và lưu trữ đầy đủ trong các thư mục tương ứng:

| Nhóm kết quả | Vị trí lưu trữ | Tệp báo cáo chính | Nội dung & Chỉ số cốt lõi |
| :--- | :--- | :--- | :--- |
| **Bài báo 1**<br>*(EVO-RL MSCC)* | `results/ketqua_2026-09-13_11-43-21/` | `Tong_20_lan_seed.md`<br>`summary_metrics.csv`<br>`Chart_seed/` | 30 đồ thị $\times$ 20 seeds $\times$ 8 thuật toán: Best/Mean/Std $\|C\|$, thời gian chạy, kiểm định thống kê Wilcoxon ($p < 0.05$), 7 biểu đồ 300 DPI. |
| **Bài báo 2**<br>*(DRL Suitability)* | `Bai_2_DeepRL_AOS_Suitability/results_bai2/` | `Tong_hop_so_lieu_Bai_2.md` | Bảng xếp hạng đa tiêu chí, tỷ lệ Win/Tie/Loss vs PPO, động thái chọn toán tử (`Split`, `Merge`, `Transfer`) qua 3 giai đoạn tiến hóa. |
| **Bài báo 3**<br>*(Cost-Benefit)* | `Bai_3_Cost_Benefit_Analysis/results_bai3/` | `Tong_hop_so_lieu_Bai_3.md` | Bóc tách chi phí vi giây (PPO Overhead < 1.5%), RAM đỉnh < 600 MB, phân tích điểm hòa vốn Pareto và Time Budget. |
| **Tổng hợp phản biện**<br>*(Mục 4.4)* | `Tong_hop_so_lieu_phan_bien/` | `1_Bang_tong_hop_28_do_thi_cong_bang.csv`<br>`Tong_hop_toan_bo_28_do_thi.md` | Ma trận đối đầu 28 đồ thị chuẩn hóa, hiệu chỉnh đa kiểm định Holm-Bonferroni, bảng số liệu định dạng LaTeX sẵn sàng nhúng báo cáo. |

---

### 5. TÓM TẮT ĐÓNG GÓP KHOA HỌC CỐT LÕI

1. **Khắc phục triệt để bài toán mở chọn toán tử tĩnh (TS. Phạm Đình Thành - 2024):** Thay thế tỷ lệ đột biến tĩnh 33% bằng PPO-AOS học trực tuyến thích nghi theo động thái quần thể.
2. **Vector trạng thái 5 chiều nén ($S_t$) & Chuẩn hóa Welford:** Nén toàn bộ động học của 100 cá thể thành vector 5D $[f_{\min}^{\text{norm}}, f_{\text{avg}}^{\text{norm}}, \rho_{\text{feas}}, \bar{\phi}^{\text{norm}}, \tau^{\text{norm}}]$ giúp mô hình học nhanh, không bùng nổ không gian trạng thái.
3. **Vượt trội SOTA trên 28/28 đồ thị đối chuẩn công bằng:** `PPO-AOS` đạt kích thước tập phủ nhỏ hơn hoặc tương đương với ý nghĩa thống kê cao ($p < 0.05$ qua kiểm định Wilcoxon có hiệu chỉnh Holm-Bonferroni).
4. **Định lượng chi phí tính toán (Overhead) cực thấp:** Bài báo 3 chỉ ra chi phí suy luận nơ-ron PPO chỉ chiếm **< 1.5%** tổng thời gian, chứng minh tính khả thi ứng dụng thực tế vượt trội.

---
*Kính chúc Quý Thầy/Cô trong Hội đồng sức khỏe và có phiên đánh giá thành công tốt đẹp!*  
**Nhóm Tác giả & Kỹ sư Dự án EVO-RL MSCC**
