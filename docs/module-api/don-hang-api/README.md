# Module API: `orders`

**Mô tả:** Module API orders.ts — 21 endpoint. Đơn hàng POS: tạo, hủy, duyệt hủy, in lại, thông báo reprint. Gắn ca (shift-sessions), audit cart. Giao diện: pages/pos…

**Mã nguồn Shop:** `artifacts/api-server/src/routes/orders.ts`

Đơn hàng POS: tạo, hủy, duyệt hủy, in lại, thông báo reprint. Gắn ca (`shift-sessions`), audit cart.

**Giao diện:** `pages/pos.tsx`, `pages/orders.tsx`, `lib/offline/checkout.ts` (offline).

**Số endpoint:** 21

## Bảng endpoint (tóm tắt)

| Method | Path | Mô tả ngắn |
|--------|------|------------|
| GET | `/orders` | Đường dẫn đầy đủ `/api/orders` |
| GET | `/orders/period-summary` | Đường dẫn đầy đủ `/api/orders/period-summary` |
| GET | `/orders/vat-queue-counts` | Đường dẫn đầy đủ `/api/orders/vat-queue-counts` |
| POST | `/orders/preprint` | Đường dẫn đầy đủ `/api/orders/preprint` |
| POST | `/orders` | Đường dẫn đầy đủ `/api/orders` |
| GET | `/orders/:id` | Đường dẫn đầy đủ `/api/orders/:id` |
| PATCH | `/orders/:id/cancel` | Đường dẫn đầy đủ `/api/orders/:id/cancel` |
| PATCH | `/orders/:id/approve-cancel` | Đường dẫn đầy đủ `/api/orders/:id/approve-cancel` |
| PATCH | `/orders/:id/reject-cancel` | Đường dẫn đầy đủ `/api/orders/:id/reject-cancel` |
| PATCH | `/orders/:id/uncancel` | Đường dẫn đầy đủ `/api/orders/:id/uncancel` |
| PATCH | `/orders/:id/invoice` | Đường dẫn đầy đủ `/api/orders/:id/invoice` |
| PATCH | `/orders/:id/invoice/issue` | Đường dẫn đầy đủ `/api/orders/:id/invoice/issue` |
| GET | `/orders/:id/invoice/pdf` | Đường dẫn đầy đủ `/api/orders/:id/invoice/pdf` |
| GET | `/orders/:id/invoice-logs` | Đường dẫn đầy đủ `/api/orders/:id/invoice-logs` |
| PATCH | `/orders/:id/payment` | Đường dẫn đầy đủ `/api/orders/:id/payment` |
| PATCH | `/orders/:id/product-proof` | Đường dẫn đầy đủ `/api/orders/:id/product-proof` |
| GET | `/orders/:id/audit-logs` | Đường dẫn đầy đủ `/api/orders/:id/audit-logs` |
| GET | `/orders/:id/payment-logs` | Đường dẫn đầy đủ `/api/orders/:id/payment-logs` |
| PATCH | `/orders/:id/note` | Đường dẫn đầy đủ `/api/orders/:id/note` |
| POST | `/orders/:id/notify-oversight` | Đường dẫn đầy đủ `/api/orders/:id/notify-oversight` |
| POST | `/orders/:id/notify-reprint` | Đường dẫn đầy đủ `/api/orders/:id/notify-reprint` |

## Chi tiết từng endpoint

### `GET /orders` {#get-orders}

Đường dẫn đầy đủ `/api/orders`. Lớp kiểm tra: `requireAuth, requireOperationalContext`.

- **Lớp kiểm tra (middleware):** `requireAuth`, `requireOperationalContext`

### `GET /orders/period-summary` {#get-orders-period-summary}

Đường dẫn đầy đủ `/api/orders/period-summary`. Lớp kiểm tra: `requireAuth, requireOperationalContext`.

- **Lớp kiểm tra (middleware):** `requireAuth`, `requireOperationalContext`

### `GET /orders/vat-queue-counts` {#get-orders-vat-queue-counts}

Đường dẫn đầy đủ `/api/orders/vat-queue-counts`. Lớp kiểm tra: `requireAuth, requireOperationalContext`.

- **Lớp kiểm tra (middleware):** `requireAuth`, `requireOperationalContext`

### `POST /orders/preprint` {#post-orders-preprint}

Đường dẫn đầy đủ `/api/orders/preprint`. Lớp kiểm tra: `requireAuth, requireDeviceApproval, requireOperationalContext`.

- **Lớp kiểm tra (middleware):** `requireAuth`, `requireDeviceApproval`, `requireOperationalContext`

### `POST /orders` {#post-orders}

Đường dẫn đầy đủ `/api/orders`. Lớp kiểm tra: `requireAuth, requireDeviceApproval, requireOperationalContext`.

- **Lớp kiểm tra (middleware):** `requireAuth`, `requireDeviceApproval`, `requireOperationalContext`

### `GET /orders/:id` {#get-orders--id}

Đường dẫn đầy đủ `/api/orders/:id`. Lớp kiểm tra: `requireAuth, requireOperationalContext`.

- **Lớp kiểm tra (middleware):** `requireAuth`, `requireOperationalContext`

### `PATCH /orders/:id/cancel` {#patch-orders--id-cancel}

Đường dẫn đầy đủ `/api/orders/:id/cancel`. Lớp kiểm tra: `requireAuth, requireOperationalContext`.

- **Lớp kiểm tra (middleware):** `requireAuth`, `requireOperationalContext`

### `PATCH /orders/:id/approve-cancel` {#patch-orders--id-approve-cancel}

Đường dẫn đầy đủ `/api/orders/:id/approve-cancel`. Lớp kiểm tra: `requireAuth, requireOperationalContext`.

- **Lớp kiểm tra (middleware):** `requireAuth`, `requireOperationalContext`

### `PATCH /orders/:id/reject-cancel` {#patch-orders--id-reject-cancel}

Đường dẫn đầy đủ `/api/orders/:id/reject-cancel`. Lớp kiểm tra: `requireAuth, requireOperationalContext`.

- **Lớp kiểm tra (middleware):** `requireAuth`, `requireOperationalContext`

### `PATCH /orders/:id/uncancel` {#patch-orders--id-uncancel}

Đường dẫn đầy đủ `/api/orders/:id/uncancel`. Lớp kiểm tra: `requireAuth, requireOperationalContext`.

- **Lớp kiểm tra (middleware):** `requireAuth`, `requireOperationalContext`

### `PATCH /orders/:id/invoice` {#patch-orders--id-invoice}

Đường dẫn đầy đủ `/api/orders/:id/invoice`. Lớp kiểm tra: `requireAuth, requireOperationalContext`.

- **Lớp kiểm tra (middleware):** `requireAuth`, `requireOperationalContext`

### `PATCH /orders/:id/invoice/issue` {#patch-orders--id-invoice-issue}

Đường dẫn đầy đủ `/api/orders/:id/invoice/issue`. Lớp kiểm tra: `requireAuth, requireOperationalContext`.

- **Lớp kiểm tra (middleware):** `requireAuth`, `requireOperationalContext`

### `GET /orders/:id/invoice/pdf` {#get-orders--id-invoice-pdf}

Đường dẫn đầy đủ `/api/orders/:id/invoice/pdf`. Lớp kiểm tra: `requireAuth, requireOperationalContext`.

- **Lớp kiểm tra (middleware):** `requireAuth`, `requireOperationalContext`

### `GET /orders/:id/invoice-logs` {#get-orders--id-invoice-logs}

Đường dẫn đầy đủ `/api/orders/:id/invoice-logs`. Lớp kiểm tra: `requireAuth, requireOperationalContext`.

- **Lớp kiểm tra (middleware):** `requireAuth`, `requireOperationalContext`

### `PATCH /orders/:id/payment` {#patch-orders--id-payment}

Đường dẫn đầy đủ `/api/orders/:id/payment`. Lớp kiểm tra: `requireAuth, requireOperationalContext`.

- **Lớp kiểm tra (middleware):** `requireAuth`, `requireOperationalContext`

### `PATCH /orders/:id/product-proof` {#patch-orders--id-product-proof}

Đường dẫn đầy đủ `/api/orders/:id/product-proof`. Lớp kiểm tra: `requireAuth, requireOperationalContext`.

- **Lớp kiểm tra (middleware):** `requireAuth`, `requireOperationalContext`

### `GET /orders/:id/audit-logs` {#get-orders--id-audit-logs}

Đường dẫn đầy đủ `/api/orders/:id/audit-logs`. Lớp kiểm tra: `requireAuth, requireOperationalContext`.

- **Lớp kiểm tra (middleware):** `requireAuth`, `requireOperationalContext`

### `GET /orders/:id/payment-logs` {#get-orders--id-payment-logs}

Đường dẫn đầy đủ `/api/orders/:id/payment-logs`. Lớp kiểm tra: `requireAuth, requireOperationalContext`.

- **Lớp kiểm tra (middleware):** `requireAuth`, `requireOperationalContext`

### `PATCH /orders/:id/note` {#patch-orders--id-note}

Đường dẫn đầy đủ `/api/orders/:id/note`. Lớp kiểm tra: `requireAuth, requireOperationalContext`.

- **Lớp kiểm tra (middleware):** `requireAuth`, `requireOperationalContext`

### `POST /orders/:id/notify-oversight` {#post-orders--id-notify-oversight}

Đường dẫn đầy đủ `/api/orders/:id/notify-oversight`. Lớp kiểm tra: `requireAuth, requireOperationalContext`.

- **Lớp kiểm tra (middleware):** `requireAuth`, `requireOperationalContext`

### `POST /orders/:id/notify-reprint` {#post-orders--id-notify-reprint}

Đường dẫn đầy đủ `/api/orders/:id/notify-reprint`. Lớp kiểm tra: `requireAuth, requireOperationalContext`.

- **Lớp kiểm tra (middleware):** `requireAuth`, `requireOperationalContext`

## Ghi chú đọc mã

- Gắn prefix `/api` trong `app.ts`; file route: `routes/index.ts` → `./orders.ts`.
- Handler đầy đủ: mở file TypeScript tại Shop (tìm theo chuỗi path).
- Quyền role: `tham-chieu/phan-quyen-rbac/README.md` (tiếng Anh gốc) + các `require*` trong từng endpoint.

**Đọc tiếp:** [Hướng dẫn Map](../../huong-dan-doc/) · [Mục lục](../../README.md)
