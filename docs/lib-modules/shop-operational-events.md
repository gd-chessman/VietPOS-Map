# Lib: `shop-operational-events.ts`

**Mô tả:** Logic backend shop-operational-events.ts (~147 dòng) — export: syncShopOperationalState, runShopPresenceSweep.

**Source Shop:** `artifacts/api-server/src/lib/shop-operational-events.ts`

**Độ lớn:** ~147 dòng.

Thư viện backend dùng chung giữa nhiều route handler — đọc file gốc để biết thuật toán đầy đủ.

## Export (2 symbol)

- `syncShopOperationalState`
- `runShopPresenceSweep`

## Import DB / schema

- `} from "@workspace/db";`

## Xem trước đầu file

```typescript
import {
  db,
  shopsTable,
  shopOperationalEventsTable,
  type ShopOperationalEventPayload,
} from "@workspace/db";
import { eq } from "drizzle-orm";
import { hasClockDrift, isShopOnline } from "./shop-presence";
import { recordSystemEvent } from "./system-event-log";

export type ShopPresenceRow = {
  id: number;
  lastSeenAt: Date | null;
  lastHeartbeatDeviceTime: Date | null;
  presenceEventState: string | null;
  clockDriftEventState: boolean | null;
};

type EventSource = ShopOperationalEventPayload["source"];

function presenceFromState(stored: string | null): "online" | "offline" {
  return stored === "online" ? "online" : "offline";
}

function driftMs(serverTime: Date, deviceTime: Date): number {
  return serverTime.getTime() - deviceTime.getTime();
}

async function insertEvent(
  shopId: number,
  eventType: "shop_online" | "shop_offline" | "clock_drift_detected" | "clock_drift_cleared",
  payload: ShopOperationalEventPayload,
  userId?: number,
): Promise<void> {
  await db.insert(shopOperationalEventsTable).values({
```
