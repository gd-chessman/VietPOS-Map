# Lib: `viettel-sinvoice/client.ts`

**Mô tả:** Logic backend viettel-sinvoice/client.ts (~489 dòng) — export: isTransientViettelPdfError, createViettelInvoice, searchViettelInvoiceByTransactionUuid, searchViettelInboundByTax, sleep, ….

**Source Shop:** `artifacts/api-server/src/lib/viettel-sinvoice/client.ts`

**Độ lớn:** ~489 dòng.

Thư viện backend dùng chung giữa nhiều route handler — đọc file gốc để biết thuật toán đầy đủ.

## Export (8 symbol)

- `isTransientViettelPdfError`
- `createViettelInvoice`
- `searchViettelInvoiceByTransactionUuid`
- `searchViettelInboundByTax`
- `sleep`
- `downloadViettelInvoiceRepresentationFile`
- `downloadViettelExchangeInvoicePdf`
- `downloadViettelInvoiceFilePortal`

## Xem trước đầu file

```typescript
import type { ViettelAuthConfig, ViettelSinvoiceConfig } from "./config";

const REQUEST_TIMEOUT_MS = 90_000;
const TOKEN_REFRESH_BUFFER_MS = 2 * 60 * 1000;
const TOKEN_FALLBACK_TTL_MS = 10 * 60 * 1000;

type LoginResponse = {
  access_token?: string;
  accessToken?: string;
  token?: string;
  expires_in?: number;
  expiresIn?: number;
  message?: string;
  detail?: string;
  title?: string;
  result?: { access_token?: string; accessToken?: string };
};

type CreateInvoiceResult = {
  supplierTaxCode?: string;
  invoiceNo?: string;
  transactionID?: string | number;
  reservationCode?: string;
  codeOfTax?: string | null;
};

type ViettelEnvelope<T> = {
  errorCode?: string | null;
  description?: string | null;
  code?: number;
  message?: string;
  data?: unknown;
  result?: T;
};

```
