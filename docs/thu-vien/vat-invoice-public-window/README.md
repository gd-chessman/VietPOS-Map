# Thư viện: `vat-invoice-public-window.ts`

**Mô tả:** [Hóa đơn bán ra] vat-invoice-public-window.ts — VAT_INVOICE_PUBLIC_EDIT_WINDOW_MS, orderPurchaseAt, vatInvoiceEditDeadline, isVatInvoicePublicEditable.

**Chủ đề:** [Hóa đơn bán ra](../../chuyen-de/hoa-don-ban-ra/)

**Mã nguồn Shop:** `artifacts/api-server/src/lib/vat-invoice-public-window.ts` · **Quy mô:** ~22 dòng

File này là **tra cứu** khi đã đọc hub chủ đề và module API tương ứng. Thuật toán đầy đủ nằm trong mã TypeScript gốc.

## Hàm/hằng export (4)

- `VAT_INVOICE_PUBLIC_EDIT_WINDOW_MS`
- `orderPurchaseAt`
- `vatInvoiceEditDeadline`
- `isVatInvoicePublicEditable`

## Trích mã (tham khảo)

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

← [Chỉ mục lib](../../chi-muc/thu-vien-backend/) · [Hub Hóa đơn bán ra](../../chuyen-de/hoa-don-ban-ra/)
