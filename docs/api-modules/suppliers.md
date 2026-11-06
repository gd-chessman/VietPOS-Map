# API module: `suppliers`

**Mô tả:** File routes suppliers.ts — 4 endpoint HTTP cho /api/.... REST handlers cho domain suppliers.

**Source Shop:** `artifacts/api-server/src/routes/suppliers.ts`

REST handlers cho domain **suppliers**.

**Số endpoint trong file:** 4

## Danh sách endpoint (tóm tắt)

| Method | Path | Mô tả ngắn |
|--------|------|------------|
| GET | `/suppliers` | `/api/suppliers` |
| GET | `/suppliers/:id` | `/api/suppliers/:id` |
| POST | `/suppliers` | `/api/suppliers` |
| PATCH | `/suppliers/:id` | `/api/suppliers/:id` |

## Chi tiết từng endpoint

### `GET /suppliers` {#get-suppliers}

`/api/suppliers`. Middleware: `requireAuth`.

- **Middleware:** `requireAuth`

### `GET /suppliers/:id` {#get-suppliers--id}

`/api/suppliers/:id`. Middleware: `requireAuth, requireHubShop, requireManagerOrAdmin`.

- **Middleware:** `requireAuth`, `requireHubShop`, `requireManagerOrAdmin`

### `POST /suppliers` {#post-suppliers}

`/api/suppliers`. Middleware: `requireAuth, requireHubShop, requireManagerOrAdmin, requireOperationalContext`.

- **Middleware:** `requireAuth`, `requireHubShop`, `requireManagerOrAdmin`, `requireOperationalContext`

### `PATCH /suppliers/:id` {#patch-suppliers--id}

`/api/suppliers/:id`. Middleware: `requireAuth, requireHubShop, requireManagerOrAdmin, requireOperationalContext`.

- **Middleware:** `requireAuth`, `requireHubShop`, `requireManagerOrAdmin`, `requireOperationalContext`

## Ghi chú đọc code

- Mount prefix `/api` qua `app.ts`; file này: `routes/index.ts` → `./suppliers.ts`.
- Handler đầy đủ: mở file TypeScript tại Shop (search theo path string).
- Quyền role: xem `reference/rbac.md` và middleware trong từng block.
