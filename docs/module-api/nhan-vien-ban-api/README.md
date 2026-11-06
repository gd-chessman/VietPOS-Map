# Module API: `sales-staff`

**Mô tả:** Module API sales-staff.ts — 4 endpoint. Nhân viên bán hàng gắn quầy.

**Mã nguồn Shop:** `artifacts/api-server/src/routes/sales-staff.ts`

Nhân viên bán hàng gắn quầy.

**Số endpoint:** 4

**Contract API:** Mỗi endpoint có mục **URL**, body/query (từ code + schema Zod orval khi có), bảng lỗi `error`, và response (Zod hoặc trường `res.json`).

## Bảng endpoint (tóm tắt)

| Method | Path | Mô tả ngắn |
|--------|------|------------|
| GET | `/sales-staff` | Đường dẫn đầy đủ `/api/sales-staff` |
| GET | `/sales-staff/:id` | Đường dẫn đầy đủ `/api/sales-staff/:id` |
| POST | `/sales-staff` | Đường dẫn đầy đủ `/api/sales-staff` |
| PATCH | `/sales-staff/:id` | Đường dẫn đầy đủ `/api/sales-staff/:id` |

## Chi tiết từng endpoint

### `GET /sales-staff` {#get-sales-staff}

Đường dẫn đầy đủ `/api/sales-staff`. Lớp kiểm tra: `requireAuth`.

**URL:** `GET /api/sales-staff`

**Lớp route:** `requireAuth`
- **Thêm trong handler:** role **`super_admin`** (403 nếu không đủ).

**Lỗi JSON** (`error` string):

| HTTP | Message |
|------|---------|
| **403** | `Không có quyền xem NV bán hàng chi nhánh này` |

### `GET /sales-staff/:id` {#get-sales-staff--id}

Đường dẫn đầy đủ `/api/sales-staff/:id`. Lớp kiểm tra: `requireAuth, requireManagerOrAdmin`.

**URL:** `GET /api/sales-staff/:id`

**Lớp route:** `requireAuth`, `requireManagerOrAdmin`

**Lỗi JSON** (`error` string):

| HTTP | Message |
|------|---------|
| **400** | `Invalid ID` |
| **404** | `Không tìm thấy nhân viên bán hàng` |

### `POST /sales-staff` {#post-sales-staff}

Đường dẫn đầy đủ `/api/sales-staff`. Lớp kiểm tra: `requireAuth, requireManagerOrAdmin, requireOperationalContext`.

**URL:** `POST /api/sales-staff`

**Lớp route:** `requireAuth`, `requireManagerOrAdmin`, `requireOperationalContext`

**Lỗi JSON** (`error` string):

| HTTP | Message |
|------|---------|
| **400** | `Số căn cước đã tồn tại trong cửa hàng` |

### `PATCH /sales-staff/:id` {#patch-sales-staff--id}

Đường dẫn đầy đủ `/api/sales-staff/:id`. Lớp kiểm tra: `requireAuth, requireManagerOrAdmin, requireOperationalContext`.

**URL:** `PATCH /api/sales-staff/:id`

**Lớp route:** `requireAuth`, `requireManagerOrAdmin`, `requireOperationalContext`

**Lỗi JSON** (`error` string):

| HTTP | Message |
|------|---------|
| **400** | `Invalid ID` |
| **404** | `Không tìm thấy nhân viên bán hàng` |
| **400** | `Số căn cước đã tồn tại trong cửa hàng` |

## Ghi chú đọc mã

- Gắn prefix `/api` trong `app.ts`; file route: `routes/index.ts` → `./sales-staff.ts`.
- Handler đầy đủ: mở file TypeScript tại Shop (tìm theo chuỗi path).
- Quyền role: `tham-chieu/phan-quyen-rbac/README.md` (tiếng Anh gốc) + các `require*` trong từng endpoint.

**Đọc tiếp:** [Hướng dẫn Map](../../huong-dan-doc/) · [Mục lục](../../README.md)
