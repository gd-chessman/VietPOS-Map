# Lib: `vn-order-period.ts`

**Mô tả:** Logic backend vn-order-period.ts (~117 dòng) — export: VN_YMD_RE, vnYmdStartInstant, vnYmdEndInclusiveInstant, resolveChartAlignedOrderPeriodBounds, appendChartAlignedOrderPeriodFilters, ….

**Source Shop:** `artifacts/api-server/src/lib/vn-order-period.ts`

**Độ lớn:** ~117 dòng.

Thư viện backend dùng chung giữa nhiều route handler — đọc file gốc để biết thuật toán đầy đủ.

## Export (7 symbol)

- `VN_YMD_RE`
- `vnYmdStartInstant`
- `vnYmdEndInclusiveInstant`
- `resolveChartAlignedOrderPeriodBounds`
- `appendChartAlignedOrderPeriodFilters`
- `appendVnYmdOrderPeriodFilters`
- `resolveStatisticsPeriodFromTo`

## Import DB / schema

- `import { ordersTable } from "@workspace/db";`

## Xem trước đầu file

```typescript
import { ordersTable } from "@workspace/db";
import { gte, lt, type SQL } from "drizzle-orm";
import {
  buildDashboardRevenueChartBuckets,
  parseDashboardChartGranularity,
} from "./dashboard-period";
import { buildVietnamCalendarDayHourBuckets } from "./vietnam-calendar";

export const VN_YMD_RE = /^\d{4}-\d{2}-\d{2}$/;

export function vnYmdStartInstant(ymd: string): Date | null {
  const s = ymd.trim();
  if (!VN_YMD_RE.test(s)) return null;
  const d = new Date(`${s}T00:00:00.000+07:00`);
  return Number.isNaN(d.getTime()) ? null : d;
}

export function vnYmdEndInclusiveInstant(ymd: string): Date | null {
  const s = ymd.trim();
  if (!VN_YMD_RE.test(s)) return null;
  const d = new Date(`${s}T23:59:59.999+07:00`);
  return Number.isNaN(d.getTime()) ? null : d;
}

function vnYmdEndExclusiveInstant(ymd: string): Date | null {
  const start = vnYmdStartInstant(ymd);
  if (!start) return null;
  return new Date(start.getTime() + 86_400_000);
}

export type ChartOrderPeriodOpts = {
  period?: string;
  fromQuery?: string;
  toQuery?: string;
  granularity?: string;
```
