# Schema: `shopOperationalEvents`

**Mô tả:** Drizzle shopOperationalEvents.ts — 1 bảng, 6 cột, 1 enum, 2 index (shop_operational_events).

**Mã nguồn Shop:** `lib/db/src/schema/shopOperationalEvents.ts`

## Cách đọc trang này

Mỗi **bảng Postgres** có bảng cột: kiểu Drizzle, `NOT NULL` / **PK**, khóa ngoại (cột FK → tên bảng đích), và ghi chú JSDoc từ mã nguồn. Enum và index được liệt kê riêng khi có trong file.

## Enum Postgres

### `shop_operational_event_type` (`shopOperationalEventTypeEnum`)

- Giá trị: `[
  "shop_online",
  "shop_offline",
  "clock_drift_detected",
  "clock_drift_cleared",
]`

## Bảng `shop_operational_events`

- **Biến Drizzle:** `shopOperationalEventsTable`

| Cột SQL | Thuộc tính TS | Kiểu | Ràng buộc | FK → bảng | Ghi chú |
|---------|---------------|------|-----------|-----------|---------|
| `id` | `id` | serial | **PK** | — | — |
| `shop_id` | `shopId` | integer | NOT NULL | `shops` | — |
| `user_id` | `userId` | integer | — | `users` | — |
| `event_type` | `eventType` | enum `shop_operational_event_type` | NOT NULL | — | — |
| `payload` | `payload` | jsonb | NOT NULL, default `{}`, JSON typed | — | — |
| `created_at` | `createdAt` | timestamp("created_at", { withTimezone: true }) | NOT NULL, default `now()` | — | — |

**Index:**

- `shop_operational_events_shop_created_idx` on `shopId`, `createdAt`
- `shop_operational_events_type_created_idx` on `eventType`, `createdAt`

## Kiểu & Zod (insert)

- `export type ShopOperationalEventPayload`
- `export type ShopOperationalEvent`

Tổng quan ER / naming: [../../tham-chieu/co-so-du-lieu-goc/](../../tham-chieu/co-so-du-lieu-goc/).
