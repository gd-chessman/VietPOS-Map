# Thư viện: `product-vat.ts`

**Mô tả:** [Sản phẩm & kho] product-vat.ts — DEFAULT_UNIT, DEFAULT_VAT_RATE, DEFAULT_TNCN_RATE, ALLOWED_VAT_RATES, normalizeUnit, ….

**Chủ đề:** [Sản phẩm & kho](../../chuyen-de/san-pham-va-kho/)

**Mã nguồn Shop:** `artifacts/api-server/src/lib/product-vat.ts` · **Quy mô:** ~61 dòng

File này là **tra cứu** khi đã đọc hub chủ đề và module API tương ứng. Thuật toán đầy đủ nằm trong mã TypeScript gốc.

## Hàm/hằng export (9)

- `DEFAULT_UNIT`
- `DEFAULT_VAT_RATE`
- `DEFAULT_TNCN_RATE`
- `ALLOWED_VAT_RATES`
- `normalizeUnit`
- `normalizeVatRate`
- `normalizeTncnRate`
- `vatAmountFromInclusive`
- `parseProductRow`

## Trích mã (tham khảo)

```typescript
export const DEFAULT_UNIT = "Cái";
export const DEFAULT_VAT_RATE = 1;
export const DEFAULT_TNCN_RATE = 0.5;
export const ALLOWED_VAT_RATES = [0, 1, 5, 8, 10] as const;

export function normalizeUnit(unit?: string | null): string {
  const u = unit?.trim();
  return u || DEFAULT_UNIT;
}

export function normalizeVatRate(rate?: number | string | null): number {
  const n = typeof rate === "string" ? parseFloat(rate) : Number(rate);
  if (!Number.isFinite(n)) return DEFAULT_VAT_RATE;
  if (ALLOWED_VAT_RATES.includes(n as (typeof ALLOWED_VAT_RATES)[number])) return n;
  return DEFAULT_VAT_RATE;
}

export function normalizeTncnRate(rate?: number | string | null): number {
  const n = typeof rate === "string" ? parseFloat(rate) : Number(rate);
  if (!Number.isFinite(n) || n < 0) return DEFAULT_TNCN_RATE;
  return Math.min(100, Math.round(n * 100) / 100);
}

export function vatAmountFromInclusive(lineTotal: number, ratePercent: number): number {
  if (ratePercent <= 0) return 0;
  return Math.round((lineTotal * ratePercent) / (100 + ratePercent));
}

export function parseProductRow(p: {
  price: string;
  costPrice: string;
  vatRate: string;
  tncnRate?: string | null;
  unit?: string | null;
  material?: string | null;
  dimensions?: string | null;
  weight?: string | null;
  manufacturer?: string | null;
  supplierId?: number | null;
  category?: string | null;
  categoryId?: number | null;
  [key: string]: unknown;
}, invQty?: number | null, hideCostPrice = false) {
  return {
    ...p,
```

← [Chỉ mục lib](../../chi-muc/thu-vien-backend/) · [Hub Sản phẩm & kho](../../chuyen-de/san-pham-va-kho/)
