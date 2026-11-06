# POS — bán hàng

**Mô tả:** Luồng POS: ca làm việc, giỏ hàng, thanh toán, in bill, hủy đơn và audit.

1. Mở ca (`shift-sessions`) nếu policy bật.
2. Thêm SP vào giỏ — trừ tồn khi **complete** order (server) hoặc ghi offline.
3. Chọn PT thanh toán; optional yêu cầu xuất HĐ (buyer fields trên order).
4. In bill / reprint → `reprint_logs`, báo cáo audit.

**Hủy đơn:** NV gửi yêu cầu + note; admin duyệt → hoàn tồn.

**Tables:** `orders`, `order_items`, `inventory`, `reprint_logs`, `pos_cart_audit_logs`.

**Mirror:** `reference/business-flows.md` § POS.
