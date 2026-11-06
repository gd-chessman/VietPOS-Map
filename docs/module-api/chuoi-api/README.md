# Module API: `chain`

**Mô tả:** Module API chain.ts — 29 endpoint. Tổ chức, shop, kho, điều chuyển (transfers). Cấu hình org (Viettel, CQT, feedback URL, agent LLM). Giao diện: pages/cha…

**Mã nguồn Shop:** `artifacts/api-server/src/routes/chain.ts`

Tổ chức, shop, kho, điều chuyển (`transfers`). Cấu hình org (Viettel, CQT, feedback URL, agent LLM).

**Giao diện:** `pages/chain.tsx`, `chain-dashboard.tsx`.

**Số endpoint:** 29

## Bảng endpoint (tóm tắt)

| Method | Path | Mô tả ngắn |
|--------|------|------------|
| GET | `/organizations` | Đường dẫn đầy đủ `/api/organizations` |
| GET | `/organizations/current` | Đường dẫn đầy đủ `/api/organizations/current` |
| PUT | `/organizations/:orgId/shop-display-order` | Đường dẫn đầy đủ `/api/organizations/:orgId/shop-display-order` |
| POST | `/organizations` | Đường dẫn đầy đủ `/api/organizations` |
| PATCH | `/organizations/:id` | Đường dẫn đầy đủ `/api/organizations/:id` |
| PATCH | `/shops/:id` | Đường dẫn đầy đủ `/api/shops/:id` |
| POST | `/shops/:id/devices/register` | Đường dẫn đầy đủ `/api/shops/:id/devices/register` |
| GET | `/shops/:id/devices` | Đường dẫn đầy đủ `/api/shops/:id/devices` |
| PATCH | `/shops/:id/devices/:deviceRowId` | Đường dẫn đầy đủ `/api/shops/:id/devices/:deviceRowId` |
| GET | `/shops/:id/devices/:deviceRowId/login-events` | Đường dẫn đầy đủ `/api/shops/:id/devices/:deviceRowId/login-events` |
| POST | `/shops/:id/create-admin` | Đường dẫn đầy đủ `/api/shops/:id/create-admin` |
| PATCH | `/shops/:id/admin-email` | Đường dẫn đầy đủ `/api/shops/:id/admin-email` |
| PATCH | `/shops/:id/reset-password` | Đường dẫn đầy đủ `/api/shops/:id/reset-password` |
| POST | `/shops` | Đường dẫn đầy đủ `/api/shops` |
| GET | `/warehouses` | Đường dẫn đầy đủ `/api/warehouses` |
| POST | `/warehouses` | Đường dẫn đầy đủ `/api/warehouses` |
| PATCH | `/warehouses/:id` | Đường dẫn đầy đủ `/api/warehouses/:id` |
| GET | `/warehouses/:id/products` | Đường dẫn đầy đủ `/api/warehouses/:id/products` |
| GET | `/warehouses/:id/inventory` | Đường dẫn đầy đủ `/api/warehouses/:id/inventory` |
| POST | `/warehouses/:id/adjust-stock` | Đường dẫn đầy đủ `/api/warehouses/:id/adjust-stock` |
| GET | `/transfers` | Đường dẫn đầy đủ `/api/transfers` |
| GET | `/transfers/:id/items` | Đường dẫn đầy đủ `/api/transfers/:id/items` |
| POST | `/transfers` | Đường dẫn đầy đủ `/api/transfers` |
| POST | `/transfers/:id/approve` | Đường dẫn đầy đủ `/api/transfers/:id/approve` |
| POST | `/transfers/:id/ship` | Đường dẫn đầy đủ `/api/transfers/:id/ship` |
| POST | `/transfers/:id/receive` | Đường dẫn đầy đủ `/api/transfers/:id/receive` |
| DELETE | `/transfers/:id` | Đường dẫn đầy đủ `/api/transfers/:id` |
| PATCH | `/transfers/:id` | Đường dẫn đầy đủ `/api/transfers/:id` |
| GET | `/warehouses/:id/movements` | Đường dẫn đầy đủ `/api/warehouses/:id/movements` |

## Chi tiết từng endpoint

### `GET /organizations` {#get-organizations}

Đường dẫn đầy đủ `/api/organizations`. Lớp kiểm tra: `requireAuth, requireChainManagement`.

- **Lớp kiểm tra (middleware):** `requireAuth`, `requireChainManagement`

### `GET /organizations/current` {#get-organizations-current}

Đường dẫn đầy đủ `/api/organizations/current`. Lớp kiểm tra: `requireAuth`.

- **Lớp kiểm tra (middleware):** `requireAuth`

### `PUT /organizations/:orgId/shop-display-order` {#put-organizations--orgId-shop-display-order}

Đường dẫn đầy đủ `/api/organizations/:orgId/shop-display-order`. Lớp kiểm tra: `requireAuth, requireChainManagement`.

- **Lớp kiểm tra (middleware):** `requireAuth`, `requireChainManagement`

### `POST /organizations` {#post-organizations}

Đường dẫn đầy đủ `/api/organizations`. Lớp kiểm tra: `requireAuth, requireChainManagement`.

- **Lớp kiểm tra (middleware):** `requireAuth`, `requireChainManagement`

### `PATCH /organizations/:id` {#patch-organizations--id}

Đường dẫn đầy đủ `/api/organizations/:id`. Lớp kiểm tra: `requireAuth, requireChainManagement`.

- **Lớp kiểm tra (middleware):** `requireAuth`, `requireChainManagement`

### `PATCH /shops/:id` {#patch-shops--id}

Đường dẫn đầy đủ `/api/shops/:id`. Lớp kiểm tra: `requireAuth`.

- **Lớp kiểm tra (middleware):** `requireAuth`

### `POST /shops/:id/devices/register` {#post-shops--id-devices-register}

Đường dẫn đầy đủ `/api/shops/:id/devices/register`. Lớp kiểm tra: `requireAuth`.

- **Lớp kiểm tra (middleware):** `requireAuth`

### `GET /shops/:id/devices` {#get-shops--id-devices}

Đường dẫn đầy đủ `/api/shops/:id/devices`. Lớp kiểm tra: `requireAuth`.

- **Lớp kiểm tra (middleware):** `requireAuth`

### `PATCH /shops/:id/devices/:deviceRowId` {#patch-shops--id-devices--deviceRowId}

Đường dẫn đầy đủ `/api/shops/:id/devices/:deviceRowId`. Lớp kiểm tra: `requireAuth`.

- **Lớp kiểm tra (middleware):** `requireAuth`

### `GET /shops/:id/devices/:deviceRowId/login-events` {#get-shops--id-devices--deviceRowId-login-events}

Đường dẫn đầy đủ `/api/shops/:id/devices/:deviceRowId/login-events`. Lớp kiểm tra: `requireAuth`.

- **Lớp kiểm tra (middleware):** `requireAuth`

### `POST /shops/:id/create-admin` {#post-shops--id-create-admin}

Đường dẫn đầy đủ `/api/shops/:id/create-admin`. Lớp kiểm tra: `requireAuth`.

- **Lớp kiểm tra (middleware):** `requireAuth`

### `PATCH /shops/:id/admin-email` {#patch-shops--id-admin-email}

Đường dẫn đầy đủ `/api/shops/:id/admin-email`. Lớp kiểm tra: `requireAuth`.

- **Lớp kiểm tra (middleware):** `requireAuth`

### `PATCH /shops/:id/reset-password` {#patch-shops--id-reset-password}

Đường dẫn đầy đủ `/api/shops/:id/reset-password`. Lớp kiểm tra: `requireAuth`.

- **Lớp kiểm tra (middleware):** `requireAuth`

### `POST /shops` {#post-shops}

Đường dẫn đầy đủ `/api/shops`. Lớp kiểm tra: `requireAuth`.

- **Lớp kiểm tra (middleware):** `requireAuth`

### `GET /warehouses` {#get-warehouses}

Đường dẫn đầy đủ `/api/warehouses`. Lớp kiểm tra: `requireAuth`.

- **Lớp kiểm tra (middleware):** `requireAuth`

### `POST /warehouses` {#post-warehouses}

Đường dẫn đầy đủ `/api/warehouses`. Lớp kiểm tra: `requireAuth`.

- **Lớp kiểm tra (middleware):** `requireAuth`

### `PATCH /warehouses/:id` {#patch-warehouses--id}

Đường dẫn đầy đủ `/api/warehouses/:id`. Lớp kiểm tra: `requireAuth`.

- **Lớp kiểm tra (middleware):** `requireAuth`

### `GET /warehouses/:id/products` {#get-warehouses--id-products}

Đường dẫn đầy đủ `/api/warehouses/:id/products`. Lớp kiểm tra: `requireAuth`.

- **Lớp kiểm tra (middleware):** `requireAuth`

### `GET /warehouses/:id/inventory` {#get-warehouses--id-inventory}

Đường dẫn đầy đủ `/api/warehouses/:id/inventory`. Lớp kiểm tra: `requireAuth`.

- **Lớp kiểm tra (middleware):** `requireAuth`

### `POST /warehouses/:id/adjust-stock` {#post-warehouses--id-adjust-stock}

Đường dẫn đầy đủ `/api/warehouses/:id/adjust-stock`. Lớp kiểm tra: `requireAuth`.

- **Lớp kiểm tra (middleware):** `requireAuth`

### `GET /transfers` {#get-transfers}

Đường dẫn đầy đủ `/api/transfers`. Lớp kiểm tra: `requireAuth`.

- **Lớp kiểm tra (middleware):** `requireAuth`

### `GET /transfers/:id/items` {#get-transfers--id-items}

Đường dẫn đầy đủ `/api/transfers/:id/items`. Lớp kiểm tra: `requireAuth`.

- **Lớp kiểm tra (middleware):** `requireAuth`

### `POST /transfers` {#post-transfers}

Đường dẫn đầy đủ `/api/transfers`. Lớp kiểm tra: `requireAuth`.

- **Lớp kiểm tra (middleware):** `requireAuth`

### `POST /transfers/:id/approve` {#post-transfers--id-approve}

Đường dẫn đầy đủ `/api/transfers/:id/approve`. Lớp kiểm tra: `requireAuth`.

- **Lớp kiểm tra (middleware):** `requireAuth`

### `POST /transfers/:id/ship` {#post-transfers--id-ship}

Đường dẫn đầy đủ `/api/transfers/:id/ship`. Lớp kiểm tra: `requireAuth`.

- **Lớp kiểm tra (middleware):** `requireAuth`

### `POST /transfers/:id/receive` {#post-transfers--id-receive}

Đường dẫn đầy đủ `/api/transfers/:id/receive`. Lớp kiểm tra: `requireAuth`.

- **Lớp kiểm tra (middleware):** `requireAuth`

### `DELETE /transfers/:id` {#delete-transfers--id}

Đường dẫn đầy đủ `/api/transfers/:id`. Lớp kiểm tra: `requireAuth`.

- **Lớp kiểm tra (middleware):** `requireAuth`

### `PATCH /transfers/:id` {#patch-transfers--id}

Đường dẫn đầy đủ `/api/transfers/:id`. Lớp kiểm tra: `requireAuth`.

- **Lớp kiểm tra (middleware):** `requireAuth`

### `GET /warehouses/:id/movements` {#get-warehouses--id-movements}

Đường dẫn đầy đủ `/api/warehouses/:id/movements`. Lớp kiểm tra: `requireAuth`.

- **Lớp kiểm tra (middleware):** `requireAuth`

## Ghi chú đọc mã

- Gắn prefix `/api` trong `app.ts`; file route: `routes/index.ts` → `./chain.ts`.
- Handler đầy đủ: mở file TypeScript tại Shop (tìm theo chuỗi path).
- Quyền role: `tham-chieu/phan-quyen-rbac/README.md` (tiếng Anh gốc) + các `require*` trong từng endpoint.

**Đọc tiếp:** [Hướng dẫn Map](../../huong-dan-doc/) · [Mục lục](../../README.md)
