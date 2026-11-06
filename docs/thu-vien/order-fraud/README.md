# Thư viện: `order-fraud.ts`

**Mô tả:** [POS & đơn hàng] order-fraud.ts — isOrderSyncSuspicious.

**Chủ đề:** [POS & đơn hàng](../../chuyen-de/pos-va-don-hang/)

**Mã nguồn Shop:** `artifacts/api-server/src/lib/order-fraud.ts` · **Quy mô:** ~16 dòng

File này là **tra cứu** khi đã đọc hub chủ đề và module API tương ứng. Thuật toán đầy đủ nằm trong mã TypeScript gốc.

## Hàm/hằng export (1)

- `isOrderSyncSuspicious`

## Trích mã (tham khảo)

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

← [Chỉ mục lib](../../chi-muc/thu-vien-backend/) · [Hub POS & đơn hàng](../../chuyen-de/pos-va-don-hang/)
