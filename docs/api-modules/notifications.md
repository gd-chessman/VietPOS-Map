# API module: `notifications`

**Mô tả:** File routes notifications.ts — 2 endpoint HTTP cho /api/.... REST handlers cho domain notifications.

**Source Shop:** `artifacts/api-server/src/routes/notifications.ts`

REST handlers cho domain **notifications**.

**Số endpoint trong file:** 2

## Danh sách endpoint (tóm tắt)

| Method | Path | Mô tả ngắn |
|--------|------|------------|
| GET | `/notifications` | `/api/notifications` |
| POST | `/notifications/read` | `/api/notifications/read` |

## Chi tiết từng endpoint

### `GET /notifications` {#get-notifications}

`/api/notifications`. Middleware: `requireAuth`.

- **Middleware:** `requireAuth`

### `POST /notifications/read` {#post-notifications-read}

`/api/notifications/read`. Middleware: `requireAuth`.

- **Middleware:** `requireAuth`

## Ghi chú đọc code

- Mount prefix `/api` qua `app.ts`; file này: `routes/index.ts` → `./notifications.ts`.
- Handler đầy đủ: mở file TypeScript tại Shop (search theo path string).
- Quyền role: xem `reference/rbac.md` và middleware trong từng block.
