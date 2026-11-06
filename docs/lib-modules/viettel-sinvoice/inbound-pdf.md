# Lib: `viettel-sinvoice/inbound-pdf.ts`

**Mô tả:** Logic backend viettel-sinvoice/inbound-pdf.ts (~134 dòng) — export: toViettelPortalIssueDate, fetchViettelInboundInvoicePdf.

**Source Shop:** `artifacts/api-server/src/lib/viettel-sinvoice/inbound-pdf.ts`

**Độ lớn:** ~134 dòng.

Thư viện backend dùng chung giữa nhiều route handler — đọc file gốc để biết thuật toán đầy đủ.

## Export (2 symbol)

- `toViettelPortalIssueDate`
- `fetchViettelInboundInvoicePdf`

## Xem trước đầu file

```typescript
import { getViettelInboundConfig, viettelInboundConfigErrorMessage } from "./config";
import { downloadViettelInvoiceFilePortal } from "./client";

function asStr(v: unknown): string | null {
  if (v == null) return null;
  const s = String(v).trim();
  return s.length ? s : null;
}

function parseRaw(rawText: string | null | undefined): Record<string, unknown> {
  if (!rawText?.trim()) return {};
  try {
    const parsed = JSON.parse(rawText) as unknown;
    if (parsed && typeof parsed === "object" && !Array.isArray(parsed)) {
      return parsed as Record<string, unknown>;
    }
  } catch {
    /* ignore */
  }
  return {};
}

/** yyyyMMddHHmmss — Viettel Portal yêu cầu. */
export function toViettelPortalIssueDate(raw: unknown, fallbackDate?: string | null): string | null {
  const s = asStr(raw);
  if (s) {
    const m = /^(\d{4})-(\d{2})-(\d{2})(?:[ T](\d{2}):(\d{2}):(\d{2}))?/.exec(s);
    if (m) {
      return `${m[1]}${m[2]}${m[3]}${m[4] ?? "00"}${m[5] ?? "00"}${m[6] ?? "00"}`;
    }
    if (/^\d{14}$/.test(s)) return s;
  }
  const fb = asStr(fallbackDate);
  if (fb && /^\d{4}-\d{2}-\d{2}/.test(fb)) {
    return `${fb.slice(0, 4)}${fb.slice(5, 7)}${fb.slice(8, 10)}000000`;
```
