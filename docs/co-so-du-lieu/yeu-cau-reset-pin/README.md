# Schema: `pinResetRequests`

**Mô tả:** Drizzle schema pinResetRequests.ts — 8 cột trên 1 bảng Postgres (pin_reset_requests).

**Mã nguồn Shop:** `lib/db/src/schema/pinResetRequests.ts`

## Bảng Postgres

- `pin_reset_requests`

## Cột (trích từ schema TS)

- `id` (id)
- `user_id` (userId)
- `shop_id` (shopId)
- `status` (status)
- `requested_at` (requestedAt)
- `resolved_at` (resolvedAt)
- `resolved_by_user_id` (resolvedByUserId)
- `resolution_mode` (resolutionMode)

## Tham chiếu (references → bảng Drizzle)

- `shopsTable`
- `usersTable`

Tổng quan quan hệ: `tham-chieu/co-so-du-lieu-goc/README.md`.
