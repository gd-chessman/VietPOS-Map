# Thư viện: `order-invoice-code.ts`

**Mô tả:** [POS & đơn hàng] order-invoice-code.ts — normalizeShopCode, formatOrderInvoiceCode, unpadOrderInvoiceCode, formatOrderStt.

**Chủ đề:** [POS & đơn hàng](../../chuyen-de/pos-va-don-hang/)

**Mã nguồn Shop:** `artifacts/api-server/src/lib/order-invoice-code.ts` · **Quy mô:** ~33 dòng

File này là **tra cứu** khi đã đọc hub chủ đề và module API tương ứng. Thuật toán đầy đủ nằm trong mã TypeScript gốc.

## Hàm/hằng export (4)

- `normalizeShopCode`
- `formatOrderInvoiceCode`
- `unpadOrderInvoiceCode`
- `formatOrderStt`

## Trích mã (tham khảo)

```typescript
/** Chuẩn hoá mã cửa hàng dùng làm prefix số HĐ POS. */
export function normalizeShopCode(code?: string | null): string {
  return (
    (code ?? "")
      .trim()
      .toUpperCase()
      .replace(/[^A-Z0-9]/g, "")
      .slice(0, 12) || "POS"
  );
}

/** Số HĐ POS: mã cửa hàng + STT trong shop, vd. HN01-42 */
export function formatOrderInvoiceCode(shopCode: string | null | undefined, shopSequence: number): string {
  if (!Number.isFinite(shopSequence) || shopSequence <= 0) return "";
  return `${normalizeShopCode(shopCode)}-${Math.floor(shopSequence)}`;
}

/** Bỏ pad 0 ở phần id: SHOP1-001103 → SHOP1-1103 */
export function unpadOrderInvoiceCode(code: string): string {
  const trimmed = code.trim();
  const i = trimmed.lastIndexOf("-");
  if (i <= 0) return trimmed;
  const n = Number(trimmed.slice(i + 1));
  if (!Number.isFinite(n) || n <= 0) return trimmed;
  return `${trimmed.slice(0, i)}-${Math.floor(n)}`;
}

/** STT đơn trong cửa hàng (vd. 42). */
export function formatOrderStt(shopSequence: number): string {
  if (!Number.isFinite(shopSequence) || shopSequence <= 0) return "—";
  return String(Math.floor(shopSequence));
}
```

← [Chỉ mục lib](../../chi-muc/thu-vien-backend/) · [Hub POS & đơn hàng](../../chuyen-de/pos-va-don-hang/)
