# API module: `feedback`

**Mô tả:** File routes feedback.ts — 5 endpoint HTTP cho /api/.... REST handlers cho domain feedback.

**Source Shop:** `artifacts/api-server/src/routes/feedback.ts`

REST handlers cho domain **feedback**.

**Số endpoint trong file:** 5

## Danh sách endpoint (tóm tắt)

| Method | Path | Mô tả ngắn |
|--------|------|------------|
| POST | `/public/feedback` | `/api/public/feedback` |
| GET | `/feedback/public-url` | `/api/feedback/public-url` |
| PATCH | `/feedback/public-url` | `/api/feedback/public-url` |
| GET | `/feedback/stats` | `/api/feedback/stats` |
| GET | `/feedback` | `/api/feedback` |

## Chi tiết từng endpoint

### `POST /public/feedback` {#post-public-feedback}

`/api/public/feedback`. Middleware: `requireAuth (mặc định — kiểm tra file)`.

### `GET /feedback/public-url` {#get-feedback-public-url}

`/api/feedback/public-url`. Middleware: `requireAuth`.

- **Middleware:** `requireAuth`

### `PATCH /feedback/public-url` {#patch-feedback-public-url}

`/api/feedback/public-url`. Middleware: `requireAuth, requireManagerOrAdmin`.

- **Middleware:** `requireAuth`, `requireManagerOrAdmin`

### `GET /feedback/stats` {#get-feedback-stats}

`/api/feedback/stats`. Middleware: `requireAuth, requireManagerOrAdmin`.

- **Middleware:** `requireAuth`, `requireManagerOrAdmin`

### `GET /feedback` {#get-feedback}

`/api/feedback`. Middleware: `requireAuth, requireManagerOrAdmin`.

- **Middleware:** `requireAuth`, `requireManagerOrAdmin`

## Ghi chú đọc code

- Mount prefix `/api` qua `app.ts`; file này: `routes/index.ts` → `./feedback.ts`.
- Handler đầy đủ: mở file TypeScript tại Shop (search theo path string).
- Quyền role: xem `reference/rbac.md` và middleware trong từng block.
