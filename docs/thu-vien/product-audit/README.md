# Thư viện: `product-audit.ts`

**Mô tả:** [Sản phẩm & kho] product-audit.ts — recordProductAudit, buildProductFieldChanges.

**Chủ đề:** [Sản phẩm & kho](../../chuyen-de/san-pham-va-kho/)

**Mã nguồn Shop:** `artifacts/api-server/src/lib/product-audit.ts` · **Quy mô:** ~63 dòng

File này là **tra cứu** khi đã đọc hub chủ đề và module API tương ứng. Thuật toán đầy đủ nằm trong mã TypeScript gốc.

## Hàm/hằng export (2)

- `recordProductAudit`
- `buildProductFieldChanges`

## Import cơ sở dữ liệu

- `import { db, productAuditLogsTable, type Product, type ProductAuditFieldChange } from "@workspace/db";`

## Trích mã (tham khảo)

```typescript
import { db, productAuditLogsTable, type Product, type ProductAuditFieldChange } from "@workspace/db";

type DbTx = Parameters<Parameters<typeof db.transaction>[0]>[0];

export async function recordProductAudit(
  tx: DbTx,
  params: {
    shopId: number;
    productId: number;
    userId: number;
    action: "create" | "update" | "discontinue";
    productName: string;
    productInternalCode?: string | null;
    changes: ProductAuditFieldChange[];
  },
): Promise<void> {
  if (params.action === "update" && params.changes.length === 0) return;
  await tx.insert(productAuditLogsTable).values({
    shopId: params.shopId,
    productId: params.productId,
    userId: params.userId,
    action: params.action,
    productName: params.productName,
    productInternalCode: params.productInternalCode ?? null,
    changes: params.changes,
  });
}

const TEXT_FIELDS = ["name", "englishName", "internalCode", "unit", "dimensions", "weight"] as const;
const NUMERIC_FIELDS = ["price", "costPrice", "vatRate"] as const;

/** Diffs the tracked product fields between the pre-update row and the update payload. Numeric columns come back from Drizzle as strings, so they're compared as numbers to avoid false positives like "10.00" vs 10. */
export function buildProductFieldChanges(
  existing: Product,
  updates: Record<string, unknown>,
): ProductAuditFieldChange[] {
  const out: ProductAuditFieldChange[] = [];

  for (const field of TEXT_FIELDS) {
    if (!(field in updates)) continue;
    const oldValue = (existing[field] as string | null) ?? null;
    const newValue = (updates[field] as string | null) ?? null;
    if (oldValue !== newValue) out.push({ field, oldValue, newValue });
  }

```

← [Chỉ mục lib](../../chi-muc/thu-vien-backend/) · [Hub Sản phẩm & kho](../../chuyen-de/san-pham-va-kho/)
