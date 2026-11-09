# Module API: `media`

**Mô tả:** Upload và quản lý file media.

**Mã nguồn Shop:** `artifacts/api-server/src/routes/media.ts`

Upload và quản lý file media.

**Số endpoint:** 1

**Contract API:** Mỗi endpoint có mục **URL**, body/query (từ code + schema Zod orval khi có), bảng lỗi `error`, và response (Zod hoặc trường `res.json`).

## Bảng endpoint (tóm tắt)

| Method | Path | Mô tả ngắn |
|--------|------|------------|
| GET | `/media` | Đường dẫn đầy đủ `/api/media` |

## Chi tiết từng endpoint

### `GET /media` {#get-media}

Đường dẫn đầy đủ `/api/media`. Lớp kiểm tra: `requireAuth, requireOperationalContext`.

**URL:** `GET /api/media`

**Lớp route:** `requireAuth`, `requireOperationalContext`
- **Thêm trong handler:** role **`super_admin`** (403 nếu không đủ).

**Query:** `category`, `from`, `limit`, `manufacturer`, `orderId`, `page`, `q`, `shopId`, `to`, `type`

**Lỗi JSON** (`error` string):

| HTTP | Message |
|------|---------|
| **403** | `Không có quyền xem thư viện ảnh` |
| **403** | `Không có quyền xem cửa hàng này` |
| **500** | `Không tải được thư viện ảnh` |

**Response 200** — trường top-level (trích `res.json`):

`categories`, `filterShopId`, `items`, `manufacturers`, `shops`, `total`

## Ghi chú đọc mã

- Gắn prefix `/api` trong `app.ts`; file route: `routes/index.ts` → `./media.ts`.
- Handler đầy đủ: mở file TypeScript tại Shop (tìm theo chuỗi path).
- Quyền role: `tham-chieu/phan-quyen-rbac/README.md` (tiếng Anh gốc) + các `require*` trong từng endpoint.

**Đọc tiếp:** [Hướng dẫn Map](../../huong-dan-doc/) · [Mục lục](../../README.md)
