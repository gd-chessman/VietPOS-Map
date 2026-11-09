# Module API: `org-viettel-settings`

**Mô tả:** Cấu hình Viettel SInvoice theo org.

**Mã nguồn Shop:** `artifacts/api-server/src/routes/org-viettel-settings.ts`

Cấu hình Viettel SInvoice theo org.

**Số endpoint:** 2

**Contract API:** Mỗi endpoint có mục **URL**, body/query (từ code + schema Zod orval khi có), bảng lỗi `error`, và response (Zod hoặc trường `res.json`).

## Bảng endpoint (tóm tắt)

| Method | Path | Mô tả ngắn |
|--------|------|------------|
| GET | `/viettel-invoice/settings` | Đường dẫn đầy đủ `/api/viettel-invoice/settings` |
| PATCH | `/viettel-invoice/settings` | Đường dẫn đầy đủ `/api/viettel-invoice/settings` |

## Chi tiết từng endpoint

### `GET /viettel-invoice/settings` {#get-viettel-invoice-settings}

Đường dẫn đầy đủ `/api/viettel-invoice/settings`. Lớp kiểm tra: `requireAuth`.

**URL:** `GET /api/viettel-invoice/settings`

**Lớp route:** `requireAuth`

**Lỗi JSON** (`error` string):

| HTTP | Message |
|------|---------|
| **404** | `Tài khoản chưa gắn tổ chức` |
| **404** | `Không tìm thấy tổ chức` |

**Response 200** — trường top-level (trích `res.json`):

`gdtPortalPasswordConfigured`, `gdtPortalUsername`, `gdtSession`, `inboundApiReady`, `inboundSyncReady`, `inboundTaxPortalReady`, `outboundReady`, `vatInboundProvider`

### `PATCH /viettel-invoice/settings` {#patch-viettel-invoice-settings}

Đường dẫn đầy đủ `/api/viettel-invoice/settings`. Lớp kiểm tra: `requireAuth`.

**URL:** `PATCH /api/viettel-invoice/settings`

**Lớp route:** `requireAuth`

**Lỗi JSON** (`error` string):

| HTTP | Message |
|------|---------|
| **403** | `Chỉ admin tổng hoặc quản trị hệ thống được cấu hình Viettel` |
| **400** | `Tài khoản hệ thống cần đăng nhập theo chi nhánh để cấu hình Viettel` |
| **400** | `Không có dữ liệu để cập nhật` |
| **404** | `Không tìm thấy tổ chức` |

**Response 200** — trường top-level (trích `res.json`):

`gdtPortalPasswordConfigured`, `gdtPortalUsername`, `gdtSession`, `inboundApiReady`, `inboundSyncReady`, `inboundTaxPortalReady`, `outboundReady`, `vatInboundProvider`

## Ghi chú đọc mã

- Gắn prefix `/api` trong `app.ts`; file route: `routes/index.ts` → `./org-viettel-settings.ts`.
- Handler đầy đủ: mở file TypeScript tại Shop (tìm theo chuỗi path).
- Quyền role: `tham-chieu/phan-quyen-rbac/README.md` (tiếng Anh gốc) + các `require*` trong từng endpoint.

**Đọc tiếp:** [Hướng dẫn Map](../../huong-dan-doc/) · [Mục lục](../../README.md)
