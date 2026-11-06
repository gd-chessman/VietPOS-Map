# Offline và đồng bộ

**Mô tả:** IndexedDB, checkout offline, API sync.

**Về trang chủ Map:** [README.md](../../README.md) · [Hướng dẫn đọc](../../huong-dan-doc/)

POS ghi local trước; worker đẩy khi có mạng.

## 1. Luồng nghiệp vụ (đọc trước)

- [11-offline-va-sync-client](../../nghiep-vu/11-offline-va-sync-client/) — IndexedDB local-db, checkout offline, pull/push sync với server.

## 2. Màn hình (giao diện)

- [ban-hang-pos](../../trang/ban-hang-pos/) — Màn bán hàng: giỏ, thanh toán, in bill, checkout offline. (URL /pos, POS, ~1988 dòng).

## 3. Module API

- [dong-bo-du-lieu](../../module-api/dong-bo-du-lieu/) — Module API sync.ts — 2 endpoint. API đồng bộ client (kéo/đẩy) cho IndexedDB offline.
- [don-hang-api](../../module-api/don-hang-api/) — Module API orders.ts — 21 endpoint. Đơn hàng POS: tạo, hủy, duyệt hủy, in lại, thông báo reprint. G…

## 4. Bảng dữ liệu (schema)

- [khoa-dong-bo-don](../../co-so-du-lieu/khoa-dong-bo-don/) — Drizzle schema orderSyncKeys.ts — 4 cột trên 1 bảng Postgres (order_sync_keys).

---

*Sinh tự động — `python3 docs/gen.py`*
