# Module API: `orders`

**Mô tả:** Module API orders.ts — 21 endpoint. Đơn hàng POS: tạo, hủy, duyệt hủy, in lại, thông báo reprint. Gắn ca (shift-sessions)…

**Mã nguồn Shop:** `artifacts/api-server/src/routes/orders.ts`

Đơn hàng POS: tạo, hủy, duyệt hủy, in lại, thông báo reprint. Gắn ca (`shift-sessions`), audit cart.

**Giao diện:** `pages/pos.tsx`, `pages/orders.tsx`, `lib/offline/checkout.ts` (offline).

**Số endpoint:** 21

**Contract API:** Mỗi endpoint có mục **URL**, body/query (từ code + schema Zod orval khi có), bảng lỗi `error`, và response (Zod hoặc trường `res.json`).

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

**URL:** `GET /api/orders`

**Lớp route:** `requireAuth`, `requireOperationalContext`

**Lỗi JSON** (`error` string):

| HTTP | Message |
|------|---------|
| **403** | `Không có quyền xem đơn hàng chi nhánh này` |

### `GET /orders/period-summary` {#get-orders-period-summary}

Đường dẫn đầy đủ `/api/orders/period-summary`. Lớp kiểm tra: `requireAuth, requireOperationalContext`.

**URL:** `GET /api/orders/period-summary`

**Lớp route:** `requireAuth`, `requireOperationalContext`

**Lỗi JSON** (`error` string):

| HTTP | Message |
|------|---------|
| **403** | `Không có quyền xem đơn hàng chi nhánh này` |

### `GET /orders/vat-queue-counts` {#get-orders-vat-queue-counts}

Đường dẫn đầy đủ `/api/orders/vat-queue-counts`. Lớp kiểm tra: `requireAuth, requireOperationalContext`.

**URL:** `GET /api/orders/vat-queue-counts`

**Lớp route:** `requireAuth`, `requireOperationalContext`

**Lỗi JSON** (`error` string):

| HTTP | Message |
|------|---------|
| **403** | `Không có quyền xem hàng đợi xuất VAT` |
| **403** | `Không có quyền xem đơn hàng chi nhánh này` |

**Response 200** — trường top-level (trích `res.json`):

`total`

### `POST /orders/preprint` {#post-orders-preprint}

Đường dẫn đầy đủ `/api/orders/preprint`. Lớp kiểm tra: `requireAuth, requireDeviceApproval, requireOperationalContext`.

**URL:** `POST /api/orders/preprint`

**Lớp route:** `requireAuth`, `requireDeviceApproval`, `requireOperationalContext`

**Request body** — schema `OrderPreprintBody` (`@workspace/api-zod`):

*(schema `OrderPreprintBody` — xem `lib/api-zod/src/generated/api.ts`)*

**Lỗi JSON** (`error` string):

| HTTP | Message |
|------|---------|
| **403** | `Vai trò này không được tạo đơn bán hàng` |
| **500** | `Không tạo được preprint` |

### `POST /orders` {#post-orders}

Đường dẫn đầy đủ `/api/orders`. Lớp kiểm tra: `requireAuth, requireDeviceApproval, requireOperationalContext`.

**URL:** `POST /api/orders`

**Lớp route:** `requireAuth`, `requireDeviceApproval`, `requireOperationalContext`

**Request body** — schema `CreateOrderBody` (`@workspace/api-zod`):

| Trường | Kiểu (Zod) | Bắt buộc |
|--------|------------|----------|
| `shopId` | `number()` | không |
| `paymentMethod` | `string()` | không |
| `note` | `string()` | không |
| `invoiceRequested` | `boolean()` | không |
| `buyerCompanyName` | `string()` | không |
| `buyerTaxCode` | `string()` | không |
| `buyerEmail` | `string()` | không |
| `buyerAddress` | `string()` | không |
| `buyerPhone` | `string()` | không |
| `paymentProofUrls` | `array(zod.string()` | không |
| `productProofUrls` | `array(zod.string()` | không |
| `deferOversightNotification` | `boolean()` | không |
| `items` | `array(
    zod.object({
      productId: zod.number()` | **có** |

**Lỗi JSON** (`error` string):

| HTTP | Message |
|------|---------|
| **403** | `Vai trò này không được tạo đơn bán hàng` |
| **400** | `Order must have at least one item` |
| **400** | `Thiếu ảnh chứng từ thanh toán` |
| **400** | `Không đủ tồn kho cho một hoặc nhiều sản phẩm` |
| **409** | `STT đơn đã được dùng — cần xử lý xung đột đồng bộ` |

**Response 201** — trường top-level (trích `res.json`):

`invoiceCodeAdjusted`

### `GET /orders/:id` {#get-orders--id}

Đường dẫn đầy đủ `/api/orders/:id`. Lớp kiểm tra: `requireAuth, requireOperationalContext`.

**URL:** `GET /api/orders/:id`

**Lớp route:** `requireAuth`, `requireOperationalContext`

**Lỗi JSON** (`error` string):

| HTTP | Message |
|------|---------|
| **400** | `Invalid order ID` |
| **404** | `Order not found` |
| **403** | `Không có quyền xem đơn hàng này` |

**Response 200** — trường top-level (trích `res.json`):

`cancelledWithoutRequest`

### `PATCH /orders/:id/cancel` {#patch-orders--id-cancel}

Đường dẫn đầy đủ `/api/orders/:id/cancel`. Lớp kiểm tra: `requireAuth, requireOperationalContext`.

**URL:** `PATCH /api/orders/:id/cancel`

**Lớp route:** `requireAuth`, `requireOperationalContext`
- **Thêm trong handler:** role **`super_admin`** (403 nếu không đủ).

**Request body** (`application/json`, trích từ code):

| Trường | Ghi chú |
|--------|---------|
| `cancelNote` | xem handler |

**Lỗi JSON** (`error` string):

| HTTP | Message |
|------|---------|
| **400** | `Invalid ID` |
| **403** | `Không có quyền huỷ đơn` |
| **404** | `Order not found` |
| **400** | `Đơn hàng đã bị huỷ` |
| **400** | `Chỉ được huỷ hoặc đề nghị huỷ đơn đã hoàn thành` |

### `PATCH /orders/:id/approve-cancel` {#patch-orders--id-approve-cancel}

Đường dẫn đầy đủ `/api/orders/:id/approve-cancel`. Lớp kiểm tra: `requireAuth, requireOperationalContext`.

**URL:** `PATCH /api/orders/:id/approve-cancel`

**Lớp route:** `requireAuth`, `requireOperationalContext`

**Lỗi JSON** (`error` string):

| HTTP | Message |
|------|---------|
| **400** | `Invalid ID` |
| **403** | `Chỉ quản trị hoặc quản lý mới có thể duyệt huỷ đơn` |
| **400** | `Đơn không ở trạng thái đề nghị huỷ` |

### `PATCH /orders/:id/reject-cancel` {#patch-orders--id-reject-cancel}

Đường dẫn đầy đủ `/api/orders/:id/reject-cancel`. Lớp kiểm tra: `requireAuth, requireOperationalContext`.

**URL:** `PATCH /api/orders/:id/reject-cancel`

**Lớp route:** `requireAuth`, `requireOperationalContext`

**Lỗi JSON** (`error` string):

| HTTP | Message |
|------|---------|
| **400** | `Invalid ID` |
| **403** | `Chỉ quản trị hoặc quản lý mới có thể từ chối huỷ đơn` |
| **400** | `Đơn không ở trạng thái đề nghị huỷ` |

### `PATCH /orders/:id/uncancel` {#patch-orders--id-uncancel}

Đường dẫn đầy đủ `/api/orders/:id/uncancel`. Lớp kiểm tra: `requireAuth, requireOperationalContext`.

**URL:** `PATCH /api/orders/:id/uncancel`

**Lớp route:** `requireAuth`, `requireOperationalContext`

**Lỗi JSON** (`error` string):

| HTTP | Message |
|------|---------|
| **400** | `Invalid ID` |
| **403** | `Chỉ quản trị hoặc quản lý mới có thể khôi phục đơn` |
| **400** | `Đơn hàng đã ở trạng thái hoàn thành` |

### `PATCH /orders/:id/invoice` {#patch-orders--id-invoice}

Đường dẫn đầy đủ `/api/orders/:id/invoice`. Lớp kiểm tra: `requireAuth, requireOperationalContext`.

**URL:** `PATCH /api/orders/:id/invoice`

**Lớp route:** `requireAuth`, `requireOperationalContext`

**Lỗi JSON** (`error` string):

| HTTP | Message |
|------|---------|
| **400** | `Invalid ID` |
| **404** | `Order not found` |
| **403** | `Không có quyền sửa đơn hàng chi nhánh này` |
| **403** | `Chỉ admin hoặc nhân viên tạo đơn mới có thể sửa thông tin hoá đơn` |
| **400** | `Chỉ sửa được hoá đơn của đơn đã hoàn thành` |

**Response 200** — trường top-level (trích `res.json`):

`message`

### `PATCH /orders/:id/invoice/issue` {#patch-orders--id-invoice-issue}

Đường dẫn đầy đủ `/api/orders/:id/invoice/issue`. Lớp kiểm tra: `requireAuth, requireOperationalContext`.

**URL:** `PATCH /api/orders/:id/invoice/issue`

**Lớp route:** `requireAuth`, `requireOperationalContext`

**Lỗi JSON** (`error` string):

| HTTP | Message |
|------|---------|
| **400** | `Invalid ID` |
| **403** | `Chỉ admin tổng, admin/kế toán chi nhánh chính mới có thể đánh dấu đã xuất VAT` |
| **404** | `Order not found` |
| **403** | `Không có quyền thao tác đơn hàng chi nhánh này` |
| **400** | `Chỉ đánh dấu được đơn đã hoàn thành` |
| **400** | `Đơn không có yêu cầu xuất hoá đơn VAT` |
| **400** | `Đơn đã được đánh dấu xuất hoá đơn` |

### `GET /orders/:id/invoice/pdf` {#get-orders--id-invoice-pdf}

Đường dẫn đầy đủ `/api/orders/:id/invoice/pdf`. Lớp kiểm tra: `requireAuth, requireOperationalContext`.

**URL:** `GET /api/orders/:id/invoice/pdf`

**Lớp route:** `requireAuth`, `requireOperationalContext`

**Lỗi JSON** (`error` string):

| HTTP | Message |
|------|---------|
| **400** | `Invalid ID` |
| **403** | `Không có quyền xem hóa đơn VAT` |
| **404** | `Order not found` |
| **403** | `Không có quyền xem đơn hàng này` |
| **400** | `Đơn chưa xuất hóa đơn điện tử` |

### `GET /orders/:id/invoice-logs` {#get-orders--id-invoice-logs}

Đường dẫn đầy đủ `/api/orders/:id/invoice-logs`. Lớp kiểm tra: `requireAuth, requireOperationalContext`.

**URL:** `GET /api/orders/:id/invoice-logs`

**Lớp route:** `requireAuth`, `requireOperationalContext`

**Lỗi JSON** (`error` string):

| HTTP | Message |
|------|---------|
| **400** | `Invalid ID` |
| **403** | `Không có quyền xem lịch sử hoá đơn` |
| **404** | `Order not found` |
| **403** | `Không có quyền xem lịch sử đơn hàng này` |

### `PATCH /orders/:id/payment` {#patch-orders--id-payment}

Đường dẫn đầy đủ `/api/orders/:id/payment`. Lớp kiểm tra: `requireAuth, requireOperationalContext`.

**URL:** `PATCH /api/orders/:id/payment`

**Lớp route:** `requireAuth`, `requireOperationalContext`
- **Thêm trong handler:** role **`super_admin`** (403 nếu không đủ).

**Lỗi JSON** (`error` string):

| HTTP | Message |
|------|---------|
| **400** | `Invalid ID` |
| **404** | `Order not found` |
| **403** | `Không có quyền sửa đơn hàng chi nhánh này` |
| **400** | `Chỉ đổi được phương thức thanh toán của đơn đã hoàn thành` |
| **403** | `Không có quyền đổi phương thức thanh toán` |
| **400** | `Thiếu ảnh chứng từ thanh toán` |
| **400** | `Phương thức thanh toán mới trùng với hiện tại` |
| **403** | `Chỉ đổi được trong ngày tạo đơn; liên hệ quản lý` |
| **403** | `Chỉnh sửa đơn hàng đã bị tắt cho chi nhánh này` |
| **409** | `Đơn hàng đã được cập nhật bởi thiết bị khác, vui lòng tải lại` |
| **500** | `Cập nhật thất bại` |

**Response 200** — trường top-level (trích `res.json`):

`currentVersion`, `message`

### `PATCH /orders/:id/product-proof` {#patch-orders--id-product-proof}

Đường dẫn đầy đủ `/api/orders/:id/product-proof`. Lớp kiểm tra: `requireAuth, requireOperationalContext`.

**URL:** `PATCH /api/orders/:id/product-proof`

**Lớp route:** `requireAuth`, `requireOperationalContext`
- **Thêm trong handler:** role **`super_admin`** (403 nếu không đủ).

**Lỗi JSON** (`error` string):

| HTTP | Message |
|------|---------|
| **400** | `Invalid ID` |
| **400** | `Thiếu ảnh chứng từ sản phẩm` |
| **404** | `Order not found` |
| **403** | `Không có quyền sửa đơn hàng chi nhánh này` |
| **400** | `Chỉ cập nhật chứng từ sản phẩm của đơn đã hoàn thành` |
| **400** | `Cửa hàng đã tắt chứng từ sản phẩm` |
| **403** | `Không có quyền cập nhật chứng từ sản phẩm` |
| **403** | `Chỉ cập nhật được trong ngày tạo đơn; liên hệ quản lý` |
| **403** | `Chỉnh sửa đơn hàng đã bị tắt cho chi nhánh này` |
| **409** | `Đơn hàng đã được cập nhật bởi thiết bị khác, vui lòng tải lại` |
| **500** | `Cập nhật thất bại` |

**Response 200** — trường top-level (trích `res.json`):

`currentVersion`, `message`

### `GET /orders/:id/audit-logs` {#get-orders--id-audit-logs}

Đường dẫn đầy đủ `/api/orders/:id/audit-logs`. Lớp kiểm tra: `requireAuth, requireOperationalContext`.

**URL:** `GET /api/orders/:id/audit-logs`

**Lớp route:** `requireAuth`, `requireOperationalContext`

**Lỗi JSON** (`error` string):

| HTTP | Message |
|------|---------|
| **400** | `Invalid ID` |
| **404** | `Order not found` |
| **403** | `Không có quyền xem lịch sử đơn hàng này` |

### `GET /orders/:id/payment-logs` {#get-orders--id-payment-logs}

Đường dẫn đầy đủ `/api/orders/:id/payment-logs`. Lớp kiểm tra: `requireAuth, requireOperationalContext`.

**URL:** `GET /api/orders/:id/payment-logs`

**Lớp route:** `requireAuth`, `requireOperationalContext`

**Lỗi JSON** (`error` string):

| HTTP | Message |
|------|---------|
| **400** | `Invalid ID` |
| **404** | `Order not found` |
| **403** | `Không có quyền xem lịch sử đơn hàng này` |

### `PATCH /orders/:id/note` {#patch-orders--id-note}

Đường dẫn đầy đủ `/api/orders/:id/note`. Lớp kiểm tra: `requireAuth, requireOperationalContext`.

**URL:** `PATCH /api/orders/:id/note`

**Lớp route:** `requireAuth`, `requireOperationalContext`

**Lỗi JSON** (`error` string):

| HTTP | Message |
|------|---------|
| **400** | `Invalid ID` |
| **404** | `Order not found` |
| **403** | `Không có quyền sửa đơn hàng chi nhánh này` |
| **409** | `Đơn hàng đã được cập nhật bởi thiết bị khác, vui lòng tải lại` |
| **500** | `Cập nhật thất bại` |

**Response 200** — trường top-level (trích `res.json`):

`currentVersion`

### `POST /orders/:id/notify-oversight` {#post-orders--id-notify-oversight}

Đường dẫn đầy đủ `/api/orders/:id/notify-oversight`. Lớp kiểm tra: `requireAuth, requireOperationalContext`.

**URL:** `POST /api/orders/:id/notify-oversight`

**Lớp route:** `requireAuth`, `requireOperationalContext`
- **Thêm trong handler:** role **`super_admin`** (403 nếu không đủ).

**Lỗi JSON** (`error` string):

| HTTP | Message |
|------|---------|
| **400** | `Invalid ID` |
| **404** | `Order not found` |
| **403** | `Không có quyền` |
| **400** | `Chỉ thông báo đơn đã hoàn thành` |
| **400** | `Quá thời gian chốt đơn trên receipt` |

**Response 200** — trường top-level (trích `res.json`):

`ok`

### `POST /orders/:id/notify-reprint` {#post-orders--id-notify-reprint}

Đường dẫn đầy đủ `/api/orders/:id/notify-reprint`. Lớp kiểm tra: `requireAuth, requireOperationalContext`.

**URL:** `POST /api/orders/:id/notify-reprint`

**Lớp route:** `requireAuth`, `requireOperationalContext`

**Lỗi JSON** (`error` string):

| HTTP | Message |
|------|---------|
| **403** | `Kế toán không được in lại hoá đơn` |
| **400** | `Invalid ID` |
| **404** | `Order not found` |

**Response 200** — trường top-level (trích `res.json`):

`ok`

## Ghi chú đọc mã

- Gắn prefix `/api` trong `app.ts`; file route: `routes/index.ts` → `./orders.ts`.
- Handler đầy đủ: mở file TypeScript tại Shop (tìm theo chuỗi path).
- Quyền role: `tham-chieu/phan-quyen-rbac/README.md` (tiếng Anh gốc) + các `require*` trong từng endpoint.

**Đọc tiếp:** [Hướng dẫn Map](../../huong-dan-doc/) · [Mục lục](../../README.md)
