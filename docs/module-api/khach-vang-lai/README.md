# Module API: `walk-in-customers`

**Mô tả:** Module API walk-in-customers.ts — 2 endpoint. Khách vãng lai (walk-in).

**Mã nguồn Shop:** `artifacts/api-server/src/routes/walk-in-customers.ts`

Khách vãng lai (walk-in).

**Số endpoint:** 2

## Bảng endpoint (tóm tắt)

| Method | Path | Mô tả ngắn |
|--------|------|------------|
| GET | `/shops/:shopId/walk-in-customers/today` | Đường dẫn đầy đủ `/api/shops/:shopId/walk-in-customers/today` |
| POST | `/shops/:shopId/walk-in-customers` | Đường dẫn đầy đủ `/api/shops/:shopId/walk-in-customers` |

## Chi tiết từng endpoint

### `GET /shops/:shopId/walk-in-customers/today` {#get-shops--shopId-walk-in-customers-today}

Đường dẫn đầy đủ `/api/shops/:shopId/walk-in-customers/today`. Lớp kiểm tra: `requireAuth`.

- **Lớp kiểm tra (middleware):** `requireAuth`

### `POST /shops/:shopId/walk-in-customers` {#post-shops--shopId-walk-in-customers}

Đường dẫn đầy đủ `/api/shops/:shopId/walk-in-customers`. Lớp kiểm tra: `requireAuth, requireOperationalContext`.

- **Lớp kiểm tra (middleware):** `requireAuth`, `requireOperationalContext`

## Ghi chú đọc mã

- Gắn prefix `/api` trong `app.ts`; file route: `routes/index.ts` → `./walk-in-customers.ts`.
- Handler đầy đủ: mở file TypeScript tại Shop (tìm theo chuỗi path).
- Quyền role: `tham-chieu/phan-quyen-rbac/README.md` (tiếng Anh gốc) + các `require*` trong từng endpoint.

**Đọc tiếp:** [Hướng dẫn Map](../../huong-dan-doc/) · [Mục lục](../../README.md)
