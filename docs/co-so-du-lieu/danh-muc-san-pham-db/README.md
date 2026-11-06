# Schema: `productCategories`

**Mô tả:** Drizzle schema productCategories.ts — 7 cột trên 1 bảng Postgres (product_categories).

**Mã nguồn Shop:** `lib/db/src/schema/productCategories.ts`

## Bảng Postgres

- `product_categories`

## Cột (trích từ schema TS)

- `id` (id)
- `shop_id` (shopId)
- `name` (name)
- `notes` (notes)
- `status` (status)
- `created_at` (createdAt)
- `updated_at` (updatedAt)

## Tham chiếu (references → bảng Drizzle)

- `shopsTable`

Tổng quan quan hệ: `tham-chieu/co-so-du-lieu-goc/README.md`.
