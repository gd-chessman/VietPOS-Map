# Lib: `viettel-sinvoice/build-payload.ts`

**Mô tả:** Logic backend viettel-sinvoice/build-payload.ts (~198 dòng) — export: mergeOrderLinesByProductForEinvoice, assertEinvoiceCatalogVatNames, buildViettelInvoicePayload.

**Source Shop:** `artifacts/api-server/src/lib/viettel-sinvoice/build-payload.ts`

**Độ lớn:** ~198 dòng.

Thư viện backend dùng chung giữa nhiều route handler — đọc file gốc để biết thuật toán đầy đủ.

## Export (3 symbol)

- `mergeOrderLinesByProductForEinvoice`
- `assertEinvoiceCatalogVatNames`
- `buildViettelInvoicePayload`

## Xem trước đầu file

```typescript
import { vatAmountFromInclusive } from "../product-vat";
import type { ViettelSinvoiceConfig } from "./config";

export type OrderLineForEinvoice = {
  productId: number;
  /** Tên SP gốc (catalog). */
  productRootName: string;
  productName: string;
  /** Chỉ `products.vat_name` — không fallback tên SP khi xuất HĐ. */
  catalogVatName: string | null;
  /** Mã SP gốc (không dùng mã biến thể khi gộp dòng). */
  productInternalCode: string | null;
  internalCode: string | null;
  unit: string;
  vatRate: number;
  quantity: number;
  /** Đơn giá đã gồm VAT (theo dòng đơn). */
  price: number;
};

/** Gộp các dòng cùng productId (nhiều biến thể) → 1 dòng HĐ, đơn giá trung bình có trọng số theo SL. */
export function mergeOrderLinesByProductForEinvoice(items: OrderLineForEinvoice[]): OrderLineForEinvoice[] {
  if (items.length <= 1) return items;

  const productOrder: number[] = [];
  const groups = new Map<number, OrderLineForEinvoice[]>();

  for (const item of items) {
    const id = item.productId;
    if (!groups.has(id)) {
      productOrder.push(id);
      groups.set(id, []);
    }
    groups.get(id)!.push(item);
  }
```
