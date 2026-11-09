# Module API: `shops`

**Mô tả:** Danh sách shop user được truy cập.

**Mã nguồn Shop:** `artifacts/api-server/src/routes/shops.ts`

Danh sách shop user được truy cập.

**Số endpoint:** 3

**Contract API:** Mỗi endpoint có mục **URL**, body/query (từ code + schema Zod orval khi có), bảng lỗi `error`, và response (Zod hoặc trường `res.json`).

## Bảng endpoint (tóm tắt)

| Method | Path | Mô tả ngắn |
|--------|------|------------|
| GET | `/shops` | Đường dẫn đầy đủ `/api/shops` |
| POST | `/shops/heartbeat` | Đường dẫn đầy đủ `/api/shops/heartbeat` |
| GET | `/shops/operational-events` | Đường dẫn đầy đủ `/api/shops/operational-events` |

## Chi tiết từng endpoint

### `GET /shops` {#get-shops}

Đường dẫn đầy đủ `/api/shops`. Lớp kiểm tra: `requireAuth`.

**URL:** `GET /api/shops`

**Lớp route:** `requireAuth`
- **Thêm trong handler:** role **`super_admin`** (403 nếu không đủ).

**Lỗi JSON** (`error` string):

| HTTP | Message |
|------|---------|
| **403** | `Không có quyền xem danh sách chi nhánh` |

### `POST /shops/heartbeat` {#post-shops-heartbeat}

Đường dẫn đầy đủ `/api/shops/heartbeat`. Lớp kiểm tra: `requireAuth`.

**URL:** `POST /api/shops/heartbeat`

**Lớp route:** `requireAuth`

**Request body** (`application/json`, trích từ code):

| Trường | Ghi chú |
|--------|---------|
| `deviceTime` | xem handler |

**Response 200** — trường top-level (trích `res.json`):

`ok`, `recorded`

### `GET /shops/operational-events` {#get-shops-operational-events}

Đường dẫn đầy đủ `/api/shops/operational-events`. Lớp kiểm tra: `requireAuth`.

**URL:** `GET /api/shops/operational-events`

**Lớp route:** `requireAuth`
- **Thêm trong handler:** role **`super_admin`** (403 nếu không đủ).

**Query:** `from`, `limit`, `page`, `shopId`, `to`

**Lỗi JSON** (`error` string):

| HTTP | Message |
|------|---------|
| **403** | `Không có quyền xem nhật ký trạng thái chi nhánh` |
| **403** | `Không có quyền xem chi nhánh này` |

**Response 200** — trường top-level (trích `res.json`):

`items`, `total`

## Ghi chú đọc mã

- Gắn prefix `/api` trong `app.ts`; file route: `routes/index.ts` → `./shops.ts`.
- Handler đầy đủ: mở file TypeScript tại Shop (tìm theo chuỗi path).
- Quyền role: `tham-chieu/phan-quyen-rbac/README.md` (tiếng Anh gốc) + các `require*` trong từng endpoint.

**Đọc tiếp:** [Hướng dẫn Map](../../huong-dan-doc/) · [Mục lục](../../README.md)
