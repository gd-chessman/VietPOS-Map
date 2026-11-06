# Schema: `reprintLogs`

**Mô tả:** Drizzle reprintLogs.ts — 1 bảng, 5 cột (reprint_logs).

**Mã nguồn Shop:** `lib/db/src/schema/reprintLogs.ts`

## Cách đọc trang này

Mỗi **bảng Postgres** có bảng cột: kiểu Drizzle, `NOT NULL` / **PK**, khóa ngoại (cột FK → tên bảng đích), và ghi chú JSDoc từ mã nguồn. Enum và index được liệt kê riêng khi có trong file.

## Bảng `reprint_logs`

- **Biến Drizzle:** `reprintLogsTable`

| Cột SQL | Thuộc tính TS | Kiểu | Ràng buộc | FK → bảng | Ghi chú |
|---------|---------------|------|-----------|-----------|---------|
| `id` | `id` | serial | **PK** | — | — |
| `order_id` | `orderId` | integer | NOT NULL | `orders` | — |
| `user_id` | `userId` | integer | NOT NULL | `users` | — |
| `shop_id` | `shopId` | integer | NOT NULL | `shops` | — |
| `reprinted_at` | `reprintedAt` | timestamp("reprinted_at", { withTimezone: true }) | NOT NULL, default `now()` | — | — |

## Kiểu & Zod (insert)

- `export type ReprintLog`

Tổng quan ER / naming: [../../tham-chieu/co-so-du-lieu-goc/](../../tham-chieu/co-so-du-lieu-goc/).
