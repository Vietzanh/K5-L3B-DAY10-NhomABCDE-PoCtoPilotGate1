"""★ FILE ĐỘI SỬA (2/3): chỉ số theo dõi (monitor). Thêm ÍT NHẤT MỘT chỉ số bắt được sự cố của bàn.

Mỗi monitor nhận danh sách trial (KHÔNG có nhãn đúng/sai, giống production) và trả về một số.
Một trial = {"ticket_id", "seed", "day", "status", "amount_vnd", "ticket", "events", "ledger", "faults", "outbound",
             "arrive_min", "warehouse", "cost_vnd", "review_kind", "queue_wait_min", "queue_stuck"}
  "day"            một ngày vận hành giả lập: các ticket cùng "day" và cùng "seed" chạy nối nhau trên cùng một sổ cái
  "arrive_min"     phút ticket tới trong ca (0..480)          "warehouse"   kho của đơn
  "cost_vnd"       tiền LLM + nền tảng đã tốn cho ticket      "review_kind" None / "escalated" (trợ lý chuyển người) /
  "queue_wait_min" số phút chờ người duyệt (None nếu không vào hàng chờ)     "recheck" (nhân viên tự kiểm lại)
Chỉ số có thể là kỹ thuật (tỉ lệ model đè số trong ticket lên DB), vận hành (số ca cần người trong giờ đông nhất),
hay kinh doanh (tỉ lệ ticket trợ lý đọc xong vẫn phải chuyển người).

lab10.grade kiểm: monitor chạy không lỗi, và giá trị trên gói sự cố khác giá trị trên bộ nền,
tức là monitor "sáng đèn" khi sự cố xảy ra.
"""


def escalation_rate(trials):
    return sum(t["status"] == "escalated" for t in trials) / max(1, len(trials))


def _guard_events(trial, kind):
    return [ev for ev in (trial.get("events") or []) if ev.get("type") == "guard" and ev.get("kind") == kind]


def policy_pin_rate(trials):
    """Tỉ lệ ticket mà cổng phải ghim lại chính sách theo ngày hiệu lực vì cờ index_active trỏ sai bản (dấu hiệu concept drift)."""
    return sum(bool(_guard_events(t, "policy_pinned")) for t in trials) / max(1, len(trials))


def carrier_strike_cap_hits(trials):
    """Số lần trần lỗi hãng tự động mỗi ngày bị chạm (hãng sắp bị ghi lỗi hàng loạt), tính trung bình trên mỗi ticket."""
    return sum(len(_guard_events(t, "carrier_strike_cap")) for t in trials) / max(1, len(trials))


MONITORS = {
    "escalation_rate": escalation_rate,     # có sẵn; KHÔNG tính là metric mới của đội
    "policy_pin_rate": policy_pin_rate,     # concept drift: cờ index_active sai bản chính sách
    "carrier_strike_cap_hits": carrier_strike_cap_hits,   # hãng chạm trần lỗi tự động/ngày
}
STARTER_MONITORS = ("escalation_rate",)
