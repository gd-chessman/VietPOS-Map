# API module: `shift-sessions`

**Mô tả:** File routes shift-sessions.ts — 3 endpoint HTTP cho /api/.... REST handlers cho domain shift-sessions.

**Source Shop:** `artifacts/api-server/src/routes/shift-sessions.ts`

REST handlers cho domain **shift-sessions**.

**Số endpoint trong file:** 3

## Danh sách endpoint (tóm tắt)

| Method | Path | Mô tả ngắn |
|--------|------|------------|
| GET | `/shift-sessions/current` | `/api/shift-sessions/current` |
| POST | `/shift-sessions` | `/api/shift-sessions` |
| PATCH | `/shift-sessions/:id/end` | `/api/shift-sessions/:id/end` |

## Chi tiết từng endpoint

### `GET /shift-sessions/current` {#get-shift-sessions-current}

`/api/shift-sessions/current`. Middleware: `requireAuth`.

- **Middleware:** `requireAuth`

### `POST /shift-sessions` {#post-shift-sessions}

`/api/shift-sessions`. Middleware: `requireAuth, requireDeviceApproval, requireOperationalContext`.

- **Middleware:** `requireAuth`, `requireDeviceApproval`, `requireOperationalContext`

### `PATCH /shift-sessions/:id/end` {#patch-shift-sessions--id-end}

`/api/shift-sessions/:id/end`. Middleware: `requireAuth`.

- **Middleware:** `requireAuth`

## Ghi chú đọc code

- Mount prefix `/api` qua `app.ts`; file này: `routes/index.ts` → `./shift-sessions.ts`.
- Handler đầy đủ: mở file TypeScript tại Shop (search theo path string).
- Quyền role: xem `reference/rbac.md` và middleware trong từng block.
