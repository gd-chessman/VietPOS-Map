# Module API: `shop-api-keys`

**Mô tả:** Module API shop-api-keys.ts — 8 endpoint. API key cho widget / thiết bị (ESP32 visitor-counts). Giao diện: pages/chain-api-keys.tsx (nếu có).

**Mã nguồn Shop:** `artifacts/api-server/src/routes/shop-api-keys.ts`

API key cho widget / thiết bị (ESP32 visitor-counts).

**Giao diện:** `pages/chain-api-keys.tsx` (nếu có).

**Số endpoint:** 8

## Bảng endpoint (tóm tắt)

| Method | Path | Mô tả ngắn |
|--------|------|------------|
| GET | `/shop-api-keys` | Đường dẫn đầy đủ `/api/shop-api-keys` |
| GET | `/shop-api-keys/overview` | Đường dẫn đầy đủ `/api/shop-api-keys/overview` |
| PATCH | `/shop-api-keys/shops/:shopId` | Đường dẫn đầy đủ `/api/shop-api-keys/shops/:shopId` |
| POST | `/shop-api-keys` | Đường dẫn đầy đủ `/api/shop-api-keys` |
| PATCH | `/shop-api-keys/:id` | Đường dẫn đầy đủ `/api/shop-api-keys/:id` |
| DELETE | `/shop-api-keys/:id` | Đường dẫn đầy đủ `/api/shop-api-keys/:id` |
| POST | `/visitor-counts/status` | Đường dẫn đầy đủ `/api/visitor-counts/status` |
| POST | `/visitor-counts` | Đường dẫn đầy đủ `/api/visitor-counts` |

## Chi tiết từng endpoint

### `GET /shop-api-keys` {#get-shop-api-keys}

Đường dẫn đầy đủ `/api/shop-api-keys`. Lớp kiểm tra: `requireAuth, requireChainManagement`.

- **Lớp kiểm tra (middleware):** `requireAuth`, `requireChainManagement`

### `GET /shop-api-keys/overview` {#get-shop-api-keys-overview}

Đường dẫn đầy đủ `/api/shop-api-keys/overview`. Lớp kiểm tra: `requireAuth, requireChainManagement`.

- **Lớp kiểm tra (middleware):** `requireAuth`, `requireChainManagement`

### `PATCH /shop-api-keys/shops/:shopId` {#patch-shop-api-keys-shops--shopId}

Đường dẫn đầy đủ `/api/shop-api-keys/shops/:shopId`. Lớp kiểm tra: `requireAuth, requireChainManagement`.

- **Lớp kiểm tra (middleware):** `requireAuth`, `requireChainManagement`

### `POST /shop-api-keys` {#post-shop-api-keys}

Đường dẫn đầy đủ `/api/shop-api-keys`. Lớp kiểm tra: `requireAuth, requireChainManagement`.

- **Lớp kiểm tra (middleware):** `requireAuth`, `requireChainManagement`

### `PATCH /shop-api-keys/:id` {#patch-shop-api-keys--id}

Đường dẫn đầy đủ `/api/shop-api-keys/:id`. Lớp kiểm tra: `requireAuth, requireChainManagement`.

- **Lớp kiểm tra (middleware):** `requireAuth`, `requireChainManagement`

### `DELETE /shop-api-keys/:id` {#delete-shop-api-keys--id}

Đường dẫn đầy đủ `/api/shop-api-keys/:id`. Lớp kiểm tra: `requireAuth, requireChainManagement`.

- **Lớp kiểm tra (middleware):** `requireAuth`, `requireChainManagement`

### `POST /visitor-counts/status` {#post-visitor-counts-status}

Đường dẫn đầy đủ `/api/visitor-counts/status`. Lớp kiểm tra: `requireAuth (mặc định — xem file)`.

### `POST /visitor-counts` {#post-visitor-counts}

Đường dẫn đầy đủ `/api/visitor-counts`. Lớp kiểm tra: `requireAuth (mặc định — xem file)`.

## Ghi chú đọc mã

- Gắn prefix `/api` trong `app.ts`; file route: `routes/index.ts` → `./shop-api-keys.ts`.
- Handler đầy đủ: mở file TypeScript tại Shop (tìm theo chuỗi path).
- Quyền role: `tham-chieu/phan-quyen-rbac/README.md` (tiếng Anh gốc) + các `require*` trong từng endpoint.

**Đọc tiếp:** [Hướng dẫn Map](../../huong-dan-doc/) · [Mục lục](../../README.md)
