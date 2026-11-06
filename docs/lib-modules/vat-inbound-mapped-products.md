# Lib: `vat-inbound-mapped-products.ts`

**Mô tả:** Logic backend vat-inbound-mapped-products.ts (~163 dòng) — export: isVatInvoiceInboundMappedOnlyForShop, INBOUND_MAPPED_NO_ELIGIBLE_LINES_MSG, filterProductIdsForInboundMappedIssue, validateOrderForI…

**Source Shop:** `artifacts/api-server/src/lib/vat-inbound-mapped-products.ts`

**Độ lớn:** ~163 dòng.

Thư viện backend dùng chung giữa nhiều route handler — đọc file gốc để biết thuật toán đầy đủ.

## Export (4 symbol)

- `isVatInvoiceInboundMappedOnlyForShop`
- `INBOUND_MAPPED_NO_ELIGIBLE_LINES_MSG`
- `filterProductIdsForInboundMappedIssue`
- `validateOrderForInboundMappedOnlyIssue`

## Import DB / schema

- `} from "@workspace/db";`

## Xem trước đầu file

```typescript
import {
  db,
  orderItemsTable,
  productsTable,
  purchaseOrderItemsTable,
  shopsTable,
  vatInboundInvoicesTable,
  type VatInboundStockLine,
} from "@workspace/db";
import { and, eq, inArray } from "drizzle-orm";
import { getHubShopIdForOrg } from "../middlewares/auth";
import { resolveOrganizationIdForShop } from "./viettel-sinvoice/config";

function normCode(code: string | null | undefined): string | null {
  const t = code?.trim();
  return t ? t.toUpperCase() : null;
}

export async function isVatInvoiceInboundMappedOnlyForShop(shopId: number): Promise<boolean> {
  const [shop] = await db
    .select({ enabled: shopsTable.vatInvoiceInboundMappedOnlyEnabled })
    .from(shopsTable)
    .where(eq(shopsTable.id, shopId));
  return shop?.enabled === true;
}

async function loadInboundMappedLookup(orgId: number): Promise<{
  productIds: Set<number>;
  internalCodes: Set<string>;
}> {
  const hubShopId = await getHubShopIdForOrg(orgId);
  const productIds = new Set<number>();
  const internalCodes = new Set<string>();
  if (hubShopId == null) return { productIds, internalCodes };

```
