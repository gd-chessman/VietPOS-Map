# Lib: `shop-presence-sweep.ts`

**Mô tả:** Logic backend shop-presence-sweep.ts (~12 dòng) — export: startShopPresenceSweepScheduler.

**Source Shop:** `artifacts/api-server/src/lib/shop-presence-sweep.ts`

**Độ lớn:** ~12 dòng.

Thư viện backend dùng chung giữa nhiều route handler — đọc file gốc để biết thuật toán đầy đủ.

## Export (1 symbol)

- `startShopPresenceSweepScheduler`

## Xem trước đầu file

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
