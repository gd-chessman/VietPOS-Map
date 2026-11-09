# Module API: `inventory`

**Mô tả:** Tồn kho cấp shop (số lượng POS).

**Mã nguồn Shop:** `artifacts/api-server/src/routes/inventory.ts`

Tồn kho cấp shop (số lượng POS).

**Số endpoint:** 2

**Contract API:** Mỗi endpoint có mục **URL**, body/query (từ code + schema Zod orval khi có), bảng lỗi `error`, và response (Zod hoặc trường `res.json`).

## Bảng endpoint (tóm tắt)

| Method | Path | Mô tả ngắn |
|--------|------|------------|
| GET | `/inventory` | Đường dẫn đầy đủ `/api/inventory` |
| PATCH | `/inventory/:productId` | Đường dẫn đầy đủ `/api/inventory/:productId` |

## Chi tiết từng endpoint

### `GET /inventory` {#get-inventory}

Đường dẫn đầy đủ `/api/inventory`. Lớp kiểm tra: `requireAuth`.

**URL:** `GET /api/inventory`

**Lớp route:** `requireAuth`

*Handler không trích được contract tự động — mở file route TypeScript.*

### `PATCH /inventory/:productId` {#patch-inventory--productId}

Đường dẫn đầy đủ `/api/inventory/:productId`. Lớp kiểm tra: `requireAuth, requireOperationalContext`.

**URL:** `PATCH /api/inventory/:productId`

**Lớp route:** `requireAuth`, `requireOperationalContext`
- **Thêm trong handler:** role **`super_admin`** (403 nếu không đủ).

**Request body** — schema `UpdateInventoryBody` (`@workspace/api-zod`):

| Trường | Kiểu (Zod) | Bắt buộc |
|--------|------------|----------|
| `quantity` | `number()` | **có** |

**Lỗi JSON** (`error` string):

| HTTP | Message |
|------|---------|
| **400** | `Invalid product ID` |
| **400** | `Quantity cannot be negative` |
| **403** | `Chỉ quản lý hoặc admin được cập nhật tồn kho` |
| **404** | `Product not found` |

**Response 200** — trường top-level (trích `res.json`):

`costPrice`, `id`, `internalCode`, `price`, `productId`, `productName`, `quantity`, `shopId`, `thumbnailUrl`, `warehouseId`

## Ghi chú đọc mã

- Gắn prefix `/api` trong `app.ts`; file route: `routes/index.ts` → `./inventory.ts`.
- Handler đầy đủ: mở file TypeScript tại Shop (tìm theo chuỗi path).
- Quyền role: `tham-chieu/phan-quyen-rbac/README.md` (tiếng Anh gốc) + các `require*` trong từng endpoint.

**Đọc tiếp:** [Hướng dẫn Map](../../huong-dan-doc/) · [Mục lục](../../README.md)
