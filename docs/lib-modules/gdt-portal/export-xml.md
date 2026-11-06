# Lib: `gdt-portal/export-xml.ts`

**Mô tả:** Logic backend gdt-portal/export-xml.ts (~23 dòng) — export: extractFirstXmlFromExportPayload, lineItemsFromExportXmlBytes.

**Source Shop:** `artifacts/api-server/src/lib/gdt-portal/export-xml.ts`

**Độ lớn:** ~23 dòng.

Thư viện backend dùng chung giữa nhiều route handler — đọc file gốc để biết thuật toán đầy đủ.

## Export (2 symbol)

- `extractFirstXmlFromExportPayload`
- `lineItemsFromExportXmlBytes`

## Import DB / schema

- `import type { VatInboundLineItem } from "@workspace/db";`

## Xem trước đầu file

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
