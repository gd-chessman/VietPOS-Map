# Thư viện: `vat-invoice-buyer-email.ts`

**Mô tả:** [Hóa đơn bán ra] vat-invoice-buyer-email.ts — deliverVatInvoiceEmailToBuyer.

**Chủ đề:** [Hóa đơn bán ra](../../chuyen-de/hoa-don-ban-ra/)

**Mã nguồn Shop:** `artifacts/api-server/src/lib/vat-invoice-buyer-email.ts` · **Quy mô:** ~50 dòng

File này là **tra cứu** khi đã đọc hub chủ đề và module API tương ứng. Thuật toán đầy đủ nằm trong mã TypeScript gốc.

## Hàm/hằng export (1)

- `deliverVatInvoiceEmailToBuyer`

## Import cơ sở dữ liệu

- `import type { ordersTable } from "@workspace/db";`

## Trích mã (tham khảo)

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
  await sendVatInvoiceBuyerEmail(
    {
      to,
      buyerCompanyName: order.buyerCompanyName,
      shopName: shopName.trim() || "Cửa hàng",
      invoiceNo,
      orderCode: order.invoiceCode?.trim() || `#${order.id}`,
      reservationCode: order.einvoiceReservationCode,
      totalAmount: Number.isFinite(total) ? total : 0,
      pdf,
```

← [Chỉ mục lib](../../chi-muc/thu-vien-backend/) · [Hub Hóa đơn bán ra](../../chuyen-de/hoa-don-ban-ra/)
