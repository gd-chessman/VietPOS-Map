# Schema: `orderItems`

**Mô tả:** Drizzle orderItems.ts — 1 bảng, 13 cột, 3 index (order_items).

**Mã nguồn Shop:** `lib/db/src/schema/orderItems.ts`

## Cách đọc trang này

Mỗi **bảng Postgres** có bảng cột: kiểu Drizzle, `NOT NULL` / **PK**, khóa ngoại (cột FK → tên bảng đích), và ghi chú JSDoc từ mã nguồn. Enum và index được liệt kê riêng khi có trong file.

## Bảng `order_items`

- **Biến Drizzle:** `orderItemsTable`

| Cột SQL | Thuộc tính TS | Kiểu | Ràng buộc | FK → bảng | Ghi chú |
|---------|---------------|------|-----------|-----------|---------|
| `id` | `id` | serial | **PK** | — | — |
| `order_id` | `orderId` | integer | NOT NULL | `orders` | — |
| `product_id` | `productId` | integer | NOT NULL | `products` | — |
| `variant_id` | `variantId` | integer | — | `product_variants` | — |
| `quantity` | `quantity` | integer | NOT NULL | — | — |
| `price` | `price` | numeric("price", { precision: 12, scale: 2 }) | NOT NULL | — | — |
| `original_price` | `originalPrice` | numeric("original_price", { precision: 12, scale: 2 }) | — | — | — |
| `product_name_snapshot` | `productNameSnapshot` | text | — | — | — |
| `internal_code_snapshot` | `internalCodeSnapshot` | text | — | — | — |
| `vat_name_snapshot` | `vatNameSnapshot` | text | — | — | — |
| `unit_snapshot` | `unitSnapshot` | text | — | — | — |
| `vat_rate_snapshot` | `vatRateSnapshot` | numeric("vat_rate_snapshot", { precision: 5, scale: 2 }) | — | — | — |
| `note` | `note` | text | — | — | — |

**Index:**

- `order_items_order_id_idx` on `orderId`
- `order_items_product_id_idx` on `productId`
- `order_items_variant_id_idx` on `variantId`

## Kiểu & Zod (insert)

- `insertOrderItemSchema` — `createInsertSchema` (xem file TS)
- `export type InsertOrderItem`
- `export type OrderItem`

Tổng quan ER / naming: [../../tham-chieu/co-so-du-lieu-goc/](../../tham-chieu/co-so-du-lieu-goc/).
