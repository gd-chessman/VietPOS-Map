# Schema: `allowedDevices`

**Mô tả:** Drizzle schema allowedDevices.ts — 8 cột trên 1 bảng Postgres (allowed_devices).

**Source Shop:** `lib/db/src/schema/allowedDevices.ts`

## Bảng Postgres

- `allowed_devices`

## Cột (trích từ schema TS)

- `id` (id)
- `shop_id` (shopId)
- `device_id` (deviceId)
- `device_name` (deviceName)
- `identifier_name` (identifierName)
- `status` (status)
- `created_at` (createdAt)
- `approved_by` (approvedBy)

## Tham chiếu (references → bảng Drizzle)

- `shopsTable`
- `usersTable`

Tổng quan quan hệ: `reference/database.md`.
