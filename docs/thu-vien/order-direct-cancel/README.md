# Thư viện: `order-direct-cancel.ts`

**Mô tả:** [POS & đơn hàng] order-direct-cancel.ts — directCancelWithoutRequestSql, sumDirectCancelledInPeriod, directCancelWithoutRequestOrderIds.

**Chủ đề:** [POS & đơn hàng](../../chuyen-de/pos-va-don-hang/)

**Mã nguồn Shop:** `artifacts/api-server/src/lib/order-direct-cancel.ts` · **Quy mô:** ~64 dòng

File này là **tra cứu** khi đã đọc hub chủ đề và module API tương ứng. Thuật toán đầy đủ nằm trong mã TypeScript gốc.

## Hàm/hằng export (3)

- `directCancelWithoutRequestSql`
- `sumDirectCancelledInPeriod`
- `directCancelWithoutRequestOrderIds`

## Import cơ sở dữ liệu

- `import { db, ordersTable, orderAuditLogsTable } from "@workspace/db";`

## Trích mã (tham khảo)

```typescript
import { db, ordersTable, orderAuditLogsTable } from "@workspace/db";
import { and, eq, inArray, sql, type SQL } from "drizzle-orm";

/** Đơn huỷ trực tiếp (audit `cancel`) — không từng có `cancel_request`. */
export function directCancelWithoutRequestSql(): SQL {
  return sql`EXISTS (
    SELECT 1 FROM ${orderAuditLogsTable} l
    WHERE l.order_id = ${ordersTable.id} AND l.action = 'cancel'
  ) AND NOT EXISTS (
    SELECT 1 FROM ${orderAuditLogsTable} l
    WHERE l.order_id = ${ordersTable.id} AND l.action = 'cancel_request'
  )`;
}

export async function sumDirectCancelledInPeriod(
  baseConditions: SQL[],
): Promise<{ count: number; revenue: number }> {
  const conditions: SQL[] = [
    ...baseConditions,
    eq(ordersTable.status, "cancelled"),
    directCancelWithoutRequestSql(),
  ];
  const [row] = await db
    .select({
      count: sql<number>`COUNT(*)`,
      revenue: sql<string>`COALESCE(SUM(${ordersTable.totalAmount}), 0)`,
    })
    .from(ordersTable)
    .where(and(...conditions));
  return {
    count: Number(row?.count ?? 0),
    revenue: parseFloat(row?.revenue ?? "0"),
  };
}

/** Batch: đơn huỷ không qua đề nghị (theo audit). */
export async function directCancelWithoutRequestOrderIds(orderIds: number[]): Promise<Set<number>> {
  if (orderIds.length === 0) return new Set();

  const withCancel = await db
    .select({ orderId: orderAuditLogsTable.orderId })
    .from(orderAuditLogsTable)
    .where(
      and(
        inArray(orderAuditLogsTable.orderId, orderIds),
```

← [Chỉ mục lib](../../chi-muc/thu-vien-backend/) · [Hub POS & đơn hàng](../../chuyen-de/pos-va-don-hang/)
