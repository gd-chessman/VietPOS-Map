# Module API: `feedback`

**Mô tả:** Module API feedback.ts — 5 endpoint. Phản hồi khách và form công khai.

**Mã nguồn Shop:** `artifacts/api-server/src/routes/feedback.ts`

Phản hồi khách và form công khai.

**Số endpoint:** 5

**Contract API:** Mỗi endpoint có mục **URL**, body/query (từ code + schema Zod orval khi có), bảng lỗi `error`, và response (Zod hoặc trường `res.json`).

## Bảng endpoint (tóm tắt)

| Method | Path | Mô tả ngắn |
|--------|------|------------|
| POST | `/public/feedback` | Đường dẫn đầy đủ `/api/public/feedback` |
| GET | `/feedback/public-url` | Đường dẫn đầy đủ `/api/feedback/public-url` |
| PATCH | `/feedback/public-url` | Đường dẫn đầy đủ `/api/feedback/public-url` |
| GET | `/feedback/stats` | Đường dẫn đầy đủ `/api/feedback/stats` |
| GET | `/feedback` | Đường dẫn đầy đủ `/api/feedback` |

## Chi tiết từng endpoint

### `POST /public/feedback` {#post-public-feedback}

Đường dẫn đầy đủ `/api/public/feedback`. Lớp kiểm tra: `requireAuth (mặc định — xem file)`.

**URL:** `POST /api/public/feedback`

**Lớp route:** `requireAuth` (hoặc public — xem route)

**Lỗi JSON** (`error` string):

| HTTP | Message |
|------|---------|
| **400** | `Cửa hàng không tồn tại` |

**Response 201** — trường top-level (trích `res.json`):

`createdAt`, `id`, `ok`

### `GET /feedback/public-url` {#get-feedback-public-url}

Đường dẫn đầy đủ `/api/feedback/public-url`. Lớp kiểm tra: `requireAuth`.

**URL:** `GET /api/feedback/public-url`

**Lớp route:** `requireAuth`

*Handler không trích được contract tự động — mở file route TypeScript.*

### `PATCH /feedback/public-url` {#patch-feedback-public-url}

Đường dẫn đầy đủ `/api/feedback/public-url`. Lớp kiểm tra: `requireAuth, requireManagerOrAdmin`.

**URL:** `PATCH /api/feedback/public-url`

**Lớp route:** `requireAuth`, `requireManagerOrAdmin`

**Lỗi JSON** (`error` string):

| HTTP | Message |
|------|---------|
| **403** | `Không xác định được tổ chức` |
| **400** | `Tài khoản hệ thống cần đăng nhập theo chi nhánh để cấu hình URL` |
| **400** | `Cần url (URL gốc công khai)` |
| **404** | `Tổ chức không tồn tại` |

### `GET /feedback/stats` {#get-feedback-stats}

Đường dẫn đầy đủ `/api/feedback/stats`. Lớp kiểm tra: `requireAuth, requireManagerOrAdmin`.

**URL:** `GET /api/feedback/stats`

**Lớp route:** `requireAuth`, `requireManagerOrAdmin`

**Query:** `shopId`

**Lỗi JSON** (`error` string):

| HTTP | Message |
|------|---------|
| **403** | `Không có quyền xem cửa hàng này` |

**Response 200** — trường top-level (trích `res.json`):

`avg`, `total`

### `GET /feedback` {#get-feedback}

Đường dẫn đầy đủ `/api/feedback`. Lớp kiểm tra: `requireAuth, requireManagerOrAdmin`.

**URL:** `GET /api/feedback`

**Lớp route:** `requireAuth`, `requireManagerOrAdmin`

**Query:** `limit`, `page`, `shopId`

**Lỗi JSON** (`error` string):

| HTTP | Message |
|------|---------|
| **403** | `Không có quyền xem cửa hàng này` |

**Response 200** — trường top-level (trích `res.json`):

`items`

## Ghi chú đọc mã

- Gắn prefix `/api` trong `app.ts`; file route: `routes/index.ts` → `./feedback.ts`.
- Handler đầy đủ: mở file TypeScript tại Shop (tìm theo chuỗi path).
- Quyền role: `tham-chieu/phan-quyen-rbac/README.md` (tiếng Anh gốc) + các `require*` trong từng endpoint.

**Đọc tiếp:** [Hướng dẫn Map](../../huong-dan-doc/) · [Mục lục](../../README.md)
