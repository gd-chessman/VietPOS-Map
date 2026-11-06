# Lib: `order-list-period-summary.ts`

**Mô tả:** Logic backend order-list-period-summary.ts (~147 dòng) — export: appendOrderListDateFilters, fetchOrderListPeriodSummary.

**Source Shop:** `artifacts/api-server/src/lib/order-list-period-summary.ts`

**Độ lớn:** ~147 dòng.

Thư viện backend dùng chung giữa nhiều route handler — đọc file gốc để biết thuật toán đầy đủ.

## Export (2 symbol)

- `appendOrderListDateFilters`
- `fetchOrderListPeriodSummary`

## Import DB / schema

- `import { db, ordersTable } from "@workspace/db";`

## Xem trước đầu file

```typescript
import { db, ordersTable } from "@workspace/db";
import { and, eq, gte, lte, sql, type SQL } from "drizzle-orm";
import type { AuthPayload } from "../middlewares/auth";
import { isShiftSessionRestrictedRole } from "./shift-sessions";
import { sumCompletedOrderDiscount } from "./order-discount";
import { sumOrdersPaymentRevenue } from "./payment-revenue";
import { orderShopFilter, type OrderListScope } from "./orders-scope";
import { appendVnYmdOrderPeriodFilters, VN_YMD_RE } from "./vn-order-period";
import { sumDirectCancelledInPeriod } from "./order-direct-cancel";

export type OrderListPeriodSummary = {
  completedOrders: number;
  completedRevenue: number;
  cancelRequestedOrders: number;
  cancelRequestedRevenue: number;
  cancelledOrders: number;
  cancelledRevenue: number;
  /** Huỷ trực tiếp (QL/Admin), không qua đề nghị huỷ — theo audit. */
  directCancelledOrders: number;
  directCancelledRevenue: number;
  discountAmount: number;
  discountedOrders: number;
  grandTotal: number;
  actualRevenue: number;
  payment: { cash: number; card: number; transfer: number };
  listLimitPerStatus: number;
};

export function appendOrderListDateFilters(
  auth: AuthPayload,
  conditions: SQL[],
  fromStr?: string,
  toStr?: string,
): void {
  if (isShiftSessionRestrictedRole(auth.role)) {
```
