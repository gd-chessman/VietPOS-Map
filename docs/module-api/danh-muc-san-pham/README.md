# Module API: `product-categories`

**Mô tả:** Module API product-categories.ts — 3 endpoint. Danh mục sản phẩm.

**Mã nguồn Shop:** `artifacts/api-server/src/routes/product-categories.ts`

Danh mục sản phẩm.

**Số endpoint:** 3

## Bảng endpoint (tóm tắt)

| Method | Path | Mô tả ngắn |
|--------|------|------------|
| GET | `/product-categories` | Đường dẫn đầy đủ `/api/product-categories` |
| POST | `/product-categories` | Đường dẫn đầy đủ `/api/product-categories`… |
| PATCH | `/product-categories/:id` | Đường dẫn đầy đủ `/api/product-categories/:id`… |

## Chi tiết từng endpoint

### `GET /product-categories` {#get-product-categories}

Đường dẫn đầy đủ `/api/product-categories`. Lớp kiểm tra: `requireAuth`.

- **Lớp kiểm tra (middleware):** `requireAuth`

### `POST /product-categories` {#post-product-categories}

Đường dẫn đầy đủ `/api/product-categories`. Lớp kiểm tra: `requireAuth, requireManagerOrAdmin, requireOperationalContext`.

- **Lớp kiểm tra (middleware):** `requireAuth`, `requireManagerOrAdmin`, `requireOperationalContext`

### `PATCH /product-categories/:id` {#patch-product-categories--id}

Đường dẫn đầy đủ `/api/product-categories/:id`. Lớp kiểm tra: `requireAuth, requireManagerOrAdmin, requireOperationalContext`.

- **Lớp kiểm tra (middleware):** `requireAuth`, `requireManagerOrAdmin`, `requireOperationalContext`

## Ghi chú đọc mã

- Gắn prefix `/api` trong `app.ts`; file route: `routes/index.ts` → `./product-categories.ts`.
- Handler đầy đủ: mở file TypeScript tại Shop (tìm theo chuỗi path).
- Quyền role: `tham-chieu/phan-quyen-rbac/README.md` (tiếng Anh gốc) + các `require*` trong từng endpoint.

**Đọc tiếp:** [Hướng dẫn Map](../../huong-dan-doc/) · [Mục lục](../../README.md)
