# Lib: `gdt-portal/map-inbound.ts`

**Mô tả:** Logic backend gdt-portal/map-inbound.ts (~209 dòng) — export: formatGdtVatRateLabel, mapGdtPurchaseRow, applyGdtDetailToMapped.

**Source Shop:** `artifacts/api-server/src/lib/gdt-portal/map-inbound.ts`

**Độ lớn:** ~209 dòng.

Thư viện backend dùng chung giữa nhiều route handler — đọc file gốc để biết thuật toán đầy đủ.

## Export (3 symbol)

- `formatGdtVatRateLabel`
- `mapGdtPurchaseRow`
- `applyGdtDetailToMapped`

## Import DB / schema

- `import type { VatInboundLineItem, VatInboundTaxRow } from "@workspace/db";`

## Xem trước đầu file

```typescript
import type { VatInboundLineItem, VatInboundTaxRow } from "@workspace/db";
import type { MappedInboundInvoice } from "../viettel-sinvoice/search-inbound";

function asStr(v: unknown): string | null {
  if (v == null) return null;
  const s = String(v).trim();
  return s.length ? s : null;
}

function asNum(v: unknown): number | null {
  if (v == null || v === "") return null;
  const n = typeof v === "number" ? v : Number(String(v).replace(",", "."));
  return Number.isFinite(n) ? n : null;
}

function asDateFromTdlap(v: unknown): string | null {
  const s = asStr(v);
  if (!s) return null;
  const d = new Date(s);
  if (!Number.isNaN(d.getTime())) return d.toISOString().slice(0, 10);
  const m = /^(\d{2})\/(\d{2})\/(\d{4})/.exec(s);
  if (m) return `${m[3]}-${m[2]}-${m[1]}`;
  const iso = /^(\d{4}-\d{2}-\d{2})/.exec(s);
  return iso?.[1] ?? null;
}

function slugPart(v: string | null): string {
  return (v ?? "").trim().replace(/[^\w.\-]+/g, "_") || "na";
}

/** CQT hay trả 0.08 / 0.1 (tỷ lệ) — hiển thị 8% / 10% như Viettel. */
export function formatGdtVatRateLabel(raw: unknown): string | null {
  const s = asStr(raw);
  if (!s) return null;
  const upper = s.toUpperCase().replace(/\s/g, "");
```
