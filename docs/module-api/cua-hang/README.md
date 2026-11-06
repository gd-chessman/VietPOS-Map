# Module API: `shops`

**Mô tả:** Module API shops.ts — 3 endpoint. Danh sách shop user được truy cập.

**Mã nguồn Shop:** `artifacts/api-server/src/routes/shops.ts`

Danh sách shop user được truy cập.

**Số endpoint:** 3

## Bảng endpoint (tóm tắt)

| Method | Path | Mô tả ngắn |
|--------|------|------------|
| GET | `/shops` | Đường dẫn đầy đủ `/api/shops` |
| POST | `/shops/heartbeat` | Đường dẫn đầy đủ `/api/shops/heartbeat` |
| GET | `/shops/operational-events` | Đường dẫn đầy đủ `/api/shops/operational-events` |

## Chi tiết từng endpoint

### `GET /shops` {#get-shops}

Đường dẫn đầy đủ `/api/shops`. Lớp kiểm tra: `requireAuth`.

- **Lớp kiểm tra (middleware):** `requireAuth`

### `POST /shops/heartbeat` {#post-shops-heartbeat}

Đường dẫn đầy đủ `/api/shops/heartbeat`. Lớp kiểm tra: `requireAuth`.

- **Lớp kiểm tra (middleware):** `requireAuth`

### `GET /shops/operational-events` {#get-shops-operational-events}

Đường dẫn đầy đủ `/api/shops/operational-events`. Lớp kiểm tra: `requireAuth`.

- **Lớp kiểm tra (middleware):** `requireAuth`

## Ghi chú đọc mã

- Gắn prefix `/api` trong `app.ts`; file route: `routes/index.ts` → `./shops.ts`.
- Handler đầy đủ: mở file TypeScript tại Shop (tìm theo chuỗi path).
- Quyền role: `tham-chieu/phan-quyen-rbac/README.md` (tiếng Anh gốc) + các `require*` trong từng endpoint.

**Đọc tiếp:** [Hướng dẫn Map](../../huong-dan-doc/) · [Mục lục](../../README.md)
