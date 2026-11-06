# Module API: `public-vat-invoice`

**Mô tả:** Module API public-vat-invoice.ts — 3 endpoint. API/form HĐ VAT công khai.

**Mã nguồn Shop:** `artifacts/api-server/src/routes/public-vat-invoice.ts`

API/form HĐ VAT công khai.

**Số endpoint:** 3

**Contract API:** Mỗi endpoint có mục **URL**, body/query (từ code + schema Zod orval khi có), bảng lỗi `error`, và response (Zod hoặc trường `res.json`).

## Bảng endpoint (tóm tắt)

| Method | Path | Mô tả ngắn |
|--------|------|------------|
| GET | `/public/vat-invoice` | Đường dẫn đầy đủ `/api/public/vat-invoice` |
| PATCH | `/public/vat-invoice` | Đường dẫn đầy đủ `/api/public/vat-invoice` |
| GET | `/public/vat-invoice/pdf` | Đường dẫn đầy đủ `/api/public/vat-invoice/pdf` |

## Chi tiết từng endpoint

### `GET /public/vat-invoice` {#get-public-vat-invoice}

Đường dẫn đầy đủ `/api/public/vat-invoice`. Lớp kiểm tra: `requireAuth (mặc định — xem file)`.

**URL:** `GET /api/public/vat-invoice`

**Lớp route:** `requireAuth` (hoặc public — xem route)

**Lỗi JSON** (`error` string):

| HTTP | Message |
|------|---------|
| **400** | `Thiếu mã truy cập hóa đơn` |
| **404** | `Không tìm thấy đơn hàng hoặc mã không hợp lệ` |
| **403** | `Cửa hàng đã tắt xuất hóa đơn điện tử cho khách` |

**Response 200** — trường top-level (trích `res.json`):

`alreadyIssued`, `amount`, `buyerAddress`, `buyerCompanyName`, `buyerEmail`, `buyerPhone`, `buyerTaxCode`, `editDeadlineAt`, `editable`, `einvoiceCodeOfTax`, `einvoiceInvoiceNo`, `einvoiceReservationCode`, `invoiceCode`, `invoiceIssuedAt`, `invoiceRequested`, `items`, `method`, `orderNote`, `orderStatus`, `paymentMethod`, `payments`, `pendingOrderSync`, `shopAddress`, `shopName`, `shopPhone`

### `PATCH /public/vat-invoice` {#patch-public-vat-invoice}

Đường dẫn đầy đủ `/api/public/vat-invoice`. Lớp kiểm tra: `requireAuth (mặc định — xem file)`.

**URL:** `PATCH /api/public/vat-invoice`

**Lớp route:** `requireAuth` (hoặc public — xem route)

**Lỗi JSON** (`error` string):

| HTTP | Message |
|------|---------|
| **400** | `Thiếu mã truy cập hóa đơn` |
| **404** | `Không tìm thấy đơn hàng hoặc mã không hợp lệ` |
| **403** | `Cửa hàng đã tắt xuất hóa đơn điện tử cho khách` |
| **400** | `Hóa đơn điện tử đã được xuất — không thể sửa thông tin` |
| **400** | `Đơn hàng đã hủy hoặc hoàn — không thể yêu cầu xuất hóa đơn` |
| **400** | `Đã quá 2 giờ sau khi mua — không thể điền hoặc sửa thông tin xuất hóa đơn điện tử` |
| **400** | `Vui lòng nhập số điện thoại` |
| **400** | `Số điện thoại không hợp lệ` |

**Response 200** — trường top-level (trích `res.json`):

`message`

### `GET /public/vat-invoice/pdf` {#get-public-vat-invoice-pdf}

Đường dẫn đầy đủ `/api/public/vat-invoice/pdf`. Lớp kiểm tra: `requireAuth (mặc định — xem file)`.

**URL:** `GET /api/public/vat-invoice/pdf`

**Lớp route:** `requireAuth` (hoặc public — xem route)

**Lỗi JSON** (`error` string):

| HTTP | Message |
|------|---------|
| **400** | `Thiếu mã truy cập hóa đơn` |
| **404** | `Không tìm thấy đơn hàng hoặc mã không hợp lệ` |
| **403** | `Cửa hàng đã tắt xuất hóa đơn điện tử cho khách` |
| **400** | `Đơn chưa xuất hóa đơn điện tử` |

## Ghi chú đọc mã

- Gắn prefix `/api` trong `app.ts`; file route: `routes/index.ts` → `./public-vat-invoice.ts`.
- Handler đầy đủ: mở file TypeScript tại Shop (tìm theo chuỗi path).
- Quyền role: `tham-chieu/phan-quyen-rbac/README.md` (tiếng Anh gốc) + các `require*` trong từng endpoint.

**Đọc tiếp:** [Hướng dẫn Map](../../huong-dan-doc/) · [Mục lục](../../README.md)
