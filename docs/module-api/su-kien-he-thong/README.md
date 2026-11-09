# Module API: `system-events`

**Mô tả:** Sự kiện / lỗi hệ thống.

**Mã nguồn Shop:** `artifacts/api-server/src/routes/system-events.ts`

Sự kiện / lỗi hệ thống.

**Số endpoint:** 1

**Contract API:** Mỗi endpoint có mục **URL**, body/query (từ code + schema Zod orval khi có), bảng lỗi `error`, và response (Zod hoặc trường `res.json`).

## Bảng endpoint (tóm tắt)

| Method | Path | Mô tả ngắn |
|--------|------|------------|
| GET | `/system-events` | Đường dẫn đầy đủ `/api/system-events` |

## Chi tiết từng endpoint

### `GET /system-events` {#get-system-events}

Đường dẫn đầy đủ `/api/system-events`. Lớp kiểm tra: `requireAuth`.

**URL:** `GET /api/system-events`

**Lớp route:** `requireAuth`
- **Thêm trong handler:** role **`super_admin`** (403 nếu không đủ).

**Query:** `category`, `from`, `limit`, `page`, `severity`, `shopId`, `to`

**Lỗi JSON** (`error` string):

| HTTP | Message |
|------|---------|
| **403** | `Chỉ super admin mới xem Báo cáo hệ thống` |

## Ghi chú đọc mã

- Gắn prefix `/api` trong `app.ts`; file route: `routes/index.ts` → `./system-events.ts`.
- Handler đầy đủ: mở file TypeScript tại Shop (tìm theo chuỗi path).
- Quyền role: `tham-chieu/phan-quyen-rbac/README.md` (tiếng Anh gốc) + các `require*` trong từng endpoint.

**Đọc tiếp:** [Hướng dẫn Map](../../huong-dan-doc/) · [Mục lục](../../README.md)
