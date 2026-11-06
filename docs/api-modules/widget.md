# API module: `widget`

**Mô tả:** File routes widget.ts — 1 endpoint HTTP cho /api/.... API phục vụ app Android widget: thống kê quầy (JWT / shop context). Repo: VietPOS-Widget/.

**Source Shop:** `artifacts/api-server/src/routes/widget.ts`

API phục vụ app Android widget: thống kê quầy (JWT / shop context).

**Repo:** `VietPOS-Widget/`.

**Số endpoint trong file:** 1

## Danh sách endpoint (tóm tắt)

| Method | Path | Mô tả ngắn |
|--------|------|------------|
| GET | `/widget/home` | `/api/widget/home` |

## Chi tiết từng endpoint

### `GET /widget/home` {#get-widget-home}

`/api/widget/home`. Middleware: `requireAuth`.

- **Middleware:** `requireAuth`

## Ghi chú đọc code

- Mount prefix `/api` qua `app.ts`; file này: `routes/index.ts` → `./widget.ts`.
- Handler đầy đủ: mở file TypeScript tại Shop (search theo path string).
- Quyền role: xem `reference/rbac.md` và middleware trong từng block.
