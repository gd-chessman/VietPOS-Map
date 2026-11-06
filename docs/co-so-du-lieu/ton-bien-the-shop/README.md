# Schema: `shopVariantStock`

**Mô tả:** Drizzle schema shopVariantStock.ts — 5 cột trên 1 bảng Postgres (shop_variant_stock).

**Mã nguồn Shop:** `lib/db/src/schema/shopVariantStock.ts`

## Bảng Postgres

- `shop_variant_stock`

## Cột (trích từ schema TS)

- `id` (id)
- `shop_id` (shopId)
- `product_id` (productId)
- `variant_id` (variantId)
- `quantity` (quantity)

## Tham chiếu (references → bảng Drizzle)

- `productVariantsTable`
- `productsTable`
- `shopsTable`

Tổng quan quan hệ: `tham-chieu/co-so-du-lieu-goc/README.md`.
