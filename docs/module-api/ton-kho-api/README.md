# Module API: `inventory`

**Mô tả:** Module API inventory.ts — 2 endpoint. Tồn kho cấp shop (số lượng POS).

**Mã nguồn Shop:** `artifacts/api-server/src/routes/inventory.ts`

Tồn kho cấp shop (số lượng POS).

**Số endpoint:** 2

## Bảng endpoint (tóm tắt)

| Method | Path | Mô tả ngắn |
|--------|------|------------|
| GET | `/inventory` | Đường dẫn đầy đủ `/api/inventory` |
| PATCH | `/inventory/:productId` | Đường dẫn đầy đủ `/api/inventory/:productId` |

## Chi tiết từng endpoint

### `GET /inventory` {#get-inventory}

Đường dẫn đầy đủ `/api/inventory`. Lớp kiểm tra: `requireAuth`.

- **Lớp kiểm tra (middleware):** `requireAuth`

### `PATCH /inventory/:productId` {#patch-inventory--productId}

Đường dẫn đầy đủ `/api/inventory/:productId`. Lớp kiểm tra: `requireAuth, requireOperationalContext`.

- **Lớp kiểm tra (middleware):** `requireAuth`, `requireOperationalContext`

## Ghi chú đọc mã

- Gắn prefix `/api` trong `app.ts`; file route: `routes/index.ts` → `./inventory.ts`.
- Handler đầy đủ: mở file TypeScript tại Shop (tìm theo chuỗi path).
- Quyền role: `tham-chieu/phan-quyen-rbac/README.md` (tiếng Anh gốc) + các `require*` trong từng endpoint.

**Đọc tiếp:** [Hướng dẫn Map](../../huong-dan-doc/) · [Mục lục](../../README.md)
