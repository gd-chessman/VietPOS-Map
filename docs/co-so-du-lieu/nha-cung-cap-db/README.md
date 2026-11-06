# Schema: `suppliers`

**Mô tả:** Drizzle suppliers.ts — 1 bảng, 12 cột, 1 enum, 2 index (suppliers).

**Mã nguồn Shop:** `lib/db/src/schema/suppliers.ts`

## Cách đọc trang này

Mỗi **bảng Postgres** có bảng cột: kiểu Drizzle, `NOT NULL` / **PK**, khóa ngoại (cột FK → tên bảng đích), và ghi chú JSDoc từ mã nguồn. Enum và index được liệt kê riêng khi có trong file.

## Liên kết nhanh

- **HTTP API:** [nha-cung-cap-api](../../module-api/nha-cung-cap-api/) (`routes/suppliers.ts`)
- **Giao diện:** [nha-cung-cap](../../trang/nha-cung-cap/)

## Enum Postgres

### `supplier_status` (`supplierStatusEnum`)

- Giá trị: `["active", "inactive"]`

## Bảng `suppliers`

- **Biến Drizzle:** `suppliersTable`

| Cột SQL | Thuộc tính TS | Kiểu | Ràng buộc | FK → bảng | Ghi chú |
|---------|---------------|------|-----------|-----------|---------|
| `id` | `id` | serial | **PK** | — | — |
| `shop_id` | `shopId` | integer | NOT NULL | `shops` | — |
| `name` | `name` | text | NOT NULL | — | — |
| `phone` | `phone` | text | — | — | — |
| `email` | `email` | text | — | — | — |
| `address` | `address` | text | — | — | — |
| `tax_code` | `taxCode` | text | — | — | — |
| `contact_person` | `contactPerson` | text | — | — | — |
| `notes` | `notes` | text | — | — | — |
| `status` | `status` | enum `supplier_status` | NOT NULL, default `active` | — | — |
| `created_at` | `createdAt` | timestamp("created_at", { withTimezone: true }) | NOT NULL, default `now()` | — | — |
| `updated_at` | `updatedAt` | timestamp("updated_at", { withTimezone: true }) | NOT NULL, default `now()` | — | — |

**Index:**

- `suppliers_shop_status_idx` on `shopId`, `status`
- `suppliers_shop_name_idx` on `shopId`, `name`

## Kiểu & Zod (insert)

- `insertSupplierSchema` — `createInsertSchema` (xem file TS)
- `export type InsertSupplier`
- `export type Supplier`

Tổng quan ER / naming: [../../tham-chieu/co-so-du-lieu-goc/](../../tham-chieu/co-so-du-lieu-goc/).
