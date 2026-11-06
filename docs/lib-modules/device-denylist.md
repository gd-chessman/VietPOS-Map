# Lib: `device-denylist.ts`

**Mô tả:** Logic backend device-denylist.ts (~91 dòng) — export: blockedDeviceCount, normalizeDeviceId, deviceIdFromRequest, isValidBlockedDeviceId, refreshDeviceDenylistFromDb, ….

**Source Shop:** `artifacts/api-server/src/lib/device-denylist.ts`

**Độ lớn:** ~91 dòng.

Thư viện backend dùng chung giữa nhiều route handler — đọc file gốc để biết thuật toán đầy đủ.

## Export (7 symbol)

- `blockedDeviceCount`
- `normalizeDeviceId`
- `deviceIdFromRequest`
- `isValidBlockedDeviceId`
- `refreshDeviceDenylistFromDb`
- `startDeviceDenylistRefreshScheduler`
- `deviceDenylistMiddleware`

## Import DB / schema

- `import { db, blockedDevicesTable } from "@workspace/db";`
- `"[device-denylist] Bảng blocked_devices chưa có — chạy: pnpm --filter @workspace/db run apply:blocked-devices",`

## Xem trước đầu file

```typescript
import type { Request, RequestHandler } from "express";
import { db, blockedDevicesTable } from "@workspace/db";
import { logger } from "./logger";

const DEFAULT_REFRESH_MS = 10 * 60 * 1000;

function refreshMs(): number {
  const raw = process.env.IP_DENYLIST_REFRESH_MS ?? process.env.DEVICE_DENYLIST_REFRESH_MS;
  if (raw == null || raw.trim() === "") return DEFAULT_REFRESH_MS;
  const n = Number(raw);
  if (!Number.isFinite(n) || n < 0) return DEFAULT_REFRESH_MS;
  return Math.floor(n);
}

const mergedBlockedDevices = new Set<string>();

function rebuildMerged(ids: string[]): void {
  mergedBlockedDevices.clear();
  for (const id of ids) {
    const n = normalizeDeviceId(id);
    if (n) mergedBlockedDevices.add(n);
  }
}

export function blockedDeviceCount(): number {
  return mergedBlockedDevices.size;
}

export function normalizeDeviceId(raw: string | undefined | null): string {
  if (raw == null) return "";
  return raw.trim().slice(0, 128);
}

export function deviceIdFromRequest(req: Request): string | null {
  const h = req.headers["x-device-id"];
```
