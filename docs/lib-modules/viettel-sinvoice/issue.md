# Lib: `viettel-sinvoice/issue.ts`

**Mô tả:** Logic backend viettel-sinvoice/issue.ts (~308 dòng) — export: issueViettelInvoiceForOrder.

**Source Shop:** `artifacts/api-server/src/lib/viettel-sinvoice/issue.ts`

**Độ lớn:** ~308 dòng.

Thư viện backend dùng chung giữa nhiều route handler — đọc file gốc để biết thuật toán đầy đủ.

## Export (1 symbol)

- `issueViettelInvoiceForOrder`

## Import DB / schema

- `import { db, orderItemsTable, ordersTable, productsTable, shopsTable } from "@workspace/db";`

## Xem trước đầu file

```typescript
import { randomUUID } from "node:crypto";
import { db, orderItemsTable, ordersTable, productsTable, shopsTable } from "@workspace/db";
import { eq, sql } from "drizzle-orm";
import {
  validateBuyerInvoiceForIssue,
  validateBuyerInvoiceForConsumerIssue,
  resolveBuyerForRetailAutoIssue,
  resolveBuyerForManualIssue,
  RETAIL_BUYER_LEGAL_NAME,
  isActivelyIssuing,
} from "../vat-invoice";
import { getViettelSinvoiceConfig, resolveOrganizationIdForShop, viettelConfigErrorMessage } from "./config";
import {
  createViettelInvoice,
  searchViettelInvoiceByTransactionUuid,
  sleep,
} from "./client";
import { buildViettelInvoicePayload } from "./build-payload";
import { deliverVatInvoiceEmailToBuyer } from "../vat-invoice-buyer-email";
import { logger } from "../logger";
import { recordEmailSystemFailure, recordVatSystemEvent } from "../system-event-log";
import {
  notifyVatInvoiceFailed,
  notifyVatInvoiceIssued,
  scheduleNotification,
} from "../user-notifications";
import {
  filterProductIdsForInboundMappedIssue,
  INBOUND_MAPPED_NO_ELIGIBLE_LINES_MSG,
  isVatInvoiceInboundMappedOnlyForShop,
} from "../vat-inbound-mapped-products";

export type ViettelIssueResult = {
  transactionUuid: string;
  invoiceNo: string | null;
```
