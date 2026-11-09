# Module API: `health`

**Mô tả:** Kiểm tra service còn sống (healthz).

**Mã nguồn Shop:** `artifacts/api-server/src/routes/health.ts`

Kiểm tra service còn sống (`healthz`).

**Số endpoint:** 1

**Contract API:** Mỗi endpoint có mục **URL**, body/query (từ code + schema Zod orval khi có), bảng lỗi `error`, và response (Zod hoặc trường `res.json`).

## Bảng endpoint (tóm tắt)

| Method | Path | Mô tả ngắn |
|--------|------|------------|
| GET | `/healthz` | Đường dẫn đầy đủ `/api/healthz` |

## Chi tiết từng endpoint

## Ghi chú đọc mã

- Gắn prefix `/api` trong `app.ts`; file route: `routes/index.ts` → `./health.ts`.
- Handler đầy đủ: mở file TypeScript tại Shop (tìm theo chuỗi path).
- Quyền role: `tham-chieu/phan-quyen-rbac/README.md` (tiếng Anh gốc) + các `require*` trong từng endpoint.

**Đọc tiếp:** [Hướng dẫn Map](../../huong-dan-doc/) · [Mục lục](../../README.md)
