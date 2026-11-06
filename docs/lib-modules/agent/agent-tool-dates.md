# Lib: `agent/agent-tool-dates.ts`

**Mô tả:** Logic backend agent/agent-tool-dates.ts (~51 dòng) — export: formatAgentToolPayloadForLlm.

**Source Shop:** `artifacts/api-server/src/lib/agent/agent-tool-dates.ts`

**Độ lớn:** ~51 dòng.

Thư viện backend dùng chung giữa nhiều route handler — đọc file gốc để biết thuật toán đầy đủ.

## Export (1 symbol)

- `formatAgentToolPayloadForLlm`

## Xem trước đầu file

```typescript
import { formatVnDateTime } from "../vietnam-calendar";

function isDateFieldKey(key: string): boolean {
  return (
    key === "createdAt"
    || key === "updatedAt"
    || key === "sentAt"
    || key === "readAt"
    || key === "clientCreatedAt"
    || key === "invoiceIssuedAt"
    || key === "einvoiceIssuingAt"
    || key === "lastSeenAt"
    || key.endsWith("At")
  );
}

function parseAsDate(value: unknown): Date | null {
  if (value instanceof Date && !Number.isNaN(value.getTime())) return value;
  if (typeof value === "string" && /^\d{4}-\d{2}-\d{2}T\d/.test(value)) {
    const d = new Date(value);
    return Number.isNaN(d.getTime()) ? null : d;
  }
  return null;
}

/** Tool JSON → LLM: mọi instant UTC thành chuỗi giờ VN (khớp UI POS). */
export function formatAgentToolPayloadForLlm(value: unknown, key?: string): unknown {
  if (key && isDateFieldKey(key)) {
    const d = parseAsDate(value);
    if (d) return formatVnDateTime(d);
  }

  if (value instanceof Date) {
    return formatVnDateTime(value);
  }
```
