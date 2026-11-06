# Lib: `product-audit.ts`

**Mô tả:** Logic backend product-audit.ts (~63 dòng) — export: recordProductAudit, buildProductFieldChanges.

**Source Shop:** `artifacts/api-server/src/lib/product-audit.ts`

**Độ lớn:** ~63 dòng.

Thư viện backend dùng chung giữa nhiều route handler — đọc file gốc để biết thuật toán đầy đủ.

## Export (2 symbol)

- `recordProductAudit`
- `buildProductFieldChanges`

## Import DB / schema

- `import { db, productAuditLogsTable, type Product, type ProductAuditFieldChange } from "@workspace/db";`

## Xem trước đầu file

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
```
