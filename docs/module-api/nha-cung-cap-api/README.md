# Module API: `suppliers`

**Mô tả:** Nhà cung cấp.

**Mã nguồn Shop:** `artifacts/api-server/src/routes/suppliers.ts`

Nhà cung cấp.

**Số endpoint:** 4

**Contract API:** Mỗi endpoint có mục **URL**, body/query (từ code + schema Zod orval khi có), bảng lỗi `error`, và response (Zod hoặc trường `res.json`).

## Bảng endpoint (tóm tắt)

| Method | Path | Mô tả ngắn |
|--------|------|------------|
| GET | `/suppliers` | Đường dẫn đầy đủ `/api/suppliers` |
| GET | `/suppliers/:id` | Đường dẫn đầy đủ `/api/suppliers/:id` |
| POST | `/suppliers` | Đường dẫn đầy đủ `/api/suppliers`… |
| PATCH | `/suppliers/:id` | Đường dẫn đầy đủ `/api/suppliers/:id`… |

## Chi tiết từng endpoint

### `GET /suppliers` {#get-suppliers}

Đường dẫn đầy đủ `/api/suppliers`. Lớp kiểm tra: `requireAuth`.

**URL:** `GET /api/suppliers`

**Lớp route:** `requireAuth`
- **Thêm trong handler:** role **`super_admin`** (403 nếu không đủ).

**Query:** `limit`, `page`, `q`

**Response 200** — trường top-level (trích `res.json`):

`total`

### `GET /suppliers/:id` {#get-suppliers--id}

Đường dẫn đầy đủ `/api/suppliers/:id`. Lớp kiểm tra: `requireAuth, requireHubShop, requireManagerOrAdmin`.

**URL:** `GET /api/suppliers/:id`

**Lớp route:** `requireAuth`, `requireHubShop`, `requireManagerOrAdmin`

**Lỗi JSON** (`error` string):

| HTTP | Message |
|------|---------|
| **400** | `Invalid ID` |
| **404** | `Không tìm thấy nhà cung cấp` |

### `POST /suppliers` {#post-suppliers}

Đường dẫn đầy đủ `/api/suppliers`. Lớp kiểm tra: `requireAuth, requireHubShop, requireManagerOrAdmin, requireOperationalContext`.

**URL:** `POST /api/suppliers`

**Lớp route:** `requireAuth`, `requireHubShop`, `requireManagerOrAdmin`, `requireOperationalContext`

*Handler không trích được contract tự động — mở file route TypeScript.*

### `PATCH /suppliers/:id` {#patch-suppliers--id}

Đường dẫn đầy đủ `/api/suppliers/:id`. Lớp kiểm tra: `requireAuth, requireHubShop, requireManagerOrAdmin, requireOperationalContext`.

**URL:** `PATCH /api/suppliers/:id`

**Lớp route:** `requireAuth`, `requireHubShop`, `requireManagerOrAdmin`, `requireOperationalContext`

**Lỗi JSON** (`error` string):

| HTTP | Message |
|------|---------|
| **400** | `Invalid ID` |
| **404** | `Không tìm thấy nhà cung cấp` |

## Ghi chú đọc mã

- Gắn prefix `/api` trong `app.ts`; file route: `routes/index.ts` → `./suppliers.ts`.
- Handler đầy đủ: mở file TypeScript tại Shop (tìm theo chuỗi path).
- Quyền role: `tham-chieu/phan-quyen-rbac/README.md` (tiếng Anh gốc) + các `require*` trong từng endpoint.

**Đọc tiếp:** [Hướng dẫn Map](../../huong-dan-doc/) · [Mục lục](../../README.md)
