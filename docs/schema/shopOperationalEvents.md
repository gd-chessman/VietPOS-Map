# Schema: `shopOperationalEvents`

**Mô tả:** Drizzle schema shopOperationalEvents.ts — 6 cột trên 1 bảng Postgres (shop_operational_events).

**Source Shop:** `lib/db/src/schema/shopOperationalEvents.ts`

## Bảng Postgres

- `shop_operational_events`

## Cột (trích từ schema TS)

- `id` (id)
- `shop_id` (shopId)
- `user_id` (userId)
- `event_type` (eventType)
- `payload` (payload)
- `created_at` (createdAt)

## Tham chiếu (references → bảng Drizzle)

- `shopsTable`
- `usersTable`

Tổng quan quan hệ: `reference/database.md`.
