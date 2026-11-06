# Schema: `vatInboundAuditLogs`

**Mô tả:** Drizzle vatInboundAuditLogs.ts — 1 bảng, 8 cột, 2 index (vat_inbound_audit_logs).

**Mã nguồn Shop:** `lib/db/src/schema/vatInboundAuditLogs.ts`

## Cách đọc trang này

Mỗi **bảng Postgres** có bảng cột: kiểu Drizzle, `NOT NULL` / **PK**, khóa ngoại (cột FK → tên bảng đích), và ghi chú JSDoc từ mã nguồn. Enum và index được liệt kê riêng khi có trong file.

## Liên kết nhanh

- **HTTP API:** [hoa-don-dau-vao](../../module-api/hoa-don-dau-vao/) (`routes/vat-inbound.ts`)

## Bảng `vat_inbound_audit_logs`

- **Biến Drizzle:** `vatInboundAuditLogsTable`

| Cột SQL | Thuộc tính TS | Kiểu | Ràng buộc | FK → bảng | Ghi chú |
|---------|---------------|------|-----------|-----------|---------|
| `id` | `id` | serial | **PK** | — | — |
| `invoice_id` | `invoiceId` | integer | NOT NULL | `vat_inbound_invoices` | — |
| `shop_id` | `shopId` | integer | NOT NULL | `shops` | — |
| `user_id` | `userId` | integer | NOT NULL | `users` | — |
| `action` | `action` | text | NOT NULL, JSON typed | — | — |
| `note` | `note` | text | — | — | — |
| `metadata` | `metadata` | jsonb | JSON typed | — | — |
| `created_at` | `createdAt` | timestamp("created_at", { withTimezone: true }) | NOT NULL, default `now()` | — | — |

**Index:**

- `vat_inbound_audit_invoice_created_idx` on `invoiceId`, `createdAt`
- `vat_inbound_audit_shop_created_idx` on `shopId`, `createdAt`

## Kiểu & Zod (insert)

- `export type VatInboundAuditAction`
- `export type VatInboundAuditMetadata`
- `export type VatInboundAuditLog`
- `export type VatInboundAuditLogInsert`

Tổng quan ER / naming: [../../tham-chieu/co-so-du-lieu-goc/](../../tham-chieu/co-so-du-lieu-goc/).
