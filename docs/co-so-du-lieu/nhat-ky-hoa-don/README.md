# Schema: `invoiceChangeLogs`

**Mô tả:** Drizzle schema invoiceChangeLogs.ts — 7 cột trên 1 bảng Postgres (invoice_change_logs).

**Mã nguồn Shop:** `lib/db/src/schema/invoiceChangeLogs.ts`

## Bảng Postgres

- `invoice_change_logs`

## Cột (trích từ schema TS)

- `id` (id)
- `order_id` (orderId)
- `shop_id` (shopId)
- `changed_by` (changedBy)
- `changed_at` (changedAt)
- `old_values` (oldValues)
- `new_values` (newValues)

## Tham chiếu (references → bảng Drizzle)

- `ordersTable`
- `shopsTable`
- `usersTable`

Tổng quan quan hệ: `tham-chieu/co-so-du-lieu-goc/README.md`.
