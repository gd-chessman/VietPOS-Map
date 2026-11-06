# Module API: `purchase-orders`

**Mô tả:** Module API purchase-orders.ts — 9 endpoint. Phiếu đặt mua (PO).

**Mã nguồn Shop:** `artifacts/api-server/src/routes/purchase-orders.ts`

Phiếu đặt mua (PO).

**Số endpoint:** 9

## Bảng endpoint (tóm tắt)

| Method | Path | Mô tả ngắn |
|--------|------|------------|
| GET | `/purchase-orders/sales-hints` | Đường dẫn đầy đủ `/api/purchase-orders/sales-hints`… |
| GET | `/purchase-orders` | Đường dẫn đầy đủ `/api/purchase-orders` |
| GET | `/purchase-orders/:id` | Đường dẫn đầy đủ `/api/purchase-orders/:id` |
| POST | `/purchase-orders` | Đường dẫn đầy đủ `/api/purchase-orders` |
| PATCH | `/purchase-orders/:id` | Đường dẫn đầy đủ `/api/purchase-orders/:id` |
| PATCH | `/purchase-orders/:id/send` | Đường dẫn đầy đủ `/api/purchase-orders/:id/send`… |
| PATCH | `/purchase-orders/:id/receive` | Đường dẫn đầy đủ `/api/purchase-orders/:id/receive`… |
| PATCH | `/purchase-orders/:id/close-short` | Đường dẫn đầy đủ `/api/purchase-orders/:id/close-short`… |
| PATCH | `/purchase-orders/:id/cancel` | Đường dẫn đầy đủ `/api/purchase-orders/:id/cancel`… |

## Chi tiết từng endpoint

### `GET /purchase-orders/sales-hints` {#get-purchase-orders-sales-hints}

Đường dẫn đầy đủ `/api/purchase-orders/sales-hints`. Lớp kiểm tra: `requireAuth, requireHubShop, requireOperationalContext`.

- **Lớp kiểm tra (middleware):** `requireAuth`, `requireHubShop`, `requireOperationalContext`

### `GET /purchase-orders` {#get-purchase-orders}

Đường dẫn đầy đủ `/api/purchase-orders`. Lớp kiểm tra: `requireAuth, requireHubShop, requireOperationalContext`.

- **Lớp kiểm tra (middleware):** `requireAuth`, `requireHubShop`, `requireOperationalContext`

### `GET /purchase-orders/:id` {#get-purchase-orders--id}

Đường dẫn đầy đủ `/api/purchase-orders/:id`. Lớp kiểm tra: `requireAuth, requireHubShop, requireOperationalContext`.

- **Lớp kiểm tra (middleware):** `requireAuth`, `requireHubShop`, `requireOperationalContext`

### `POST /purchase-orders` {#post-purchase-orders}

Đường dẫn đầy đủ `/api/purchase-orders`. Lớp kiểm tra: `requireAuth, requireHubShop, requireOperationalContext`.

- **Lớp kiểm tra (middleware):** `requireAuth`, `requireHubShop`, `requireOperationalContext`

### `PATCH /purchase-orders/:id` {#patch-purchase-orders--id}

Đường dẫn đầy đủ `/api/purchase-orders/:id`. Lớp kiểm tra: `requireAuth, requireHubShop, requireOperationalContext`.

- **Lớp kiểm tra (middleware):** `requireAuth`, `requireHubShop`, `requireOperationalContext`

### `PATCH /purchase-orders/:id/send` {#patch-purchase-orders--id-send}

Đường dẫn đầy đủ `/api/purchase-orders/:id/send`. Lớp kiểm tra: `requireAuth, requireHubShop, requireOperationalContext`.

- **Lớp kiểm tra (middleware):** `requireAuth`, `requireHubShop`, `requireOperationalContext`

### `PATCH /purchase-orders/:id/receive` {#patch-purchase-orders--id-receive}

Đường dẫn đầy đủ `/api/purchase-orders/:id/receive`. Lớp kiểm tra: `requireAuth, requireHubShop, requireOperationalContext`.

- **Lớp kiểm tra (middleware):** `requireAuth`, `requireHubShop`, `requireOperationalContext`

### `PATCH /purchase-orders/:id/close-short` {#patch-purchase-orders--id-close-short}

Đường dẫn đầy đủ `/api/purchase-orders/:id/close-short`. Lớp kiểm tra: `requireAuth, requireHubShop, requireOperationalContext`.

- **Lớp kiểm tra (middleware):** `requireAuth`, `requireHubShop`, `requireOperationalContext`

### `PATCH /purchase-orders/:id/cancel` {#patch-purchase-orders--id-cancel}

Đường dẫn đầy đủ `/api/purchase-orders/:id/cancel`. Lớp kiểm tra: `requireAuth, requireHubShop, requireOperationalContext`.

- **Lớp kiểm tra (middleware):** `requireAuth`, `requireHubShop`, `requireOperationalContext`

## Ghi chú đọc mã

- Gắn prefix `/api` trong `app.ts`; file route: `routes/index.ts` → `./purchase-orders.ts`.
- Handler đầy đủ: mở file TypeScript tại Shop (tìm theo chuỗi path).
- Quyền role: `tham-chieu/phan-quyen-rbac/README.md` (tiếng Anh gốc) + các `require*` trong từng endpoint.

**Đọc tiếp:** [Hướng dẫn Map](../../huong-dan-doc/) · [Mục lục](../../README.md)
