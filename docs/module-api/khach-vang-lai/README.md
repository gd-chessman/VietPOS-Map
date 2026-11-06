# Module API: `walk-in-customers`

**Mô tả:** Module API walk-in-customers.ts — 2 endpoint. Khách vãng lai (walk-in).

**Mã nguồn Shop:** `artifacts/api-server/src/routes/walk-in-customers.ts`

Khách vãng lai (walk-in).

**Số endpoint:** 2

**Contract API:** Mỗi endpoint có mục **URL**, body/query (từ code + schema Zod orval khi có), bảng lỗi `error`, và response (Zod hoặc trường `res.json`).

## Bảng endpoint (tóm tắt)

| Method | Path | Mô tả ngắn |
|--------|------|------------|
| GET | `/shops/:shopId/walk-in-customers/today` | Đường dẫn đầy đủ `/api/shops/:shopId/walk-in-customers/today` |
| POST | `/shops/:shopId/walk-in-customers` | Đường dẫn đầy đủ `/api/shops/:shopId/walk-in-customers` |

## Chi tiết từng endpoint

### `GET /shops/:shopId/walk-in-customers/today` {#get-shops--shopId-walk-in-customers-today}

Đường dẫn đầy đủ `/api/shops/:shopId/walk-in-customers/today`. Lớp kiểm tra: `requireAuth`.

**URL:** `GET /api/shops/:shopId/walk-in-customers/today`

**Lớp route:** `requireAuth`

**Path params:** `shopId`

**Lỗi JSON** (`error` string):

| HTTP | Message |
|------|---------|
| **400** | `Invalid shop id` |
| **403** | `Forbidden` |

**Response 200** — trường top-level (trích `res.json`):

`beams`, `count`

### `POST /shops/:shopId/walk-in-customers` {#post-shops--shopId-walk-in-customers}

Đường dẫn đầy đủ `/api/shops/:shopId/walk-in-customers`. Lớp kiểm tra: `requireAuth, requireOperationalContext`.

**URL:** `POST /api/shops/:shopId/walk-in-customers`

**Lớp route:** `requireAuth`, `requireOperationalContext`

**Request body** (`application/json`, trích từ code):

| Trường | Ghi chú |
|--------|---------|
| `add` | xem handler |
| `quantity` | xem handler |

**Path params:** `shopId`

**Lỗi JSON** (`error` string):

| HTTP | Message |
|------|---------|
| **400** | `Invalid shop id` |
| **403** | `Forbidden` |
| **403** | `Cửa hàng đã tắt nhập khách thủ công` |
| **400** | `Số khách phải >= 1` |

**Response 201** — trường top-level (trích `res.json`):

`count`

## Ghi chú đọc mã

- Gắn prefix `/api` trong `app.ts`; file route: `routes/index.ts` → `./walk-in-customers.ts`.
- Handler đầy đủ: mở file TypeScript tại Shop (tìm theo chuỗi path).
- Quyền role: `tham-chieu/phan-quyen-rbac/README.md` (tiếng Anh gốc) + các `require*` trong từng endpoint.

**Đọc tiếp:** [Hướng dẫn Map](../../huong-dan-doc/) · [Mục lục](../../README.md)
