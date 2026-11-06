# Schema: `warehouses`

**Mô tả:** Drizzle warehouses.ts — 1 bảng, 7 cột (warehouses).

**Mã nguồn Shop:** `lib/db/src/schema/warehouses.ts`

## Cách đọc trang này

Mỗi **bảng Postgres** có bảng cột: kiểu Drizzle, `NOT NULL` / **PK**, khóa ngoại (cột FK → tên bảng đích), và ghi chú JSDoc từ mã nguồn. Enum và index được liệt kê riêng khi có trong file.

## Liên kết nhanh

- **HTTP API:** [chuoi-api](../../module-api/chuoi-api/) (`routes/chain.ts`)

## Bảng `warehouses`

- **Biến Drizzle:** `warehousesTable`

| Cột SQL | Thuộc tính TS | Kiểu | Ràng buộc | FK → bảng | Ghi chú |
|---------|---------------|------|-----------|-----------|---------|
| `id` | `id` | serial | **PK** | — | — |
| `organization_id` | `organizationId` | integer | NOT NULL | `organizations` | — |
| `shop_id` | `shopId` | integer | — | `shops` | — |
| `name` | `name` | text | NOT NULL | — | — |
| `warehouse_type` | `warehouseType` | text | NOT NULL, default `store_backroom` | — | — |
| `status` | `status` | text | NOT NULL, default `active` | — | — |
| `created_at` | `createdAt` | timestamp("created_at", { withTimezone: true }) | NOT NULL, default `now()` | — | — |

## Kiểu & Zod (insert)

- `insertWarehouseSchema` — `createInsertSchema` (xem file TS)
- `export type InsertWarehouse`
- `export type Warehouse`

Tổng quan ER / naming: [../../tham-chieu/co-so-du-lieu-goc/](../../tham-chieu/co-so-du-lieu-goc/).
