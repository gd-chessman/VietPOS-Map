# API module: `blocked-devices`

**Mô tả:** File routes blocked-devices.ts — 3 endpoint HTTP cho /api/.... Danh sách Device ID (header client) bị chặn mọi /api/*. - Quyền: super_admin (giống blocked-ips). - Device ID lấy từ cl…

**Source Shop:** `artifacts/api-server/src/routes/blocked-devices.ts`

Danh sách **Device ID** (header client) bị chặn mọi `/api/*`.

- **Quyền:** `super_admin` (giống blocked-ips).
- Device ID lấy từ client (`x-device-id` / cookie — xem `device-denylist.ts`).

**Middleware:** `deviceDenylistMiddleware()` trên `/api`.

**UI:** tab **Chặn thiết bị** → `DeviceBanSection` trong `access-block.tsx`.

**Số endpoint trong file:** 3

## Danh sách endpoint (tóm tắt)

| Method | Path | Mô tả ngắn |
|--------|------|------------|
| GET | `/blocked-devices` | Liệt kê thiết bị bị chặn (tương tự IP) |
| POST | `/blocked-devices` | Thêm device id; validate qua `isValidBlockedDeviceId` |
| DELETE | `/blocked-devices/:id` | Bỏ chặn thiết bị |

## Chi tiết từng endpoint

### `GET /blocked-devices` {#get-blocked-devices}

Liệt kê thiết bị bị chặn (tương tự IP). Middleware: `requireAuth`.

- **Middleware:** `requireAuth`

### `POST /blocked-devices` {#post-blocked-devices}

Thêm device id; validate qua `isValidBlockedDeviceId`. Middleware: `requireAuth`.

- **Middleware:** `requireAuth`

### `DELETE /blocked-devices/:id` {#delete-blocked-devices--id}

Bỏ chặn thiết bị. Middleware: `requireAuth`.

- **Middleware:** `requireAuth`

## Ghi chú đọc code

- Mount prefix `/api` qua `app.ts`; file này: `routes/index.ts` → `./blocked-devices.ts`.
- Handler đầy đủ: mở file TypeScript tại Shop (search theo path string).
- Quyền role: xem `reference/rbac.md` và middleware trong từng block.

## Luồng nghiệp vụ liên quan

- `nghiep-vu/10-truy-cap-an-ninh.md`
- UI: `frontend-pages/access-block.md`
- Middleware: `lib-modules/ip-denylist.md`, `lib-modules/device-denylist.md`, `lib-modules/api-access-observations.md`
