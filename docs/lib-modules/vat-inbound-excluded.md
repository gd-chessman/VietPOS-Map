# Lib: `vat-inbound-excluded.ts`

**Mô tả:** Logic backend vat-inbound-excluded.ts (~47 dòng) — export: listExcludedLineIndexes.

**Source Shop:** `artifacts/api-server/src/lib/vat-inbound-excluded.ts`

**Độ lớn:** ~47 dòng.

Thư viện backend dùng chung giữa nhiều route handler — đọc file gốc để biết thuật toán đầy đủ.

## Export (1 symbol)

- `listExcludedLineIndexes`

## Import DB / schema

- `import type { VatInboundLineItem, VatInboundStockLine } from "@workspace/db";`

## Xem trước đầu file

```typescript
import type { VatInboundLineItem, VatInboundStockLine } from "@workspace/db";

function isNonStockVatLine(name: string | null | undefined): boolean {
  const n = (name ?? "").normalize("NFC").replace(/\s+/g, " ").trim();
  if (!n) return false;
  return /phí\s*(dịch vụ|thanh toán|giao dịch|chuyển khoản|cổng thanh toán)/i.test(n);
}

function stockableVatLineIndexes(lineItems: VatInboundLineItem[]): number[] {
  const out: number[] = [];
  lineItems.forEach((it, i) => {
    if (it.name?.trim() && !isNonStockVatLine(it.name)) out.push(i);
  });
  return out;
}

export function listExcludedLineIndexes(input: {
  lineItems: VatInboundLineItem[];
  stockLines: VatInboundStockLine[] | null | undefined;
  stockExcludedLineIndexes: number[] | null | undefined;
  stockExcludedLinesDismissedAt: Date | null | undefined;
  stockStatus: string | null | undefined;
}): number[] {
  if (input.stockExcludedLinesDismissedAt) return [];
  const stored = input.stockExcludedLineIndexes;
  if (stored?.length) return [...stored].sort((a, b) => a - b);
  /** Khớp POS: `null` = không suy đoán (tránh ghép thiếu sai khi chưa lưu index). */
  if (stored === null) return [];
  if (!input.stockStatus) return [];
  const items = input.lineItems ?? [];
  const stockable = stockableVatLineIndexes(items);
  if (!stockable.length) return [];
  const stockLines = input.stockLines ?? [];
  const included = new Set<number>();
  for (const idx of stockable) {
```
