# Module API: `product-audit-reports`

**Mô tả:** Module API product-audit-reports.ts — 2 endpoint. Báo cáo thay đổi sản phẩm.

**Mã nguồn Shop:** `artifacts/api-server/src/routes/product-audit-reports.ts`

Báo cáo thay đổi sản phẩm.

**Số endpoint:** 2

## Bảng endpoint (tóm tắt)

| Method | Path | Mô tả ngắn |
|--------|------|------------|
| GET | `/reports/product-audit/summary` | Đường dẫn đầy đủ `/api/reports/product-audit/summary` |
| GET | `/reports/product-audit` | Đường dẫn đầy đủ `/api/reports/product-audit` |

## Chi tiết từng endpoint

### `GET /reports/product-audit/summary` {#get-reports-product-audit-summary}

Đường dẫn đầy đủ `/api/reports/product-audit/summary`. Lớp kiểm tra: `requireAuth`.

- **Lớp kiểm tra (middleware):** `requireAuth`

### `GET /reports/product-audit` {#get-reports-product-audit}

Đường dẫn đầy đủ `/api/reports/product-audit`. Lớp kiểm tra: `requireAuth`.

- **Lớp kiểm tra (middleware):** `requireAuth`

## Ghi chú đọc mã

- Gắn prefix `/api` trong `app.ts`; file route: `routes/index.ts` → `./product-audit-reports.ts`.
- Handler đầy đủ: mở file TypeScript tại Shop (tìm theo chuỗi path).
- Quyền role: `tham-chieu/phan-quyen-rbac/README.md` (tiếng Anh gốc) + các `require*` trong từng endpoint.

**Đọc tiếp:** [Hướng dẫn Map](../../huong-dan-doc/) · [Mục lục](../../README.md)
