# Schema: `users`

**Mô tả:** Drizzle users.ts — 1 bảng, 13 cột, 2 enum, 2 index (users).

**Mã nguồn Shop:** `lib/db/src/schema/users.ts`

## Cách đọc trang này

Mỗi **bảng Postgres** có bảng cột: kiểu Drizzle, `NOT NULL` / **PK**, khóa ngoại (cột FK → tên bảng đích), và ghi chú JSDoc từ mã nguồn. Enum và index được liệt kê riêng khi có trong file.

## Enum Postgres

### `user_role` (`userRoleEnum`)

- Giá trị: `["super_admin", "admin", "manager", "staff", "accountant", "warehouse_keeper"]`

### `user_status` (`userStatusEnum`)

- Giá trị: `["active", "on_leave", "resigned"]`

## Bảng `users`

- **Biến Drizzle:** `usersTable`

| Cột SQL | Thuộc tính TS | Kiểu | Ràng buộc | FK → bảng | Ghi chú |
|---------|---------------|------|-----------|-----------|---------|
| `id` | `id` | serial | **PK** | — | — |
| `name` | `name` | text | — | — | — |
| `email` | `email` | text | NOT NULL | — | — |
| `password` | `password` | text | NOT NULL | — | — |
| `role` | `role` | enum `user_role` | NOT NULL, default `staff` | — | — |
| `status` | `status` | enum `user_status` | NOT NULL, default `active` | — | — |
| `organization_id` | `organizationId` | integer | — | `organizations` | — |
| `shop_id` | `shopId` | integer | NOT NULL | `shops` | — |
| `pin_hash` | `pinHash` | text | — | — | — |
| `pin_set_at` | `pinSetAt` | timestamp("pin_set_at", { withTimezone: true }) | — | — | — |
| `pin_failed_attempts` | `pinFailedAttempts` | integer | NOT NULL, default `0` | — | — |
| `pin_locked_until` | `pinLockedUntil` | timestamp("pin_locked_until", { withTimezone: true }) | — | — | — |
| `agent_assistant_enabled` | `agentAssistantEnabled` | boolean | NOT NULL, default `false` | — | — |

**Index:**

- `users_shop_email_uidx` on `shopId`, `email`
- `users_org_email_uidx` on `organizationId`, `email`

## Kiểu & Zod (insert)

- `insertUserSchema` — `createInsertSchema` (xem file TS)
- `export type InsertUser`
- `export type User`

Tổng quan ER / naming: [../../tham-chieu/co-so-du-lieu-goc/](../../tham-chieu/co-so-du-lieu-goc/).
