# Lib: `vat-inbound-tax-sync.ts`

**Mô tả:** Logic backend vat-inbound-tax-sync.ts (~400 dòng) — export: syncVatInboundInvoicesFromTax.

**Source Shop:** `artifacts/api-server/src/lib/vat-inbound-tax-sync.ts`

**Độ lớn:** ~400 dòng.

Thư viện backend dùng chung giữa nhiều route handler — đọc file gốc để biết thuật toán đầy đủ.

## Export (1 symbol)

- `syncVatInboundInvoicesFromTax`

## Import DB / schema

- `} from "@workspace/db";`

## Xem trước đầu file

```typescript
import {
  db,
  vatInboundInvoicesTable,
  organizationsTable,
  purchaseOrdersTable,
  type VatInboundInvoiceRow,
  type VatInboundLineItem,
  type VatInboundTaxRow,
} from "@workspace/db";
import { and, desc, eq, sql } from "drizzle-orm";
import { fetchViettelInboundInvoices } from "./viettel-sinvoice/search-inbound";
import { resolveGdtTaxCodeForOrganization } from "./viettel-sinvoice/config";
import { fetchGdtInboundInvoices } from "./gdt-portal/fetch-inbound";
import { gdtCredentialsReady } from "./org-gdt-settings";
import { getGdtSessionPublic, normalizeVatInboundProvider } from "./gdt-portal/org-session";
import { processVatInboundAutoBatch, type VatInboundAutoProcessResult } from "./vat-inbound-auto-process";
import { notifyVatInboundAutoProcessResults } from "./user-notifications";
import {
  parseVatInboundAutoArchiveTaxCodes,
  vatInboundShouldAutoArchiveByMarkedMst,
} from "./vat-inbound-auto-archive-mst";
import { backfillVatInboundArchiveByMarkedMst } from "./vat-inbound-marked-mst-backfill";

type UpsertBody = {
  clientId: string;
  fileName: string;
  importedAt: string | null;
  invoiceDate: string | null;
  invoiceNo: string | null;
  series: string | null;
  templateNo: string | null;
  formCode: string | null;
  sellerName: string | null;
  sellerTaxCode: string | null;
  sellerAddress: string | null;
```
