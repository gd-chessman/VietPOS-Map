# Truy cập và an ninh

**Mô tả:** Chặn IP/thiết bị, quan sát truy cập và RBAC liên quan.

## Mục đích

Bảo vệ API khỏi client lạ (IP / thiết bị) và cho **super admin** quan sát ai đang gọi `/api` trước khi quyết định chặn.

## Lớp bảo vệ (thứ tự trong `app.ts`)

| Lớp | File lib | Hành vi |
|-----|----------|---------|
| Quan sát | `api-access-observations.ts` | Ghi cặp deviceId+IP, đếm hit; **không** chặn |
| Chặn IP | `ip-denylist.ts` | 403 nếu IP trong DB hoặc env `IP_DENYLIST` / `BLOCKED_IPS` |
| Chặn thiết bị | `device-denylist.ts` | 403 nếu `deviceId` header trong `blocked_devices` |

Cache denylist refresh định kỳ + ngay sau POST/DELETE từ UI admin.

## UI quản trị

**Đường dẫn:** `/access-block` — menu **Chặn truy cập** (chỉ `super_admin`).

| Tab | Component | Chức năng |
|-----|-----------|-----------|
| Tổng quan | `AccessOverviewSection` | Bảng quan sát RAM, chặn nhanh |
| Chặn IP | `IpBanSection` | CRUD bảng `blocked_ips` |
| Chặn thiết bị | `DeviceBanSection` | CRUD bảng `blocked_devices` |

URL cũ `/ip-ban`, `/device-ban` redirect sang `?tab=`.

## API modules

- `GET/POST/DELETE /api/blocked-ips` — `routes/blocked-ips.ts`
- `GET/POST/DELETE /api/blocked-devices` — `routes/blocked-devices.ts`
- `GET /api/access-observations` — `routes/access-observations.ts`

Tất cả yêu cầu JWT + **`super_admin`**.

## Database

- `blocked_ips` — cột `ip`, `note`, `created_by` → users
- `blocked_devices` — `device_id`, `note`, `created_by`
- Quan sát: **không** có bảng Postgres (in-memory TTL)

## RBAC liên quan khác

- Menu POS / quyền shop: `lib/session-permissions.ts`, `tham-chieu/rbac/README.md`
- **Device login events** / **allowed devices**: schema riêng — đăng nhập thiết bị tin cậy, khác denylist

## Frontend docs

- `trang/chan-truy-cap/README.md`
- `trang/tong-quan-truy-cap/README.md`
- `trang/chan-ip/README.md`, `device-ban.md`

**Mirror:** `tham-chieu/rbac/README.md`, `tham-chieu/public-access/README.md`.
