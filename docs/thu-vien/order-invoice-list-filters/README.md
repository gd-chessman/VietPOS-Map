# Thư viện: `order-invoice-list-filters.ts`

**Mô tả:** [POS & đơn hàng] order-invoice-list-filters.ts — invoiceListFilters.

**Chủ đề:** [POS & đơn hàng](../../chuyen-de/pos-va-don-hang/)

**Mã nguồn Shop:** `artifacts/api-server/src/lib/order-invoice-list-filters.ts` · **Quy mô:** ~45 dòng

File này là **tra cứu** khi đã đọc hub chủ đề và module API tương ứng. Thuật toán đầy đủ nằm trong mã TypeScript gốc.

## Hàm/hằng export (1)

- `invoiceListFilters`

## Import cơ sở dữ liệu

- `import { ordersTable } from "@workspace/db";`

## Trích mã (tham khảo)

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
  }
  if (rawInvoice === "true") {
    return [eq(ordersTable.invoiceRequested, "true")];
  }
  if (rawInvoice === "false") {
    return [eq(ordersTable.invoiceRequested, "false")];
  }
  return [];
}
```

← [Chỉ mục lib](../../chi-muc/thu-vien-backend/) · [Hub POS & đơn hàng](../../chuyen-de/pos-va-don-hang/)
