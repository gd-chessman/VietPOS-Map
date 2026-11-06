# Thư viện: `gdt-portal/connect-with-captcha.ts`

**Mô tả:** [Hóa đơn đầu vào] gdt-portal/connect-with-captcha.ts — gdtPortalConnectWithCaptcha, gdtPortalFetchCaptcha, gdtPortalConnectFailed.

**Chủ đề:** [Hóa đơn đầu vào](../../../chuyen-de/hoa-don-dau-vao/)

**Mã nguồn Shop:** `artifacts/api-server/src/lib/gdt-portal/connect-with-captcha.ts` · **Quy mô:** ~61 dòng

File này là **tra cứu** khi đã đọc hub chủ đề và module API tương ứng. Thuật toán đầy đủ nằm trong mã TypeScript gốc.

## Hàm/hằng export (3)

- `gdtPortalConnectWithCaptcha`
- `gdtPortalFetchCaptcha`
- `gdtPortalConnectFailed`

## Trích mã (tham khảo)

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
    probeWarning =
      probeErr instanceof Error ? probeErr.message : "CQT timeout khi thử kéo HĐ (504/500).";
  }
  dropCaptchaClient(orgId);

  const session = await getGdtSessionPublic(orgId);
  const message = probeWarning
    ? `Đã đăng nhập CQT và lưu phiên. Thử kéo HĐ chưa xong: ${probeWarning}`
    : `Kết nối CQT thành công (thấy ${sampleCount ?? 0} HĐ mẫu trong ngày hôm nay).`;

```

← [Chỉ mục lib](../../../chi-muc/thu-vien-backend/) · [Hub Hóa đơn đầu vào](../../../chuyen-de/hoa-don-dau-vao/)
