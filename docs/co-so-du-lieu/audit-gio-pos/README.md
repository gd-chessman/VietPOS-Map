# Schema: `posCartAuditLogs`

**Mô tả:** Drizzle posCartAuditLogs.ts — 1 bảng, 17 cột, 2 enum, 5 index (pos_cart_audit_logs).

**Mã nguồn Shop:** `lib/db/src/schema/posCartAuditLogs.ts`

## Cách đọc trang này

Mỗi **bảng Postgres** có bảng cột: kiểu Drizzle, `NOT NULL` / **PK**, khóa ngoại (cột FK → tên bảng đích), và ghi chú JSDoc từ mã nguồn. Enum và index được liệt kê riêng khi có trong file.

## Liên kết nhanh

- **HTTP API:** [audit-gio-hang-pos](../../module-api/audit-gio-hang-pos/) (`routes/pos-cart-audit.ts`)

## Enum Postgres

### `pos_cart_audit_action` (`posCartAuditActionEnum`)

- Giá trị: `[
  "session_tab_close",
  "cart_clear",
  "cart_item_remove",
  "cart_item_qty_decrease",
  "cart_price_override",
  "session_tab_add",
  "cart_checkout",
]`

### `pos_cart_audit_risk` (`posCartAuditRiskEnum`)

- Giá trị: `[
  "low",
  "medium",
  "high",
]`

## Bảng `pos_cart_audit_logs`

- **Biến Drizzle:** `posCartAuditLogsTable`

| Cột SQL | Thuộc tính TS | Kiểu | Ràng buộc | FK → bảng | Ghi chú |
|---------|---------------|------|-----------|-----------|---------|
| `id` | `id` | serial | **PK** | — | — |
| `shop_id` | `shopId` | integer | NOT NULL | `shops` | — |
| `user_id` | `userId` | integer | NOT NULL | `users` | — |
| `shift_session_id` | `shiftSessionId` | integer | — | `shift_sessions` | — |
| `order_id` | `orderId` | integer | — | `orders` | — |
| `session_tab_id` | `sessionTabId` | text | NOT NULL | — | — |
| `tab_label` | `tabLabel` | text | NOT NULL | — | — |
| `action` | `action` | enum `pos_cart_audit_action` | NOT NULL | — | — |
| `risk_level` | `riskLevel` | enum `pos_cart_audit_risk` | NOT NULL | — | — |
| `product_id` | `productId` | integer | — | — | — |
| `product_name` | `productName` | text | — | — | — |
| `quantity_before` | `quantityBefore` | integer | — | — | — |
| `quantity_after` | `quantityAfter` | integer | — | — | — |
| `amount_before` | `amountBefore` | numeric("amount_before", { precision: 12, scale: 2 }) | — | — | — |
| `amount_after` | `amountAfter` | numeric("amount_after", { precision: 12, scale: 2 }) | — | — | — |
| `metadata` | `metadata` | jsonb | JSON typed | — | — |
| `created_at` | `createdAt` | timestamp("created_at", { withTimezone: true }) | NOT NULL, default `now()` | — | — |

**Index:**

- `pos_cart_audit_logs_shop_created_idx` on `shopId`, `createdAt`
- `pos_cart_audit_logs_shop_user_created_idx` on `shopId`, `userId`, `createdAt`
- `pos_cart_audit_logs_shop_risk_created_idx` on `shopId`, `riskLevel`, `createdAt`
- `pos_cart_audit_logs_session_tab_idx` on `shopId`, `sessionTabId`
- `pos_cart_audit_logs_order_idx` on `orderId`

## Kiểu & Zod (insert)

- `export type PosCartAuditMetadata`
- `export type PosCartAuditLog`
- `export type PosCartAuditLogInsert`

Tổng quan ER / naming: [../../tham-chieu/co-so-du-lieu-goc/](../../tham-chieu/co-so-du-lieu-goc/).
