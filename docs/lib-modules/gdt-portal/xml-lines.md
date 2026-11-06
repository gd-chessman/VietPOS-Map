# Lib: `gdt-portal/xml-lines.ts`

**Mô tả:** Logic backend gdt-portal/xml-lines.ts (~46 dòng) — export: parseLineItemsFromCqtXml.

**Source Shop:** `artifacts/api-server/src/lib/gdt-portal/xml-lines.ts`

**Độ lớn:** ~46 dòng.

Thư viện backend dùng chung giữa nhiều route handler — đọc file gốc để biết thuật toán đầy đủ.

## Export (1 symbol)

- `parseLineItemsFromCqtXml`

## Import DB / schema

- `import type { VatInboundLineItem } from "@workspace/db";`

## Xem trước đầu file

```typescript
import type { VatInboundLineItem } from "@workspace/db";
import { formatGdtVatRateLabel } from "./map-inbound";

function tagText(block: string, localName: string): string | null {
  const re = new RegExp(`<(?:[\\w.-]+:)?${localName}[^>]*>([\\s\\S]*?)<\\/(?:[\\w.-]+:)?${localName}>`, "i");
  const m = re.exec(block);
  if (!m?.[1]) return null;
  const t = m[1].replace(/<[^>]+>/g, "").trim();
  return t.length ? t : null;
}

function parseNum(raw: string | null): number | null {
  if (!raw) return null;
  const n = Number(raw.replace(/,/g, "").trim());
  return Number.isFinite(n) ? n : null;
}

/** Dòng hàng từ XML HĐĐT (HHDVu / THHDVu …). */
export function parseLineItemsFromCqtXml(xml: string): VatInboundLineItem[] {
  const lines: VatInboundLineItem[] = [];
  const re = /<(?:[\w.-]+:)?HHDVu\b[^>]*>([\s\S]*?)<\/(?:[\w.-]+:)?HHDVu>/gi;
  let m: RegExpExecArray | null;
  let idx = 0;
  while ((m = re.exec(xml)) !== null) {
    const block = m[1] ?? "";
    const name =
      tagText(block, "THHDVu")
      ?? tagText(block, "Ten")
      ?? tagText(block, "TenHHDVu")
      ?? "";
    if (!name) continue;
    idx++;
    lines.push({
      lineNo: parseNum(tagText(block, "STT")) ?? idx,
      name,
```
