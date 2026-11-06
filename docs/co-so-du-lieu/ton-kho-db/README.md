# Schema: `inventory`

**Mô tả:** Drizzle inventory.ts — 1 bảng, 6 cột, 2 index (inventory).

**Mã nguồn Shop:** `lib/db/src/schema/inventory.ts`

## Cách đọc trang này

Mỗi **bảng Postgres** có bảng cột: kiểu Drizzle, `NOT NULL` / **PK**, khóa ngoại (cột FK → tên bảng đích), và ghi chú JSDoc từ mã nguồn. Enum và index được liệt kê riêng khi có trong file.

## Liên kết nhanh

- **HTTP API:** [ton-kho-api](../../module-api/ton-kho-api/) (`routes/inventory.ts`)
- **Giao diện:** [ton-kho](../../trang/ton-kho/)

## Bảng `inventory`

- **Biến Drizzle:** `inventoryTable`

| Cột SQL | Thuộc tính TS | Kiểu | Ràng buộc | FK → bảng | Ghi chú |
|---------|---------------|------|-----------|-----------|---------|
| `id` | `id` | serial | **PK** | — | — |
| `product_id` | `productId` | integer | NOT NULL | `products` | — |
| `variant_id` | `variantId` | integer | — | `product_variants` | — |
| `warehouse_id` | `warehouseId` | integer | — | `warehouses` | — |
| `shop_id` | `shopId` | integer | — | `shops` | — |
| `quantity` | `quantity` | integer | NOT NULL, default `0` | — | — |

**Index:**

- UNIQUE `(unique)` on `productId`, `warehouseId`
- UNIQUE `(unique)` on `productId`, `shopId`

## Kiểu & Zod (insert)

- `insertInventorySchema` — `createInsertSchema` (xem file TS)
- `export type InsertInventory`
- `export type Inventory`

Tổng quan ER / naming: [../../tham-chieu/co-so-du-lieu-goc/](../../tham-chieu/co-so-du-lieu-goc/).
