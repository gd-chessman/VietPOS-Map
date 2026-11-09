# POS và đơn hàng

**Mô tả:** Quầy bán, giỏ hàng, thanh toán, ca làm việc, hủy đơn.

**Về trang chủ Map:** [README.md](../../README.md) · [Hướng dẫn đọc](../../huong-dan-doc/)

Luồng doanh thu chính — từ màn POS đến bảng `orders`.

## 1. Luồng nghiệp vụ (đọc trước)

- [02-pos-ban-hang](../../nghiep-vu/02-pos-ban-hang/) — Luồng POS: ca làm việc, giỏ hàng, thanh toán, in bill, hủy đơn và audit.

## 2. Màn hình (giao diện)

- [ban-hang-pos](../../trang/ban-hang-pos/) — Màn bán hàng: giỏ, thanh toán, in bill, checkout offline. (URL /pos, POS, ~1988 dòng).
- [don-hang](../../trang/don-hang/) — Danh sách đơn, hủy/duyệt hủy, in lại. (URL /orders, Orders, ~22 dòng).

## 3. Module API

- [don-hang-api](../../module-api/don-hang-api/) — Module API orders.ts — 21 endpoint. Đơn hàng POS: tạo, hủy, duyệt hủy, in lại, thông báo reprint. G…
- [ca-lam-viec](../../module-api/ca-lam-viec/) — Module API shift-sessions.ts — 3 endpoint. Ca làm việc mở/đóng.
- [audit-gio-hang-pos](../../module-api/audit-gio-hang-pos/) — Module API pos-cart-audit.ts — 3 endpoint. Audit thao tác giỏ hàng POS.

## 4. Bảng dữ liệu (schema)

- [don-hang-db](../../co-so-du-lieu/don-hang-db/) — Drizzle orders.ts — 1 bảng, 39 cột, 2 enum, 4 index (orders).
- [chi-tiet-don-hang](../../co-so-du-lieu/chi-tiet-don-hang/) — Drizzle orderItems.ts — 1 bảng, 13 cột, 3 index (order_items).
- [ca-lam-viec-db](../../co-so-du-lieu/ca-lam-viec-db/) — Drizzle shiftSessions.ts — 2 bảng, 7 cột, 1 index (shift_sessions, shift_session_staff).

## 5. Thư viện backend (một số file quan trọng)

Tra cứu đủ: [README.md](../../chi-muc/thu-vien-backend/)

- [manager-order-cancel-window](../../thu-vien/manager-order-cancel-window/) — [POS & đơn hàng] manager-order-cancel-window.ts — MANAGER_ORDER_CANCEL_WINDOW_DAYS, MANAG…
- [order-audit](../../thu-vien/order-audit/) — [POS & đơn hàng] order-audit.ts — mapAuditLogRow, insertOrderAuditLog, listOrderAuditLogs.
- [order-direct-cancel](../../thu-vien/order-direct-cancel/) — [POS & đơn hàng] order-direct-cancel.ts — directCancelWithoutRequestSql, sumDirectCancell…
- [order-discount](../../thu-vien/order-discount/) — [POS & đơn hàng] order-discount.ts — computeOrderDiscountAmount, fetchDashboardChartOrder…
- [order-fraud](../../thu-vien/order-fraud/) — [POS & đơn hàng] order-fraud.ts — isOrderSyncSuspicious.
- [order-invoice-code](../../thu-vien/order-invoice-code/) — [POS & đơn hàng] order-invoice-code.ts — normalizeShopCode, formatOrderInvoiceCode, unpad…
- [order-invoice-list-filters](../../thu-vien/order-invoice-list-filters/) — [POS & đơn hàng] order-invoice-list-filters.ts — invoiceListFilters.
- [order-list-period-summary](../../thu-vien/order-list-period-summary/) — [POS & đơn hàng] order-list-period-summary.ts — appendOrderListDateFilters, fetchOrderLis…
- [order-preprint](../../thu-vien/order-preprint/) — [POS & đơn hàng] order-preprint.ts — newInvoicePublicToken, upsertOrderPreprintReservatio…
- [order-shop-sequence](../../thu-vien/order-shop-sequence/) — [POS & đơn hàng] order-shop-sequence.ts — allocateShopOrderSequence, resolveShopOrderSequ…
- [payment-revenue](../../thu-vien/payment-revenue/) — [POS & đơn hàng] payment-revenue.ts — emptyPaymentRevenue, addOrderPaymentRevenue, sumOrd…
- [shift-sessions](../../thu-vien/shift-sessions/) — [POS & đơn hàng] shift-sessions.ts — getActiveShiftSession, isShiftSessionRestrictedRole,…
- [vn-order-period](../../thu-vien/vn-order-period/) — [POS & đơn hàng] vn-order-period.ts — VN_YMD_RE, vnYmdStartInstant, vnYmdEndInclusiveInst…

---

*Sinh tự động — `python3 docs/gen.py`*
