# Schema: `stockTransfers`

**Mô tả:** Drizzle schema stockTransfers.ts — 17 cột trên 2 bảng Postgres (stock_transfers, stock_transfer_items).

**Mã nguồn Shop:** `lib/db/src/schema/stockTransfers.ts`

## Bảng Postgres

- `stock_transfers`
- `stock_transfer_items`

## Cột (trích từ schema TS)

- `id` (id)
- `from_warehouse_id` (fromWarehouseId)
- `to_warehouse_id` (toWarehouseId)
- `requested_by` (requestedBy)
- `approved_by` (approvedBy)
- `status` (status)
- `note` (note)
- `created_at` (createdAt)
- `approved_at` (approvedAt)
- `shipped_at` (shippedAt)
- `received_at` (receivedAt)
- `id` (id)
- `transfer_id` (transferId)
- `product_id` (productId)
- `requested_qty` (requestedQty)
- `shipped_qty` (shippedQty)
- `received_qty` (receivedQty)

## Tham chiếu (references → bảng Drizzle)

- `stockTransfersTable`
- `usersTable`
- `warehousesTable`

Tổng quan quan hệ: `tham-chieu/co-so-du-lieu-goc/README.md`.
