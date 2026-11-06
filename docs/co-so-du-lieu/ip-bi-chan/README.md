# Schema: `blockedIps`

**Mô tả:** Drizzle blockedIps.ts — 1 bảng, 5 cột, 1 index (blocked_ips).

**Mã nguồn Shop:** `lib/db/src/schema/blockedIps.ts`

## Cách đọc trang này

Mỗi **bảng Postgres** có bảng cột: kiểu Drizzle, `NOT NULL` / **PK**, khóa ngoại (cột FK → tên bảng đích), và ghi chú JSDoc từ mã nguồn. Enum và index được liệt kê riêng khi có trong file.

## Liên kết nhanh

- **HTTP API:** [chan-ip-api](../../module-api/chan-ip-api/) (`routes/blocked-ips.ts`)

## Bảng `blocked_ips`

*IP bị chặn toàn bộ /api — quản lý qua giao diện quản trị hệ thống.*

- **Biến Drizzle:** `blockedIpsTable`

| Cột SQL | Thuộc tính TS | Kiểu | Ràng buộc | FK → bảng | Ghi chú |
|---------|---------------|------|-----------|-----------|---------|
| `id` | `id` | serial | **PK** | — | — |
| `ip` | `ip` | text | NOT NULL | — | — |
| `note` | `note` | text | — | — | — |
| `created_at` | `createdAt` | timestamp("created_at", { withTimezone: true }) | NOT NULL, default `now()` | — | — |
| `created_by` | `createdBy` | integer | — | `users` | — |

**Index:**

- `blocked_ips_ip_idx` on `ip`

## Kiểu & Zod (insert)

- `export type BlockedIp`

Tổng quan ER / naming: [../../tham-chieu/co-so-du-lieu-goc/](../../tham-chieu/co-so-du-lieu-goc/).
