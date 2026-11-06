# Schema: `productCategories`

**Mô tả:** Drizzle productCategories.ts — 1 bảng, 7 cột, 1 enum, 2 index (product_categories).

**Mã nguồn Shop:** `lib/db/src/schema/productCategories.ts`

## Cách đọc trang này

Mỗi **bảng Postgres** có bảng cột: kiểu Drizzle, `NOT NULL` / **PK**, khóa ngoại (cột FK → tên bảng đích), và ghi chú JSDoc từ mã nguồn. Enum và index được liệt kê riêng khi có trong file.

## Liên kết nhanh

- **HTTP API:** [danh-muc-san-pham](../../module-api/danh-muc-san-pham/) (`routes/product-categories.ts`)

## Enum Postgres

### `product_category_status` (`productCategoryStatusEnum`)

- Giá trị: `["active", "inactive"]`

## Bảng `product_categories`

- **Biến Drizzle:** `productCategoriesTable`

| Cột SQL | Thuộc tính TS | Kiểu | Ràng buộc | FK → bảng | Ghi chú |
|---------|---------------|------|-----------|-----------|---------|
| `id` | `id` | serial | **PK** | — | — |
| `shop_id` | `shopId` | integer | NOT NULL | `shops` | — |
| `name` | `name` | text | NOT NULL | — | — |
| `notes` | `notes` | text | — | — | — |
| `status` | `status` | enum `product_category_status` | NOT NULL, default `active` | — | — |
| `created_at` | `createdAt` | timestamp("created_at", { withTimezone: true }) | NOT NULL, default `now()` | — | — |
| `updated_at` | `updatedAt` | timestamp("updated_at", { withTimezone: true }) | NOT NULL, default `now()` | — | — |

**Index:**

- `product_categories_shop_name_uidx` on `shopId`, `name`
- `product_categories_shop_status_idx` on `shopId`, `status`

## Kiểu & Zod (insert)

- `insertProductCategorySchema` — `createInsertSchema` (xem file TS)
- `export type InsertProductCategory`
- `export type ProductCategory`

Tổng quan ER / naming: [../../tham-chieu/co-so-du-lieu-goc/](../../tham-chieu/co-so-du-lieu-goc/).
