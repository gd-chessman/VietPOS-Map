# Module API: `notifications`

**Mô tả:** Module API notifications.ts — 2 endpoint. Thông báo in-app cho user.

**Mã nguồn Shop:** `artifacts/api-server/src/routes/notifications.ts`

Thông báo in-app cho user.

**Số endpoint:** 2

## Bảng endpoint (tóm tắt)

| Method | Path | Mô tả ngắn |
|--------|------|------------|
| GET | `/notifications` | Đường dẫn đầy đủ `/api/notifications` |
| POST | `/notifications/read` | Đường dẫn đầy đủ `/api/notifications/read` |

## Chi tiết từng endpoint

### `GET /notifications` {#get-notifications}

Đường dẫn đầy đủ `/api/notifications`. Lớp kiểm tra: `requireAuth`.

- **Lớp kiểm tra (middleware):** `requireAuth`

### `POST /notifications/read` {#post-notifications-read}

Đường dẫn đầy đủ `/api/notifications/read`. Lớp kiểm tra: `requireAuth`.

- **Lớp kiểm tra (middleware):** `requireAuth`

## Ghi chú đọc mã

- Gắn prefix `/api` trong `app.ts`; file route: `routes/index.ts` → `./notifications.ts`.
- Handler đầy đủ: mở file TypeScript tại Shop (tìm theo chuỗi path).
- Quyền role: `tham-chieu/phan-quyen-rbac/README.md` (tiếng Anh gốc) + các `require*` trong từng endpoint.

**Đọc tiếp:** [Hướng dẫn Map](../../huong-dan-doc/) · [Mục lục](../../README.md)
