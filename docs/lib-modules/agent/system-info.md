# Lib: `agent/system-info.ts`

**Mô tả:** Logic backend agent/system-info.ts (~176 dòng) — export: buildAgentSystemInfo.

**Source Shop:** `artifacts/api-server/src/lib/agent/system-info.ts`

**Độ lớn:** ~176 dòng.

Thư viện backend dùng chung giữa nhiều route handler — đọc file gốc để biết thuật toán đầy đủ.

## Export (1 symbol)

- `buildAgentSystemInfo`

## Import DB / schema

- `import { db, shopsTable } from "@workspace/db";`

## Xem trước đầu file

```typescript
import { sql, eq, inArray, and } from "drizzle-orm";
import { db, shopsTable } from "@workspace/db";
import type { AuthPayload } from "../../middlewares/auth";
import { userCanViewChainDashboard } from "../../middlewares/auth";
import { resolveChainShopScope } from "../chain-shop-scope";
import { isShopOnline, hasClockDrift } from "../shop-presence";
import { resolveAgentLlmForAuth } from "./chat";
import { agentToolDefinitionsForAuth } from "./tools";

export type AgentSystemIssue = {
  level: "ok" | "warn" | "error";
  code: string;
  message: string;
};

async function shopRowsForAuth(auth: AuthPayload) {
  const scope = await resolveChainShopScope(auth, null);
  if (!scope) return [];
  if (scope.filterShopId) {
    return db
      .select({
        id: shopsTable.id,
        lastSeenAt: shopsTable.lastSeenAt,
        lastHeartbeatDeviceTime: shopsTable.lastHeartbeatDeviceTime,
      })
      .from(shopsTable)
      .where(eq(shopsTable.id, scope.filterShopId));
  }
  if (scope.mode === "all") {
    return db
      .select({
        id: shopsTable.id,
        lastSeenAt: shopsTable.lastSeenAt,
        lastHeartbeatDeviceTime: shopsTable.lastHeartbeatDeviceTime,
      })
```
