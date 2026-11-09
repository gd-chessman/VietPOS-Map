# Module API: `reports`

**Mô tả:** Báo cáo nhân viên, in lại bill.

**Mã nguồn Shop:** `artifacts/api-server/src/routes/reports.ts`

Báo cáo nhân viên, in lại bill.

**Số endpoint:** 4

**Contract API:** Mỗi endpoint có mục **URL**, body/query (từ code + schema Zod orval khi có), bảng lỗi `error`, và response (Zod hoặc trường `res.json`).

## Bảng endpoint (tóm tắt)

| Method | Path | Mô tả ngắn |
|--------|------|------------|
| GET | `/reports/staff` | Đường dẫn đầy đủ `/api/reports/staff` |
| GET | `/reports/sales-staff` | Đường dẫn đầy đủ `/api/reports/sales-staff` |
| GET | `/reports/reprints` | Đường dẫn đầy đủ `/api/reports/reprints` |
| GET | `/reports/staff/:userId/detail` | Đường dẫn đầy đủ `/api/reports/staff/:userId/detail` |

## Chi tiết từng endpoint

### `GET /reports/staff` {#get-reports-staff}

Đường dẫn đầy đủ `/api/reports/staff`. Lớp kiểm tra: `requireAuth`.

**URL:** `GET /api/reports/staff`

**Lớp route:** `requireAuth`

*Handler không trích được contract tự động — mở file route TypeScript.*

### `GET /reports/sales-staff` {#get-reports-sales-staff}

Đường dẫn đầy đủ `/api/reports/sales-staff`. Lớp kiểm tra: `requireAuth`.

**URL:** `GET /api/reports/sales-staff`

**Lớp route:** `requireAuth`

**Response 200** — trường top-level (trích `res.json`):

`orderCount`, `revenue`, `staff`, `unassigned`

### `GET /reports/reprints` {#get-reports-reprints}

Đường dẫn đầy đủ `/api/reports/reprints`. Lớp kiểm tra: `requireAuth`.

**URL:** `GET /api/reports/reprints`

**Lớp route:** `requireAuth`

*Handler không trích được contract tự động — mở file route TypeScript.*

### `GET /reports/staff/:userId/detail` {#get-reports-staff--userId-detail}

Đường dẫn đầy đủ `/api/reports/staff/:userId/detail`. Lớp kiểm tra: `requireAuth`.

**URL:** `GET /api/reports/staff/:userId/detail`

**Lớp route:** `requireAuth`

**Query:** `shopId`

**Lỗi JSON** (`error` string):

| HTTP | Message |
|------|---------|
| **400** | `Invalid userId` |
| **404** | `User not found` |
| **403** | `Không có quyền xem chi nhánh này` |
| **403** | `Nhân viên không thuộc chi nhánh này` |

**Response 200** — trường top-level (trích `res.json`):

`cancelledOrders`, `orderTotalAmount`, `reprints`, `totalAmount`

## Ghi chú đọc mã

- Gắn prefix `/api` trong `app.ts`; file route: `routes/index.ts` → `./reports.ts`.
- Handler đầy đủ: mở file TypeScript tại Shop (tìm theo chuỗi path).
- Quyền role: `tham-chieu/phan-quyen-rbac/README.md` (tiếng Anh gốc) + các `require*` trong từng endpoint.

**Đọc tiếp:** [Hướng dẫn Map](../../huong-dan-doc/) · [Mục lục](../../README.md)
