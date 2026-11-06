# Lib: `system-event-log.ts`

**Mô tả:** Logic backend system-event-log.ts (~177 dòng) — export: recordSystemEvent, recordEmailSystemFailure, recordEmailSmtpNotConfigured, recordVatSystemEvent, recordSyncSystemEvent, ….

**Source Shop:** `artifacts/api-server/src/lib/system-event-log.ts`

**Độ lớn:** ~177 dòng.

Thư viện backend dùng chung giữa nhiều route handler — đọc file gốc để biết thuật toán đầy đủ.

## Export (6 symbol)

- `recordSystemEvent`
- `recordEmailSystemFailure`
- `recordEmailSmtpNotConfigured`
- `recordVatSystemEvent`
- `recordSyncSystemEvent`
- `recordApiSystemEvent`

## Import DB / schema

- `import { db, shopsTable, systemEventLogsTable, type SystemEventCategory, type SystemEventSeverity } from "@workspace/db";`

## Xem trước đầu file

```typescript
import { db, shopsTable, systemEventLogsTable, type SystemEventCategory, type SystemEventSeverity } from "@workspace/db";
import { eq } from "drizzle-orm";
import { logger } from "./logger";

function sanitizeDetail(detail: Record<string, unknown> | null | undefined): Record<string, unknown> | null {
  if (!detail || typeof detail !== "object") return null;
  const out: Record<string, unknown> = {};
  for (const [k, v] of Object.entries(detail)) {
    const key = k.toLowerCase();
    if (key.includes("password") || key.includes("token") || key.includes("secret") || key.includes("smtp")) continue;
    if (typeof v === "string" && v.length > 500) {
      out[k] = `${v.slice(0, 500)}…`;
    } else {
      out[k] = v;
    }
  }
  return Object.keys(out).length > 0 ? out : null;
}

function errorMessage(err: unknown): string {
  if (err instanceof Error) return err.message.slice(0, 500);
  return String(err).slice(0, 500);
}

export type RecordSystemEventInput = {
  category: SystemEventCategory;
  severity: SystemEventSeverity;
  code: string;
  message: string;
  detail?: Record<string, unknown> | null;
  shopId?: number | null;
  organizationId?: number | null;
  userId?: number | null;
  deviceId?: string | null;
};
```
