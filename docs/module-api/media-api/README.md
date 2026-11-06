# Module API: `media`

**Mô tả:** Module API media.ts — 1 endpoint. Upload và quản lý file media.

**Mã nguồn Shop:** `artifacts/api-server/src/routes/media.ts`

Upload và quản lý file media.

**Số endpoint:** 1

## Bảng endpoint (tóm tắt)

| Method | Path | Mô tả ngắn |
|--------|------|------------|
| GET | `/media` | Đường dẫn đầy đủ `/api/media` |

## Chi tiết từng endpoint

### `GET /media` {#get-media}

Đường dẫn đầy đủ `/api/media`. Lớp kiểm tra: `requireAuth, requireOperationalContext`.

- **Lớp kiểm tra (middleware):** `requireAuth`, `requireOperationalContext`

## Ghi chú đọc mã

- Gắn prefix `/api` trong `app.ts`; file route: `routes/index.ts` → `./media.ts`.
- Handler đầy đủ: mở file TypeScript tại Shop (tìm theo chuỗi path).
- Quyền role: `tham-chieu/phan-quyen-rbac/README.md` (tiếng Anh gốc) + các `require*` trong từng endpoint.

**Đọc tiếp:** [Hướng dẫn Map](../../huong-dan-doc/) · [Mục lục](../../README.md)
