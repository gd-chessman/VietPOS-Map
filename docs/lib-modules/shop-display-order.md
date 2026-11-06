# Lib: `shop-display-order.ts`

**Mô tả:** Logic backend shop-display-order.ts (~16 dòng) — export: shopsOrderByDisplay, compareShopsByDisplay, sortShopsByDisplay.

**Source Shop:** `artifacts/api-server/src/lib/shop-display-order.ts`

**Độ lớn:** ~16 dòng.

Thư viện backend dùng chung giữa nhiều route handler — đọc file gốc để biết thuật toán đầy đủ.

## Export (3 symbol)

- `shopsOrderByDisplay`
- `compareShopsByDisplay`
- `sortShopsByDisplay`

## Import DB / schema

- `import { shopsTable } from "@workspace/db";`

## Xem trước đầu file

```typescript
import { asc } from "drizzle-orm";
import { shopsTable } from "@workspace/db";

export const shopsOrderByDisplay = [asc(shopsTable.displayOrder), asc(shopsTable.id)] as const;

export function compareShopsByDisplay(
  a: { id: number; displayOrder: number },
  b: { id: number; displayOrder: number },
): number {
  return a.displayOrder - b.displayOrder || a.id - b.id;
}

export function sortShopsByDisplay<T extends { id: number; displayOrder: number }>(shops: T[]): T[] {
  return [...shops].sort(compareShopsByDisplay);
}
```
