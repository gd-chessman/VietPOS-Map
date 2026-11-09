# Module API: `notifications`

**Mô tả:** Thông báo in-app cho user.

**Mã nguồn Shop:** `artifacts/api-server/src/routes/notifications.ts`

Thông báo in-app cho user.

**Số endpoint:** 2

**Contract API:** Mỗi endpoint có mục **URL**, body/query (từ code + schema Zod orval khi có), bảng lỗi `error`, và response (Zod hoặc trường `res.json`).

## Bảng endpoint (tóm tắt)

| Method | Path | Mô tả ngắn |
|--------|------|------------|
| GET | `/notifications` | Đường dẫn đầy đủ `/api/notifications` |
| POST | `/notifications/read` | Đường dẫn đầy đủ `/api/notifications/read` |

## Chi tiết từng endpoint

### `GET /notifications` {#get-notifications}

Đường dẫn đầy đủ `/api/notifications`. Lớp kiểm tra: `requireAuth`.

**URL:** `GET /api/notifications`

**Lớp route:** `requireAuth`

**Query:** `limit`, `page`, `type`, `unreadOnly`

**Response 200** — trường top-level (trích `res.json`):

`body`, `createdAt`, `href`, `id`, `items`, `notificationKey`, `readAt`, `severity`, `shopCode`, `shopId`, `title`, `total`, `type`, `unreadCount`

### `POST /notifications/read` {#post-notifications-read}

Đường dẫn đầy đủ `/api/notifications/read`. Lớp kiểm tra: `requireAuth`.

**URL:** `POST /api/notifications/read`

**Lớp route:** `requireAuth`

**Lỗi JSON** (`error` string):

| HTTP | Message |
|------|---------|
| **400** | `Cần ids hoặc all: true` |

**Response 200** — trường top-level (trích `res.json`):

`all`, `ok`

## Ghi chú đọc mã

- Gắn prefix `/api` trong `app.ts`; file route: `routes/index.ts` → `./notifications.ts`.
- Handler đầy đủ: mở file TypeScript tại Shop (tìm theo chuỗi path).
- Quyền role: `tham-chieu/phan-quyen-rbac/README.md` (tiếng Anh gốc) + các `require*` trong từng endpoint.

**Đọc tiếp:** [Hướng dẫn Map](../../huong-dan-doc/) · [Mục lục](../../README.md)
