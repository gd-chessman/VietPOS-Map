# Schema: `systemEventLogs`

**Mô tả:** Drizzle systemEventLogs.ts — 1 bảng, 11 cột, 4 index (system_event_logs).

**Mã nguồn Shop:** `lib/db/src/schema/systemEventLogs.ts`

## Cách đọc trang này

Mỗi **bảng Postgres** có bảng cột: kiểu Drizzle, `NOT NULL` / **PK**, khóa ngoại (cột FK → tên bảng đích), và ghi chú JSDoc từ mã nguồn. Enum và index được liệt kê riêng khi có trong file.

## Bảng `system_event_logs`

- **Biến Drizzle:** `systemEventLogsTable`

| Cột SQL | Thuộc tính TS | Kiểu | Ràng buộc | FK → bảng | Ghi chú |
|---------|---------------|------|-----------|-----------|---------|
| `id` | `id` | serial | **PK** | — | — |
| `organization_id` | `organizationId` | integer | — | `organizations` | — |
| `shop_id` | `shopId` | integer | — | `shops` | — |
| `user_id` | `userId` | integer | — | `users` | — |
| `device_id` | `deviceId` | text | — | — | — |
| `category` | `category` | text | NOT NULL, JSON typed | — | — |
| `severity` | `severity` | text | NOT NULL, JSON typed | — | — |
| `code` | `code` | text | NOT NULL | — | — |
| `message` | `message` | text | NOT NULL | — | — |
| `detail` | `detail` | jsonb | JSON typed | — | — |
| `created_at` | `createdAt` | timestamp("created_at", { withTimezone: true }) | NOT NULL, default `now()` | — | — |

**Index:**

- `system_event_logs_org_created_idx` on `organizationId`, `createdAt`
- `system_event_logs_shop_created_idx` on `shopId`, `createdAt`
- `system_event_logs_category_created_idx` on `category`, `createdAt`
- `system_event_logs_severity_created_idx` on `severity`, `createdAt`

## Kiểu & Zod (insert)

- `export type SystemEventCategory`
- `export type SystemEventSeverity`
- `export type SystemEventDetail`
- `export type SystemEventLog`

Tổng quan ER / naming: [../../tham-chieu/co-so-du-lieu-goc/](../../tham-chieu/co-so-du-lieu-goc/).
