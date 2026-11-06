# API module: `sales-staff`

**Mô tả:** File routes sales-staff.ts — 4 endpoint HTTP cho /api/.... REST handlers cho domain sales-staff.

**Source Shop:** `artifacts/api-server/src/routes/sales-staff.ts`

REST handlers cho domain **sales-staff**.

**Số endpoint trong file:** 4

## Danh sách endpoint (tóm tắt)

| Method | Path | Mô tả ngắn |
|--------|------|------------|
| GET | `/sales-staff` | `/api/sales-staff` |
| GET | `/sales-staff/:id` | `/api/sales-staff/:id` |
| POST | `/sales-staff` | `/api/sales-staff` |
| PATCH | `/sales-staff/:id` | `/api/sales-staff/:id` |

## Chi tiết từng endpoint

### `GET /sales-staff` {#get-sales-staff}

`/api/sales-staff`. Middleware: `requireAuth`.

- **Middleware:** `requireAuth`

### `GET /sales-staff/:id` {#get-sales-staff--id}

`/api/sales-staff/:id`. Middleware: `requireAuth, requireManagerOrAdmin`.

- **Middleware:** `requireAuth`, `requireManagerOrAdmin`

### `POST /sales-staff` {#post-sales-staff}

`/api/sales-staff`. Middleware: `requireAuth, requireManagerOrAdmin, requireOperationalContext`.

- **Middleware:** `requireAuth`, `requireManagerOrAdmin`, `requireOperationalContext`

### `PATCH /sales-staff/:id` {#patch-sales-staff--id}

`/api/sales-staff/:id`. Middleware: `requireAuth, requireManagerOrAdmin, requireOperationalContext`.

- **Middleware:** `requireAuth`, `requireManagerOrAdmin`, `requireOperationalContext`

## Ghi chú đọc code

- Mount prefix `/api` qua `app.ts`; file này: `routes/index.ts` → `./sales-staff.ts`.
- Handler đầy đủ: mở file TypeScript tại Shop (search theo path string).
- Quyền role: xem `reference/rbac.md` và middleware trong từng block.
