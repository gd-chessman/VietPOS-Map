# Lib: `inbound-stock-receive.ts`

**Mô tả:** Logic backend inbound-stock-receive.ts (~170 dòng) — export: applyInvoiceInventoryReceive, reverseInvoiceInventoryReceive.

**Source Shop:** `artifacts/api-server/src/lib/inbound-stock-receive.ts`

**Độ lớn:** ~170 dòng.

Thư viện backend dùng chung giữa nhiều route handler — đọc file gốc để biết thuật toán đầy đủ.

## Export (2 symbol)

- `applyInvoiceInventoryReceive`
- `reverseInvoiceInventoryReceive`

## Import DB / schema

- `} from "@workspace/db";`

## Xem trước đầu file

```typescript
import {
  db,
  inventoryTable,
  productsTable,
} from "@workspace/db";
import { and, eq } from "drizzle-orm";
import { recordInventoryChange, recordProductChange } from "./change-log";
import { recordProductAudit } from "./product-audit";
import { reverseWeightedAverageCost, roundMoney2, weightedAverageCost } from "./weighted-average-cost";
import { ensureVariant0 } from "./product-variants";
import { adjustShopStockByVariant, getShopStockQty } from "./inventory-variant";

type DbTx = Parameters<Parameters<typeof db.transaction>[0]>[0];

export type InboundReceiveLine = {
  productId: number | null;
  productName: string;
  prevReceived: number;
  nextReceived: number;
  orderQty: number;
  inboundCost: number | null;
};

/**
 * Cộng tồn + bình quân gia quyền theo SL nhận thêm (trên hoá đơn đầu vào).
 */
export async function applyInvoiceInventoryReceive(
  tx: DbTx,
  params: {
    shopId: number;
    userId: number;
    useWeightedAverageCost: boolean;
    items: InboundReceiveLine[];
  },
): Promise<{ status: "received" | "partial"; totalDelta: number }> {
```
