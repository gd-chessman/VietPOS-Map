# Module API: `sync`

**Mô tả:** Đồng bộ offline IndexedDB ↔ server.

**Mã nguồn Shop:** `artifacts/api-server/src/routes/sync.ts`

API đồng bộ client (kéo/đẩy) cho IndexedDB offline.

**Số endpoint:** 2

**Contract API:** Mỗi endpoint có mục **URL**, body/query (từ code + schema Zod orval khi có), bảng lỗi `error`, và response (Zod hoặc trường `res.json`).

## Bảng endpoint (tóm tắt)

| Method | Path | Mô tả ngắn |
|--------|------|------------|
| GET | `/sync/catalog` | Đường dẫn đầy đủ `/api/sync/catalog` |
| GET | `/sync/shift-orders` | Đường dẫn đầy đủ `/api/sync/shift-orders` |

## Chi tiết từng endpoint

### `GET /sync/catalog` {#get-sync-catalog}

Đường dẫn đầy đủ `/api/sync/catalog`. Lớp kiểm tra: `requireAuth`.

**URL:** `GET /api/sync/catalog`

**Lớp route:** `requireAuth`

**Query:** `since`

**Response 200** — trường top-level (trích `res.json`):

`allowOverselling`, `deletedIds`, `nextSeq`

### `GET /sync/shift-orders` {#get-sync-shift-orders}

Đường dẫn đầy đủ `/api/sync/shift-orders`. Lớp kiểm tra: `requireAuth`.

**URL:** `GET /api/sync/shift-orders`

**Lớp route:** `requireAuth`

**Query:** `shiftSessionId`

**Lỗi JSON** (`error` string):

| HTTP | Message |
|------|---------|
| **400** | `shiftSessionId required` |

## Ghi chú đọc mã

- Gắn prefix `/api` trong `app.ts`; file route: `routes/index.ts` → `./sync.ts`.
- Handler đầy đủ: mở file TypeScript tại Shop (tìm theo chuỗi path).
- Quyền role: `tham-chieu/phan-quyen-rbac/README.md` (tiếng Anh gốc) + các `require*` trong từng endpoint.

**Đọc tiếp:** [Hướng dẫn Map](../../huong-dan-doc/) · [Mục lục](../../README.md)
