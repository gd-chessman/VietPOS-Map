# Schema: `orderAuditLogs`

**Mô tả:** Drizzle orderAuditLogs.ts — 1 bảng, 11 cột, 2 enum, 3 index (order_audit_logs).

**Mã nguồn Shop:** `lib/db/src/schema/orderAuditLogs.ts`

## Cách đọc trang này

Mỗi **bảng Postgres** có bảng cột: kiểu Drizzle, `NOT NULL` / **PK**, khóa ngoại (cột FK → tên bảng đích), và ghi chú JSDoc từ mã nguồn. Enum và index được liệt kê riêng khi có trong file.

## Liên kết nhanh

- **HTTP API:** [bao-cao-audit-don](../../module-api/bao-cao-audit-don/) (`routes/order-audit-reports.ts`)

## Enum Postgres

### `order_audit_action` (`orderAuditActionEnum`)

- Giá trị: `[
  "payment_change",
  "cancel",
  "cancel_request",
  "cancel_approve",
  "cancel_reject",
  "uncancel",
]`

### `order_audit_sensitivity` (`orderAuditSensitivityEnum`)

- Giá trị: `[
  "none",
  "low",
  "medium",
  "high",
]`

## Bảng `order_audit_logs`

- **Biến Drizzle:** `orderAuditLogsTable`

| Cột SQL | Thuộc tính TS | Kiểu | Ràng buộc | FK → bảng | Ghi chú |
|---------|---------------|------|-----------|-----------|---------|
| `id` | `id` | serial | **PK** | — | — |
| `order_id` | `orderId` | integer | NOT NULL | `orders` | — |
| `shop_id` | `shopId` | integer | NOT NULL | `shops` | — |
| `user_id` | `userId` | integer | NOT NULL | `users` | — |
| `action` | `action` | enum `order_audit_action` | NOT NULL | — | — |
| `sensitivity_level` | `sensitivityLevel` | enum `order_audit_sensitivity` | NOT NULL, default `none` | — | — |
| `sensitivity_label` | `sensitivityLabel` | text | — | — | — |
| `cash_impact` | `cashImpact` | numeric("cash_impact", { precision: 12, scale: 2 }) | — | — | — |
| `note` | `note` | text | — | — | — |
| `metadata` | `metadata` | jsonb | JSON typed | — | — |
| `created_at` | `createdAt` | timestamp("created_at", { withTimezone: true }) | NOT NULL, default `now()` | — | — |

**Index:**

- `order_audit_logs_order_created_idx` on `orderId`, `createdAt`
- `order_audit_logs_shop_created_idx` on `shopId`, `createdAt`
- `order_audit_logs_shop_sensitivity_created_idx` on `shopId`, `sensitivityLevel`, `createdAt`

## Kiểu & Zod (insert)

- `export type OrderAuditMetadata`
- `export type OrderAuditLog`
- `export type OrderAuditLogInsert`

Tổng quan ER / naming: [../../tham-chieu/co-so-du-lieu-goc/](../../tham-chieu/co-so-du-lieu-goc/).
