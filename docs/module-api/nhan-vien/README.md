# Module API: `staff`

**Mô tả:** Quản lý tài khoản nhân viên (admin).

**Mã nguồn Shop:** `artifacts/api-server/src/routes/staff.ts`

Quản lý tài khoản nhân viên (admin).

**Số endpoint:** 7

**Contract API:** Mỗi endpoint có mục **URL**, body/query (từ code + schema Zod orval khi có), bảng lỗi `error`, và response (Zod hoặc trường `res.json`).

## Bảng endpoint (tóm tắt)

| Method | Path | Mô tả ngắn |
|--------|------|------------|
| GET | `/staff` | Đường dẫn đầy đủ `/api/staff` |
| POST | `/staff` | Đường dẫn đầy đủ `/api/staff` |
| PATCH | `/staff/:id` | Đường dẫn đầy đủ `/api/staff/:id` |
| DELETE | `/staff/:id` | Đường dẫn đầy đủ `/api/staff/:id` |
| GET | `/staff/pin-reset-requests` | Đường dẫn đầy đủ `/api/staff/pin-reset-requests` |
| POST | `/staff/pin-reset-requests/:id/resolve` | Đường dẫn đầy đủ `/api/staff/pin-reset-requests/:id/resolve` |
| POST | `/staff/pin-reset-requests/:id/dismiss` | Đường dẫn đầy đủ `/api/staff/pin-reset-requests/:id/dismiss` |

## Chi tiết từng endpoint

### `GET /staff` {#get-staff}

Đường dẫn đầy đủ `/api/staff`. Lớp kiểm tra: `requireAuth`.

**URL:** `GET /api/staff`

**Lớp route:** `requireAuth`

**Lỗi JSON** (`error` string):

| HTTP | Message |
|------|---------|
| **403** | `Admin access required` |

### `POST /staff` {#post-staff}

Đường dẫn đầy đủ `/api/staff`. Lớp kiểm tra: `requireAuth, requireOperationalContext`.

**URL:** `POST /api/staff`

**Lớp route:** `requireAuth`, `requireOperationalContext`

**Request body** — schema `CreateStaffBody` (`@workspace/api-zod`):

| Trường | Kiểu (Zod) | Bắt buộc |
|--------|------------|----------|
| `name` | `string()` | không |
| `email` | `string()` | **có** |
| `password` | `string()` | **có** |
| `role` | `string()` | không |

**Lỗi JSON** (`error` string):

| HTTP | Message |
|------|---------|
| **403** | `Admin access required` |
| **403** | `Không có quyền tạo nhân viên cho chi nhánh này` |
| **403** | `Không được phép tạo tài khoản quản trị viên` |
| **403** | `Không được phép tạo tài khoản quản lý` |

### `PATCH /staff/:id` {#patch-staff--id}

Đường dẫn đầy đủ `/api/staff/:id`. Lớp kiểm tra: `requireAuth, requireOperationalContext`.

**URL:** `PATCH /api/staff/:id`

**Lớp route:** `requireAuth`, `requireOperationalContext`
- **Thêm trong handler:** role **`super_admin`** (403 nếu không đủ).

**Request body** — schema `UpdateStaffBody` (`@workspace/api-zod`):

| Trường | Kiểu (Zod) | Bắt buộc |
|--------|------------|----------|
| `name` | `string()` | không |
| `email` | `string()` | không |
| `password` | `string()` | không |
| `role` | `string()` | không |
| `status` | `enum(["active", "on_leave", "resigned"])` | không |

**Lỗi JSON** (`error` string):

| HTTP | Message |
|------|---------|
| **400** | `Invalid ID` |
| **403** | `Admin access required` |
| **400** | `Cannot deactivate yourself` |
| **404** | `Staff not found` |
| **403** | `Không được phép quản lý tài khoản quản lý khác` |
| **400** | `Không thể ngừng hoạt động Admin tổng` |
| **403** | `Không được đổi vai trò quản trị hệ thống` |
| **403** | `Không được phép cấp quyền quản lý` |

### `DELETE /staff/:id` {#delete-staff--id}

Đường dẫn đầy đủ `/api/staff/:id`. Lớp kiểm tra: `requireAuth, requireOperationalContext`.

**URL:** `DELETE /api/staff/:id`

**Lớp route:** `requireAuth`, `requireOperationalContext`
- **Thêm trong handler:** role **`super_admin`** (403 nếu không đủ).

**Lỗi JSON** (`error` string):

| HTTP | Message |
|------|---------|
| **400** | `Invalid ID` |
| **403** | `Admin access required` |
| **400** | `Cannot deactivate yourself` |
| **404** | `Staff not found` |
| **403** | `Không được phép quản lý tài khoản quản lý khác` |
| **400** | `Không thể ngừng hoạt động Admin tổng` |
| **403** | `Không được phép ngừng hoạt động quản trị viên` |

### `GET /staff/pin-reset-requests` {#get-staff-pin-reset-requests}

Đường dẫn đầy đủ `/api/staff/pin-reset-requests`. Lớp kiểm tra: `requireAuth`.

**URL:** `GET /api/staff/pin-reset-requests`

**Lớp route:** `requireAuth`

**Lỗi JSON** (`error` string):

| HTTP | Message |
|------|---------|
| **403** | `Admin access required` |

### `POST /staff/pin-reset-requests/:id/resolve` {#post-staff-pin-reset-requests--id-resolve}

Đường dẫn đầy đủ `/api/staff/pin-reset-requests/:id/resolve`. Lớp kiểm tra: `requireAuth, requireOperationalContext`.

**URL:** `POST /api/staff/pin-reset-requests/:id/resolve`

**Lớp route:** `requireAuth`, `requireOperationalContext`

**Request body** (`application/json`, trích từ code):

| Trường | Ghi chú |
|--------|---------|
| `mode` | xem handler |
| `pin` | xem handler |

**Lỗi JSON** (`error` string):

| HTTP | Message |
|------|---------|
| **403** | `Admin access required` |
| **400** | `Invalid ID` |
| **400** | `mode phải là user_sets hoặc admin_sets_pin` |
| **404** | `Không tìm thấy yêu cầu` |
| **403** | `Không được xử lý yêu cầu của vai trò này` |
| **403** | `Không được phép quản lý tài khoản quản lý khác` |

**Response 200** — trường top-level (trích `res.json`):

`message`, `ok`

### `POST /staff/pin-reset-requests/:id/dismiss` {#post-staff-pin-reset-requests--id-dismiss}

Đường dẫn đầy đủ `/api/staff/pin-reset-requests/:id/dismiss`. Lớp kiểm tra: `requireAuth, requireOperationalContext`.

**URL:** `POST /api/staff/pin-reset-requests/:id/dismiss`

**Lớp route:** `requireAuth`, `requireOperationalContext`

**Lỗi JSON** (`error` string):

| HTTP | Message |
|------|---------|
| **403** | `Admin access required` |
| **400** | `Invalid ID` |
| **404** | `Không tìm thấy yêu cầu` |
| **403** | `Không được xử lý yêu cầu của vai trò này` |
| **403** | `Không được phép quản lý tài khoản quản lý khác` |

**Response 200** — trường top-level (trích `res.json`):

`message`, `ok`

## Ghi chú đọc mã

- Gắn prefix `/api` trong `app.ts`; file route: `routes/index.ts` → `./staff.ts`.
- Handler đầy đủ: mở file TypeScript tại Shop (tìm theo chuỗi path).
- Quyền role: `tham-chieu/phan-quyen-rbac/README.md` (tiếng Anh gốc) + các `require*` trong từng endpoint.

**Đọc tiếp:** [Hướng dẫn Map](../../huong-dan-doc/) · [Mục lục](../../README.md)
