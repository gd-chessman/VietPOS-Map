# Thư viện: `pin-reset-requests.ts`

**Mô tả:** [Đăng nhập & phiên] pin-reset-requests.ts — upsertPendingPinResetRequest, canSetPinWithoutPasswordAfterUserSetsReset, clearUserPin, setUserPin, markPinResetRequestResolved, ….

**Chủ đề:** [Đăng nhập & phiên](../../chuyen-de/dang-nhap-va-phien/)

**Mã nguồn Shop:** `artifacts/api-server/src/lib/pin-reset-requests.ts` · **Quy mô:** ~98 dòng

File này là **tra cứu** khi đã đọc hub chủ đề và module API tương ứng. Thuật toán đầy đủ nằm trong mã TypeScript gốc.

## Hàm/hằng export (6)

- `upsertPendingPinResetRequest`
- `canSetPinWithoutPasswordAfterUserSetsReset`
- `clearUserPin`
- `setUserPin`
- `markPinResetRequestResolved`
- `markPinResetRequestCancelled`

## Import cơ sở dữ liệu

- `import { db, pinResetRequestsTable, usersTable, type User } from "@workspace/db";`

← [Chỉ mục lib](../../chi-muc/thu-vien-backend/) · [Hub Đăng nhập & phiên](../../chuyen-de/dang-nhap-va-phien/)
