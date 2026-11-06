# Lib: `org-gdt-settings.ts`

**Mô tả:** Logic backend org-gdt-settings.ts (~92 dòng) — export: stripOrgGdtPassword, applyGdtSettingsFromBody, gdtCredentialsReady, buildVatInboundChannelStatus.

**Source Shop:** `artifacts/api-server/src/lib/org-gdt-settings.ts`

**Độ lớn:** ~92 dòng.

Thư viện backend dùng chung giữa nhiều route handler — đọc file gốc để biết thuật toán đầy đủ.

## Export (4 symbol)

- `stripOrgGdtPassword`
- `applyGdtSettingsFromBody`
- `gdtCredentialsReady`
- `buildVatInboundChannelStatus`

## Xem trước đầu file

```typescript
import type { GdtSessionPublic } from "./gdt-portal/org-session";
import { normalizeVatInboundProvider } from "./gdt-portal/org-session";
import type { ViettelConfigReadiness, ViettelInvoiceSettingsPublic } from "./org-viettel-settings";
import { viettelConfigReadiness } from "./org-viettel-settings";

export type OrgGdtDbFields = {
  vatInboundProvider?: string | null;
  gdtPortalUsername?: string | null;
  gdtPortalPassword?: string | null;
};

export type VatInboundChannelStatus = ViettelConfigReadiness & {
  vatInboundProvider: "viettel" | "gdt_direct";
  gdtPortalUsername: string | null;
  gdtPortalPasswordConfigured: boolean;
  gdtSession: GdtSessionPublic;
  /** Đủ điều kiện bật auto-sync / kéo HĐ theo kênh đang chọn. */
  inboundSyncReady: boolean;
};

export function stripOrgGdtPassword<T extends OrgGdtDbFields>(
  org: T,
): Omit<T, "gdtPortalPassword"> & { gdtPortalPasswordConfigured: boolean } {
  const { gdtPortalPassword, ...rest } = org;
  return {
    ...rest,
    gdtPortalPasswordConfigured: Boolean(gdtPortalPassword?.trim()),
  };
}

function optText(v: unknown): string | null | undefined {
  if (v === undefined) return undefined;
  if (v === null || v === "") return null;
  if (typeof v !== "string") return undefined;
  const t = v.trim();
```
