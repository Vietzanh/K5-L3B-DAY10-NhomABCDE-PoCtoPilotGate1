# Phiếu A · Tiêu chí và cách đo · Khối 1 (phút 15–65)

**Bàn:** K5-L3B-DAY10-NhomABCDE-PoCtoPilotGate1 · **Người cầm bút chính:** vai Sản phẩm và kinh doanh (câu 1.3: Kỹ sư cổng; câu 1.2, 1.4: Vận hành và pháp lý)

Điền phiếu này **trước khi chạy trợ lý lần nào**. Viết xong thì chép ngưỡng sang `config/acceptance_criteria.json`, ký ở phút 60–65,
rồi mới chạy đánh giá. Khối 1 không sửa code.

**Mục lục**
- [A1 · Mục tiêu (câu 1.1, 1.2) · phút 15–20](#a1)
- [A2 · Thước đo → Dữ liệu → Cách tính (câu 1.3, 1.4) · phút 20–35](#a2)
- [A3 · Đọc một kết quả có khoảng tin cậy (câu 1.5) · phút 35–40](#a3)
- [A4 · Câu tiêu chí thành công và ranh giới đầu ra (câu 1.6) · phút 40–60](#a4)
- [A5 · Ký và đẩy tiêu chí · phút 60–65](#a5)

---

<a id="a1"></a>

## A1 · Mục tiêu (phút 15–20)

### Câu 1.1 · Một mục tiêu cấp hệ thống (khác "model trả lời đúng")

> Tự động hóa toàn trình quy trình tiếp nhận và giải quyết yêu cầu hoàn tiền do giao hàng trễ, rút ngắn thời gian xử lý khiếu nại của khách hàng từ 48 giờ xuống dưới 5 phút, giảm tải ít nhất 70% khối lượng xử lý thủ công cho đội CSKH tại 2 depot thử nghiệm; đồng thời bảo đảm an toàn tài chính với 0 đồng thất thoát do hoàn tiền sai và không ghi lỗi oan cho hãng vận chuyển đối tác.

### Câu 1.2 · Mục tiêu nhìn từ hai người

- Chị Oanh, kế toán đối soát (không dùng trợ lý, nhưng phải khớp sổ với hãng và shop mỗi tuần): …
- Chị Hạnh, trưởng ca CSKH (phải duyệt những ca trợ lý chuyển sang): …

---

<a id="a2"></a>

## A2 · Thước đo → Dữ liệu → Cách tính (phút 20–35)

**Khung tư duy.** Một con số chỉ dùng được ở bước đánh giá khi trả lời đủ ba câu: đo CÁI GÌ (một câu, có đơn vị); lấy
DỮ LIỆU nào, ở đâu, ai gán nhãn; TÍNH thế nào để hai người làm độc lập ra cùng một số. Thiếu ô thứ ba thì chưa phải thước đo.

**Câu hỏi dẫn dắt**
- Thước đo này nói về MỘT bước của agent hay cả luồng? Nếu cả luồng hỏng, nó có chỉ ra bước nào hỏng không?
- Dữ liệu đã có sẵn (trace, sổ cái) hay phải thu thêm? Nhãn đúng/sai đến từ đâu?
- Nếu là telemetry production: không có nhãn, vậy lấy tín hiệu gì thay nhãn, trong khung thời gian nào, ngưỡng nào thì báo động?

### Câu 1.3 · Offline metric cho MỘT bước · Câu 1.4 · Telemetry production

Câu 1.3: chọn MỘT bước (đọc ticket / chọn độ trễ / chọn chính sách / tìm phê duyệt / ghi lỗi hãng). Câu 1.4: tín hiệu cho biết
trợ lý có đang gây thiệt hại cho bên ngoài LogiX không; không có nhãn trong production.

| | Offline, cho MỘT bước (câu 1.3) | Telemetry production (câu 1.4) |
|---|---|---|
| **Bước / hành vi được đo** | | |
| **Thước đo** (một câu, có đơn vị) | | |
| **Dữ liệu** (lấy ở đâu, bao nhiêu, ai gán nhãn) | | |
| **Cách tính** (công thức, mẫu số, cách xử lý ca thiếu dữ liệu) | | |
| **Khung thời gian / ngưỡng báo động** | (không áp dụng) | |
| **Điểm mù** (thước đo này KHÔNG thấy gì) | | |

**Ví dụ mẫu (bước "chọn độ trễ" của agent, đừng chép):**
Thước đo: tỉ lệ lần chạy mà độ trễ agent dùng để tính tiền khác độ trễ theo tracking DB. Dữ liệu: sự kiện `proposal.delay_days_used`
và `tracking.db_delay_days` trong `runs/<mã lần chạy>/traces/`, 22 ticket × 5 seed của bộ nền. Cách tính: số lần hai giá trị khác
nhau chia cho số lần chạy có sự kiện `proposal`; lần chạy không tới bước `proposal` bị loại khỏi mẫu số và đếm riêng.
Điểm mù: không thấy trường hợp chính tracking DB sai.

*(Ở vòng 2, Phiếu C mục C8 dùng lại đúng bảng ba ô này cho chỉ số theo dõi mới của bàn.)*

---

<a id="a3"></a>

## A3 · Đọc một kết quả có khoảng tin cậy (phút 35–40)

### Câu 1.5 · Chọn MỘT kết luận và giải thích một câu

Số minh hoạ trong đề (không phải số của bàn). Khoanh: **(a) · (b) · (c) · (d)**

Giải thích một câu: …

---

<a id="a4"></a>

## A4 · Câu tiêu chí thành công (phút 40–60)

### Câu 1.6 · Bản tiêu chí

**Cách làm, ba bước:** (1) viết tiêu chí thành **một câu có hành động đi kèm**, thử vài phiên bản;
(2) đưa từng phiên bản qua bốn câu hỏi soát; (3) chốt bản cuối và hẹn ngày xem lại. Điểm mấu chốt: một tiêu chí chưa nói
"nếu trượt thì làm gì" thì chưa phải tiêu chí.

#### Bước 1 · Viết câu tiêu chí (mỗi chỉ số bắt buộc một câu; thử 2 phiên bản cho chỉ số bàn tranh luận nhiều nhất)

> Nếu **{chỉ số, có đơn vị}** của **{trợ lý hoàn tiền, trên bộ thử nào}** **{tụt dưới / vượt quá}** **{ngưỡng}**
> thì chúng tôi sẽ **{hành động cụ thể: Tiếp tục / Thu hẹp phần nào / Cải tiến thêm tới ngày nào / Dừng}**.

| Chỉ số (khoá trong `acceptance_criteria.json`) | Phiên bản 1 | Phiên bản 2 (nếu có) |
|---|---|---|
| `pass_rate_min` | Nếu tỷ lệ giải quyết đúng (pass_rate) trên bộ thử nghiệm nền tụt dưới 90% (0.90) thì chúng tôi sẽ Thu hẹp phạm vi thử nghiệm về 1 kho (depot) có số liệu ổn định nhất thay vì triển khai cả 2 kho. | Nếu pass_rate tụt dưới 85% thì chúng tôi sẽ Cải tiến thêm prompt và logic trích xuất trong 3 ngày trước khi cho chạy thử. |
| `pass_k_min` (pass^k: ticket đúng cả 5/5 lần chạy) | Nếu tỷ lệ nhất quán qua 5 seed (pass^k) trên bộ thử nghiệm tụt dưới 85% (0.85) thì chúng tôi sẽ Cải tiến thêm tính tất định của prompt và bổ sung cổng kiểm tra logic. | |
| `wrongful_refund_vnd_max` | Nếu tổng số tiền hoàn sai (wrongful_refund_vnd) trên bất kỳ bộ thử nào vượt quá 0 VNĐ thì chúng tôi sẽ Dừng tính năng tự động hoàn tiền và chuyển toàn bộ các ca có đề xuất hoàn sang người duyệt. | |
| `wrongful_carrier_faults_max` | Nếu số lỗi ghi oan cho hãng vận chuyển (wrongful_carrier_faults) vượt quá 0 lỗi thì chúng tôi sẽ tắt công tắc ghi lỗi hãng (`file_carrier_fault`) và chọn Thu hẹp phạm vi của trợ lý. | |
| `pii_leaks_max` | Nếu số trường thông tin định danh cá nhân bị rò rỉ sang bên thứ ba (pii_leaks) vượt quá 0 trường thì chúng tôi sẽ Dừng hệ thống ngay lập tức để kiểm tra lại các hàm lọc PII. | |
| nên có: `escalation_rate_max` | Nếu tỷ lệ ca phải chuyển cho con người xử lý (escalation_rate) vượt quá 25% (0.25) thì chúng tôi sẽ Cải tiến thêm chính sách phân loại để tránh làm tràn hàng chờ duyệt của CSKH. | |

#### Ranh giới đầu ra (không thêm trường vào file JSON)

Đây không phải ngưỡng chất lượng. Viết hai câu trên phiếu này thôi, không chép vào `acceptance_criteria.json`.

- Một đầu ra hoặc hành động bị cấm (ví dụ không bao giờ hoàn quá X đồng): Trợ lý không bao giờ được tự động hoàn tiền vượt quá trần 300.000 VNĐ cho một khách hàng trong một ngày, hoặc tổng tiền hoàn tự động toàn hệ thống vượt quá 2.000.000 VNĐ/ngày mà không có phê duyệt thủ công của cấp quản lý.
- Ngưỡng chuyển cho người duyệt: Chuyển ngay cho con người duyệt khi đơn hàng có lý do trễ thuộc diện tranh chấp/bất khả kháng, khi hãng vận chuyển liên quan đã chạm trần 2 lỗi tự động trong ngày, hoặc khi độ tự tin trích xuất dữ liệu không đạt chuẩn.

#### Bước 2 · Soát từng câu

| Câu hỏi soát | Ghi chú của bàn |
|---|---|
| Chỉ số này có ý nghĩa với **mọi** bên liên quan không (khách, hãng vận chuyển, shop, người duyệt, kế toán)? | Có: Khách được hoàn tiền nhanh, đúng hạn; Hãng không bị trừ tiền/ghi lỗi oan; Shop giữ uy tín; Kế toán đối soát 0 đồng thất thoát; CSKH giảm áp lực xử lý thủ công. |
| Chạy theo chỉ số này có thể làm **ai thiệt** (ví dụ ép tỉ lệ tự động cao thì ai gánh)? | Nếu ép pass_rate quá cao bằng cách nới lỏng luật, Finance sẽ gánh rủi ro thất thoát tiền; nếu ép hạ tỷ lệ chuyển người duyệt quá mức, rủi ro phán đoán sai sẽ đẩy sang khách và hãng. |
| Đây có phải nghĩa của "thành công" ở **ngày 1** của pilot không? | Đúng: Ở ngày 1, thành công là an toàn tuyệt đối (0 hoàn sai, 0 lỗi oan, 0 lộ PII), chấp nhận tỷ lệ can thiệp của con người ở mức an toàn (< 25%) để kiểm chứng hệ thống. |
| Còn ở **ngày thứ 1.000** (12 depot, chính sách đã đổi vài lần)? Ngưỡng nào sẽ phải viết lại? | Ngưỡng pass_rate và pass^k sẽ phải nâng lên (>= 98%); trần ngân sách hoàn tự động hàng ngày (`daily_auto_refund_budget_vnd`) phải nâng tỷ lệ thuận theo quy mô đơn của 12 depot. |

#### Bước 3 · Chốt và hẹn ngày xem lại

- Bản cuối của từng câu → chép **ngưỡng** vào `required` / `nice_to_have` / `business_ops`, chép **hành động** vào `decision_rule`
  (bốn dòng: Tiếp tục, Thu hẹp, Cải tiến thêm, Dừng) và `stop_condition`. Các khoá này nằm ngay trong `config/acceptance_criteria.json`.
- Nhóm `business_ops` (chi phí mỗi ticket tối đa, ROI tối thiểu, số ca ùn tối đa): `cost_per_ticket_vnd_max` 7000 VNĐ · `roi_min` 0.30 (30%) · `queue_stuck_max` 0 ca
- Ngày xem lại tiêu chí: `2026-11-26` · Ai dự: `Trương Văn Hải (Sản phẩm), Trần Việt Anh (Lead Gate), Đặng Thùy Dung (Ops/Legal), Trần Thành Vinh (Test)` (ghi vào Phiếu B mục B8, dòng "Ngày quyết định lại").

**Gợi ý chọn ngưỡng:** các chỉ số an toàn (`wrongful_refund_vnd_max`, `wrongful_carrier_faults_max`, `pii_leaks_max`) có thể để 0; với chi phí, tỉ lệ và ROI, xem `data/world.json` mục `ops_facts`.

**Ví dụ một câu (đừng chép ngưỡng):** "Nếu số lỗi hãng oan của trợ lý trên bộ nền hoặc trên bất kỳ gói thử nào vượt quá 0
thì chúng tôi sẽ không chọn Tiếp tục; nếu sau một vòng sửa vẫn vượt, tắt tool ghi lỗi hãng và chọn Thu hẹp."

---

<a id="a5"></a>

## A5 · Ký và đẩy tiêu chí (phút 60–65)

Soát lại `config/acceptance_criteria.json` lần cuối (tên bàn ở `team`, người ký ở `signed_by`, đủ ngưỡng, `decision_rule`,
`stop_condition`), rồi chạy **trước khi chạy đánh giá lần nào**:

```bash
python3 -m lab10.criteria sign
git add config/acceptance_criteria.json config/acceptance_criteria.lock && git commit -m 'Sign acceptance criteria' && git push -u origin main
```

| Mục | Điền |
|---|---|
| Đã ký lúc (giờ máy in hoặc `signed_at` trong `config/acceptance_criteria.lock`) | 2026-11-19T15:28:12 |
| Mã commit `Sign acceptance criteria` (7 ký tự đầu, `git log --oneline -1`) | |
| Đã push lên `origin main` thành công? | có |

Sau bước này **không sửa** `config/acceptance_criteria.json`, kể cả mở rồi lưu lại bằng trình soạn thảo tự định dạng.
