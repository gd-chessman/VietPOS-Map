# Schema: `shiftSessions`

**Mô tả:** Drizzle shiftSessions.ts — 2 bảng, 7 cột, 1 index (shift_sessions, shift_session_staff).

**Mã nguồn Shop:** `lib/db/src/schema/shiftSessions.ts`

## Cách đọc trang này

Mỗi **bảng Postgres** có bảng cột: kiểu Drizzle, `NOT NULL` / **PK**, khóa ngoại (cột FK → tên bảng đích), và ghi chú JSDoc từ mã nguồn. Enum và index được liệt kê riêng khi có trong file.

## Liên kết nhanh

- **HTTP API:** [ca-lam-viec](../../module-api/ca-lam-viec/) (`routes/shift-sessions.ts`)

## Bảng `shift_sessions`

- **Biến Drizzle:** `shiftSessionsTable`

| Cột SQL | Thuộc tính TS | Kiểu | Ràng buộc | FK → bảng | Ghi chú |
|---------|---------------|------|-----------|-----------|---------|
| `id` | `id` | serial | **PK** | — | — |
| `shop_id` | `shopId` | integer | NOT NULL | `shops` | — |
| `user_id` | `userId` | integer | NOT NULL | `users` | — |
| `started_at` | `startedAt` | timestamp("started_at", { withTimezone: true }) | NOT NULL, default `now()` | — | — |
| `ended_at` | `endedAt` | timestamp("ended_at", { withTimezone: true }) | — | — | — |

**Index:**

- `shift_sessions_shop_user_open_idx` on `shopId`, `userId`, `endedAt`

## Bảng `shift_session_staff`

- **Biến Drizzle:** `shiftSessionStaffTable`

| Cột SQL | Thuộc tính TS | Kiểu | Ràng buộc | FK → bảng | Ghi chú |
|---------|---------------|------|-----------|-----------|---------|
| `session_id` | `sessionId` | integer | NOT NULL | `shift_sessions` | — |
| `sales_staff_id` | `salesStaffId` | integer | NOT NULL | `sales_staff` | — |

## Kiểu & Zod (insert)

- `export type ShiftSession`
- `export type ShiftSessionStaff`

Tổng quan ER / naming: [../../tham-chieu/co-so-du-lieu-goc/](../../tham-chieu/co-so-du-lieu-goc/).
