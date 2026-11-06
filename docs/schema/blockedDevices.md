# Schema: `blockedDevices`

**Mô tả:** Drizzle schema blockedDevices.ts — 5 cột trên 1 bảng Postgres (blocked_devices).

**Source Shop:** `lib/db/src/schema/blockedDevices.ts`

## Bảng Postgres

- `blocked_devices`

## Cột (trích từ schema TS)

- `id` (id)
- `device_id` (deviceId)
- `note` (note)
- `created_at` (createdAt)
- `created_by` (createdBy)

## Tham chiếu (references → bảng Drizzle)

- `usersTable`

Tổng quan quan hệ: `reference/database.md`.
