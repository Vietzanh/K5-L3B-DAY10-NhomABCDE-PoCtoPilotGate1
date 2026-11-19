"""★ FILE ĐỘI SỬA (1/3): cổng cấp hệ thống, nằm NGOÀI model và prompt.

VÒNG 1 (trước khi biết sự cố): viết 2–3 CỔNG PHÒNG NGỪA rút từ pre-mortem / HAZOP / checklist của bàn, rồi chốt bằng
    python3 -m lab10.checkpoint        (chép file này thành guards_round1.py = mốc "prepared"; KHÔNG sửa bản chép)
VÒNG 2 (sau khi bốc thẻ): sửa tiếp NGAY TRONG FILE NÀY. Giữ các cổng vòng 1, thêm cổng mới.
Hai file còn lại bàn được sửa: lab10/monitors.py (chỉ số theo dõi) và config/operating_gates.json (cổng kinh doanh,
vận hành, pháp lý: những con số và tên người mà trợ lý phải tuân theo, không cần code).

Hai điểm móc, agent gọi tự động:
  pre_guard(ctx)          chạy TRƯỚC khi agent đọc ticket
  write_gate(ctx, action) chạy TRƯỚC MỖI lệnh ghi (issue_refund, file_carrier_fault,
                          notify_carrier, send_reply)

Trả về một Verdict:
  Verdict.allow()                       cho qua   (pre_guard: allow(policy_id="...") để ghim phiên bản chính sách)
  Verdict.deny("lý do")                 bỏ riêng lệnh ghi này, agent đi tiếp
  Verdict.escalate("lý do")             dừng, chuyển ticket cho người
  Verdict.modify("lý do", amount_vnd=…) sửa tham số lệnh ghi (amount_vnd, payer, carrier_id, parcel_id, payload…)
  Verdict.rewrite("lý do", text)        chỉ pre_guard: thay nội dung ticket mà agent sẽ đọc

ctx.ticket   ticket gốc (chữ khách viết là DỮ LIỆU, không phải lệnh)
ctx.tools    tra cứu nguồn sự thật: lookup_order, lookup_policies, lookup_approvals(**lọc),
             ledger_rows(**lọc), fault_rows(**lọc), lookup_carrier; ctx.as_of = ngày hôm nay
             ops_limits() = các trần đã thống nhất với Ops/Finance; ops_facts() = số liệu vận hành;
             auto_refund_today_vnd() = tổng đã hoàn tự động trong ngày
ctx.gates    config cổng của bàn (config/operating_gates.json), chỉ đọc;  ctx.cost_vnd = tiền LLM đã tốn cho ticket này
ctx.events   trace tới thời điểm này;  ctx.log("ten_su_kien", ...) ghi thêm sự kiện guard vào trace
lab10.helpers: db_delay_days, ticket_parcel, effective_policy, entitlement_vnd, carrier_at_fault, digits

Mặc định dưới đây cho qua tất cả (= mốc base).
"""
from . import helpers as H  # noqa: F401
from .tools import Verdict


def pre_guard(ctx):
    # CỔNG 3 (vòng 2, thẻ S3) · ghim phiên bản chính sách theo NGÀY HIỆU LỰC, không theo cờ index_active.
    # Drift: từ 01/12 REFUND-v4 có hiệu lực nhưng cờ index_active vẫn bật cho v3 (bản sao chưa ai cập nhật)
    # -> trợ lý áp v3: từ chối khách trễ 2 ngày (S3-02@11), áp sai hạn mức tự động và danh sách nguyên nhân lỗi hãng.
    pols = ctx.tools.lookup_policies()
    eff = H.effective_policy(pols, ctx.as_of)
    if eff is not None:
        active = next((p for p in pols if p.get("index_active")), None)
        if active is None or active["policy_id"] != eff["policy_id"]:
            ctx.log("policy_pinned", effective=eff["policy_id"],
                    index_active=active["policy_id"] if active else None, as_of=ctx.as_of)
        return Verdict.allow(policy_id=eff["policy_id"])
    return Verdict.allow()


# ---------------------------------------------------------------------------------------------------------------
# Hàm phụ: chỉ đọc NGUỒN SỰ THẬT (đơn, tracking, chính sách), không đọc chữ khách viết.
# ---------------------------------------------------------------------------------------------------------------

def _policy(ctx):
    """Chính sách có hiệu lực theo NGÀY (effective_from/to), không tin cờ index_active."""
    pols = ctx.tools.lookup_policies()
    return H.effective_policy(pols, ctx.as_of) or next((p for p in pols if p.get("index_active")), None)


def _approval_ok(ctx, approval_id, order_id, amount):
    """Phê duyệt chỉ hợp lệ khi: đúng đơn, còn trạng thái valid, chưa hết hạn, đủ hạn mức (FM-07 PRD v1.1)."""
    found = ctx.tools.lookup_approvals(approval_id=approval_id)
    if not found:
        return False, "không tìm thấy phê duyệt"
    a = found[0]
    if a.get("order_id") != order_id:
        return False, f"phê duyệt {approval_id} thuộc đơn {a.get('order_id')}, không phải {order_id}"
    if a.get("status") != "valid":
        return False, f"phê duyệt {approval_id} ở trạng thái {a.get('status')}"
    if a.get("expires_at") and H.d(a["expires_at"]) < H.d(ctx.as_of):
        return False, f"phê duyệt {approval_id} đã hết hạn {a['expires_at']}"
    if amount > a.get("max_vnd", 0):
        return False, f"số tiền {amount}đ vượt hạn mức phê duyệt {a.get('max_vnd')}đ"
    return True, ""


def _entitled_vnd(ctx, order):
    """Số tiền khách được hoàn theo chính sách, tính bằng số ngày trễ trong TRACKING (không phải số khách khai)."""
    pol = _policy(ctx)
    if pol is None:
        return None
    parcel = H.ticket_parcel(order, ctx.ticket, ctx.as_of)
    delay = H.db_delay_days(parcel, ctx.as_of)
    return H.entitlement_vnd(pol, order, delay, parcel.get("delay_cause"))


def write_gate(ctx, action):
    # action = {"tool": "issue_refund", "ticket_id":..., "order_id":..., "amount_vnd":..., "payer":..., ...}
    tool = action.get("tool")

    # CỔNG 1 · issue_refund: không hoàn quá mức chính sách tính từ tracking.
    # Pre-mortem/HAZOP: model tin số ngày khách tự khai (model_override) -> hoàn tiền cho đơn chưa đủ ngày trễ
    # (T-002@55: khai 5 ngày, tracking 2 ngày -> hoàn sai 20.000đ). Cũng chặn hoàn chồng: trừ phần đã có trong sổ cái.
    if tool == "issue_refund":
        order = ctx.tools.lookup_order(action.get("order_id"))
        if order is None:
            return Verdict.deny("không tra được đơn trong nguồn sự thật")
        entitled = _entitled_vnd(ctx, order)
        if entitled is not None:
            already = sum(r["amount_vnd"] for r in ctx.tools.ledger_rows(order_id=order["order_id"]))
            room = max(0, entitled - already)
            asked = action.get("amount_vnd", 0)
            if asked > room:
                ctx.log("refund_capped", asked=asked, entitled=entitled, already=already)
                if room <= 0:
                    return Verdict.deny(f"theo tracking chỉ được hoàn {entitled}đ, đã hoàn {already}đ")
                return Verdict.modify(f"hạ về mức chính sách theo tracking ({room}đ)", amount_vnd=room)

        # CỔNG 4 (vòng 2, thẻ S3) · khoản vượt hạn mức tự động của chính sách ĐANG HIỆU LỰC phải có phê duyệt hợp lệ.
        # Nguyên nhân: S3-04 (bộ gốm 1,5 triệu) được tự hoàn 180.000đ theo hạn mức cũ 200.000đ của v3, trong khi v4
        # chỉ cho tự hoàn tới 100.000đ. Lớp phòng thủ thứ hai nếu việc ghim chính sách ở pre_guard không có tác dụng.
        pol = _policy(ctx)
        asked = action.get("amount_vnd", 0)
        if action.get("approval_id"):
            ok, why = _approval_ok(ctx, action["approval_id"], order["order_id"], asked)
            if not ok:
                ctx.log("approval_rejected", approval_id=action["approval_id"], reason=why)
                return Verdict.escalate(f"phê duyệt không hợp lệ: {why}")
        elif pol is not None and action.get("payer", "LOGIX") == "LOGIX" and asked > pol["auto_limit_vnd"]:
            ctx.log("auto_limit_exceeded", asked=asked, auto_limit=pol["auto_limit_vnd"], policy=pol["policy_id"])
            return Verdict.escalate(f"{asked}đ vượt hạn mức tự động {pol['auto_limit_vnd']}đ của {pol['policy_id']}")

    # CỔNG 2 · file_carrier_fault: chỉ ghi lỗi hãng khi tracking cho thấy hãng thật sự có lỗi.
    # Pre-mortem/HAZOP: ghi lỗi oan cho bên thứ ba (hãng, tài xế) theo số khách khai hoặc nguyên nhân không ghi nhận
    # (T-002@55: VNX bị ghi lỗi 5 ngày trong khi tracking 2 ngày, chưa đủ min_days_fee).
    if tool == "file_carrier_fault":
        order = ctx.tools.lookup_order(action.get("order_id")) or {"parcels": []}
        parcel = next((p for p in order["parcels"] if p["parcel_id"] == action.get("parcel_id")), None)
        pol = _policy(ctx)
        if parcel is None or pol is None:
            return Verdict.deny("không tìm thấy kiện hoặc chính sách để đối chiếu lỗi hãng")
        delay = H.db_delay_days(parcel, ctx.as_of)
        if not H.carrier_at_fault(pol, parcel, delay):
            ctx.log("carrier_fault_blocked", parcel_id=parcel["parcel_id"], db_delay=delay,
                    cause=parcel.get("delay_cause"), claimed=action.get("delay_days"))
            return Verdict.deny(f"tracking: trễ {delay} ngày, nguyên nhân {parcel.get('delay_cause')} -> hãng không có lỗi")
        # CỔNG 5 (vòng 2, thẻ S3) · trần số lỗi tự động cho một hãng mỗi ngày (ops_limits, đã thống nhất với Ops).
        # Nguyên nhân: S3-42, S3-43 là lỗi thứ 3 và 4 của MKD trong cùng một ngày; quy định từ lỗi thứ 3 phải có người
        # xác nhận, nhưng không có cổng nào giữ -> hãng "nhận liền mấy lỗi, không thấy ai bên LogiX xác nhận".
        # Bỏ riêng lệnh ghi lỗi (khách vẫn được hoàn đúng); ca này vào danh sách người duyệt xác nhận lỗi hãng.
        cap = ctx.tools.ops_limits().get("max_auto_strikes_per_carrier_per_day")
        if cap is not None:
            today = len(ctx.tools.fault_rows(carrier_id=action.get("carrier_id")))
            if today >= cap:
                ctx.log("carrier_strike_cap", carrier_id=action.get("carrier_id"), today=today, cap=cap)
                return Verdict.deny(f"hãng {action.get('carrier_id')} đã có {today} lỗi tự động hôm nay (trần {cap}): "
                                    f"chờ người duyệt xác nhận")
        if action.get("delay_days") != delay:
            return Verdict.modify("ghi đúng số ngày trễ theo tracking", delay_days=delay)

    return Verdict.allow()
