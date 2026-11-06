# Lib: `product-variants.ts`

**Mô tả:** Logic backend product-variants.ts (~451 dòng) — export: suggestVariantCode, getVariant0, ensureVariantColumns, ensureVariant0, syncProductFromVariant0, ….

**Source Shop:** `artifacts/api-server/src/lib/product-variants.ts`

**Độ lớn:** ~451 dòng.

Thư viện backend dùng chung giữa nhiều route handler — đọc file gốc để biết thuật toán đầy đủ.

## Export (12 symbol)

- `suggestVariantCode`
- `getVariant0`
- `ensureVariantColumns`
- `ensureVariant0`
- `syncProductFromVariant0`
- `syncVariant0FromProduct`
- `nextVariantIndex`
- `listVariantsForProducts`
- `ensureShopVariant0s`
- `variantExtraStockRuleError`
- `assertProductVariantStockRule`
- `assertVariantNameUnique`

## Import DB / schema

- `} from "@workspace/db";`

## Xem trước đầu file

```typescript
import { and, asc, eq, inArray, sql } from "drizzle-orm";
import {
  db,
  inventoryTable,
  productsTable,
  productVariantsTable,
  shopVariantStockTable,
  type Product,
  type ProductVariant,
} from "@workspace/db";

type DbTx = Parameters<Parameters<typeof db.transaction>[0]>[0];
type DbLike = typeof db | DbTx;

export type VariantDto = {
  id: number;
  productId: number;
  variantIndex: number;
  internalCode: string | null;
  name: string;
  englishName: string | null;
  price: number;
  costPrice: number;
  thumbnailUrl: string | null;
  status: string;
  quantity: number;
  effectiveThumbnailUrl: string | null;
  dimensions: string | null;
  weight: string | null;
};

function money(n: string | number): number {
  const v = typeof n === "number" ? n : parseFloat(String(n));
  return Number.isFinite(v) ? v : 0;
}
```
