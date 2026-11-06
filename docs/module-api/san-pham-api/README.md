# Module API: `products`

**Mô tả:** Module API products.ts — 11 endpoint. Quản lý sản phẩm (thêm/sửa/xóa), import Excel, biến thể, ẩn/hiện SP, giá/giá vốn theo role. Giao diện: pages/products.t…

**Mã nguồn Shop:** `artifacts/api-server/src/routes/products.ts`

Quản lý sản phẩm (thêm/sửa/xóa), import Excel, biến thể, ẩn/hiện SP, giá/giá vốn theo role.

**Giao diện:** `pages/products.tsx`.

**Số endpoint:** 11

## Bảng endpoint (tóm tắt)

| Method | Path | Mô tả ngắn |
|--------|------|------------|
| GET | `/products` | Đường dẫn đầy đủ `/api/products` |
| POST | `/products` | Đường dẫn đầy đủ `/api/products` |
| POST | `/products/import` | Đường dẫn đầy đủ `/api/products/import` |
| GET | `/products/product-sales` | Đường dẫn đầy đủ `/api/products/product-sales` |
| GET | `/products/variant-sales` | Đường dẫn đầy đủ `/api/products/variant-sales` |
| GET | `/products/:id` | Đường dẫn đầy đủ `/api/products/:id` |
| PATCH | `/products/:id` | Đường dẫn đầy đủ `/api/products/:id` |
| DELETE | `/products/:id` | Đường dẫn đầy đủ `/api/products/:id` |
| POST | `/products/:id/variants` | Đường dẫn đầy đủ `/api/products/:id/variants`… |
| PATCH | `/products/:id/variants/:variantId` | Đường dẫn đầy đủ `/api/products/:id/variants/:variantId` |
| DELETE | `/products/:id/variants/:variantId` | Đường dẫn đầy đủ `/api/products/:id/variants/:variantId`… |

## Chi tiết từng endpoint

### `GET /products` {#get-products}

Đường dẫn đầy đủ `/api/products`. Lớp kiểm tra: `requireAuth`.

- **Lớp kiểm tra (middleware):** `requireAuth`

### `POST /products` {#post-products}

Đường dẫn đầy đủ `/api/products`. Lớp kiểm tra: `requireAuth, requireCatalogShop, requireOperationalContext`.

- **Lớp kiểm tra (middleware):** `requireAuth`, `requireCatalogShop`, `requireOperationalContext`

### `POST /products/import` {#post-products-import}

Đường dẫn đầy đủ `/api/products/import`. Lớp kiểm tra: `requireAuth, requireCatalogShop, requireOperationalContext`.

- **Lớp kiểm tra (middleware):** `requireAuth`, `requireCatalogShop`, `requireOperationalContext`

### `GET /products/product-sales` {#get-products-product-sales}

Đường dẫn đầy đủ `/api/products/product-sales`. Lớp kiểm tra: `requireAuth`.

- **Lớp kiểm tra (middleware):** `requireAuth`

### `GET /products/variant-sales` {#get-products-variant-sales}

Đường dẫn đầy đủ `/api/products/variant-sales`. Lớp kiểm tra: `requireAuth`.

- **Lớp kiểm tra (middleware):** `requireAuth`

### `GET /products/:id` {#get-products--id}

Đường dẫn đầy đủ `/api/products/:id`. Lớp kiểm tra: `requireAuth`.

- **Lớp kiểm tra (middleware):** `requireAuth`

### `PATCH /products/:id` {#patch-products--id}

Đường dẫn đầy đủ `/api/products/:id`. Lớp kiểm tra: `requireAuth, requireCatalogShop, requireOperationalContext`.

- **Lớp kiểm tra (middleware):** `requireAuth`, `requireCatalogShop`, `requireOperationalContext`

### `DELETE /products/:id` {#delete-products--id}

Đường dẫn đầy đủ `/api/products/:id`. Lớp kiểm tra: `requireAuth, requireCatalogShop, requireOperationalContext`.

- **Lớp kiểm tra (middleware):** `requireAuth`, `requireCatalogShop`, `requireOperationalContext`

### `POST /products/:id/variants` {#post-products--id-variants}

Đường dẫn đầy đủ `/api/products/:id/variants`. Lớp kiểm tra: `requireAuth, requireCatalogShop, requireOperationalContext`.

- **Lớp kiểm tra (middleware):** `requireAuth`, `requireCatalogShop`, `requireOperationalContext`

### `PATCH /products/:id/variants/:variantId` {#patch-products--id-variants--variantId}

Đường dẫn đầy đủ `/api/products/:id/variants/:variantId`. Lớp kiểm tra: `requireAuth, requireOperationalContext`.

- **Lớp kiểm tra (middleware):** `requireAuth`, `requireOperationalContext`

### `DELETE /products/:id/variants/:variantId` {#delete-products--id-variants--variantId}

Đường dẫn đầy đủ `/api/products/:id/variants/:variantId`. Lớp kiểm tra: `requireAuth, requireCatalogShop, requireOperationalContext`.

- **Lớp kiểm tra (middleware):** `requireAuth`, `requireCatalogShop`, `requireOperationalContext`

## Ghi chú đọc mã

- Gắn prefix `/api` trong `app.ts`; file route: `routes/index.ts` → `./products.ts`.
- Handler đầy đủ: mở file TypeScript tại Shop (tìm theo chuỗi path).
- Quyền role: `tham-chieu/phan-quyen-rbac/README.md` (tiếng Anh gốc) + các `require*` trong từng endpoint.

**Đọc tiếp:** [Hướng dẫn Map](../../huong-dan-doc/) · [Mục lục](../../README.md)
