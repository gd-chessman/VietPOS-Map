# Thư viện: `order-shop-sequence.ts`

**Mô tả:** [POS & đơn hàng] order-shop-sequence.ts — allocateShopOrderSequence, resolveShopOrderSequence, queryMaxShopOrderSequence.

**Chủ đề:** [POS & đơn hàng](../../chuyen-de/pos-va-don-hang/)

**Mã nguồn Shop:** `artifacts/api-server/src/lib/order-shop-sequence.ts` · **Quy mô:** ~70 dòng

File này là **tra cứu** khi đã đọc hub chủ đề và module API tương ứng. Thuật toán đầy đủ nằm trong mã TypeScript gốc.

## Hàm/hằng export (3)

- `allocateShopOrderSequence`
- `resolveShopOrderSequence`
- `queryMaxShopOrderSequence`

## Import cơ sở dữ liệu

- `import { ordersTable } from "@workspace/db";`

## Trích mã (tham khảo)

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
export async function resolveShopOrderSequence(
  dbOrTx: DbLike,
  shopId: number,
  preferred?: number | null,
  options?: { fallbackIfTaken?: boolean },
): Promise<ResolvedShopSequence> {
  if (preferred != null && Number.isInteger(preferred) && preferred > 0) {
    const [existing] = await dbOrTx
      .select({ id: ordersTable.id })
      .from(ordersTable)
```

← [Chỉ mục lib](../../chi-muc/thu-vien-backend/) · [Hub POS & đơn hàng](../../chuyen-de/pos-va-don-hang/)
