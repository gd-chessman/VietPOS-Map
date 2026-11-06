# API module: `health`

**Mô tả:** File routes health.ts — 1 endpoint HTTP cho /api/.... REST handlers cho domain health.

**Source Shop:** `artifacts/api-server/src/routes/health.ts`

REST handlers cho domain **health**.

**Số endpoint trong file:** 1

## Danh sách endpoint (tóm tắt)

| Method | Path | Mô tả ngắn |
|--------|------|------------|
| GET | `/healthz` | `/api/healthz` |

## Chi tiết từng endpoint

## Ghi chú đọc code

- Mount prefix `/api` qua `app.ts`; file này: `routes/index.ts` → `./health.ts`.
- Handler đầy đủ: mở file TypeScript tại Shop (search theo path string).
- Quyền role: xem `reference/rbac.md` và middleware trong từng block.
