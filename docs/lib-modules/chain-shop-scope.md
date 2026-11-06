# Lib: `chain-shop-scope.ts`

**Mô tả:** Logic backend chain-shop-scope.ts (~106 dòng) — export: parseOptionalShopId, resolveChainShopScope, resolveStatisticsShopScope, resolveReportShopScope, shopIdFilter, ….

**Source Shop:** `artifacts/api-server/src/lib/chain-shop-scope.ts`

**Độ lớn:** ~106 dòng.

Thư viện backend dùng chung giữa nhiều route handler — đọc file gốc để biết thuật toán đầy đủ.

## Export (8 symbol)

- `parseOptionalShopId`
- `resolveChainShopScope`
- `resolveStatisticsShopScope`
- `resolveReportShopScope`
- `shopIdFilter`
- `isMultiShopView`
- `effectiveShopIds`
- `loadShopNameMap`

## Import DB / schema

- `import { db, shopsTable } from "@workspace/db";`

## Xem trước đầu file

```typescript
import { db, shopsTable } from "@workspace/db";
import { eq, inArray, sql, type SQL, type AnyColumn, and } from "drizzle-orm";
import {
  isMasterAdmin,
  resolveOrganizationId,
  userCanViewChainDashboard,
  getHubShopIdForAuth,
  type AuthPayload,
} from "../middlewares/auth";

export type ChainShopScope = {
  mode: "all" | "org";
  shopIds: number[];
  filterShopId: number | null;
};

export function parseOptionalShopId(input: unknown): number | null {
  if (typeof input !== "string" || !input.trim()) return null;
  const n = Number(input);
  return Number.isFinite(n) && n > 0 ? n : null;
}

export async function resolveChainShopScope(
  auth: AuthPayload,
  requestedShopId: number | null,
  includeInactive = false,
): Promise<ChainShopScope | null> {
  if (auth.role === "super_admin" || isMasterAdmin(auth)) {
    return { mode: "all", shopIds: [], filterShopId: requestedShopId };
  }
  const orgId = await resolveOrganizationId(auth);
  const shopWhere = orgId
    ? includeInactive
      ? eq(shopsTable.organizationId, orgId)
      : and(eq(shopsTable.organizationId, orgId), eq(shopsTable.status, "active"))
```
