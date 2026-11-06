# API module: `notification-settings`

**Mô tả:** File routes notification-settings.ts — 2 endpoint HTTP cho /api/.... REST handlers cho domain notification-settings.

**Source Shop:** `artifacts/api-server/src/routes/notification-settings.ts`

REST handlers cho domain **notification-settings**.

**Số endpoint trong file:** 2

## Danh sách endpoint (tóm tắt)

| Method | Path | Mô tả ngắn |
|--------|------|------------|
| GET | `/notification-settings` | `/api/notification-settings` |
| PATCH | `/notification-settings` | `/api/notification-settings` |

## Chi tiết từng endpoint

### `GET /notification-settings` {#get-notification-settings}

`/api/notification-settings`. Middleware: `requireAuth`.

- **Middleware:** `requireAuth`

### `PATCH /notification-settings` {#patch-notification-settings}

`/api/notification-settings`. Middleware: `requireAuth`.

- **Middleware:** `requireAuth`

## Ghi chú đọc code

- Mount prefix `/api` qua `app.ts`; file này: `routes/index.ts` → `./notification-settings.ts`.
- Handler đầy đủ: mở file TypeScript tại Shop (search theo path string).
- Quyền role: xem `reference/rbac.md` và middleware trong từng block.
