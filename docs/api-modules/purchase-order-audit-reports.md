# API module: `purchase-order-audit-reports`

**Mô tả:** File routes purchase-order-audit-reports.ts — 2 endpoint HTTP cho /api/.... REST handlers cho domain purchase-order-audit-reports.

**Source Shop:** `artifacts/api-server/src/routes/purchase-order-audit-reports.ts`

REST handlers cho domain **purchase-order-audit-reports**.

**Số endpoint trong file:** 2

## Danh sách endpoint (tóm tắt)

| Method | Path | Mô tả ngắn |
|--------|------|------------|
| GET | `/reports/purchase-order-audit/summary` | `/api/reports/purchase-order-audit/summary` |
| GET | `/reports/purchase-order-audit` | `/api/reports/purchase-order-audit` |

## Chi tiết từng endpoint

### `GET /reports/purchase-order-audit/summary` {#get-reports-purchase-order-audit-summary}

`/api/reports/purchase-order-audit/summary`. Middleware: `requireAuth`.

- **Middleware:** `requireAuth`

### `GET /reports/purchase-order-audit` {#get-reports-purchase-order-audit}

`/api/reports/purchase-order-audit`. Middleware: `requireAuth`.

- **Middleware:** `requireAuth`

## Ghi chú đọc code

- Mount prefix `/api` qua `app.ts`; file này: `routes/index.ts` → `./purchase-order-audit-reports.ts`.
- Handler đầy đủ: mở file TypeScript tại Shop (search theo path string).
- Quyền role: xem `reference/rbac.md` và middleware trong từng block.
