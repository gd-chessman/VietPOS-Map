# Schema: `productVariants`

**Mô tả:** Drizzle schema productVariants.ts — 14 cột trên 1 bảng Postgres (product_variants).

**Mã nguồn Shop:** `lib/db/src/schema/productVariants.ts`

## Bảng Postgres

- `product_variants`

## Cột (trích từ schema TS)

- `id` (id)
- `product_id` (productId)
- `shop_id` (shopId)
- `variant_index` (variantIndex)
- `internal_code` (internalCode)
- `name` (name)
- `english_name` (englishName)
- `price` (price)
- `cost_price` (costPrice)
- `thumbnail_url` (thumbnailUrl)
- `dimensions` (dimensions)
- `weight` (weight)
- `quantity` (quantity)
- `status` (status)

## Tham chiếu (references → bảng Drizzle)

- `productsTable`
- `shopsTable`

Tổng quan quan hệ: `tham-chieu/co-so-du-lieu-goc/README.md`.
