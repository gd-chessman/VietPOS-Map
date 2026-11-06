# API module: `stock-requests`

**Mô tả:** File routes stock-requests.ts — 14 endpoint HTTP cho /api/.... Phiếu yêu cầu nhập/xuất nội bộ: tạo → duyệt → hoàn tất → cập nhật tồn. Frontend: pages/stock-requests.tsx.

**Source Shop:** `artifacts/api-server/src/routes/stock-requests.ts`

Phiếu yêu cầu nhập/xuất nội bộ: tạo → duyệt → hoàn tất → cập nhật tồn.

**Frontend:** `pages/stock-requests.tsx`.

**Số endpoint trong file:** 14

## Danh sách endpoint (tóm tắt)

| Method | Path | Mô tả ngắn |
|--------|------|------------|
| GET | `/stock-requests` | `/api/stock-requests` |
| GET | `/stock-requests/pending-count` | `/api/stock-requests/pending-count` |
| GET | `/stock-requests/approved-count` | `/api/stock-requests/approved-count` |
| GET | `/stock-requests/in-transit-count` | `/api/stock-requests/in-transit-count` |
| GET | `/stock-requests/meta/hub-shop` | `/api/stock-requests/meta/hub-shop` |
| GET | `/stock-requests/meta/hub-inventory` | `/api/stock-requests/meta/hub-inventory` |
| GET | `/stock-requests/meta/shop-inventory` | `/api/stock-requests/meta/shop-inventory` |
| GET | `/stock-requests/:id` | `/api/stock-requests/:id` |
| POST | `/stock-requests` | `/api/stock-requests` |
| PATCH | `/stock-requests/:id/approve` | `/api/stock-requests/:id/approve` |
| PATCH | `/stock-requests/:id/ship` | `/api/stock-requests/:id/ship` |
| PATCH | `/stock-requests/:id/reject` | `/api/stock-requests/:id/reject` |
| PATCH | `/stock-requests/:id/complete` | `/api/stock-requests/:id/complete` |
| PATCH | `/stock-requests/:id/cancel` | `/api/stock-requests/:id/cancel` |

## Chi tiết từng endpoint

### `GET /stock-requests` {#get-stock-requests}

`/api/stock-requests`. Middleware: `requireAuth`.

- **Middleware:** `requireAuth`

### `GET /stock-requests/pending-count` {#get-stock-requests-pending-count}

`/api/stock-requests/pending-count`. Middleware: `requireAuth`.

- **Middleware:** `requireAuth`

### `GET /stock-requests/approved-count` {#get-stock-requests-approved-count}

`/api/stock-requests/approved-count`. Middleware: `requireAuth`.

- **Middleware:** `requireAuth`

### `GET /stock-requests/in-transit-count` {#get-stock-requests-in-transit-count}

`/api/stock-requests/in-transit-count`. Middleware: `requireAuth`.

- **Middleware:** `requireAuth`

### `GET /stock-requests/meta/hub-shop` {#get-stock-requests-meta-hub-shop}

`/api/stock-requests/meta/hub-shop`. Middleware: `requireAuth`.

- **Middleware:** `requireAuth`

### `GET /stock-requests/meta/hub-inventory` {#get-stock-requests-meta-hub-inventory}

`/api/stock-requests/meta/hub-inventory`. Middleware: `requireAuth`.

- **Middleware:** `requireAuth`

### `GET /stock-requests/meta/shop-inventory` {#get-stock-requests-meta-shop-inventory}

`/api/stock-requests/meta/shop-inventory`. Middleware: `requireAuth`.

- **Middleware:** `requireAuth`

### `GET /stock-requests/:id` {#get-stock-requests--id}

`/api/stock-requests/:id`. Middleware: `requireAuth`.

- **Middleware:** `requireAuth`

### `POST /stock-requests` {#post-stock-requests}

`/api/stock-requests`. Middleware: `requireAuth`.

- **Middleware:** `requireAuth`

### `PATCH /stock-requests/:id/approve` {#patch-stock-requests--id-approve}

`/api/stock-requests/:id/approve`. Middleware: `requireAuth`.

- **Middleware:** `requireAuth`

### `PATCH /stock-requests/:id/ship` {#patch-stock-requests--id-ship}

`/api/stock-requests/:id/ship`. Middleware: `requireAuth`.

- **Middleware:** `requireAuth`

### `PATCH /stock-requests/:id/reject` {#patch-stock-requests--id-reject}

`/api/stock-requests/:id/reject`. Middleware: `requireAuth`.

- **Middleware:** `requireAuth`

### `PATCH /stock-requests/:id/complete` {#patch-stock-requests--id-complete}

`/api/stock-requests/:id/complete`. Middleware: `requireAuth`.

- **Middleware:** `requireAuth`

### `PATCH /stock-requests/:id/cancel` {#patch-stock-requests--id-cancel}

`/api/stock-requests/:id/cancel`. Middleware: `requireAuth`.

- **Middleware:** `requireAuth`

## Ghi chú đọc code

- Mount prefix `/api` qua `app.ts`; file này: `routes/index.ts` → `./stock-requests.ts`.
- Handler đầy đủ: mở file TypeScript tại Shop (search theo path string).
- Quyền role: xem `reference/rbac.md` và middleware trong từng block.
