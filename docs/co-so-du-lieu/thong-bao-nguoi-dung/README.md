# Schema: `userNotifications`

**Mô tả:** Drizzle schema userNotifications.ts — 11 cột trên 1 bảng Postgres (user_notifications).

**Mã nguồn Shop:** `lib/db/src/schema/userNotifications.ts`

## Bảng Postgres

- `user_notifications`

## Cột (trích từ schema TS)

- `id` (id)
- `user_id` (userId)
- `shop_id` (shopId)
- `notification_key` (notificationKey)
- `type` (type)
- `title` (title)
- `body` (body)
- `href` (href)
- `severity` (severity)
- `created_at` (createdAt)
- `read_at` (readAt)

## Tham chiếu (references → bảng Drizzle)

- `shopsTable`
- `usersTable`

Tổng quan quan hệ: `tham-chieu/co-so-du-lieu-goc/README.md`.
