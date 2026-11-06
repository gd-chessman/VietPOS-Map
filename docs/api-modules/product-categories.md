# API module: `product-categories`

**Mô tả:** File routes product-categories.ts — 3 endpoint HTTP cho /api/.... REST handlers cho domain product-categories.

**Source Shop:** `artifacts/api-server/src/routes/product-categories.ts`

REST handlers cho domain **product-categories**.

**Số endpoint trong file:** 3

## Danh sách endpoint (tóm tắt)

| Method | Path | Mô tả ngắn |
|--------|------|------------|
| GET | `/product-categories` | `/api/product-categories` |
| POST | `/product-categories` | `/api/product-categories` |
| PATCH | `/product-categories/:id` | `/api/product-categories/:id` |

## Chi tiết từng endpoint

### `GET /product-categories` {#get-product-categories}

`/api/product-categories`. Middleware: `requireAuth`.

- **Middleware:** `requireAuth`

### `POST /product-categories` {#post-product-categories}

`/api/product-categories`. Middleware: `requireAuth, requireManagerOrAdmin, requireOperationalContext`.

- **Middleware:** `requireAuth`, `requireManagerOrAdmin`, `requireOperationalContext`

### `PATCH /product-categories/:id` {#patch-product-categories--id}

`/api/product-categories/:id`. Middleware: `requireAuth, requireManagerOrAdmin, requireOperationalContext`.

- **Middleware:** `requireAuth`, `requireManagerOrAdmin`, `requireOperationalContext`

## Ghi chú đọc code

- Mount prefix `/api` qua `app.ts`; file này: `routes/index.ts` → `./product-categories.ts`.
- Handler đầy đủ: mở file TypeScript tại Shop (search theo path string).
- Quyền role: xem `reference/rbac.md` và middleware trong từng block.
