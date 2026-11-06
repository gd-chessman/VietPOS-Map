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
| GET | `/access-observations` | Query `?limit=` (mặc định 200); trả `items`, thống kê `today`, `ttlHours`, `storage: memory`… |

## Chi tiết từng endpoint

### `GET /access-observations` {#get-access-observations}

Query `?limit=` (mặc định 200); trả `items`, thống kê `today`, `ttlHours`, `storage: memory`. Lớp kiểm tra: `requireAuth`.

- **Lớp kiểm tra (middleware):** `requireAuth`

## Ghi chú đọc mã

- Gắn prefix `/api` trong `app.ts`; file route: `routes/index.ts` → `./access-observations.ts`.
- Handler đầy đủ: mở file TypeScript tại Shop (tìm theo chuỗi path).
- Quyền role: `tham-chieu/phan-quyen-rbac/README.md` (tiếng Anh gốc) + các `require*` trong từng endpoint.

**Đọc tiếp:** [Hướng dẫn Map](../../huong-dan-doc/) · [Mục lục](../../README.md)

## Luồng nghiệp vụ liên quan

- `nghiep-vu/10-truy-cap-an-ninh/README.md`
- UI: `trang/chan-truy-cap/README.md`
- Middleware: `thu-vien/ip-denylist/README.md`, `thu-vien/device-denylist/README.md`, `thu-vien/api-access-observations/README.md`
