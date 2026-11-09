# Thư viện: `manager-order-cancel-window.ts`

**Mô tả:** [POS & đơn hàng] manager-order-cancel-window.ts — MANAGER_ORDER_CANCEL_WINDOW_DAYS, MANAGER_ORDER_CANCEL_WINDOW_ERROR, orderCreatedWithinVnCalendarDays, managerOrderCancelWindowError.

**Chủ đề:** [POS & đơn hàng](../../chuyen-de/pos-va-don-hang/)

**Mã nguồn Shop:** `artifacts/api-server/src/lib/manager-order-cancel-window.ts` · **Quy mô:** ~34 dòng

File này là **tra cứu** khi đã đọc hub chủ đề và module API tương ứng. Thuật toán đầy đủ nằm trong mã TypeScript gốc.

## Hàm/hằng export (4)

- `MANAGER_ORDER_CANCEL_WINDOW_DAYS`
- `MANAGER_ORDER_CANCEL_WINDOW_ERROR`
- `orderCreatedWithinVnCalendarDays`
- `managerOrderCancelWindowError`

## Trích mã (tham khảo)

```typescript
import { vnAddCalendarDays, vnCalendarDay, vnDayBoundsExclusive } from "./vietnam-calendar";

/** Số ngày lịch VN (gần nhất) — khớp giới hạn danh sách đơn của nhân viên bán hàng. */
export const MANAGER_ORDER_CANCEL_WINDOW_DAYS = 3;

export const MANAGER_ORDER_CANCEL_WINDOW_ERROR = `Quản lý chỉ được huỷ, duyệt, từ chối hoặc khôi phục đơn trong ${MANAGER_ORDER_CANCEL_WINDOW_DAYS} ngày gần nhất (theo ngày tạo đơn, giờ Việt Nam).`;

/** Đơn có `createdAt` nằm trong cửa sổ [hôm nay−(days−1) 00:00+07, hết ngày hôm nay). */
export function orderCreatedWithinVnCalendarDays(
  orderCreatedAt: Date,
  days: number = MANAGER_ORDER_CANCEL_WINDOW_DAYS,
  now = new Date(),
): boolean {
  if (days < 1) return false;
  const today = vnCalendarDay(now);
  const earliestYmd = vnAddCalendarDays(today, -(days - 1));
  const start = new Date(`${earliestYmd}T00:00:00.000+07:00`);
  const { endExclusive } = vnDayBoundsExclusive(now);
  const t = orderCreatedAt.getTime();
  return t >= start.getTime() && t < endExclusive.getTime();
}

/** `null` nếu được phép; chuỗi lỗi nếu role manager ngoài cửa sổ. */
export function managerOrderCancelWindowError(
  role: string | undefined,
  orderCreatedAt: Date,
): string | null {
  if (role !== "manager") return null;
  if (orderCreatedWithinVnCalendarDays(orderCreatedAt, MANAGER_ORDER_CANCEL_WINDOW_DAYS)) {
    return null;
  }
  return MANAGER_ORDER_CANCEL_WINDOW_ERROR;
}
```

← [Chỉ mục lib](../../chi-muc/thu-vien-backend/) · [Hub POS & đơn hàng](../../chuyen-de/pos-va-don-hang/)
