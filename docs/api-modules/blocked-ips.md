# API module: `blocked-ips`

**Mô tả:** File routes blocked-ips.ts — 3 endpoint HTTP cho /api/.... Danh sách IP bị chặn toàn cục trên mọi request /api/*. - Quyền: requireAuth + role super_admin (403 nếu không đủ). - Sa…

**Source Shop:** `artifacts/api-server/src/routes/blocked-ips.ts`

Danh sách IP bị chặn toàn cục trên **mọi** request `/api/*`.

- **Quyền:** `requireAuth` + role **`super_admin`** (403 nếu không đủ).
- Sau POST/DELETE: gọi `refreshIpDenylistFromDb()` — cache in-memory middleware cập nhật ngay.
- GET trả thêm `envDenylistEnabled` (biến `IP_DENYLIST` / `BLOCKED_IPS`) và `describeSeenClientIp(req)`.

**Middleware:** `ipDenylistMiddleware()` mount trên `/api` trong `app.ts` (trước router).

**Lib:** `lib/ip-denylist.ts`. **UI:** tab **Chặn IP** trong `access-block.tsx` → `IpBanSection`.

**Số endpoint trong file:** 3

## Danh sách endpoint (tóm tắt)

| Method | Path | Mô tả ngắn |
|--------|------|------------|
| GET | `/blocked-ips` | Liệt kê `blocked_ips` + nhãn người tạo; kèm cờ env denylist và IP client hiện tại |
| POST | `/blocked-ips` | Thêm IP (normalize IPv4/IPv6); body `{ ip, note? }`; refresh denylist cache |
| DELETE | `/blocked-ips/:id` | Xóa một dòng; refresh denylist cache |

## Chi tiết từng endpoint

### `GET /blocked-ips` {#get-blocked-ips}

Liệt kê `blocked_ips` + nhãn người tạo; kèm cờ env denylist và IP client hiện tại. Middleware: `requireAuth`.

- **Middleware:** `requireAuth`

### `POST /blocked-ips` {#post-blocked-ips}

Thêm IP (normalize IPv4/IPv6); body `{ ip, note? }`; refresh denylist cache. Middleware: `requireAuth`.

- **Middleware:** `requireAuth`

### `DELETE /blocked-ips/:id` {#delete-blocked-ips--id}

Xóa một dòng; refresh denylist cache. Middleware: `requireAuth`.

- **Middleware:** `requireAuth`

## Ghi chú đọc code

- Mount prefix `/api` qua `app.ts`; file này: `routes/index.ts` → `./blocked-ips.ts`.
- Handler đầy đủ: mở file TypeScript tại Shop (search theo path string).
- Quyền role: xem `reference/rbac.md` và middleware trong từng block.

## Luồng nghiệp vụ liên quan

- `nghiep-vu/10-truy-cap-an-ninh.md`
- UI: `frontend-pages/access-block.md`
- Middleware: `lib-modules/ip-denylist.md`, `lib-modules/device-denylist.md`, `lib-modules/api-access-observations.md`
