# Schema: `orderSyncKeys`

**Mô tả:** Drizzle schema orderSyncKeys.ts — 4 cột trên 1 bảng Postgres (order_sync_keys).

**Mã nguồn Shop:** `lib/db/src/schema/orderSyncKeys.ts`

## Bảng Postgres

- `order_sync_keys`

## Cột (trích từ schema TS)

- `client_order_id` (clientOrderId)
- `order_id` (orderId)
- `shop_id` (shopId)
- `created_at` (createdAt)

## Tham chiếu (references → bảng Drizzle)

- `ordersTable`
- `shopsTable`

Tổng quan quan hệ: `tham-chieu/co-so-du-lieu-goc/README.md`.
