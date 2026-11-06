# Module API: `org-viettel-settings`

**Mô tả:** Module API org-viettel-settings.ts — 2 endpoint. Cấu hình Viettel SInvoice theo org.

**Mã nguồn Shop:** `artifacts/api-server/src/routes/org-viettel-settings.ts`

Cấu hình Viettel SInvoice theo org.

**Số endpoint:** 2

## Bảng endpoint (tóm tắt)

| Method | Path | Mô tả ngắn |
|--------|------|------------|
| GET | `/viettel-invoice/settings` | Đường dẫn đầy đủ `/api/viettel-invoice/settings` |
| PATCH | `/viettel-invoice/settings` | Đường dẫn đầy đủ `/api/viettel-invoice/settings` |

## Chi tiết từng endpoint

### `GET /viettel-invoice/settings` {#get-viettel-invoice-settings}

Đường dẫn đầy đủ `/api/viettel-invoice/settings`. Lớp kiểm tra: `requireAuth`.

- **Lớp kiểm tra (middleware):** `requireAuth`

### `PATCH /viettel-invoice/settings` {#patch-viettel-invoice-settings}

Đường dẫn đầy đủ `/api/viettel-invoice/settings`. Lớp kiểm tra: `requireAuth`.

- **Lớp kiểm tra (middleware):** `requireAuth`

## Ghi chú đọc mã

- Gắn prefix `/api` trong `app.ts`; file route: `routes/index.ts` → `./org-viettel-settings.ts`.
- Handler đầy đủ: mở file TypeScript tại Shop (tìm theo chuỗi path).
- Quyền role: `tham-chieu/phan-quyen-rbac/README.md` (tiếng Anh gốc) + các `require*` trong từng endpoint.

**Đọc tiếp:** [Hướng dẫn Map](../../huong-dan-doc/) · [Mục lục](../../README.md)
