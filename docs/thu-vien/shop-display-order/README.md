# Thư viện: `shop-display-order.ts`

**Mô tả:** [POS & đơn hàng] shop-display-order.ts — shopsOrderByDisplay, compareShopsByDisplay, sortShopsByDisplay.

**Chủ đề:** [POS & đơn hàng](../../chuyen-de/pos-va-don-hang/)

**Mã nguồn Shop:** `artifacts/api-server/src/lib/shop-display-order.ts` · **Quy mô:** ~16 dòng

File này là **tra cứu** khi đã đọc hub chủ đề và module API tương ứng. Thuật toán đầy đủ nằm trong mã TypeScript gốc.

## Hàm/hằng export (3)

- `shopsOrderByDisplay`
- `compareShopsByDisplay`
- `sortShopsByDisplay`

## Import cơ sở dữ liệu

- `import { shopsTable } from "@workspace/db";`

## Trích mã (tham khảo)

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

← [Chỉ mục lib](../../chi-muc/thu-vien-backend/) · [Hub POS & đơn hàng](../../chuyen-de/pos-va-don-hang/)
