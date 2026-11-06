# Schema: `inventoryMovements`

**Mô tả:** Drizzle schema inventoryMovements.ts — 9 cột trên 1 bảng Postgres (inventory_movements).

**Mã nguồn Shop:** `lib/db/src/schema/inventoryMovements.ts`

## Bảng Postgres

- `inventory_movements`

## Cột (trích từ schema TS)

- `id` (id)
- `product_id` (productId)
- `warehouse_id` (warehouseId)
- `movement_type` (movementType)
- `quantity_delta` (quantityDelta)
- `reference_type` (referenceType)
- `reference_id` (referenceId)
- `note` (note)
- `created_at` (createdAt)

## Tham chiếu (references → bảng Drizzle)

- `warehousesTable`

Tổng quan quan hệ: `tham-chieu/co-so-du-lieu-goc/README.md`.
