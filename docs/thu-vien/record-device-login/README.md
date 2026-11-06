# Thư viện: `record-device-login.ts`

**Mô tả:** [Kiến trúc / dùng chung] record-device-login.ts — recordDeviceLoginEvent.

**Chủ đề:** [Kiến trúc / dùng chung](../../chuyen-de/kien-truc-he-thong/)

**Mã nguồn Shop:** `artifacts/api-server/src/lib/record-device-login.ts` · **Quy mô:** ~37 dòng

File này là **tra cứu** khi đã đọc hub chủ đề và module API tương ứng. Thuật toán đầy đủ nằm trong mã TypeScript gốc.

## Hàm/hằng export (1)

- `recordDeviceLoginEvent`

## Import cơ sở dữ liệu

- `import { db, deviceLoginEventsTable, type User } from "@workspace/db";`

## Trích mã (tham khảo)

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
}
```

← [Chỉ mục lib](../../chi-muc/thu-vien-backend/) · [Hub Kiến trúc / dùng chung](../../chuyen-de/kien-truc-he-thong/)
