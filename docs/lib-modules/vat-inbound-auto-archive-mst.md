# Lib: `vat-inbound-auto-archive-mst.ts`

**Mô tả:** Logic backend vat-inbound-auto-archive-mst.ts (~58 dòng) — export: taxDigitsOnly, parseVatInboundAutoArchiveTaxCodes, normalizeVatInboundAutoArchiveTaxCodesInput, formatVatInboundAutoArchiveTaxCodesF…

**Source Shop:** `artifacts/api-server/src/lib/vat-inbound-auto-archive-mst.ts`

**Độ lớn:** ~58 dòng.

Thư viện backend dùng chung giữa nhiều route handler — đọc file gốc để biết thuật toán đầy đủ.

## Export (5 symbol)

- `taxDigitsOnly`
- `parseVatInboundAutoArchiveTaxCodes`
- `normalizeVatInboundAutoArchiveTaxCodesInput`
- `formatVatInboundAutoArchiveTaxCodesForForm`
- `vatInboundShouldAutoArchiveByMarkedMst`

## Xem trước đầu file

```typescript
/** MST đánh dấu trên tổ chức — HĐ kéo từ thuế trùng sẽ tự lưu trữ (tab Lưu trữ, không Đang dùng). */

export function taxDigitsOnly(raw: string | null | undefined): string {
  return (raw ?? "").replace(/[^0-9]/g, "");
}

export function parseVatInboundAutoArchiveTaxCodes(raw: string | null | undefined): Set<string> {
  const set = new Set<string>();
  if (!raw?.trim()) return set;
  const trimmed = raw.trim();
  if (trimmed.startsWith("[")) {
    try {
      const arr = JSON.parse(trimmed) as unknown;
      if (Array.isArray(arr)) {
        for (const item of arr) {
          const d = taxDigitsOnly(String(item));
          if (d.length >= 10) set.add(d);
        }
        return set;
      }
    } catch {
      /* plain text below */
    }
  }
  for (const part of trimmed.split(/[\n,;]+/)) {
    const d = taxDigitsOnly(part);
    if (d.length >= 10) set.add(d);
  }
  return set;
}

/** Chuỗi lưu DB: mỗi MST một dòng (chỉ chữ số). */
export function normalizeVatInboundAutoArchiveTaxCodesInput(input: unknown): string | null {
  if (input == null || input === "") return null;
  if (typeof input !== "string") return null;
```
