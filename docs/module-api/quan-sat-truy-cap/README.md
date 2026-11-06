# Module API: `access-observations`

**Mô tả:** Module API access-observations.ts — 1 endpoint. Tổng hợp cặp (deviceId, IP) đã gọi API — lưu in-memory (TTL giờ, xem accessObservationTtlHours). - Dùng tab Tổng quan t…

**Mã nguồn Shop:** `artifacts/api-server/src/routes/access-observations.ts`

Tổng hợp **cặp (deviceId, IP)** đã gọi API — lưu **in-memory** (TTL giờ, xem `accessObservationTtlHours`).

- Dùng tab **Tổng quan** trên `/access-block`: bảng hit count, chặn nhanh IP hoặc thiết bị từ một dòng.
- Ghi nhận qua `accessObservationMiddleware()` trên mọi `/api` (không chặn, chỉ quan sát).

**Lib:** `lib/api-access-observations.ts`. **UI:** `AccessOverviewSection`.

**Số endpoint:** 1

## Bảng endpoint (tóm tắt)

| Method | Path | Mô tả ngắn |
|--------|------|------------|
| GET | `/access-observations` | Bảng quan sát cặp deviceId+IP (RAM, TTL ~48h) |

## Chi tiết từng endpoint

### `GET /access-observations` {#get-access-observations}

Bảng quan sát cặp deviceId+IP (RAM, TTL ~48h). Route: `requireAuth` + **super_admin** trong handler.

**URL:** `GET /api/access-observations`

**Quyền:** super_admin (403: `"Chỉ quản trị hệ thống được xem tổng quan truy cập"`).

**Query:**

| Param | Mặc định | Mô tả |
|-------|----------|--------|
| `limit` | `200` | Số dòng trả về (parse number; NaN → 200) |

**Response 200:**

| Trường | Ý nghĩa |
|--------|---------|
| `items[]` | Mỗi dòng: `deviceId`, `ip`, `hitCount`, `todayHitCount`, `firstSeen`, `lastSeen` (ISO), `deviceName` |
| `today` | `{ calendarDay, totalHits, uniqueDevices, uniqueIps, activePairs }` — theo lịch VN |
| `ttlHours` | TTL store (lib: 48h) |
| `storage` | Luôn `"memory"` — **mất khi restart API** |

**Ghi nhận dữ liệu:** middleware `accessObservationMiddleware` trên mọi `/api` (không chặn).

**500:** `{ "error": "Không tải được tổng quan truy cập" }`

## Ghi chú đọc mã

- Gắn prefix `/api` trong `app.ts`; file route: `routes/index.ts` → `./access-observations.ts`.
- Handler đầy đủ: mở file TypeScript tại Shop (tìm theo chuỗi path).
- Quyền role: `tham-chieu/phan-quyen-rbac/README.md` (tiếng Anh gốc) + các `require*` trong từng endpoint.

**Đọc tiếp:** [Hướng dẫn Map](../../huong-dan-doc/) · [Mục lục](../../README.md)

## Luồng nghiệp vụ liên quan

- `nghiep-vu/10-truy-cap-an-ninh/README.md`
- UI: `trang/chan-truy-cap/README.md`
- Middleware: `thu-vien/ip-denylist/README.md`, `thu-vien/device-denylist/README.md`, `thu-vien/api-access-observations/README.md`
