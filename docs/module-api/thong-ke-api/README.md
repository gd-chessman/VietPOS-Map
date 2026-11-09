# Module API: `statistics`

**Mô tả:** Thống kê bán theo sản phẩm.

**Mã nguồn Shop:** `artifacts/api-server/src/routes/statistics.ts`

Thống kê bán theo sản phẩm.

**Số endpoint:** 6

**Contract API:** Mỗi endpoint có mục **URL**, body/query (từ code + schema Zod orval khi có), bảng lỗi `error`, và response (Zod hoặc trường `res.json`).

## Bảng endpoint (tóm tắt)

| Method | Path | Mô tả ngắn |
|--------|------|------------|
| GET | `/statistics/products` | Đường dẫn đầy đủ `/api/statistics/products` |
| GET | `/statistics/overview` | Đường dẫn đầy đủ `/api/statistics/overview` |
| GET | `/statistics/trend` | Đường dẫn đầy đủ `/api/statistics/trend` |
| GET | `/statistics/product-sales` | Đường dẫn đầy đủ `/api/statistics/product-sales` |
| GET | `/statistics/top-products` | Đường dẫn đầy đủ `/api/statistics/top-products` |
| GET | `/statistics/catalog` | Đường dẫn đầy đủ `/api/statistics/catalog` |

## Chi tiết từng endpoint

### `GET /statistics/products` {#get-statistics-products}

Đường dẫn đầy đủ `/api/statistics/products`. Lớp kiểm tra: `requireAuth`.

**URL:** `GET /api/statistics/products`

**Lớp route:** `requireAuth`

*Handler không trích được contract tự động — mở file route TypeScript.*

### `GET /statistics/overview` {#get-statistics-overview}

Đường dẫn đầy đủ `/api/statistics/overview`. Lớp kiểm tra: `requireAuth`.

**URL:** `GET /api/statistics/overview`

**Lớp route:** `requireAuth`

**Response 200** — trường top-level (trích `res.json`):

`current`, `from`, `previous`, `to`

### `GET /statistics/trend` {#get-statistics-trend}

Đường dẫn đầy đủ `/api/statistics/trend`. Lớp kiểm tra: `requireAuth`.

**URL:** `GET /api/statistics/trend`

**Lớp route:** `requireAuth`

**Response 200** — trường top-level (trích `res.json`):

`current`, `from`, `previous`, `to`

### `GET /statistics/product-sales` {#get-statistics-product-sales}

Đường dẫn đầy đủ `/api/statistics/product-sales`. Lớp kiểm tra: `requireAuth`.

**URL:** `GET /api/statistics/product-sales`

**Lớp route:** `requireAuth`

**Lỗi JSON** (`error` string):

| HTTP | Message |
|------|---------|
| **400** | `productId required` |

**Response 200** — trường top-level (trích `res.json`):

`data`

### `GET /statistics/top-products` {#get-statistics-top-products}

Đường dẫn đầy đủ `/api/statistics/top-products`. Lớp kiểm tra: `requireAuth`.

**URL:** `GET /api/statistics/top-products`

**Lớp route:** `requireAuth`

**Query:** `categoryId`, `from`, `granularity`, `limit`, `page`, `period`, `q`, `sortBy`, `supplierId`, `to`

**Response 200** — trường top-level (trích `res.json`):

`summary`, `totalCost`, `totalProfit`, `totalQuantity`, `totalRevenue`

### `GET /statistics/catalog` {#get-statistics-catalog}

Đường dẫn đầy đủ `/api/statistics/catalog`. Lớp kiểm tra: `requireAuth`.

**URL:** `GET /api/statistics/catalog`

**Lớp route:** `requireAuth`

*Handler không trích được contract tự động — mở file route TypeScript.*

## Ghi chú đọc mã

- Gắn prefix `/api` trong `app.ts`; file route: `routes/index.ts` → `./statistics.ts`.
- Handler đầy đủ: mở file TypeScript tại Shop (tìm theo chuỗi path).
- Quyền role: `tham-chieu/phan-quyen-rbac/README.md` (tiếng Anh gốc) + các `require*` trong từng endpoint.

**Đọc tiếp:** [Hướng dẫn Map](../../huong-dan-doc/) · [Mục lục](../../README.md)
