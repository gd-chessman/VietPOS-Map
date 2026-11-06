# Lib: `entity-status.ts`

**Mô tả:** Logic backend entity-status.ts (~220 dòng) — export: getOperationalContext, getShopOperationalBlock, isShopActive, assertVoucherTransition, assertWarehouseOperational, ….

**Source Shop:** `artifacts/api-server/src/lib/entity-status.ts`

**Độ lớn:** ~220 dòng.

Thư viện backend dùng chung giữa nhiều route handler — đọc file gốc để biết thuật toán đầy đủ.

## Export (11 symbol)

- `getOperationalContext`
- `getShopOperationalBlock`
- `isShopActive`
- `assertVoucherTransition`
- `assertWarehouseOperational`
- `assertTransferTransition`
- `closeOpenShiftSessionsForShop`
- `cascadeOrgDeactivation`
- `cascadeShopDeactivation`
- `cascadeOrgActivation`
- `cascadeShopActivation`

## Import DB / schema

- `} from "@workspace/db";`

## Xem trước đầu file

```typescript
import {
  db,
  shopsTable,
  organizationsTable,
  warehousesTable,
  shiftSessionsTable,
} from "@workspace/db";
import { eq, and, isNull } from "drizzle-orm";

export type EntityStatus = "active" | "inactive";

export interface OperationalContext {
  shopId: number;
  shopStatus: EntityStatus;
  shopName: string | null;
  organizationId: number | null;
  orgStatus: EntityStatus | null;
  isOperational: boolean;
  blockedReason: string | null;
}

export type VoucherAction = "create" | "approve" | "ship" | "complete" | "cancel" | "reject";

export type TransferAction = "create" | "approve" | "ship" | "receive" | "cancel" | "update";

export async function getOperationalContext(shopId: number): Promise<OperationalContext | null> {
  const [shop] = await db.select().from(shopsTable).where(eq(shopsTable.id, shopId));
  if (!shop) return null;

  let orgStatus: EntityStatus | null = null;
  if (shop.organizationId) {
    const [org] = await db
      .select({ status: organizationsTable.status })
      .from(organizationsTable)
      .where(eq(organizationsTable.id, shop.organizationId));
```
