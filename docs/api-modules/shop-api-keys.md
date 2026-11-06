# API module: `shop-api-keys`

**Mô tả:** File routes shop-api-keys.ts — 8 endpoint HTTP cho /api/.... API key cho widget / thiết bị (ESP32 visitor-counts). Frontend: pages/chain-api-keys.tsx (nếu có).

**Source Shop:** `artifacts/api-server/src/routes/shop-api-keys.ts`

API key cho widget / thiết bị (ESP32 visitor-counts).

**Frontend:** `pages/chain-api-keys.tsx` (nếu có).

**Số endpoint trong file:** 8

## Danh sách endpoint (tóm tắt)

| Method | Path | Mô tả ngắn |
|--------|------|------------|
| GET | `/shop-api-keys` | `/api/shop-api-keys` |
| GET | `/shop-api-keys/overview` | `/api/shop-api-keys/overview` |
| PATCH | `/shop-api-keys/shops/:shopId` | `/api/shop-api-keys/shops/:shopId` |
| POST | `/shop-api-keys` | `/api/shop-api-keys` |
| PATCH | `/shop-api-keys/:id` | `/api/shop-api-keys/:id` |
| DELETE | `/shop-api-keys/:id` | `/api/shop-api-keys/:id` |
| POST | `/visitor-counts/status` | `/api/visitor-counts/status` |
| POST | `/visitor-counts` | `/api/visitor-counts` |

## Chi tiết từng endpoint

### `GET /shop-api-keys` {#get-shop-api-keys}

`/api/shop-api-keys`. Middleware: `requireAuth, requireChainManagement`.

- **Middleware:** `requireAuth`, `requireChainManagement`

### `GET /shop-api-keys/overview` {#get-shop-api-keys-overview}

`/api/shop-api-keys/overview`. Middleware: `requireAuth, requireChainManagement`.

- **Middleware:** `requireAuth`, `requireChainManagement`

### `PATCH /shop-api-keys/shops/:shopId` {#patch-shop-api-keys-shops--shopId}

`/api/shop-api-keys/shops/:shopId`. Middleware: `requireAuth, requireChainManagement`.

- **Middleware:** `requireAuth`, `requireChainManagement`

### `POST /shop-api-keys` {#post-shop-api-keys}

`/api/shop-api-keys`. Middleware: `requireAuth, requireChainManagement`.

- **Middleware:** `requireAuth`, `requireChainManagement`

### `PATCH /shop-api-keys/:id` {#patch-shop-api-keys--id}

`/api/shop-api-keys/:id`. Middleware: `requireAuth, requireChainManagement`.

- **Middleware:** `requireAuth`, `requireChainManagement`

### `DELETE /shop-api-keys/:id` {#delete-shop-api-keys--id}

`/api/shop-api-keys/:id`. Middleware: `requireAuth, requireChainManagement`.

- **Middleware:** `requireAuth`, `requireChainManagement`

### `POST /visitor-counts/status` {#post-visitor-counts-status}

`/api/visitor-counts/status`. Middleware: `requireAuth (mặc định — kiểm tra file)`.

### `POST /visitor-counts` {#post-visitor-counts}

`/api/visitor-counts`. Middleware: `requireAuth (mặc định — kiểm tra file)`.

## Ghi chú đọc code

- Mount prefix `/api` qua `app.ts`; file này: `routes/index.ts` → `./shop-api-keys.ts`.
- Handler đầy đủ: mở file TypeScript tại Shop (search theo path string).
- Quyền role: xem `reference/rbac.md` và middleware trong từng block.
