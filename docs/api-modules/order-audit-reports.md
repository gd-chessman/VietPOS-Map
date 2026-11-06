# API module: `order-audit-reports`

**Mô tả:** File routes order-audit-reports.ts — 2 endpoint HTTP cho /api/.... REST handlers cho domain order-audit-reports.

**Source Shop:** `artifacts/api-server/src/routes/order-audit-reports.ts`

REST handlers cho domain **order-audit-reports**.

**Số endpoint trong file:** 2

## Danh sách endpoint (tóm tắt)

| Method | Path | Mô tả ngắn |
|--------|------|------------|
| GET | `/reports/order-audit/summary` | `/api/reports/order-audit/summary` |
| GET | `/reports/order-audit` | `/api/reports/order-audit` |

## Chi tiết từng endpoint

### `GET /reports/order-audit/summary` {#get-reports-order-audit-summary}

`/api/reports/order-audit/summary`. Middleware: `requireAuth`.

- **Middleware:** `requireAuth`

### `GET /reports/order-audit` {#get-reports-order-audit}

`/api/reports/order-audit`. Middleware: `requireAuth`.

- **Middleware:** `requireAuth`

## Ghi chú đọc code

- Mount prefix `/api` qua `app.ts`; file này: `routes/index.ts` → `./order-audit-reports.ts`.
- Handler đầy đủ: mở file TypeScript tại Shop (search theo path string).
- Quyền role: xem `reference/rbac.md` và middleware trong từng block.
