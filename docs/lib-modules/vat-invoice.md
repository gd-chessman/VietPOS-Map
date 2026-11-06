# Lib: `vat-invoice.ts`

**Mô tả:** Logic backend vat-invoice.ts (~262 dòng) — export: normalizeTaxCode, isValidTaxCode, isNumericTaxCode, isValidEmail, normalizePhone, ….

**Source Shop:** `artifacts/api-server/src/lib/vat-invoice.ts`

**Độ lớn:** ~262 dòng.

Thư viện backend dùng chung giữa nhiều route handler — đọc file gốc để biết thuật toán đầy đủ.

## Export (18 symbol)

- `normalizeTaxCode`
- `isValidTaxCode`
- `isNumericTaxCode`
- `isValidEmail`
- `normalizePhone`
- `isValidBuyerPhone`
- `validateBuyerInvoice`
- `validateBuyerInvoiceForIssue`
- `RETAIL_BUYER_LEGAL_NAME`
- `validateBuyerInvoiceForConsumerIssue`
- `resolveBuyerForManualIssue`
- `resolveBuyerForRetailAutoIssue`
- `normalizeBuyerInvoiceFields`
- `EINVOICE_ISSUING_TTL_MS`
- `isActivelyIssuing`
- `resolveInvoiceStatus`
- `mapOrderInvoiceFields`
- `invoiceSnapshotFromOrder`

## Xem trước đầu file

```typescript
export type BuyerInvoiceInput = {
  invoiceRequested?: boolean;
  buyerCompanyName?: string;
  buyerTaxCode?: string;
  buyerEmail?: string;
  buyerAddress?: string;
  buyerPhone?: string;
};

export function normalizeTaxCode(raw: string): string {
  return raw.replace(/\s/g, "").toUpperCase();
}

/** Định dạng chuẩn 10 số (hoặc 10-3) — chỉ bắt buộc lúc chính thức "xuất HĐ VAT", không bắt buộc lúc nhập ở POS. */
export function isValidTaxCode(code: string): boolean {
  return /^[0-9]{10}(-[0-9]{3})?$/.test(code);
}

/** Lúc nhập ở POS: không giới hạn độ dài, chỉ cần toàn chữ số. */
export function isNumericTaxCode(code: string): boolean {
  return /^[0-9]+$/.test(code);
}

export function isValidEmail(email: string): boolean {
  return /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email);
}

export function normalizePhone(raw: string): string {
  return raw.replace(/[\s.-]/g, "");
}

export function isValidBuyerPhone(phone: string): boolean {
  const p = normalizePhone(phone);
  return /^(0|\+84)[0-9]{8,10}$/.test(p) || /^[0-9]{9,11}$/.test(p);
}
```
