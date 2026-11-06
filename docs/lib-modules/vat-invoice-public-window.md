# Lib: `vat-invoice-public-window.ts`

**Mô tả:** Logic backend vat-invoice-public-window.ts (~22 dòng) — export: VAT_INVOICE_PUBLIC_EDIT_WINDOW_MS, orderPurchaseAt, vatInvoiceEditDeadline, isVatInvoicePublicEditable.

**Source Shop:** `artifacts/api-server/src/lib/vat-invoice-public-window.ts`

**Độ lớn:** ~22 dòng.

Thư viện backend dùng chung giữa nhiều route handler — đọc file gốc để biết thuật toán đầy đủ.

## Export (4 symbol)

- `VAT_INVOICE_PUBLIC_EDIT_WINDOW_MS`
- `orderPurchaseAt`
- `vatInvoiceEditDeadline`
- `isVatInvoicePublicEditable`

## Xem trước đầu file

```typescript
/** Khách được điền / sửa thông tin xuất HĐ điện tử trong 2 giờ sau khi mua. */
export const VAT_INVOICE_PUBLIC_EDIT_WINDOW_MS = 2 * 60 * 60 * 1000;

export function orderPurchaseAt(order: { clientCreatedAt: Date | null; createdAt: Date }): Date {
  return order.clientCreatedAt ?? order.createdAt;
}

export function vatInvoiceEditDeadline(order: { clientCreatedAt: Date | null; createdAt: Date }): Date {
  return new Date(orderPurchaseAt(order).getTime() + VAT_INVOICE_PUBLIC_EDIT_WINDOW_MS);
}

export function isVatInvoicePublicEditable(order: {
  clientCreatedAt: Date | null;
  createdAt: Date;
  invoiceIssuedAt: Date | null;
  status: string;
}): boolean {
  if (order.invoiceIssuedAt) return false;
  if (order.status === "cancelled" || order.status === "refunded") return false;
  return Date.now() <= vatInvoiceEditDeadline(order).getTime();
}
```
