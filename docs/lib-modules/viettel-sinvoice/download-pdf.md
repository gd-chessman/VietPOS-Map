# Lib: `viettel-sinvoice/download-pdf.ts`

**Mô tả:** Logic backend viettel-sinvoice/download-pdf.ts (~103 dòng) — export: fetchViettelInvoicePdf, fetchViettelInvoicePdfForOrder.

**Source Shop:** `artifacts/api-server/src/lib/viettel-sinvoice/download-pdf.ts`

**Độ lớn:** ~103 dòng.

Thư viện backend dùng chung giữa nhiều route handler — đọc file gốc để biết thuật toán đầy đủ.

## Export (2 symbol)

- `fetchViettelInvoicePdf`
- `fetchViettelInvoicePdfForOrder`

## Import DB / schema

- `import { ordersTable } from "@workspace/db";`

## Xem trước đầu file

```typescript
import { getViettelSinvoiceConfig, resolveOrganizationIdForShop, type ViettelSinvoiceConfig } from "./config";
import {
  downloadViettelExchangeInvoicePdf,
  downloadViettelInvoiceRepresentationFile,
  isTransientViettelPdfError,
  sleep,
} from "./client";
import { ordersTable } from "@workspace/db";

export type ViettelInvoicePdf = {
  buffer: Buffer;
  fileName: string;
  mimeType: string;
};

const PDF_RETRY_DELAYS_MS = [0, 2000];

function isPdfBuffer(buf: Buffer): boolean {
  return buf.length >= 4 && buf.subarray(0, 4).toString("ascii") === "%PDF";
}

async function tryRepresentation(
  config: ViettelSinvoiceConfig,
  input: { invoiceNo: string; templateCode: string; transactionUuid?: string },
): Promise<ViettelInvoicePdf> {
  const file = await downloadViettelInvoiceRepresentationFile(config, {
    invoiceNo: input.invoiceNo,
    templateCode: input.templateCode,
    transactionUuid: input.transactionUuid,
    fileType: "PDF",
  });
  if (!isPdfBuffer(file.buffer)) {
    throw new Error("Viettel trả file không phải PDF");
  }
  return { ...file, mimeType: "application/pdf" };
```
