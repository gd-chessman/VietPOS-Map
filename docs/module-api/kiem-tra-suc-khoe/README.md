# Module API: `health`

**Mô tả:** Module API health.ts — 1 endpoint. Kiểm tra service còn sống (healthz).

**Mã nguồn Shop:** `artifacts/api-server/src/routes/health.ts`

Kiểm tra service còn sống (`healthz`).

**Số endpoint:** 1

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
