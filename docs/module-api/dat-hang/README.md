# Module API: `purchase-orders`

**Mô tả:** Module API purchase-orders.ts — 9 endpoint. Phiếu đặt mua (PO).

**Mã nguồn Shop:** `artifacts/api-server/src/routes/purchase-orders.ts`

Phiếu đặt mua (PO).

**Số endpoint:** 9

**Contract API:** Mỗi endpoint có mục **URL**, body/query (từ code + schema Zod orval khi có), bảng lỗi `error`, và response (Zod hoặc trường `res.json`).

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

**URL:** `GET /api/purchase-orders/sales-hints`

**Lớp route:** `requireAuth`, `requireHubShop`, `requireOperationalContext`

**Query:** `days`

**Lỗi JSON** (`error` string):

| HTTP | Message |
|------|---------|
| **400** | `Tài khoản chưa gắn cửa hàng` |
| **403** | `Không có quyền xem gợi ý đặt hàng` |

**Response 200** — trường top-level (trích `res.json`):

`from`, `productId`, `products`, `soldQty`

### `GET /purchase-orders` {#get-purchase-orders}

Đường dẫn đầy đủ `/api/purchase-orders`. Lớp kiểm tra: `requireAuth, requireHubShop, requireOperationalContext`.

**URL:** `GET /api/purchase-orders`

**Lớp route:** `requireAuth`, `requireHubShop`, `requireOperationalContext`

**Query:** `status`

**Lỗi JSON** (`error` string):

| HTTP | Message |
|------|---------|
| **400** | `Tài khoản chưa gắn cửa hàng` |
| **400** | `Trạng thái không hợp lệ` |

### `GET /purchase-orders/:id` {#get-purchase-orders--id}

Đường dẫn đầy đủ `/api/purchase-orders/:id`. Lớp kiểm tra: `requireAuth, requireHubShop, requireOperationalContext`.

**URL:** `GET /api/purchase-orders/:id`

**Lớp route:** `requireAuth`, `requireHubShop`, `requireOperationalContext`

**Path params:** `id`

**Lỗi JSON** (`error` string):

| HTTP | Message |
|------|---------|
| **400** | `Tài khoản chưa gắn cửa hàng` |
| **400** | `ID không hợp lệ` |
| **404** | `Không tìm thấy phiếu đặt hàng` |

**Response 200** — trường top-level (trích `res.json`):

`address`, `contactPerson`, `email`, `id`, `itemCount`, `items`, `logs`, `name`, `phone`, `requesterEmail`, `requesterName`, `status`, `supplier`, `taxCode`, `totalQty`

### `POST /purchase-orders` {#post-purchase-orders}

Đường dẫn đầy đủ `/api/purchase-orders`. Lớp kiểm tra: `requireAuth, requireHubShop, requireOperationalContext`.

**URL:** `POST /api/purchase-orders`

**Lớp route:** `requireAuth`, `requireHubShop`, `requireOperationalContext`

**Lỗi JSON** (`error` string):

| HTTP | Message |
|------|---------|
| **403** | `Không có quyền tạo phiếu đặt hàng` |
| **400** | `Tài khoản chưa gắn cửa hàng` |
| **400** | `Nhà cung cấp không thuộc cửa hàng` |

**Response 201** — trường top-level (trích `res.json`):

`hàng`, `itemCount`, `items`, `requesterEmail`, `requesterName`, `totalQty`

### `PATCH /purchase-orders/:id` {#patch-purchase-orders--id}

Đường dẫn đầy đủ `/api/purchase-orders/:id`. Lớp kiểm tra: `requireAuth, requireHubShop, requireOperationalContext`.

**URL:** `PATCH /api/purchase-orders/:id`

**Lớp route:** `requireAuth`, `requireHubShop`, `requireOperationalContext`

**Path params:** `id`

**Lỗi JSON** (`error` string):

| HTTP | Message |
|------|---------|
| **403** | `Không có quyền cập nhật phiếu đặt hàng` |
| **400** | `Tài khoản chưa gắn cửa hàng` |
| **400** | `ID không hợp lệ` |
| **404** | `Không tìm thấy phiếu` |
| **400** | `Chỉ cập nhật được phiếu chưa nhận hàng` |

**Response 200** — trường top-level (trích `res.json`):

`itemCount`, `items`, `phiếu`, `requesterEmail`, `requesterName`, `supplierId`, `totalQty`

### `PATCH /purchase-orders/:id/send` {#patch-purchase-orders--id-send}

Đường dẫn đầy đủ `/api/purchase-orders/:id/send`. Lớp kiểm tra: `requireAuth, requireHubShop, requireOperationalContext`.

**URL:** `PATCH /api/purchase-orders/:id/send`

**Lớp route:** `requireAuth`, `requireHubShop`, `requireOperationalContext`

**Path params:** `id`

**Lỗi JSON** (`error` string):

| HTTP | Message |
|------|---------|
| **403** | `Không có quyền` |
| **400** | `Tài khoản chưa gắn cửa hàng` |
| **400** | `ID không hợp lệ` |
| **404** | `Không tìm thấy phiếu` |
| **400** | `Chỉ phiếu chờ gửi mới đánh dấu đã gửi` |

### `PATCH /purchase-orders/:id/receive` {#patch-purchase-orders--id-receive}

Đường dẫn đầy đủ `/api/purchase-orders/:id/receive`. Lớp kiểm tra: `requireAuth, requireHubShop, requireOperationalContext`.

**URL:** `PATCH /api/purchase-orders/:id/receive`

**Lớp route:** `requireAuth`, `requireHubShop`, `requireOperationalContext`

**Lỗi JSON** (`error` string):

| HTTP | Message |
|------|---------|
| **400** | `Nhận hàng và nhập kho thực hiện trên hoá đơn đầu vào (VAT inbound), không trên phiếu đặt hàng.` |

### `PATCH /purchase-orders/:id/close-short` {#patch-purchase-orders--id-close-short}

Đường dẫn đầy đủ `/api/purchase-orders/:id/close-short`. Lớp kiểm tra: `requireAuth, requireHubShop, requireOperationalContext`.

**URL:** `PATCH /api/purchase-orders/:id/close-short`

**Lớp route:** `requireAuth`, `requireHubShop`, `requireOperationalContext`

**Lỗi JSON** (`error` string):

| HTTP | Message |
|------|---------|
| **400** | `Đóng phần thiếu thực hiện trên hoá đơn đầu vào (VAT inbound), không trên phiếu đặt hàng.` |

### `PATCH /purchase-orders/:id/cancel` {#patch-purchase-orders--id-cancel}

Đường dẫn đầy đủ `/api/purchase-orders/:id/cancel`. Lớp kiểm tra: `requireAuth, requireHubShop, requireOperationalContext`.

**URL:** `PATCH /api/purchase-orders/:id/cancel`

**Lớp route:** `requireAuth`, `requireHubShop`, `requireOperationalContext`

**Path params:** `id`

**Lỗi JSON** (`error` string):

| HTTP | Message |
|------|---------|
| **403** | `Không có quyền` |
| **400** | `Tài khoản chưa gắn cửa hàng` |
| **400** | `ID không hợp lệ` |
| **404** | `Không tìm thấy phiếu` |
| **400** | `Không thể huỷ phiếu ở trạng thái hiện tại` |
| **400** | `Cần nhập lý do huỷ phiếu` |

## Ghi chú đọc mã

- Gắn prefix `/api` trong `app.ts`; file route: `routes/index.ts` → `./purchase-orders.ts`.
- Handler đầy đủ: mở file TypeScript tại Shop (tìm theo chuỗi path).
- Quyền role: `tham-chieu/phan-quyen-rbac/README.md` (tiếng Anh gốc) + các `require*` trong từng endpoint.

**Đọc tiếp:** [Hướng dẫn Map](../../huong-dan-doc/) · [Mục lục](../../README.md)
