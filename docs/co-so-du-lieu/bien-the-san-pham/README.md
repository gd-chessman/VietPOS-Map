# Schema: `productVariants`

**Mô tả:** Drizzle productVariants.ts — 1 bảng, 14 cột, 4 index (product_variants).

**Mã nguồn Shop:** `lib/db/src/schema/productVariants.ts`

## Cách đọc trang này

Mỗi **bảng Postgres** có bảng cột: kiểu Drizzle, `NOT NULL` / **PK**, khóa ngoại (cột FK → tên bảng đích), và ghi chú JSDoc từ mã nguồn. Enum và index được liệt kê riêng khi có trong file.

## Bảng `product_variants`

*Biến thể bán được của sản phẩm. `variantIndex = 0` là biến thể gốc — đồng bộ name/price/code/ảnh/tồn với hàng `products` + `inventory`.*

- **Biến Drizzle:** `productVariantsTable`

| Cột SQL | Thuộc tính TS | Kiểu | Ràng buộc | FK → bảng | Ghi chú |
|---------|---------------|------|-----------|-----------|---------|
| `id` | `id` | serial | **PK** | — | — |
| `product_id` | `productId` | integer | NOT NULL | `products` | — |
| `shop_id` | `shopId` | integer | NOT NULL | `shops` | — |
| `variant_index` | `variantIndex` | integer | NOT NULL, default `0` | — | — |
| `internal_code` | `internalCode` | text | — | — | — |
| `name` | `name` | text | NOT NULL | — | — |
| `english_name` | `englishName` | text | — | — | — |
| `price` | `price` | numeric("price", { precision: 12, scale: 2 }) | NOT NULL | — | — |
| `cost_price` | `costPrice` | numeric("cost_price", { precision: 12, scale: 2 }) | NOT NULL | — | — |
| `thumbnail_url` | `thumbnailUrl` | text | — | — | — |
| `dimensions` | `dimensions` | text | — | — | — |
| `weight` | `weight` | text | — | — | — |
| `quantity` | `quantity` | integer | NOT NULL, default `0` | — | — |
| `status` | `status` | productStatusEnum | NOT NULL, default `active` | — | — |

**Index:**

- `product_variants_product_index_uidx` on `productId`, `variantIndex`
- `product_variants_shop_code_uidx` on `shopId`, `internalCode`
- `product_variants_product_id_idx` on `productId`
- `product_variants_shop_id_idx` on `shopId`

## Kiểu & Zod (insert)

- `insertProductVariantSchema` — `createInsertSchema` (xem file TS)
- `export type InsertProductVariant`
- `export type ProductVariant`

Tổng quan ER / naming: [../../tham-chieu/co-so-du-lieu-goc/](../../tham-chieu/co-so-du-lieu-goc/).
