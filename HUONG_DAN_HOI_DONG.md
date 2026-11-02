# HƯỚNG DẪN NGHIỆM THU DÀNH CHO HỘI ĐỒNG KHOA HỌC
## ĐỀ TÀI: KHUNG TỐI ƯU HÓA TIẾN HÓA KẾT HỢP HỌC TĂNG CƯỜNG SÂU (EVO-RL / PPO-AOS) CHO BÀI TOÁN MINIMUM s-CLUB COVER
**Gói sản phẩm:** `Sanpham_nckh` | **Phiên bản:** Hoàn thiện nghiệm thu | **Độc lập & Khả chuyển 100%**

---

### KÍNH GỬI QUÝ THẦY CÔ VÀ CÁC THÀNH VIÊN HỘI ĐỒNG ĐÁNH GIÁ

Nhóm nghiên cứu trân trọng gửi tới Quý Hội đồng toàn bộ gói sản phẩm phần mềm, cơ sở dữ liệu thực nghiệm, mã nguồn và tài liệu học thuật hoàn chỉnh của đề tài. Gói sản phẩm được tổ chức tinh gọn, khả chuyển và sẵn sàng thực thi 1-Click trên mọi máy tính Windows mà không cần cấu hình phức tạp.

---

### 1. BẮT ĐẦU NHANH (QUICK START - 1 CLICK)

> [!IMPORTANT]
> **Khởi chạy trực quan nhanh nhất:** Quý Thầy/Cô chỉ cần nhấp đúp chuột vào tệp:
> ```cmd
> CHAY_CHUONG_TRINH_TONG.bat
> ```
> *(Hoặc tệp phím tắt `CHAY.bat` tại thư mục gốc. Nếu máy tính mới chưa cài đặt môi trường, vui lòng nhấp đúp `setup.bat` trước).*

#### Giao diện Menu Điều khiển Trực quan (`CHAY_CHUONG_TRINH_TONG.bat`):
* **`--- [A] CHƯƠNG TRÌNH THỰC NGHIỆM (EVO-RL MSCC) ---`**
  * **`[1]` Tùy Chọn Đồ Thị Theo Tên:** Nhập hoặc dán danh sách tên đồ thị tùy ý để chạy.
  * **`[2]` Giao Diện Tương Tác Chọn Đồ Thị TUI:** Dùng phím mũi tên [▲/▼], phím Space [X] và Enter để chọn đồ thị trực quan.
  * **`[3]` Tùy Chỉnh Siêu Tham Số Nâng Cao:** Thiết lập $s$, số seeds (mặc định 20), số workers (10), epochs (200), pop_size (100).
* **`--- [B] XUẤT BIỂU ĐỒ, SỐ LIỆU VÀ BÁO CÁO KHOA HỌC ---`**
  * **`[4]` Xuất Biểu Đồ Phân Tích & Hội Tụ:** Tự động tạo thư mục `Chart_seed/` chứa 7 biểu đồ 600 DPI (PNG) và Vector PDF.
  * **`[5]` Tổng Hợp Bảng Số Liệu Báo Cáo:** Trích xuất tự động ma trận kết quả 30 đồ thị, CSV và báo cáo Markdown.
* **`--- [C] CÔNG CỤ VÀ TIỆN ÍCH HỆ THỐNG ---`**
  * **`[6]` Kiểm Tra Toàn Diện Hệ Thống:** Chạy tự động 9 giai đoạn kiểm chứng (< 5 giây).
  * **`[7]` Thiết Lập Môi Trường & GPU:** Cài đặt thư viện tự động và kiểm tra card đồ họa NVIDIA CUDA.
  * **`[0]` Thoát chương trình.**

---

### 2. KIỂM CHỨNG NHANH TOÀN HỆ THỐNG TRONG 5 GIÂY

Để đánh giá nhanh tính toàn vẹn của mã nguồn, thư viện và dữ liệu trước khi nghiệm thu:
* **Cách 1:** Chọn phím **`[6]`** trong `CHAY_CHUONG_TRINH_TONG.bat`.
* **Cách 2:** Mở thư mục **`Run.bat/`** và nhấp đúp `verify_all.bat`.
* **Cách 3:** Chạy lệnh Terminal: `python verify_system.py`.

*Kết quả kiểm chứng chuẩn khi đạt:*
```text
[✓] TẤT CẢ 9/9 GIAI ĐOẠN ĐÃ VƯỢT QUA XUẤT SẮC! (~5s)
Hệ thống 'Sanpham_nckh' đạt chuẩn 100% tính độc lập, khả chuyển và sẵn sàng nộp Hội đồng!
```

---

### 3. CẤU TRÚC GÓI SẢN PHẨM TINH GỌN

Toàn bộ các tệp thực thi chi tiết đã được gom gọn gàng, trực quan và dễ sử dụng:

```text
Sanpham_nckh/
├── CHAY_CHUONG_TRINH_TONG.bat   <-- [CHÍNH] Menu tổng điều khiển trực quan tất cả tính năng
├── CHAY.bat                    <-- Phím tắt 1-Click nhanh khởi chạy Menu Tổng
├── setup.bat                    <-- Cài đặt môi trường tự động (Python, CUDA, thư viện)
│
├── Run.bat/                     <-- THƯ MỤC CHỨA CÁC RUNNER CHI TIẾT:
│   ├── run.bat                  <-- Runner thực nghiệm EVO-RL MSCC (tùy chọn đồ thị & siêu tham số)
│   ├── runbieudo.bat            <-- Xuất biểu đồ chuẩn 600 DPI & Vector PDF (Chart_seed)
│   ├── run_tong_hop_so_lieu.bat <-- Trích xuất và tổng hợp báo cáo số liệu
│   ├── verify_all.bat           <-- Kiểm chứng tự động 9 giai đoạn mã nguồn
│   └── RUN_ALL.bat              <-- Phím tắt chuyển tiếp tới CHAY_CHUONG_TRINH_TONG.bat
│
├── configs/                     <-- Cấu hình siêu tham số giải thuật (khóa cứng chuẩn đối chuẩn)
├── dataset/ & problem/          <-- Nạp đồ thị, mô hình hóa SClubGraph, Individual, Fitness
├── operators/                   <-- Toán tử di truyền Crossover, Mutation (Split/Merge/Transfer), Repair
├── rl/ & environment/           <-- Não bộ Deep RL: Mạng Actor-Critic MLP, MDP Gym Environment, Reward
├── trainer/ & analysis/         <-- Vòng lặp tiến hóa lai (GGA + PPO), vẽ biểu đồ 600 DPI
│
├── pbodulieu/                   <-- Bộ 30 đồ thị benchmark chuẩn (12 mạng thực tế + 18 DIMACS)
├── results/                     <-- Cơ sở dữ liệu kết quả thực nghiệm (30 đồ thị x 20 seeds x 8 thuật toán)
└── Tong_hop_so_lieu_phan_bien/  <-- Bộ công cụ tổng hợp số liệu đối chuẩn & bảng Markdown
```

---

### 4. BẢN ĐỒ DỮ LIỆU KẾT QUẢ THỰC NGHIỆM

Toàn bộ kết quả thực nghiệm chính thức đã được chạy sẵn và lưu trữ đầy đủ trong các thư mục tương ứng:

| Nhóm kết quả | Vị trí lưu trữ | Tệp báo cáo chính | Nội dung & Chỉ số cốt lõi |
| :--- | :--- | :--- | :--- |
| **Thực nghiệm EVO-RL MSCC** | `results/ketqua_2026-09-13_11-43-21/` | `Tong_20_lan_seed.md`<br>`summary_metrics.csv`<br>`Chart_seed/` | 30 đồ thị $\times$ 20 seeds $\times$ 8 thuật toán: Best/Mean/Std $\|C\|$, thời gian chạy, kiểm định thống kê Wilcoxon ($p < 0.05$), 7 biểu đồ 600 DPI và vector PDF. |
| **Tổng hợp số liệu đối chuẩn** | `Tong_hop_so_lieu_phan_bien/` | `1_Bang_tong_hop_30_do_thi_cong_bang.csv`<br>`Tong_hop_toan_bo_30_do_thi.md` | Ma trận đối đầu 30 đồ thị chuẩn hóa, hiệu chỉnh đa kiểm định Holm-Bonferroni, bảng chi tiết từng đồ thị kèm liên kết Markdown. |

---

### 5. TÓM TẮT ĐÓNG GÓP KHOA HỌC CỐT LÕI

1. **Khắc phục triệt để bài toán mở chọn toán tử tĩnh (TS. Phạm Đình Thành - 2024):** Thay thế tỷ lệ đột biến tĩnh 33% bằng PPO-AOS học trực tuyến thích nghi theo động thái quần thể.
2. **Vector trạng thái 5 chiều nén ($S_t$) & Chuẩn hóa Welford:** Nén toàn bộ động học của 100 cá thể thành vector 5D $[f_{\min}^{\text{norm}}, f_{\text{avg}}^{\text{norm}}, \rho_{\text{feas}}, \bar{\phi}^{\text{norm}}, \tau^{\text{norm}}]$ giúp mô hình học nhanh, không bùng nổ không gian trạng thái.
3. **Hàm phần thưởng Feasibility-Aware 4 thành phần:** Định hướng cân bằng giữa thu gọn kích thước tập phủ và sửa sai nghiệm không khả thi.
4. **Vượt trội SOTA trên 30 đồ thị benchmark đối chuẩn công bằng:** `PPO-AOS` đạt kích thước tập phủ nhỏ hơn hoặc tương đương với ý nghĩa thống kê cao ($p < 0.05$ qua kiểm định Wilcoxon có hiệu chỉnh Holm-Bonferroni).

---
*Kính chúc Quý Thầy/Cô trong Hội đồng sức khỏe và có phiên đánh giá thành công tốt đẹp!*  
**Nhóm Tác giả & Kỹ sư Dự án EVO-RL MSCC**
