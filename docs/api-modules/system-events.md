# API module: `system-events`

**Mô tả:** File routes system-events.ts — 1 endpoint HTTP cho /api/.... REST handlers cho domain system-events.

**Source Shop:** `artifacts/api-server/src/routes/system-events.ts`

REST handlers cho domain **system-events**.

**Số endpoint trong file:** 1

## Danh sách endpoint (tóm tắt)

| Method | Path | Mô tả ngắn |
|--------|------|------------|
| GET | `/system-events` | `/api/system-events` |

## Chi tiết từng endpoint

### `GET /system-events` {#get-system-events}

`/api/system-events`. Middleware: `requireAuth`.

- **Middleware:** `requireAuth`

## Ghi chú đọc code

- Mount prefix `/api` qua `app.ts`; file này: `routes/index.ts` → `./system-events.ts`.
- Handler đầy đủ: mở file TypeScript tại Shop (search theo path string).
- Quyền role: xem `reference/rbac.md` và middleware trong từng block.
