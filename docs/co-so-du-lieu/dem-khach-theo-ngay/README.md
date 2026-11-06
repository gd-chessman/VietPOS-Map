# Schema: `shopDailyVisitorCounts`

**Mô tả:** Drizzle shopDailyVisitorCounts.ts — 1 bảng, 5 cột (shop_daily_visitor_counts).

**Mã nguồn Shop:** `lib/db/src/schema/shopDailyVisitorCounts.ts`

## Cách đọc trang này

Mỗi **bảng Postgres** có bảng cột: kiểu Drizzle, `NOT NULL` / **PK**, khóa ngoại (cột FK → tên bảng đích), và ghi chú JSDoc từ mã nguồn. Enum và index được liệt kê riêng khi có trong file.

## Liên kết nhanh

- **HTTP API:** [khach-vang-lai](../../module-api/khach-vang-lai/) (`routes/walk-in-customers.ts`)

## Bảng `shop_daily_visitor_counts`

- **Biến Drizzle:** `shopDailyVisitorCountsTable`

| Cột SQL | Thuộc tính TS | Kiểu | Ràng buộc | FK → bảng | Ghi chú |
|---------|---------------|------|-----------|-----------|---------|
| `shop_id` | `shopId` | integer | NOT NULL | `shops` | — |
| `visit_date` | `visitDate` | date | NOT NULL | — | — |
| `visitor_count` | `visitorCount` | integer | NOT NULL, default `0` | — | — |
| `beam_count` | `beamCount` | integer | NOT NULL, default `0` | — | — |
| `updated_at` | `updatedAt` | timestamp("updated_at", { withTimezone: true }) | NOT NULL, default `now()` | — | — |

Tổng quan ER / naming: [../../tham-chieu/co-so-du-lieu-goc/](../../tham-chieu/co-so-du-lieu-goc/).
