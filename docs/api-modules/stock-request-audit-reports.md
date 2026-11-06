# API module: `stock-request-audit-reports`

**Mô tả:** File routes stock-request-audit-reports.ts — 2 endpoint HTTP cho /api/.... REST handlers cho domain stock-request-audit-reports.

**Source Shop:** `artifacts/api-server/src/routes/stock-request-audit-reports.ts`

REST handlers cho domain **stock-request-audit-reports**.

**Số endpoint trong file:** 2

## Danh sách endpoint (tóm tắt)

| Method | Path | Mô tả ngắn |
|--------|------|------------|
| GET | `/reports/stock-request-audit/summary` | `/api/reports/stock-request-audit/summary` |
| GET | `/reports/stock-request-audit` | `/api/reports/stock-request-audit` |

## Chi tiết từng endpoint

### `GET /reports/stock-request-audit/summary` {#get-reports-stock-request-audit-summary}

`/api/reports/stock-request-audit/summary`. Middleware: `requireAuth`.

- **Middleware:** `requireAuth`

### `GET /reports/stock-request-audit` {#get-reports-stock-request-audit}

`/api/reports/stock-request-audit`. Middleware: `requireAuth`.

- **Middleware:** `requireAuth`

## Ghi chú đọc code

- Mount prefix `/api` qua `app.ts`; file này: `routes/index.ts` → `./stock-request-audit-reports.ts`.
- Handler đầy đủ: mở file TypeScript tại Shop (search theo path string).
- Quyền role: xem `reference/rbac.md` và middleware trong từng block.
