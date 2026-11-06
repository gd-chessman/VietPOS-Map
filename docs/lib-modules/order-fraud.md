# Lib: `order-fraud.ts`

**Mô tả:** Logic backend order-fraud.ts (~16 dòng) — export: isOrderSyncSuspicious.

**Source Shop:** `artifacts/api-server/src/lib/order-fraud.ts`

**Độ lớn:** ~16 dòng.

Thư viện backend dùng chung giữa nhiều route handler — đọc file gốc để biết thuật toán đầy đủ.

## Export (1 symbol)

- `isOrderSyncSuspicious`

## Xem trước đầu file

```typescript
import { getTimeDriftWarningThresholdMs } from "./time-drift";

/**
 * The POS app always creates orders through the local offline queue, then pushes them to the
 * server carrying the local device's clock at creation time (`clientCreatedAt`). For an online
 * device that push happens within seconds, so the gap to the server's `createdAt` (set on
 * insert) is negligible; an order that was genuinely created offline and only synced later can
 * carry a real gap. A large gap can also mean a device clock was tampered with to backdate or
 * postdate a sale, so we surface it to admins as a fraud warning instead of silently trusting it.
 */
export function isOrderSyncSuspicious(order: { createdAt: Date; clientCreatedAt: Date | null }): boolean {
  if (!order.clientCreatedAt) return false;
  const diffMs = Math.abs(order.createdAt.getTime() - order.clientCreatedAt.getTime());
  return diffMs > getTimeDriftWarningThresholdMs();
}
```
