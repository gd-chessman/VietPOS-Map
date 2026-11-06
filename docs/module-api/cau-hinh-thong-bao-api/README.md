# Module API: `notification-settings`

**Mô tả:** Module API notification-settings.ts — 2 endpoint. Cấu hình thông báo platform/org.

**Mã nguồn Shop:** `artifacts/api-server/src/routes/notification-settings.ts`

Cấu hình thông báo platform/org.

**Số endpoint:** 2

**Contract API:** Mỗi endpoint có mục **URL**, body/query (từ code + schema Zod orval khi có), bảng lỗi `error`, và response (Zod hoặc trường `res.json`).

## Bảng endpoint (tóm tắt)

| Method | Path | Mô tả ngắn |
|--------|------|------------|
| GET | `/notification-settings` | Đường dẫn đầy đủ `/api/notification-settings` |
| PATCH | `/notification-settings` | Đường dẫn đầy đủ `/api/notification-settings` |

## Chi tiết từng endpoint

### `GET /notification-settings` {#get-notification-settings}

Đường dẫn đầy đủ `/api/notification-settings`. Lớp kiểm tra: `requireAuth`.

**URL:** `GET /api/notification-settings`

**Lớp route:** `requireAuth`
- **Thêm trong handler:** role **`super_admin`** (403 nếu không đủ).

**Lỗi JSON** (`error` string):

| HTTP | Message |
|------|---------|
| **500** | `Không tải được cài đặt thông báo. Thử khởi động lại máy chủ và cập nhật cơ sở dữ liệu.` |

**Response 200** — trường top-level (trích `res.json`):

`Chuỗi`, `Email`, `app`, `overview`, `recipientRoleOptions`

### `PATCH /notification-settings` {#patch-notification-settings}

Đường dẫn đầy đủ `/api/notification-settings`. Lớp kiểm tra: `requireAuth`.

**URL:** `PATCH /api/notification-settings`

**Lớp route:** `requireAuth`
- **Thêm trong handler:** role **`super_admin`** (403 nếu không đủ).

**Lỗi JSON** (`error` string):

| HTTP | Message |
|------|---------|
| **400** | `Cần mảng updates` |
| **400** | `Không có cập nhật hợp lệ` |
| **500** | `Không lưu được cài đặt. Thử khởi động lại máy chủ.` |

**Response 200** — trường top-level (trích `res.json`):

`ok`, `recipientRoleOptions`

## Ghi chú đọc mã

- Gắn prefix `/api` trong `app.ts`; file route: `routes/index.ts` → `./notification-settings.ts`.
- Handler đầy đủ: mở file TypeScript tại Shop (tìm theo chuỗi path).
- Quyền role: `tham-chieu/phan-quyen-rbac/README.md` (tiếng Anh gốc) + các `require*` trong từng endpoint.

**Đọc tiếp:** [Hướng dẫn Map](../../huong-dan-doc/) · [Mục lục](../../README.md)
