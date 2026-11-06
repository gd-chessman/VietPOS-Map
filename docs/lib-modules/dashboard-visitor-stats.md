# Lib: `dashboard-visitor-stats.ts`

**Mô tả:** Logic backend dashboard-visitor-stats.ts (~240 dòng) — export: visitDateString, visitorsPerBuyer, sumVisitorsForShopOnDate, visitorsByShopOnDate, sumVisitorsForShopsOnDate, ….

**Source Shop:** `artifacts/api-server/src/lib/dashboard-visitor-stats.ts`

**Độ lớn:** ~240 dòng.

Thư viện backend dùng chung giữa nhiều route handler — đọc file gốc để biết thuật toán đầy đủ.

## Export (12 symbol)

- `visitDateString`
- `visitorsPerBuyer`
- `sumVisitorsForShopOnDate`
- `visitorsByShopOnDate`
- `sumVisitorsForShopsOnDate`
- `sumVisitorsForChainScopeOnDate`
- `visitDateRangeFromChartBuckets`
- `sumVisitorsForShopBetweenVisitDates`
- `visitorsGroupedByVisitDateForShop`
- `visitorsGroupedByVisitDateForChainScope`
- `sumVisitorsForChartBucket`
- `sumVisitorsForChainScopeBetweenVisitDates`

## Import DB / schema

- `import { db, shopDailyVisitorCountsTable } from "@workspace/db";`

## Xem trước đầu file

```typescript
import { db, shopDailyVisitorCountsTable } from "@workspace/db";
import { and, eq, gte, inArray, lte, sql } from "drizzle-orm";
import type { ChainShopScope } from "./chain-shop-scope";
import { effectiveShopIds } from "./chain-shop-scope";
import { vnCalendarDay } from "./vietnam-calendar";

export function visitDateString(d = new Date()): string {
  return vnCalendarDay(d);
}

export function visitorsPerBuyer(visitors: number, completedOrders: number): number | null {
  if (completedOrders <= 0) return null;
  return Math.round((visitors / completedOrders) * 100) / 100;
}

export async function sumVisitorsForShopOnDate(shopId: number, visitDate: string): Promise<number> {
  const [row] = await db
    .select({ total: shopDailyVisitorCountsTable.visitorCount })
    .from(shopDailyVisitorCountsTable)
    .where(
      and(
        eq(shopDailyVisitorCountsTable.shopId, shopId),
        eq(shopDailyVisitorCountsTable.visitDate, visitDate),
      ),
    );
  return Number(row?.total ?? 0);
}

/** Khách vào theo từng shop trong một ngày `visit_date`. */
export async function visitorsByShopOnDate(shopIds: number[], visitDate: string): Promise<Map<number, number>> {
  const map = new Map<number, number>();
  if (shopIds.length === 0) return map;
  const rows = await db
    .select({
      shopId: shopDailyVisitorCountsTable.shopId,
```
