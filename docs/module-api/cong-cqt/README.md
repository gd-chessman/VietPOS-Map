# Module API: `org-gdt-portal`

**Mô tả:** Module API org-gdt-portal.ts — 4 endpoint. Session CQT trực tiếp (captcha, connect) — dùng chung org với HĐ đầu vào.

**Mã nguồn Shop:** `artifacts/api-server/src/routes/org-gdt-portal.ts`

Session CQT trực tiếp (captcha, connect) — dùng chung org với HĐ đầu vào.

**Số endpoint:** 4

## Bảng endpoint (tóm tắt)

| Method | Path | Mô tả ngắn |
|--------|------|------------|
| GET | `/organizations/:orgId/gdt/status` | Đường dẫn đầy đủ `/api/organizations/:orgId/gdt/status` |
| POST | `/organizations/:orgId/gdt/captcha` | Đường dẫn đầy đủ `/api/organizations/:orgId/gdt/captcha` |
| POST | `/organizations/:orgId/gdt/test-connect` | Đường dẫn đầy đủ `/api/organizations/:orgId/gdt/test-connect` |
| POST | `/organizations/:orgId/gdt/disconnect` | Đường dẫn đầy đủ `/api/organizations/:orgId/gdt/disconnect` |

## Chi tiết từng endpoint

### `GET /organizations/:orgId/gdt/status` {#get-organizations--orgId-gdt-status}

Đường dẫn đầy đủ `/api/organizations/:orgId/gdt/status`. Lớp kiểm tra: `requireAuth`.

- **Lớp kiểm tra (middleware):** `requireAuth`

### `POST /organizations/:orgId/gdt/captcha` {#post-organizations--orgId-gdt-captcha}

Đường dẫn đầy đủ `/api/organizations/:orgId/gdt/captcha`. Lớp kiểm tra: `requireAuth`.

- **Lớp kiểm tra (middleware):** `requireAuth`

### `POST /organizations/:orgId/gdt/test-connect` {#post-organizations--orgId-gdt-test-connect}

Đường dẫn đầy đủ `/api/organizations/:orgId/gdt/test-connect`. Lớp kiểm tra: `requireAuth`.

- **Lớp kiểm tra (middleware):** `requireAuth`

### `POST /organizations/:orgId/gdt/disconnect` {#post-organizations--orgId-gdt-disconnect}

Đường dẫn đầy đủ `/api/organizations/:orgId/gdt/disconnect`. Lớp kiểm tra: `requireAuth`.

- **Lớp kiểm tra (middleware):** `requireAuth`

## Ghi chú đọc mã

- Gắn prefix `/api` trong `app.ts`; file route: `routes/index.ts` → `./org-gdt-portal.ts`.
- Handler đầy đủ: mở file TypeScript tại Shop (tìm theo chuỗi path).
- Quyền role: `tham-chieu/phan-quyen-rbac/README.md` (tiếng Anh gốc) + các `require*` trong từng endpoint.

**Đọc tiếp:** [Hướng dẫn Map](../../huong-dan-doc/) · [Mục lục](../../README.md)
