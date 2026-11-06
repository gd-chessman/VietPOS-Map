# Lib: `product-vat.ts`

**Mô tả:** Logic backend product-vat.ts (~61 dòng) — export: DEFAULT_UNIT, DEFAULT_VAT_RATE, DEFAULT_TNCN_RATE, ALLOWED_VAT_RATES, normalizeUnit, ….

**Source Shop:** `artifacts/api-server/src/lib/product-vat.ts`

**Độ lớn:** ~61 dòng.

Thư viện backend dùng chung giữa nhiều route handler — đọc file gốc để biết thuật toán đầy đủ.

## Export (9 symbol)

- `DEFAULT_UNIT`
- `DEFAULT_VAT_RATE`
- `DEFAULT_TNCN_RATE`
- `ALLOWED_VAT_RATES`
- `normalizeUnit`
- `normalizeVatRate`
- `normalizeTncnRate`
- `vatAmountFromInclusive`
- `parseProductRow`

## Xem trước đầu file

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
```
