# Lib: `vat-inbound-auto-process.ts`

**Mô tả:** Logic backend vat-inbound-auto-process.ts (~563 dòng) — export: invoiceEligibleForAutoMap, processVatInboundAutoForInvoice, processVatInboundAutoBatch.

**Source Shop:** `artifacts/api-server/src/lib/vat-inbound-auto-process.ts`

**Độ lớn:** ~563 dòng.

Thư viện backend dùng chung giữa nhiều route handler — đọc file gốc để biết thuật toán đầy đủ.

## Export (3 symbol)

- `invoiceEligibleForAutoMap`
- `processVatInboundAutoForInvoice`
- `processVatInboundAutoBatch`

## Import DB / schema

- `} from "@workspace/db";`

## Xem trước đầu file

```typescript
import {
  db,
  inventoryTable,
  productsTable,
  organizationsTable,
  shopsTable,
  suppliersTable,
  vatInboundInvoicesTable,
  type VatInboundInvoiceRow,
  type VatInboundLineItem,
  type VatInboundStockLine,
  type VatInboundStockStatus,
} from "@workspace/db";
import { and, eq, sql } from "drizzle-orm";
import { recordInventoryChange, recordProductChange } from "./change-log";
import { recordProductAudit } from "./product-audit";
import { applyInvoiceInventoryReceive } from "./inbound-stock-receive";
import { insertVatInboundAuditLog } from "./vat-inbound-audit";
import { normalizeUnit, normalizeVatRate } from "./product-vat";
import { assertUniqueSupplierVatName, findSupplierVatNameConflict, normalizeVatNameKey } from "./product-vat-name";
import { ensureVariant0 } from "./product-variants";
import { buildAutoInternalCodeBase, buildAutoInternalCodeDuplicate } from "./vat-inbound-product-code";
import { logger } from "./logger";

type DbTx = Parameters<Parameters<typeof db.transaction>[0]>[0];

export type VatInboundAutoProcessResult = {
  invoiceId: number;
  invoiceLabel: string;
  mapped: boolean;
  received: boolean;
  linesMapped: number;
  linesSkipped: number;
  productsCreated: number;
  createdProductCodes: string[];
```
