# Lib: `vat-inbound-marked-mst-backfill.ts`

**Mô tả:** Logic backend vat-inbound-marked-mst-backfill.ts (~50 dòng) — export: backfillVatInboundArchiveByMarkedMst.

**Source Shop:** `artifacts/api-server/src/lib/vat-inbound-marked-mst-backfill.ts`

**Độ lớn:** ~50 dòng.

Thư viện backend dùng chung giữa nhiều route handler — đọc file gốc để biết thuật toán đầy đủ.

## Export (1 symbol)

- `backfillVatInboundArchiveByMarkedMst`

## Import DB / schema

- `import { db, organizationsTable, shopsTable, vatInboundInvoicesTable } from "@workspace/db";`

## Xem trước đầu file

```typescript
import { db, organizationsTable, shopsTable, vatInboundInvoicesTable } from "@workspace/db";
import { and, eq, inArray, isNull } from "drizzle-orm";
import {
  parseVatInboundAutoArchiveTaxCodes,
  vatInboundShouldAutoArchiveByMarkedMst,
} from "./vat-inbound-auto-archive-mst";

/** Áp danh sách MST đánh dấu lên mọi HĐ đầu vào cũ của tổ chức (chưa lưu trữ). */
export async function backfillVatInboundArchiveByMarkedMst(orgId: number): Promise<number> {
  const [org] = await db
    .select({ vatInboundAutoArchiveTaxCodes: organizationsTable.vatInboundAutoArchiveTaxCodes })
    .from(organizationsTable)
    .where(eq(organizationsTable.id, orgId))
    .limit(1);
  const marked = parseVatInboundAutoArchiveTaxCodes(org?.vatInboundAutoArchiveTaxCodes);
  if (marked.size === 0) return 0;

  const shopRows = await db
    .select({ id: shopsTable.id })
    .from(shopsTable)
    .where(eq(shopsTable.organizationId, orgId));
  const shopIds = shopRows.map((s) => s.id);
  if (shopIds.length === 0) return 0;

  const rows = await db
    .select({
      id: vatInboundInvoicesTable.id,
      sellerTaxCode: vatInboundInvoicesTable.sellerTaxCode,
      buyerTaxCode: vatInboundInvoicesTable.buyerTaxCode,
    })
    .from(vatInboundInvoicesTable)
    .where(and(inArray(vatInboundInvoicesTable.shopId, shopIds), isNull(vatInboundInvoicesTable.archivedAt)));

  const ids: number[] = [];
  for (const row of rows) {
```
