# Team

## Thông tin nhóm

- Tên nhóm (`TenNhom`, không dấu, không khoảng trắng): NhomABCDE
- Lớp: `L3B`
- Repo của bàn: `https://github.com/Vietzanh/K5-L3B-DAY10-NhomABCDE-PoCtoPilotGate1`
- Thẻ sự cố đã bốc (S1–S8):

## Thành viên

Họ tên đầy đủ và MSSV của **mọi** thành viên; bàn 3 người thì để trống dòng 4. Vai: Kỹ sư cổng · Sản phẩm và kinh doanh · Vận hành và pháp lý (README mục 3, phút 0–15).

| STT | Họ và tên       | MSSV        | Vai                   | Trưởng nhóm |
| --: | --------------- | ----------- | --------------------- | :---------: |
|   1 | Trần Việt Anh   | 2A202604029 | Vận hành & Pháp lý    |      x      |
|   2 | Trương Văn Hải  | 2A202604018 | Sản phẩm & Kinh doanh |
|   3 | Đặng Thùy Dung  | 2A202604116 | Kỹ sư cổng 1          |             |
|   4 | Trần Thành Vinh | 2A202603821 | Kỹ sư cổng 2          |             |

Ghi `members` trong `submission/submission.json` theo dạng `"HoVaTen-MSSV"`, khớp bảng trên.

## Cá nhân

Mỗi thành viên tự viết một mục bên dưới (chép mẫu, đổi tiêu đề thành họ tên không dấu và MSSV, ví dụ `## NguyenVanAn-20241234`).

## TruongVanHai-2A202604018

### Phần việc phụ trách

- **Vai trò:** Sản phẩm & Kinh doanh (Product & Business)
- **Nhiệm vụ chính:**
  - **Khối 1 (Phiếu A):** 
    - Câu 1.1 (Mục tiêu hệ thống theo PRD v1.1 §3).
    - Câu 1.6 (Bản tiêu chí chấp nhận "Nếu ... thì ...", soát ranh giới đầu ra).
    - File cấu hình: `config/acceptance_criteria.json` (ngưỡng pass rate, pass^k, trần hoàn sai, lỗi hãng, PII, chi phí, ROI, điều kiện dừng, quy tắc quyết định `decision_rule`).
  - **Khối 2 (Phiếu B):** 
    - Câu 2.3 (Bản đồ dữ liệu & kịch bản Data Drift trong 3 tháng).
    - Câu 2.9 (Cổng kinh doanh trong `config/operating_gates.json` mục `business`: trần tiền hoàn ngày, ngân sách ticket, phạm vi pilot, ROI).
    - Câu 2.5 (Tham gia Pre-mortem lăng kính kinh doanh) & B8 (Chốt Quyết định v1).
  - **Khối 3 (Phiếu C):** 
    - Câu 3.2 (Specification ngăn chặn tác hại của thẻ sự cố).
    - Câu 3.5 (Điều chỉnh cổng kinh doanh trong `config/operating_gates.json`).
    - Câu 3.4 & 3.7 (Tham gia Fault Tree).
    - Câu 3.8 / C12 (Đồng thuận Quyết định v2 và 3 dòng bắt buộc).

### Đóng góp cụ thể

- Hoàn thành Checkpoint 1: Xác nhận vai trò trong bàn, thiết lập mục cá nhân trong `TEAM.md`.
- Rà soát các tài liệu đầu vào: `data/world.json` (mục `ops_facts`, `ops_limits`), file mẫu `config/acceptance_criteria.example.json`.
- Chuẩn bị tài liệu đối chiếu PRD v1.1 (§2, §3, §6) và Eval Card từ Lab 9 để sẵn sàng cho Checkpoint 2 (soạn thảo và ký tiêu chí nghiệm thu).

### Bằng chứng

- Thiết lập mục cá nhân trong `TEAM.md`.
- Sẵn sàng các tài liệu chuẩn bị cho Khối 1 và commit ký tiêu chí tiếp theo.

### Exit ticket

- **Một điều học được:** Bản tiêu chí chấp nhận phải được ký và khóa bằng mã hash trước khi nhìn thấy số liệu đo đạc thực tế để đảm bảo tính khách quan (đặt luật trước, xem số sau).
- **Một điều còn chưa chắc:** Cách cân đối giữa việc hạ trần hoàn tiền để tránh rủi ro tài chính với việc giữ cho tỷ lệ ca phải chuyển người duyệt (escalation rate) không bị quá tải.

## HoVaTen-MSSV

### Phần việc phụ trách

Vai trong bàn; câu nào của đề, mục nào của phiếu A/B/C, file nào (`lab10/guards.py`, `config/operating_gates.json`, …).

### Đóng góp cụ thể

...

### Bằng chứng

Mã commit, mã lần chạy (`runs/<mã>`), dòng trong phiếu.

### Exit ticket

Một điều học được, một điều còn chưa chắc.
