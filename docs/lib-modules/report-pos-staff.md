# Lib: `report-pos-staff.ts`

**Mô tả:** Logic backend report-pos-staff.ts (~110 dòng) — export: buildPosStaffReport.

**Source Shop:** `artifacts/api-server/src/lib/report-pos-staff.ts`

**Độ lớn:** ~110 dòng.

Thư viện backend dùng chung giữa nhiều route handler — đọc file gốc để biết thuật toán đầy đủ.

## Export (1 symbol)

- `buildPosStaffReport`

## Import DB / schema

- `import { db, ordersTable, reprintLogsTable, usersTable } from "@workspace/db";`

## Xem trước đầu file

```typescript
import { db, ordersTable, reprintLogsTable, usersTable } from "@workspace/db";
import { and, eq, gte, lte } from "drizzle-orm";
import type { AuthPayload } from "../middlewares/auth";
import { canViewPosAuditReports } from "../middlewares/auth";
import {
  isMultiShopView,
  loadShopNameMap,
  resolveReportShopScope,
  shopIdFilter,
} from "./chain-shop-scope";
import { resolveChartAlignedOrderPeriodBounds } from "./vn-order-period";

export type PosStaffReportInput = {
  shopId?: number;
  period?: string;
  from?: string;
  to?: string;
};

/** Hiệu quả tài khoản POS (user đăng nhập bán hàng) — khác NV bán hàng (sales_staff). */
export async function buildPosStaffReport(auth: AuthPayload, input: PosStaffReportInput) {
  if (!canViewPosAuditReports(auth.role)) {
    throw new Error("Không có quyền xem báo cáo nhân viên");
  }
  const scope = await resolveReportShopScope(auth, input.shopId ?? null);
  if (!scope) throw new Error("Không có quyền xem chi nhánh này");

  const bounds = resolveChartAlignedOrderPeriodBounds({
    period: input.period ?? (input.from && input.to ? "range" : "last_week"),
    fromQuery: input.from,
    toQuery: input.to,
  });
  const from = bounds?.start;
  const to = bounds ? new Date(bounds.endExclusive.getTime() - 1) : undefined;

```
