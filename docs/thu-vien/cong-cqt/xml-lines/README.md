# Thư viện: `gdt-portal/xml-lines.ts`

**Mô tả:** [Hóa đơn đầu vào] gdt-portal/xml-lines.ts — parseLineItemsFromCqtXml.

**Chủ đề:** [Hóa đơn đầu vào](../../../chuyen-de/hoa-don-dau-vao/)

**Mã nguồn Shop:** `artifacts/api-server/src/lib/gdt-portal/xml-lines.ts` · **Quy mô:** ~46 dòng

File này là **tra cứu** khi đã đọc hub chủ đề và module API tương ứng. Thuật toán đầy đủ nằm trong mã TypeScript gốc.

## Hàm/hằng export (1)

- `parseLineItemsFromCqtXml`

## Import cơ sở dữ liệu

- `import type { VatInboundLineItem } from "@workspace/db";`

## Trích mã (tham khảo)

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
      unit: tagText(block, "DVTinh") ?? tagText(block, "DVT"),
      quantity: parseNum(tagText(block, "SLuong") ?? tagText(block, "SL")),
      unitPrice: parseNum(tagText(block, "DGia")),
      amount: parseNum(tagText(block, "ThTien") ?? tagText(block, "TTien")),
      discount: parseNum(tagText(block, "STCKhau") ?? tagText(block, "TlCKhau")),
      vatRate: formatGdtVatRateLabel(tagText(block, "TSuat") ?? tagText(block, "LTSuat")),
    });
  }
  return lines;
}
```

← [Chỉ mục lib](../../../chi-muc/thu-vien-backend/) · [Hub Hóa đơn đầu vào](../../../chuyen-de/hoa-don-dau-vao/)
