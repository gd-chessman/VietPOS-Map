# API module: `sync`

**Mô tả:** File routes sync.ts — 2 endpoint HTTP cho /api/.... Endpoint đồng bộ client (pull/push) cho offline IndexedDB.

**Source Shop:** `artifacts/api-server/src/routes/sync.ts`

Endpoint đồng bộ client (pull/push) cho offline IndexedDB.

**Số endpoint trong file:** 2

## Danh sách endpoint (tóm tắt)

| Method | Path | Mô tả ngắn |
|--------|------|------------|
| GET | `/sync/catalog` | `/api/sync/catalog` |
| GET | `/sync/shift-orders` | `/api/sync/shift-orders` |

## Chi tiết từng endpoint

### `GET /sync/catalog` {#get-sync-catalog}

`/api/sync/catalog`. Middleware: `requireAuth`.

- **Middleware:** `requireAuth`

### `GET /sync/shift-orders` {#get-sync-shift-orders}

`/api/sync/shift-orders`. Middleware: `requireAuth`.

- **Middleware:** `requireAuth`

## Ghi chú đọc code

- Mount prefix `/api` qua `app.ts`; file này: `routes/index.ts` → `./sync.ts`.
- Handler đầy đủ: mở file TypeScript tại Shop (search theo path string).
- Quyền role: xem `reference/rbac.md` và middleware trong từng block.
