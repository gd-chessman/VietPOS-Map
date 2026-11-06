# API module: `inventory`

**Mô tả:** File routes inventory.ts — 2 endpoint HTTP cho /api/.... REST handlers cho domain inventory.

**Source Shop:** `artifacts/api-server/src/routes/inventory.ts`

REST handlers cho domain **inventory**.

**Số endpoint trong file:** 2

## Danh sách endpoint (tóm tắt)

| Method | Path | Mô tả ngắn |
|--------|------|------------|
| GET | `/inventory` | `/api/inventory` |
| PATCH | `/inventory/:productId` | `/api/inventory/:productId` |

## Chi tiết từng endpoint

### `GET /inventory` {#get-inventory}

`/api/inventory`. Middleware: `requireAuth`.

- **Middleware:** `requireAuth`

### `PATCH /inventory/:productId` {#patch-inventory--productId}

`/api/inventory/:productId`. Middleware: `requireAuth, requireOperationalContext`.

- **Middleware:** `requireAuth`, `requireOperationalContext`

## Ghi chú đọc code

- Mount prefix `/api` qua `app.ts`; file này: `routes/index.ts` → `./inventory.ts`.
- Handler đầy đủ: mở file TypeScript tại Shop (search theo path string).
- Quyền role: xem `reference/rbac.md` và middleware trong từng block.
