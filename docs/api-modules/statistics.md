# API module: `statistics`

**Mô tả:** File routes statistics.ts — 6 endpoint HTTP cho /api/.... REST handlers cho domain statistics.

**Source Shop:** `artifacts/api-server/src/routes/statistics.ts`

REST handlers cho domain **statistics**.

**Số endpoint trong file:** 6

## Danh sách endpoint (tóm tắt)

| Method | Path | Mô tả ngắn |
|--------|------|------------|
| GET | `/statistics/products` | `/api/statistics/products` |
| GET | `/statistics/overview` | `/api/statistics/overview` |
| GET | `/statistics/trend` | `/api/statistics/trend` |
| GET | `/statistics/product-sales` | `/api/statistics/product-sales` |
| GET | `/statistics/top-products` | `/api/statistics/top-products` |
| GET | `/statistics/catalog` | `/api/statistics/catalog` |

## Chi tiết từng endpoint

### `GET /statistics/products` {#get-statistics-products}

`/api/statistics/products`. Middleware: `requireAuth`.

- **Middleware:** `requireAuth`

### `GET /statistics/overview` {#get-statistics-overview}

`/api/statistics/overview`. Middleware: `requireAuth`.

- **Middleware:** `requireAuth`

### `GET /statistics/trend` {#get-statistics-trend}

`/api/statistics/trend`. Middleware: `requireAuth`.

- **Middleware:** `requireAuth`

### `GET /statistics/product-sales` {#get-statistics-product-sales}

`/api/statistics/product-sales`. Middleware: `requireAuth`.

- **Middleware:** `requireAuth`

### `GET /statistics/top-products` {#get-statistics-top-products}

`/api/statistics/top-products`. Middleware: `requireAuth`.

- **Middleware:** `requireAuth`

### `GET /statistics/catalog` {#get-statistics-catalog}

`/api/statistics/catalog`. Middleware: `requireAuth`.

- **Middleware:** `requireAuth`

## Ghi chú đọc code

- Mount prefix `/api` qua `app.ts`; file này: `routes/index.ts` → `./statistics.ts`.
- Handler đầy đủ: mở file TypeScript tại Shop (search theo path string).
- Quyền role: xem `reference/rbac.md` và middleware trong từng block.
