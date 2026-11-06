# Thư viện: `vat-inbound-product-code.ts`

**Mô tả:** [Hóa đơn đầu vào] vat-inbound-product-code.ts — initialsFromVatName, vatLinePriceThousands, buildAutoInternalCodeBase, buildAutoInternalCodeDuplicate.

**Chủ đề:** [Hóa đơn đầu vào](../../chuyen-de/hoa-don-dau-vao/)

**Mã nguồn Shop:** `artifacts/api-server/src/lib/vat-inbound-product-code.ts` · **Quy mô:** ~33 dòng

File này là **tra cứu** khi đã đọc hub chủ đề và module API tương ứng. Thuật toán đầy đủ nằm trong mã TypeScript gốc.

## Hàm/hằng export (4)

- `initialsFromVatName`
- `vatLinePriceThousands`
- `buildAutoInternalCodeBase`
- `buildAutoInternalCodeDuplicate`

## Trích mã (tham khảo)

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

← [Chỉ mục lib](../../chi-muc/thu-vien-backend/) · [Hub Hóa đơn đầu vào](../../chuyen-de/hoa-don-dau-vao/)
