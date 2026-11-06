# Lib: `order-audit.ts`

**Mô tả:** Logic backend order-audit.ts (~151 dòng) — export: mapAuditLogRow, insertOrderAuditLog, listOrderAuditLogs.

**Source Shop:** `artifacts/api-server/src/lib/order-audit.ts`

**Độ lớn:** ~151 dòng.

Thư viện backend dùng chung giữa nhiều route handler — đọc file gốc để biết thuật toán đầy đủ.

## Export (3 symbol)

- `mapAuditLogRow`
- `insertOrderAuditLog`
- `listOrderAuditLogs`

## Import DB / schema

- `} from "@workspace/db";`

## Xem trước đầu file

```typescript
import {
  db,
  orderAuditLogsTable,
  paymentChangeLogsTable,
  ordersTable,
  usersTable,
  classifyOrderAuditEvent,
  type OrderAuditLogInsert,
  type OrderAuditMetadata,
  type OrderAuditSensitivityLevel,
} from "@workspace/db";
import { eq, desc } from "drizzle-orm";

type DbTx = Parameters<Parameters<typeof db.transaction>[0]>[0];

export type OrderAuditAction = OrderAuditLogInsert["action"];

export function mapAuditLogRow(
  row: {
    id: number;
    action: OrderAuditAction;
    createdAt: Date;
    userName: string | null;
    note: string | null;
    metadata: OrderAuditMetadata | null;
    sensitivityLevel: OrderAuditSensitivityLevel;
    sensitivityLabel: string | null;
    cashImpact: string | null;
  },
): OrderAuditLogRow {
  return {
    id: row.id,
    action: row.action,
    createdAt: row.createdAt.toISOString(),
    userName: row.userName,
```
