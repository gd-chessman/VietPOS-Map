# Lib: `record-device-login.ts`

**Mô tả:** Logic backend record-device-login.ts (~37 dòng) — export: recordDeviceLoginEvent.

**Source Shop:** `artifacts/api-server/src/lib/record-device-login.ts`

**Độ lớn:** ~37 dòng.

Thư viện backend dùng chung giữa nhiều route handler — đọc file gốc để biết thuật toán đầy đủ.

## Export (1 symbol)

- `recordDeviceLoginEvent`

## Import DB / schema

- `import { db, deviceLoginEventsTable, type User } from "@workspace/db";`

## Xem trước đầu file

```typescript
import type { Request } from "express";
import { db, deviceLoginEventsTable, type User } from "@workspace/db";
import { deviceIdFromRequest } from "./device-denylist";
import { clientIpFromRequest } from "./ip-denylist";

export type DeviceLoginMethod = "password" | "pin_setup" | "pin_verify" | "pin_device";

function truncateUserAgent(raw: string | undefined): string | null {
  if (!raw) return null;
  const t = raw.trim();
  if (!t) return null;
  return t.slice(0, 512);
}

/** Ghi lịch sử đăng nhập khi có X-Device-Id; lỗi ghi log không chặn phiên. */
export async function recordDeviceLoginEvent(
  req: Request,
  user: Pick<User, "id" | "shopId">,
  method: DeviceLoginMethod,
): Promise<void> {
  const deviceId = deviceIdFromRequest(req);
  if (!deviceId) return;

  const ip = clientIpFromRequest(req) || null;
  const uaHeader = req.headers["user-agent"];
  const userAgent = truncateUserAgent(typeof uaHeader === "string" ? uaHeader : undefined);

  await db.insert(deviceLoginEventsTable).values({
    shopId: user.shopId,
    deviceId,
    userId: user.id,
    method,
    ip,
    userAgent,
  });
```
