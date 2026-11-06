# Module API: `pos-cart-audit`

**Mô tả:** Module API pos-cart-audit.ts — 3 endpoint. Audit thao tác giỏ hàng POS.

**Mã nguồn Shop:** `artifacts/api-server/src/routes/pos-cart-audit.ts`

Audit thao tác giỏ hàng POS.

**Số endpoint:** 3

## Bảng endpoint (tóm tắt)

| Method | Path | Mô tả ngắn |
|--------|------|------------|
| POST | `/pos/cart-audit` | Đường dẫn đầy đủ `/api/pos/cart-audit` |
| GET | `/reports/pos-cart-audit/summary` | Đường dẫn đầy đủ `/api/reports/pos-cart-audit/summary` |
| GET | `/reports/pos-cart-audit` | Đường dẫn đầy đủ `/api/reports/pos-cart-audit` |

## Chi tiết từng endpoint

### `POST /pos/cart-audit` {#post-pos-cart-audit}

Đường dẫn đầy đủ `/api/pos/cart-audit`. Lớp kiểm tra: `requireAuth`.

- **Lớp kiểm tra (middleware):** `requireAuth`

### `GET /reports/pos-cart-audit/summary` {#get-reports-pos-cart-audit-summary}

Đường dẫn đầy đủ `/api/reports/pos-cart-audit/summary`. Lớp kiểm tra: `requireAuth`.

- **Lớp kiểm tra (middleware):** `requireAuth`

### `GET /reports/pos-cart-audit` {#get-reports-pos-cart-audit}

Đường dẫn đầy đủ `/api/reports/pos-cart-audit`. Lớp kiểm tra: `requireAuth`.

- **Lớp kiểm tra (middleware):** `requireAuth`

## Ghi chú đọc mã

- Gắn prefix `/api` trong `app.ts`; file route: `routes/index.ts` → `./pos-cart-audit.ts`.
- Handler đầy đủ: mở file TypeScript tại Shop (tìm theo chuỗi path).
- Quyền role: `tham-chieu/phan-quyen-rbac/README.md` (tiếng Anh gốc) + các `require*` trong từng endpoint.

**Đọc tiếp:** [Hướng dẫn Map](../../huong-dan-doc/) · [Mục lục](../../README.md)
