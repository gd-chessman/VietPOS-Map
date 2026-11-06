# Schema: `orderSyncKeys`

**Mô tả:** Drizzle orderSyncKeys.ts — 1 bảng, 4 cột (order_sync_keys).

**Mã nguồn Shop:** `lib/db/src/schema/orderSyncKeys.ts`

## Cách đọc trang này

Mỗi **bảng Postgres** có bảng cột: kiểu Drizzle, `NOT NULL` / **PK**, khóa ngoại (cột FK → tên bảng đích), và ghi chú JSDoc từ mã nguồn. Enum và index được liệt kê riêng khi có trong file.

## Liên kết nhanh

- **HTTP API:** [dong-bo-du-lieu](../../module-api/dong-bo-du-lieu/) (`routes/sync.ts`)

## Bảng `order_sync_keys`

*Maps client-generated order IDs to server orders for offline sync idempotency.*

- **Biến Drizzle:** `orderSyncKeysTable`

| Cột SQL | Thuộc tính TS | Kiểu | Ràng buộc | FK → bảng | Ghi chú |
|---------|---------------|------|-----------|-----------|---------|
| `client_order_id` | `clientOrderId` | text | **PK** | — | — |
| `order_id` | `orderId` | integer | NOT NULL | `orders` | — |
| `shop_id` | `shopId` | integer | NOT NULL | `shops` | — |
| `created_at` | `createdAt` | timestamp("created_at", { withTimezone: true }) | NOT NULL, default `now()` | — | — |

## Kiểu & Zod (insert)

- `export type OrderSyncKey`

Tổng quan ER / naming: [../../tham-chieu/co-so-du-lieu-goc/](../../tham-chieu/co-so-du-lieu-goc/).
