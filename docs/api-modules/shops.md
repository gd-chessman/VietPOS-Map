# API module: `shops`

**Mô tả:** File routes shops.ts — 3 endpoint HTTP cho /api/.... REST handlers cho domain shops.

**Source Shop:** `artifacts/api-server/src/routes/shops.ts`

REST handlers cho domain **shops**.

**Số endpoint trong file:** 3

## Danh sách endpoint (tóm tắt)

| Method | Path | Mô tả ngắn |
|--------|------|------------|
| GET | `/shops` | `/api/shops` |
| POST | `/shops/heartbeat` | `/api/shops/heartbeat` |
| GET | `/shops/operational-events` | `/api/shops/operational-events` |

## Chi tiết từng endpoint

### `GET /shops` {#get-shops}

`/api/shops`. Middleware: `requireAuth`.

- **Middleware:** `requireAuth`

### `POST /shops/heartbeat` {#post-shops-heartbeat}

`/api/shops/heartbeat`. Middleware: `requireAuth`.

- **Middleware:** `requireAuth`

### `GET /shops/operational-events` {#get-shops-operational-events}

`/api/shops/operational-events`. Middleware: `requireAuth`.

- **Middleware:** `requireAuth`

## Ghi chú đọc code

- Mount prefix `/api` qua `app.ts`; file này: `routes/index.ts` → `./shops.ts`.
- Handler đầy đủ: mở file TypeScript tại Shop (search theo path string).
- Quyền role: xem `reference/rbac.md` và middleware trong từng block.
