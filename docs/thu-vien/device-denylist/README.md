# Thư viện: `device-denylist.ts`

**Mô tả:** [An ninh] device-denylist.ts — blockedDeviceCount, normalizeDeviceId, deviceIdFromRequest, isValidBlockedDeviceId, refreshDeviceDenylistFromDb, ….

**Chủ đề:** [An ninh](../../chuyen-de/an-ninh-truy-cap/)

**Mã nguồn Shop:** `artifacts/api-server/src/lib/device-denylist.ts` · **Quy mô:** ~91 dòng

File này là **tra cứu** khi đã đọc hub chủ đề và module API tương ứng. Thuật toán đầy đủ nằm trong mã TypeScript gốc.

## Hàm/hằng export (7)

- `blockedDeviceCount`
- `normalizeDeviceId`
- `deviceIdFromRequest`
- `isValidBlockedDeviceId`
- `refreshDeviceDenylistFromDb`
- `startDeviceDenylistRefreshScheduler`
- `deviceDenylistMiddleware`

## Import cơ sở dữ liệu

- `import { db, blockedDevicesTable } from "@workspace/db";`
- `"[device-denylist] Bảng blocked_devices chưa có — chạy: pnpm --filter @workspace/db run apply:blocked-devices",`

← [Chỉ mục lib](../../chi-muc/thu-vien-backend/) · [Hub An ninh](../../chuyen-de/an-ninh-truy-cap/)
