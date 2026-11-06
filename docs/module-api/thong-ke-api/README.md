# Module API: `statistics`

**Mô tả:** Module API statistics.ts — 6 endpoint. Thống kê bán theo sản phẩm.

**Mã nguồn Shop:** `artifacts/api-server/src/routes/statistics.ts`

Thống kê bán theo sản phẩm.

**Số endpoint:** 6

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

- **Lớp kiểm tra (middleware):** `requireAuth`

### `GET /statistics/overview` {#get-statistics-overview}

Đường dẫn đầy đủ `/api/statistics/overview`. Lớp kiểm tra: `requireAuth`.

- **Lớp kiểm tra (middleware):** `requireAuth`

### `GET /statistics/trend` {#get-statistics-trend}

Đường dẫn đầy đủ `/api/statistics/trend`. Lớp kiểm tra: `requireAuth`.

- **Lớp kiểm tra (middleware):** `requireAuth`

### `GET /statistics/product-sales` {#get-statistics-product-sales}

Đường dẫn đầy đủ `/api/statistics/product-sales`. Lớp kiểm tra: `requireAuth`.

- **Lớp kiểm tra (middleware):** `requireAuth`

### `GET /statistics/top-products` {#get-statistics-top-products}

Đường dẫn đầy đủ `/api/statistics/top-products`. Lớp kiểm tra: `requireAuth`.

- **Lớp kiểm tra (middleware):** `requireAuth`

### `GET /statistics/catalog` {#get-statistics-catalog}

Đường dẫn đầy đủ `/api/statistics/catalog`. Lớp kiểm tra: `requireAuth`.

- **Lớp kiểm tra (middleware):** `requireAuth`

## Ghi chú đọc mã

- Gắn prefix `/api` trong `app.ts`; file route: `routes/index.ts` → `./statistics.ts`.
- Handler đầy đủ: mở file TypeScript tại Shop (tìm theo chuỗi path).
- Quyền role: `tham-chieu/phan-quyen-rbac/README.md` (tiếng Anh gốc) + các `require*` trong từng endpoint.

**Đọc tiếp:** [Hướng dẫn Map](../../huong-dan-doc/) · [Mục lục](../../README.md)
