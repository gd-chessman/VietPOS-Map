# Lib: `viettel-sinvoice/search-inbound.ts`

**Mô tả:** Logic backend viettel-sinvoice/search-inbound.ts (~361 dòng) — export: mapViettelInboundInvoice, splitInboundDateRange, isViettelDemoTaxCode, fetchViettelInboundInvoices, assertViettelInboundInvoiceE…

**Source Shop:** `artifacts/api-server/src/lib/viettel-sinvoice/search-inbound.ts`

**Độ lớn:** ~361 dòng.

Thư viện backend dùng chung giữa nhiều route handler — đọc file gốc để biết thuật toán đầy đủ.

## Export (6 symbol)

- `mapViettelInboundInvoice`
- `splitInboundDateRange`
- `isViettelDemoTaxCode`
- `fetchViettelInboundInvoices`
- `assertViettelInboundInvoiceExists`
- `isTaxSyncedVatInboundClientId`

## Import DB / schema

- `import type { VatInboundLineItem, VatInboundTaxRow } from "@workspace/db";`

## Xem trước đầu file

```typescript
import type { VatInboundLineItem, VatInboundTaxRow } from "@workspace/db";
import { getViettelInboundConfig, toGdtPortalTaxCode, viettelInboundConfigErrorMessage } from "./config";
import { searchViettelInboundByTax, type ViettelInboundTaxInvoice } from "./client";

const PAGE_SIZE = 100;
const MAX_PAGES = 50;
const MAX_MONTHS_PER_REQUEST = 3;
const MAX_RANGE_MONTHS = 12;

export type MappedInboundInvoice = {
  clientId: string;
  fileName: string;
  invoiceDate: string | null;
  invoiceNo: string | null;
  series: string | null;
  templateNo: string | null;
  formCode: string | null;
  sellerName: string | null;
  sellerTaxCode: string | null;
  sellerAddress: string | null;
  sellerPhone: string | null;
  sellerBank: string | null;
  buyerName: string | null;
  buyerPersonName: string | null;
  buyerTaxCode: string | null;
  buyerAddress: string | null;
  paymentMethod: string | null;
  currency: string | null;
  exchangeRate: string | null;
  amountUntaxed: number | null;
  taxAmount: number | null;
  feeAmount: number | null;
  commercialDiscount: number | null;
  totalAmount: number | null;
  amountInWords: string | null;
```
