# Trợ lý AI, widget, đếm khách

**Mô tả:** Agent chat, widget Android, ESP32 visitor-counts.

**Về trang chủ Map:** [README.md](../../README.md) · [Hướng dẫn đọc](../../huong-dan-doc/)

Tích hợp ngoài quầy — API key shop.

## 1. Luồng nghiệp vụ (đọc trước)

- [12-widget-va-dem-khach](../../nghiep-vu/12-widget-va-dem-khach/) — App widget Android, ESP32 visitor-counts và shop API keys.

## 2. Màn hình (giao diện)

- [tro-ly-ai](../../trang/tro-ly-ai/) — Trợ lý AI chat + panel trạng thái hệ thống (DB, cloud sync, shop online).
- [kiem-audit-tro-ly](../../trang/kiem-audit-tro-ly/) — Xem lịch sử hội thoại Trợ lý AI đã lưu.

## 3. Module API

- [tro-ly-ai-api](../../module-api/tro-ly-ai-api/) — Trợ lý AI: chat và công cụ đọc dữ liệu kinh doanh.
- [widget-quay](../../module-api/widget-quay/) — API cho app widget Android.
- [khoa-api-cua-hang](../../module-api/khoa-api-cua-hang/) — API key shop (widget, ESP32).

## 4. Bảng dữ liệu (schema)

- [khoa-api-shop](../../co-so-du-lieu/khoa-api-shop/) — Drizzle shopApiKeys.ts — 1 bảng, 9 cột (shop_api_keys).
- [dem-khach-theo-ngay](../../co-so-du-lieu/dem-khach-theo-ngay/) — Drizzle shopDailyVisitorCounts.ts — 1 bảng, 5 cột (shop_daily_visitor_counts).
- [tro-ly-ai-chat](../../co-so-du-lieu/tro-ly-ai-chat/) — Drizzle agentChat.ts — 2 bảng, 12 cột, 3 index (agent_chat_threads, agent_chat_messages).

## 5. Thư viện backend (một số file quan trọng)

Tra cứu đủ: [README.md](../../chi-muc/thu-vien-backend/)

- [widget-home](../../thu-vien/widget-home/) — [Kiến trúc / dùng chung] widget-home.ts — computeDayBlockForShops, computeInbound…

---

*Sinh tự động — `python3 docs/gen.py`*
