# Lib: `product-category.ts`

**Mô tả:** Logic backend product-category.ts (~98 dòng) — export: findCategoryByName, resolveProductCategory, syncProductCategoryNameFromCategory.

**Source Shop:** `artifacts/api-server/src/lib/product-category.ts`

**Độ lớn:** ~98 dòng.

Thư viện backend dùng chung giữa nhiều route handler — đọc file gốc để biết thuật toán đầy đủ.

## Export (3 symbol)

- `findCategoryByName`
- `resolveProductCategory`
- `syncProductCategoryNameFromCategory`

## Import DB / schema

- `import { db, productsTable, productCategoriesTable } from "@workspace/db";`

## Xem trước đầu file

```typescript
import { db, productsTable, productCategoriesTable } from "@workspace/db";
import { and, eq, sql } from "drizzle-orm";

type DbLike = Pick<typeof db, "select" | "insert" | "update">;

export type ResolvedProductCategory = {
  categoryId: number | null;
  category: string | null;
};

/** Tìm loại SP theo tên (không phân biệt hoa thường) trong cùng shop. */
export async function findCategoryByName(
  shopId: number,
  name: string,
  executor: DbLike = db,
) {
  const key = name.trim().toLowerCase();
  if (!key) return null;
  const [row] = await executor
    .select()
    .from(productCategoriesTable)
    .where(
      and(
        eq(productCategoriesTable.shopId, shopId),
        sql`lower(trim(${productCategoriesTable.name})) = ${key}`,
      ),
    )
    .limit(1);
  return row ?? null;
}

/**
 * Chuẩn hóa loại SP:
 * - `categoryId` ưu tiên hơn `category` (tên)
 * - tên trống / id null → bỏ liên kết
```
