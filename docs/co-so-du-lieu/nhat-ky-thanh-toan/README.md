# Schema: `paymentChangeLogs`

**Mô tả:** Drizzle schema paymentChangeLogs.ts — 8 cột trên 1 bảng Postgres (payment_change_logs).

**Mã nguồn Shop:** `lib/db/src/schema/paymentChangeLogs.ts`

## Bảng Postgres

- `payment_change_logs`

## Cột (trích từ schema TS)

- `id` (id)
- `order_id` (orderId)
- `shop_id` (shopId)
- `changed_by` (changedBy)
- `changed_at` (changedAt)
- `old_payment_method` (oldPaymentMethod)
- `new_payment_method` (newPaymentMethod)
- `reason` (reason)

## Tham chiếu (references → bảng Drizzle)

- `ordersTable`
- `shopsTable`
- `usersTable`

Tổng quan quan hệ: `tham-chieu/co-so-du-lieu-goc/README.md`.
