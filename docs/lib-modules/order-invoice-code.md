# Lib: `order-invoice-code.ts`

**Mô tả:** Logic backend order-invoice-code.ts (~33 dòng) — export: normalizeShopCode, formatOrderInvoiceCode, unpadOrderInvoiceCode, formatOrderStt.

**Source Shop:** `artifacts/api-server/src/lib/order-invoice-code.ts`

**Độ lớn:** ~33 dòng.

Thư viện backend dùng chung giữa nhiều route handler — đọc file gốc để biết thuật toán đầy đủ.

## Export (4 symbol)

- `normalizeShopCode`
- `formatOrderInvoiceCode`
- `unpadOrderInvoiceCode`
- `formatOrderStt`

## Xem trước đầu file

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
