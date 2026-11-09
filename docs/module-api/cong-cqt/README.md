# Module API: `org-gdt-portal`

**Mô tả:** Phiên đăng nhập CQT (captcha).

**Mã nguồn Shop:** `artifacts/api-server/src/routes/org-gdt-portal.ts`

Session CQT trực tiếp (captcha, connect) — dùng chung org với HĐ đầu vào.

**Số endpoint:** 4

**Contract API:** Mỗi endpoint có mục **URL**, body/query (từ code + schema Zod orval khi có), bảng lỗi `error`, và response (Zod hoặc trường `res.json`).

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

**URL:** `GET /api/organizations/:orgId/gdt/status`

**Lớp route:** `requireAuth`

**Path params:** `orgId`

**Response 200** — trường top-level (trích `res.json`):

`ok`

### `POST /organizations/:orgId/gdt/captcha` {#post-organizations--orgId-gdt-captcha}

Đường dẫn đầy đủ `/api/organizations/:orgId/gdt/captcha`. Lớp kiểm tra: `requireAuth`.

**URL:** `POST /api/organizations/:orgId/gdt/captcha`

**Lớp route:** `requireAuth`

**Path params:** `orgId`

**Response 200** — trường top-level (trích `res.json`):

`ok`

### `POST /organizations/:orgId/gdt/test-connect` {#post-organizations--orgId-gdt-test-connect}

Đường dẫn đầy đủ `/api/organizations/:orgId/gdt/test-connect`. Lớp kiểm tra: `requireAuth`.

**URL:** `POST /api/organizations/:orgId/gdt/test-connect`

**Lớp route:** `requireAuth`

**Path params:** `orgId`

**Lỗi JSON** (`error` string):

| HTTP | Message |
|------|---------|
| **400** | `Nhập mã captcha` |

**Response 200** — trường top-level (trích `res.json`):

`message`, `ok`, `probeWarning`, `sampleCount`, `session`

### `POST /organizations/:orgId/gdt/disconnect` {#post-organizations--orgId-gdt-disconnect}

Đường dẫn đầy đủ `/api/organizations/:orgId/gdt/disconnect`. Lớp kiểm tra: `requireAuth`.

**URL:** `POST /api/organizations/:orgId/gdt/disconnect`

**Lớp route:** `requireAuth`

**Path params:** `orgId`

**Response 200** — trường top-level (trích `res.json`):

`ok`

## Ghi chú đọc mã

- Gắn prefix `/api` trong `app.ts`; file route: `routes/index.ts` → `./org-gdt-portal.ts`.
- Handler đầy đủ: mở file TypeScript tại Shop (tìm theo chuỗi path).
- Quyền role: `tham-chieu/phan-quyen-rbac/README.md` (tiếng Anh gốc) + các `require*` trong từng endpoint.

**Đọc tiếp:** [Hướng dẫn Map](../../huong-dan-doc/) · [Mục lục](../../README.md)
