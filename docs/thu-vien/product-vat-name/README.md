# Thư viện: `product-vat-name.ts`

**Mô tả:** [Sản phẩm & kho] product-vat-name.ts — normalizeVatNameKey, findSupplierVatNameConflict, assertUniqueSupplierVatName.

**Chủ đề:** [Sản phẩm & kho](../../chuyen-de/san-pham-va-kho/)

**Mã nguồn Shop:** `artifacts/api-server/src/lib/product-vat-name.ts` · **Quy mô:** ~62 dòng

File này là **tra cứu** khi đã đọc hub chủ đề và module API tương ứng. Thuật toán đầy đủ nằm trong mã TypeScript gốc.

## Hàm/hằng export (3)

- `normalizeVatNameKey`
- `findSupplierVatNameConflict`
- `assertUniqueSupplierVatName`

## Import cơ sở dữ liệu

- `import { db, productsTable } from "@workspace/db";`

## Trích mã (tham khảo)

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
    if (!r.vatName) return false;
    if (input.excludeProductId != null && r.id === input.excludeProductId) return false;
    return normalizeVatNameKey(r.vatName) === key;
  });
  return hit?.vatName ? { id: hit.id, name: hit.name, vatName: hit.vatName } : null;
}

export async function assertUniqueSupplierVatName(
  executor: DbLike,
  input: { shopId: number; supplierId: number | null; vatName: string | null; excludeProductId?: number },
```

← [Chỉ mục lib](../../chi-muc/thu-vien-backend/) · [Hub Sản phẩm & kho](../../chuyen-de/san-pham-va-kho/)
