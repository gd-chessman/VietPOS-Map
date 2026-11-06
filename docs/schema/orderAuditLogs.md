# Schema: `orderAuditLogs`

**Mô tả:** Drizzle schema orderAuditLogs.ts — 11 cột trên 1 bảng Postgres (order_audit_logs).

**Source Shop:** `lib/db/src/schema/orderAuditLogs.ts`

## Bảng Postgres

- `order_audit_logs`

## Cột (trích từ schema TS)

- `id` (id)
- `order_id` (orderId)
- `shop_id` (shopId)
- `user_id` (userId)
- `action` (action)
- `sensitivity_level` (sensitivityLevel)
- `sensitivity_label` (sensitivityLabel)
- `cash_impact` (cashImpact)
- `note` (note)
- `metadata` (metadata)
- `created_at` (createdAt)

## Tham chiếu (references → bảng Drizzle)

- `ordersTable`
- `shopsTable`
- `usersTable`

Tổng quan quan hệ: `reference/database.md`.
