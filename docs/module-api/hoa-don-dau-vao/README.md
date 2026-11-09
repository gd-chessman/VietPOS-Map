# Module API: `vat-inbound`

**Mô tả:** Module API vat-inbound.ts — 28 endpoint. Module lớn nhất về HĐ mua vào VAT: import PDF/Excel, kéo CQT/Viettel, ghép SP, nhập kho, lưu trữ, MST lọc (tab Khác)…

**Mã nguồn Shop:** `artifacts/api-server/src/routes/vat-inbound.ts`

Module **lớn nhất** về HĐ mua vào VAT: import PDF/Excel, kéo **CQT/Viettel**, ghép SP, nhập kho,
lưu trữ, MST lọc (tab Khác), audit, hoàn tác nhập kho / bỏ ghép dòng.

**Lib quan trọng:** `lib/vat-inbound-tax-sync.ts`, `lib/gdt-portal/*`, `lib/vat-inbound-auto-archive-mst.ts`,
`lib/viettel-sinvoice/*`, `lib/inbound-stock-receive.ts`.

**Giao diện:** `pages/vat-inbound.tsx`, `lib/vat-inbound-api.ts`, IndexedDB `@workspace/local-db`.

**Quyền:** hub shop + `requireVatInboundAccess` (admin, manager, accountant, warehouse_keeper tại CN chính).

**Số endpoint:** 28

**Contract API:** Mỗi endpoint có mục **URL**, body/query (từ code + schema Zod orval khi có), bảng lỗi `error`, và response (Zod hoặc trường `res.json`).

## Bảng endpoint (tóm tắt)

| Method | Path | Mô tả ngắn |
|--------|------|------------|
| GET | `/vat-inbound` | Danh sách HĐ mua vào của **hub shop**; không trả `pdfBase64` (chỉ cờ `hasPdf`); tự relink PO nếu thiếu; join trạng thái … |
| GET | `/vat-inbound/marked-mst-archive` | Đọc chuỗi MST lọc từ `organizations… |
| PATCH | `/vat-inbound/marked-mst-archive` | Lưu MST lọc (admin/manager); normalize input; **backfill** archive HĐ trùng MST ngay sau lưu… |
| POST | `/vat-inbound/backfill-marked-mst-archive` | Chạy lại backfill archive theo MST (ops / sau migration)… |
| POST | `/vat-inbound/gdt/captcha` | Lấy captcha CQT cho org `gdt_direct` — trả session tạm captcha store… |
| POST | `/vat-inbound/gdt/reconnect` | Đăng nhập lại CQT sau captcha; lưu session org GDT… |
| POST | `/vat-inbound/sync-tax` | Kéo HĐ từ CQT/Viettel theo `from`/`to`; map XML → DB; auto archive MST; có thể split khoảng dài… |
| GET | `/vat-inbound/:id/pdf` | Tải PDF base64 đã lưu hoặc fetch Viettel nếu thiếu… |
| GET | `/vat-inbound/:id` | Chi tiết một HĐ (metadata + stock lines, không full PDF trong list)… |
| POST | `/vat-inbound` | Upsert HĐ (import PDF/Excel từ client); parse fields; sync archive MST on write… |
| POST | `/vat-inbound/:id/verify-viettel` | Xác thực HĐ với Viettel SInvoice; cập nhật trạng thái verify… |
| POST | `/vat-inbound/:id/stock-receipt` | Ghép dòng HĐ ↔ SP; tạo/cập nhật `stockLines`; có thể tạo SP/NCC/PO inline… |
| GET | `/vat-inbound/:id/purchase-order` | Lấy PO gắn HĐ (nếu có) |
| POST | `/vat-inbound/:id/receive-stock` | Nhập kho theo dòng đã ghép; cập nhật tồn + giá vốn BQ; đổi `stockStatus`… |
| POST | `/vat-inbound/:id/restore-line` | Khôi phục dòng đã loại trừ khỏi ghép hàng… |
| POST | `/vat-inbound/:id/dismiss-excluded-lines` | Bỏ qua dòng không nhập (phí, dịch vụ…) — ghi audit… |
| POST | `/vat-inbound/:id/undo-dismiss-excluded-lines` | Hoàn tác bỏ qua dòng (nếu policy cho phép)… |
| POST | `/vat-inbound/:id/request-undo-dismiss-excluded` | NV gửi yêu cầu hoàn tác bỏ qua dòng |
| POST | `/vat-inbound/:id/approve-undo-dismiss-excluded` | Quản lý duyệt hoàn tác bỏ qua dòng |
| POST | `/vat-inbound/:id/reject-undo-dismiss-excluded` | Từ chối yêu cầu hoàn tác bỏ qua dòng |
| POST | `/vat-inbound/:id/close-short` | Chốt nhập **thiếu** — đóng phiếu với trạng thái `closed_short`… |
| POST | `/vat-inbound/:id/request-rollback` | Yêu cầu hoàn tác nhập kho (rollback inventory)… |
| POST | `/vat-inbound/:id/approve-rollback` | Duyệt rollback — trừ lại tồn đã nhập |
| POST | `/vat-inbound/:id/reject-rollback` | Từ chối yêu cầu rollback |
| GET | `/vat-inbound/:id/audit-logs` | Nhật ký thao tác trên HĐ (`vat_inbound_audit_logs`)… |
| POST | `/vat-inbound/:id/archive` | Lưu trữ thủ công (`archivedAt`) |
| POST | `/vat-inbound/:id/unarchive` | Bỏ lưu trữ |
| DELETE | `/vat-inbound/:id` | Xóa HĐ (policy + trạng thái kho); thường admin… |

## Chi tiết từng endpoint

### `GET /vat-inbound` {#get-vat-inbound}

Danh sách HĐ mua vào của **hub shop**; không trả `pdfBase64` (chỉ cờ `hasPdf`); tự relink PO nếu thiếu; join trạng thái PO. Lớp kiểm tra: `requireAuth, requireOperationalContext, requireVatInboundAccess`.

**URL:** `GET /api/vat-inbound`

**Lớp route:** `requireAuth`, `requireOperationalContext`, `requireVatInboundAccess`

*Handler không trích được contract tự động — mở file route TypeScript.*

### `GET /vat-inbound/marked-mst-archive` {#get-vat-inbound-marked-mst-archive}

Đọc chuỗi MST lọc từ `organizations.vat_inbound_auto_archive_tax_codes`. Lớp kiểm tra: `requireAuth, requireOperationalContext, requireVatInboundAccess`.

**URL:** `GET /api/vat-inbound/marked-mst-archive`

**Lớp route:** `requireAuth`, `requireOperationalContext`, `requireVatInboundAccess`

**Lỗi JSON** (`error` string):

| HTTP | Message |
|------|---------|
| **400** | `Không xác định được tổ chức` |

**Response 200** — trường top-level (trích `res.json`):

`codes`

### `PATCH /vat-inbound/marked-mst-archive` {#patch-vat-inbound-marked-mst-archive}

Lưu MST lọc (admin/manager); normalize input; **backfill** archive HĐ trùng MST ngay sau lưu. Lớp kiểm tra: `requireAuth, requireOperationalContext, requireVatInboundAccess`.

**URL:** `PATCH /api/vat-inbound/marked-mst-archive`

**Lớp route:** `requireAuth`, `requireOperationalContext`, `requireVatInboundAccess`

**Lỗi JSON** (`error` string):

| HTTP | Message |
|------|---------|
| **403** | `Chỉ quản lý hoặc admin được sửa danh sách MST lọc` |
| **400** | `Không xác định được tổ chức` |
| **400** | `codes phải là chuỗi hoặc null` |

**Response 200** — trường top-level (trích `res.json`):

`codes`

### `POST /vat-inbound/backfill-marked-mst-archive` {#post-vat-inbound-backfill-marked-mst-archive}

Chạy lại backfill archive theo MST (ops / sau migration). Lớp kiểm tra: `requireAuth, requireOperationalContext, requireVatInboundAccess`.

**URL:** `POST /api/vat-inbound/backfill-marked-mst-archive`

**Lớp route:** `requireAuth`, `requireOperationalContext`, `requireVatInboundAccess`

**Lỗi JSON** (`error` string):

| HTTP | Message |
|------|---------|
| **400** | `Không xác định được tổ chức` |

### `POST /vat-inbound/gdt/captcha` {#post-vat-inbound-gdt-captcha}

Lấy captcha CQT cho org `gdt_direct` — trả session tạm captcha store. Lớp kiểm tra: `requireAuth, requireOperationalContext, requireVatInboundAccess`.

**URL:** `POST /api/vat-inbound/gdt/captcha`

**Lớp route:** `requireAuth`, `requireOperationalContext`, `requireVatInboundAccess`

**Response 200** — trường top-level (trích `res.json`):

`ok`

### `POST /vat-inbound/gdt/reconnect` {#post-vat-inbound-gdt-reconnect}

Đăng nhập lại CQT sau captcha; lưu session org GDT. Lớp kiểm tra: `requireAuth, requireOperationalContext, requireVatInboundAccess`.

**URL:** `POST /api/vat-inbound/gdt/reconnect`

**Lớp route:** `requireAuth`, `requireOperationalContext`, `requireVatInboundAccess`

**Response 200** — trường top-level (trích `res.json`):

`message`, `ok`, `probeWarning`, `sampleCount`, `session`

### `POST /vat-inbound/sync-tax` {#post-vat-inbound-sync-tax}

Kéo HĐ từ CQT/Viettel theo `from`/`to`; map XML → DB; auto archive MST; có thể split khoảng dài. Lớp kiểm tra: `requireAuth, requireOperationalContext, requireVatInboundAccess`.

**URL:** `POST /api/vat-inbound/sync-tax`

**Lớp route:** `requireAuth`, `requireOperationalContext`, `requireVatInboundAccess`

**Request body** (`application/json`, trích từ code):

| Trường | Ghi chú |
|--------|---------|
| `from` | xem handler |
| `to` | xem handler |

**Lỗi JSON** (`error` string):

| HTTP | Message |
|------|---------|
| **400** | `Cần from và to dạng YYYY-MM-DD` |
| **400** | `Không xác định được tổ chức để đồng bộ hóa đơn đầu vào` |

**Response 200** — trường top-level (trích `res.json`):

`archivedMarkedMst`, `autoProcessed`, `backfillArchivedMarkedMst`, `created`, `fetched`, `from`, `to`, `updated`

### `GET /vat-inbound/:id/pdf` {#get-vat-inbound--id-pdf}

Tải PDF base64 đã lưu hoặc fetch Viettel nếu thiếu. Lớp kiểm tra: `requireAuth, requireOperationalContext, requireVatInboundAccess`.

**URL:** `GET /api/vat-inbound/:id/pdf`

**Lớp route:** `requireAuth`, `requireOperationalContext`, `requireVatInboundAccess`

**Lỗi JSON** (`error` string):

| HTTP | Message |
|------|---------|
| **400** | `Invalid ID` |
| **404** | `Không tìm thấy hoá đơn` |
| **400** | `Không xác định được tổ chức để tải PDF Viettel` |

### `GET /vat-inbound/:id` {#get-vat-inbound--id}

Chi tiết một HĐ (metadata + stock lines, không full PDF trong list). Lớp kiểm tra: `requireAuth, requireOperationalContext, requireVatInboundAccess`.

**URL:** `GET /api/vat-inbound/:id`

**Lớp route:** `requireAuth`, `requireOperationalContext`, `requireVatInboundAccess`

**Lỗi JSON** (`error` string):

| HTTP | Message |
|------|---------|
| **400** | `Invalid ID` |
| **404** | `Không tìm thấy hoá đơn` |

### `POST /vat-inbound` {#post-vat-inbound}

Upsert HĐ (import PDF/Excel từ client); parse fields; sync archive MST on write. Lớp kiểm tra: `requireAuth, requireOperationalContext, requireVatInboundAccess`.

**URL:** `POST /api/vat-inbound`

**Lớp route:** `requireAuth`, `requireOperationalContext`, `requireVatInboundAccess`

*Handler không trích được contract tự động — mở file route TypeScript.*

### `POST /vat-inbound/:id/verify-viettel` {#post-vat-inbound--id-verify-viettel}

Xác thực HĐ với Viettel SInvoice; cập nhật trạng thái verify. Lớp kiểm tra: `requireAuth, requireOperationalContext, requireVatInboundAccess`.

**URL:** `POST /api/vat-inbound/:id/verify-viettel`

**Lớp route:** `requireAuth`, `requireOperationalContext`, `requireVatInboundAccess`

**Lỗi JSON** (`error` string):

| HTTP | Message |
|------|---------|
| **403** | `Không có quyền ghép hàng` |
| **400** | `Tài khoản chưa gắn cửa hàng` |
| **400** | `Invalid ID` |
| **404** | `Không tìm thấy hoá đơn` |

**Response 200** — trường top-level (trích `res.json`):

`message`, `ok`, `skipped`

### `POST /vat-inbound/:id/stock-receipt` {#post-vat-inbound--id-stock-receipt}

Ghép dòng HĐ ↔ SP; tạo/cập nhật `stockLines`; có thể tạo SP/NCC/PO inline. Lớp kiểm tra: `requireAuth, requireOperationalContext, requireVatInboundAccess`.

**URL:** `POST /api/vat-inbound/:id/stock-receipt`

**Lớp route:** `requireAuth`, `requireOperationalContext`, `requireVatInboundAccess`

**Lỗi JSON** (`error` string):

| HTTP | Message |
|------|---------|
| **403** | `Không có quyền ghép hàng` |
| **400** | `Tài khoản chưa gắn cửa hàng` |
| **400** | `Invalid ID` |
| **404** | `Không tìm thấy hoá đơn` |
| **400** | `Hoá đơn đang chờ duyệt hoàn tác. Không thể sửa ghép hàng.` |
| **400** | `Hoá đơn này đã xử lý theo phiếu đặt cũ. Không ghép hàng lại trên hoá đơn.` |
| **400** | `Cần ít nhất một dòng hàng để ghép hàng` |
| **400** | `Dòng hàng không hợp lệ` |
| **400** | `Số lượng nhập phải là số nguyên ≥ 1` |
| **400** | `Giá nhập không hợp lệ` |
| **400** | `Tên sản phẩm mới là bắt buộc` |
| **400** | `Giá bán sản phẩm mới không hợp lệ` |
| **400** | `Mã nội bộ là bắt buộc khi tạo sản phẩm mới` |
| **400** | `Mỗi dòng cần chọn sản phẩm hoặc bật tạo sản phẩm mới` |
| **400** | `Không chọn trùng một sản phẩm trên nhiều dòng` |

**Response 201** — trường top-level (trích `res.json`):

`createdProductIds`, `message`, `mới`, `status`, `supplierCreated`, `supplierId`

### `GET /vat-inbound/:id/purchase-order` {#get-vat-inbound--id-purchase-order}

Lấy PO gắn HĐ (nếu có). Lớp kiểm tra: `requireAuth, requireOperationalContext, requireVatInboundAccess`.

**URL:** `GET /api/vat-inbound/:id/purchase-order`

**Lớp route:** `requireAuth`, `requireOperationalContext`, `requireVatInboundAccess`

**Lỗi JSON** (`error` string):

| HTTP | Message |
|------|---------|
| **400** | `Tài khoản chưa gắn cửa hàng` |
| **400** | `Invalid ID` |
| **404** | `Không tìm thấy hoá đơn` |
| **400** | `Hoá đơn chưa ghép hàng. Ghép sản phẩm trước khi nhập kho.` |
| **404** | `Không tìm thấy phiếu đặt hàng cũ` |

**Response 200** — trường top-level (trích `res.json`):

`code`, `costPrice`, `id`, `internalCode`, `items`, `note`, `orderQty`, `productId`, `productName`, `receivedQty`, `status`, `supplierName`, `unit`

### `POST /vat-inbound/:id/receive-stock` {#post-vat-inbound--id-receive-stock}

Nhập kho theo dòng đã ghép; cập nhật tồn + giá vốn BQ; đổi `stockStatus`. Lớp kiểm tra: `requireAuth, requireOperationalContext, requireVatInboundAccess`.

**URL:** `POST /api/vat-inbound/:id/receive-stock`

**Lớp route:** `requireAuth`, `requireOperationalContext`, `requireVatInboundAccess`

**Lỗi JSON** (`error` string):

| HTTP | Message |
|------|---------|
| **403** | `Không có quyền nhập kho` |
| **400** | `Tài khoản chưa gắn cửa hàng` |
| **400** | `Invalid ID` |
| **404** | `Không tìm thấy hoá đơn` |
| **400** | `Hoá đơn này không còn nhận thêm hàng` |
| **400** | `Hoá đơn đang chờ duyệt hoàn tác — không nhập thêm` |
| **400** | `Hoá đơn chưa ghép hàng. Ghép sản phẩm trước khi nhập kho.` |
| **400** | `Dòng nhận hàng không hợp lệ` |
| **400** | `ID dòng hàng không hợp lệ` |
| **400** | `Trùng ID dòng hàng` |
| **400** | `Số lượng đã nhận phải là số nguyên ≥ 0` |
| **400** | `Phải gửi đủ tất cả dòng hàng` |

**Response 200** — trường top-level (trích `res.json`):

`message`, `status`, `totalDelta`, `đơn`

### `POST /vat-inbound/:id/restore-line` {#post-vat-inbound--id-restore-line}

Khôi phục dòng đã loại trừ khỏi ghép hàng. Lớp kiểm tra: `requireAuth, requireOperationalContext, requireVatInboundAccess`.

**URL:** `POST /api/vat-inbound/:id/restore-line`

**Lớp route:** `requireAuth`, `requireOperationalContext`, `requireVatInboundAccess`

**Lỗi JSON** (`error` string):

| HTTP | Message |
|------|---------|
| **403** | `Không có quyền khôi phục dòng hàng` |
| **400** | `Tài khoản chưa gắn cửa hàng` |
| **400** | `Invalid ID` |
| **404** | `Không tìm thấy hoá đơn` |
| **400** | `Hoá đơn chưa được ghép hàng` |
| **400** | `Hoá đơn đang chờ duyệt hoàn tác — không thể khôi phục dòng` |
| **400** | `Vị trí dòng hoá đơn không hợp lệ` |

**Response 200** — trường top-level (trích `res.json`):

`message`, `newLine`, `nextExcluded`, `ok`, `stockExcludedLineIndexes`, `stockStatus`

### `POST /vat-inbound/:id/dismiss-excluded-lines` {#post-vat-inbound--id-dismiss-excluded-lines}

Bỏ qua dòng không nhập (phí, dịch vụ…) — ghi audit. Lớp kiểm tra: `requireAuth, requireOperationalContext, requireVatInboundAccess`.

**URL:** `POST /api/vat-inbound/:id/dismiss-excluded-lines`

**Lớp route:** `requireAuth`, `requireOperationalContext`, `requireVatInboundAccess`

**Lỗi JSON** (`error` string):

| HTTP | Message |
|------|---------|
| **403** | `Không có quyền chốt ghép thiếu` |
| **400** | `Tài khoản chưa gắn cửa hàng` |
| **400** | `Invalid ID` |
| **404** | `Không tìm thấy hoá đơn` |
| **400** | `Đã xác nhận không ghép các dòng còn lại trước đó` |
| **400** | `Hoá đơn không còn dòng ghép thiếu` |

**Response 200** — trường top-level (trích `res.json`):

`message`, `ok`, `stockExcludedLinesDismissedAt`

### `POST /vat-inbound/:id/undo-dismiss-excluded-lines` {#post-vat-inbound--id-undo-dismiss-excluded-lines}

Hoàn tác bỏ qua dòng (nếu policy cho phép). Lớp kiểm tra: `requireAuth, requireOperationalContext, requireVatInboundAccess`.

**URL:** `POST /api/vat-inbound/:id/undo-dismiss-excluded-lines`

**Lớp route:** `requireAuth`, `requireOperationalContext`, `requireVatInboundAccess`

**Lỗi JSON** (`error` string):

| HTTP | Message |
|------|---------|
| **403** | `Chỉ quản lý / quản trị được hoàn tác chốt ghép thiếu` |
| **400** | `Tài khoản chưa gắn cửa hàng` |
| **400** | `Invalid ID` |
| **404** | `Không tìm thấy hoá đơn` |

**Response 200** — trường top-level (trích `res.json`):

`message`, `ok`, `stockExcludedLineIndexes`

### `POST /vat-inbound/:id/request-undo-dismiss-excluded` {#post-vat-inbound--id-request-undo-dismiss-excluded}

NV gửi yêu cầu hoàn tác bỏ qua dòng. Lớp kiểm tra: `requireAuth, requireOperationalContext, requireVatInboundAccess`.

**URL:** `POST /api/vat-inbound/:id/request-undo-dismiss-excluded`

**Lớp route:** `requireAuth`, `requireOperationalContext`, `requireVatInboundAccess`

**Lỗi JSON** (`error` string):

| HTTP | Message |
|------|---------|
| **403** | `Không có quyền đề nghị hoàn tác chốt ghép thiếu` |
| **400** | `Tài khoản chưa gắn cửa hàng` |
| **400** | `Invalid ID` |
| **400** | `Nhập lý do (ít nhất 3 ký tự)` |
| **404** | `Không tìm thấy hoá đơn` |
| **400** | `Hoá đơn chưa chốt không ghép dòng còn lại` |
| **400** | `Đã có đề nghị hoàn tác chốt ghép thiếu đang chờ duyệt` |

**Response 200** — trường top-level (trích `res.json`):

`applied`, `message`, `ok`, `stockExcludedLineIndexes`, `undoDismissExcludedRequestNote`, `undoDismissExcludedRequestedAt`

### `POST /vat-inbound/:id/approve-undo-dismiss-excluded` {#post-vat-inbound--id-approve-undo-dismiss-excluded}

Quản lý duyệt hoàn tác bỏ qua dòng. Lớp kiểm tra: `requireAuth, requireOperationalContext, requireVatInboundAccess`.

**URL:** `POST /api/vat-inbound/:id/approve-undo-dismiss-excluded`

**Lớp route:** `requireAuth`, `requireOperationalContext`, `requireVatInboundAccess`

**Lỗi JSON** (`error` string):

| HTTP | Message |
|------|---------|
| **403** | `Chỉ quản lý / quản trị được duyệt hoàn tác chốt ghép thiếu` |
| **400** | `Tài khoản chưa gắn cửa hàng` |
| **400** | `Invalid ID` |
| **404** | `Không tìm thấy hoá đơn` |
| **400** | `Hoá đơn không có đề nghị hoàn tác chốt ghép thiếu đang chờ` |

**Response 200** — trường top-level (trích `res.json`):

`message`, `ok`, `stockExcludedLineIndexes`

### `POST /vat-inbound/:id/reject-undo-dismiss-excluded` {#post-vat-inbound--id-reject-undo-dismiss-excluded}

Từ chối yêu cầu hoàn tác bỏ qua dòng. Lớp kiểm tra: `requireAuth, requireOperationalContext, requireVatInboundAccess`.

**URL:** `POST /api/vat-inbound/:id/reject-undo-dismiss-excluded`

**Lớp route:** `requireAuth`, `requireOperationalContext`, `requireVatInboundAccess`

**Lỗi JSON** (`error` string):

| HTTP | Message |
|------|---------|
| **403** | `Chỉ quản lý / quản trị được từ chối đề nghị` |
| **400** | `Tài khoản chưa gắn cửa hàng` |
| **400** | `Invalid ID` |
| **404** | `Không tìm thấy hoá đơn` |
| **400** | `Hoá đơn không có đề nghị hoàn tác chốt ghép thiếu đang chờ` |

**Response 200** — trường top-level (trích `res.json`):

`message`, `ok`

### `POST /vat-inbound/:id/close-short` {#post-vat-inbound--id-close-short}

Chốt nhập **thiếu** — đóng phiếu với trạng thái `closed_short`. Lớp kiểm tra: `requireAuth, requireOperationalContext, requireVatInboundAccess`.

**URL:** `POST /api/vat-inbound/:id/close-short`

**Lớp route:** `requireAuth`, `requireOperationalContext`, `requireVatInboundAccess`

**Lỗi JSON** (`error` string):

| HTTP | Message |
|------|---------|
| **403** | `Không có quyền đóng phần thiếu` |
| **400** | `Tài khoản chưa gắn cửa hàng` |
| **400** | `Invalid ID` |
| **404** | `Không tìm thấy hoá đơn` |
| **400** | `Chỉ hoá đơn nhập còn thiếu mới được đóng phần thiếu` |

**Response 200** — trường top-level (trích `res.json`):

`message`, `status`

### `POST /vat-inbound/:id/request-rollback` {#post-vat-inbound--id-request-rollback}

Yêu cầu hoàn tác nhập kho (rollback inventory). Lớp kiểm tra: `requireAuth, requireOperationalContext, requireVatInboundAccess`.

**URL:** `POST /api/vat-inbound/:id/request-rollback`

**Lớp route:** `requireAuth`, `requireOperationalContext`, `requireVatInboundAccess`

**Lỗi JSON** (`error` string):

| HTTP | Message |
|------|---------|
| **403** | `Không có quyền đề nghị hoàn tác` |
| **400** | `Tài khoản chưa gắn cửa hàng` |
| **400** | `Invalid ID` |
| **400** | `Nhập lý do hoàn tác (ít nhất 3 ký tự)` |
| **404** | `Không tìm thấy hoá đơn` |
| **400** | `Chỉ hoàn tác được phiếu đã nhập kho (đủ / thiếu / còn thiếu)` |

**Response 200** — trường top-level (trích `res.json`):

`message`, `status`

### `POST /vat-inbound/:id/approve-rollback` {#post-vat-inbound--id-approve-rollback}

Duyệt rollback — trừ lại tồn đã nhập. Lớp kiểm tra: `requireAuth, requireOperationalContext, requireVatInboundAccess`.

**URL:** `POST /api/vat-inbound/:id/approve-rollback`

**Lớp route:** `requireAuth`, `requireOperationalContext`, `requireVatInboundAccess`

**Lỗi JSON** (`error` string):

| HTTP | Message |
|------|---------|
| **403** | `Chỉ quản lý / admin được duyệt hoàn tác` |
| **400** | `Tài khoản chưa gắn cửa hàng` |
| **400** | `Invalid ID` |
| **404** | `Không tìm thấy hoá đơn` |
| **400** | `Hoá đơn không có đề nghị hoàn tác đang chờ` |

**Response 200** — trường top-level (trích `res.json`):

`message`

### `POST /vat-inbound/:id/reject-rollback` {#post-vat-inbound--id-reject-rollback}

Từ chối yêu cầu rollback. Lớp kiểm tra: `requireAuth, requireOperationalContext, requireVatInboundAccess`.

**URL:** `POST /api/vat-inbound/:id/reject-rollback`

**Lớp route:** `requireAuth`, `requireOperationalContext`, `requireVatInboundAccess`

**Lỗi JSON** (`error` string):

| HTTP | Message |
|------|---------|
| **403** | `Chỉ quản lý / admin được từ chối hoàn tác` |
| **400** | `Tài khoản chưa gắn cửa hàng` |
| **400** | `Invalid ID` |
| **404** | `Không tìm thấy hoá đơn` |
| **400** | `Hoá đơn không có đề nghị hoàn tác đang chờ` |

**Response 200** — trường top-level (trích `res.json`):

`message`, `status`

### `GET /vat-inbound/:id/audit-logs` {#get-vat-inbound--id-audit-logs}

Nhật ký thao tác trên HĐ (`vat_inbound_audit_logs`). Lớp kiểm tra: `requireAuth, requireOperationalContext, requireVatInboundAccess`.

**URL:** `GET /api/vat-inbound/:id/audit-logs`

**Lớp route:** `requireAuth`, `requireOperationalContext`, `requireVatInboundAccess`

**Lỗi JSON** (`error` string):

| HTTP | Message |
|------|---------|
| **400** | `Tài khoản chưa gắn cửa hàng` |
| **400** | `Invalid ID` |
| **404** | `Không tìm thấy hoá đơn` |

### `POST /vat-inbound/:id/archive` {#post-vat-inbound--id-archive}

Lưu trữ thủ công (`archivedAt`). Lớp kiểm tra: `requireAuth, requireOperationalContext, requireVatInboundAccess`.

**URL:** `POST /api/vat-inbound/:id/archive`

**Lớp route:** `requireAuth`, `requireOperationalContext`, `requireVatInboundAccess`

**Lỗi JSON** (`error` string):

| HTTP | Message |
|------|---------|
| **400** | `Invalid ID` |
| **404** | `Không tìm thấy hoá đơn` |

### `POST /vat-inbound/:id/unarchive` {#post-vat-inbound--id-unarchive}

Bỏ lưu trữ. Lớp kiểm tra: `requireAuth, requireOperationalContext, requireVatInboundAccess`.

**URL:** `POST /api/vat-inbound/:id/unarchive`

**Lớp route:** `requireAuth`, `requireOperationalContext`, `requireVatInboundAccess`

**Lỗi JSON** (`error` string):

| HTTP | Message |
|------|---------|
| **400** | `Invalid ID` |
| **404** | `Không tìm thấy hoá đơn` |

### `DELETE /vat-inbound/:id` {#delete-vat-inbound--id}

Xóa HĐ (policy + trạng thái kho); thường admin. Lớp kiểm tra: `requireAuth, requireOperationalContext, requireVatInboundAccess`.

**URL:** `DELETE /api/vat-inbound/:id`

**Lớp route:** `requireAuth`, `requireOperationalContext`, `requireVatInboundAccess`

**Lỗi JSON** (`error` string):

| HTTP | Message |
|------|---------|
| **400** | `Invalid ID` |
| **404** | `Không tìm thấy hoá đơn` |

**Response 200** — trường top-level (trích `res.json`):

`ok`

## Ghi chú đọc mã

- Gắn prefix `/api` trong `app.ts`; file route: `routes/index.ts` → `./vat-inbound.ts`.
- Handler đầy đủ: mở file TypeScript tại Shop (tìm theo chuỗi path).
- Quyền role: `tham-chieu/phan-quyen-rbac/README.md` (tiếng Anh gốc) + các `require*` trong từng endpoint.

**Đọc tiếp:** [Hướng dẫn Map](../../huong-dan-doc/) · [Mục lục](../../README.md)

## Luồng nghiệp vụ liên quan

- `nghiep-vu/06-hoa-don-dau-vao-tong-quan/README.md`
- `nghiep-vu/07-hd-dau-vao-mst-loc/README.md`
- `nghiep-vu/08-hd-dau-vao-cqt-sync/README.md`
- UI: `trang/hoa-don-dau-vao/README.md`
- Lib: `thu-vien/vat-inbound-tax-sync/README.md`, `thu-vien/cong-cqt/README.md`…
