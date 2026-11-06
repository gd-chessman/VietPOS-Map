# Schema: `invoiceChangeLogs`

**Mô tả:** Drizzle invoiceChangeLogs.ts — 1 bảng, 7 cột, 1 index (invoice_change_logs).

**Mã nguồn Shop:** `lib/db/src/schema/invoiceChangeLogs.ts`

## Cách đọc trang này

Mỗi **bảng Postgres** có bảng cột: kiểu Drizzle, `NOT NULL` / **PK**, khóa ngoại (cột FK → tên bảng đích), và ghi chú JSDoc từ mã nguồn. Enum và index được liệt kê riêng khi có trong file.

## Bảng `invoice_change_logs`

- **Biến Drizzle:** `invoiceChangeLogsTable`

| Cột SQL | Thuộc tính TS | Kiểu | Ràng buộc | FK → bảng | Ghi chú |
|---------|---------------|------|-----------|-----------|---------|
| `id` | `id` | serial | **PK** | — | — |
| `order_id` | `orderId` | integer | NOT NULL | `orders` | — |
| `shop_id` | `shopId` | integer | NOT NULL | `shops` | — |
| `changed_by` | `changedBy` | integer | NOT NULL | `users` | — |
| `changed_at` | `changedAt` | timestamp("changed_at", { withTimezone: true }) | NOT NULL, default `now()` | — | — |
| `old_values` | `oldValues` | jsonb | NOT NULL, JSON typed | — | — |
| `new_values` | `newValues` | jsonb | NOT NULL, JSON typed | — | — |

**Index:**

- `invoice_change_logs_order_idx` on `orderId`, `changedAt`

## Kiểu & Zod (insert)

- `export type InvoiceSnapshot`
- `export type InvoiceChangeLog`

Tổng quan ER / naming: [../../tham-chieu/co-so-du-lieu-goc/](../../tham-chieu/co-so-du-lieu-goc/).
