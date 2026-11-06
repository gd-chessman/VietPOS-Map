# Schema: `blockedIps`

**Mô tả:** Drizzle schema blockedIps.ts — 5 cột trên 1 bảng Postgres (blocked_ips).

**Source Shop:** `lib/db/src/schema/blockedIps.ts`

## Bảng Postgres

- `blocked_ips`

## Cột (trích từ schema TS)

- `id` (id)
- `ip` (ip)
- `note` (note)
- `created_at` (createdAt)
- `created_by` (createdBy)

## Tham chiếu (references → bảng Drizzle)

- `usersTable`

Tổng quan quan hệ: `reference/database.md`.
