# Thư viện: `shop-presence.ts`

**Mô tả:** [Chuỗi cửa hàng] shop-presence.ts — SHOP_PRESENCE_TIMEOUT_MS, isShopOnline, CLOCK_DRIFT_WARNING_MS, hasClockDrift.

**Chủ đề:** [Chuỗi cửa hàng](../../chuyen-de/chuoi-cua-hang/)

**Mã nguồn Shop:** `artifacts/api-server/src/lib/shop-presence.ts` · **Quy mô:** ~25 dòng

File này là **tra cứu** khi đã đọc hub chủ đề và module API tương ứng. Thuật toán đầy đủ nằm trong mã TypeScript gốc.

## Hàm/hằng export (4)

- `SHOP_PRESENCE_TIMEOUT_MS`
- `isShopOnline`
- `CLOCK_DRIFT_WARNING_MS`
- `hasClockDrift`

## Trích mã (tham khảo)

```typescript
/**
 * Ngưỡng coi shop là offline. Heartbeat gửi mỗi 30s (xem POST /shops/heartbeat và
 * pos-app useShopHeartbeat); ngưỡng đặt gấp 3 lần chu kỳ đó để chịu được jitter mạng
 * và việc trình duyệt throttle setInterval khi tab chạy nền, tránh báo offline giả.
 */
export const SHOP_PRESENCE_TIMEOUT_MS = 90_000;

export function isShopOnline(lastSeenAt: Date | null, now: Date = new Date()): boolean {
  if (!lastSeenAt) return false;
  return now.getTime() - lastSeenAt.getTime() <= SHOP_PRESENCE_TIMEOUT_MS;
}

/**
 * Ngưỡng lệch giờ giữa thiết bị chi nhánh và server để cảnh báo admin. So sánh giờ server
 * lúc nhận heartbeat với giờ do chính thiết bị gửi kèm trong cùng request đó, nên độ trễ
 * mạng gần như không đáng kể — 60s đủ rộng để không báo giả nhưng vẫn bắt được các lệch
 * giờ thực sự (sai múi giờ, đồng hồ thiết bị chạy sai...).
 */
export const CLOCK_DRIFT_WARNING_MS = 60_000;

export function hasClockDrift(serverTime: Date | null, deviceTime: Date | null): boolean {
  if (!serverTime || !deviceTime) return false;
  return Math.abs(serverTime.getTime() - deviceTime.getTime()) > CLOCK_DRIFT_WARNING_MS;
}
```

← [Chỉ mục lib](../../chi-muc/thu-vien-backend/) · [Hub Chuỗi cửa hàng](../../chuyen-de/chuoi-cua-hang/)
