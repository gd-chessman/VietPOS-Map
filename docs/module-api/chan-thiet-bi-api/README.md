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
| GET | `/blocked-devices` | Liệt kê thiết bị bị chặn (tương tự IP) |
| POST | `/blocked-devices` | Thêm device id; validate qua `isValidBlockedDeviceId` |
| DELETE | `/blocked-devices/:id` | Bỏ chặn thiết bị |

## Chi tiết từng endpoint

### `GET /blocked-devices` {#get-blocked-devices}

Liệt kê thiết bị bị chặn (tương tự IP). Lớp kiểm tra: `requireAuth`.

- **Lớp kiểm tra (middleware):** `requireAuth`

### `POST /blocked-devices` {#post-blocked-devices}

Thêm device id; validate qua `isValidBlockedDeviceId`. Lớp kiểm tra: `requireAuth`.

- **Lớp kiểm tra (middleware):** `requireAuth`

### `DELETE /blocked-devices/:id` {#delete-blocked-devices--id}

Bỏ chặn thiết bị. Lớp kiểm tra: `requireAuth`.

- **Lớp kiểm tra (middleware):** `requireAuth`

## Ghi chú đọc mã

- Gắn prefix `/api` trong `app.ts`; file route: `routes/index.ts` → `./blocked-devices.ts`.
- Handler đầy đủ: mở file TypeScript tại Shop (tìm theo chuỗi path).
- Quyền role: `tham-chieu/phan-quyen-rbac/README.md` (tiếng Anh gốc) + các `require*` trong từng endpoint.

**Đọc tiếp:** [Hướng dẫn Map](../../huong-dan-doc/) · [Mục lục](../../README.md)

## Luồng nghiệp vụ liên quan

- `nghiep-vu/10-truy-cap-an-ninh/README.md`
- UI: `trang/chan-truy-cap/README.md`
- Middleware: `thu-vien/ip-denylist/README.md`, `thu-vien/device-denylist/README.md`, `thu-vien/api-access-observations/README.md`
