# Schema: `allowedDevices`

**Mô tả:** Drizzle allowedDevices.ts — 1 bảng, 8 cột (allowed_devices).

**Mã nguồn Shop:** `lib/db/src/schema/allowedDevices.ts`

## Cách đọc trang này

Mỗi **bảng Postgres** có bảng cột: kiểu Drizzle, `NOT NULL` / **PK**, khóa ngoại (cột FK → tên bảng đích), và ghi chú JSDoc từ mã nguồn. Enum và index được liệt kê riêng khi có trong file.

## Liên kết nhanh

- **HTTP API:** [quan-sat-truy-cap](../../module-api/quan-sat-truy-cap/) (`routes/access-observations.ts`)

## Bảng `allowed_devices`

*Tracks which browser-generated device IDs are approved to operate as a POS for a given shop.*

- **Biến Drizzle:** `allowedDevicesTable`

| Cột SQL | Thuộc tính TS | Kiểu | Ràng buộc | FK → bảng | Ghi chú |
|---------|---------------|------|-----------|-----------|---------|
| `id` | `id` | serial | **PK** | — | — |
| `shop_id` | `shopId` | integer | NOT NULL | `shops` | — |
| `device_id` | `deviceId` | text | NOT NULL | — | — |
| `device_name` | `deviceName` | text | — | — | — |
| `identifier_name` | `identifierName` | text | — | — | — |
| `status` | `status` | text | NOT NULL, default `pending` | — | — |
| `created_at` | `createdAt` | timestamp("created_at", { withTimezone: true }) | NOT NULL, default `now()` | — | — |
| `approved_by` | `approvedBy` | integer | — | `users` | — |

## Kiểu & Zod (insert)

- `export type AllowedDevice`

Tổng quan ER / naming: [../../tham-chieu/co-so-du-lieu-goc/](../../tham-chieu/co-so-du-lieu-goc/).
