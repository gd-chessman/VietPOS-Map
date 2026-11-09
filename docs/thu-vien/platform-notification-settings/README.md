# Thư viện: `platform-notification-settings.ts`

**Mô tả:** [Kiến trúc / dùng chung] platform-notification-settings.ts — RECIPIENT_ROLE_OPTIONS, invalidateNotificationSettingsCache, defaultRecipientRolesForType, effectiveRecipientRoles…

**Chủ đề:** [Kiến trúc / dùng chung](../../chuyen-de/kien-truc-he-thong/)

**Mã nguồn Shop:** `artifacts/api-server/src/lib/platform-notification-settings.ts` · **Quy mô:** ~467 dòng

File này là **tra cứu** khi đã đọc hub chủ đề và module API tương ứng. Thuật toán đầy đủ nằm trong mã TypeScript gốc.

## Hàm/hằng export (10)

- `RECIPIENT_ROLE_OPTIONS`
- `invalidateNotificationSettingsCache`
- `defaultRecipientRolesForType`
- `effectiveRecipientRoles`
- `getRecipientRolesForNotification`
- `ensureDefaultRows`
- `getNotificationChannelFlags`
- `listNotificationSettingsForAdmin`
- `patchNotificationSettings`
- `shouldSendNotificationEmail`

## Import cơ sở dữ liệu

- `import { db, platformNotificationSettingsTable } from "@workspace/db";`

← [Chỉ mục lib](../../chi-muc/thu-vien-backend/) · [Hub Kiến trúc / dùng chung](../../chuyen-de/kien-truc-he-thong/)
