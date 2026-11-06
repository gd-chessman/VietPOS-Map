# Module API: `sync`

**Mô tả:** Module API sync.ts — 2 endpoint. API đồng bộ client (kéo/đẩy) cho IndexedDB offline.

**Mã nguồn Shop:** `artifacts/api-server/src/routes/sync.ts`

API đồng bộ client (kéo/đẩy) cho IndexedDB offline.

**Số endpoint:** 2

## Bảng endpoint (tóm tắt)

| Method | Path | Mô tả ngắn |
|--------|------|------------|
| GET | `/sync/catalog` | Đường dẫn đầy đủ `/api/sync/catalog` |
| GET | `/sync/shift-orders` | Đường dẫn đầy đủ `/api/sync/shift-orders` |

## Chi tiết từng endpoint

### `GET /sync/catalog` {#get-sync-catalog}

Đường dẫn đầy đủ `/api/sync/catalog`. Lớp kiểm tra: `requireAuth`.

- **Lớp kiểm tra (middleware):** `requireAuth`

### `GET /sync/shift-orders` {#get-sync-shift-orders}

Đường dẫn đầy đủ `/api/sync/shift-orders`. Lớp kiểm tra: `requireAuth`.

- **Lớp kiểm tra (middleware):** `requireAuth`

## Ghi chú đọc mã

- Gắn prefix `/api` trong `app.ts`; file route: `routes/index.ts` → `./sync.ts`.
- Handler đầy đủ: mở file TypeScript tại Shop (tìm theo chuỗi path).
- Quyền role: `tham-chieu/phan-quyen-rbac/README.md` (tiếng Anh gốc) + các `require*` trong từng endpoint.

**Đọc tiếp:** [Hướng dẫn Map](../../huong-dan-doc/) · [Mục lục](../../README.md)
