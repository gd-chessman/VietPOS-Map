# Lib: `dashboard-period.ts`

**Mô tả:** Logic backend dashboard-period.ts (~284 dòng) — export: resolveDashboardPeriodRange, parseDashboardChartGranularity, parseQuarterChartGranularity, buildDashboardRevenueChartBuckets.

**Source Shop:** `artifacts/api-server/src/lib/dashboard-period.ts`

**Độ lớn:** ~284 dòng.

Thư viện backend dùng chung giữa nhiều route handler — đọc file gốc để biết thuật toán đầy đủ.

## Export (4 symbol)

- `resolveDashboardPeriodRange`
- `parseDashboardChartGranularity`
- `parseQuarterChartGranularity`
- `buildDashboardRevenueChartBuckets`

## Xem trước đầu file

```typescript
import {
  buildVietnamCalendarDayHourBuckets,
  vnAddCalendarDays,
  vnCalendarDay,
  vnDayBoundsExclusive,
} from "./vietnam-calendar";

export type DashboardPeriod =
  | "day"
  | "yesterday"
  | "last_week"
  | "this_week"
  | "this_month"
  | "last_month"
  | "q1"
  | "q2"
  | "q3"
  | "q4"
  | "this_year"
  | "last_year";

export type ChartBucket = { start: Date; end: Date; label: string };

function startOfDay(d: Date): Date {
  const x = new Date(d);
  x.setHours(0, 0, 0, 0);
  return x;
}

function endOfDay(d: Date): Date {
  const x = new Date(d);
  x.setHours(23, 59, 59, 999);
  return x;
}

```
