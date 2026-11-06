# Thư viện: `shop-presence-sweep.ts`

**Mô tả:** [Chuỗi cửa hàng] shop-presence-sweep.ts — startShopPresenceSweepScheduler.

**Chủ đề:** [Chuỗi cửa hàng](../../chuyen-de/chuoi-cua-hang/)

**Mã nguồn Shop:** `artifacts/api-server/src/lib/shop-presence-sweep.ts` · **Quy mô:** ~12 dòng

File này là **tra cứu** khi đã đọc hub chủ đề và module API tương ứng. Thuật toán đầy đủ nằm trong mã TypeScript gốc.

## Hàm/hằng export (1)

- `startShopPresenceSweepScheduler`

## Trích mã (tham khảo)

```typescript
import { runShopPresenceSweep } from "./shop-operational-events";

const TICK_MS = 45_000;

let timer: ReturnType<typeof setInterval> | null = null;

export function startShopPresenceSweepScheduler(): void {
  if (timer) return;
  void runShopPresenceSweep();
  timer = setInterval(() => void runShopPresenceSweep(), TICK_MS);
}
```

← [Chỉ mục lib](../../chi-muc/thu-vien-backend/) · [Hub Chuỗi cửa hàng](../../chuyen-de/chuoi-cua-hang/)
