# Module API: `auth`

**Mô tả:** Module API auth.ts — 8 endpoint. Đăng nhập, JWT, PIN, phiên người dùng.

**Mã nguồn Shop:** `artifacts/api-server/src/routes/auth.ts`

Đăng nhập, JWT, PIN, phiên người dùng.

**Số endpoint:** 8

## Bảng endpoint (tóm tắt)

| Method | Path | Mô tả ngắn |
|--------|------|------------|
| POST | `/auth/login` | Đường dẫn đầy đủ `/api/auth/login` |
| GET | `/auth/me` | Đường dẫn đầy đủ `/api/auth/me` |
| POST | `/auth/logout` | Đường dẫn đầy đủ `/api/auth/logout` |
| POST | `/auth/pin/set` | Đường dẫn đầy đủ `/api/auth/pin/set` |
| POST | `/auth/pin/setup` | Đường dẫn đầy đủ `/api/auth/pin/setup` |
| POST | `/auth/pin/device` | Đường dẫn đầy đủ `/api/auth/pin/device` |
| POST | `/auth/pin/verify` | Đường dẫn đầy đủ `/api/auth/pin/verify` |
| POST | `/auth/pin/forgot-request` | Đường dẫn đầy đủ `/api/auth/pin/forgot-request` |

## Chi tiết từng endpoint

### `POST /auth/login` {#post-auth-login}

Đường dẫn đầy đủ `/api/auth/login`. Lớp kiểm tra: `requireAuth (mặc định — xem file)`.

### `GET /auth/me` {#get-auth-me}

Đường dẫn đầy đủ `/api/auth/me`. Lớp kiểm tra: `requireAuth`.

- **Lớp kiểm tra (middleware):** `requireAuth`

### `POST /auth/logout` {#post-auth-logout}

Đường dẫn đầy đủ `/api/auth/logout`. Lớp kiểm tra: `requireAuth`.

- **Lớp kiểm tra (middleware):** `requireAuth`

### `POST /auth/pin/setup` {#post-auth-pin-setup}

Đường dẫn đầy đủ `/api/auth/pin/setup`. Lớp kiểm tra: `requireAuth (mặc định — xem file)`.

### `POST /auth/pin/device` {#post-auth-pin-device}

Đường dẫn đầy đủ `/api/auth/pin/device`. Lớp kiểm tra: `requireAuth (mặc định — xem file)`.

### `POST /auth/pin/verify` {#post-auth-pin-verify}

Đường dẫn đầy đủ `/api/auth/pin/verify`. Lớp kiểm tra: `requireAuth (mặc định — xem file)`.

### `POST /auth/pin/forgot-request` {#post-auth-pin-forgot-request}

Đường dẫn đầy đủ `/api/auth/pin/forgot-request`. Lớp kiểm tra: `requireAuth (mặc định — xem file)`.

## Ghi chú đọc mã

- Gắn prefix `/api` trong `app.ts`; file route: `routes/index.ts` → `./auth.ts`.
- Handler đầy đủ: mở file TypeScript tại Shop (tìm theo chuỗi path).
- Quyền role: `tham-chieu/phan-quyen-rbac/README.md` (tiếng Anh gốc) + các `require*` trong từng endpoint.

**Đọc tiếp:** [Hướng dẫn Map](../../huong-dan-doc/) · [Mục lục](../../README.md)
