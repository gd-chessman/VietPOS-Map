# Thư viện: `vat-inbound-marked-mst-backfill.ts`

**Mô tả:** [Hóa đơn đầu vào] vat-inbound-marked-mst-backfill.ts — backfillVatInboundArchiveByMarkedMst.

**Chủ đề:** [Hóa đơn đầu vào](../../chuyen-de/hoa-don-dau-vao/)

**Mã nguồn Shop:** `artifacts/api-server/src/lib/vat-inbound-marked-mst-backfill.ts` · **Quy mô:** ~50 dòng

File này là **tra cứu** khi đã đọc hub chủ đề và module API tương ứng. Thuật toán đầy đủ nằm trong mã TypeScript gốc.

## Hàm/hằng export (1)

- `backfillVatInboundArchiveByMarkedMst`

## Import cơ sở dữ liệu

- `import { db, organizationsTable, shopsTable, vatInboundInvoicesTable } from "@workspace/db";`

## Trích mã (tham khảo)

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
    if (vatInboundShouldAutoArchiveByMarkedMst(row.sellerTaxCode, row.buyerTaxCode, marked)) {
      ids.push(row.id);
    }
  }
  if (ids.length === 0) return 0;

  const now = new Date();
  await db
    .update(vatInboundInvoicesTable)
    .set({ archivedAt: now, updatedAt: now })
```

← [Chỉ mục lib](../../chi-muc/thu-vien-backend/) · [Hub Hóa đơn đầu vào](../../chuyen-de/hoa-don-dau-vao/)
