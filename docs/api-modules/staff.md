# API module: `staff`

**Mô tả:** File routes staff.ts — 7 endpoint HTTP cho /api/.... REST handlers cho domain staff.

**Source Shop:** `artifacts/api-server/src/routes/staff.ts`

REST handlers cho domain **staff**.

**Số endpoint trong file:** 7

## Danh sách endpoint (tóm tắt)

| Method | Path | Mô tả ngắn |
|--------|------|------------|
| GET | `/staff` | `/api/staff` |
| POST | `/staff` | `/api/staff` |
| PATCH | `/staff/:id` | `/api/staff/:id` |
| DELETE | `/staff/:id` | `/api/staff/:id` |
| GET | `/staff/pin-reset-requests` | `/api/staff/pin-reset-requests` |
| POST | `/staff/pin-reset-requests/:id/resolve` | `/api/staff/pin-reset-requests/:id/resolve` |
| POST | `/staff/pin-reset-requests/:id/dismiss` | `/api/staff/pin-reset-requests/:id/dismiss` |

## Chi tiết từng endpoint

### `GET /staff` {#get-staff}

`/api/staff`. Middleware: `requireAuth`.

- **Middleware:** `requireAuth`

### `POST /staff` {#post-staff}

`/api/staff`. Middleware: `requireAuth, requireOperationalContext`.

- **Middleware:** `requireAuth`, `requireOperationalContext`

### `PATCH /staff/:id` {#patch-staff--id}

`/api/staff/:id`. Middleware: `requireAuth, requireOperationalContext`.

- **Middleware:** `requireAuth`, `requireOperationalContext`

### `DELETE /staff/:id` {#delete-staff--id}

`/api/staff/:id`. Middleware: `requireAuth, requireOperationalContext`.

- **Middleware:** `requireAuth`, `requireOperationalContext`

### `GET /staff/pin-reset-requests` {#get-staff-pin-reset-requests}

`/api/staff/pin-reset-requests`. Middleware: `requireAuth`.

- **Middleware:** `requireAuth`

### `POST /staff/pin-reset-requests/:id/resolve` {#post-staff-pin-reset-requests--id-resolve}

`/api/staff/pin-reset-requests/:id/resolve`. Middleware: `requireAuth, requireOperationalContext`.

- **Middleware:** `requireAuth`, `requireOperationalContext`

### `POST /staff/pin-reset-requests/:id/dismiss` {#post-staff-pin-reset-requests--id-dismiss}

`/api/staff/pin-reset-requests/:id/dismiss`. Middleware: `requireAuth, requireOperationalContext`.

- **Middleware:** `requireAuth`, `requireOperationalContext`

## Ghi chú đọc code

- Mount prefix `/api` qua `app.ts`; file này: `routes/index.ts` → `./staff.ts`.
- Handler đầy đủ: mở file TypeScript tại Shop (search theo path string).
- Quyền role: xem `reference/rbac.md` và middleware trong từng block.
