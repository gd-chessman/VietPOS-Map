# API module: `walk-in-customers`

**Mô tả:** File routes walk-in-customers.ts — 2 endpoint HTTP cho /api/.... REST handlers cho domain walk-in-customers.

**Source Shop:** `artifacts/api-server/src/routes/walk-in-customers.ts`

REST handlers cho domain **walk-in-customers**.

**Số endpoint trong file:** 2

## Danh sách endpoint (tóm tắt)

| Method | Path | Mô tả ngắn |
|--------|------|------------|
| GET | `/shops/:shopId/walk-in-customers/today` | `/api/shops/:shopId/walk-in-customers/today` |
| POST | `/shops/:shopId/walk-in-customers` | `/api/shops/:shopId/walk-in-customers` |

## Chi tiết từng endpoint

### `GET /shops/:shopId/walk-in-customers/today` {#get-shops--shopId-walk-in-customers-today}

`/api/shops/:shopId/walk-in-customers/today`. Middleware: `requireAuth`.

- **Middleware:** `requireAuth`

### `POST /shops/:shopId/walk-in-customers` {#post-shops--shopId-walk-in-customers}

`/api/shops/:shopId/walk-in-customers`. Middleware: `requireAuth, requireOperationalContext`.

- **Middleware:** `requireAuth`, `requireOperationalContext`

## Ghi chú đọc code

- Mount prefix `/api` qua `app.ts`; file này: `routes/index.ts` → `./walk-in-customers.ts`.
- Handler đầy đủ: mở file TypeScript tại Shop (search theo path string).
- Quyền role: xem `reference/rbac.md` và middleware trong từng block.
