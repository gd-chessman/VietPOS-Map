# Module API: `product-categories`

**Mô tả:** Danh mục sản phẩm.

**Mã nguồn Shop:** `artifacts/api-server/src/routes/product-categories.ts`

Danh mục sản phẩm.

**Số endpoint:** 3

**Contract API:** Mỗi endpoint có mục **URL**, body/query (từ code + schema Zod orval khi có), bảng lỗi `error`, và response (Zod hoặc trường `res.json`).

## Bảng endpoint (tóm tắt)

| Method | Path | Mô tả ngắn |
|--------|------|------------|
| GET | `/product-categories` | Đường dẫn đầy đủ `/api/product-categories` |
| POST | `/product-categories` | Đường dẫn đầy đủ `/api/product-categories`… |
| PATCH | `/product-categories/:id` | Đường dẫn đầy đủ `/api/product-categories/:id`… |

## Chi tiết từng endpoint

### `GET /product-categories` {#get-product-categories}

Đường dẫn đầy đủ `/api/product-categories`. Lớp kiểm tra: `requireAuth`.

**URL:** `GET /api/product-categories`

**Lớp route:** `requireAuth`
- **Thêm trong handler:** role **`super_admin`** (403 nếu không đủ).

**Query:** `limit`, `page`

**Response 200** — trường top-level (trích `res.json`):

`activeCount`, `inactiveCount`, `items`, `total`

### `POST /product-categories` {#post-product-categories}

Đường dẫn đầy đủ `/api/product-categories`. Lớp kiểm tra: `requireAuth, requireManagerOrAdmin, requireOperationalContext`.

**URL:** `POST /api/product-categories`

**Lớp route:** `requireAuth`, `requireManagerOrAdmin`, `requireOperationalContext`

**Lỗi JSON** (`error` string):

| HTTP | Message |
|------|---------|
| **400** | `Đã có loại sản phẩm cùng tên` |

### `PATCH /product-categories/:id` {#patch-product-categories--id}

Đường dẫn đầy đủ `/api/product-categories/:id`. Lớp kiểm tra: `requireAuth, requireManagerOrAdmin, requireOperationalContext`.

**URL:** `PATCH /api/product-categories/:id`

**Lớp route:** `requireAuth`, `requireManagerOrAdmin`, `requireOperationalContext`

**Lỗi JSON** (`error` string):

| HTTP | Message |
|------|---------|
| **400** | `Invalid ID` |
| **404** | `Không tìm thấy loại sản phẩm` |
| **400** | `Đã có loại sản phẩm cùng tên` |

## Ghi chú đọc mã

- Gắn prefix `/api` trong `app.ts`; file route: `routes/index.ts` → `./product-categories.ts`.
- Handler đầy đủ: mở file TypeScript tại Shop (tìm theo chuỗi path).
- Quyền role: `tham-chieu/phan-quyen-rbac/README.md` (tiếng Anh gốc) + các `require*` trong từng endpoint.

**Đọc tiếp:** [Hướng dẫn Map](../../huong-dan-doc/) · [Mục lục](../../README.md)
