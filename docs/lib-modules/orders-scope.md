# Lib: `orders-scope.ts`

**Mô tả:** Logic backend orders-scope.ts (~107 dòng) — export: parseOptionalShopId, resolveOrderListScope, orderShopFilter, canAccessOrder, loadOrderForCancelModeration.

**Source Shop:** `artifacts/api-server/src/lib/orders-scope.ts`

**Độ lớn:** ~107 dòng.

Thư viện backend dùng chung giữa nhiều route handler — đọc file gốc để biết thuật toán đầy đủ.

## Export (5 symbol)

- `parseOptionalShopId`
- `resolveOrderListScope`
- `orderShopFilter`
- `canAccessOrder`
- `loadOrderForCancelModeration`

## Import DB / schema

- `import { db, shopsTable, ordersTable, usersTable } from "@workspace/db";`

## Xem trước đầu file

```typescript
import { db, shopsTable, ordersTable, usersTable } from "@workspace/db";
import { eq, inArray, type SQL } from "drizzle-orm";
import {
  isMasterAdmin,
  resolveOrganizationId,
  userCanViewOrgOrders,
  type AuthPayload,
} from "../middlewares/auth";

export type OrderListScope = {
  shopIds: number[];
  filterShopId: number | null;
  canViewOrg: boolean;
};

export function parseOptionalShopId(input: unknown): number | null {
  if (input === undefined || input === null || input === "") return null;
  const n = Number(input);
  return Number.isFinite(n) && n > 0 ? n : null;
}

export async function resolveOrderListScope(
  auth: AuthPayload,
  requestedShopId: number | null,
): Promise<OrderListScope | null> {
  const canViewOrg = await userCanViewOrgOrders(auth);

  if (auth.role === "super_admin" || isMasterAdmin(auth)) {
    if (requestedShopId) {
      return { shopIds: [requestedShopId], filterShopId: requestedShopId, canViewOrg: true };
    }
    const all = await db.select({ id: shopsTable.id }).from(shopsTable);
    return { shopIds: all.map((s) => s.id), filterShopId: null, canViewOrg: true };
  }

```
