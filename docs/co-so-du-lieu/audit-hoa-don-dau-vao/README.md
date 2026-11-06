# Schema: `vatInboundAuditLogs`

**Mô tả:** Drizzle schema vatInboundAuditLogs.ts — 8 cột trên 1 bảng Postgres (vat_inbound_audit_logs).

**Mã nguồn Shop:** `lib/db/src/schema/vatInboundAuditLogs.ts`

## Bảng Postgres

- `vat_inbound_audit_logs`

## Cột (trích từ schema TS)

- `id` (id)
- `invoice_id` (invoiceId)
- `shop_id` (shopId)
- `user_id` (userId)
- `action` (action)
- `note` (note)
- `metadata` (metadata)
- `created_at` (createdAt)

## Tham chiếu (references → bảng Drizzle)

- `shopsTable`
- `usersTable`
- `vatInboundInvoicesTable`

Tổng quan quan hệ: `tham-chieu/co-so-du-lieu-goc/README.md`.
