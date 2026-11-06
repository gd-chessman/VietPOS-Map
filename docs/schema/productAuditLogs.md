# Schema: `productAuditLogs`

**Mô tả:** Drizzle schema productAuditLogs.ts — 9 cột trên 1 bảng Postgres (product_audit_logs).

**Source Shop:** `lib/db/src/schema/productAuditLogs.ts`

## Bảng Postgres

- `product_audit_logs`

## Cột (trích từ schema TS)

- `id` (id)
- `shop_id` (shopId)
- `product_id` (productId)
- `user_id` (userId)
- `action` (action)
- `product_name` (productName)
- `product_internal_code` (productInternalCode)
- `changes` (changes)
- `created_at` (createdAt)

## Tham chiếu (references → bảng Drizzle)

- `productsTable`
- `shopsTable`
- `usersTable`

Tổng quan quan hệ: `reference/database.md`.
