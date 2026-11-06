# Lib: `change-log.ts`

**Mô tả:** Logic backend change-log.ts (~30 dòng) — export: recordProductChange, recordInventoryChange.

**Source Shop:** `artifacts/api-server/src/lib/change-log.ts`

**Độ lớn:** ~30 dòng.

Thư viện backend dùng chung giữa nhiều route handler — đọc file gốc để biết thuật toán đầy đủ.

## Export (2 symbol)

- `recordProductChange`
- `recordInventoryChange`

## Import DB / schema

- `import { db, changeLogTable, productsTable, inventoryTable } from "@workspace/db";`

## Xem trước đầu file

```typescript
import { db, changeLogTable, productsTable, inventoryTable } from "@workspace/db";
import { eq } from "drizzle-orm";

type DbTx = Parameters<Parameters<typeof db.transaction>[0]>[0];

/**
 * Records a product-row change for incremental catalog sync (GET /sync/catalog). A product is
 * visible to its owning shop AND every shop that has an inventory row for it (same rule the
 * full catalog pull uses), so the change must fan out to all of those shops — not just the
 * owner — otherwise a branch shop's incremental pull would silently miss the update.
 */
export async function recordProductChange(tx: DbTx, productId: number, changeType: "upsert" | "delete"): Promise<void> {
  const [product] = await tx.select({ shopId: productsTable.shopId }).from(productsTable).where(eq(productsTable.id, productId));
  const invRows = await tx.select({ shopId: inventoryTable.shopId }).from(inventoryTable).where(eq(inventoryTable.productId, productId));

  const shopIds = new Set<number>();
  if (product?.shopId != null) shopIds.add(product.shopId);
  for (const r of invRows) if (r.shopId != null) shopIds.add(r.shopId);
  if (shopIds.size === 0) return;

  await tx.insert(changeLogTable).values(
    [...shopIds].map((shopId) => ({ shopId, entityType: "product" as const, entityId: productId, changeType })),
  );
}

/** Records a pure inventory-quantity change — only affects the one shop whose inventory row changed. */
export async function recordInventoryChange(tx: DbTx, shopId: number, productId: number): Promise<void> {
  await tx.insert(changeLogTable).values({ shopId, entityType: "inventory" as const, entityId: productId, changeType: "upsert" });
}
```
