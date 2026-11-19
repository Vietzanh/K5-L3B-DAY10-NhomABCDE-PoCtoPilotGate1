# Team

## Thông tin nhóm

- Tên nhóm (`TenNhom`, không dấu, không khoảng trắng): NhomABCDE
- Lớp: `L3B`
- Repo của bàn: `https://github.com/Vietzanh/K5-L3B-DAY10-NhomABCDE-PoCtoPilotGate1`
- Thẻ sự cố đã bốc (S1–S8): S3

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
- Hoàn thành Checkpoint 2 (Khối 1):
  - Viết mục tiêu cấp hệ thống tại Câu 1.1 (Phiếu A, mục A1) dựa trên PRD v1.1 §3.
  - Soạn thảo toàn bộ Bản tiêu chí chấp nhận tại Câu 1.6 (Phiếu A, mục A4) gồm bảng câu tiêu chí "Nếu ... thì ...", các câu ranh giới đầu ra, 4 câu hỏi soát và xác lập thời hạn xem lại tiêu chí.
  - Thiết lập các ngưỡng bắt buộc, ngưỡng kinh doanh vận hành (`business_ops`), điều kiện dừng và 4 quy tắc quyết định `decision_rule` trong `config/acceptance_criteria.json`.
  - Thực hiện lệnh ký `python -m lab10.criteria sign`, sinh mã niêm phong hash SHA-256 trong `config/acceptance_criteria.lock`.
- Hoàn thành Checkpoint 3 (Khối 2):
  - Viết Bản đồ dữ liệu & kịch bản Data Drift trong 3 tháng tại Câu 2.3 (Phiếu B, mục B3).
  - Điền các con số kinh doanh tại Câu 2.9 (Phiếu B, mục B7.4) và cấu hình `config/operating_gates.json` (mục `business`: ngân sách ticket 1.500đ, trần hoàn tự động 2.000.000đ/ngày, ROI tối thiểu 0.30).
  - Tham gia Pre-mortem lăng kính kinh doanh tại Câu 2.5 (Phiếu B, mục B6) và đồng thuận Quyết định v1 tại Mục B8.
- Hoàn thành Checkpoint 4 & 5 (Khối 3 & Chốt Gate 1):
  - Soạn thảo Specification định lượng tại Câu 3.2 (Phiếu C, mục C5) ràng buộc phiên bản hiệu lực theo ngày (`effective_from <= as_of <= effective_to`) và trần phạt đối tác 2 lỗi/hãng/ngày.
  - Tham gia xây dựng Fault Tree trước sửa (Câu 3.4, mục C6) và sau sửa (Câu 3.7, mục C9) cùng cả bàn.
  - Rà soát các chỉ số kinh doanh tại mốc after: ROI đạt 1.51 (> 0.30 đã ký), chi phí mỗi ticket 3.980đ (< 7.000đ), độ phủ pilot đạt 100%.
  - Thống nhất Quyết định Gate 1 v2 là "Tiếp tục" tại Mục C12 và hoàn thiện 3 dòng bắt buộc cho gói nộp bài.

### Bằng chứng

- Commit ký tiêu chí bắt buộc: `015490a` ("Sign acceptance criteria").
- Mã niêm phong hash SHA-256 tiêu chí: `7d12c9c2d2dd7245217d35d8733c39b1bd77da70603750ed19ad865f6c6a44fa`.
- Hash chốt cổng vòng 1: `69a3da71`.
- Báo cáo tự kiểm tra thẻ sự cố S3: `R-S3-grade-20261119-172718-690ce3` (PASS-VISIBLE: 6/6 check đạt ✅).
- Các mốc chạy: Base `R-S3-before-20261119-172718-690ce3`, Prepared `R-S3-prepared-20261119-172719-690ce3`, After `R-S3-after-20261119-172719-690ce3`.
- Bằng chứng trong phiếu: Phiếu A (A1, A4); Phiếu B (B3, B6, B7.4, B8); Phiếu C (C5, C6, C7, C9, C12).
- Commit hoàn tất bài nộp: `dcd8a93` ("chore: sync submission package after final grade").

### Exit ticket

- **Một điều học được:** Quy tắc nghiệp vụ đổi đời thực (Concept Drift) nếu không có cơ chế ghim kiểm tra theo ngày hiệu lực thì cờ database cũ sẽ làm hệ thống AI tự động hóa vi phạm pháp lý và tài chính hàng loạt.
- **Một điều còn chưa chắc:** Trong môi trường sản xuất thực tế khi xảy ra thiên tai kéo dài qua nhiều tuần, cần cơ chế tự động điều phối ngưỡng lỗi tuần (5 lỗi/7 ngày) như thế nào để vừa bảo vệ đối tác vừa không để lọt lỗi vận hành nghiêm trọng.

## DangThuyDung-2A202604116

### Phần việc phụ trách

- **Vai trò:** Kỹ sư cổng 1 (chạy lệnh đo, code cổng phòng ngừa, chốt vòng 1).
- **File chính:** `lab10/guards.py` (`pre_guard`, `write_gate`); chạy `lab10.eval`, `lab10.gate`, `lab10.checkpoint`, `lab10.grade`.
- **Phiếu:** A câu 1.3 và 1.5 · B mục B0 (dòng 1–3), B1 (câu 2.1), B7.1 (câu 2.6) · C mục C0 (dòng 1–5), C2 lỗi 1 và lỗi 3 (câu 3.1), C7 (câu 3.5).

### Đóng góp cụ thể

- **Câu 2.1:** chạy mốc base, so với tiêu chí đã ký; chỉ ra 2 ngưỡng an toàn trượt (hoàn sai 20.000đ, 1 lỗi hãng oan, cùng từ `T-002@55`, kho HCM / hãng VNX) và tỉ lệ chuyển người sát trần (0,2273 / 0,25); khuyến nghị cổng "kết hợp".
- **Câu 2.6 · cổng vòng 1** trong `write_gate`: (1) trước `issue_refund`, tính lại số tiền được hoàn từ tracking + chính sách hiệu lực theo ngày, trừ phần đã hoàn, đòi quá thì `modify` / `deny`; (2) trước `file_carrier_fault`, chỉ ghi lỗi khi `carrier_at_fault` theo tracking. Dùng `deny`/`modify` thay vì `escalate` để không vượt trần chuyển người 0,25 đã ký.
- **Chốt vòng 1** (`checkpoint` `69a3da71`), chạy mốc prepared và `gate`: cả 9 dòng ĐẠT trên bộ nền. Chép mục `business` từ B7.4 của Hải vào config trước khi chốt.
- **Vòng 2, thẻ S3:** chạy `grade` mốc prepared; phát hiện và sửa lỗi integrity giả do xuống dòng CRLF trên Windows (checkout lại LF, nội dung không đổi). Trace `S3-02` (áp chính sách v3 dù v4 đã hiệu lực) và `S3-42`/`S3-43` (lỗi thứ 3, 4 của MKD trong một ngày).
- **Câu 3.5 · cổng vòng 2:** (3) `pre_guard` ghim chính sách theo ngày hiệu lực, không theo cờ `index_active`, ghi sự kiện `policy_pinned`; (5) trong `write_gate`, trần lỗi tự động mỗi hãng mỗi ngày đọc từ `ops_limits`, ghi sự kiện `carrier_strike_cap`. Hai sự kiện này là đầu vào cho các metric trong `monitors.py`.
- Ghép lại bảng C8 của Vinh bị mất khi gộp nhánh.

### Bằng chứng

- **Commit:** `4fdce67` (B0, B1) · `25faff4` (cổng 1, 2 + B7.1) · `8fc035d` (Phiếu A câu 1.3, 1.5) · `e9a75de` (config `business`) · `b66bc32` (chốt vòng 1) · `5e2285b` (B0 dòng 3) · `26d9a90` (cổng ghim chính sách + C2 lỗi 1) · `14dac60` (trần lỗi hãng/ngày + C2 lỗi 3) · `d08878c` (C7) · `da8e4b8`, `d927a45` (C0) · `e2eeaab` (ghép C8 của Vinh).
- **Mã lần chạy:** base `R-base-before-20261119-154112-bde05c` · cổng vòng 1 `R-base-after-20261119-155814-c54894` · prepared `R-base-prepared-20261119-163205-7f05d4` · S3 prepared `R-S3-prepared-20261119-163718-97c54a` · S3 sau ghim chính sách `R-S3-after-20261119-165606-64db18` · S3 sau trần lỗi hãng `R-S3-after-20261119-165948-f19d4a` (60/60 đạt) · grade `R-S3-grade-20261119-171012-baede0` (PASS-VISIBLE).
- **Trong phiếu:** Phiếu B mục B0, B1, B7.1; Phiếu C mục C0, C2 (lỗi 1, lỗi 3), C7.
- **Dùng AI:** dùng Claude (Claude Code) để đọc code lab, gợi ý và viết cổng trong `guards.py`, chạy lệnh và soạn nháp các ô phiếu; các con số, cổng và kết luận đã được đối chiếu lại với trace và report.

### Exit ticket

- **Một điều học được:** *(Dung tự viết)*
- **Một điều còn chưa chắc:** *(Dung tự viết)*

## HoVaTen-MSSV

### Phần việc phụ trách

Vai trong bàn; câu nào của đề, mục nào của phiếu A/B/C, file nào (`lab10/guards.py`, `config/operating_gates.json`, …).

### Đóng góp cụ thể

...

### Bằng chứng

Mã commit, mã lần chạy (`runs/<mã>`), dòng trong phiếu.

### Exit ticket

Một điều học được, một điều còn chưa chắc.
