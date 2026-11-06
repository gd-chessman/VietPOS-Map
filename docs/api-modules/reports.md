# API module: `reports`

**Mô tả:** File routes reports.ts — 4 endpoint HTTP cho /api/.... REST handlers cho domain reports.

**Source Shop:** `artifacts/api-server/src/routes/reports.ts`

REST handlers cho domain **reports**.

**Số endpoint trong file:** 4

## Danh sách endpoint (tóm tắt)

| Method | Path | Mô tả ngắn |
|--------|------|------------|
| GET | `/reports/staff` | `/api/reports/staff` |
| GET | `/reports/sales-staff` | `/api/reports/sales-staff` |
| GET | `/reports/reprints` | `/api/reports/reprints` |
| GET | `/reports/staff/:userId/detail` | `/api/reports/staff/:userId/detail` |

## Chi tiết từng endpoint

### `GET /reports/staff` {#get-reports-staff}

`/api/reports/staff`. Middleware: `requireAuth`.

- **Middleware:** `requireAuth`

### `GET /reports/sales-staff` {#get-reports-sales-staff}

`/api/reports/sales-staff`. Middleware: `requireAuth`.

- **Middleware:** `requireAuth`

### `GET /reports/reprints` {#get-reports-reprints}

`/api/reports/reprints`. Middleware: `requireAuth`.

- **Middleware:** `requireAuth`

### `GET /reports/staff/:userId/detail` {#get-reports-staff--userId-detail}

`/api/reports/staff/:userId/detail`. Middleware: `requireAuth`.

- **Middleware:** `requireAuth`

## Ghi chú đọc code

- Mount prefix `/api` qua `app.ts`; file này: `routes/index.ts` → `./reports.ts`.
- Handler đầy đủ: mở file TypeScript tại Shop (search theo path string).
- Quyền role: xem `reference/rbac.md` và middleware trong từng block.
