# API module: `public-vat-invoice`

**Mô tả:** File routes public-vat-invoice.ts — 3 endpoint HTTP cho /api/.... REST handlers cho domain public-vat-invoice.

**Source Shop:** `artifacts/api-server/src/routes/public-vat-invoice.ts`

REST handlers cho domain **public-vat-invoice**.

**Số endpoint trong file:** 3

## Danh sách endpoint (tóm tắt)

| Method | Path | Mô tả ngắn |
|--------|------|------------|
| GET | `/public/vat-invoice` | `/api/public/vat-invoice` |
| PATCH | `/public/vat-invoice` | `/api/public/vat-invoice` |
| GET | `/public/vat-invoice/pdf` | `/api/public/vat-invoice/pdf` |

## Chi tiết từng endpoint

### `GET /public/vat-invoice` {#get-public-vat-invoice}

`/api/public/vat-invoice`. Middleware: `requireAuth (mặc định — kiểm tra file)`.

### `PATCH /public/vat-invoice` {#patch-public-vat-invoice}

`/api/public/vat-invoice`. Middleware: `requireAuth (mặc định — kiểm tra file)`.

### `GET /public/vat-invoice/pdf` {#get-public-vat-invoice-pdf}

`/api/public/vat-invoice/pdf`. Middleware: `requireAuth (mặc định — kiểm tra file)`.

## Ghi chú đọc code

- Mount prefix `/api` qua `app.ts`; file này: `routes/index.ts` → `./public-vat-invoice.ts`.
- Handler đầy đủ: mở file TypeScript tại Shop (search theo path string).
- Quyền role: xem `reference/rbac.md` và middleware trong từng block.
