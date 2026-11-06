# Schema: `orderPreprintReservations`

**Mô tả:** Drizzle schema orderPreprintReservations.ts — 10 cột trên 1 bảng Postgres (order_preprint_reservations).

**Source Shop:** `lib/db/src/schema/orderPreprintReservations.ts`

## Bảng Postgres

- `order_preprint_reservations`

## Cột (trích từ schema TS)

- `client_order_id` (clientOrderId)
- `shop_id` (shopId)
- `user_id` (userId)
- `shop_sequence` (shopSequence)
- `invoice_code` (invoiceCode)
- `invoice_public_token` (invoicePublicToken)
- `total_amount` (totalAmount)
- `client_created_at` (clientCreatedAt)
- `consumed_order_id` (consumedOrderId)
- `created_at` (createdAt)

## Tham chiếu (references → bảng Drizzle)

- `ordersTable`
- `shopsTable`
- `usersTable`

Tổng quan quan hệ: `reference/database.md`.
