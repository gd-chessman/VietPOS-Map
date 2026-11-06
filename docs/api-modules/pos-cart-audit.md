# API module: `pos-cart-audit`

**Mô tả:** File routes pos-cart-audit.ts — 3 endpoint HTTP cho /api/.... REST handlers cho domain pos-cart-audit.

**Source Shop:** `artifacts/api-server/src/routes/pos-cart-audit.ts`

REST handlers cho domain **pos-cart-audit**.

**Số endpoint trong file:** 3

## Danh sách endpoint (tóm tắt)

| Method | Path | Mô tả ngắn |
|--------|------|------------|
| POST | `/pos/cart-audit` | `/api/pos/cart-audit` |
| GET | `/reports/pos-cart-audit/summary` | `/api/reports/pos-cart-audit/summary` |
| GET | `/reports/pos-cart-audit` | `/api/reports/pos-cart-audit` |

## Chi tiết từng endpoint

### `POST /pos/cart-audit` {#post-pos-cart-audit}

`/api/pos/cart-audit`. Middleware: `requireAuth`.

- **Middleware:** `requireAuth`

### `GET /reports/pos-cart-audit/summary` {#get-reports-pos-cart-audit-summary}

`/api/reports/pos-cart-audit/summary`. Middleware: `requireAuth`.

- **Middleware:** `requireAuth`

### `GET /reports/pos-cart-audit` {#get-reports-pos-cart-audit}

`/api/reports/pos-cart-audit`. Middleware: `requireAuth`.

- **Middleware:** `requireAuth`

## Ghi chú đọc code

- Mount prefix `/api` qua `app.ts`; file này: `routes/index.ts` → `./pos-cart-audit.ts`.
- Handler đầy đủ: mở file TypeScript tại Shop (search theo path string).
- Quyền role: xem `reference/rbac.md` và middleware trong từng block.
