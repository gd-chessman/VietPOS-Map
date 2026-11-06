# Schema: `userNotifications`

**Mô tả:** Drizzle userNotifications.ts — 1 bảng, 11 cột, 2 index (user_notifications).

**Mã nguồn Shop:** `lib/db/src/schema/userNotifications.ts`

## Cách đọc trang này

Mỗi **bảng Postgres** có bảng cột: kiểu Drizzle, `NOT NULL` / **PK**, khóa ngoại (cột FK → tên bảng đích), và ghi chú JSDoc từ mã nguồn. Enum và index được liệt kê riêng khi có trong file.

## Liên kết nhanh

- **HTTP API:** [thong-bao](../../module-api/thong-bao/) (`routes/notifications.ts`)

## Bảng `user_notifications`

- **Biến Drizzle:** `userNotificationsTable`

| Cột SQL | Thuộc tính TS | Kiểu | Ràng buộc | FK → bảng | Ghi chú |
|---------|---------------|------|-----------|-----------|---------|
| `id` | `id` | serial | **PK** | — | — |
| `user_id` | `userId` | integer | NOT NULL | `users` | — |
| `shop_id` | `shopId` | integer | NOT NULL | `shops` | — |
| `notification_key` | `notificationKey` | text | NOT NULL | — | — |
| `type` | `type` | text | NOT NULL | — | — |
| `title` | `title` | text | NOT NULL | — | — |
| `body` | `body` | text | NOT NULL | — | — |
| `href` | `href` | text | NOT NULL | — | — |
| `severity` | `severity` | text | NOT NULL, default `info` | — | — |
| `created_at` | `createdAt` | timestamp("created_at", { withTimezone: true }) | NOT NULL, default `now()` | — | — |
| `read_at` | `readAt` | timestamp("read_at", { withTimezone: true }) | — | — | — |

**Index:**

- `user_notifications_user_key_uidx` on `userId`, `notificationKey`
- `user_notifications_user_unread_idx` on `userId`, `readAt`

## Kiểu & Zod (insert)

- `export type UserNotification`

Tổng quan ER / naming: [../../tham-chieu/co-so-du-lieu-goc/](../../tham-chieu/co-so-du-lieu-goc/).
