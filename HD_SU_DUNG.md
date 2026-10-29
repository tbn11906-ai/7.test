# HỆ THỐNG TIẾP NHẬN YÊU CẦU HIỆU CHUẨN & QUẢN LÝ SỔ THEO DÕI PTĐ
## CÔNG TY CỔ PHẦN CÔNG NGHỆ DIGI (DIGI TECHNOLOGIES)
**Phòng Dịch Vụ & Công Nghệ Hiệu Chuẩn**

---

### 1. HƯỚNG DẪN KHỞI CHẠY NHANH
- **Cách 1 (Khuyên dùng - Đầy đủ Backend + SQLite + Xuất Excel ISO):**
  Nhấp đúp chuột vào file: `CHAY_UNG_DUNG.bat` (hoặc mở Terminal gõ `python app.py`).
  Trình duyệt web sẽ tự động mở tại địa chỉ: **`http://localhost:5000`**
- **Cách 2 (Mở trực tiếp trên trình duyệt):**
  Nhấp đúp chuột vào file `index.html` để mở trong Chrome, Edge, Cốc Cốc hoặc Firefox.

---

### 2. TÀI KHOẢN ĐĂNG NHẬP
- Giao diện đăng nhập chuẩn phong cách **Glassmorphism**, logo DIGI Technologies sắc nét.
- **Bảo mật:** Không tự động điền mật khẩu, người dùng nhập trực tiếp thông tin xác thực:
  * **Admin CST:** `CST@digivn.com` / `CST@654`
  * **Nhân viên:** `nhanvien@digivn.com` / `123456`

---

### 3. CÁC TÍNH NĂNG THEO CẤU TRÚC MỚI NHẤT
1. **Thanh điều hướng (Navbar):**
   - **Tab 1: Tiếp Nhận**
   - **Tab 2: Phiếu Yêu Cầu**
   - **Tab 3: Sổ theo dõi**
2. **Tab 1 (Tiếp Nhận):**
   - **Mục 1:** Thông tin Khách Hàng.
   - **Mục 2:** Thông tin Phương Tiện Đo & khối nhập **MÃ MẪU** (Nhiệt, Nhiệt ẩm, Áp, Khí).
   - **Mục 3:** Quy trình hiệu chuẩn (QTHC Nhiệt kế, QTHC Nhiệt ẩm kế, QTHC Áp kế, QTHC Nồng độ khí).
   - **Mục 4:** Bảng chọn thông số hiệu chuẩn:
     * Nhóm Khí: 1.500.000 VNĐ / chỉ tiêu khí.
     * Nhóm Đo lường: Nhiệt độ 500.000 VNĐ, Chênh áp 500.000 VNĐ, **Nhiệt ẩm 750.000 VNĐ** (đã bỏ chữ chiếc).
   - **Mục 5:** Sắp xếp lại thứ tự tiếp nhận:
     1. **Ngày nhận PTĐ**
     2. **Ngày trả kết quả dự kiến**
     3. **Người Bàn giao**
     4. **Người nhận**
     5. **Nhân viên hiệu chuẩn (NVHC)**, Hình thức trả kết quả, Phụ tùng kèm theo & Lưu ý khác.
   - **Yêu cầu hiệu chuẩn (Mục 9):** Đã tinh chỉnh thành **"Hiệu chuẩn có hiệu chỉnh"** (bỏ cụm từ cho phép mở máy kiểm tra).
3. **Tab 2 (Phiếu Yêu Cầu BM.6.2.5):**
   - Căn chỉnh ngay hàng thẳng lối, chuẩn in A4 ISO 1 trang gọn gàng.
   - Tự động hiển thị "Hiệu chuẩn có hiệu chỉnh" tại Mục 9.
   - Chữ ký điện tử Ms. Nguyễn Thị Thúy Bình và bảng kiểm soát tài liệu BM.6.2.5 chuẩn mực.
4. **Tab 3 (Sổ theo dõi):**
   - **Thanh tiêu đề hạn chế màu sắc:** Thiết kế chuẩn mực ISO đơn sắc thanh lịch (nền slate-200/slate-100 trung tính, chữ đậm sắc nét, viền xám tinh tế, không màu mè sặc sỡ).
   - **Ghim cố định tiêu đề (Sticky Header):** Bảng cuộn dọc & cuộn ngang mượt mà, thanh tiêu đề 2 tầng luôn được ghim trên cùng.
   - **Bổ sung đầy đủ 5 cột chuyên biệt:**
     1. **Người nhận PTĐ**
     2. **Ngày nhận PTĐ**
     3. **Người trả PTĐ**
     4. **Ngày trả PTĐ**
     5. **Ngày hiệu chuẩn tiếp theo**
   - Modal chỉnh sửa (dành cho Admin) cập nhật trực tiếp đầy đủ 5 trường thông tin trên.
   - **Xuất file Excel (.xlsx):** Cấu trúc 20 cột chuẩn ISO, tiêu đề màu sắc trang nhã, công thức và định dạng tiền tệ chuyên nghiệp.
