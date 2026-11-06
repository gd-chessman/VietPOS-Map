# Thư viện: `ip-denylist.ts`

**Mô tả:** [An ninh] ip-denylist.ts — normalizeClientIp, blockedIpCount, clientIpFromRequest, describeSeenClientIp, refreshIpDenylistFromDb, ….

**Chủ đề:** [An ninh](../../chuyen-de/an-ninh-truy-cap/)

**Mã nguồn Shop:** `artifacts/api-server/src/lib/ip-denylist.ts` · **Quy mô:** ~159 dòng

File này là **tra cứu** khi đã đọc hub chủ đề và module API tương ứng. Thuật toán đầy đủ nằm trong mã TypeScript gốc.

## Hàm/hằng export (8)

- `normalizeClientIp`
- `blockedIpCount`
- `clientIpFromRequest`
- `describeSeenClientIp`
- `refreshIpDenylistFromDb`
- `startIpDenylistRefreshScheduler`
- `ipDenylistMiddleware`
- `isValidBlockedIp`

## Import cơ sở dữ liệu

- `import { db, blockedIpsTable } from "@workspace/db";`
- `"[ip-denylist] Bảng blocked_ips chưa có — chạy: pnpm --filter @workspace/db run apply:blocked-ips",`

← [Chỉ mục lib](../../chi-muc/thu-vien-backend/) · [Hub An ninh](../../chuyen-de/an-ninh-truy-cap/)
