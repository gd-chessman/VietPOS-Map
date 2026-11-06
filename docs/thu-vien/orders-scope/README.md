# Thư viện: `orders-scope.ts`

**Mô tả:** [POS & đơn hàng] orders-scope.ts — parseOptionalShopId, resolveOrderListScope, orderShopFilter, canAccessOrder, loadOrderForCancelModeration.

**Chủ đề:** [POS & đơn hàng](../../chuyen-de/pos-va-don-hang/)

**Mã nguồn Shop:** `artifacts/api-server/src/lib/orders-scope.ts` · **Quy mô:** ~107 dòng

File này là **tra cứu** khi đã đọc hub chủ đề và module API tương ứng. Thuật toán đầy đủ nằm trong mã TypeScript gốc.

## Hàm/hằng export (5)

- `parseOptionalShopId`
- `resolveOrderListScope`
- `orderShopFilter`
- `canAccessOrder`
- `loadOrderForCancelModeration`

## Import cơ sở dữ liệu

- `import { db, shopsTable, ordersTable, usersTable } from "@workspace/db";`

← [Chỉ mục lib](../../chi-muc/thu-vien-backend/) · [Hub POS & đơn hàng](../../chuyen-de/pos-va-don-hang/)
