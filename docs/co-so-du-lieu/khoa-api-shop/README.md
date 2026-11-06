# Schema: `shopApiKeys`

**Mô tả:** Drizzle shopApiKeys.ts — 1 bảng, 9 cột (shop_api_keys).

**Mã nguồn Shop:** `lib/db/src/schema/shopApiKeys.ts`

## Cách đọc trang này

Mỗi **bảng Postgres** có bảng cột: kiểu Drizzle, `NOT NULL` / **PK**, khóa ngoại (cột FK → tên bảng đích), và ghi chú JSDoc từ mã nguồn. Enum và index được liệt kê riêng khi có trong file.

## Liên kết nhanh

- **HTTP API:** [khoa-api-cua-hang](../../module-api/khoa-api-cua-hang/) (`routes/shop-api-keys.ts`)

## Bảng `shop_api_keys`

*Key cấp cho một cửa hàng. Mạch đếm khách gửi api_key để cộng lượt.*

- **Biến Drizzle:** `shopApiKeysTable`

| Cột SQL | Thuộc tính TS | Kiểu | Ràng buộc | FK → bảng | Ghi chú |
|---------|---------------|------|-----------|-----------|---------|
| `id` | `id` | serial | **PK** | — | — |
| `shop_id` | `shopId` | integer | NOT NULL | `shops` | — |
| `label` | `label` | text | — | — | — |
| `count_mode` | `countMode` | text | NOT NULL, default `two_beams_one_guest` | — | — |
| `beam_carry` | `beamCarry` | integer | NOT NULL, default `0` | — | — |
| `beam_carry_visit_date` | `beamCarryVisitDate` | text | — | — | — |
| `api_key` | `apiKey` | text | NOT NULL | — | — |
| `status` | `status` | text | NOT NULL, default `active` | — | — |
| `created_at` | `createdAt` | timestamp("created_at", { withTimezone: true }) | NOT NULL, default `now()` | — | — |

Tổng quan ER / naming: [../../tham-chieu/co-so-du-lieu-goc/](../../tham-chieu/co-so-du-lieu-goc/).
