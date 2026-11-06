# API module: `orders`

**Mô tả:** File routes orders.ts — 21 endpoint HTTP cho /api/.... Đơn hàng POS: tạo, hủy, duyệt hủy, in lại, thông báo reprint. Gắn ca (shift-sessions), audit cart. Frontend: pages/pos.…

**Source Shop:** `artifacts/api-server/src/routes/orders.ts`

Đơn hàng POS: tạo, hủy, duyệt hủy, in lại, thông báo reprint. Gắn ca (`shift-sessions`), audit cart.

**Frontend:** `pages/pos.tsx`, `pages/orders.tsx`, `lib/offline/checkout.ts` (offline).

**Số endpoint trong file:** 21

## Danh sách endpoint (tóm tắt)

| Method | Path | Mô tả ngắn |
|--------|------|------------|
| GET | `/orders` | `/api/orders` |
| GET | `/orders/period-summary` | `/api/orders/period-summary` |
| GET | `/orders/vat-queue-counts` | `/api/orders/vat-queue-counts` |
| POST | `/orders/preprint` | `/api/orders/preprint` |
| POST | `/orders` | `/api/orders` |
| GET | `/orders/:id` | `/api/orders/:id` |
| PATCH | `/orders/:id/cancel` | `/api/orders/:id/cancel` |
| PATCH | `/orders/:id/approve-cancel` | `/api/orders/:id/approve-cancel` |
| PATCH | `/orders/:id/reject-cancel` | `/api/orders/:id/reject-cancel` |
| PATCH | `/orders/:id/uncancel` | `/api/orders/:id/uncancel` |
| PATCH | `/orders/:id/invoice` | `/api/orders/:id/invoice` |
| PATCH | `/orders/:id/invoice/issue` | `/api/orders/:id/invoice/issue` |
| GET | `/orders/:id/invoice/pdf` | `/api/orders/:id/invoice/pdf` |
| GET | `/orders/:id/invoice-logs` | `/api/orders/:id/invoice-logs` |
| PATCH | `/orders/:id/payment` | `/api/orders/:id/payment` |
| PATCH | `/orders/:id/product-proof` | `/api/orders/:id/product-proof` |
| GET | `/orders/:id/audit-logs` | `/api/orders/:id/audit-logs` |
| GET | `/orders/:id/payment-logs` | `/api/orders/:id/payment-logs` |
| PATCH | `/orders/:id/note` | `/api/orders/:id/note` |
| POST | `/orders/:id/notify-oversight` | `/api/orders/:id/notify-oversight` |
| POST | `/orders/:id/notify-reprint` | `/api/orders/:id/notify-reprint` |

## Chi tiết từng endpoint

### `GET /orders` {#get-orders}

`/api/orders`. Middleware: `requireAuth, requireOperationalContext`.

- **Middleware:** `requireAuth`, `requireOperationalContext`

### `GET /orders/period-summary` {#get-orders-period-summary}

`/api/orders/period-summary`. Middleware: `requireAuth, requireOperationalContext`.

- **Middleware:** `requireAuth`, `requireOperationalContext`

### `GET /orders/vat-queue-counts` {#get-orders-vat-queue-counts}

`/api/orders/vat-queue-counts`. Middleware: `requireAuth, requireOperationalContext`.

- **Middleware:** `requireAuth`, `requireOperationalContext`

### `POST /orders/preprint` {#post-orders-preprint}

`/api/orders/preprint`. Middleware: `requireAuth, requireDeviceApproval, requireOperationalContext`.

- **Middleware:** `requireAuth`, `requireDeviceApproval`, `requireOperationalContext`

### `POST /orders` {#post-orders}

`/api/orders`. Middleware: `requireAuth, requireDeviceApproval, requireOperationalContext`.

- **Middleware:** `requireAuth`, `requireDeviceApproval`, `requireOperationalContext`

### `GET /orders/:id` {#get-orders--id}

`/api/orders/:id`. Middleware: `requireAuth, requireOperationalContext`.

- **Middleware:** `requireAuth`, `requireOperationalContext`

### `PATCH /orders/:id/cancel` {#patch-orders--id-cancel}

`/api/orders/:id/cancel`. Middleware: `requireAuth, requireOperationalContext`.

- **Middleware:** `requireAuth`, `requireOperationalContext`

### `PATCH /orders/:id/approve-cancel` {#patch-orders--id-approve-cancel}

`/api/orders/:id/approve-cancel`. Middleware: `requireAuth, requireOperationalContext`.

- **Middleware:** `requireAuth`, `requireOperationalContext`

### `PATCH /orders/:id/reject-cancel` {#patch-orders--id-reject-cancel}

`/api/orders/:id/reject-cancel`. Middleware: `requireAuth, requireOperationalContext`.

- **Middleware:** `requireAuth`, `requireOperationalContext`

### `PATCH /orders/:id/uncancel` {#patch-orders--id-uncancel}

`/api/orders/:id/uncancel`. Middleware: `requireAuth, requireOperationalContext`.

- **Middleware:** `requireAuth`, `requireOperationalContext`

### `PATCH /orders/:id/invoice` {#patch-orders--id-invoice}

`/api/orders/:id/invoice`. Middleware: `requireAuth, requireOperationalContext`.

- **Middleware:** `requireAuth`, `requireOperationalContext`

### `PATCH /orders/:id/invoice/issue` {#patch-orders--id-invoice-issue}

`/api/orders/:id/invoice/issue`. Middleware: `requireAuth, requireOperationalContext`.

- **Middleware:** `requireAuth`, `requireOperationalContext`

### `GET /orders/:id/invoice/pdf` {#get-orders--id-invoice-pdf}

`/api/orders/:id/invoice/pdf`. Middleware: `requireAuth, requireOperationalContext`.

- **Middleware:** `requireAuth`, `requireOperationalContext`

### `GET /orders/:id/invoice-logs` {#get-orders--id-invoice-logs}

`/api/orders/:id/invoice-logs`. Middleware: `requireAuth, requireOperationalContext`.

- **Middleware:** `requireAuth`, `requireOperationalContext`

### `PATCH /orders/:id/payment` {#patch-orders--id-payment}

`/api/orders/:id/payment`. Middleware: `requireAuth, requireOperationalContext`.

- **Middleware:** `requireAuth`, `requireOperationalContext`

### `PATCH /orders/:id/product-proof` {#patch-orders--id-product-proof}

`/api/orders/:id/product-proof`. Middleware: `requireAuth, requireOperationalContext`.

- **Middleware:** `requireAuth`, `requireOperationalContext`

### `GET /orders/:id/audit-logs` {#get-orders--id-audit-logs}

`/api/orders/:id/audit-logs`. Middleware: `requireAuth, requireOperationalContext`.

- **Middleware:** `requireAuth`, `requireOperationalContext`

### `GET /orders/:id/payment-logs` {#get-orders--id-payment-logs}

`/api/orders/:id/payment-logs`. Middleware: `requireAuth, requireOperationalContext`.

- **Middleware:** `requireAuth`, `requireOperationalContext`

### `PATCH /orders/:id/note` {#patch-orders--id-note}

`/api/orders/:id/note`. Middleware: `requireAuth, requireOperationalContext`.

- **Middleware:** `requireAuth`, `requireOperationalContext`

### `POST /orders/:id/notify-oversight` {#post-orders--id-notify-oversight}

`/api/orders/:id/notify-oversight`. Middleware: `requireAuth, requireOperationalContext`.

- **Middleware:** `requireAuth`, `requireOperationalContext`

### `POST /orders/:id/notify-reprint` {#post-orders--id-notify-reprint}

`/api/orders/:id/notify-reprint`. Middleware: `requireAuth, requireOperationalContext`.

- **Middleware:** `requireAuth`, `requireOperationalContext`

## Ghi chú đọc code

- Mount prefix `/api` qua `app.ts`; file này: `routes/index.ts` → `./orders.ts`.
- Handler đầy đủ: mở file TypeScript tại Shop (search theo path string).
- Quyền role: xem `reference/rbac.md` và middleware trong từng block.
