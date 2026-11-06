# API module: `auth`

**Mô tả:** File routes auth.ts — 8 endpoint HTTP cho /api/.... REST handlers cho domain auth.

**Source Shop:** `artifacts/api-server/src/routes/auth.ts`

REST handlers cho domain **auth**.

**Số endpoint trong file:** 8

## Danh sách endpoint (tóm tắt)

| Method | Path | Mô tả ngắn |
|--------|------|------------|
| POST | `/auth/login` | `/api/auth/login` |
| GET | `/auth/me` | `/api/auth/me` |
| POST | `/auth/logout` | `/api/auth/logout` |
| POST | `/auth/pin/set` | `/api/auth/pin/set` |
| POST | `/auth/pin/setup` | `/api/auth/pin/setup` |
| POST | `/auth/pin/device` | `/api/auth/pin/device` |
| POST | `/auth/pin/verify` | `/api/auth/pin/verify` |
| POST | `/auth/pin/forgot-request` | `/api/auth/pin/forgot-request` |

## Chi tiết từng endpoint

### `POST /auth/login` {#post-auth-login}

`/api/auth/login`. Middleware: `requireAuth (mặc định — kiểm tra file)`.

### `GET /auth/me` {#get-auth-me}

`/api/auth/me`. Middleware: `requireAuth`.

- **Middleware:** `requireAuth`

### `POST /auth/logout` {#post-auth-logout}

`/api/auth/logout`. Middleware: `requireAuth`.

- **Middleware:** `requireAuth`

### `POST /auth/pin/setup` {#post-auth-pin-setup}

`/api/auth/pin/setup`. Middleware: `requireAuth (mặc định — kiểm tra file)`.

### `POST /auth/pin/device` {#post-auth-pin-device}

`/api/auth/pin/device`. Middleware: `requireAuth (mặc định — kiểm tra file)`.

### `POST /auth/pin/verify` {#post-auth-pin-verify}

`/api/auth/pin/verify`. Middleware: `requireAuth (mặc định — kiểm tra file)`.

### `POST /auth/pin/forgot-request` {#post-auth-pin-forgot-request}

`/api/auth/pin/forgot-request`. Middleware: `requireAuth (mặc định — kiểm tra file)`.

## Ghi chú đọc code

- Mount prefix `/api` qua `app.ts`; file này: `routes/index.ts` → `./auth.ts`.
- Handler đầy đủ: mở file TypeScript tại Shop (search theo path string).
- Quyền role: xem `reference/rbac.md` và middleware trong từng block.
