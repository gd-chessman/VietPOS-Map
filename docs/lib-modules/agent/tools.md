# Lib: `agent/tools.ts`

**Mô tả:** Logic backend agent/tools.ts (~317 dòng) — export: agentToolDefinitionsForAuth, invokeAgentTool.

**Source Shop:** `artifacts/api-server/src/lib/agent/tools.ts`

**Độ lớn:** ~317 dòng.

Thư viện backend dùng chung giữa nhiều route handler — đọc file gốc để biết thuật toán đầy đủ.

## Export (2 symbol)

- `agentToolDefinitionsForAuth`
- `invokeAgentTool`

## Import DB / schema

- `import { db, inventoryTable, productsTable, shopsTable } from "@workspace/db";`

## Xem trước đầu file

```typescript
import { z } from "zod/v4";
import { db, inventoryTable, productsTable, shopsTable } from "@workspace/db";
import { and, eq, ilike, inArray, lt, or } from "drizzle-orm";
import type { AuthPayload } from "../../middlewares/auth";
import { formatAgentToolPayloadForLlm } from "./agent-tool-dates";
import {
  effectiveShopIds,
  resolveStatisticsShopScope,
  shopIdFilter,
} from "../chain-shop-scope";
import { computeDayBlockForShops } from "../widget-home";
import { vnDayBoundsExclusive } from "../vietnam-calendar";
import { shopsOrderByDisplay } from "../shop-display-order";
import { readBusinessDataSchema, runReadBusinessData, AGENT_READ_DATASETS } from "./read-business-data";
import { querySystemEventLogs, vnTodayYmd } from "../system-event-query";

/** Cùng phạm vi Thống kê / read_business_data — chi nhánh con chỉ shop đăng nhập. */
async function shopIdsForAgentScope(
  auth: AuthPayload,
  shopId?: number,
): Promise<{
  scope: NonNullable<Awaited<ReturnType<typeof resolveStatisticsShopScope>>>;
  shopIds: number[];
}> {
  const scope = await resolveStatisticsShopScope(auth, shopId ?? null);
  if (!scope) {
    throw new Error("Không có quyền xem chi nhánh này");
  }
  let shopIds = effectiveShopIds(scope);
  if (scope.mode === "all" && !scope.filterShopId) {
    const rows = await db.select({ id: shopsTable.id }).from(shopsTable);
    shopIds = rows.map((r) => r.id);
  }
  return { scope, shopIds };
}
```
