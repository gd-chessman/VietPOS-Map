# Schema: `products`

**Mô tả:** Drizzle products.ts — 1 bảng, 21 cột, 1 enum, 4 index (products).

**Mã nguồn Shop:** `lib/db/src/schema/products.ts`

## Cách đọc trang này

Mỗi **bảng Postgres** có bảng cột: kiểu Drizzle, `NOT NULL` / **PK**, khóa ngoại (cột FK → tên bảng đích), và ghi chú JSDoc từ mã nguồn. Enum và index được liệt kê riêng khi có trong file.

## Liên kết nhanh

- **HTTP API:** [san-pham-api](../../module-api/san-pham-api/) (`routes/products.ts`)
- **Giao diện:** [san-pham](../../trang/san-pham/)

## Enum Postgres

### `product_status` (`productStatusEnum`)

- Giá trị: `["active", "discontinued"]`

## Bảng `products`

- **Biến Drizzle:** `productsTable`

| Cột SQL | Thuộc tính TS | Kiểu | Ràng buộc | FK → bảng | Ghi chú |
|---------|---------------|------|-----------|-----------|---------|
| `id` | `id` | serial | **PK** | — | — |
| `internal_code` | `internalCode` | text | — | — | — |
| `internal_name` | `internalName` | text | — | — | — |
| `english_name` | `englishName` | text | — | — | — |
| `vat_name` | `vatName` | text | — | — | — |
| `unit` | `unit` | text | NOT NULL, default `Cái` | — | — |
| `vat_rate` | `vatRate` | numeric("vat_rate", { precision: 5, scale: 2 }) | NOT NULL, default `1` | — | — |
| `tncn_rate` | `tncnRate` | numeric("tncn_rate", { precision: 5, scale: 2 }) | NOT NULL, default `0.5` | — | — |
| `material` | `material` | text | — | — | — |
| `dimensions` | `dimensions` | text | — | — | — |
| `weight` | `weight` | text | — | — | — |
| `manufacturer` | `manufacturer` | text | — | — | — |
| `supplier_id` | `supplierId` | integer | — | `suppliers` | — |
| `category` | `category` | text | — | — | — |
| `category_id` | `categoryId` | integer | — | `product_categories` | — |
| `name` | `name` | text | NOT NULL | — | — |
| `price` | `price` | numeric("price", { precision: 12, scale: 2 }) | NOT NULL | — | — |
| `cost_price` | `costPrice` | numeric("cost_price", { precision: 12, scale: 2 }) | NOT NULL | — | — |
| `shop_id` | `shopId` | integer | NOT NULL | `shops` | — |
| `status` | `status` | enum `product_status` | NOT NULL, default `active` | — | — |
| `thumbnail_url` | `thumbnailUrl` | text | — | — | — |

**Index:**

- `products_shop_internal_code_uidx` on `shopId`, `internalCode`
- `products_shop_supplier_vat_name_uidx` on `shopId`, `supplierId`, `vatName`
- `products_shop_supplier_idx` on `shopId`, `supplierId`
- `products_shop_category_idx` on `shopId`, `categoryId`

## Kiểu & Zod (insert)

- `insertProductSchema` — `createInsertSchema` (xem file TS)
- `export type InsertProduct`
- `export type Product`

Tổng quan ER / naming: [../../tham-chieu/co-so-du-lieu-goc/](../../tham-chieu/co-so-du-lieu-goc/).
