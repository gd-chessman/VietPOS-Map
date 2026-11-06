# Schema: `blockedDevices`

**Mô tả:** Drizzle blockedDevices.ts — 1 bảng, 5 cột, 1 index (blocked_devices).

**Mã nguồn Shop:** `lib/db/src/schema/blockedDevices.ts`

## Cách đọc trang này

Mỗi **bảng Postgres** có bảng cột: kiểu Drizzle, `NOT NULL` / **PK**, khóa ngoại (cột FK → tên bảng đích), và ghi chú JSDoc từ mã nguồn. Enum và index được liệt kê riêng khi có trong file.

## Liên kết nhanh

- **HTTP API:** [chan-thiet-bi-api](../../module-api/chan-thiet-bi-api/) (`routes/blocked-devices.ts`)

## Bảng `blocked_devices`

*Device ID (X-Device-Id) bị chặn toàn bộ /api — trước và sau đăng nhập.*

- **Biến Drizzle:** `blockedDevicesTable`

| Cột SQL | Thuộc tính TS | Kiểu | Ràng buộc | FK → bảng | Ghi chú |
|---------|---------------|------|-----------|-----------|---------|
| `id` | `id` | serial | **PK** | — | — |
| `device_id` | `deviceId` | text | NOT NULL | — | — |
| `note` | `note` | text | — | — | — |
| `created_at` | `createdAt` | timestamp("created_at", { withTimezone: true }) | NOT NULL, default `now()` | — | — |
| `created_by` | `createdBy` | integer | — | `users` | — |

**Index:**

- `blocked_devices_device_id_idx` on `deviceId`

## Kiểu & Zod (insert)

- `export type BlockedDevice`

Tổng quan ER / naming: [../../tham-chieu/co-so-du-lieu-goc/](../../tham-chieu/co-so-du-lieu-goc/).
