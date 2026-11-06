# Schema: `inventory`

**Mô tả:** Drizzle schema inventory.ts — 6 cột trên 1 bảng Postgres (inventory).

**Mã nguồn Shop:** `lib/db/src/schema/inventory.ts`

## Bảng Postgres

- `inventory`

## Cột (trích từ schema TS)

- `id` (id)
- `product_id` (productId)
- `variant_id` (variantId)
- `warehouse_id` (warehouseId)
- `shop_id` (shopId)
- `quantity` (quantity)

## Tham chiếu (references → bảng Drizzle)

- `productVariantsTable`
- `productsTable`
- `shopsTable`
- `warehousesTable`

Tổng quan quan hệ: `tham-chieu/co-so-du-lieu-goc/README.md`.
