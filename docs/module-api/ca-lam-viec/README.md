# Module API: `shift-sessions`

**Mô tả:** Module API shift-sessions.ts — 3 endpoint. Ca làm việc mở/đóng.

**Mã nguồn Shop:** `artifacts/api-server/src/routes/shift-sessions.ts`

Ca làm việc mở/đóng.

**Số endpoint:** 3

## Bảng endpoint (tóm tắt)

| Method | Path | Mô tả ngắn |
|--------|------|------------|
| GET | `/shift-sessions/current` | Đường dẫn đầy đủ `/api/shift-sessions/current` |
| POST | `/shift-sessions` | Đường dẫn đầy đủ `/api/shift-sessions` |
| PATCH | `/shift-sessions/:id/end` | Đường dẫn đầy đủ `/api/shift-sessions/:id/end` |

## Chi tiết từng endpoint

### `GET /shift-sessions/current` {#get-shift-sessions-current}

Đường dẫn đầy đủ `/api/shift-sessions/current`. Lớp kiểm tra: `requireAuth`.

- **Lớp kiểm tra (middleware):** `requireAuth`

### `POST /shift-sessions` {#post-shift-sessions}

Đường dẫn đầy đủ `/api/shift-sessions`. Lớp kiểm tra: `requireAuth, requireDeviceApproval, requireOperationalContext`.

- **Lớp kiểm tra (middleware):** `requireAuth`, `requireDeviceApproval`, `requireOperationalContext`

### `PATCH /shift-sessions/:id/end` {#patch-shift-sessions--id-end}

Đường dẫn đầy đủ `/api/shift-sessions/:id/end`. Lớp kiểm tra: `requireAuth`.

- **Lớp kiểm tra (middleware):** `requireAuth`

## Ghi chú đọc mã

- Gắn prefix `/api` trong `app.ts`; file route: `routes/index.ts` → `./shift-sessions.ts`.
- Handler đầy đủ: mở file TypeScript tại Shop (tìm theo chuỗi path).
- Quyền role: `tham-chieu/phan-quyen-rbac/README.md` (tiếng Anh gốc) + các `require*` trong từng endpoint.

**Đọc tiếp:** [Hướng dẫn Map](../../huong-dan-doc/) · [Mục lục](../../README.md)
