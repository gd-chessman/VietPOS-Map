# Module API: `suppliers`

**Mô tả:** Module API suppliers.ts — 4 endpoint. Nhà cung cấp.

**Mã nguồn Shop:** `artifacts/api-server/src/routes/suppliers.ts`

Nhà cung cấp.

**Số endpoint:** 4

## Bảng endpoint (tóm tắt)

| Method | Path | Mô tả ngắn |
|--------|------|------------|
| GET | `/suppliers` | Đường dẫn đầy đủ `/api/suppliers` |
| GET | `/suppliers/:id` | Đường dẫn đầy đủ `/api/suppliers/:id` |
| POST | `/suppliers` | Đường dẫn đầy đủ `/api/suppliers`… |
| PATCH | `/suppliers/:id` | Đường dẫn đầy đủ `/api/suppliers/:id`… |

## Chi tiết từng endpoint

### `GET /suppliers` {#get-suppliers}

Đường dẫn đầy đủ `/api/suppliers`. Lớp kiểm tra: `requireAuth`.

- **Lớp kiểm tra (middleware):** `requireAuth`

### `GET /suppliers/:id` {#get-suppliers--id}

Đường dẫn đầy đủ `/api/suppliers/:id`. Lớp kiểm tra: `requireAuth, requireHubShop, requireManagerOrAdmin`.

- **Lớp kiểm tra (middleware):** `requireAuth`, `requireHubShop`, `requireManagerOrAdmin`

### `POST /suppliers` {#post-suppliers}

Đường dẫn đầy đủ `/api/suppliers`. Lớp kiểm tra: `requireAuth, requireHubShop, requireManagerOrAdmin, requireOperationalContext`.

- **Lớp kiểm tra (middleware):** `requireAuth`, `requireHubShop`, `requireManagerOrAdmin`, `requireOperationalContext`

### `PATCH /suppliers/:id` {#patch-suppliers--id}

Đường dẫn đầy đủ `/api/suppliers/:id`. Lớp kiểm tra: `requireAuth, requireHubShop, requireManagerOrAdmin, requireOperationalContext`.

- **Lớp kiểm tra (middleware):** `requireAuth`, `requireHubShop`, `requireManagerOrAdmin`, `requireOperationalContext`

## Ghi chú đọc mã

- Gắn prefix `/api` trong `app.ts`; file route: `routes/index.ts` → `./suppliers.ts`.
- Handler đầy đủ: mở file TypeScript tại Shop (tìm theo chuỗi path).
- Quyền role: `tham-chieu/phan-quyen-rbac/README.md` (tiếng Anh gốc) + các `require*` trong từng endpoint.

**Đọc tiếp:** [Hướng dẫn Map](../../huong-dan-doc/) · [Mục lục](../../README.md)
