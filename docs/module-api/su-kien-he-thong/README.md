# Module API: `system-events`

**Mô tả:** Module API system-events.ts — 1 endpoint. Sự kiện / lỗi hệ thống.

**Mã nguồn Shop:** `artifacts/api-server/src/routes/system-events.ts`

Sự kiện / lỗi hệ thống.

**Số endpoint:** 1

## Bảng endpoint (tóm tắt)

| Method | Path | Mô tả ngắn |
|--------|------|------------|
| GET | `/system-events` | Đường dẫn đầy đủ `/api/system-events` |

## Chi tiết từng endpoint

### `GET /system-events` {#get-system-events}

Đường dẫn đầy đủ `/api/system-events`. Lớp kiểm tra: `requireAuth`.

- **Lớp kiểm tra (middleware):** `requireAuth`

## Ghi chú đọc mã

- Gắn prefix `/api` trong `app.ts`; file route: `routes/index.ts` → `./system-events.ts`.
- Handler đầy đủ: mở file TypeScript tại Shop (tìm theo chuỗi path).
- Quyền role: `tham-chieu/phan-quyen-rbac/README.md` (tiếng Anh gốc) + các `require*` trong từng endpoint.

**Đọc tiếp:** [Hướng dẫn Map](../../huong-dan-doc/) · [Mục lục](../../README.md)
