# Module API: `blocked-ips`

**Mô tả:** Module API blocked-ips.ts — 3 endpoint. Danh sách IP bị chặn toàn cục trên mọi request /api/*. - Quyền: requireAuth + role super_admin (403 nếu không đủ). - Sa…

**Mã nguồn Shop:** `artifacts/api-server/src/routes/blocked-ips.ts`

Danh sách IP bị chặn toàn cục trên **mọi** request `/api/*`.

- **Quyền:** `requireAuth` + role **`super_admin`** (403 nếu không đủ).
- Sau POST/DELETE: gọi `refreshIpDenylistFromDb()` — cache in-memory middleware cập nhật ngay.
- GET trả thêm `envDenylistEnabled` (biến `IP_DENYLIST` / `BLOCKED_IPS`) và `describeSeenClientIp(req)`.

**Middleware:** `ipDenylistMiddleware()` mount trên `/api` trong `app.ts` (trước router).

**Lib:** `lib/ip-denylist.ts`. **UI:** tab **Chặn IP** trong `access-block.tsx` → `IpBanSection`.

**Số endpoint:** 3

## Bảng endpoint (tóm tắt)

| Method | Path | Mô tả ngắn |
|--------|------|------------|
| GET | `/blocked-ips` | Liệt kê `blocked_ips` + nhãn người tạo; kèm cờ env denylist và IP client hiện tại |
| POST | `/blocked-ips` | Thêm IP (normalize IPv4/IPv6); body `{ ip, note? }`; refresh denylist cache |
| DELETE | `/blocked-ips/:id` | Xóa một dòng; refresh denylist cache |

## Chi tiết từng endpoint

### `GET /blocked-ips` {#get-blocked-ips}

Liệt kê `blocked_ips` + nhãn người tạo; kèm cờ env denylist và IP client hiện tại. Lớp kiểm tra: `requireAuth`.

- **Lớp kiểm tra (middleware):** `requireAuth`

### `POST /blocked-ips` {#post-blocked-ips}

Thêm IP (normalize IPv4/IPv6); body `{ ip, note? }`; refresh denylist cache. Lớp kiểm tra: `requireAuth`.

- **Lớp kiểm tra (middleware):** `requireAuth`

### `DELETE /blocked-ips/:id` {#delete-blocked-ips--id}

Xóa một dòng; refresh denylist cache. Lớp kiểm tra: `requireAuth`.

- **Lớp kiểm tra (middleware):** `requireAuth`

## Ghi chú đọc mã

- Gắn prefix `/api` trong `app.ts`; file route: `routes/index.ts` → `./blocked-ips.ts`.
- Handler đầy đủ: mở file TypeScript tại Shop (tìm theo chuỗi path).
- Quyền role: `tham-chieu/phan-quyen-rbac/README.md` (tiếng Anh gốc) + các `require*` trong từng endpoint.

**Đọc tiếp:** [Hướng dẫn Map](../../huong-dan-doc/) · [Mục lục](../../README.md)

## Luồng nghiệp vụ liên quan

- `nghiep-vu/10-truy-cap-an-ninh/README.md`
- UI: `trang/chan-truy-cap/README.md`
- Middleware: `thu-vien/ip-denylist/README.md`, `thu-vien/device-denylist/README.md`, `thu-vien/api-access-observations/README.md`
