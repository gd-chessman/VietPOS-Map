# Module API: `blocked-devices`

**Mô tả:** Module API blocked-devices.ts — 3 endpoint. Danh sách Device ID (header client) bị chặn mọi /api/*. - Quyền: super_admin (giống blocked-ips). - Device ID lấy từ cl…

**Mã nguồn Shop:** `artifacts/api-server/src/routes/blocked-devices.ts`

Danh sách **Device ID** (header client) bị chặn mọi `/api/*`.

- **Quyền:** `super_admin` (giống blocked-ips).
- Device ID lấy từ client (`x-device-id` / cookie — xem `device-denylist.ts`).

**Middleware:** `deviceDenylistMiddleware()` trên `/api`.

**UI:** tab **Chặn thiết bị** → `DeviceBanSection` trong `access-block.tsx`.

**Số endpoint:** 3

## Bảng endpoint (tóm tắt)

| Method | Path | Mô tả ngắn |
|--------|------|------------|
| GET | `/blocked-devices` | Liệt kê thiết bị bị chặn + Device ID request hiện tại |
| POST | `/blocked-devices` | Thêm Device ID vào denylist; refresh cache |
| DELETE | `/blocked-devices/:id` | Bỏ chặn thiết bị theo id bảng `blocked_devices` |

## Chi tiết từng endpoint

### `GET /blocked-devices` {#get-blocked-devices}

Liệt kê thiết bị bị chặn + Device ID request hiện tại. Route: `requireAuth` + **super_admin** trong handler.

**URL:** `GET /api/blocked-devices`

**Quyền:** `requireAuth` + **super_admin** (403: `"Chỉ quản trị hệ thống được quản lý thiết bị bị chặn"`).

**Response 200:**

| Trường | Ý nghĩa |
|--------|---------|
| `items[]` | `id`, `deviceId`, `deviceName` (từ `allowed_devices` nếu có), `note`, `createdAt`, `createdByLabel` |
| `thisDeviceId` | Device ID client gửi lên request (header/cookie — xem `device-denylist.ts`) |

**500:** `{ "error": "Không tải được danh sách. Chạy pnpm --filter @workspace/db run apply:blocked-devices rồi thử lại." }`

### `POST /blocked-devices` {#post-blocked-devices}

Thêm Device ID vào denylist; refresh cache. Route: `requireAuth` + **super_admin** trong handler.

**URL:** `POST /api/blocked-devices`

**Quyền:** super_admin.

**Body JSON:**

| Trường | Bắt buộc | Mô tả |
|--------|----------|--------|
| `deviceId` hoặc `device_id` | có | Chuỗi 8–128 ký tự sau `normalizeDeviceId` |
| `note` | không | ≤ 500 ký tự |

**201:** `{ id, deviceId, deviceName, note, createdAt, createdByLabel: null }`

| HTTP | `error` |
|------|---------|
| **400** | `"Cần Device ID"` / `"Device ID không hợp lệ (8–128 ký tự)"` |
| **409** | `"Thiết bị này đã có trong danh sách chặn"` |
| **500** | `"Không thêm được thiết bị vào danh sách chặn"` |

**Side effect:** `refreshDeviceDenylistFromDb()`.

### `DELETE /blocked-devices/:id` {#delete-blocked-devices--id}

Bỏ chặn thiết bị theo id bảng `blocked_devices`. Route: `requireAuth` + **super_admin** trong handler.

**URL:** `DELETE /api/blocked-devices/:id`

**Quyền:** super_admin. Path `id` — integer > 0.

| HTTP | Body |
|------|------|
| **400** | `{ "error": "ID không hợp lệ" }` |
| **404** | `{ "error": "Không tìm thấy thiết bị trong danh sách" }` |
| **200** | `{ "ok": true }` |
| **500** | `{ "error": "Không xóa được thiết bị khỏi danh sách" }` |

**Side effect:** `refreshDeviceDenylistFromDb()`.

## Ghi chú đọc mã

- Gắn prefix `/api` trong `app.ts`; file route: `routes/index.ts` → `./blocked-devices.ts`.
- Handler đầy đủ: mở file TypeScript tại Shop (tìm theo chuỗi path).
- Quyền role: `tham-chieu/phan-quyen-rbac/README.md` (tiếng Anh gốc) + các `require*` trong từng endpoint.

**Đọc tiếp:** [Hướng dẫn Map](../../huong-dan-doc/) · [Mục lục](../../README.md)

## Luồng nghiệp vụ liên quan

- `nghiep-vu/10-truy-cap-an-ninh/README.md`
- UI: `trang/chan-truy-cap/README.md`
- Middleware: `thu-vien/ip-denylist/README.md`, `thu-vien/device-denylist/README.md`, `thu-vien/api-access-observations/README.md`
