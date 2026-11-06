# Module API: `stock-requests`

**Mô tả:** Module API stock-requests.ts — 14 endpoint. Phiếu yêu cầu nhập/xuất nội bộ: tạo → duyệt → hoàn tất → cập nhật tồn. Giao diện: pages/stock-requests.tsx.

**Mã nguồn Shop:** `artifacts/api-server/src/routes/stock-requests.ts`

Phiếu yêu cầu nhập/xuất nội bộ: tạo → duyệt → hoàn tất → cập nhật tồn.

**Giao diện:** `pages/stock-requests.tsx`.

**Số endpoint:** 14

## Bảng endpoint (tóm tắt)

| Method | Path | Mô tả ngắn |
|--------|------|------------|
| GET | `/stock-requests` | Đường dẫn đầy đủ `/api/stock-requests` |
| GET | `/stock-requests/pending-count` | Đường dẫn đầy đủ `/api/stock-requests/pending-count` |
| GET | `/stock-requests/approved-count` | Đường dẫn đầy đủ `/api/stock-requests/approved-count` |
| GET | `/stock-requests/in-transit-count` | Đường dẫn đầy đủ `/api/stock-requests/in-transit-count` |
| GET | `/stock-requests/meta/hub-shop` | Đường dẫn đầy đủ `/api/stock-requests/meta/hub-shop` |
| GET | `/stock-requests/meta/hub-inventory` | Đường dẫn đầy đủ `/api/stock-requests/meta/hub-inventory` |
| GET | `/stock-requests/meta/shop-inventory` | Đường dẫn đầy đủ `/api/stock-requests/meta/shop-inventory` |
| GET | `/stock-requests/:id` | Đường dẫn đầy đủ `/api/stock-requests/:id` |
| POST | `/stock-requests` | Đường dẫn đầy đủ `/api/stock-requests` |
| PATCH | `/stock-requests/:id/approve` | Đường dẫn đầy đủ `/api/stock-requests/:id/approve` |
| PATCH | `/stock-requests/:id/ship` | Đường dẫn đầy đủ `/api/stock-requests/:id/ship` |
| PATCH | `/stock-requests/:id/reject` | Đường dẫn đầy đủ `/api/stock-requests/:id/reject` |
| PATCH | `/stock-requests/:id/complete` | Đường dẫn đầy đủ `/api/stock-requests/:id/complete` |
| PATCH | `/stock-requests/:id/cancel` | Đường dẫn đầy đủ `/api/stock-requests/:id/cancel` |

## Chi tiết từng endpoint

### `GET /stock-requests` {#get-stock-requests}

Đường dẫn đầy đủ `/api/stock-requests`. Lớp kiểm tra: `requireAuth`.

- **Lớp kiểm tra (middleware):** `requireAuth`

### `GET /stock-requests/pending-count` {#get-stock-requests-pending-count}

Đường dẫn đầy đủ `/api/stock-requests/pending-count`. Lớp kiểm tra: `requireAuth`.

- **Lớp kiểm tra (middleware):** `requireAuth`

### `GET /stock-requests/approved-count` {#get-stock-requests-approved-count}

Đường dẫn đầy đủ `/api/stock-requests/approved-count`. Lớp kiểm tra: `requireAuth`.

- **Lớp kiểm tra (middleware):** `requireAuth`

### `GET /stock-requests/in-transit-count` {#get-stock-requests-in-transit-count}

Đường dẫn đầy đủ `/api/stock-requests/in-transit-count`. Lớp kiểm tra: `requireAuth`.

- **Lớp kiểm tra (middleware):** `requireAuth`

### `GET /stock-requests/meta/hub-shop` {#get-stock-requests-meta-hub-shop}

Đường dẫn đầy đủ `/api/stock-requests/meta/hub-shop`. Lớp kiểm tra: `requireAuth`.

- **Lớp kiểm tra (middleware):** `requireAuth`

### `GET /stock-requests/meta/hub-inventory` {#get-stock-requests-meta-hub-inventory}

Đường dẫn đầy đủ `/api/stock-requests/meta/hub-inventory`. Lớp kiểm tra: `requireAuth`.

- **Lớp kiểm tra (middleware):** `requireAuth`

### `GET /stock-requests/meta/shop-inventory` {#get-stock-requests-meta-shop-inventory}

Đường dẫn đầy đủ `/api/stock-requests/meta/shop-inventory`. Lớp kiểm tra: `requireAuth`.

- **Lớp kiểm tra (middleware):** `requireAuth`

### `GET /stock-requests/:id` {#get-stock-requests--id}

Đường dẫn đầy đủ `/api/stock-requests/:id`. Lớp kiểm tra: `requireAuth`.

- **Lớp kiểm tra (middleware):** `requireAuth`

### `POST /stock-requests` {#post-stock-requests}

Đường dẫn đầy đủ `/api/stock-requests`. Lớp kiểm tra: `requireAuth`.

- **Lớp kiểm tra (middleware):** `requireAuth`

### `PATCH /stock-requests/:id/approve` {#patch-stock-requests--id-approve}

Đường dẫn đầy đủ `/api/stock-requests/:id/approve`. Lớp kiểm tra: `requireAuth`.

- **Lớp kiểm tra (middleware):** `requireAuth`

### `PATCH /stock-requests/:id/ship` {#patch-stock-requests--id-ship}

Đường dẫn đầy đủ `/api/stock-requests/:id/ship`. Lớp kiểm tra: `requireAuth`.

- **Lớp kiểm tra (middleware):** `requireAuth`

### `PATCH /stock-requests/:id/reject` {#patch-stock-requests--id-reject}

Đường dẫn đầy đủ `/api/stock-requests/:id/reject`. Lớp kiểm tra: `requireAuth`.

- **Lớp kiểm tra (middleware):** `requireAuth`

### `PATCH /stock-requests/:id/complete` {#patch-stock-requests--id-complete}

Đường dẫn đầy đủ `/api/stock-requests/:id/complete`. Lớp kiểm tra: `requireAuth`.

- **Lớp kiểm tra (middleware):** `requireAuth`

### `PATCH /stock-requests/:id/cancel` {#patch-stock-requests--id-cancel}

Đường dẫn đầy đủ `/api/stock-requests/:id/cancel`. Lớp kiểm tra: `requireAuth`.

- **Lớp kiểm tra (middleware):** `requireAuth`

## Ghi chú đọc mã

- Gắn prefix `/api` trong `app.ts`; file route: `routes/index.ts` → `./stock-requests.ts`.
- Handler đầy đủ: mở file TypeScript tại Shop (tìm theo chuỗi path).
- Quyền role: `tham-chieu/phan-quyen-rbac/README.md` (tiếng Anh gốc) + các `require*` trong từng endpoint.

**Đọc tiếp:** [Hướng dẫn Map](../../huong-dan-doc/) · [Mục lục](../../README.md)
