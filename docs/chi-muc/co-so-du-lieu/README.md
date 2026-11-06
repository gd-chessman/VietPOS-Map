# Chỉ mục cơ sở dữ liệu (Drizzle)

**Mô tả:** 43 file schema — bảng cột, quan hệ FK, index; nhóm theo nghiệp vụ.

← [Bản đồ chính](../../README.md) · [Hướng dẫn đọc](../../huong-dan-doc/)

---

Postgres + **Drizzle ORM** (`lib/db/src/schema`). Mỗi file TS có thể khai báo nhiều bảng; trang con có **bảng cột đầy đủ** (kiểu, PK/FK, index, enum, ghi chú JSDoc).

Tài liệu ER tổng thể (tiếng Anh, Shop gốc): [co-so-du-lieu-goc](../../tham-chieu/co-so-du-lieu-goc/).

### Tài khoản, shop & tổ chức

users, shops, organizations, nhân viên bán, reset PIN.

- [nguoi-dung](../../co-so-du-lieu/nguoi-dung/) — Drizzle users.ts — 1 bảng, 13 cột, 2 enum, 2 index (users).
- [cua-hang-db](../../co-so-du-lieu/cua-hang-db/) — Drizzle shops.ts — 1 bảng, 31 cột (shops).
- [to-chuc](../../co-so-du-lieu/to-chuc/) — Drizzle organizations.ts — 1 bảng, 39 cột (organizations).
- [nhan-vien-ban-db](../../co-so-du-lieu/nhan-vien-ban-db/) — Drizzle salesStaff.ts — 1 bảng, 13 cột, 1 enum, 2 index (sales_staff).
- [yeu-cau-reset-pin](../../co-so-du-lieu/yeu-cau-reset-pin/) — Drizzle pinResetRequests.ts — 1 bảng, 8 cột, 1 index (pin_reset_requests).

### An ninh truy cập

Chặn IP/thiết bị, allowlist, sự kiện đăng nhập.

- [ip-bi-chan](../../co-so-du-lieu/ip-bi-chan/) — Drizzle blockedIps.ts — 1 bảng, 5 cột, 1 index (blocked_ips).
- [thiet-bi-bi-chan](../../co-so-du-lieu/thiet-bi-bi-chan/) — Drizzle blockedDevices.ts — 1 bảng, 5 cột, 1 index (blocked_devices).
- [thiet-bi-duoc-phep](../../co-so-du-lieu/thiet-bi-duoc-phep/) — Drizzle allowedDevices.ts — 1 bảng, 8 cột (allowed_devices).
- [su-kien-dang-nhap-thiet-bi](../../co-so-du-lieu/su-kien-dang-nhap-thiet-bi/) — Drizzle deviceLoginEvents.ts — 1 bảng, 8 cột, 1 enum, 2 index (device_login_events).

### POS & đơn hàng

Đơn, dòng đơn, ca, in trước, đồng bộ offline, audit POS.

- [don-hang-db](../../co-so-du-lieu/don-hang-db/) — Drizzle orders.ts — 1 bảng, 39 cột, 2 enum, 4 index (orders).
- [chi-tiet-don-hang](../../co-so-du-lieu/chi-tiet-don-hang/) — Drizzle orderItems.ts — 1 bảng, 13 cột, 3 index (order_items).
- [ca-lam-viec-db](../../co-so-du-lieu/ca-lam-viec-db/) — Drizzle shiftSessions.ts — 2 bảng, 7 cột, 1 index (shift_sessions, shift_session_staff).
- [giu-so-in-truoc](../../co-so-du-lieu/giu-so-in-truoc/) — Drizzle orderPreprintReservations.ts — 1 bảng, 10 cột, 1 index (order_preprint_reservations).
- [khoa-dong-bo-don](../../co-so-du-lieu/khoa-dong-bo-don/) — Drizzle orderSyncKeys.ts — 1 bảng, 4 cột (order_sync_keys).
- [audit-don-hang](../../co-so-du-lieu/audit-don-hang/) — Drizzle orderAuditLogs.ts — 1 bảng, 11 cột, 2 enum, 3 index (order_audit_logs).
- [audit-gio-pos](../../co-so-du-lieu/audit-gio-pos/) — Drizzle posCartAuditLogs.ts — 1 bảng, 17 cột, 2 enum, 5 index (pos_cart_audit_logs).
- [nhat-ky-in-lai](../../co-so-du-lieu/nhat-ky-in-lai/) — Drizzle reprintLogs.ts — 1 bảng, 5 cột (reprint_logs).
- [nhat-ky-thanh-toan](../../co-so-du-lieu/nhat-ky-thanh-toan/) — Drizzle paymentChangeLogs.ts — 1 bảng, 8 cột, 1 index (payment_change_logs).
- [nhat-ky-hoa-don](../../co-so-du-lieu/nhat-ky-hoa-don/) — Drizzle invoiceChangeLogs.ts — 1 bảng, 7 cột, 1 index (invoice_change_logs).

### Sản phẩm & tồn

SP, biến thể, danh mục, tồn shop, biến động, NCC.

- [san-pham-db](../../co-so-du-lieu/san-pham-db/) — Drizzle products.ts — 1 bảng, 21 cột, 1 enum, 4 index (products).
- [bien-the-san-pham](../../co-so-du-lieu/bien-the-san-pham/) — Drizzle productVariants.ts — 1 bảng, 14 cột, 4 index (product_variants).
- [danh-muc-san-pham-db](../../co-so-du-lieu/danh-muc-san-pham-db/) — Drizzle productCategories.ts — 1 bảng, 7 cột, 1 enum, 2 index (product_categories).
- [ton-kho-db](../../co-so-du-lieu/ton-kho-db/) — Drizzle inventory.ts — 1 bảng, 6 cột, 2 index (inventory).
- [bien-dong-ton](../../co-so-du-lieu/bien-dong-ton/) — Drizzle inventoryMovements.ts — 1 bảng, 9 cột (inventory_movements).
- [ton-bien-the-shop](../../co-so-du-lieu/ton-bien-the-shop/) — Drizzle shopVariantStock.ts — 1 bảng, 5 cột, 1 index (shop_variant_stock).
- [nha-cung-cap-db](../../co-so-du-lieu/nha-cung-cap-db/) — Drizzle suppliers.ts — 1 bảng, 12 cột, 1 enum, 2 index (suppliers).
- [audit-san-pham](../../co-so-du-lieu/audit-san-pham/) — Drizzle productAuditLogs.ts — 1 bảng, 9 cột, 1 enum, 3 index (product_audit_logs).

### Kho, phiếu & đặt hàng

Kho vật lý, phiếu nhập/xuất, chuyển kho, PO.

- [kho-hang](../../co-so-du-lieu/kho-hang/) — Drizzle warehouses.ts — 1 bảng, 7 cột (warehouses).
- [phieu-yeu-cau-kho](../../co-so-du-lieu/phieu-yeu-cau-kho/) — Drizzle stockRequests.ts — 3 bảng, 32 cột (stock_requests, stock_request_logs, stock_request_items).
- [chuyen-kho](../../co-so-du-lieu/chuyen-kho/) — Drizzle stockTransfers.ts — 2 bảng, 17 cột (stock_transfers, stock_transfer_items).
- [phieu-dat-hang](../../co-so-du-lieu/phieu-dat-hang/) — Drizzle purchaseOrders.ts — 3 bảng, 32 cột, 5 index (purchase_orders, purchase_order_items, purchase_order_lo…

### Hóa đơn đầu vào & CQT

HĐ mua vào, audit, phiên GDT.

- [hoa-don-dau-vao-db](../../co-so-du-lieu/hoa-don-dau-vao-db/) — Drizzle vatInboundInvoices.ts — 1 bảng, 55 cột, 3 index (vat_inbound_invoices).
- [audit-hoa-don-dau-vao](../../co-so-du-lieu/audit-hoa-don-dau-vao/) — Drizzle vatInboundAuditLogs.ts — 1 bảng, 8 cột, 2 index (vat_inbound_audit_logs).
- [phien-thue-cqt](../../co-so-du-lieu/phien-thue-cqt/) — Drizzle orgGdtTaxSessions.ts — 1 bảng, 8 cột (org_gdt_tax_sessions).

### Thông báo, widget & nhật ký hệ thống

API key, khách qua cửa, feedback, AI chat, event log.

- [khoa-api-shop](../../co-so-du-lieu/khoa-api-shop/) — Drizzle shopApiKeys.ts — 1 bảng, 9 cột (shop_api_keys).
- [dem-khach-theo-ngay](../../co-so-du-lieu/dem-khach-theo-ngay/) — Drizzle shopDailyVisitorCounts.ts — 1 bảng, 5 cột (shop_daily_visitor_counts).
- [phan-hoi-khach-hang](../../co-so-du-lieu/phan-hoi-khach-hang/) — Drizzle customerFeedback.ts — 1 bảng, 8 cột, 2 index (customer_feedback).
- [tro-ly-ai-chat](../../co-so-du-lieu/tro-ly-ai-chat/) — Drizzle agentChat.ts — 2 bảng, 12 cột, 3 index (agent_chat_threads, agent_chat_messages).
- [cau-hinh-thong-bao-nen-tang](../../co-so-du-lieu/cau-hinh-thong-bao-nen-tang/) — Drizzle platformNotificationSettings.ts — 1 bảng, 5 cột (platform_notification_settings).
- [thong-bao-nguoi-dung](../../co-so-du-lieu/thong-bao-nguoi-dung/) — Drizzle userNotifications.ts — 1 bảng, 11 cột, 2 index (user_notifications).
- [nhat-ky-thay-doi](../../co-so-du-lieu/nhat-ky-thay-doi/) — Drizzle changeLog.ts — 1 bảng, 6 cột, 2 index (change_log).
- [nhat-ky-su-kien](../../co-so-du-lieu/nhat-ky-su-kien/) — Drizzle systemEventLogs.ts — 1 bảng, 11 cột, 4 index (system_event_logs).
- [su-kien-van-hanh-shop](../../co-so-du-lieu/su-kien-van-hanh-shop/) — Drizzle shopOperationalEvents.ts — 1 bảng, 6 cột, 1 enum, 2 index (shop_operational_events).

