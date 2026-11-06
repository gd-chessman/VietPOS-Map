# Module API: `purchase-order-audit-reports`

**Mô tả:** Module API purchase-order-audit-reports.ts — 2 endpoint. Báo cáo audit phiếu mua.

**Mã nguồn Shop:** `artifacts/api-server/src/routes/purchase-order-audit-reports.ts`

Báo cáo audit phiếu mua.

**Số endpoint:** 2

## Bảng endpoint (tóm tắt)

| Method | Path | Mô tả ngắn |
|--------|------|------------|
| GET | `/reports/purchase-order-audit/summary` | Đường dẫn đầy đủ `/api/reports/purchase-order-audit/summary` |
| GET | `/reports/purchase-order-audit` | Đường dẫn đầy đủ `/api/reports/purchase-order-audit` |

## Chi tiết từng endpoint

### `GET /reports/purchase-order-audit/summary` {#get-reports-purchase-order-audit-summary}

Đường dẫn đầy đủ `/api/reports/purchase-order-audit/summary`. Lớp kiểm tra: `requireAuth`.

- **Lớp kiểm tra (middleware):** `requireAuth`

### `GET /reports/purchase-order-audit` {#get-reports-purchase-order-audit}

Đường dẫn đầy đủ `/api/reports/purchase-order-audit`. Lớp kiểm tra: `requireAuth`.

- **Lớp kiểm tra (middleware):** `requireAuth`

## Ghi chú đọc mã

- Gắn prefix `/api` trong `app.ts`; file route: `routes/index.ts` → `./purchase-order-audit-reports.ts`.
- Handler đầy đủ: mở file TypeScript tại Shop (tìm theo chuỗi path).
- Quyền role: `tham-chieu/phan-quyen-rbac/README.md` (tiếng Anh gốc) + các `require*` trong từng endpoint.

**Đọc tiếp:** [Hướng dẫn Map](../../huong-dan-doc/) · [Mục lục](../../README.md)
