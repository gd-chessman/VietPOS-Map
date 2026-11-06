# Module API: `dashboard`

**Mô tả:** Module API dashboard.ts — 17 endpoint. Số liệu tổng quan: doanh thu, đơn, tồn thấp.

**Mã nguồn Shop:** `artifacts/api-server/src/routes/dashboard.ts`

Số liệu tổng quan: doanh thu, đơn, tồn thấp.

**Số endpoint:** 17

**Contract API:** Mỗi endpoint có mục **URL**, body/query (từ code + schema Zod orval khi có), bảng lỗi `error`, và response (Zod hoặc trường `res.json`).

## Bảng endpoint (tóm tắt)

| Method | Path | Mô tả ngắn |
|--------|------|------------|
| GET | `/dashboard` | Đường dẫn đầy đủ `/api/dashboard` |
| GET | `/chain-dashboard` | Đường dẫn đầy đủ `/api/chain-dashboard` |
| GET | `/dashboard/revenue-chart` | Đường dẫn đầy đủ `/api/dashboard/revenue-chart` |
| GET | `/dashboard/period-visitor-stats` | Đường dẫn đầy đủ `/api/dashboard/period-visitor-stats` |
| GET | `/dashboard/period-sold-stats` | Đường dẫn đầy đủ `/api/dashboard/period-sold-stats` |
| GET | `/dashboard/period-cancel-stats` | Đường dẫn đầy đủ `/api/dashboard/period-cancel-stats` |
| GET | `/chain-dashboard/revenue-chart` | Đường dẫn đầy đủ `/api/chain-dashboard/revenue-chart` |
| GET | `/chain-dashboard/period-visitor-stats` | Đường dẫn đầy đủ `/api/chain-dashboard/period-visitor-stats` |
| GET | `/chain-dashboard/period-sold-stats` | Đường dẫn đầy đủ `/api/chain-dashboard/period-sold-stats` |
| GET | `/chain-dashboard/period-cancel-stats` | Đường dẫn đầy đủ `/api/chain-dashboard/period-cancel-stats` |
| GET | `/dashboard/top-products` | Đường dẫn đầy đủ `/api/dashboard/top-products` |
| GET | `/chain-dashboard/top-products` | Đường dẫn đầy đủ `/api/chain-dashboard/top-products` |
| GET | `/dashboard/orders-today` | Đường dẫn đầy đủ `/api/dashboard/orders-today` |
| GET | `/chain-dashboard/orders-today` | Đường dẫn đầy đủ `/api/chain-dashboard/orders-today` |
| GET | `/chain-dashboard/orders-yesterday` | Đường dẫn đầy đủ `/api/chain-dashboard/orders-yesterday` |
| GET | `/dashboard/low-stock` | Đường dẫn đầy đủ `/api/dashboard/low-stock` |
| GET | `/chain-dashboard/low-stock` | Đường dẫn đầy đủ `/api/chain-dashboard/low-stock` |

## Chi tiết từng endpoint

### `GET /dashboard` {#get-dashboard}

Đường dẫn đầy đủ `/api/dashboard`. Lớp kiểm tra: `requireAuth`.

**URL:** `GET /api/dashboard`

**Lớp route:** `requireAuth`

**Query:** `shopId`

**Response 200** — trường top-level (trích `res.json`):

`lowStockCount`, `todayCancelledOrders`, `todayCancelledRevenue`, `todayCardRevenue`, `todayCashRevenue`, `todayDiscountAmount`, `todayDiscountedOrders`, `todayOrders`, `todayPendingOrders`, `todayPendingRevenue`, `todayRevenue`, `todayTransferRevenue`, `todayVisitors`, `todayVisitorsPerBuyer`, `totalCancelledQuantity`, `totalOrders`, `totalPendingQuantity`, `totalProducts`, `totalRevenue`, `totalSoldQuantity`

### `GET /chain-dashboard` {#get-chain-dashboard}

Đường dẫn đầy đủ `/api/chain-dashboard`. Lớp kiểm tra: `requireAuth`.

**URL:** `GET /api/chain-dashboard`

**Lớp route:** `requireAuth`

**Query:** `shopId`

**Lỗi JSON** (`error` string):

| HTTP | Message |
|------|---------|
| **403** | `Không có quyền xem dữ liệu chi nhánh này` |

**Response 200** — trường top-level (trích `res.json`):

`lowStockCount`, `todayCancelledOrders`, `todayCancelledRevenue`, `todayDiscountAmount`, `todayDiscountedOrders`, `todayOrders`, `todayPendingOrders`, `todayPendingRevenue`, `totalCancelledQuantity`, `totalOrders`, `totalPendingQuantity`, `totalProducts`, `totalRevenue`, `totalSoldQuantity`, `yesterdayOrders`

### `GET /dashboard/revenue-chart` {#get-dashboard-revenue-chart}

Đường dẫn đầy đủ `/api/dashboard/revenue-chart`. Lớp kiểm tra: `requireAuth`.

**URL:** `GET /api/dashboard/revenue-chart`

**Lớp route:** `requireAuth`

**Query:** `from`, `granularity`, `period`, `shopId`, `to`

*Handler không trích được contract tự động — mở file route TypeScript.*

### `GET /dashboard/period-visitor-stats` {#get-dashboard-period-visitor-stats}

Đường dẫn đầy đủ `/api/dashboard/period-visitor-stats`. Lớp kiểm tra: `requireAuth`.

**URL:** `GET /api/dashboard/period-visitor-stats`

**Lớp route:** `requireAuth`

**Query:** `from`, `granularity`, `period`, `shopId`, `to`

**Response 200** — trường top-level (trích `res.json`):

`periodVisitors`

### `GET /dashboard/period-sold-stats` {#get-dashboard-period-sold-stats}

Đường dẫn đầy đủ `/api/dashboard/period-sold-stats`. Lớp kiểm tra: `requireAuth`.

**URL:** `GET /api/dashboard/period-sold-stats`

**Lớp route:** `requireAuth`

**Query:** `from`, `granularity`, `period`, `shopId`, `to`

**Response 200** — trường top-level (trích `res.json`):

`periodSoldQuantity`

### `GET /dashboard/period-cancel-stats` {#get-dashboard-period-cancel-stats}

Đường dẫn đầy đủ `/api/dashboard/period-cancel-stats`. Lớp kiểm tra: `requireAuth`.

**URL:** `GET /api/dashboard/period-cancel-stats`

**Lớp route:** `requireAuth`

**Query:** `from`, `granularity`, `period`, `shopId`, `to`

**Response 200** — trường top-level (trích `res.json`):

`directCancelledOrders`, `directCancelledRevenue`

### `GET /chain-dashboard/revenue-chart` {#get-chain-dashboard-revenue-chart}

Đường dẫn đầy đủ `/api/chain-dashboard/revenue-chart`. Lớp kiểm tra: `requireAuth`.

**URL:** `GET /api/chain-dashboard/revenue-chart`

**Lớp route:** `requireAuth`

**Query:** `from`, `granularity`, `period`, `shopId`, `to`

**Lỗi JSON** (`error` string):

| HTTP | Message |
|------|---------|
| **403** | `Không có quyền xem dữ liệu chi nhánh này` |

### `GET /chain-dashboard/period-visitor-stats` {#get-chain-dashboard-period-visitor-stats}

Đường dẫn đầy đủ `/api/chain-dashboard/period-visitor-stats`. Lớp kiểm tra: `requireAuth`.

**URL:** `GET /api/chain-dashboard/period-visitor-stats`

**Lớp route:** `requireAuth`

**Query:** `from`, `granularity`, `period`, `shopId`, `to`

**Lỗi JSON** (`error` string):

| HTTP | Message |
|------|---------|
| **403** | `Không có quyền xem dữ liệu chi nhánh này` |

**Response 200** — trường top-level (trích `res.json`):

`periodVisitors`

### `GET /chain-dashboard/period-sold-stats` {#get-chain-dashboard-period-sold-stats}

Đường dẫn đầy đủ `/api/chain-dashboard/period-sold-stats`. Lớp kiểm tra: `requireAuth`.

**URL:** `GET /api/chain-dashboard/period-sold-stats`

**Lớp route:** `requireAuth`

**Query:** `from`, `granularity`, `period`, `shopId`, `to`

**Lỗi JSON** (`error` string):

| HTTP | Message |
|------|---------|
| **403** | `Không có quyền xem dữ liệu chi nhánh này` |

**Response 200** — trường top-level (trích `res.json`):

`periodSoldQuantity`

### `GET /chain-dashboard/period-cancel-stats` {#get-chain-dashboard-period-cancel-stats}

Đường dẫn đầy đủ `/api/chain-dashboard/period-cancel-stats`. Lớp kiểm tra: `requireAuth`.

**URL:** `GET /api/chain-dashboard/period-cancel-stats`

**Lớp route:** `requireAuth`

**Query:** `from`, `granularity`, `period`, `shopId`, `to`

**Lỗi JSON** (`error` string):

| HTTP | Message |
|------|---------|
| **403** | `Không có quyền xem dữ liệu chi nhánh này` |

**Response 200** — trường top-level (trích `res.json`):

`directCancelledOrders`, `directCancelledRevenue`

### `GET /dashboard/top-products` {#get-dashboard-top-products}

Đường dẫn đầy đủ `/api/dashboard/top-products`. Lớp kiểm tra: `requireAuth`.

**URL:** `GET /api/dashboard/top-products`

**Lớp route:** `requireAuth`

**Query:** `catalog`, `categoryId`, `from`, `granularity`, `limit`, `page`, `period`, `q`, `shopId`, `sortBy`, `supplierId`, `to`

**Response 200** — trường top-level (trích `res.json`):

`items`, `payment`, `paymentOrders`, `summary`, `total`, `totalProfit`, `totalQuantity`, `totalRevenue`

### `GET /chain-dashboard/top-products` {#get-chain-dashboard-top-products}

Đường dẫn đầy đủ `/api/chain-dashboard/top-products`. Lớp kiểm tra: `requireAuth`.

**URL:** `GET /api/chain-dashboard/top-products`

**Lớp route:** `requireAuth`

**Query:** `from`, `granularity`, `limit`, `page`, `period`, `shopId`, `sortBy`, `to`

**Lỗi JSON** (`error` string):

| HTTP | Message |
|------|---------|
| **403** | `Không có quyền xem dữ liệu chi nhánh này` |

### `GET /dashboard/orders-today` {#get-dashboard-orders-today}

Đường dẫn đầy đủ `/api/dashboard/orders-today`. Lớp kiểm tra: `requireAuth`.

**URL:** `GET /api/dashboard/orders-today`

**Lớp route:** `requireAuth`

**Query:** `shopId`

*Handler không trích được contract tự động — mở file route TypeScript.*

### `GET /chain-dashboard/orders-today` {#get-chain-dashboard-orders-today}

Đường dẫn đầy đủ `/api/chain-dashboard/orders-today`. Lớp kiểm tra: `requireAuth`.

**URL:** `GET /api/chain-dashboard/orders-today`

**Lớp route:** `requireAuth`

**Query:** `shopId`

**Lỗi JSON** (`error` string):

| HTTP | Message |
|------|---------|
| **403** | `Không có quyền xem dữ liệu chi nhánh này` |

### `GET /chain-dashboard/orders-yesterday` {#get-chain-dashboard-orders-yesterday}

Đường dẫn đầy đủ `/api/chain-dashboard/orders-yesterday`. Lớp kiểm tra: `requireAuth`.

**URL:** `GET /api/chain-dashboard/orders-yesterday`

**Lớp route:** `requireAuth`

**Query:** `shopId`

**Lỗi JSON** (`error` string):

| HTTP | Message |
|------|---------|
| **403** | `Không có quyền xem dữ liệu chi nhánh này` |

### `GET /dashboard/low-stock` {#get-dashboard-low-stock}

Đường dẫn đầy đủ `/api/dashboard/low-stock`. Lớp kiểm tra: `requireAuth`.

**URL:** `GET /api/dashboard/low-stock`

**Lớp route:** `requireAuth`

**Query:** `shopId`, `threshold`

*Handler không trích được contract tự động — mở file route TypeScript.*

### `GET /chain-dashboard/low-stock` {#get-chain-dashboard-low-stock}

Đường dẫn đầy đủ `/api/chain-dashboard/low-stock`. Lớp kiểm tra: `requireAuth`.

**URL:** `GET /api/chain-dashboard/low-stock`

**Lớp route:** `requireAuth`

**Query:** `shopId`, `threshold`

**Lỗi JSON** (`error` string):

| HTTP | Message |
|------|---------|
| **403** | `Không có quyền xem dữ liệu chi nhánh này` |

## Ghi chú đọc mã

- Gắn prefix `/api` trong `app.ts`; file route: `routes/index.ts` → `./dashboard.ts`.
- Handler đầy đủ: mở file TypeScript tại Shop (tìm theo chuỗi path).
- Quyền role: `tham-chieu/phan-quyen-rbac/README.md` (tiếng Anh gốc) + các `require*` trong từng endpoint.

**Đọc tiếp:** [Hướng dẫn Map](../../huong-dan-doc/) · [Mục lục](../../README.md)
