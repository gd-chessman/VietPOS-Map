# Lib: `time-drift.ts`

**Mô tả:** Logic backend time-drift.ts (~14 dòng) — export: getTimeDriftWarningThresholdMs.

**Source Shop:** `artifacts/api-server/src/lib/time-drift.ts`

**Độ lớn:** ~14 dòng.

Thư viện backend dùng chung giữa nhiều route handler — đọc file gốc để biết thuật toán đầy đủ.

## Export (1 symbol)

- `getTimeDriftWarningThresholdMs`

## Xem trước đầu file

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
