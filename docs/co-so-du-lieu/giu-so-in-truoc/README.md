# Schema: `orderPreprintReservations`

**Mô tả:** Drizzle orderPreprintReservations.ts — 1 bảng, 10 cột, 1 index (order_preprint_reservations).

**Mã nguồn Shop:** `lib/db/src/schema/orderPreprintReservations.ts`

## Cách đọc trang này

Mỗi **bảng Postgres** có bảng cột: kiểu Drizzle, `NOT NULL` / **PK**, khóa ngoại (cột FK → tên bảng đích), và ghi chú JSDoc từ mã nguồn. Enum và index được liệt kê riêng khi có trong file.

## Liên kết nhanh

- **HTTP API:** [don-hang-api](../../module-api/don-hang-api/) (`routes/orders.ts`)

## Bảng `order_preprint_reservations`

*Token + số HĐ dự kiến trước POST /orders — cùng token gắn lên đơn khi sync.*

- **Biến Drizzle:** `orderPreprintReservationsTable`

| Cột SQL | Thuộc tính TS | Kiểu | Ràng buộc | FK → bảng | Ghi chú |
|---------|---------------|------|-----------|-----------|---------|
| `client_order_id` | `clientOrderId` | text | **PK** | — | — |
| `shop_id` | `shopId` | integer | NOT NULL | `shops` | — |
| `user_id` | `userId` | integer | NOT NULL | `users` | — |
| `shop_sequence` | `shopSequence` | integer | NOT NULL | — | — |
| `invoice_code` | `invoiceCode` | text | NOT NULL | — | — |
| `invoice_public_token` | `invoicePublicToken` | text | — | — | — |
| `total_amount` | `totalAmount` | numeric("total_amount", { precision: 12, scale: 2 }) | — | — | — |
| `client_created_at` | `clientCreatedAt` | timestamp("client_created_at", { withTimezone: true }) | — | — | — |
| `consumed_order_id` | `consumedOrderId` | integer | — | `orders` | — |
| `created_at` | `createdAt` | timestamp("created_at", { withTimezone: true }) | NOT NULL, default `now()` | — | — |

**Index:**

- `order_preprint_reservations_token_uidx` on `invoicePublicToken`

## Kiểu & Zod (insert)

- `export type OrderPreprintReservation`

Tổng quan ER / naming: [../../tham-chieu/co-so-du-lieu-goc/](../../tham-chieu/co-so-du-lieu-goc/).
