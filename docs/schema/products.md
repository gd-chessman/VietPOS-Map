# Schema: `products`

**Mô tả:** Drizzle schema products.ts — 21 cột trên 1 bảng Postgres (products).

**Source Shop:** `lib/db/src/schema/products.ts`

## Bảng Postgres

- `products`

## Cột (trích từ schema TS)

- `id` (id)
- `internal_code` (internalCode)
- `internal_name` (internalName)
- `english_name` (englishName)
- `vat_name` (vatName)
- `unit` (unit)
- `vat_rate` (vatRate)
- `tncn_rate` (tncnRate)
- `material` (material)
- `dimensions` (dimensions)
- `weight` (weight)
- `manufacturer` (manufacturer)
- `supplier_id` (supplierId)
- `category` (category)
- `category_id` (categoryId)
- `name` (name)
- `price` (price)
- `cost_price` (costPrice)
- `shop_id` (shopId)
- `status` (status)
- `thumbnail_url` (thumbnailUrl)

## Tham chiếu (references → bảng Drizzle)

- `productCategoriesTable`
- `shopsTable`
- `suppliersTable`

Tổng quan quan hệ: `reference/database.md`.
