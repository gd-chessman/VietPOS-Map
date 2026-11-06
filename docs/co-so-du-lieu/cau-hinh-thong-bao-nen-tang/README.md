# Schema: `platformNotificationSettings`

**Mô tả:** Drizzle platformNotificationSettings.ts — 1 bảng, 5 cột (platform_notification_settings).

**Mã nguồn Shop:** `lib/db/src/schema/platformNotificationSettings.ts`

## Cách đọc trang này

Mỗi **bảng Postgres** có bảng cột: kiểu Drizzle, `NOT NULL` / **PK**, khóa ngoại (cột FK → tên bảng đích), và ghi chú JSDoc từ mã nguồn. Enum và index được liệt kê riêng khi có trong file.

## Bảng `platform_notification_settings`

*Cài đặt kênh thông báo toàn hệ thống (chỉ super_admin sửa).*

- **Biến Drizzle:** `platformNotificationSettingsTable`

| Cột SQL | Thuộc tính TS | Kiểu | Ràng buộc | FK → bảng | Ghi chú |
|---------|---------------|------|-----------|-----------|---------|
| `notification_type` | `notificationType` | text | **PK** | — | — |
| `in_app_enabled` | `inAppEnabled` | boolean | NOT NULL, default `true` | — | — |
| `email_enabled` | `emailEnabled` | boolean | NOT NULL, default `true` | — | — |
| `recipient_roles` | `recipientRoles` | jsonb | JSON typed | — | — |
| `updated_at` | `updatedAt` | timestamp("updated_at", { withTimezone: true }) | NOT NULL, default `now()` | — | — |

## Kiểu & Zod (insert)

- `export type PlatformNotificationSetting`

Tổng quan ER / naming: [../../tham-chieu/co-so-du-lieu-goc/](../../tham-chieu/co-so-du-lieu-goc/).
