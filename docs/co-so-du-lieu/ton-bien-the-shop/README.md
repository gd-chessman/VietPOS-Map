# Schema: `shopVariantStock`

**Mô tả:** Drizzle shopVariantStock.ts — 1 bảng, 5 cột, 1 index (shop_variant_stock).

**Mã nguồn Shop:** `lib/db/src/schema/shopVariantStock.ts`

## Cách đọc trang này

Mỗi **bảng Postgres** có bảng cột: kiểu Drizzle, `NOT NULL` / **PK**, khóa ngoại (cột FK → tên bảng đích), và ghi chú JSDoc từ mã nguồn. Enum và index được liệt kê riêng khi có trong file.

## Liên kết nhanh

- **HTTP API:** [ton-kho-api](../../module-api/ton-kho-api/) (`routes/inventory.ts`)

## Bảng `shop_variant_stock`

*Tồn biến thể thêm (index > 0) theo từng chi nhánh. Biến thể 0 vẫn dùng `inventory` (productId, shopId).*

- **Biến Drizzle:** `shopVariantStockTable`

| Cột SQL | Thuộc tính TS | Kiểu | Ràng buộc | FK → bảng | Ghi chú |
|---------|---------------|------|-----------|-----------|---------|
| `id` | `id` | serial | **PK** | — | — |
| `shop_id` | `shopId` | integer | NOT NULL | `shops` | — |
| `product_id` | `productId` | integer | NOT NULL | `products` | — |
| `variant_id` | `variantId` | integer | NOT NULL | `product_variants` | — |
| `quantity` | `quantity` | integer | NOT NULL, default `0` | — | — |

**Index:**

- UNIQUE `(unique)` on `shopId`, `variantId`

## Kiểu & Zod (insert)

- `insertShopVariantStockSchema` — `createInsertSchema` (xem file TS)
- `export type InsertShopVariantStock`
- `export type ShopVariantStock`

Tổng quan ER / naming: [../../tham-chieu/co-so-du-lieu-goc/](../../tham-chieu/co-so-du-lieu-goc/).
