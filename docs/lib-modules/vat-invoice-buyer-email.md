# Lib: `vat-invoice-buyer-email.ts`

**Mô tả:** Logic backend vat-invoice-buyer-email.ts (~50 dòng) — export: deliverVatInvoiceEmailToBuyer.

**Source Shop:** `artifacts/api-server/src/lib/vat-invoice-buyer-email.ts`

**Độ lớn:** ~50 dòng.

Thư viện backend dùng chung giữa nhiều route handler — đọc file gốc để biết thuật toán đầy đủ.

## Export (1 symbol)

- `deliverVatInvoiceEmailToBuyer`

## Import DB / schema

- `import type { ordersTable } from "@workspace/db";`

## Xem trước đầu file

```typescript
import type { ordersTable } from "@workspace/db";
import { sendVatInvoiceBuyerEmail } from "../email";
import { logger } from "./logger";
import { fetchViettelInvoicePdfForOrder } from "./viettel-sinvoice/download-pdf";
import { sleep } from "./viettel-sinvoice/client";

/**
 * Gửi HĐĐT cho người mua qua SMTP tổ chức (hoặc .env dự phòng).
 * Không phụ thuộc cấu hình email trên cổng S-Invoice.
 */
export async function deliverVatInvoiceEmailToBuyer(
  order: typeof ordersTable.$inferSelect,
  shopName: string,
): Promise<void> {
  const to = order.buyerEmail?.trim().toLowerCase();
  if (!to) return;

  const invoiceNo = order.einvoiceInvoiceNo?.trim();
  if (!invoiceNo) {
    throw new Error("Đơn chưa có số hóa đơn điện tử");
  }

  let pdf: { buffer: Buffer; fileName: string } | undefined;
  try {
    await sleep(1500);
    const file = await fetchViettelInvoicePdfForOrder(order);
    pdf = { buffer: file.buffer, fileName: file.fileName };
  } catch (err) {
    logger.warn(
      { orderId: order.id, err: err instanceof Error ? err.message : String(err) },
      "Không tải PDF HĐĐT để đính kèm email — vẫn gửi mail không file",
    );
  }

  const total = Number.parseFloat(String(order.totalAmount));
```
