# Thư viện: `vat-inbound-excluded.ts`

**Mô tả:** [Hóa đơn đầu vào] vat-inbound-excluded.ts — listExcludedLineIndexes.

**Chủ đề:** [Hóa đơn đầu vào](../../chuyen-de/hoa-don-dau-vao/)

**Mã nguồn Shop:** `artifacts/api-server/src/lib/vat-inbound-excluded.ts` · **Quy mô:** ~47 dòng

File này là **tra cứu** khi đã đọc hub chủ đề và module API tương ứng. Thuật toán đầy đủ nằm trong mã TypeScript gốc.

## Hàm/hằng export (1)

- `listExcludedLineIndexes`

## Import cơ sở dữ liệu

- `import type { VatInboundLineItem, VatInboundStockLine } from "@workspace/db";`

## Trích mã (tham khảo)

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
    const name = items[idx]?.name?.trim().toLowerCase() ?? "";
    if (!name) continue;
    const matched = stockLines.some((l) => {
      if (l.lineIndex != null && l.lineIndex === idx) return true;
      const vn = (l.vatName ?? l.productName ?? "").trim().toLowerCase();
      return vn === name;
    });
    if (matched) included.add(idx);
  }
  return stockable.filter((i) => !included.has(i));
```

← [Chỉ mục lib](../../chi-muc/thu-vien-backend/) · [Hub Hóa đơn đầu vào](../../chuyen-de/hoa-don-dau-vao/)
