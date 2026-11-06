# Lib: `vat-inbound-product-code.ts`

**Mô tả:** Logic backend vat-inbound-product-code.ts (~33 dòng) — export: initialsFromVatName, vatLinePriceThousands, buildAutoInternalCodeBase, buildAutoInternalCodeDuplicate.

**Source Shop:** `artifacts/api-server/src/lib/vat-inbound-product-code.ts`

**Độ lớn:** ~33 dòng.

Thư viện backend dùng chung giữa nhiều route handler — đọc file gốc để biết thuật toán đầy đủ.

## Export (4 symbol)

- `initialsFromVatName`
- `vatLinePriceThousands`
- `buildAutoInternalCodeBase`
- `buildAutoInternalCodeDuplicate`

## Xem trước đầu file

```typescript
/** Chữ cái đầu mỗi từ trong tên VAT (giữ Đ/đ). */
export function initialsFromVatName(vatName: string): string {
  return vatName
    .trim()
    .split(/\s+/)
    .filter((w) => w.length > 0)
    .map((w) => w[0]!.toUpperCase())
    .join("")
    .replace(/[^a-zA-Z0-9Đđ]/g, "");
}

/** Đơn giá VND → phần số mã (150.000 → 150). */
export function vatLinePriceThousands(unitPriceVnd: number | null | undefined): number {
  if (unitPriceVnd == null || !Number.isFinite(unitPriceVnd)) return 0;
  return Math.round(unitPriceVnd / 1000);
}

export function buildAutoInternalCodeBase(vatName: string, unitPriceVnd: number | null | undefined): string {
  const prefix = initialsFromVatName(vatName) || "SP";
  const k = vatLinePriceThousands(unitPriceVnd);
  const raw = `${prefix}${k}`;
  const sanitized = raw.replace(/[^a-zA-Z0-9Đđ_-]/g, "");
  return sanitized.slice(0, 40) || `SP${k}`;
}

/** Trùng mã gốc: LS150 → LS150N2, LS150N3… (tránh nhầm biến thể LS150-01). */
export function buildAutoInternalCodeDuplicate(base: string, duplicateIndex: number): string {
  if (duplicateIndex < 2) return base;
  const suffix = `N${duplicateIndex}`;
  const maxBase = Math.max(1, 40 - suffix.length);
  return `${base.slice(0, maxBase)}${suffix}`;
}
```
