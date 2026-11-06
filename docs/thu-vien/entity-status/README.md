# Thư viện: `entity-status.ts`

**Mô tả:** [Kiến trúc / dùng chung] entity-status.ts — getOperationalContext, getShopOperationalBlock, isShopActive, assertVoucherTransition, assertWarehouseOperational, ….

**Chủ đề:** [Kiến trúc / dùng chung](../../chuyen-de/kien-truc-he-thong/)

**Mã nguồn Shop:** `artifacts/api-server/src/lib/entity-status.ts` · **Quy mô:** ~220 dòng

File này là **tra cứu** khi đã đọc hub chủ đề và module API tương ứng. Thuật toán đầy đủ nằm trong mã TypeScript gốc.

## Hàm/hằng export (11)

- `getOperationalContext`
- `getShopOperationalBlock`
- `isShopActive`
- `assertVoucherTransition`
- `assertWarehouseOperational`
- `assertTransferTransition`
- `closeOpenShiftSessionsForShop`
- `cascadeOrgDeactivation`
- `cascadeShopDeactivation`
- `cascadeOrgActivation`
- `cascadeShopActivation`

## Import cơ sở dữ liệu

- `} from "@workspace/db";`

← [Chỉ mục lib](../../chi-muc/thu-vien-backend/) · [Hub Kiến trúc / dùng chung](../../chuyen-de/kien-truc-he-thong/)
