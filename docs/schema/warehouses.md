# Schema: `warehouses`

**Mô tả:** Drizzle schema warehouses.ts — 7 cột trên 1 bảng Postgres (warehouses).

**Source Shop:** `lib/db/src/schema/warehouses.ts`

## Bảng Postgres

- `warehouses`

## Cột (trích từ schema TS)

- `id` (id)
- `organization_id` (organizationId)
- `shop_id` (shopId)
- `name` (name)
- `warehouse_type` (warehouseType)
- `status` (status)
- `created_at` (createdAt)

## Tham chiếu (references → bảng Drizzle)

- `organizationsTable`
- `shopsTable`

Tổng quan quan hệ: `reference/database.md`.
