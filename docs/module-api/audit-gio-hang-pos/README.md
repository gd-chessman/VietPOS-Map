# Module API: `pos-cart-audit`

**Mô tả:** Audit thao tác giỏ hàng POS.

**Mã nguồn Shop:** `artifacts/api-server/src/routes/pos-cart-audit.ts`

Audit thao tác giỏ hàng POS.

**Số endpoint:** 3

**Contract API:** Mỗi endpoint có mục **URL**, body/query (từ code + schema Zod orval khi có), bảng lỗi `error`, và response (Zod hoặc trường `res.json`).

## Bảng endpoint (tóm tắt)

| Method | Path | Mô tả ngắn |
|--------|------|------------|
| POST | `/pos/cart-audit` | Đường dẫn đầy đủ `/api/pos/cart-audit` |
| GET | `/reports/pos-cart-audit/summary` | Đường dẫn đầy đủ `/api/reports/pos-cart-audit/summary` |
| GET | `/reports/pos-cart-audit` | Đường dẫn đầy đủ `/api/reports/pos-cart-audit` |

## Chi tiết từng endpoint

### `POST /pos/cart-audit` {#post-pos-cart-audit}

Đường dẫn đầy đủ `/api/pos/cart-audit`. Lớp kiểm tra: `requireAuth`.

**URL:** `POST /api/pos/cart-audit`

**Lớp route:** `requireAuth`

**Lỗi JSON** (`error` string):

| HTTP | Message |
|------|---------|
| **400** | `No events provided` |
| **400** | `orderId not found for cart_checkout` |
| **403** | `Forbidden` |

**Response 201** — trường top-level (trích `res.json`):

`count`, `ok`

### `GET /reports/pos-cart-audit/summary` {#get-reports-pos-cart-audit-summary}

Đường dẫn đầy đủ `/api/reports/pos-cart-audit/summary`. Lớp kiểm tra: `requireAuth`.

**URL:** `GET /api/reports/pos-cart-audit/summary`

**Lớp route:** `requireAuth`

**Query:** `shopId`

**Lỗi JSON** (`error` string):

| HTTP | Message |
|------|---------|
| **403** | `Không có quyền xem chi nhánh này` |

**Response 200** — trường top-level (trích `res.json`):

`clearedValueTotal`, `totalEvents`

### `GET /reports/pos-cart-audit` {#get-reports-pos-cart-audit}

Đường dẫn đầy đủ `/api/reports/pos-cart-audit`. Lớp kiểm tra: `requireAuth`.

**URL:** `GET /api/reports/pos-cart-audit`

**Lớp route:** `requireAuth`

**Query:** `shopId`

**Lỗi JSON** (`error` string):

| HTTP | Message |
|------|---------|
| **403** | `Không có quyền xem chi nhánh này` |

## Ghi chú đọc mã

- Gắn prefix `/api` trong `app.ts`; file route: `routes/index.ts` → `./pos-cart-audit.ts`.
- Handler đầy đủ: mở file TypeScript tại Shop (tìm theo chuỗi path).
- Quyền role: `tham-chieu/phan-quyen-rbac/README.md` (tiếng Anh gốc) + các `require*` trong từng endpoint.

**Đọc tiếp:** [Hướng dẫn Map](../../huong-dan-doc/) · [Mục lục](../../README.md)
