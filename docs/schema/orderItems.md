# Schema: `orderItems`

**Mô tả:** Drizzle schema orderItems.ts — 13 cột trên 1 bảng Postgres (order_items).

**Source Shop:** `lib/db/src/schema/orderItems.ts`

## Bảng Postgres

- `order_items`

## Cột (trích từ schema TS)

- `id` (id)
- `order_id` (orderId)
- `product_id` (productId)
- `variant_id` (variantId)
- `quantity` (quantity)
- `price` (price)
- `original_price` (originalPrice)
- `product_name_snapshot` (productNameSnapshot)
- `internal_code_snapshot` (internalCodeSnapshot)
- `vat_name_snapshot` (vatNameSnapshot)
- `unit_snapshot` (unitSnapshot)
- `vat_rate_snapshot` (vatRateSnapshot)
- `note` (note)

## Tham chiếu (references → bảng Drizzle)

- `ordersTable`
- `productVariantsTable`
- `productsTable`

Tổng quan quan hệ: `reference/database.md`.
