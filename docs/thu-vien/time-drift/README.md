# Thư viện: `time-drift.ts`

**Mô tả:** [Kiến trúc / dùng chung] time-drift.ts — getTimeDriftWarningThresholdMs.

**Chủ đề:** [Kiến trúc / dùng chung](../../chuyen-de/kien-truc-he-thong/)

**Mã nguồn Shop:** `artifacts/api-server/src/lib/time-drift.ts` · **Quy mô:** ~14 dòng

File này là **tra cứu** khi đã đọc hub chủ đề và module API tương ứng. Thuật toán đầy đủ nằm trong mã TypeScript gốc.

## Hàm/hằng export (1)

- `getTimeDriftWarningThresholdMs`

## Trích mã (tham khảo)

```typescript
/**
 * Shared "how big a clock gap is suspicious" setting, used both to flag orders whose local
 * creation time drifted too far from the server's sync-arrival time (order-fraud.ts) and to warn
 * a user on login whose device clock has drifted from the server's clock.
 */
const DEFAULT_WARNING_MINUTES = 30;

export function getTimeDriftWarningThresholdMs(): number {
  const raw = process.env.ORDER_SYNC_WARNING_MINUTES;
  const minutes = raw != null && raw.trim() !== "" ? Number(raw) : NaN;
  const effectiveMinutes = Number.isFinite(minutes) && minutes > 0 ? minutes : DEFAULT_WARNING_MINUTES;
  return effectiveMinutes * 60 * 1000;
}
```

← [Chỉ mục lib](../../chi-muc/thu-vien-backend/) · [Hub Kiến trúc / dùng chung](../../chuyen-de/kien-truc-he-thong/)
