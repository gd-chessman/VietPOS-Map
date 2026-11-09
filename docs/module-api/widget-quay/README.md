# Module API: `widget`

**Mô tả:** API cho app widget Android.

**Mã nguồn Shop:** `artifacts/api-server/src/routes/widget.ts`

API phục vụ app Android widget: thống kê quầy (JWT / shop context).

**Repo:** `VietPOS-Widget/`.

**Số endpoint:** 1

**Contract API:** Mỗi endpoint có mục **URL**, body/query (từ code + schema Zod orval khi có), bảng lỗi `error`, và response (Zod hoặc trường `res.json`).

## Bảng endpoint (tóm tắt)

| Method | Path | Mô tả ngắn |
|--------|------|------------|
| GET | `/widget/home` | Đường dẫn đầy đủ `/api/widget/home` |

## Chi tiết từng endpoint

### `GET /widget/home` {#get-widget-home}

Đường dẫn đầy đủ `/api/widget/home`. Lớp kiểm tra: `requireAuth`.

**URL:** `GET /api/widget/home`

**Lớp route:** `requireAuth`

*Handler không trích được contract tự động — mở file route TypeScript.*

## Ghi chú đọc mã

- Gắn prefix `/api` trong `app.ts`; file route: `routes/index.ts` → `./widget.ts`.
- Handler đầy đủ: mở file TypeScript tại Shop (tìm theo chuỗi path).
- Quyền role: `tham-chieu/phan-quyen-rbac/README.md` (tiếng Anh gốc) + các `require*` trong từng endpoint.

**Đọc tiếp:** [Hướng dẫn Map](../../huong-dan-doc/) · [Mục lục](../../README.md)
