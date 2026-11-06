# Schema: `shiftSessions`

**Mô tả:** Drizzle schema shiftSessions.ts — 7 cột trên 2 bảng Postgres (shift_sessions, shift_session_staff).

**Mã nguồn Shop:** `lib/db/src/schema/shiftSessions.ts`

## Bảng Postgres

- `shift_sessions`
- `shift_session_staff`

## Cột (trích từ schema TS)

- `id` (id)
- `shop_id` (shopId)
- `user_id` (userId)
- `started_at` (startedAt)
- `ended_at` (endedAt)
- `session_id` (sessionId)
- `sales_staff_id` (salesStaffId)

## Tham chiếu (references → bảng Drizzle)

- `salesStaffTable`
- `shiftSessionsTable`
- `shopsTable`
- `usersTable`

Tổng quan quan hệ: `tham-chieu/co-so-du-lieu-goc/README.md`.
