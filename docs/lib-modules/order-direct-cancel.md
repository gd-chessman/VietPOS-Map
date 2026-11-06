# Lib: `order-direct-cancel.ts`

**Mô tả:** Logic backend order-direct-cancel.ts (~64 dòng) — export: directCancelWithoutRequestSql, sumDirectCancelledInPeriod, directCancelWithoutRequestOrderIds.

**Source Shop:** `artifacts/api-server/src/lib/order-direct-cancel.ts`

**Độ lớn:** ~64 dòng.

Thư viện backend dùng chung giữa nhiều route handler — đọc file gốc để biết thuật toán đầy đủ.

## Export (3 symbol)

- `directCancelWithoutRequestSql`
- `sumDirectCancelledInPeriod`
- `directCancelWithoutRequestOrderIds`

## Import DB / schema

- `import { db, ordersTable, orderAuditLogsTable } from "@workspace/db";`

## Xem trước đầu file

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

```
