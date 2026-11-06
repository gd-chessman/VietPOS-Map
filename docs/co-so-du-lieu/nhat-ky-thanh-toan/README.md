# Schema: `paymentChangeLogs`

**Mô tả:** Drizzle paymentChangeLogs.ts — 1 bảng, 8 cột, 1 index (payment_change_logs).

**Mã nguồn Shop:** `lib/db/src/schema/paymentChangeLogs.ts`

## Cách đọc trang này

Mỗi **bảng Postgres** có bảng cột: kiểu Drizzle, `NOT NULL` / **PK**, khóa ngoại (cột FK → tên bảng đích), và ghi chú JSDoc từ mã nguồn. Enum và index được liệt kê riêng khi có trong file.

## Bảng `payment_change_logs`

- **Biến Drizzle:** `paymentChangeLogsTable`

| Cột SQL | Thuộc tính TS | Kiểu | Ràng buộc | FK → bảng | Ghi chú |
|---------|---------------|------|-----------|-----------|---------|
| `id` | `id` | serial | **PK** | — | — |
| `order_id` | `orderId` | integer | NOT NULL | `orders` | — |
| `shop_id` | `shopId` | integer | NOT NULL | `shops` | — |
| `changed_by` | `changedBy` | integer | NOT NULL | `users` | — |
| `changed_at` | `changedAt` | timestamp("changed_at", { withTimezone: true }) | NOT NULL, default `now()` | — | — |
| `old_payment_method` | `oldPaymentMethod` | paymentMethodEnum | NOT NULL | — | — |
| `new_payment_method` | `newPaymentMethod` | paymentMethodEnum | NOT NULL | — | — |
| `reason` | `reason` | text | NOT NULL | — | — |

**Index:**

- `payment_change_logs_order_idx` on `orderId`, `changedAt`

## Kiểu & Zod (insert)

- `export type PaymentChangeLog`

Tổng quan ER / naming: [../../tham-chieu/co-so-du-lieu-goc/](../../tham-chieu/co-so-du-lieu-goc/).
