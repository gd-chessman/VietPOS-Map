# Thư viện: `vat-inbound-audit.ts`

**Mô tả:** [Hóa đơn đầu vào] vat-inbound-audit.ts — insertVatInboundAuditLog, listVatInboundAuditLogs.

**Chủ đề:** [Hóa đơn đầu vào](../../chuyen-de/hoa-don-dau-vao/)

**Mã nguồn Shop:** `artifacts/api-server/src/lib/vat-inbound-audit.ts` · **Quy mô:** ~66 dòng

File này là **tra cứu** khi đã đọc hub chủ đề và module API tương ứng. Thuật toán đầy đủ nằm trong mã TypeScript gốc.

## Hàm/hằng export (2)

- `insertVatInboundAuditLog`
- `listVatInboundAuditLogs`

## Import cơ sở dữ liệu

- `} from "@workspace/db";`

## Trích mã (tham khảo)

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
  createdAt: string;
  userName: string | null;
  note: string | null;
  metadata: VatInboundAuditMetadata | null;
};

export async function listVatInboundAuditLogs(invoiceId: number): Promise<VatInboundAuditLogRow[]> {
  const rows = await db
    .select({
      id: vatInboundAuditLogsTable.id,
```

← [Chỉ mục lib](../../chi-muc/thu-vien-backend/) · [Hub Hóa đơn đầu vào](../../chuyen-de/hoa-don-dau-vao/)
