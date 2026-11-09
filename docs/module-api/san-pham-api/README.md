# Module API: `products`

**Mô tả:** Module API products.ts — 11 endpoint. Quản lý sản phẩm (thêm/sửa/xóa), import Excel, biến thể, ẩn/hiện SP…

**Mã nguồn Shop:** `artifacts/api-server/src/routes/products.ts`

Quản lý sản phẩm (thêm/sửa/xóa), import Excel, biến thể, ẩn/hiện SP, giá/giá vốn theo role.

**Giao diện:** `pages/products.tsx`.

**Số endpoint:** 11

**Contract API:** Mỗi endpoint có mục **URL**, body/query (từ code + schema Zod orval khi có), bảng lỗi `error`, và response (Zod hoặc trường `res.json`).

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

**URL:** `GET /api/products`

**Lớp route:** `requireAuth`

*Handler không trích được contract tự động — mở file route TypeScript.*

### `POST /products` {#post-products}

Đường dẫn đầy đủ `/api/products`. Lớp kiểm tra: `requireAuth, requireCatalogShop, requireOperationalContext`.

**URL:** `POST /api/products`

**Lớp route:** `requireAuth`, `requireCatalogShop`, `requireOperationalContext`

**Request body** — schema `CreateProductBody` (`@workspace/api-zod`):

| Trường | Kiểu (Zod) | Bắt buộc |
|--------|------------|----------|
| `internalCode` | `string()` | không |
| `internalName` | `string()` | không |
| `englishName` | `string()` | không |
| `vatName` | `string()` | không |
| `unit` | `string()` | không |
| `vatRate` | `number()` | không |
| `tncnRate` | `number()` | không |
| `material` | `string()` | không |
| `dimensions` | `string()` | không |
| `weight` | `string()` | không |
| `manufacturer` | `string()` | không |
| `supplierId` | `number()` | **có** |
| `category` | `string()` | **có** |
| `categoryId` | `number()` | **có** |
| `name` | `string()` | **có** |
| `price` | `number()` | **có** |
| `costPrice` | `number()` | **có** |
| `initialQuantity` | `number()` | không |
| `thumbnailUrl` | `string()` | không |

**Response 201** — trường top-level (trích `res.json`):

`message`

### `POST /products/import` {#post-products-import}

Đường dẫn đầy đủ `/api/products/import`. Lớp kiểm tra: `requireAuth, requireCatalogShop, requireOperationalContext`.

**URL:** `POST /api/products/import`

**Lớp route:** `requireAuth`, `requireCatalogShop`, `requireOperationalContext`

**Lỗi JSON** (`error` string):

| HTTP | Message |
|------|---------|
| **400** | `Body phải có 'rows' hoặc 'variantRows' không rỗng` |

**Response 200** — trường top-level (trích `res.json`):

`productErrors`, `total`, `variantErrors`, `variantsTotal`

### `GET /products/product-sales` {#get-products-product-sales}

Đường dẫn đầy đủ `/api/products/product-sales`. Lớp kiểm tra: `requireAuth`.

**URL:** `GET /api/products/product-sales`

**Lớp route:** `requireAuth`

*Handler không trích được contract tự động — mở file route TypeScript.*

### `GET /products/variant-sales` {#get-products-variant-sales}

Đường dẫn đầy đủ `/api/products/variant-sales`. Lớp kiểm tra: `requireAuth`.

**URL:** `GET /api/products/variant-sales`

**Lớp route:** `requireAuth`

*Handler không trích được contract tự động — mở file route TypeScript.*

### `GET /products/:id` {#get-products--id}

Đường dẫn đầy đủ `/api/products/:id`. Lớp kiểm tra: `requireAuth`.

**URL:** `GET /api/products/:id`

**Lớp route:** `requireAuth`

**Lỗi JSON** (`error` string):

| HTTP | Message |
|------|---------|
| **400** | `Invalid product ID` |
| **404** | `Product not found` |

**Response 200** — trường top-level (trích `res.json`):

`costPrice`, `variants`

### `PATCH /products/:id` {#patch-products--id}

Đường dẫn đầy đủ `/api/products/:id`. Lớp kiểm tra: `requireAuth, requireCatalogShop, requireOperationalContext`.

**URL:** `PATCH /api/products/:id`

**Lớp route:** `requireAuth`, `requireCatalogShop`, `requireOperationalContext`

**Request body** — schema `UpdateProductBody` (`@workspace/api-zod`):

| Trường | Kiểu (Zod) | Bắt buộc |
|--------|------------|----------|
| `internalCode` | `string()` | không |
| `internalName` | `string()` | không |
| `englishName` | `string()` | không |
| `vatName` | `string()` | không |
| `unit` | `string()` | không |
| `vatRate` | `number()` | không |
| `tncnRate` | `number()` | không |
| `material` | `string()` | không |
| `dimensions` | `string()` | không |
| `weight` | `string()` | không |
| `manufacturer` | `string()` | không |
| `supplierId` | `number()` | **có** |
| `category` | `string()` | **có** |
| `categoryId` | `number()` | **có** |
| `name` | `string()` | không |
| `price` | `number()` | không |
| `costPrice` | `number()` | không |
| `quantity` | `number()` | không |
| `thumbnailUrl` | `string()` | không |

**Lỗi JSON** (`error` string):

| HTTP | Message |
|------|---------|
| **400** | `Invalid product ID` |
| **404** | `Product not found` |

**Response 200** — trường top-level (trích `res.json`):

`message`

### `DELETE /products/:id` {#delete-products--id}

Đường dẫn đầy đủ `/api/products/:id`. Lớp kiểm tra: `requireAuth, requireCatalogShop, requireOperationalContext`.

**URL:** `DELETE /api/products/:id`

**Lớp route:** `requireAuth`, `requireCatalogShop`, `requireOperationalContext`

**Lỗi JSON** (`error` string):

| HTTP | Message |
|------|---------|
| **400** | `Invalid product ID` |
| **404** | `Product not found` |

### `POST /products/:id/variants` {#post-products--id-variants}

Đường dẫn đầy đủ `/api/products/:id/variants`. Lớp kiểm tra: `requireAuth, requireCatalogShop, requireOperationalContext`.

**URL:** `POST /api/products/:id/variants`

**Lớp route:** `requireAuth`, `requireCatalogShop`, `requireOperationalContext`

**Path params:** `id`

**Lỗi JSON** (`error` string):

| HTTP | Message |
|------|---------|
| **400** | `Invalid product ID` |
| **404** | `Product not found` |

**Response 201** — trường top-level (trích `res.json`):

`message`

### `PATCH /products/:id/variants/:variantId` {#patch-products--id-variants--variantId}

Đường dẫn đầy đủ `/api/products/:id/variants/:variantId`. Lớp kiểm tra: `requireAuth, requireOperationalContext`.

**URL:** `PATCH /api/products/:id/variants/:variantId`

**Lớp route:** `requireAuth`, `requireOperationalContext`
- **Thêm trong handler:** role **`super_admin`** (403 nếu không đủ).

**Path params:** `id`, `variantId`

**Lỗi JSON** (`error` string):

| HTTP | Message |
|------|---------|
| **400** | `Invalid id` |
| **403** | `Chỉ chi nhánh chính được quản lý sản phẩm` |
| **403** | `Không có quyền chia tồn biến thể` |
| **404** | `Variant not found` |

### `DELETE /products/:id/variants/:variantId` {#delete-products--id-variants--variantId}

Đường dẫn đầy đủ `/api/products/:id/variants/:variantId`. Lớp kiểm tra: `requireAuth, requireCatalogShop, requireOperationalContext`.

**URL:** `DELETE /api/products/:id/variants/:variantId`

**Lớp route:** `requireAuth`, `requireCatalogShop`, `requireOperationalContext`

**Path params:** `id`, `variantId`

**Lỗi JSON** (`error` string):

| HTTP | Message |
|------|---------|
| **400** | `Invalid id` |
| **404** | `Variant not found` |

**Response 200** — trường top-level (trích `res.json`):

`message`

## Ghi chú đọc mã

- Gắn prefix `/api` trong `app.ts`; file route: `routes/index.ts` → `./products.ts`.
- Handler đầy đủ: mở file TypeScript tại Shop (tìm theo chuỗi path).
- Quyền role: `tham-chieu/phan-quyen-rbac/README.md` (tiếng Anh gốc) + các `require*` trong từng endpoint.

**Đọc tiếp:** [Hướng dẫn Map](../../huong-dan-doc/) · [Mục lục](../../README.md)
