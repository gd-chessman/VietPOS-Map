# Lib: `report-sales-staff-performance.ts`

**Mô tả:** Logic backend report-sales-staff-performance.ts (~172 dòng) — export: buildSalesStaffPerformanceReport.

**Source Shop:** `artifacts/api-server/src/lib/report-sales-staff-performance.ts`

**Độ lớn:** ~172 dòng.

Thư viện backend dùng chung giữa nhiều route handler — đọc file gốc để biết thuật toán đầy đủ.

## Export (1 symbol)

- `buildSalesStaffPerformanceReport`

## Import DB / schema

- `} from "@workspace/db";`

## Xem trước đầu file

```typescript
import {
  db,
  ordersTable,
  salesStaffTable,
  shiftSessionStaffTable,
} from "@workspace/db";
import { and, count, eq, gte, inArray, isNotNull, lte, sql } from "drizzle-orm";
import type { AuthPayload } from "../middlewares/auth";
import { canViewPosAuditReports } from "../middlewares/auth";
import {
  effectiveShopIds,
  isMultiShopView,
  loadShopNameMap,
  resolveReportShopScope,
  shopIdFilter,
  type ChainShopScope,
} from "./chain-shop-scope";
import { resolveChartAlignedOrderPeriodBounds } from "./vn-order-period";

export type SalesStaffPerformanceInput = {
  shopId?: number;
  period?: string;
  from?: string;
  to?: string;
};

export async function buildSalesStaffPerformanceReport(
  auth: AuthPayload,
  input: SalesStaffPerformanceInput,
) {
  if (!canViewPosAuditReports(auth.role)) {
    throw new Error("Không có quyền xem báo cáo nhân viên bán hàng");
  }
  const scope = await resolveReportShopScope(auth, input.shopId ?? null);
  if (!scope) throw new Error("Không có quyền xem chi nhánh này");
```
