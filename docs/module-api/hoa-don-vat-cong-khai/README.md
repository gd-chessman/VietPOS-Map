# Module API: `public-vat-invoice`

**Mô tả:** Module API public-vat-invoice.ts — 3 endpoint. API/form HĐ VAT công khai.

**Mã nguồn Shop:** `artifacts/api-server/src/routes/public-vat-invoice.ts`

API/form HĐ VAT công khai.

**Số endpoint:** 3

## Bảng endpoint (tóm tắt)

| Method | Path | Mô tả ngắn |
|--------|------|------------|
| GET | `/public/vat-invoice` | Đường dẫn đầy đủ `/api/public/vat-invoice` |
| PATCH | `/public/vat-invoice` | Đường dẫn đầy đủ `/api/public/vat-invoice` |
| GET | `/public/vat-invoice/pdf` | Đường dẫn đầy đủ `/api/public/vat-invoice/pdf` |

## Chi tiết từng endpoint

### `GET /public/vat-invoice` {#get-public-vat-invoice}

Đường dẫn đầy đủ `/api/public/vat-invoice`. Lớp kiểm tra: `requireAuth (mặc định — xem file)`.

### `PATCH /public/vat-invoice` {#patch-public-vat-invoice}

Đường dẫn đầy đủ `/api/public/vat-invoice`. Lớp kiểm tra: `requireAuth (mặc định — xem file)`.

### `GET /public/vat-invoice/pdf` {#get-public-vat-invoice-pdf}

Đường dẫn đầy đủ `/api/public/vat-invoice/pdf`. Lớp kiểm tra: `requireAuth (mặc định — xem file)`.

## Ghi chú đọc mã

- Gắn prefix `/api` trong `app.ts`; file route: `routes/index.ts` → `./public-vat-invoice.ts`.
- Handler đầy đủ: mở file TypeScript tại Shop (tìm theo chuỗi path).
- Quyền role: `tham-chieu/phan-quyen-rbac/README.md` (tiếng Anh gốc) + các `require*` trong từng endpoint.

**Đọc tiếp:** [Hướng dẫn Map](../../huong-dan-doc/) · [Mục lục](../../README.md)
