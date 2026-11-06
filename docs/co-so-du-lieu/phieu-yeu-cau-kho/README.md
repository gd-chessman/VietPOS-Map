# Schema: `stockRequests`

**Mô tả:** Drizzle schema stockRequests.ts — 32 cột trên 3 bảng Postgres (stock_requests, stock_request_logs, stock_request_items).

**Mã nguồn Shop:** `lib/db/src/schema/stockRequests.ts`

## Bảng Postgres

- `stock_requests`
- `stock_request_logs`
- `stock_request_items`

## Cột (trích từ schema TS)

- `id` (id)
- `shop_id` (shopId)
- `from_shop_id` (fromShopId)
- `to_shop_id` (toShopId)
- `warehouse_id` (warehouseId)
- `request_type` (requestType)
- `status` (status)
- `requested_by` (requestedBy)
- `approved_by` (approvedBy)
- `rejected_by` (rejectedBy)
- `completed_by` (completedBy)
- `cancelled_by` (cancelledBy)
- `reject_note` (rejectNote)
- `cancel_note` (cancelNote)
- `receiver_name` (receiverName)
- `note` (note)
- `created_at` (createdAt)
- `approved_at` (approvedAt)
- `completed_at` (completedAt)
- `cancelled_at` (cancelledAt)
- `id` (id)
- `request_id` (requestId)
- `action` (action)
- `user_id` (userId)
- `note` (note)
- `created_at` (createdAt)
- `id` (id)
- `request_id` (requestId)
- `product_id` (productId)
- `variant_id` (variantId)
- `quantity` (quantity)
- `note` (note)

## Tham chiếu (references → bảng Drizzle)

- `shopsTable`
- `stockRequestsTable`
- `usersTable`
- `warehousesTable`

Tổng quan quan hệ: `tham-chieu/co-so-du-lieu-goc/README.md`.
