# Lib: `gdt-portal/captcha-store.ts`

**Mô tả:** Logic backend gdt-portal/captcha-store.ts (~19 dòng) — export: getOrCreateCaptchaClient, dropCaptchaClient.

**Source Shop:** `artifacts/api-server/src/lib/gdt-portal/captcha-store.ts`

**Độ lớn:** ~19 dòng.

Thư viện backend dùng chung giữa nhiều route handler — đọc file gốc để biết thuật toán đầy đủ.

## Export (2 symbol)

- `getOrCreateCaptchaClient`
- `dropCaptchaClient`

## Xem trước đầu file

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
