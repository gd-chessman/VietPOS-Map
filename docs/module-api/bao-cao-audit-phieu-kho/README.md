# Module API: `stock-request-audit-reports`

**Mô tả:** Báo cáo audit phiếu nhập/xuất.

**Mã nguồn Shop:** `artifacts/api-server/src/routes/stock-request-audit-reports.ts`

Báo cáo audit phiếu nhập/xuất.

**Số endpoint:** 2

**Contract API:** Mỗi endpoint có mục **URL**, body/query (từ code + schema Zod orval khi có), bảng lỗi `error`, và response (Zod hoặc trường `res.json`).

## Bảng endpoint (tóm tắt)

| Method | Path | Mô tả ngắn |
|--------|------|------------|
| GET | `/reports/stock-request-audit/summary` | Đường dẫn đầy đủ `/api/reports/stock-request-audit/summary` |
| GET | `/reports/stock-request-audit` | Đường dẫn đầy đủ `/api/reports/stock-request-audit` |

## Chi tiết từng endpoint

### `GET /reports/stock-request-audit/summary` {#get-reports-stock-request-audit-summary}

Đường dẫn đầy đủ `/api/reports/stock-request-audit/summary`. Lớp kiểm tra: `requireAuth`.

**URL:** `GET /api/reports/stock-request-audit/summary`

**Lớp route:** `requireAuth`

**Query:** `shopId`

**Lỗi JSON** (`error` string):

| HTTP | Message |
|------|---------|
| **403** | `Không có quyền xem chi nhánh này` |

**Response 200** — trường top-level (trích `res.json`):

`totalEvents`

### `GET /reports/stock-request-audit` {#get-reports-stock-request-audit}

Đường dẫn đầy đủ `/api/reports/stock-request-audit`. Lớp kiểm tra: `requireAuth`.

**URL:** `GET /api/reports/stock-request-audit`

**Lớp route:** `requireAuth`

**Query:** `shopId`

**Lỗi JSON** (`error` string):

| HTTP | Message |
|------|---------|
| **403** | `Không có quyền xem chi nhánh này` |

**Response 200** — trường top-level (trích `res.json`):

`createdAt`, `fromShopName`, `items`, `shopName`, `toShopName`

## Ghi chú đọc mã

- Gắn prefix `/api` trong `app.ts`; file route: `routes/index.ts` → `./stock-request-audit-reports.ts`.
- Handler đầy đủ: mở file TypeScript tại Shop (tìm theo chuỗi path).
- Quyền role: `tham-chieu/phan-quyen-rbac/README.md` (tiếng Anh gốc) + các `require*` trong từng endpoint.

**Đọc tiếp:** [Hướng dẫn Map](../../huong-dan-doc/) · [Mục lục](../../README.md)
