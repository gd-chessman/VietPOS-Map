# Lib: `platform-notification-settings.ts`

**Mô tả:** Logic backend platform-notification-settings.ts (~467 dòng) — export: RECIPIENT_ROLE_OPTIONS, invalidateNotificationSettingsCache, defaultRecipientRolesForType, effectiveRecipientRoles, getRecipientR…

**Source Shop:** `artifacts/api-server/src/lib/platform-notification-settings.ts`

**Độ lớn:** ~467 dòng.

Thư viện backend dùng chung giữa nhiều route handler — đọc file gốc để biết thuật toán đầy đủ.

## Export (10 symbol)

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

## Import DB / schema

- `import { db, platformNotificationSettingsTable } from "@workspace/db";`

## Xem trước đầu file

```typescript
import { db, platformNotificationSettingsTable } from "@workspace/db";
import { eq } from "drizzle-orm";

export const RECIPIENT_ROLE_OPTIONS = [
  { key: "super_admin", label: "Quản trị hệ thống" },
  { key: "admin_platform", label: "Quản trị tổng" },
  { key: "hub_admin", label: "Quản trị chi nhánh" },
  { key: "hub_manager", label: "Quản lý tổng" },
  { key: "shop_manager", label: "Quản lý chi nhánh" },
  { key: "shop_accountant", label: "Kế toán tại cửa hàng" },
  { key: "shop_warehouse_keeper", label: "Thủ kho tại cửa hàng" },
] as const;

export type RecipientRoleKey = (typeof RECIPIENT_ROLE_OPTIONS)[number]["key"];

const ALL_ROLE_KEYS = new Set<string>(RECIPIENT_ROLE_OPTIONS.map((o) => o.key));

export type NotificationTypeDef = {
  type: string;
  label: string;
  description: string;
  recipients: string;
  supportsEmail: boolean;
  category: string;
  availableRecipientRoles: RecipientRoleKey[];
  defaultRecipientRoles: RecipientRoleKey[];
  /** Shop lẻ (không org) — bổ sung vai trò nhận khi bật. */
  standaloneRecipientRoles?: RecipientRoleKey[];
};

/** Giám sát bán hàng / chuỗi — 5 vai trò; mặc định bật 4 (không bật quản lý chi nhánh con). */
const CHAIN_OVERSIGHT_TYPES: RecipientRoleKey[] = [
  "super_admin",
  "admin_platform",
  "hub_admin",
```
