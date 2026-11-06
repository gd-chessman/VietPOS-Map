# Lib: `order-discount.ts`

**Mô tả:** Logic backend order-discount.ts (~108 dòng) — export: computeOrderDiscountAmount, fetchDashboardChartOrders, sumCompletedOrderDiscount.

**Source Shop:** `artifacts/api-server/src/lib/order-discount.ts`

**Độ lớn:** ~108 dòng.

Thư viện backend dùng chung giữa nhiều route handler — đọc file gốc để biết thuật toán đầy đủ.

## Export (3 symbol)

- `computeOrderDiscountAmount`
- `fetchDashboardChartOrders`
- `sumCompletedOrderDiscount`

## Import DB / schema

- `import { db, orderItemsTable, ordersTable } from "@workspace/db";`

## Xem trước đầu file

```typescript
import { and, eq, gte, inArray, lt, sql, type SQL } from "drizzle-orm";
import { db, orderItemsTable, ordersTable } from "@workspace/db";

const listSubtotalSelect = sql<string>`COALESCE(SUM(${orderItemsTable.quantity} * (
  CASE
    WHEN ${orderItemsTable.originalPrice} IS NOT NULL
      AND ${orderItemsTable.originalPrice}::numeric > ${orderItemsTable.price}::numeric
    THEN ${orderItemsTable.originalPrice}::numeric
    ELSE ${orderItemsTable.price}::numeric
  END
)), 0)`;

export function computeOrderDiscountAmount(listSubtotal: number, totalAmount: number): number {
  const discount = listSubtotal - totalAmount;
  if (!Number.isFinite(discount) || discount <= 0) return 0;
  return Math.round(discount * 100) / 100;
}

export type DashboardChartOrderRow = {
  totalAmount: number | string;
  status: string;
  paymentMethod: string;
  payments?: unknown;
  createdAt: Date | string;
  discountAmount: number;
};

/** Đơn trong khoảng thời gian biểu đồ — kèm tiền giảm giá (đơn hoàn thành). */
export async function fetchDashboardChartOrders(
  scopeWhere: SQL,
  overallStart: Date,
  overallEnd: Date,
): Promise<DashboardChartOrderRow[]> {
  const rows = await db
    .select({
```
