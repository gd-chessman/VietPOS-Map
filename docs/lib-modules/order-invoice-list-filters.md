# Lib: `order-invoice-list-filters.ts`

**Mô tả:** Logic backend order-invoice-list-filters.ts (~45 dòng) — export: invoiceListFilters.

**Source Shop:** `artifacts/api-server/src/lib/order-invoice-list-filters.ts`

**Độ lớn:** ~45 dòng.

Thư viện backend dùng chung giữa nhiều route handler — đọc file gốc để biết thuật toán đầy đủ.

## Export (1 symbol)

- `invoiceListFilters`

## Import DB / schema

- `import { ordersTable } from "@workspace/db";`

## Xem trước đầu file

```typescript
import { ordersTable } from "@workspace/db";
import { eq, isNull, isNotNull, sql, type SQL } from "drizzle-orm";

export function invoiceListFilters(
  rawInvoiceStatus: string | null,
  rawInvoice: string | null,
): SQL[] {
  if (rawInvoiceStatus === "pending") {
    return [
      eq(ordersTable.invoiceRequested, "true"),
      isNull(ordersTable.invoiceIssuedAt),
      sql`(${ordersTable.einvoiceIssueError} IS NULL OR BTRIM(${ordersTable.einvoiceIssueError}) = '')`,
      sql`(${ordersTable.einvoiceIssuingAt} IS NULL OR ${ordersTable.einvoiceIssuingAt} <= NOW() - INTERVAL '10 minutes')`,
    ];
  }
  if (rawInvoiceStatus === "issuing") {
    return [
      eq(ordersTable.invoiceRequested, "true"),
      isNull(ordersTable.invoiceIssuedAt),
      sql`(${ordersTable.einvoiceIssuingAt} IS NOT NULL AND ${ordersTable.einvoiceIssuingAt} > NOW() - INTERVAL '10 minutes')`,
    ];
  }
  if (rawInvoiceStatus === "failed") {
    return [
      eq(ordersTable.invoiceRequested, "true"),
      isNull(ordersTable.invoiceIssuedAt),
      sql`(${ordersTable.einvoiceIssueError} IS NOT NULL AND BTRIM(${ordersTable.einvoiceIssueError}) <> '')`,
      sql`(${ordersTable.einvoiceIssuingAt} IS NULL OR ${ordersTable.einvoiceIssuingAt} <= NOW() - INTERVAL '10 minutes')`,
    ];
  }
  if (rawInvoiceStatus === "issued") {
    return [eq(ordersTable.invoiceRequested, "true"), isNotNull(ordersTable.invoiceIssuedAt)];
  }
  if (rawInvoiceStatus === "none") {
    return [eq(ordersTable.invoiceRequested, "false")];
```
