# API module: `org-gdt-portal`

**Mô tả:** File routes org-gdt-portal.ts — 4 endpoint HTTP cho /api/.... Session CQT trực tiếp (captcha, connect) — dùng chung org với HĐ đầu vào.

**Source Shop:** `artifacts/api-server/src/routes/org-gdt-portal.ts`

Session CQT trực tiếp (captcha, connect) — dùng chung org với HĐ đầu vào.

**Số endpoint trong file:** 4

## Danh sách endpoint (tóm tắt)

| Method | Path | Mô tả ngắn |
|--------|------|------------|
| GET | `/organizations/:orgId/gdt/status` | `/api/organizations/:orgId/gdt/status` |
| POST | `/organizations/:orgId/gdt/captcha` | `/api/organizations/:orgId/gdt/captcha` |
| POST | `/organizations/:orgId/gdt/test-connect` | `/api/organizations/:orgId/gdt/test-connect` |
| POST | `/organizations/:orgId/gdt/disconnect` | `/api/organizations/:orgId/gdt/disconnect` |

## Chi tiết từng endpoint

### `GET /organizations/:orgId/gdt/status` {#get-organizations--orgId-gdt-status}

`/api/organizations/:orgId/gdt/status`. Middleware: `requireAuth`.

- **Middleware:** `requireAuth`

### `POST /organizations/:orgId/gdt/captcha` {#post-organizations--orgId-gdt-captcha}

`/api/organizations/:orgId/gdt/captcha`. Middleware: `requireAuth`.

- **Middleware:** `requireAuth`

### `POST /organizations/:orgId/gdt/test-connect` {#post-organizations--orgId-gdt-test-connect}

`/api/organizations/:orgId/gdt/test-connect`. Middleware: `requireAuth`.

- **Middleware:** `requireAuth`

### `POST /organizations/:orgId/gdt/disconnect` {#post-organizations--orgId-gdt-disconnect}

`/api/organizations/:orgId/gdt/disconnect`. Middleware: `requireAuth`.

- **Middleware:** `requireAuth`

## Ghi chú đọc code

- Mount prefix `/api` qua `app.ts`; file này: `routes/index.ts` → `./org-gdt-portal.ts`.
- Handler đầy đủ: mở file TypeScript tại Shop (search theo path string).
- Quyền role: xem `reference/rbac.md` và middleware trong từng block.
