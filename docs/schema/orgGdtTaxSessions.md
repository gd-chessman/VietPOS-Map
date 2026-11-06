# Schema: `orgGdtTaxSessions`

**Mô tả:** Drizzle schema orgGdtTaxSessions.ts — 8 cột trên 1 bảng Postgres (org_gdt_tax_sessions).

**Source Shop:** `lib/db/src/schema/orgGdtTaxSessions.ts`

## Bảng Postgres

- `org_gdt_tax_sessions`

## Cột (trích từ schema TS)

- `id` (id)
- `organization_id` (organizationId)
- `gdt_access_token_enc` (gdtAccessTokenEnc)
- `gdt_token_expires_at` (gdtTokenExpiresAt)
- `connected_at` (connectedAt)
- `last_test_at` (lastTestAt)
- `last_test_ok` (lastTestOk)
- `updated_at` (updatedAt)

## Tham chiếu (references → bảng Drizzle)

- `organizationsTable`

Tổng quan quan hệ: `reference/database.md`.
