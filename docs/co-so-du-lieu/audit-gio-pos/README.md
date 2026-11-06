# Schema: `posCartAuditLogs`

**Mô tả:** Drizzle schema posCartAuditLogs.ts — 17 cột trên 1 bảng Postgres (pos_cart_audit_logs).

**Mã nguồn Shop:** `lib/db/src/schema/posCartAuditLogs.ts`

## Bảng Postgres

- `pos_cart_audit_logs`

## Cột (trích từ schema TS)

- `id` (id)
- `shop_id` (shopId)
- `user_id` (userId)
- `shift_session_id` (shiftSessionId)
- `order_id` (orderId)
- `session_tab_id` (sessionTabId)
- `tab_label` (tabLabel)
- `action` (action)
- `risk_level` (riskLevel)
- `product_id` (productId)
- `product_name` (productName)
- `quantity_before` (quantityBefore)
- `quantity_after` (quantityAfter)
- `amount_before` (amountBefore)
- `amount_after` (amountAfter)
- `metadata` (metadata)
- `created_at` (createdAt)

## Tham chiếu (references → bảng Drizzle)

- `ordersTable`
- `shiftSessionsTable`
- `shopsTable`
- `usersTable`

Tổng quan quan hệ: `tham-chieu/co-so-du-lieu-goc/README.md`.
