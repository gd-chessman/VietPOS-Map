# Lib: `system-event-query.ts`

**Mô tả:** Logic backend system-event-query.ts (~153 dòng) — export: vnTodayYmd, querySystemEventLogs.

**Source Shop:** `artifacts/api-server/src/lib/system-event-query.ts`

**Độ lớn:** ~153 dòng.

Thư viện backend dùng chung giữa nhiều route handler — đọc file gốc để biết thuật toán đầy đủ.

## Export (2 symbol)

- `vnTodayYmd`
- `querySystemEventLogs`

## Import DB / schema

- `import { db, shopsTable, systemEventLogsTable, usersTable } from "@workspace/db";`

## Xem trước đầu file

```typescript
import { db, shopsTable, systemEventLogsTable, usersTable } from "@workspace/db";
import { and, desc, eq, gte, inArray, lt, sql, type SQL } from "drizzle-orm";
import type { AuthPayload } from "../middlewares/auth";
import { isMasterAdmin, resolveOrganizationId } from "../middlewares/auth";
import { VN_YMD_RE, vnYmdStartInstant } from "./vn-order-period";

export type SystemEventLogRow = {
  id: number;
  organizationId: number | null;
  shopId: number | null;
  shopName: string | null;
  shopCode: string | null;
  userId: number | null;
  userName: string | null;
  deviceId: string | null;
  category: string;
  severity: string;
  code: string;
  message: string;
  detail: Record<string, unknown> | null;
  createdAt: string;
};

export type SystemEventQueryInput = {
  shopId?: number | null;
  from?: string;
  to?: string;
  category?: string;
  severity?: string;
  page?: number;
  limit?: number;
};

function appendSystemEventDateFilters(conditions: SQL[], fromYmd: string, toYmd?: string): void {
  const start = vnYmdStartInstant(fromYmd);
```
