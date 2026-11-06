# Thư viện: `vat-inbound-auto-archive-mst.ts`

**Mô tả:** [Hóa đơn đầu vào] vat-inbound-auto-archive-mst.ts — taxDigitsOnly, parseVatInboundAutoArchiveTaxCodes, normalizeVatInboundAutoArchiveTaxCodesInput, formatVatInboundAutoArchiveTaxCodesForForm, vatInbo…

**Chủ đề:** [Hóa đơn đầu vào](../../chuyen-de/hoa-don-dau-vao/)

**Mã nguồn Shop:** `artifacts/api-server/src/lib/vat-inbound-auto-archive-mst.ts` · **Quy mô:** ~58 dòng

File này là **tra cứu** khi đã đọc hub chủ đề và module API tương ứng. Thuật toán đầy đủ nằm trong mã TypeScript gốc.

## Hàm/hằng export (5)

- `taxDigitsOnly`
- `parseVatInboundAutoArchiveTaxCodes`
- `normalizeVatInboundAutoArchiveTaxCodesInput`
- `formatVatInboundAutoArchiveTaxCodesForForm`
- `vatInboundShouldAutoArchiveByMarkedMst`

## Trích mã (tham khảo)

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
  const set = parseVatInboundAutoArchiveTaxCodes(input);
  if (set.size === 0) return null;
  return [...set].sort().join("\n");
}

export function formatVatInboundAutoArchiveTaxCodesForForm(raw: string | null | undefined): string {
  const set = parseVatInboundAutoArchiveTaxCodes(raw);
  return [...set].sort().join("\n");
}

```

← [Chỉ mục lib](../../chi-muc/thu-vien-backend/) · [Hub Hóa đơn đầu vào](../../chuyen-de/hoa-don-dau-vao/)
