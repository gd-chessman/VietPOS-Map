# Lib: `order-shop-sequence.ts`

**Mô tả:** Logic backend order-shop-sequence.ts (~70 dòng) — export: allocateShopOrderSequence, resolveShopOrderSequence, queryMaxShopOrderSequence.

**Source Shop:** `artifacts/api-server/src/lib/order-shop-sequence.ts`

**Độ lớn:** ~70 dòng.

Thư viện backend dùng chung giữa nhiều route handler — đọc file gốc để biết thuật toán đầy đủ.

## Export (3 symbol)

- `allocateShopOrderSequence`
- `resolveShopOrderSequence`
- `queryMaxShopOrderSequence`

## Import DB / schema

- `import { ordersTable } from "@workspace/db";`

## Xem trước đầu file

```typescript
import { ordersTable } from "@workspace/db";
import { and, eq, sql } from "drizzle-orm";
import type { NodePgDatabase } from "drizzle-orm/node-postgres";

type DbLike = Pick<NodePgDatabase<Record<string, never>>, "select">;

export class ShopSequenceTakenError extends Error {
  constructor() {
    super("SHOP_SEQUENCE_TAKEN");
    this.name = "ShopSequenceTakenError";
  }
}

/** STT tiếp theo trong cửa hàng (gọi trong transaction tạo đơn). */
export async function allocateShopOrderSequence(dbOrTx: DbLike, shopId: number): Promise<number> {
  const [row] = await dbOrTx
    .select({
      maxSeq: sql<string>`COALESCE(MAX(${ordersTable.shopSequence}), 0)`,
    })
    .from(ordersTable)
    .where(eq(ordersTable.shopId, shopId));
  const maxSeq = Number(row?.maxSeq ?? 0);
  return maxSeq + 1;
}

export type ResolvedShopSequence = {
  sequence: number;
  /** STT client gửi nhưng đã bị chiếm — server đã cấp sequence khác. */
  adjustedFrom: number | null;
};

/**
 * POS offline gửi STT đã in — dùng nếu còn trống.
 * Trùng: fallbackIfTaken → max+1; không thì ShopSequenceTakenError.
 */
```
