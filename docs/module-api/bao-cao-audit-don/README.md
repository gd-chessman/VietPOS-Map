# Module API: `order-audit-reports`

**Mô tả:** Module API order-audit-reports.ts — 2 endpoint. Báo cáo audit đơn hàng.

**Mã nguồn Shop:** `artifacts/api-server/src/routes/order-audit-reports.ts`

Báo cáo audit đơn hàng.

**Số endpoint:** 2

**Contract API:** Mỗi endpoint có mục **URL**, body/query (từ code + schema Zod orval khi có), bảng lỗi `error`, và response (Zod hoặc trường `res.json`).

## Bảng endpoint (tóm tắt)

| Method | Path | Mô tả ngắn |
|--------|------|------------|
| GET | `/reports/order-audit/summary` | Đường dẫn đầy đủ `/api/reports/order-audit/summary` |
| GET | `/reports/order-audit` | Đường dẫn đầy đủ `/api/reports/order-audit` |

## Chi tiết từng endpoint

### `GET /reports/order-audit/summary` {#get-reports-order-audit-summary}

Đường dẫn đầy đủ `/api/reports/order-audit/summary`. Lớp kiểm tra: `requireAuth`.

**URL:** `GET /api/reports/order-audit/summary`

**Lớp route:** `requireAuth`

**Query:** `shopId`

**Lỗi JSON** (`error` string):

| HTTP | Message |
|------|---------|
| **403** | `Không có quyền xem chi nhánh này` |

**Response 200** — trường top-level (trích `res.json`):

`cashImpactDownTotal`, `cashImpactUpTotal`, `totalEvents`

### `GET /reports/order-audit` {#get-reports-order-audit}

Đường dẫn đầy đủ `/api/reports/order-audit`. Lớp kiểm tra: `requireAuth`.

**URL:** `GET /api/reports/order-audit`

**Lớp route:** `requireAuth`

**Query:** `shopId`

**Lỗi JSON** (`error` string):

| HTTP | Message |
|------|---------|
| **403** | `Không có quyền xem chi nhánh này` |

## Ghi chú đọc mã

- Gắn prefix `/api` trong `app.ts`; file route: `routes/index.ts` → `./order-audit-reports.ts`.
- Handler đầy đủ: mở file TypeScript tại Shop (tìm theo chuỗi path).
- Quyền role: `tham-chieu/phan-quyen-rbac/README.md` (tiếng Anh gốc) + các `require*` trong từng endpoint.

**Đọc tiếp:** [Hướng dẫn Map](../../huong-dan-doc/) · [Mục lục](../../README.md)
