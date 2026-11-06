# Thư viện: `gdt-portal/captcha-store.ts`

**Mô tả:** [Hóa đơn đầu vào] gdt-portal/captcha-store.ts — getOrCreateCaptchaClient, dropCaptchaClient.

**Chủ đề:** [Hóa đơn đầu vào](../../../chuyen-de/hoa-don-dau-vao/)

**Mã nguồn Shop:** `artifacts/api-server/src/lib/gdt-portal/captcha-store.ts` · **Quy mô:** ~19 dòng

File này là **tra cứu** khi đã đọc hub chủ đề và module API tương ứng. Thuật toán đầy đủ nằm trong mã TypeScript gốc.

## Hàm/hằng export (2)

- `getOrCreateCaptchaClient`
- `dropCaptchaClient`

## Trích mã (tham khảo)

```typescript
import { GdtPortalClient } from "./client";

/** Phiên captcha tạm theo org (TTL ngắn, không scale multi-instance — đủ cho single server). */
const clients = new Map<number, { client: GdtPortalClient; at: number }>();
const TTL_MS = 5 * 60_000;

export function getOrCreateCaptchaClient(orgId: number): GdtPortalClient {
  const now = Date.now();
  const hit = clients.get(orgId);
  if (hit && now - hit.at < TTL_MS) return hit.client;
  const client = new GdtPortalClient();
  clients.set(orgId, { client, at: now });
  return client;
}

export function dropCaptchaClient(orgId: number): void {
  clients.delete(orgId);
}
```

← [Chỉ mục lib](../../../chi-muc/thu-vien-backend/) · [Hub Hóa đơn đầu vào](../../../chuyen-de/hoa-don-dau-vao/)
