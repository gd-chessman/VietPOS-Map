# Module API: `shop-api-keys`

**Mô tả:** API key shop (widget, ESP32).

**Mã nguồn Shop:** `artifacts/api-server/src/routes/shop-api-keys.ts`

API key cho widget / thiết bị (ESP32 visitor-counts).

**Giao diện:** `pages/chain-api-keys.tsx` (nếu có).

**Số endpoint:** 8

**Contract API:** Mỗi endpoint có mục **URL**, body/query (từ code + schema Zod orval khi có), bảng lỗi `error`, và response (Zod hoặc trường `res.json`).

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

**URL:** `GET /api/shop-api-keys`

**Lớp route:** `requireAuth`, `requireChainManagement`

*Handler không trích được contract tự động — mở file route TypeScript.*

### `GET /shop-api-keys/overview` {#get-shop-api-keys-overview}

Đường dẫn đầy đủ `/api/shop-api-keys/overview`. Lớp kiểm tra: `requireAuth, requireChainManagement`.

**URL:** `GET /api/shop-api-keys/overview`

**Lớp route:** `requireAuth`, `requireChainManagement`

*Handler không trích được contract tự động — mở file route TypeScript.*

### `PATCH /shop-api-keys/shops/:shopId` {#patch-shop-api-keys-shops--shopId}

Đường dẫn đầy đủ `/api/shop-api-keys/shops/:shopId`. Lớp kiểm tra: `requireAuth, requireChainManagement`.

**URL:** `PATCH /api/shop-api-keys/shops/:shopId`

**Lớp route:** `requireAuth`, `requireChainManagement`

**Request body** (`application/json`, trích từ code):

| Trường | Ghi chú |
|--------|---------|
| `manualVisitorEntryEnabled` | xem handler |

**Path params:** `shopId`

**Lỗi JSON** (`error` string):

| HTTP | Message |
|------|---------|
| **400** | `Cửa hàng không hợp lệ` |
| **400** | `Thiếu manualVisitorEntryEnabled` |
| **400** | `manualVisitorEntryEnabled phải là boolean` |
| **404** | `Không tìm thấy cửa hàng` |

### `POST /shop-api-keys` {#post-shop-api-keys}

Đường dẫn đầy đủ `/api/shop-api-keys`. Lớp kiểm tra: `requireAuth, requireChainManagement`.

**URL:** `POST /api/shop-api-keys`

**Lớp route:** `requireAuth`, `requireChainManagement`

**Request body** (`application/json`, trích từ code):

| Trường | Ghi chú |
|--------|---------|
| `countMode` | xem handler |
| `label` | xem handler |
| `shopId` | xem handler |

**Lỗi JSON** (`error` string):

| HTTP | Message |
|------|---------|
| **400** | `Chọn cửa hàng để cấp API key` |
| **400** | `Cửa hàng không hoạt động` |

**Response 201** — trường top-level (trích `res.json`):

`createdAt`, `id`, `shopCode`, `shopId`, `shopName`

### `PATCH /shop-api-keys/:id` {#patch-shop-api-keys--id}

Đường dẫn đầy đủ `/api/shop-api-keys/:id`. Lớp kiểm tra: `requireAuth, requireChainManagement`.

**URL:** `PATCH /api/shop-api-keys/:id`

**Lớp route:** `requireAuth`, `requireChainManagement`

**Request body** (`application/json`, trích từ code):

| Trường | Ghi chú |
|--------|---------|
| `countMode` | xem handler |
| `label` | xem handler |
| `status` | xem handler |

**Path params:** `id`

**Lỗi JSON** (`error` string):

| HTTP | Message |
|------|---------|
| **400** | `API key không hợp lệ` |
| **400** | `status phải là active hoặc disabled` |
| **400** | `countMode không hợp lệ` |
| **400** | `Không có thay đổi` |
| **404** | `Không tìm thấy API key` |

### `DELETE /shop-api-keys/:id` {#delete-shop-api-keys--id}

Đường dẫn đầy đủ `/api/shop-api-keys/:id`. Lớp kiểm tra: `requireAuth, requireChainManagement`.

**URL:** `DELETE /api/shop-api-keys/:id`

**Lớp route:** `requireAuth`, `requireChainManagement`

**Request body** (`application/json`, trích từ code):

| Trường | Ghi chú |
|--------|---------|
| `apiKey` | xem handler |
| `shopCode` | xem handler |
| `shopId` | xem handler |

**Path params:** `id`

**Lỗi JSON** (`error` string):

| HTTP | Message |
|------|---------|
| **400** | `API key không hợp lệ` |
| **404** | `Không tìm thấy API key` |
| **401** | `API key không hợp lệ` |
| **403** | `Cửa hàng đang ngừng hoạt động` |
| **403** | `API key không thuộc cửa hàng này` |

**Response 200** — trường top-level (trích `res.json`):

`ok`

### `POST /visitor-counts/status` {#post-visitor-counts-status}

Đường dẫn đầy đủ `/api/visitor-counts/status`. Lớp kiểm tra: `requireAuth (mặc định — xem file)`.

**URL:** `POST /api/visitor-counts/status`

**Lớp route:** `requireAuth` (hoặc public — xem route)

**Response 200** — trường top-level (trích `res.json`):

`ok`, `serverTime`, `shopId`, `shopName`, `visitorCount`

### `POST /visitor-counts` {#post-visitor-counts}

Đường dẫn đầy đủ `/api/visitor-counts`. Lớp kiểm tra: `requireAuth (mặc định — xem file)`.

**URL:** `POST /api/visitor-counts`

**Lớp route:** `requireAuth` (hoặc public — xem route)

**Request body** (`application/json`, trích từ code):

| Trường | Ghi chú |
|--------|---------|
| `count` | xem handler |

**Response 201** — trường top-level (trích `res.json`):

`beamsReported`, `countMode`, `guestsAdded`, `ok`, `shopId`, `shopName`

## Ghi chú đọc mã

- Gắn prefix `/api` trong `app.ts`; file route: `routes/index.ts` → `./shop-api-keys.ts`.
- Handler đầy đủ: mở file TypeScript tại Shop (tìm theo chuỗi path).
- Quyền role: `tham-chieu/phan-quyen-rbac/README.md` (tiếng Anh gốc) + các `require*` trong từng endpoint.

**Đọc tiếp:** [Hướng dẫn Map](../../huong-dan-doc/) · [Mục lục](../../README.md)
