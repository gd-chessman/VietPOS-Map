# Module API: `auth`

**Mô tả:** Đăng nhập, JWT, PIN, phiên người dùng.

**Mã nguồn Shop:** `artifacts/api-server/src/routes/auth.ts`

Đăng nhập, JWT, PIN, phiên người dùng.

**Số endpoint:** 8

**Contract API:** Mỗi endpoint có mục **URL**, body/query (từ code + schema Zod orval khi có), bảng lỗi `error`, và response (Zod hoặc trường `res.json`).

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

**URL:** `POST /api/auth/login`

**Lớp route:** `requireAuth` (hoặc public — xem route)

**Request body** — schema `LoginBody` (`@workspace/api-zod`):

| Trường | Kiểu (Zod) | Bắt buộc |
|--------|------------|----------|
| `email` | `string()` | **có** |
| `password` | `string()` | **có** |

**Lỗi JSON** (`error` string):

| HTTP | Message |
|------|---------|
| **400** | `Invalid request body` |
| **401** | `Invalid email or password` |

**Response 200** — trường top-level (trích `res.json`):

`message`, `pinChallengeToken`, `pinRequired`, `pinSetupRequired`, `user`

### `GET /auth/me` {#get-auth-me}

Đường dẫn đầy đủ `/api/auth/me`. Lớp kiểm tra: `requireAuth`.

**URL:** `GET /api/auth/me`

**Lớp route:** `requireAuth`

**Lỗi JSON** (`error` string):

| HTTP | Message |
|------|---------|
| **404** | `User not found` |

### `POST /auth/logout` {#post-auth-logout}

Đường dẫn đầy đủ `/api/auth/logout`. Lớp kiểm tra: `requireAuth`.

**URL:** `POST /api/auth/logout`

**Lớp route:** `requireAuth`

**Response 200** — trường top-level (trích `res.json`):

`ok`

### `POST /auth/pin/setup` {#post-auth-pin-setup}

Đường dẫn đầy đủ `/api/auth/pin/setup`. Lớp kiểm tra: `requireAuth (mặc định — xem file)`.

**URL:** `POST /api/auth/pin/setup`

**Lớp route:** `requireAuth` (hoặc public — xem route)

**Request body** (`application/json`, trích từ code):

| Trường | Ghi chú |
|--------|---------|
| `pin` | xem handler |
| `pinChallengeToken` | xem handler |

**Lỗi JSON** (`error` string):

| HTTP | Message |
|------|---------|
| **400** | `Phiên đăng nhập hết hạn — đăng nhập lại bằng email và mật khẩu.` |
| **401** | `Phiên đăng nhập hết hạn — đăng nhập lại bằng email và mật khẩu.` |
| **400** | `Tài khoản đã có mã PIN — dùng đổi PIN trong Quyền của tôi.` |

**Response 200** — trường top-level (trích `res.json`):

`message`

### `POST /auth/pin/device` {#post-auth-pin-device}

Đường dẫn đầy đủ `/api/auth/pin/device`. Lớp kiểm tra: `requireAuth (mặc định — xem file)`.

**URL:** `POST /api/auth/pin/device`

**Lớp route:** `requireAuth` (hoặc public — xem route)

**Request body** (`application/json`, trích từ code):

| Trường | Ghi chú |
|--------|---------|
| `pin` | xem handler |
| `userId` | xem handler |

**Lỗi JSON** (`error` string):

| HTTP | Message |
|------|---------|
| **400** | `Invalid request body` |
| **401** | `Mã PIN không đúng.` |
| **400** | `Chưa thiết lập mã PIN — đăng nhập email/mật khẩu một lần để đặt PIN.` |

**Response 200** — trường top-level (trích `res.json`):

`message`

### `POST /auth/pin/verify` {#post-auth-pin-verify}

Đường dẫn đầy đủ `/api/auth/pin/verify`. Lớp kiểm tra: `requireAuth (mặc định — xem file)`.

**URL:** `POST /api/auth/pin/verify`

**Lớp route:** `requireAuth` (hoặc public — xem route)

**Request body** (`application/json`, trích từ code):

| Trường | Ghi chú |
|--------|---------|
| `pin` | xem handler |
| `pinChallengeToken` | xem handler |

**Lỗi JSON** (`error` string):

| HTTP | Message |
|------|---------|
| **400** | `Phiên đăng nhập hết hạn — đăng nhập lại bằng email và mật khẩu.` |
| **401** | `Phiên đăng nhập hết hạn — đăng nhập lại bằng email và mật khẩu.` |
| **400** | `Tài khoản chưa thiết lập mã PIN.` |
| **401** | `Mã PIN không đúng.` |

**Response 200** — trường top-level (trích `res.json`):

`message`

### `POST /auth/pin/forgot-request` {#post-auth-pin-forgot-request}

Đường dẫn đầy đủ `/api/auth/pin/forgot-request`. Lớp kiểm tra: `requireAuth (mặc định — xem file)`.

**URL:** `POST /api/auth/pin/forgot-request`

**Lớp route:** `requireAuth` (hoặc public — xem route)
- **Thêm trong handler:** role **`super_admin`** (403 nếu không đủ).

**Request body** (`application/json`, trích từ code):

| Trường | Ghi chú |
|--------|---------|
| `email` | xem handler |
| `password` | xem handler |
| `pinChallengeToken` | xem handler |
| `userId` | xem handler |

**Lỗi JSON** (`error` string):

| HTTP | Message |
|------|---------|
| **401** | `Phiên đăng nhập hết hạn — đăng nhập lại bằng email và mật khẩu.` |
| **401** | `Email hoặc mật khẩu không đúng.` |
| **403** | `Tài khoản không hoạt động.` |
| **400** | `Thiếu thông tin xác thực.` |
| **403** | `Quản trị hệ thống không được gửi yêu cầu quên mã PIN qua ứng dụng. Liên hệ vận hành để reset PIN.` |
| **400** | `Tài khoản này không dùng mã PIN.` |

**Response 200** — trường top-level (trích `res.json`):

`created`, `message`, `ok`

## Ghi chú đọc mã

- Gắn prefix `/api` trong `app.ts`; file route: `routes/index.ts` → `./auth.ts`.
- Handler đầy đủ: mở file TypeScript tại Shop (tìm theo chuỗi path).
- Quyền role: `tham-chieu/phan-quyen-rbac/README.md` (tiếng Anh gốc) + các `require*` trong từng endpoint.

**Đọc tiếp:** [Hướng dẫn Map](../../huong-dan-doc/) · [Mục lục](../../README.md)
