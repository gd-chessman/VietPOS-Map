# Thư viện: `agent/agent-tool-dates.ts`

**Mô tả:** [Trợ lý AI] agent/agent-tool-dates.ts — formatAgentToolPayloadForLlm.

**Chủ đề:** [Trợ lý AI](../../../chuyen-de/tro-ly-widget/)

**Mã nguồn Shop:** `artifacts/api-server/src/lib/agent/agent-tool-dates.ts` · **Quy mô:** ~51 dòng

File này là **tra cứu** khi đã đọc hub chủ đề và module API tương ứng. Thuật toán đầy đủ nằm trong mã TypeScript gốc.

## Hàm/hằng export (1)

- `formatAgentToolPayloadForLlm`

## Trích mã (tham khảo)

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

  if (Array.isArray(value)) {
    return value.map((item) => formatAgentToolPayloadForLlm(item));
  }

  if (value && typeof value === "object") {
    const out: Record<string, unknown> = {};
    for (const [k, v] of Object.entries(value as Record<string, unknown>)) {
      out[k] = formatAgentToolPayloadForLlm(v, k);
    }
```

← [Chỉ mục lib](../../../chi-muc/thu-vien-backend/) · [Hub Trợ lý AI](../../../chuyen-de/tro-ly-widget/)
