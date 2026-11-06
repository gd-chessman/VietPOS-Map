# Module API: `sales-staff`

**Mô tả:** Module API sales-staff.ts — 4 endpoint. Nhân viên bán hàng gắn quầy.

**Mã nguồn Shop:** `artifacts/api-server/src/routes/sales-staff.ts`

Nhân viên bán hàng gắn quầy.

**Số endpoint:** 4

## Bảng endpoint (tóm tắt)

| Method | Path | Mô tả ngắn |
|--------|------|------------|
| GET | `/sales-staff` | Đường dẫn đầy đủ `/api/sales-staff` |
| GET | `/sales-staff/:id` | Đường dẫn đầy đủ `/api/sales-staff/:id` |
| POST | `/sales-staff` | Đường dẫn đầy đủ `/api/sales-staff` |
| PATCH | `/sales-staff/:id` | Đường dẫn đầy đủ `/api/sales-staff/:id` |

## Chi tiết từng endpoint

### `GET /sales-staff` {#get-sales-staff}

Đường dẫn đầy đủ `/api/sales-staff`. Lớp kiểm tra: `requireAuth`.

- **Lớp kiểm tra (middleware):** `requireAuth`

### `GET /sales-staff/:id` {#get-sales-staff--id}

Đường dẫn đầy đủ `/api/sales-staff/:id`. Lớp kiểm tra: `requireAuth, requireManagerOrAdmin`.

- **Lớp kiểm tra (middleware):** `requireAuth`, `requireManagerOrAdmin`

### `POST /sales-staff` {#post-sales-staff}

Đường dẫn đầy đủ `/api/sales-staff`. Lớp kiểm tra: `requireAuth, requireManagerOrAdmin, requireOperationalContext`.

- **Lớp kiểm tra (middleware):** `requireAuth`, `requireManagerOrAdmin`, `requireOperationalContext`

### `PATCH /sales-staff/:id` {#patch-sales-staff--id}

Đường dẫn đầy đủ `/api/sales-staff/:id`. Lớp kiểm tra: `requireAuth, requireManagerOrAdmin, requireOperationalContext`.

- **Lớp kiểm tra (middleware):** `requireAuth`, `requireManagerOrAdmin`, `requireOperationalContext`

## Ghi chú đọc mã

- Gắn prefix `/api` trong `app.ts`; file route: `routes/index.ts` → `./sales-staff.ts`.
- Handler đầy đủ: mở file TypeScript tại Shop (tìm theo chuỗi path).
- Quyền role: `tham-chieu/phan-quyen-rbac/README.md` (tiếng Anh gốc) + các `require*` trong từng endpoint.

**Đọc tiếp:** [Hướng dẫn Map](../../huong-dan-doc/) · [Mục lục](../../README.md)
