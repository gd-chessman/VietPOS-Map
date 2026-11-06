# Schema: `deviceLoginEvents`

**Mô tả:** Drizzle deviceLoginEvents.ts — 1 bảng, 8 cột, 1 enum, 2 index (device_login_events).

**Mã nguồn Shop:** `lib/db/src/schema/deviceLoginEvents.ts`

## Cách đọc trang này

Mỗi **bảng Postgres** có bảng cột: kiểu Drizzle, `NOT NULL` / **PK**, khóa ngoại (cột FK → tên bảng đích), và ghi chú JSDoc từ mã nguồn. Enum và index được liệt kê riêng khi có trong file.

## Liên kết nhanh

- **HTTP API:** [quan-sat-truy-cap](../../module-api/quan-sat-truy-cap/) (`routes/access-observations.ts`)

## Enum Postgres

### `device_login_method` (`deviceLoginMethodEnum`)

- Giá trị: `[
  "password",
  "pin_setup",
  "pin_verify",
  "pin_device",
]`

## Bảng `device_login_events`

- **Biến Drizzle:** `deviceLoginEventsTable`

| Cột SQL | Thuộc tính TS | Kiểu | Ràng buộc | FK → bảng | Ghi chú |
|---------|---------------|------|-----------|-----------|---------|
| `id` | `id` | serial | **PK** | — | — |
| `shop_id` | `shopId` | integer | NOT NULL | `shops` | — |
| `device_id` | `deviceId` | text | NOT NULL | — | — |
| `user_id` | `userId` | integer | NOT NULL | `users` | — |
| `method` | `method` | enum `device_login_method` | NOT NULL | — | — |
| `ip` | `ip` | text | — | — | — |
| `user_agent` | `userAgent` | text | — | — | — |
| `created_at` | `createdAt` | timestamp("created_at", { withTimezone: true }) | NOT NULL, default `now()` | — | — |

**Index:**

- `device_login_events_shop_device_created_idx` on `shopId`, `deviceId`, `createdAt`
- `device_login_events_user_created_idx` on `userId`, `createdAt`

## Kiểu & Zod (insert)

- `export type DeviceLoginEvent`

Tổng quan ER / naming: [../../tham-chieu/co-so-du-lieu-goc/](../../tham-chieu/co-so-du-lieu-goc/).
