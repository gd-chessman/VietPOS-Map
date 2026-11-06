# Lib: `gdt-portal/connect-with-captcha.ts`

**Mô tả:** Logic backend gdt-portal/connect-with-captcha.ts (~61 dòng) — export: gdtPortalConnectWithCaptcha, gdtPortalFetchCaptcha, gdtPortalConnectFailed.

**Source Shop:** `artifacts/api-server/src/lib/gdt-portal/connect-with-captcha.ts`

**Độ lớn:** ~61 dòng.

Thư viện backend dùng chung giữa nhiều route handler — đọc file gốc để biết thuật toán đầy đủ.

## Export (3 symbol)

- `gdtPortalConnectWithCaptcha`
- `gdtPortalFetchCaptcha`
- `gdtPortalConnectFailed`

## Xem trước đầu file

```typescript
import { captchaDataUrl } from "./client";
import { getOrCreateCaptchaClient, dropCaptchaClient } from "./captcha-store";
import {
  getGdtSessionPublic,
  markGdtTestFailed,
  resolveGdtPortalCredentials,
  saveGdtSessionToken,
  type GdtSessionPublic,
} from "./org-session";

export type GdtConnectWithCaptchaResult = {
  message: string;
  session: GdtSessionPublic;
  sampleCount: number | null;
  probeWarning: string | null;
};

export async function gdtPortalConnectWithCaptcha(
  orgId: number,
  captchaValue: string,
  credOverrides?: { username?: string; password?: string },
): Promise<GdtConnectWithCaptchaResult> {
  const cap = captchaValue.trim();
  if (!cap) throw new Error("Nhập mã captcha");

  const { username, password } = await resolveGdtPortalCredentials(orgId, credOverrides);
  const client = getOrCreateCaptchaClient(orgId);
  await client.authenticate(username, password, cap);
  await saveGdtSessionToken(orgId, client.token);

  let sampleCount: number | null = null;
  let probeWarning: string | null = null;
  try {
    sampleCount = await client.smokeTestPurchaseList();
  } catch (probeErr) {
```
