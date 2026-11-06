# Schema: `productAuditLogs`

**Mô tả:** Drizzle productAuditLogs.ts — 1 bảng, 9 cột, 1 enum, 3 index (product_audit_logs).

**Mã nguồn Shop:** `lib/db/src/schema/productAuditLogs.ts`

## Cách đọc trang này

Mỗi **bảng Postgres** có bảng cột: kiểu Drizzle, `NOT NULL` / **PK**, khóa ngoại (cột FK → tên bảng đích), và ghi chú JSDoc từ mã nguồn. Enum và index được liệt kê riêng khi có trong file.

## Liên kết nhanh

- **HTTP API:** [bao-cao-audit-san-pham](../../module-api/bao-cao-audit-san-pham/) (`routes/product-audit-reports.ts`)

## Enum Postgres

### `product_audit_action` (`productAuditActionEnum`)

- Giá trị: `[
  "create",
  "update",
  "discontinue",
]`

## Bảng `product_audit_logs`

- **Biến Drizzle:** `productAuditLogsTable`

| Cột SQL | Thuộc tính TS | Kiểu | Ràng buộc | FK → bảng | Ghi chú |
|---------|---------------|------|-----------|-----------|---------|
| `id` | `id` | serial | **PK** | — | — |
| `shop_id` | `shopId` | integer | NOT NULL | `shops` | — |
| `product_id` | `productId` | integer | NOT NULL | `products` | — |
| `user_id` | `userId` | integer | NOT NULL | `users` | — |
| `action` | `action` | enum `product_audit_action` | NOT NULL | — | — |
| `product_name` | `productName` | text | NOT NULL | — | — |
| `product_internal_code` | `productInternalCode` | text | — | — | — |
| `changes` | `changes` | jsonb | NOT NULL, default `[]`, JSON typed | — | — |
| `created_at` | `createdAt` | timestamp("created_at", { withTimezone: true }) | NOT NULL, default `now()` | — | — |

**Index:**

- `product_audit_logs_shop_created_idx` on `shopId`, `createdAt`
- `product_audit_logs_shop_product_created_idx` on `shopId`, `productId`, `createdAt`
- `product_audit_logs_shop_user_created_idx` on `shopId`, `userId`, `createdAt`

## Kiểu & Zod (insert)

- `export type ProductAuditFieldChange`
- `export type ProductAuditLog`
- `export type ProductAuditLogInsert`

Tổng quan ER / naming: [../../tham-chieu/co-so-du-lieu-goc/](../../tham-chieu/co-so-du-lieu-goc/).
