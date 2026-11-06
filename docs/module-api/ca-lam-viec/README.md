# Module API: `shift-sessions`

**Mô tả:** Module API shift-sessions.ts — 3 endpoint. Ca làm việc mở/đóng.

**Mã nguồn Shop:** `artifacts/api-server/src/routes/shift-sessions.ts`

Ca làm việc mở/đóng.

**Số endpoint:** 3

**Contract API:** Mỗi endpoint có mục **URL**, body/query (từ code + schema Zod orval khi có), bảng lỗi `error`, và response (Zod hoặc trường `res.json`).

## Bảng endpoint (tóm tắt)

| Method | Path | Mô tả ngắn |
|--------|------|------------|
| GET | `/shift-sessions/current` | Đường dẫn đầy đủ `/api/shift-sessions/current` |
| POST | `/shift-sessions` | Đường dẫn đầy đủ `/api/shift-sessions` |
| PATCH | `/shift-sessions/:id/end` | Đường dẫn đầy đủ `/api/shift-sessions/:id/end` |

## Chi tiết từng endpoint

### `GET /shift-sessions/current` {#get-shift-sessions-current}

Đường dẫn đầy đủ `/api/shift-sessions/current`. Lớp kiểm tra: `requireAuth`.

**URL:** `GET /api/shift-sessions/current`

**Lớp route:** `requireAuth`

*Handler không trích được contract tự động — mở file route TypeScript.*

### `POST /shift-sessions` {#post-shift-sessions}

Đường dẫn đầy đủ `/api/shift-sessions`. Lớp kiểm tra: `requireAuth, requireDeviceApproval, requireOperationalContext`.

**URL:** `POST /api/shift-sessions`

**Lớp route:** `requireAuth`, `requireDeviceApproval`, `requireOperationalContext`

**Lỗi JSON** (`error` string):

| HTTP | Message |
|------|---------|
| **400** | `Một hoặc nhiều nhân viên không hợp lệ hoặc đã nghỉ việc` |
| **403** | `Đã có phiên ca đang mở. Đăng xuất và đăng nhập lại để chọn NV ca mới.` |
| **500** | `Không thể mở phiên ca` |

### `PATCH /shift-sessions/:id/end` {#patch-shift-sessions--id-end}

Đường dẫn đầy đủ `/api/shift-sessions/:id/end`. Lớp kiểm tra: `requireAuth`.

**URL:** `PATCH /api/shift-sessions/:id/end`

**Lớp route:** `requireAuth`

**Lỗi JSON** (`error` string):

| HTTP | Message |
|------|---------|
| **400** | `Mã phiên ca không hợp lệ` |
| **404** | `Không tìm thấy phiên ca đang mở` |

## Ghi chú đọc mã

- Gắn prefix `/api` trong `app.ts`; file route: `routes/index.ts` → `./shift-sessions.ts`.
- Handler đầy đủ: mở file TypeScript tại Shop (tìm theo chuỗi path).
- Quyền role: `tham-chieu/phan-quyen-rbac/README.md` (tiếng Anh gốc) + các `require*` trong từng endpoint.

**Đọc tiếp:** [Hướng dẫn Map](../../huong-dan-doc/) · [Mục lục](../../README.md)
