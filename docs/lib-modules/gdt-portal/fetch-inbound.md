# Lib: `gdt-portal/fetch-inbound.ts`

**Mô tả:** Logic backend gdt-portal/fetch-inbound.ts (~106 dòng) — export: fetchGdtInboundInvoices.

**Source Shop:** `artifacts/api-server/src/lib/gdt-portal/fetch-inbound.ts`

**Độ lớn:** ~106 dòng.

Thư viện backend dùng chung giữa nhiều route handler — đọc file gốc để biết thuật toán đầy đủ.

## Export (1 symbol)

- `fetchGdtInboundInvoices`

## Xem trước đầu file

```typescript
import { loadGdtPortalClientForOrg } from "./org-session";
import { applyGdtDetailToMapped, mapGdtPurchaseRow } from "./map-inbound";
import { lineItemsFromExportXmlBytes } from "./export-xml";
import type { MappedInboundInvoice } from "../viettel-sinvoice/search-inbound";
import { logger } from "../logger";

/** Số HĐ enrich song song (detail/XML) — tránh WAF CQT khi quá cao. */
const ENRICH_CONCURRENCY = 4;

async function mapWithConcurrency<T, R>(
  items: T[],
  concurrency: number,
  fn: (item: T, index: number) => Promise<R>,
): Promise<R[]> {
  if (items.length === 0) return [];
  const results = new Array<R>(items.length);
  let nextIndex = 0;
  const workers = Array.from({ length: Math.min(concurrency, items.length) }, async () => {
    while (true) {
      const i = nextIndex++;
      if (i >= items.length) break;
      results[i] = await fn(items[i]!, i);
    }
  });
  await Promise.all(workers);
  return results;
}

function invoiceKeysFromRow(row: Record<string, unknown>): {
  nbmst: string;
  khhdon: string;
  shdon: string;
  khmshdon: string;
} | null {
  const nbmst = String(row.nbmst ?? "").trim();
```
