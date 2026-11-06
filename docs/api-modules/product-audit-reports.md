# API module: `product-audit-reports`

**Mô tả:** File routes product-audit-reports.ts — 2 endpoint HTTP cho /api/.... REST handlers cho domain product-audit-reports.

**Source Shop:** `artifacts/api-server/src/routes/product-audit-reports.ts`

REST handlers cho domain **product-audit-reports**.

**Số endpoint trong file:** 2

## Danh sách endpoint (tóm tắt)

| Method | Path | Mô tả ngắn |
|--------|------|------------|
| GET | `/reports/product-audit/summary` | `/api/reports/product-audit/summary` |
| GET | `/reports/product-audit` | `/api/reports/product-audit` |

## Chi tiết từng endpoint

### `GET /reports/product-audit/summary` {#get-reports-product-audit-summary}

`/api/reports/product-audit/summary`. Middleware: `requireAuth`.

- **Middleware:** `requireAuth`

### `GET /reports/product-audit` {#get-reports-product-audit}

`/api/reports/product-audit`. Middleware: `requireAuth`.

- **Middleware:** `requireAuth`

## Ghi chú đọc code

- Mount prefix `/api` qua `app.ts`; file này: `routes/index.ts` → `./product-audit-reports.ts`.
- Handler đầy đủ: mở file TypeScript tại Shop (search theo path string).
- Quyền role: xem `reference/rbac.md` và middleware trong từng block.
