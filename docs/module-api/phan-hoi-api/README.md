# Module API: `feedback`

**Mô tả:** Module API feedback.ts — 5 endpoint. Phản hồi khách và form công khai.

**Mã nguồn Shop:** `artifacts/api-server/src/routes/feedback.ts`

Phản hồi khách và form công khai.

**Số endpoint:** 5

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

### `GET /feedback/public-url` {#get-feedback-public-url}

Đường dẫn đầy đủ `/api/feedback/public-url`. Lớp kiểm tra: `requireAuth`.

- **Lớp kiểm tra (middleware):** `requireAuth`

### `PATCH /feedback/public-url` {#patch-feedback-public-url}

Đường dẫn đầy đủ `/api/feedback/public-url`. Lớp kiểm tra: `requireAuth, requireManagerOrAdmin`.

- **Lớp kiểm tra (middleware):** `requireAuth`, `requireManagerOrAdmin`

### `GET /feedback/stats` {#get-feedback-stats}

Đường dẫn đầy đủ `/api/feedback/stats`. Lớp kiểm tra: `requireAuth, requireManagerOrAdmin`.

- **Lớp kiểm tra (middleware):** `requireAuth`, `requireManagerOrAdmin`

### `GET /feedback` {#get-feedback}

Đường dẫn đầy đủ `/api/feedback`. Lớp kiểm tra: `requireAuth, requireManagerOrAdmin`.

- **Lớp kiểm tra (middleware):** `requireAuth`, `requireManagerOrAdmin`

## Ghi chú đọc mã

- Gắn prefix `/api` trong `app.ts`; file route: `routes/index.ts` → `./feedback.ts`.
- Handler đầy đủ: mở file TypeScript tại Shop (tìm theo chuỗi path).
- Quyền role: `tham-chieu/phan-quyen-rbac/README.md` (tiếng Anh gốc) + các `require*` trong từng endpoint.

**Đọc tiếp:** [Hướng dẫn Map](../../huong-dan-doc/) · [Mục lục](../../README.md)
