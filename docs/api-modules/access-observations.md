# API module: `access-observations`

**Mô tả:** File routes access-observations.ts — 1 endpoint HTTP cho /api/.... Tổng hợp cặp (deviceId, IP) đã gọi API — lưu in-memory (TTL giờ, xem accessObservationTtlHours). - Dùng tab Tổng quan t…

**Source Shop:** `artifacts/api-server/src/routes/access-observations.ts`

Tổng hợp **cặp (deviceId, IP)** đã gọi API — lưu **in-memory** (TTL giờ, xem `accessObservationTtlHours`).

- Dùng tab **Tổng quan** trên `/access-block`: bảng hit count, chặn nhanh IP hoặc thiết bị từ một dòng.
- Ghi nhận qua `accessObservationMiddleware()` trên mọi `/api` (không chặn, chỉ quan sát).

**Lib:** `lib/api-access-observations.ts`. **UI:** `AccessOverviewSection`.

**Số endpoint trong file:** 1

## Danh sách endpoint (tóm tắt)

| Method | Path | Mô tả ngắn |
|--------|------|------------|
| GET | `/access-observations` | Query `?limit=` (mặc định 200); trả `items`, thống kê `today`, `ttlHours`, `storage: memory` |

## Chi tiết từng endpoint

### `GET /access-observations` {#get-access-observations}

Query `?limit=` (mặc định 200); trả `items`, thống kê `today`, `ttlHours`, `storage: memory`. Middleware: `requireAuth`.

- **Middleware:** `requireAuth`

## Ghi chú đọc code

- Mount prefix `/api` qua `app.ts`; file này: `routes/index.ts` → `./access-observations.ts`.
- Handler đầy đủ: mở file TypeScript tại Shop (search theo path string).
- Quyền role: xem `reference/rbac.md` và middleware trong từng block.

## Luồng nghiệp vụ liên quan

- `nghiep-vu/10-truy-cap-an-ninh.md`
- UI: `frontend-pages/access-block.md`
- Middleware: `lib-modules/ip-denylist.md`, `lib-modules/device-denylist.md`, `lib-modules/api-access-observations.md`
