# API module: `org-viettel-settings`

**Mô tả:** File routes org-viettel-settings.ts — 2 endpoint HTTP cho /api/.... REST handlers cho domain org-viettel-settings.

**Source Shop:** `artifacts/api-server/src/routes/org-viettel-settings.ts`

REST handlers cho domain **org-viettel-settings**.

**Số endpoint trong file:** 2

## Danh sách endpoint (tóm tắt)

| Method | Path | Mô tả ngắn |
|--------|------|------------|
| GET | `/viettel-invoice/settings` | `/api/viettel-invoice/settings` |
| PATCH | `/viettel-invoice/settings` | `/api/viettel-invoice/settings` |

## Chi tiết từng endpoint

### `GET /viettel-invoice/settings` {#get-viettel-invoice-settings}

`/api/viettel-invoice/settings`. Middleware: `requireAuth`.

- **Middleware:** `requireAuth`

### `PATCH /viettel-invoice/settings` {#patch-viettel-invoice-settings}

`/api/viettel-invoice/settings`. Middleware: `requireAuth`.

- **Middleware:** `requireAuth`

## Ghi chú đọc code

- Mount prefix `/api` qua `app.ts`; file này: `routes/index.ts` → `./org-viettel-settings.ts`.
- Handler đầy đủ: mở file TypeScript tại Shop (search theo path string).
- Quyền role: xem `reference/rbac.md` và middleware trong từng block.
