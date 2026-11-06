# Thư viện: `gdt-portal/export-xml.ts`

**Mô tả:** [Hóa đơn đầu vào] gdt-portal/export-xml.ts — extractFirstXmlFromExportPayload, lineItemsFromExportXmlBytes.

**Chủ đề:** [Hóa đơn đầu vào](../../../chuyen-de/hoa-don-dau-vao/)

**Mã nguồn Shop:** `artifacts/api-server/src/lib/gdt-portal/export-xml.ts` · **Quy mô:** ~23 dòng

File này là **tra cứu** khi đã đọc hub chủ đề và module API tương ứng. Thuật toán đầy đủ nằm trong mã TypeScript gốc.

## Hàm/hằng export (2)

- `extractFirstXmlFromExportPayload`
- `lineItemsFromExportXmlBytes`

## Import cơ sở dữ liệu

- `import type { VatInboundLineItem } from "@workspace/db";`

## Trích mã (tham khảo)

```typescript
import { unzipSync } from "fflate";
import { parseLineItemsFromCqtXml } from "./xml-lines";
import type { VatInboundLineItem } from "@workspace/db";

export function extractFirstXmlFromExportPayload(raw: Buffer): string {
  if (!raw.length) throw new Error("CQT trả file rỗng (export-xml).");
  if (raw[0] === 0x50 && raw[1] === 0x4b) {
    const files = unzipSync(new Uint8Array(raw));
    const names = Object.keys(files).filter((n) => n.toLowerCase().endsWith(".xml"));
    const pick = names[0] ?? Object.keys(files)[0];
    if (!pick) throw new Error("ZIP từ CQT không có file bên trong.");
    return new TextDecoder("utf-8").decode(files[pick]!);
  }
  const text = raw.toString("utf-8").replace(/^\uFEFF/, "").trimStart();
  if (text.startsWith("<")) return text;
  throw new Error("Phản hồi export-xml không phải ZIP/XML.");
}

export function lineItemsFromExportXmlBytes(raw: Buffer): VatInboundLineItem[] {
  const xml = extractFirstXmlFromExportPayload(raw);
  return parseLineItemsFromCqtXml(xml);
}
```

← [Chỉ mục lib](../../../chi-muc/thu-vien-backend/) · [Hub Hóa đơn đầu vào](../../../chuyen-de/hoa-don-dau-vao/)
