# Module API: `widget`

**Mô tả:** Module API widget.ts — 1 endpoint. API phục vụ app Android widget: thống kê quầy (JWT / shop context). Repo: VietPOS-Widget/.

**Mã nguồn Shop:** `artifacts/api-server/src/routes/widget.ts`

API phục vụ app Android widget: thống kê quầy (JWT / shop context).

**Repo:** `VietPOS-Widget/`.

**Số endpoint:** 1

## Bảng endpoint (tóm tắt)

| Method | Path | Mô tả ngắn |
|--------|------|------------|
| GET | `/widget/home` | Đường dẫn đầy đủ `/api/widget/home` |

## Chi tiết từng endpoint

### `GET /widget/home` {#get-widget-home}

Đường dẫn đầy đủ `/api/widget/home`. Lớp kiểm tra: `requireAuth`.

- **Lớp kiểm tra (middleware):** `requireAuth`

## Ghi chú đọc mã

- Gắn prefix `/api` trong `app.ts`; file route: `routes/index.ts` → `./widget.ts`.
- Handler đầy đủ: mở file TypeScript tại Shop (tìm theo chuỗi path).
- Quyền role: `tham-chieu/phan-quyen-rbac/README.md` (tiếng Anh gốc) + các `require*` trong từng endpoint.

**Đọc tiếp:** [Hướng dẫn Map](../../huong-dan-doc/) · [Mục lục](../../README.md)
