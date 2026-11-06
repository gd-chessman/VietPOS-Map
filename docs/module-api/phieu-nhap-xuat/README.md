# Module API: `stock-requests`

**Mô tả:** Module API stock-requests.ts — 14 endpoint. Phiếu yêu cầu nhập/xuất nội bộ: tạo → duyệt → hoàn tất → cập nhật tồn. Giao diện: pages/stock-requests.tsx.

**Mã nguồn Shop:** `artifacts/api-server/src/routes/stock-requests.ts`

Phiếu yêu cầu nhập/xuất nội bộ: tạo → duyệt → hoàn tất → cập nhật tồn.

**Giao diện:** `pages/stock-requests.tsx`.

**Số endpoint:** 14

**Contract API:** Mỗi endpoint có mục **URL**, body/query (từ code + schema Zod orval khi có), bảng lỗi `error`, và response (Zod hoặc trường `res.json`).

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

**URL:** `GET /api/stock-requests`

**Lớp route:** `requireAuth`

*Handler không trích được contract tự động — mở file route TypeScript.*

### `GET /stock-requests/pending-count` {#get-stock-requests-pending-count}

Đường dẫn đầy đủ `/api/stock-requests/pending-count`. Lớp kiểm tra: `requireAuth`.

**URL:** `GET /api/stock-requests/pending-count`

**Lớp route:** `requireAuth`
- **Thêm trong handler:** role **`super_admin`** (403 nếu không đủ).

**Response 200** — trường top-level (trích `res.json`):

`count`

### `GET /stock-requests/approved-count` {#get-stock-requests-approved-count}

Đường dẫn đầy đủ `/api/stock-requests/approved-count`. Lớp kiểm tra: `requireAuth`.

**URL:** `GET /api/stock-requests/approved-count`

**Lớp route:** `requireAuth`
- **Thêm trong handler:** role **`super_admin`** (403 nếu không đủ).

**Response 200** — trường top-level (trích `res.json`):

`count`

### `GET /stock-requests/in-transit-count` {#get-stock-requests-in-transit-count}

Đường dẫn đầy đủ `/api/stock-requests/in-transit-count`. Lớp kiểm tra: `requireAuth`.

**URL:** `GET /api/stock-requests/in-transit-count`

**Lớp route:** `requireAuth`
- **Thêm trong handler:** role **`super_admin`** (403 nếu không đủ).

**Response 200** — trường top-level (trích `res.json`):

`count`

### `GET /stock-requests/meta/hub-shop` {#get-stock-requests-meta-hub-shop}

Đường dẫn đầy đủ `/api/stock-requests/meta/hub-shop`. Lớp kiểm tra: `requireAuth`.

**URL:** `GET /api/stock-requests/meta/hub-shop`

**Lớp route:** `requireAuth`

**Lỗi JSON** (`error` string):

| HTTP | Message |
|------|---------|
| **404** | `Không xác định kho tổng` |

### `GET /stock-requests/meta/hub-inventory` {#get-stock-requests-meta-hub-inventory}

Đường dẫn đầy đủ `/api/stock-requests/meta/hub-inventory`. Lớp kiểm tra: `requireAuth`.

**URL:** `GET /api/stock-requests/meta/hub-inventory`

**Lớp route:** `requireAuth`

*Handler không trích được contract tự động — mở file route TypeScript.*

### `GET /stock-requests/meta/shop-inventory` {#get-stock-requests-meta-shop-inventory}

Đường dẫn đầy đủ `/api/stock-requests/meta/shop-inventory`. Lớp kiểm tra: `requireAuth`.

**URL:** `GET /api/stock-requests/meta/shop-inventory`

**Lớp route:** `requireAuth`

**Lỗi JSON** (`error` string):

| HTTP | Message |
|------|---------|
| **400** | `shopId không hợp lệ` |
| **403** | `Không có quyền xem tồn chi nhánh này` |

### `GET /stock-requests/:id` {#get-stock-requests--id}

Đường dẫn đầy đủ `/api/stock-requests/:id`. Lớp kiểm tra: `requireAuth`.

**URL:** `GET /api/stock-requests/:id`

**Lớp route:** `requireAuth`

**Lỗi JSON** (`error` string):

| HTTP | Message |
|------|---------|
| **400** | `Invalid ID` |
| **404** | `Not found` |
| **403** | `Forbidden` |

### `POST /stock-requests` {#post-stock-requests}

Đường dẫn đầy đủ `/api/stock-requests`. Lớp kiểm tra: `requireAuth`.

**URL:** `POST /api/stock-requests`

**Lớp route:** `requireAuth`

**Lỗi JSON** (`error` string):

| HTTP | Message |
|------|---------|
| **400** | `requestType must be 'import' or 'export'` |
| **400** | `items must be a non-empty array` |
| **400** | `Danh sách sản phẩm/biến thể có trùng lặp` |
| **400** | `Mỗi dòng cần productId và số lượng > 0` |

### `PATCH /stock-requests/:id/approve` {#patch-stock-requests--id-approve}

Đường dẫn đầy đủ `/api/stock-requests/:id/approve`. Lớp kiểm tra: `requireAuth`.

**URL:** `PATCH /api/stock-requests/:id/approve`

**Lớp route:** `requireAuth`

**Lỗi JSON** (`error` string):

| HTTP | Message |
|------|---------|
| **404** | `Not found` |
| **403** | `Không có quyền duyệt phiếu này` |

### `PATCH /stock-requests/:id/ship` {#patch-stock-requests--id-ship}

Đường dẫn đầy đủ `/api/stock-requests/:id/ship`. Lớp kiểm tra: `requireAuth`.

**URL:** `PATCH /api/stock-requests/:id/ship`

**Lớp route:** `requireAuth`

**Lỗi JSON** (`error` string):

| HTTP | Message |
|------|---------|
| **404** | `Not found` |
| **403** | `Không có quyền xác nhận vận chuyển phiếu này` |

**Response 200** — trường top-level (trích `res.json`):

`tại`

### `PATCH /stock-requests/:id/reject` {#patch-stock-requests--id-reject}

Đường dẫn đầy đủ `/api/stock-requests/:id/reject`. Lớp kiểm tra: `requireAuth`.

**URL:** `PATCH /api/stock-requests/:id/reject`

**Lớp route:** `requireAuth`

**Lỗi JSON** (`error` string):

| HTTP | Message |
|------|---------|
| **404** | `Not found` |
| **403** | `Không có quyền từ chối phiếu này` |

### `PATCH /stock-requests/:id/complete` {#patch-stock-requests--id-complete}

Đường dẫn đầy đủ `/api/stock-requests/:id/complete`. Lớp kiểm tra: `requireAuth`.

**URL:** `PATCH /api/stock-requests/:id/complete`

**Lớp route:** `requireAuth`

**Lỗi JSON** (`error` string):

| HTTP | Message |
|------|---------|
| **404** | `Not found` |
| **403** | `Không có quyền xác nhận nhận hàng phiếu nhập này` |
| **403** | `Không có quyền xác nhận nhận hàng phiếu xuất này` |

**Response 200** — trường top-level (trích `res.json`):

`tại`

### `PATCH /stock-requests/:id/cancel` {#patch-stock-requests--id-cancel}

Đường dẫn đầy đủ `/api/stock-requests/:id/cancel`. Lớp kiểm tra: `requireAuth`.

**URL:** `PATCH /api/stock-requests/:id/cancel`

**Lớp route:** `requireAuth`

**Lỗi JSON** (`error` string):

| HTTP | Message |
|------|---------|
| **404** | `Not found` |

## Ghi chú đọc mã

- Gắn prefix `/api` trong `app.ts`; file route: `routes/index.ts` → `./stock-requests.ts`.
- Handler đầy đủ: mở file TypeScript tại Shop (tìm theo chuỗi path).
- Quyền role: `tham-chieu/phan-quyen-rbac/README.md` (tiếng Anh gốc) + các `require*` trong từng endpoint.

**Đọc tiếp:** [Hướng dẫn Map](../../huong-dan-doc/) · [Mục lục](../../README.md)
