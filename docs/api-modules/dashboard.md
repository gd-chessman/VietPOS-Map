# API module: `dashboard`

**Mô tả:** File routes dashboard.ts — 17 endpoint HTTP cho /api/.... REST handlers cho domain dashboard.

**Source Shop:** `artifacts/api-server/src/routes/dashboard.ts`

REST handlers cho domain **dashboard**.

**Số endpoint trong file:** 17

## Danh sách endpoint (tóm tắt)

| Method | Path | Mô tả ngắn |
|--------|------|------------|
| GET | `/dashboard` | `/api/dashboard` |
| GET | `/chain-dashboard` | `/api/chain-dashboard` |
| GET | `/dashboard/revenue-chart` | `/api/dashboard/revenue-chart` |
| GET | `/dashboard/period-visitor-stats` | `/api/dashboard/period-visitor-stats` |
| GET | `/dashboard/period-sold-stats` | `/api/dashboard/period-sold-stats` |
| GET | `/dashboard/period-cancel-stats` | `/api/dashboard/period-cancel-stats` |
| GET | `/chain-dashboard/revenue-chart` | `/api/chain-dashboard/revenue-chart` |
| GET | `/chain-dashboard/period-visitor-stats` | `/api/chain-dashboard/period-visitor-stats` |
| GET | `/chain-dashboard/period-sold-stats` | `/api/chain-dashboard/period-sold-stats` |
| GET | `/chain-dashboard/period-cancel-stats` | `/api/chain-dashboard/period-cancel-stats` |
| GET | `/dashboard/top-products` | `/api/dashboard/top-products` |
| GET | `/chain-dashboard/top-products` | `/api/chain-dashboard/top-products` |
| GET | `/dashboard/orders-today` | `/api/dashboard/orders-today` |
| GET | `/chain-dashboard/orders-today` | `/api/chain-dashboard/orders-today` |
| GET | `/chain-dashboard/orders-yesterday` | `/api/chain-dashboard/orders-yesterday` |
| GET | `/dashboard/low-stock` | `/api/dashboard/low-stock` |
| GET | `/chain-dashboard/low-stock` | `/api/chain-dashboard/low-stock` |

## Chi tiết từng endpoint

### `GET /dashboard` {#get-dashboard}

`/api/dashboard`. Middleware: `requireAuth`.

- **Middleware:** `requireAuth`

### `GET /chain-dashboard` {#get-chain-dashboard}

`/api/chain-dashboard`. Middleware: `requireAuth`.

- **Middleware:** `requireAuth`

### `GET /dashboard/revenue-chart` {#get-dashboard-revenue-chart}

`/api/dashboard/revenue-chart`. Middleware: `requireAuth`.

- **Middleware:** `requireAuth`

### `GET /dashboard/period-visitor-stats` {#get-dashboard-period-visitor-stats}

`/api/dashboard/period-visitor-stats`. Middleware: `requireAuth`.

- **Middleware:** `requireAuth`

### `GET /dashboard/period-sold-stats` {#get-dashboard-period-sold-stats}

`/api/dashboard/period-sold-stats`. Middleware: `requireAuth`.

- **Middleware:** `requireAuth`

### `GET /dashboard/period-cancel-stats` {#get-dashboard-period-cancel-stats}

`/api/dashboard/period-cancel-stats`. Middleware: `requireAuth`.

- **Middleware:** `requireAuth`

### `GET /chain-dashboard/revenue-chart` {#get-chain-dashboard-revenue-chart}

`/api/chain-dashboard/revenue-chart`. Middleware: `requireAuth`.

- **Middleware:** `requireAuth`

### `GET /chain-dashboard/period-visitor-stats` {#get-chain-dashboard-period-visitor-stats}

`/api/chain-dashboard/period-visitor-stats`. Middleware: `requireAuth`.

- **Middleware:** `requireAuth`

### `GET /chain-dashboard/period-sold-stats` {#get-chain-dashboard-period-sold-stats}

`/api/chain-dashboard/period-sold-stats`. Middleware: `requireAuth`.

- **Middleware:** `requireAuth`

### `GET /chain-dashboard/period-cancel-stats` {#get-chain-dashboard-period-cancel-stats}

`/api/chain-dashboard/period-cancel-stats`. Middleware: `requireAuth`.

- **Middleware:** `requireAuth`

### `GET /dashboard/top-products` {#get-dashboard-top-products}

`/api/dashboard/top-products`. Middleware: `requireAuth`.

- **Middleware:** `requireAuth`

### `GET /chain-dashboard/top-products` {#get-chain-dashboard-top-products}

`/api/chain-dashboard/top-products`. Middleware: `requireAuth`.

- **Middleware:** `requireAuth`

### `GET /dashboard/orders-today` {#get-dashboard-orders-today}

`/api/dashboard/orders-today`. Middleware: `requireAuth`.

- **Middleware:** `requireAuth`

### `GET /chain-dashboard/orders-today` {#get-chain-dashboard-orders-today}

`/api/chain-dashboard/orders-today`. Middleware: `requireAuth`.

- **Middleware:** `requireAuth`

### `GET /chain-dashboard/orders-yesterday` {#get-chain-dashboard-orders-yesterday}

`/api/chain-dashboard/orders-yesterday`. Middleware: `requireAuth`.

- **Middleware:** `requireAuth`

### `GET /dashboard/low-stock` {#get-dashboard-low-stock}

`/api/dashboard/low-stock`. Middleware: `requireAuth`.

- **Middleware:** `requireAuth`

### `GET /chain-dashboard/low-stock` {#get-chain-dashboard-low-stock}

`/api/chain-dashboard/low-stock`. Middleware: `requireAuth`.

- **Middleware:** `requireAuth`

## Ghi chú đọc code

- Mount prefix `/api` qua `app.ts`; file này: `routes/index.ts` → `./dashboard.ts`.
- Handler đầy đủ: mở file TypeScript tại Shop (search theo path string).
- Quyền role: xem `reference/rbac.md` và middleware trong từng block.
