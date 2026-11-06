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

**Contract API:** Mỗi endpoint có mục **URL**, body/query (từ code + schema Zod orval khi có), bảng lỗi `error`, và response (Zod hoặc trường `res.json`).

## Bảng endpoint (tóm tắt)

| Method | Path | Mô tả ngắn |
|--------|------|------------|
| GET | `/blocked-ips` | Liệt kê IP bị chặn; kèm IP client đang xem và cờ denylist từ env |
| POST | `/blocked-ips` | Thêm một IP vào `blocked_ips`; refresh cache denylist |
| DELETE | `/blocked-ips/:id` | Xóa một dòng `blocked_ips` theo id; refresh cache |

## Chi tiết từng endpoint

### `GET /blocked-ips` {#get-blocked-ips}

Liệt kê IP bị chặn; kèm IP client đang xem và cờ denylist từ env. Route: `requireAuth` + **super_admin** trong handler.

**URL:** `GET /api/blocked-ips`

**Quyền:** Cookie/JWT qua `requireAuth` → trong handler bắt buộc `req.auth.role === "super_admin"`.

| HTTP | Khi nào | Body lỗi (JSON) |
|------|---------|-----------------|
| **403** | Không phải super_admin | `{ "error": "Chỉ quản trị hệ thống được quản lý IP bị chặn" }` |
| **500** | Lỗi DB / chưa có bảng | `{ "error": "Không tải được danh sách IP. Cập nhật cơ sở dữ liệu (pnpm --filter @workspace/db push) rồi thử lại." }` |

**Response 200:**

| Trường | Kiểu | Ý nghĩa |
|--------|------|---------|
| `items[]` | array | Mỗi phần tử: `id`, `ip`, `note`, `createdAt` (ISO), `createdByLabel` (tên hoặc email người tạo) |
| `envDenylistEnabled` | boolean | `true` nếu có `IP_DENYLIST` hoặc `BLOCKED_IPS` trong env (chặn thêm ngoài DB) |
| `seenClientIp` | string | IP đã dùng để đối chiếu denylist (proxy-aware) |
| `socketIp` | string | IP socket trực tiếp |
| `trustProxy` | boolean | Express trust proxy |
| `xForwardedFor` | string \| null | Header X-Forwarded-For nếu có |

**Side effect:** không đổi DB (chỉ đọc). Sau POST/DELETE module khác gọi `refreshIpDenylistFromDb()`.

### `POST /blocked-ips` {#post-blocked-ips}

Thêm một IP vào `blocked_ips`; refresh cache denylist. Route: `requireAuth` + **super_admin** trong handler.

**URL:** `POST /api/blocked-ips`

**Quyền:** `requireAuth` + **super_admin** (403 giống GET).

**Request body** (`application/json`):

| Trường | Bắt buộc | Mô tả |
|--------|----------|--------|
| `ip` | có | Chuỗi IPv4/IPv6; server `normalizeClientIp` + `isValidBlockedIp` |
| `note` | không | Ghi chú, tối đa 500 ký tự |

**Response 201:** `{ id, ip, note, createdAt, createdByLabel: null }`

| HTTP | Khi nào | `error` |
|------|---------|---------|
| **400** | Thiếu/sai `ip` | `"Cần địa chỉ IP"` hoặc `"Địa chỉ IP không hợp lệ"` |
| **409** | Trùng IP (unique) | `"IP này đã có trong danh sách chặn"` |
| **500** | Lỗi insert | `"Không thêm được IP vào danh sách chặn"` |

**Side effect:** insert `blocked_ips`; gọi `refreshIpDenylistFromDb()` — middleware chặn IP ngay trên mọi `/api/*`.

### `DELETE /blocked-ips/:id` {#delete-blocked-ips--id}

Xóa một dòng `blocked_ips` theo id; refresh cache. Route: `requireAuth` + **super_admin** trong handler.

**URL:** `DELETE /api/blocked-ips/:id`

**Quyền:** `requireAuth` + **super_admin**.

**Path:** `id` — số nguyên dương (PK bảng `blocked_ips`).

| HTTP | Khi nào | Body |
|------|---------|------|
| **400** | `id` không hợp lệ | `{ "error": "ID không hợp lệ" }` |
| **404** | Không có dòng | `{ "error": "Không tìm thấy IP trong danh sách" }` |
| **200** | OK | `{ "ok": true }` |
| **500** | Lỗi xóa | `{ "error": "Không xóa được IP khỏi danh sách" }` |

**Side effect:** `refreshIpDenylistFromDb()`.

## Ghi chú đọc mã

- Gắn prefix `/api` trong `app.ts`; file route: `routes/index.ts` → `./blocked-ips.ts`.
- Handler đầy đủ: mở file TypeScript tại Shop (tìm theo chuỗi path).
- Quyền role: `tham-chieu/phan-quyen-rbac/README.md` (tiếng Anh gốc) + các `require*` trong từng endpoint.

**Đọc tiếp:** [Hướng dẫn Map](../../huong-dan-doc/) · [Mục lục](../../README.md)

## Luồng nghiệp vụ liên quan

- `nghiep-vu/10-truy-cap-an-ninh/README.md`
- UI: `trang/chan-truy-cap/README.md`
- Middleware: `thu-vien/ip-denylist/README.md`, `thu-vien/device-denylist/README.md`, `thu-vien/api-access-observations/README.md`
