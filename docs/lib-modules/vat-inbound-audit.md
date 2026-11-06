# Lib: `vat-inbound-audit.ts`

**Mô tả:** Logic backend vat-inbound-audit.ts (~66 dòng) — export: insertVatInboundAuditLog, listVatInboundAuditLogs.

**Source Shop:** `artifacts/api-server/src/lib/vat-inbound-audit.ts`

**Độ lớn:** ~66 dòng.

Thư viện backend dùng chung giữa nhiều route handler — đọc file gốc để biết thuật toán đầy đủ.

## Export (2 symbol)

- `insertVatInboundAuditLog`
- `listVatInboundAuditLogs`

## Import DB / schema

- `} from "@workspace/db";`

## Xem trước đầu file

```typescript
import {
  db,
  vatInboundAuditLogsTable,
  usersTable,
  type VatInboundAuditAction,
  type VatInboundAuditMetadata,
} from "@workspace/db";
import { asc, eq } from "drizzle-orm";

type DbTx = Parameters<Parameters<typeof db.transaction>[0]>[0];

export async function insertVatInboundAuditLog(
  tx: DbTx,
  entry: {
    invoiceId: number;
    shopId: number;
    userId: number;
    action: VatInboundAuditAction;
    note?: string | null;
    metadata?: VatInboundAuditMetadata | null;
  },
): Promise<void> {
  await tx.insert(vatInboundAuditLogsTable).values({
    invoiceId: entry.invoiceId,
    shopId: entry.shopId,
    userId: entry.userId,
    action: entry.action,
    note: entry.note?.trim() || null,
    metadata: entry.metadata ?? null,
  });
}

export type VatInboundAuditLogRow = {
  id: number;
  action: VatInboundAuditAction;
```
