# Lib: `vat-inbound-auto-sync.ts`

**Mô tả:** Logic backend vat-inbound-auto-sync.ts (~151 dòng) — export: isVatInboundAutoSyncWindow, vatInboundAutoSyncSlotKey, vatInboundAutoSyncDateRange, runVatInboundAutoSyncBatch, startVatInboundAutoSyncSch…

**Source Shop:** `artifacts/api-server/src/lib/vat-inbound-auto-sync.ts`

**Độ lớn:** ~151 dòng.

Thư viện backend dùng chung giữa nhiều route handler — đọc file gốc để biết thuật toán đầy đủ.

## Export (5 symbol)

- `isVatInboundAutoSyncWindow`
- `vatInboundAutoSyncSlotKey`
- `vatInboundAutoSyncDateRange`
- `runVatInboundAutoSyncBatch`
- `startVatInboundAutoSyncScheduler`

## Import DB / schema

- `import { db, organizationsTable, usersTable } from "@workspace/db";`

## Xem trước đầu file

```typescript
import { db, organizationsTable, usersTable } from "@workspace/db";
import { and, eq } from "drizzle-orm";
import { getHubShopIdForOrg } from "../middlewares/auth";
import { syncVatInboundInvoicesFromTax } from "./vat-inbound-tax-sync";
import { toPublicViettelSettings } from "./org-viettel-settings";
import { buildVatInboundChannelStatus } from "./org-gdt-settings";
import { getGdtSessionPublic } from "./gdt-portal/org-session";
import { notifyVatInboundAutoSyncNewInvoices } from "./user-notifications";
import { logger } from "./logger";
import { recordApiSystemEvent } from "./system-event-log";

const VN_TZ = "Asia/Ho_Chi_Minh";
const TICK_MS = 60_000;
let timer: ReturnType<typeof setInterval> | null = null;
let running = false;
/** orgId → slot key đã chạy (YYYY-MM-DD-HH VN) */
const lastRunSlotByOrg = new Map<number, string>();

function vnCalendarDay(d: Date): string {
  return d.toLocaleDateString("en-CA", { timeZone: VN_TZ });
}

function vnHourMinute(d: Date): { hour: number; minute: number } {
  const parts = new Intl.DateTimeFormat("en-US", {
    timeZone: VN_TZ,
    hour: "numeric",
    minute: "numeric",
    hour12: false,
  }).formatToParts(d);
  const hour = Number(parts.find((p) => p.type === "hour")?.value ?? 0);
  const minute = Number(parts.find((p) => p.type === "minute")?.value ?? 0);
  return { hour, minute };
}

export function isVatInboundAutoSyncWindow(now: Date): boolean {
```
