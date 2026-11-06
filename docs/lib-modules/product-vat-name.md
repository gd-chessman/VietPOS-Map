# Lib: `product-vat-name.ts`

**Mô tả:** Logic backend product-vat-name.ts (~62 dòng) — export: normalizeVatNameKey, findSupplierVatNameConflict, assertUniqueSupplierVatName.

**Source Shop:** `artifacts/api-server/src/lib/product-vat-name.ts`

**Độ lớn:** ~62 dòng.

Thư viện backend dùng chung giữa nhiều route handler — đọc file gốc để biết thuật toán đầy đủ.

## Export (3 symbol)

- `normalizeVatNameKey`
- `findSupplierVatNameConflict`
- `assertUniqueSupplierVatName`

## Import DB / schema

- `import { db, productsTable } from "@workspace/db";`

## Xem trước đầu file

```typescript
import { db, productsTable } from "@workspace/db";
import { and, eq, sql } from "drizzle-orm";

type DbLike = Pick<typeof db, "select">;

export function normalizeVatNameKey(s: string): string {
  return s
    .normalize("NFD")
    .replace(/[\u0300-\u036f]/g, "")
    .toLowerCase()
    .replace(/\s+/g, " ")
    .trim();
}

export async function findSupplierVatNameConflict(
  executor: DbLike,
  input: { shopId: number; supplierId: number; vatName: string; excludeProductId?: number },
): Promise<{ id: number; name: string; vatName: string } | null> {
  const key = normalizeVatNameKey(input.vatName);
  if (!key) return null;
  const rows = await executor
    .select({
      id: productsTable.id,
      name: productsTable.name,
      vatName: productsTable.vatName,
    })
    .from(productsTable)
    .where(
      and(
        eq(productsTable.shopId, input.shopId),
        eq(productsTable.supplierId, input.supplierId),
        sql`${productsTable.vatName} is not null`,
      ),
    );
  const hit = rows.find((r) => {
```
