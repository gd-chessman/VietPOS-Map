# Trợ lý AI, widget, đếm khách

**Mô tả:** Agent chat, widget Android, ESP32 visitor-counts.

**Về trang chủ Map:** [README.md](../../README.md) · [Hướng dẫn đọc](../../huong-dan-doc/)

Tích hợp ngoài quầy — API key shop.

## 1. Luồng nghiệp vụ (đọc trước)

- [12-widget-va-dem-khach](../../nghiep-vu/12-widget-va-dem-khach/) — App widget Android, ESP32 visitor-counts và shop API keys.

## 2. Màn hình (giao diện)

- [tro-ly-ai](../../trang/tro-ly-ai/) — Trợ lý AI chat + panel trạng thái hệ thống (DB, cloud sync, shop online). (URL /agent-assistant, Ag…
- [kiem-audit-tro-ly](../../trang/kiem-audit-tro-ly/) — Xem lịch sử hội thoại Trợ lý AI đã lưu. (URL /agent-chat-audit, AgentChatAuditPage, ~269 dòng).

## 3. Module API

- [tro-ly-ai-api](../../module-api/tro-ly-ai-api/) — Module API agent.ts — 10 endpoint. Trợ lý AI: chat, thông tin hệ thống (DB, đồng bộ cloud, shop onl…
- [widget-quay](../../module-api/widget-quay/) — Module API widget.ts — 1 endpoint. API phục vụ app Android widget: thống kê quầy (JWT / shop contex…
- [khoa-api-cua-hang](../../module-api/khoa-api-cua-hang/) — Module API shop-api-keys.ts — 8 endpoint. API key cho widget / thiết bị (ESP32 visitor-counts). Gia…

## 4. Bảng dữ liệu (schema)

- [khoa-api-shop](../../co-so-du-lieu/khoa-api-shop/) — Drizzle schema shopApiKeys.ts — 9 cột trên 1 bảng Postgres (shop_api_keys).
- [dem-khach-theo-ngay](../../co-so-du-lieu/dem-khach-theo-ngay/) — Drizzle schema shopDailyVisitorCounts.ts — 5 cột trên 1 bảng Postgres (shop_daily_visitor_counts).
- [tro-ly-ai-chat](../../co-so-du-lieu/tro-ly-ai-chat/) — Drizzle schema agentChat.ts — 12 cột trên 2 bảng Postgres (agent_chat_threads, agent_chat_messages).

## 5. Thư viện backend (một số file quan trọng)

Tra cứu đủ: [README.md](../../chi-muc/thu-vien-backend/)

- [widget-home](../../thu-vien/widget-home/) — [Kiến trúc / dùng chung] widget-home.ts — computeDayBlockForShops, computeInbound, comput…

---

*Sinh tự động — `python3 docs/gen.py`*
