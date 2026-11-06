# Module API: `notification-settings`

**Mô tả:** Module API notification-settings.ts — 2 endpoint. Cấu hình thông báo platform/org.

**Mã nguồn Shop:** `artifacts/api-server/src/routes/notification-settings.ts`

Cấu hình thông báo platform/org.

**Số endpoint:** 2

## Bảng endpoint (tóm tắt)

| Method | Path | Mô tả ngắn |
|--------|------|------------|
| GET | `/notification-settings` | Đường dẫn đầy đủ `/api/notification-settings` |
| PATCH | `/notification-settings` | Đường dẫn đầy đủ `/api/notification-settings` |

## Chi tiết từng endpoint

### `GET /notification-settings` {#get-notification-settings}

Đường dẫn đầy đủ `/api/notification-settings`. Lớp kiểm tra: `requireAuth`.

- **Lớp kiểm tra (middleware):** `requireAuth`

### `PATCH /notification-settings` {#patch-notification-settings}

Đường dẫn đầy đủ `/api/notification-settings`. Lớp kiểm tra: `requireAuth`.

- **Lớp kiểm tra (middleware):** `requireAuth`

## Ghi chú đọc mã

- Gắn prefix `/api` trong `app.ts`; file route: `routes/index.ts` → `./notification-settings.ts`.
- Handler đầy đủ: mở file TypeScript tại Shop (tìm theo chuỗi path).
- Quyền role: `tham-chieu/phan-quyen-rbac/README.md` (tiếng Anh gốc) + các `require*` trong từng endpoint.

**Đọc tiếp:** [Hướng dẫn Map](../../huong-dan-doc/) · [Mục lục](../../README.md)
