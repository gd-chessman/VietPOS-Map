# API module: `purchase-orders`

**Mô tả:** File routes purchase-orders.ts — 9 endpoint HTTP cho /api/.... REST handlers cho domain purchase-orders.

**Source Shop:** `artifacts/api-server/src/routes/purchase-orders.ts`

REST handlers cho domain **purchase-orders**.

**Số endpoint trong file:** 9

## Danh sách endpoint (tóm tắt)

| Method | Path | Mô tả ngắn |
|--------|------|------------|
| GET | `/purchase-orders/sales-hints` | `/api/purchase-orders/sales-hints` |
| GET | `/purchase-orders` | `/api/purchase-orders` |
| GET | `/purchase-orders/:id` | `/api/purchase-orders/:id` |
| POST | `/purchase-orders` | `/api/purchase-orders` |
| PATCH | `/purchase-orders/:id` | `/api/purchase-orders/:id` |
| PATCH | `/purchase-orders/:id/send` | `/api/purchase-orders/:id/send` |
| PATCH | `/purchase-orders/:id/receive` | `/api/purchase-orders/:id/receive` |
| PATCH | `/purchase-orders/:id/close-short` | `/api/purchase-orders/:id/close-short` |
| PATCH | `/purchase-orders/:id/cancel` | `/api/purchase-orders/:id/cancel` |

## Chi tiết từng endpoint

### `GET /purchase-orders/sales-hints` {#get-purchase-orders-sales-hints}

`/api/purchase-orders/sales-hints`. Middleware: `requireAuth, requireHubShop, requireOperationalContext`.

- **Middleware:** `requireAuth`, `requireHubShop`, `requireOperationalContext`

### `GET /purchase-orders` {#get-purchase-orders}

`/api/purchase-orders`. Middleware: `requireAuth, requireHubShop, requireOperationalContext`.

- **Middleware:** `requireAuth`, `requireHubShop`, `requireOperationalContext`

### `GET /purchase-orders/:id` {#get-purchase-orders--id}

`/api/purchase-orders/:id`. Middleware: `requireAuth, requireHubShop, requireOperationalContext`.

- **Middleware:** `requireAuth`, `requireHubShop`, `requireOperationalContext`

### `POST /purchase-orders` {#post-purchase-orders}

`/api/purchase-orders`. Middleware: `requireAuth, requireHubShop, requireOperationalContext`.

- **Middleware:** `requireAuth`, `requireHubShop`, `requireOperationalContext`

### `PATCH /purchase-orders/:id` {#patch-purchase-orders--id}

`/api/purchase-orders/:id`. Middleware: `requireAuth, requireHubShop, requireOperationalContext`.

- **Middleware:** `requireAuth`, `requireHubShop`, `requireOperationalContext`

### `PATCH /purchase-orders/:id/send` {#patch-purchase-orders--id-send}

`/api/purchase-orders/:id/send`. Middleware: `requireAuth, requireHubShop, requireOperationalContext`.

- **Middleware:** `requireAuth`, `requireHubShop`, `requireOperationalContext`

### `PATCH /purchase-orders/:id/receive` {#patch-purchase-orders--id-receive}

`/api/purchase-orders/:id/receive`. Middleware: `requireAuth, requireHubShop, requireOperationalContext`.

- **Middleware:** `requireAuth`, `requireHubShop`, `requireOperationalContext`

### `PATCH /purchase-orders/:id/close-short` {#patch-purchase-orders--id-close-short}

`/api/purchase-orders/:id/close-short`. Middleware: `requireAuth, requireHubShop, requireOperationalContext`.

- **Middleware:** `requireAuth`, `requireHubShop`, `requireOperationalContext`

### `PATCH /purchase-orders/:id/cancel` {#patch-purchase-orders--id-cancel}

`/api/purchase-orders/:id/cancel`. Middleware: `requireAuth, requireHubShop, requireOperationalContext`.

- **Middleware:** `requireAuth`, `requireHubShop`, `requireOperationalContext`

## Ghi chú đọc code

- Mount prefix `/api` qua `app.ts`; file này: `routes/index.ts` → `./purchase-orders.ts`.
- Handler đầy đủ: mở file TypeScript tại Shop (search theo path string).
- Quyền role: xem `reference/rbac.md` và middleware trong từng block.
