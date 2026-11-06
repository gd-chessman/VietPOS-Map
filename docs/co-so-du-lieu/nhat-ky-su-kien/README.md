# Schema: `systemEventLogs`

**Mô tả:** Drizzle schema systemEventLogs.ts — 11 cột trên 1 bảng Postgres (system_event_logs).

**Mã nguồn Shop:** `lib/db/src/schema/systemEventLogs.ts`

## Bảng Postgres

- `system_event_logs`

## Cột (trích từ schema TS)

- `id` (id)
- `organization_id` (organizationId)
- `shop_id` (shopId)
- `user_id` (userId)
- `device_id` (deviceId)
- `category` (category)
- `severity` (severity)
- `code` (code)
- `message` (message)
- `detail` (detail)
- `created_at` (createdAt)

## Tham chiếu (references → bảng Drizzle)

- `organizationsTable`
- `shopsTable`
- `usersTable`

Tổng quan quan hệ: `tham-chieu/co-so-du-lieu-goc/README.md`.
