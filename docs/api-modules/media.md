# API module: `media`

**Mô tả:** File routes media.ts — 1 endpoint HTTP cho /api/.... REST handlers cho domain media.

**Source Shop:** `artifacts/api-server/src/routes/media.ts`

REST handlers cho domain **media**.

**Số endpoint trong file:** 1

## Danh sách endpoint (tóm tắt)

| Method | Path | Mô tả ngắn |
|--------|------|------------|
| GET | `/media` | `/api/media` |

## Chi tiết từng endpoint

### `GET /media` {#get-media}

`/api/media`. Middleware: `requireAuth, requireOperationalContext`.

- **Middleware:** `requireAuth`, `requireOperationalContext`

## Ghi chú đọc code

- Mount prefix `/api` qua `app.ts`; file này: `routes/index.ts` → `./media.ts`.
- Handler đầy đủ: mở file TypeScript tại Shop (search theo path string).
- Quyền role: xem `reference/rbac.md` và middleware trong từng block.
