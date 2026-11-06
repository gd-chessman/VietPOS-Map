# API module: `chain`

**Mô tả:** File routes chain.ts — 29 endpoint HTTP cho /api/.... Tổ chức, shop, kho, điều chuyển (transfers). Cấu hình org (Viettel, CQT, feedback URL, agent LLM). Frontend: pages/chai…

**Source Shop:** `artifacts/api-server/src/routes/chain.ts`

Tổ chức, shop, kho, điều chuyển (`transfers`). Cấu hình org (Viettel, CQT, feedback URL, agent LLM).

**Frontend:** `pages/chain.tsx`, `chain-dashboard.tsx`.

**Số endpoint trong file:** 29

## Danh sách endpoint (tóm tắt)

| Method | Path | Mô tả ngắn |
|--------|------|------------|
| GET | `/organizations` | `/api/organizations` |
| GET | `/organizations/current` | `/api/organizations/current` |
| PUT | `/organizations/:orgId/shop-display-order` | `/api/organizations/:orgId/shop-display-order` |
| POST | `/organizations` | `/api/organizations` |
| PATCH | `/organizations/:id` | `/api/organizations/:id` |
| PATCH | `/shops/:id` | `/api/shops/:id` |
| POST | `/shops/:id/devices/register` | `/api/shops/:id/devices/register` |
| GET | `/shops/:id/devices` | `/api/shops/:id/devices` |
| PATCH | `/shops/:id/devices/:deviceRowId` | `/api/shops/:id/devices/:deviceRowId` |
| GET | `/shops/:id/devices/:deviceRowId/login-events` | `/api/shops/:id/devices/:deviceRowId/login-events` |
| POST | `/shops/:id/create-admin` | `/api/shops/:id/create-admin` |
| PATCH | `/shops/:id/admin-email` | `/api/shops/:id/admin-email` |
| PATCH | `/shops/:id/reset-password` | `/api/shops/:id/reset-password` |
| POST | `/shops` | `/api/shops` |
| GET | `/warehouses` | `/api/warehouses` |
| POST | `/warehouses` | `/api/warehouses` |
| PATCH | `/warehouses/:id` | `/api/warehouses/:id` |
| GET | `/warehouses/:id/products` | `/api/warehouses/:id/products` |
| GET | `/warehouses/:id/inventory` | `/api/warehouses/:id/inventory` |
| POST | `/warehouses/:id/adjust-stock` | `/api/warehouses/:id/adjust-stock` |
| GET | `/transfers` | `/api/transfers` |
| GET | `/transfers/:id/items` | `/api/transfers/:id/items` |
| POST | `/transfers` | `/api/transfers` |
| POST | `/transfers/:id/approve` | `/api/transfers/:id/approve` |
| POST | `/transfers/:id/ship` | `/api/transfers/:id/ship` |
| POST | `/transfers/:id/receive` | `/api/transfers/:id/receive` |
| DELETE | `/transfers/:id` | `/api/transfers/:id` |
| PATCH | `/transfers/:id` | `/api/transfers/:id` |
| GET | `/warehouses/:id/movements` | `/api/warehouses/:id/movements` |

## Chi tiết từng endpoint

### `GET /organizations` {#get-organizations}

`/api/organizations`. Middleware: `requireAuth, requireChainManagement`.

- **Middleware:** `requireAuth`, `requireChainManagement`

### `GET /organizations/current` {#get-organizations-current}

`/api/organizations/current`. Middleware: `requireAuth`.

- **Middleware:** `requireAuth`

### `PUT /organizations/:orgId/shop-display-order` {#put-organizations--orgId-shop-display-order}

`/api/organizations/:orgId/shop-display-order`. Middleware: `requireAuth, requireChainManagement`.

- **Middleware:** `requireAuth`, `requireChainManagement`

### `POST /organizations` {#post-organizations}

`/api/organizations`. Middleware: `requireAuth, requireChainManagement`.

- **Middleware:** `requireAuth`, `requireChainManagement`

### `PATCH /organizations/:id` {#patch-organizations--id}

`/api/organizations/:id`. Middleware: `requireAuth, requireChainManagement`.

- **Middleware:** `requireAuth`, `requireChainManagement`

### `PATCH /shops/:id` {#patch-shops--id}

`/api/shops/:id`. Middleware: `requireAuth`.

- **Middleware:** `requireAuth`

### `POST /shops/:id/devices/register` {#post-shops--id-devices-register}

`/api/shops/:id/devices/register`. Middleware: `requireAuth`.

- **Middleware:** `requireAuth`

### `GET /shops/:id/devices` {#get-shops--id-devices}

`/api/shops/:id/devices`. Middleware: `requireAuth`.

- **Middleware:** `requireAuth`

### `PATCH /shops/:id/devices/:deviceRowId` {#patch-shops--id-devices--deviceRowId}

`/api/shops/:id/devices/:deviceRowId`. Middleware: `requireAuth`.

- **Middleware:** `requireAuth`

### `GET /shops/:id/devices/:deviceRowId/login-events` {#get-shops--id-devices--deviceRowId-login-events}

`/api/shops/:id/devices/:deviceRowId/login-events`. Middleware: `requireAuth`.

- **Middleware:** `requireAuth`

### `POST /shops/:id/create-admin` {#post-shops--id-create-admin}

`/api/shops/:id/create-admin`. Middleware: `requireAuth`.

- **Middleware:** `requireAuth`

### `PATCH /shops/:id/admin-email` {#patch-shops--id-admin-email}

`/api/shops/:id/admin-email`. Middleware: `requireAuth`.

- **Middleware:** `requireAuth`

### `PATCH /shops/:id/reset-password` {#patch-shops--id-reset-password}

`/api/shops/:id/reset-password`. Middleware: `requireAuth`.

- **Middleware:** `requireAuth`

### `POST /shops` {#post-shops}

`/api/shops`. Middleware: `requireAuth`.

- **Middleware:** `requireAuth`

### `GET /warehouses` {#get-warehouses}

`/api/warehouses`. Middleware: `requireAuth`.

- **Middleware:** `requireAuth`

### `POST /warehouses` {#post-warehouses}

`/api/warehouses`. Middleware: `requireAuth`.

- **Middleware:** `requireAuth`

### `PATCH /warehouses/:id` {#patch-warehouses--id}

`/api/warehouses/:id`. Middleware: `requireAuth`.

- **Middleware:** `requireAuth`

### `GET /warehouses/:id/products` {#get-warehouses--id-products}

`/api/warehouses/:id/products`. Middleware: `requireAuth`.

- **Middleware:** `requireAuth`

### `GET /warehouses/:id/inventory` {#get-warehouses--id-inventory}

`/api/warehouses/:id/inventory`. Middleware: `requireAuth`.

- **Middleware:** `requireAuth`

### `POST /warehouses/:id/adjust-stock` {#post-warehouses--id-adjust-stock}

`/api/warehouses/:id/adjust-stock`. Middleware: `requireAuth`.

- **Middleware:** `requireAuth`

### `GET /transfers` {#get-transfers}

`/api/transfers`. Middleware: `requireAuth`.

- **Middleware:** `requireAuth`

### `GET /transfers/:id/items` {#get-transfers--id-items}

`/api/transfers/:id/items`. Middleware: `requireAuth`.

- **Middleware:** `requireAuth`

### `POST /transfers` {#post-transfers}

`/api/transfers`. Middleware: `requireAuth`.

- **Middleware:** `requireAuth`

### `POST /transfers/:id/approve` {#post-transfers--id-approve}

`/api/transfers/:id/approve`. Middleware: `requireAuth`.

- **Middleware:** `requireAuth`

### `POST /transfers/:id/ship` {#post-transfers--id-ship}

`/api/transfers/:id/ship`. Middleware: `requireAuth`.

- **Middleware:** `requireAuth`

### `POST /transfers/:id/receive` {#post-transfers--id-receive}

`/api/transfers/:id/receive`. Middleware: `requireAuth`.

- **Middleware:** `requireAuth`

### `DELETE /transfers/:id` {#delete-transfers--id}

`/api/transfers/:id`. Middleware: `requireAuth`.

- **Middleware:** `requireAuth`

### `PATCH /transfers/:id` {#patch-transfers--id}

`/api/transfers/:id`. Middleware: `requireAuth`.

- **Middleware:** `requireAuth`

### `GET /warehouses/:id/movements` {#get-warehouses--id-movements}

`/api/warehouses/:id/movements`. Middleware: `requireAuth`.

- **Middleware:** `requireAuth`

## Ghi chú đọc code

- Mount prefix `/api` qua `app.ts`; file này: `routes/index.ts` → `./chain.ts`.
- Handler đầy đủ: mở file TypeScript tại Shop (search theo path string).
- Quyền role: xem `reference/rbac.md` và middleware trong từng block.
