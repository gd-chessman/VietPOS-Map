# Module API: `chain`

**Mô tả:** Module API chain.ts — 29 endpoint. Tổ chức, shop, kho, điều chuyển (transfers). Cấu hình org (Viettel, CQT, feedback URL, agent LLM). Giao diện: pages/cha…

**Mã nguồn Shop:** `artifacts/api-server/src/routes/chain.ts`

Tổ chức, shop, kho, điều chuyển (`transfers`). Cấu hình org (Viettel, CQT, feedback URL, agent LLM).

**Giao diện:** `pages/chain.tsx`, `chain-dashboard.tsx`.

**Số endpoint:** 29

**Contract API:** Mỗi endpoint có mục **URL**, body/query (từ code + schema Zod orval khi có), bảng lỗi `error`, và response (Zod hoặc trường `res.json`).

## Bảng endpoint (tóm tắt)

| Method | Path | Mô tả ngắn |
|--------|------|------------|
| GET | `/organizations` | Đường dẫn đầy đủ `/api/organizations` |
| GET | `/organizations/current` | Đường dẫn đầy đủ `/api/organizations/current` |
| PUT | `/organizations/:orgId/shop-display-order` | Đường dẫn đầy đủ `/api/organizations/:orgId/shop-display-order` |
| POST | `/organizations` | Đường dẫn đầy đủ `/api/organizations` |
| PATCH | `/organizations/:id` | Đường dẫn đầy đủ `/api/organizations/:id` |
| PATCH | `/shops/:id` | Đường dẫn đầy đủ `/api/shops/:id` |
| POST | `/shops/:id/devices/register` | Đường dẫn đầy đủ `/api/shops/:id/devices/register` |
| GET | `/shops/:id/devices` | Đường dẫn đầy đủ `/api/shops/:id/devices` |
| PATCH | `/shops/:id/devices/:deviceRowId` | Đường dẫn đầy đủ `/api/shops/:id/devices/:deviceRowId` |
| GET | `/shops/:id/devices/:deviceRowId/login-events` | Đường dẫn đầy đủ `/api/shops/:id/devices/:deviceRowId/login-events` |
| POST | `/shops/:id/create-admin` | Đường dẫn đầy đủ `/api/shops/:id/create-admin` |
| PATCH | `/shops/:id/admin-email` | Đường dẫn đầy đủ `/api/shops/:id/admin-email` |
| PATCH | `/shops/:id/reset-password` | Đường dẫn đầy đủ `/api/shops/:id/reset-password` |
| POST | `/shops` | Đường dẫn đầy đủ `/api/shops` |
| GET | `/warehouses` | Đường dẫn đầy đủ `/api/warehouses` |
| POST | `/warehouses` | Đường dẫn đầy đủ `/api/warehouses` |
| PATCH | `/warehouses/:id` | Đường dẫn đầy đủ `/api/warehouses/:id` |
| GET | `/warehouses/:id/products` | Đường dẫn đầy đủ `/api/warehouses/:id/products` |
| GET | `/warehouses/:id/inventory` | Đường dẫn đầy đủ `/api/warehouses/:id/inventory` |
| POST | `/warehouses/:id/adjust-stock` | Đường dẫn đầy đủ `/api/warehouses/:id/adjust-stock` |
| GET | `/transfers` | Đường dẫn đầy đủ `/api/transfers` |
| GET | `/transfers/:id/items` | Đường dẫn đầy đủ `/api/transfers/:id/items` |
| POST | `/transfers` | Đường dẫn đầy đủ `/api/transfers` |
| POST | `/transfers/:id/approve` | Đường dẫn đầy đủ `/api/transfers/:id/approve` |
| POST | `/transfers/:id/ship` | Đường dẫn đầy đủ `/api/transfers/:id/ship` |
| POST | `/transfers/:id/receive` | Đường dẫn đầy đủ `/api/transfers/:id/receive` |
| DELETE | `/transfers/:id` | Đường dẫn đầy đủ `/api/transfers/:id` |
| PATCH | `/transfers/:id` | Đường dẫn đầy đủ `/api/transfers/:id` |
| GET | `/warehouses/:id/movements` | Đường dẫn đầy đủ `/api/warehouses/:id/movements` |

## Chi tiết từng endpoint

### `GET /organizations` {#get-organizations}

Đường dẫn đầy đủ `/api/organizations`. Lớp kiểm tra: `requireAuth, requireChainManagement`.

**URL:** `GET /api/organizations`

**Lớp route:** `requireAuth`, `requireChainManagement`

**Lỗi JSON** (`error` string):

| HTTP | Message |
|------|---------|
| **403** | `Forbidden` |

### `GET /organizations/current` {#get-organizations-current}

Đường dẫn đầy đủ `/api/organizations/current`. Lớp kiểm tra: `requireAuth`.

**URL:** `GET /api/organizations/current`

**Lớp route:** `requireAuth`

**Lỗi JSON** (`error` string):

| HTTP | Message |
|------|---------|
| **404** | `Tài khoản chưa gắn tổ chức` |
| **404** | `Không tìm thấy tổ chức` |

### `PUT /organizations/:orgId/shop-display-order` {#put-organizations--orgId-shop-display-order}

Đường dẫn đầy đủ `/api/organizations/:orgId/shop-display-order`. Lớp kiểm tra: `requireAuth, requireChainManagement`.

**URL:** `PUT /api/organizations/:orgId/shop-display-order`

**Lớp route:** `requireAuth`, `requireChainManagement`
- **Thêm trong handler:** role **`super_admin`** (403 nếu không đủ).

**Lỗi JSON** (`error` string):

| HTTP | Message |
|------|---------|
| **400** | `Invalid organization ID` |
| **403** | `Chỉ được sắp xếp chi nhánh trong tổ chức của bạn` |
| **400** | `shopIds phải là mảng id chi nhánh` |
| **400** | `Danh sách phải gồm đúng mọi chi nhánh của tổ chức, mỗi id một lần` |

**Response 200** — trường top-level (trích `res.json`):

`ok`

### `POST /organizations` {#post-organizations}

Đường dẫn đầy đủ `/api/organizations`. Lớp kiểm tra: `requireAuth, requireChainManagement`.

**URL:** `POST /api/organizations`

**Lớp route:** `requireAuth`, `requireChainManagement`

**Lỗi JSON** (`error` string):

| HTTP | Message |
|------|---------|
| **403** | `Chỉ admin tổng hoặc quản trị hệ thống được tạo tổ chức` |
| **400** | `Mã và tên tổ chức phải có ít nhất 2 ký tự` |

### `PATCH /organizations/:id` {#patch-organizations--id}

Đường dẫn đầy đủ `/api/organizations/:id`. Lớp kiểm tra: `requireAuth, requireChainManagement`.

**URL:** `PATCH /api/organizations/:id`

**Lớp route:** `requireAuth`, `requireChainManagement`
- **Thêm trong handler:** role **`super_admin`** (403 nếu không đủ).

**Lỗi JSON** (`error` string):

| HTTP | Message |
|------|---------|
| **403** | `Chỉ admin tổng hoặc quản trị hệ thống được sửa tổ chức` |
| **400** | `Invalid ID` |
| **403** | `Chỉ quản trị hệ thống được chấm dứt/kích hoạt lại chuỗi` |
| **400** | `vatInboundAutoSyncEnabled phải là true/false` |
| **400** | `vatInboundAutoMapEnabled phải là true/false` |
| **400** | `vatInboundAutoReceiveEnabled phải là true/false` |
| **400** | `Không có dữ liệu để cập nhật` |
| **400** | `Không thể ngừng hoạt động tổ chức tổng` |
| **404** | `Tổ chức không tồn tại` |

### `PATCH /shops/:id` {#patch-shops--id}

Đường dẫn đầy đủ `/api/shops/:id`. Lớp kiểm tra: `requireAuth`.

**URL:** `PATCH /api/shops/:id`

**Lớp route:** `requireAuth`

**Lỗi JSON** (`error` string):

| HTTP | Message |
|------|---------|
| **403** | `Không có quyền cấu hình vận hành cửa hàng này` |
| **400** | `Invalid ID` |
| **403** | `Forbidden` |
| **400** | `Mã cửa hàng đã được dùng ở cửa hàng khác` |
| **400** | `allowOverselling phải là boolean` |
| **400** | `allowOrderEdit phải là boolean` |
| **400** | `allowStaffEditPayment phải là boolean` |
| **400** | `allowStaffEditCart phải là boolean` |
| **400** | `allowStaffApproveStock phải là boolean` |
| **400** | `deviceControlEnabled phải là boolean` |
| **400** | `weightedAverageCostEnabled phải là boolean` |
| **400** | `vatInvoicePublicEnabled phải là boolean` |
| **400** | `vatInvoiceAutoIssueEnabled phải là boolean` |
| **400** | `Bật xuất hóa đơn điện tử cho khách trước khi bật tự xuất HĐ` |
| **400** | `vatInvoiceInboundMappedOnlyEnabled phải là boolean` |
| **400** | `hubAdminDashboardProfitEnabled phải là boolean` |
| **400** | `Chỉ cấu hình tại cửa hàng tổng` |
| **400** | `hubAccountantDashboardProfitEnabled phải là boolean` |
| **400** | `hubManagerCatalogSalesCountEnabled phải là boolean` |
| **400** | `hubAccountantCatalogSalesCountEnabled phải là boolean` |
| **400** | `paymentProofEnabled phải là boolean` |
| **400** | `productProofEnabled phải là boolean` |
| **400** | `mobileWebPosEnabled phải là boolean` |
| **400** | `Không có dữ liệu để cập nhật` |
| **400** | `Không thể ngừng hoạt động cửa hàng tổng` |
| **404** | `Cửa hàng không tồn tại` |

### `POST /shops/:id/devices/register` {#post-shops--id-devices-register}

Đường dẫn đầy đủ `/api/shops/:id/devices/register`. Lớp kiểm tra: `requireAuth`.

**URL:** `POST /api/shops/:id/devices/register`

**Lớp route:** `requireAuth`

**Lỗi JSON** (`error` string):

| HTTP | Message |
|------|---------|
| **400** | `Invalid ID` |
| **403** | `Forbidden` |
| **400** | `Thiếu X-Device-Id` |
| **404** | `Cửa hàng không tồn tại` |

**Response 200** — trường top-level (trích `res.json`):

`deviceControlEnabled`, `status`

### `GET /shops/:id/devices` {#get-shops--id-devices}

Đường dẫn đầy đủ `/api/shops/:id/devices`. Lớp kiểm tra: `requireAuth`.

**URL:** `GET /api/shops/:id/devices`

**Lớp route:** `requireAuth`

**Lỗi JSON** (`error` string):

| HTTP | Message |
|------|---------|
| **400** | `Invalid ID` |
| **403** | `Forbidden` |

### `PATCH /shops/:id/devices/:deviceRowId` {#patch-shops--id-devices--deviceRowId}

Đường dẫn đầy đủ `/api/shops/:id/devices/:deviceRowId`. Lớp kiểm tra: `requireAuth`.

**URL:** `PATCH /api/shops/:id/devices/:deviceRowId`

**Lớp route:** `requireAuth`

**Request body** (`application/json`, trích từ code):

| Trường | Ghi chú |
|--------|---------|
| `deviceName` | xem handler |
| `status` | xem handler |

**Lỗi JSON** (`error` string):

| HTTP | Message |
|------|---------|
| **400** | `Invalid ID` |
| **403** | `Forbidden` |
| **403** | `Chỉ admin tổng được duyệt/thu hồi hoặc đổi tên thiết bị` |
| **400** | `Không có dữ liệu để cập nhật` |
| **404** | `Thiết bị không tồn tại` |

### `GET /shops/:id/devices/:deviceRowId/login-events` {#get-shops--id-devices--deviceRowId-login-events}

Đường dẫn đầy đủ `/api/shops/:id/devices/:deviceRowId/login-events`. Lớp kiểm tra: `requireAuth`.

**URL:** `GET /api/shops/:id/devices/:deviceRowId/login-events`

**Lớp route:** `requireAuth`

**Query:** `from`, `limit`, `page`, `to`

**Lỗi JSON** (`error` string):

| HTTP | Message |
|------|---------|
| **400** | `Invalid ID` |
| **403** | `Forbidden` |
| **404** | `Thiết bị không tồn tại` |

**Response 200** — trường top-level (trích `res.json`):

`createdAt`, `email`, `id`, `ip`, `items`, `method`, `name`, `role`, `user`, `userAgent`

### `POST /shops/:id/create-admin` {#post-shops--id-create-admin}

Đường dẫn đầy đủ `/api/shops/:id/create-admin`. Lớp kiểm tra: `requireAuth`.

**URL:** `POST /api/shops/:id/create-admin`

**Lớp route:** `requireAuth`

**Lỗi JSON** (`error` string):

| HTTP | Message |
|------|---------|
| **403** | `Forbidden` |
| **400** | `Invalid ID` |
| **400** | `Email hợp lệ và mật khẩu tối thiểu 6 ký tự` |
| **404** | `Cửa hàng không tồn tại` |
| **409** | `Cửa hàng đã có tài khoản admin` |

### `PATCH /shops/:id/admin-email` {#patch-shops--id-admin-email}

Đường dẫn đầy đủ `/api/shops/:id/admin-email`. Lớp kiểm tra: `requireAuth`.

**URL:** `PATCH /api/shops/:id/admin-email`

**Lớp route:** `requireAuth`

**Lỗi JSON** (`error` string):

| HTTP | Message |
|------|---------|
| **403** | `Forbidden` |
| **400** | `Invalid ID` |
| **400** | `Email không hợp lệ` |
| **404** | `Không có tài khoản admin cho cửa hàng này` |

**Response 200** — trường top-level (trích `res.json`):

`email`, `ok`

### `PATCH /shops/:id/reset-password` {#patch-shops--id-reset-password}

Đường dẫn đầy đủ `/api/shops/:id/reset-password`. Lớp kiểm tra: `requireAuth`.

**URL:** `PATCH /api/shops/:id/reset-password`

**Lớp route:** `requireAuth`

**Lỗi JSON** (`error` string):

| HTTP | Message |
|------|---------|
| **403** | `Forbidden` |
| **400** | `Invalid ID` |
| **400** | `Mật khẩu tối thiểu 6 ký tự` |
| **404** | `Không tìm thấy tài khoản admin cho cửa hàng này` |

**Response 200** — trường top-level (trích `res.json`):

`email`, `ok`

### `POST /shops` {#post-shops}

Đường dẫn đầy đủ `/api/shops`. Lớp kiểm tra: `requireAuth`.

**URL:** `POST /api/shops`

**Lớp route:** `requireAuth`

**Lỗi JSON** (`error` string):

| HTTP | Message |
|------|---------|
| **403** | `Forbidden` |
| **400** | `Tên cửa hàng và tổ chức là bắt buộc` |
| **400** | `Mã cửa hàng đã được dùng ở cửa hàng khác` |

### `GET /warehouses` {#get-warehouses}

Đường dẫn đầy đủ `/api/warehouses`. Lớp kiểm tra: `requireAuth`.

**URL:** `GET /api/warehouses`

**Lớp route:** `requireAuth`

*Handler không trích được contract tự động — mở file route TypeScript.*

### `POST /warehouses` {#post-warehouses}

Đường dẫn đầy đủ `/api/warehouses`. Lớp kiểm tra: `requireAuth`.

**URL:** `POST /api/warehouses`

**Lớp route:** `requireAuth`

**Lỗi JSON** (`error` string):

| HTTP | Message |
|------|---------|
| **403** | `Forbidden` |
| **400** | `organizationId và tên kho là bắt buộc` |

### `PATCH /warehouses/:id` {#patch-warehouses--id}

Đường dẫn đầy đủ `/api/warehouses/:id`. Lớp kiểm tra: `requireAuth`.

**URL:** `PATCH /api/warehouses/:id`

**Lớp route:** `requireAuth`

**Lỗi JSON** (`error` string):

| HTTP | Message |
|------|---------|
| **403** | `Forbidden` |
| **400** | `Invalid ID` |
| **400** | `Không có dữ liệu để cập nhật` |
| **404** | `Kho không tồn tại` |

### `GET /warehouses/:id/products` {#get-warehouses--id-products}

Đường dẫn đầy đủ `/api/warehouses/:id/products`. Lớp kiểm tra: `requireAuth`.

**URL:** `GET /api/warehouses/:id/products`

**Lớp route:** `requireAuth`

**Lỗi JSON** (`error` string):

| HTTP | Message |
|------|---------|
| **400** | `Invalid ID` |
| **404** | `Kho không tồn tại` |

### `GET /warehouses/:id/inventory` {#get-warehouses--id-inventory}

Đường dẫn đầy đủ `/api/warehouses/:id/inventory`. Lớp kiểm tra: `requireAuth`.

**URL:** `GET /api/warehouses/:id/inventory`

**Lớp route:** `requireAuth`

**Lỗi JSON** (`error` string):

| HTTP | Message |
|------|---------|
| **400** | `Invalid ID` |
| **404** | `Kho không tồn tại` |

### `POST /warehouses/:id/adjust-stock` {#post-warehouses--id-adjust-stock}

Đường dẫn đầy đủ `/api/warehouses/:id/adjust-stock`. Lớp kiểm tra: `requireAuth`.

**URL:** `POST /api/warehouses/:id/adjust-stock`

**Lớp route:** `requireAuth`

**Lỗi JSON** (`error` string):

| HTTP | Message |
|------|---------|
| **403** | `Forbidden` |
| **400** | `Invalid ID` |
| **400** | `productId và quantity (>= 0) là bắt buộc` |
| **404** | `Kho không tồn tại` |

### `GET /transfers` {#get-transfers}

Đường dẫn đầy đủ `/api/transfers`. Lớp kiểm tra: `requireAuth`.

**URL:** `GET /api/transfers`

**Lớp route:** `requireAuth`

*Handler không trích được contract tự động — mở file route TypeScript.*

### `GET /transfers/:id/items` {#get-transfers--id-items}

Đường dẫn đầy đủ `/api/transfers/:id/items`. Lớp kiểm tra: `requireAuth`.

**URL:** `GET /api/transfers/:id/items`

**Lớp route:** `requireAuth`

**Lỗi JSON** (`error` string):

| HTTP | Message |
|------|---------|
| **400** | `Invalid ID` |

### `POST /transfers` {#post-transfers}

Đường dẫn đầy đủ `/api/transfers`. Lớp kiểm tra: `requireAuth`.

**URL:** `POST /api/transfers`

**Lớp route:** `requireAuth`

**Lỗi JSON** (`error` string):

| HTTP | Message |
|------|---------|
| **400** | `Kho nguồn và kho đích không hợp lệ` |
| **400** | `Phải có ít nhất 1 sản phẩm trong phiếu chuyển kho` |

### `POST /transfers/:id/approve` {#post-transfers--id-approve}

Đường dẫn đầy đủ `/api/transfers/:id/approve`. Lớp kiểm tra: `requireAuth`.

**URL:** `POST /api/transfers/:id/approve`

**Lớp route:** `requireAuth`

**Lỗi JSON** (`error` string):

| HTTP | Message |
|------|---------|
| **403** | `Forbidden` |
| **404** | `Phiếu không tồn tại` |

### `POST /transfers/:id/ship` {#post-transfers--id-ship}

Đường dẫn đầy đủ `/api/transfers/:id/ship`. Lớp kiểm tra: `requireAuth`.

**URL:** `POST /api/transfers/:id/ship`

**Lớp route:** `requireAuth`

**Lỗi JSON** (`error` string):

| HTTP | Message |
|------|---------|
| **404** | `Phiếu không tồn tại` |
| **400** | `Phiếu chưa được duyệt` |
| **404** | `Kho nguồn không tồn tại` |

### `POST /transfers/:id/receive` {#post-transfers--id-receive}

Đường dẫn đầy đủ `/api/transfers/:id/receive`. Lớp kiểm tra: `requireAuth`.

**URL:** `POST /api/transfers/:id/receive`

**Lớp route:** `requireAuth`

**Lỗi JSON** (`error` string):

| HTTP | Message |
|------|---------|
| **404** | `Phiếu không tồn tại` |
| **400** | `Phiếu chưa được xuất kho` |
| **404** | `Kho đích không tồn tại` |

### `DELETE /transfers/:id` {#delete-transfers--id}

Đường dẫn đầy đủ `/api/transfers/:id`. Lớp kiểm tra: `requireAuth`.

**URL:** `DELETE /api/transfers/:id`

**Lớp route:** `requireAuth`

**Lỗi JSON** (`error` string):

| HTTP | Message |
|------|---------|
| **403** | `Forbidden` |
| **404** | `Phiếu không tồn tại` |
| **400** | `Chỉ có thể huỷ phiếu đang ở trạng thái nháp` |

**Response 200** — trường top-level (trích `res.json`):

`ok`

### `PATCH /transfers/:id` {#patch-transfers--id}

Đường dẫn đầy đủ `/api/transfers/:id`. Lớp kiểm tra: `requireAuth`.

**URL:** `PATCH /api/transfers/:id`

**Lớp route:** `requireAuth`

**Lỗi JSON** (`error` string):

| HTTP | Message |
|------|---------|
| **403** | `Forbidden` |
| **404** | `Phiếu không tồn tại` |
| **400** | `Chỉ có thể chỉnh sửa phiếu ở trạng thái nháp` |
| **400** | `Phải có ít nhất 1 sản phẩm` |

**Response 200** — trường top-level (trích `res.json`):

`ok`

### `GET /warehouses/:id/movements` {#get-warehouses--id-movements}

Đường dẫn đầy đủ `/api/warehouses/:id/movements`. Lớp kiểm tra: `requireAuth`.

**URL:** `GET /api/warehouses/:id/movements`

**Lớp route:** `requireAuth`

**Lỗi JSON** (`error` string):

| HTTP | Message |
|------|---------|
| **400** | `Invalid ID` |

## Ghi chú đọc mã

- Gắn prefix `/api` trong `app.ts`; file route: `routes/index.ts` → `./chain.ts`.
- Handler đầy đủ: mở file TypeScript tại Shop (tìm theo chuỗi path).
- Quyền role: `tham-chieu/phan-quyen-rbac/README.md` (tiếng Anh gốc) + các `require*` trong từng endpoint.

**Đọc tiếp:** [Hướng dẫn Map](../../huong-dan-doc/) · [Mục lục](../../README.md)
