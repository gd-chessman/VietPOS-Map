# API module: `products`

**Mô tả:** File routes products.ts — 11 endpoint HTTP cho /api/.... CRUD sản phẩm, import Excel, variant, ẩn/hiện SP, giá/giá vốn theo role. Frontend: pages/products.tsx.

**Source Shop:** `artifacts/api-server/src/routes/products.ts`

CRUD sản phẩm, import Excel, variant, ẩn/hiện SP, giá/giá vốn theo role.

**Frontend:** `pages/products.tsx`.

**Số endpoint trong file:** 11

## Danh sách endpoint (tóm tắt)

| Method | Path | Mô tả ngắn |
|--------|------|------------|
| GET | `/products` | `/api/products` |
| POST | `/products` | `/api/products` |
| POST | `/products/import` | `/api/products/import` |
| GET | `/products/product-sales` | `/api/products/product-sales` |
| GET | `/products/variant-sales` | `/api/products/variant-sales` |
| GET | `/products/:id` | `/api/products/:id` |
| PATCH | `/products/:id` | `/api/products/:id` |
| DELETE | `/products/:id` | `/api/products/:id` |
| POST | `/products/:id/variants` | `/api/products/:id/variants` |
| PATCH | `/products/:id/variants/:variantId` | `/api/products/:id/variants/:variantId` |
| DELETE | `/products/:id/variants/:variantId` | `/api/products/:id/variants/:variantId` |

## Chi tiết từng endpoint

### `GET /products` {#get-products}

`/api/products`. Middleware: `requireAuth`.

- **Middleware:** `requireAuth`

### `POST /products` {#post-products}

`/api/products`. Middleware: `requireAuth, requireCatalogShop, requireOperationalContext`.

- **Middleware:** `requireAuth`, `requireCatalogShop`, `requireOperationalContext`

### `POST /products/import` {#post-products-import}

`/api/products/import`. Middleware: `requireAuth, requireCatalogShop, requireOperationalContext`.

- **Middleware:** `requireAuth`, `requireCatalogShop`, `requireOperationalContext`

### `GET /products/product-sales` {#get-products-product-sales}

`/api/products/product-sales`. Middleware: `requireAuth`.

- **Middleware:** `requireAuth`

### `GET /products/variant-sales` {#get-products-variant-sales}

`/api/products/variant-sales`. Middleware: `requireAuth`.

- **Middleware:** `requireAuth`

### `GET /products/:id` {#get-products--id}

`/api/products/:id`. Middleware: `requireAuth`.

- **Middleware:** `requireAuth`

### `PATCH /products/:id` {#patch-products--id}

`/api/products/:id`. Middleware: `requireAuth, requireCatalogShop, requireOperationalContext`.

- **Middleware:** `requireAuth`, `requireCatalogShop`, `requireOperationalContext`

### `DELETE /products/:id` {#delete-products--id}

`/api/products/:id`. Middleware: `requireAuth, requireCatalogShop, requireOperationalContext`.

- **Middleware:** `requireAuth`, `requireCatalogShop`, `requireOperationalContext`

### `POST /products/:id/variants` {#post-products--id-variants}

`/api/products/:id/variants`. Middleware: `requireAuth, requireCatalogShop, requireOperationalContext`.

- **Middleware:** `requireAuth`, `requireCatalogShop`, `requireOperationalContext`

### `PATCH /products/:id/variants/:variantId` {#patch-products--id-variants--variantId}

`/api/products/:id/variants/:variantId`. Middleware: `requireAuth, requireOperationalContext`.

- **Middleware:** `requireAuth`, `requireOperationalContext`

### `DELETE /products/:id/variants/:variantId` {#delete-products--id-variants--variantId}

`/api/products/:id/variants/:variantId`. Middleware: `requireAuth, requireCatalogShop, requireOperationalContext`.

- **Middleware:** `requireAuth`, `requireCatalogShop`, `requireOperationalContext`

## Ghi chú đọc code

- Mount prefix `/api` qua `app.ts`; file này: `routes/index.ts` → `./products.ts`.
- Handler đầy đủ: mở file TypeScript tại Shop (search theo path string).
- Quyền role: xem `reference/rbac.md` và middleware trong từng block.
