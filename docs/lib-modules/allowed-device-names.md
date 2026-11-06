# Lib: `allowed-device-names.ts`

**Mô tả:** Logic backend allowed-device-names.ts (~94 dòng) — export: lookupDeviceNamesByDeviceIds.

**Source Shop:** `artifacts/api-server/src/lib/allowed-device-names.ts`

**Độ lớn:** ~94 dòng.

Thư viện backend dùng chung giữa nhiều route handler — đọc file gốc để biết thuật toán đầy đủ.

## Export (1 symbol)

- `lookupDeviceNamesByDeviceIds`

## Import DB / schema

- `import { db, allowedDevicesTable, deviceLoginEventsTable } from "@workspace/db";`

## Xem trước đầu file

```typescript
import { db, allowedDevicesTable, deviceLoginEventsTable } from "@workspace/db";
import { desc, inArray } from "drizzle-orm";

function displayNameFromAllowed(row: {
  deviceName: string | null;
  identifierName: string | null;
}): string | null {
  const deviceName = row.deviceName?.trim();
  if (deviceName) return deviceName;
  const identifierName = row.identifierName?.trim();
  if (identifierName) return identifierName;
  return null;
}

function labelFromUserAgent(userAgent: string | null | undefined): string | null {
  if (!userAgent?.trim()) return null;
  const ua = userAgent.trim();
  const tauri = ua.match(/\bTauri\/[\d.]+/i);
  if (tauri) return "VietPOS (Tauri)";
  const platform =
    ua.match(/\(([^)]+)\)/)?.[1]?.split(";")[0]?.trim()
    ?? ua.slice(0, 48);
  if (!platform) return null;
  return platform.length <= 56 ? platform : `${platform.slice(0, 53)}…`;
}

async function lookupLoginUserAgentLabels(deviceIds: string[]): Promise<Map<string, string>> {
  const rows = await db
    .select({
      deviceId: deviceLoginEventsTable.deviceId,
      userAgent: deviceLoginEventsTable.userAgent,
    })
    .from(deviceLoginEventsTable)
    .where(inArray(deviceLoginEventsTable.deviceId, deviceIds))
    .orderBy(desc(deviceLoginEventsTable.createdAt));
```
