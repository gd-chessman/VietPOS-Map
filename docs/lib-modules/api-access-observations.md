# Lib: `api-access-observations.ts`

**Mô tả:** Logic backend api-access-observations.ts (~157 dòng) — export: recordApiAccessObservation, summarizeAccessObservationsToday, listAccessObservations, accessObservationMiddleware, startAccessObservatio…

**Source Shop:** `artifacts/api-server/src/lib/api-access-observations.ts`

**Độ lớn:** ~157 dòng.

Thư viện backend dùng chung giữa nhiều route handler — đọc file gốc để biết thuật toán đầy đủ.

## Export (6 symbol)

- `recordApiAccessObservation`
- `summarizeAccessObservationsToday`
- `listAccessObservations`
- `accessObservationMiddleware`
- `startAccessObservationMaintenance`
- `accessObservationTtlHours`

## Xem trước đầu file

```typescript
import type { RequestHandler } from "express";
import { clientIpFromRequest } from "./ip-denylist";
import { deviceIdFromRequest, isValidBlockedDeviceId } from "./device-denylist";
import { vnCalendarDay } from "./vietnam-calendar";

const TTL_MS = 48 * 60 * 60 * 1000;
const MAX_ENTRIES = 20_000;
const SWEEP_MS = 15 * 60 * 1000;

export type AccessObservationRow = {
  deviceId: string;
  ip: string;
  hitCount: number;
  todayHitCount: number;
  firstSeen: string;
  lastSeen: string;
};

export type AccessObservationTodayStats = {
  calendarDay: string;
  totalHits: number;
  uniqueDevices: number;
  uniqueIps: number;
  activePairs: number;
};

type Entry = {
  deviceId: string;
  ip: string;
  hitCount: number;
  firstSeen: number;
  lastSeen: number;
  todayCalendarDay: string;
  todayHitCount: number;
};
```
