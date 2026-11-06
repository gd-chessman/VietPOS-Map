# Lib: `inventory-variant.ts`

**Mô tả:** Logic backend inventory-variant.ts (~328 dòng) — export: upsertShopStockByProduct, upsertShopExtraVariantStock, upsertShopStockByVariant, getShopStockQty, mapShopExtraVariantQuantities, ….

**Source Shop:** `artifacts/api-server/src/lib/inventory-variant.ts`

**Độ lớn:** ~328 dòng.

Thư viện backend dùng chung giữa nhiều route handler — đọc file gốc để biết thuật toán đầy đủ.

## Export (7 symbol)

- `upsertShopStockByProduct`
- `upsertShopExtraVariantStock`
- `upsertShopStockByVariant`
- `getShopStockQty`
- `mapShopExtraVariantQuantities`
- `adjustShopStockByVariant`
- `changeStockForOrderLine`

## Import DB / schema

- `} from "@workspace/db";`

## Xem trước đầu file

```typescript
import { and, eq, inArray, sql } from "drizzle-orm";
import {
  db,
  inventoryTable,
  productVariantsTable,
  shopVariantStockTable,
  type ProductVariant,
} from "@workspace/db";
import { ensureVariant0, getVariant0 } from "./product-variants";

type DbTx = Parameters<Parameters<typeof db.transaction>[0]>[0];
type DbLike = typeof db | DbTx;

/** Upsert tồn shop (inventory) + đồng bộ biến thể 0.quantity */
export async function upsertShopStockByProduct(
  tx: DbLike,
  product: {
    id: number;
    shopId: number;
    name: string;
    englishName?: string | null;
    price: string | number;
    costPrice: string | number;
    internalCode: string | null;
    thumbnailUrl: string | null;
    dimensions?: string | null;
    weight?: string | null;
    status: "active" | "discontinued";
  },
  shopId: number,
  quantity: number,
): Promise<ProductVariant> {
  const v0 = await ensureVariant0(tx, {
    id: product.id,
    shopId: product.shopId,
```
