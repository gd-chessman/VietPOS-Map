# Schema: `deviceLoginEvents`

**Mô tả:** Drizzle schema deviceLoginEvents.ts — 8 cột trên 1 bảng Postgres (device_login_events).

**Source Shop:** `lib/db/src/schema/deviceLoginEvents.ts`

## Bảng Postgres

- `device_login_events`

## Cột (trích từ schema TS)

- `id` (id)
- `shop_id` (shopId)
- `device_id` (deviceId)
- `user_id` (userId)
- `method` (method)
- `ip` (ip)
- `user_agent` (userAgent)
- `created_at` (createdAt)

## Tham chiếu (references → bảng Drizzle)

- `shopsTable`
- `usersTable`

Tổng quan quan hệ: `reference/database.md`.
