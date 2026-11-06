# Schema: `reprintLogs`

**Mô tả:** Drizzle schema reprintLogs.ts — 5 cột trên 1 bảng Postgres (reprint_logs).

**Mã nguồn Shop:** `lib/db/src/schema/reprintLogs.ts`

## Bảng Postgres

- `reprint_logs`

## Cột (trích từ schema TS)

- `id` (id)
- `order_id` (orderId)
- `user_id` (userId)
- `shop_id` (shopId)
- `reprinted_at` (reprintedAt)

## Tham chiếu (references → bảng Drizzle)

- `ordersTable`
- `shopsTable`
- `usersTable`

Tổng quan quan hệ: `tham-chieu/co-so-du-lieu-goc/README.md`.
