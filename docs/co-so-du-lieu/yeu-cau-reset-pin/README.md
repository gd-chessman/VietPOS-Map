# Schema: `pinResetRequests`

**Mô tả:** Drizzle pinResetRequests.ts — 1 bảng, 8 cột, 1 index (pin_reset_requests).

**Mã nguồn Shop:** `lib/db/src/schema/pinResetRequests.ts`

## Cách đọc trang này

Mỗi **bảng Postgres** có bảng cột: kiểu Drizzle, `NOT NULL` / **PK**, khóa ngoại (cột FK → tên bảng đích), và ghi chú JSDoc từ mã nguồn. Enum và index được liệt kê riêng khi có trong file.

## Bảng `pin_reset_requests`

*Yêu cầu quên mã PIN — quản trị xử lý tại /staff.*

- **Biến Drizzle:** `pinResetRequestsTable`

| Cột SQL | Thuộc tính TS | Kiểu | Ràng buộc | FK → bảng | Ghi chú |
|---------|---------------|------|-----------|-----------|---------|
| `id` | `id` | serial | **PK** | — | — |
| `user_id` | `userId` | integer | NOT NULL | `users` | — |
| `shop_id` | `shopId` | integer | NOT NULL | `shops` | — |
| `status` | `status` | text | NOT NULL, default `pending` | — | — |
| `requested_at` | `requestedAt` | timestamp("requested_at", { withTimezone: true }) | NOT NULL, default `now()` | — | — |
| `resolved_at` | `resolvedAt` | timestamp("resolved_at", { withTimezone: true }) | — | — | — |
| `resolved_by_user_id` | `resolvedByUserId` | integer | — | `users` | — |
| `resolution_mode` | `resolutionMode` | text | — | — | — |

**Index:**

- `pin_reset_requests_shop_status_idx` on `shopId`, `status`

## Kiểu & Zod (insert)

- `export type PinResetRequest`

Tổng quan ER / naming: [../../tham-chieu/co-so-du-lieu-goc/](../../tham-chieu/co-so-du-lieu-goc/).
