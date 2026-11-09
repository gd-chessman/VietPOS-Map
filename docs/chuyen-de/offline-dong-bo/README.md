# Offline và đồng bộ

**Mô tả:** IndexedDB, checkout offline, API sync.

**Về trang chủ Map:** [README.md](../../README.md) · [Hướng dẫn đọc](../../huong-dan-doc/)

POS ghi local trước; worker đẩy khi có mạng.

## 1. Luồng nghiệp vụ (đọc trước)

- [11-offline-va-sync-client](../../nghiep-vu/11-offline-va-sync-client/) — IndexedDB local-db, checkout offline, pull/push sync với server.

## 2. Màn hình (giao diện)

- [ban-hang-pos](../../trang/ban-hang-pos/) — Màn bán hàng: giỏ, thanh toán, in bill, checkout offline.

## 3. Module API

- [dong-bo-du-lieu](../../module-api/dong-bo-du-lieu/) — Đồng bộ offline IndexedDB ↔ server.
- [don-hang-api](../../module-api/don-hang-api/) — Đơn POS: tạo, hủy, duyệt, in lại.

## 4. Bảng dữ liệu (schema)

- [khoa-dong-bo-don](../../co-so-du-lieu/khoa-dong-bo-don/) — Drizzle orderSyncKeys.ts — 1 bảng, 4 cột (order_sync_keys).

---

*Sinh tự động — `python3 docs/gen.py`*
