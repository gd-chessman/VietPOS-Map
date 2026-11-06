# Schema: `changeLog`

**Mô tả:** Drizzle schema changeLog.ts — 6 cột trên 1 bảng Postgres (change_log).

**Source Shop:** `lib/db/src/schema/changeLog.ts`

## Bảng Postgres

- `change_log`

## Cột (trích từ schema TS)

- `seq` (seq)
- `shop_id` (shopId)
- `entity_type` (entityType)
- `entity_id` (entityId)
- `change_type` (changeType)
- `created_at` (createdAt)

## Tham chiếu (references → bảng Drizzle)

- `shopsTable`

Tổng quan quan hệ: `reference/database.md`.
