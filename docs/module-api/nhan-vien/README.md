# Module API: `staff`

**Mô tả:** Module API staff.ts — 7 endpoint. Quản lý tài khoản nhân viên (admin).

**Mã nguồn Shop:** `artifacts/api-server/src/routes/staff.ts`

Quản lý tài khoản nhân viên (admin).

**Số endpoint:** 7

## Bảng endpoint (tóm tắt)

| Method | Path | Mô tả ngắn |
|--------|------|------------|
| GET | `/staff` | Đường dẫn đầy đủ `/api/staff` |
| POST | `/staff` | Đường dẫn đầy đủ `/api/staff` |
| PATCH | `/staff/:id` | Đường dẫn đầy đủ `/api/staff/:id` |
| DELETE | `/staff/:id` | Đường dẫn đầy đủ `/api/staff/:id` |
| GET | `/staff/pin-reset-requests` | Đường dẫn đầy đủ `/api/staff/pin-reset-requests` |
| POST | `/staff/pin-reset-requests/:id/resolve` | Đường dẫn đầy đủ `/api/staff/pin-reset-requests/:id/resolve` |
| POST | `/staff/pin-reset-requests/:id/dismiss` | Đường dẫn đầy đủ `/api/staff/pin-reset-requests/:id/dismiss` |

## Chi tiết từng endpoint

### `GET /staff` {#get-staff}

Đường dẫn đầy đủ `/api/staff`. Lớp kiểm tra: `requireAuth`.

- **Lớp kiểm tra (middleware):** `requireAuth`

### `POST /staff` {#post-staff}

Đường dẫn đầy đủ `/api/staff`. Lớp kiểm tra: `requireAuth, requireOperationalContext`.

- **Lớp kiểm tra (middleware):** `requireAuth`, `requireOperationalContext`

### `PATCH /staff/:id` {#patch-staff--id}

Đường dẫn đầy đủ `/api/staff/:id`. Lớp kiểm tra: `requireAuth, requireOperationalContext`.

- **Lớp kiểm tra (middleware):** `requireAuth`, `requireOperationalContext`

### `DELETE /staff/:id` {#delete-staff--id}

Đường dẫn đầy đủ `/api/staff/:id`. Lớp kiểm tra: `requireAuth, requireOperationalContext`.

- **Lớp kiểm tra (middleware):** `requireAuth`, `requireOperationalContext`

### `GET /staff/pin-reset-requests` {#get-staff-pin-reset-requests}

Đường dẫn đầy đủ `/api/staff/pin-reset-requests`. Lớp kiểm tra: `requireAuth`.

- **Lớp kiểm tra (middleware):** `requireAuth`

### `POST /staff/pin-reset-requests/:id/resolve` {#post-staff-pin-reset-requests--id-resolve}

Đường dẫn đầy đủ `/api/staff/pin-reset-requests/:id/resolve`. Lớp kiểm tra: `requireAuth, requireOperationalContext`.

- **Lớp kiểm tra (middleware):** `requireAuth`, `requireOperationalContext`

### `POST /staff/pin-reset-requests/:id/dismiss` {#post-staff-pin-reset-requests--id-dismiss}

Đường dẫn đầy đủ `/api/staff/pin-reset-requests/:id/dismiss`. Lớp kiểm tra: `requireAuth, requireOperationalContext`.

- **Lớp kiểm tra (middleware):** `requireAuth`, `requireOperationalContext`

## Ghi chú đọc mã

- Gắn prefix `/api` trong `app.ts`; file route: `routes/index.ts` → `./staff.ts`.
- Handler đầy đủ: mở file TypeScript tại Shop (tìm theo chuỗi path).
- Quyền role: `tham-chieu/phan-quyen-rbac/README.md` (tiếng Anh gốc) + các `require*` trong từng endpoint.

**Đọc tiếp:** [Hướng dẫn Map](../../huong-dan-doc/) · [Mục lục](../../README.md)
