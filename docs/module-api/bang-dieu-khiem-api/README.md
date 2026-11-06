# Module API: `dashboard`

**Mô tả:** Module API dashboard.ts — 17 endpoint. Số liệu tổng quan: doanh thu, đơn, tồn thấp.

**Mã nguồn Shop:** `artifacts/api-server/src/routes/dashboard.ts`

Số liệu tổng quan: doanh thu, đơn, tồn thấp.

**Số endpoint:** 17

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

- **Lớp kiểm tra (middleware):** `requireAuth`

### `GET /chain-dashboard` {#get-chain-dashboard}

Đường dẫn đầy đủ `/api/chain-dashboard`. Lớp kiểm tra: `requireAuth`.

- **Lớp kiểm tra (middleware):** `requireAuth`

### `GET /dashboard/revenue-chart` {#get-dashboard-revenue-chart}

Đường dẫn đầy đủ `/api/dashboard/revenue-chart`. Lớp kiểm tra: `requireAuth`.

- **Lớp kiểm tra (middleware):** `requireAuth`

### `GET /dashboard/period-visitor-stats` {#get-dashboard-period-visitor-stats}

Đường dẫn đầy đủ `/api/dashboard/period-visitor-stats`. Lớp kiểm tra: `requireAuth`.

- **Lớp kiểm tra (middleware):** `requireAuth`

### `GET /dashboard/period-sold-stats` {#get-dashboard-period-sold-stats}

Đường dẫn đầy đủ `/api/dashboard/period-sold-stats`. Lớp kiểm tra: `requireAuth`.

- **Lớp kiểm tra (middleware):** `requireAuth`

### `GET /dashboard/period-cancel-stats` {#get-dashboard-period-cancel-stats}

Đường dẫn đầy đủ `/api/dashboard/period-cancel-stats`. Lớp kiểm tra: `requireAuth`.

- **Lớp kiểm tra (middleware):** `requireAuth`

### `GET /chain-dashboard/revenue-chart` {#get-chain-dashboard-revenue-chart}

Đường dẫn đầy đủ `/api/chain-dashboard/revenue-chart`. Lớp kiểm tra: `requireAuth`.

- **Lớp kiểm tra (middleware):** `requireAuth`

### `GET /chain-dashboard/period-visitor-stats` {#get-chain-dashboard-period-visitor-stats}

Đường dẫn đầy đủ `/api/chain-dashboard/period-visitor-stats`. Lớp kiểm tra: `requireAuth`.

- **Lớp kiểm tra (middleware):** `requireAuth`

### `GET /chain-dashboard/period-sold-stats` {#get-chain-dashboard-period-sold-stats}

Đường dẫn đầy đủ `/api/chain-dashboard/period-sold-stats`. Lớp kiểm tra: `requireAuth`.

- **Lớp kiểm tra (middleware):** `requireAuth`

### `GET /chain-dashboard/period-cancel-stats` {#get-chain-dashboard-period-cancel-stats}

Đường dẫn đầy đủ `/api/chain-dashboard/period-cancel-stats`. Lớp kiểm tra: `requireAuth`.

- **Lớp kiểm tra (middleware):** `requireAuth`

### `GET /dashboard/top-products` {#get-dashboard-top-products}

Đường dẫn đầy đủ `/api/dashboard/top-products`. Lớp kiểm tra: `requireAuth`.

- **Lớp kiểm tra (middleware):** `requireAuth`

### `GET /chain-dashboard/top-products` {#get-chain-dashboard-top-products}

Đường dẫn đầy đủ `/api/chain-dashboard/top-products`. Lớp kiểm tra: `requireAuth`.

- **Lớp kiểm tra (middleware):** `requireAuth`

### `GET /dashboard/orders-today` {#get-dashboard-orders-today}

Đường dẫn đầy đủ `/api/dashboard/orders-today`. Lớp kiểm tra: `requireAuth`.

- **Lớp kiểm tra (middleware):** `requireAuth`

### `GET /chain-dashboard/orders-today` {#get-chain-dashboard-orders-today}

Đường dẫn đầy đủ `/api/chain-dashboard/orders-today`. Lớp kiểm tra: `requireAuth`.

- **Lớp kiểm tra (middleware):** `requireAuth`

### `GET /chain-dashboard/orders-yesterday` {#get-chain-dashboard-orders-yesterday}

Đường dẫn đầy đủ `/api/chain-dashboard/orders-yesterday`. Lớp kiểm tra: `requireAuth`.

- **Lớp kiểm tra (middleware):** `requireAuth`

### `GET /dashboard/low-stock` {#get-dashboard-low-stock}

Đường dẫn đầy đủ `/api/dashboard/low-stock`. Lớp kiểm tra: `requireAuth`.

- **Lớp kiểm tra (middleware):** `requireAuth`

### `GET /chain-dashboard/low-stock` {#get-chain-dashboard-low-stock}

Đường dẫn đầy đủ `/api/chain-dashboard/low-stock`. Lớp kiểm tra: `requireAuth`.

- **Lớp kiểm tra (middleware):** `requireAuth`

## Ghi chú đọc mã

- Gắn prefix `/api` trong `app.ts`; file route: `routes/index.ts` → `./dashboard.ts`.
- Handler đầy đủ: mở file TypeScript tại Shop (tìm theo chuỗi path).
- Quyền role: `tham-chieu/phan-quyen-rbac/README.md` (tiếng Anh gốc) + các `require*` trong từng endpoint.

**Đọc tiếp:** [Hướng dẫn Map](../../huong-dan-doc/) · [Mục lục](../../README.md)
