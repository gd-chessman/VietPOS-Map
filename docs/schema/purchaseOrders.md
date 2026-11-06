# Schema: `purchaseOrders`

**Mô tả:** Drizzle schema purchaseOrders.ts — 32 cột trên 3 bảng Postgres (purchase_orders, purchase_order_items, purchase_order_logs).

**Source Shop:** `lib/db/src/schema/purchaseOrders.ts`

## Bảng Postgres

- `purchase_orders`
- `purchase_order_items`
- `purchase_order_logs`

## Cột (trích từ schema TS)

- `id` (id)
- `shop_id` (shopId)
- `supplier_id` (supplierId)
- `supplier_name` (supplierName)
- `status` (status)
- `note` (note)
- `code` (code)
- `requested_by` (requestedBy)
- `sent_at` (sentAt)
- `received_at` (receivedAt)
- `cancelled_at` (cancelledAt)
- `cancelled_by` (cancelledBy)
- `cancel_note` (cancelNote)
- `created_at` (createdAt)
- `updated_at` (updatedAt)
- `id` (id)
- `purchase_order_id` (purchaseOrderId)
- `product_id` (productId)
- `product_name` (productName)
- `internal_code` (internalCode)
- `unit` (unit)
- `stock_qty` (stockQty)
- `order_qty` (orderQty)
- `received_qty` (receivedQty)
- `cost_price` (costPrice)
- `note` (note)
- `id` (id)
- `purchase_order_id` (purchaseOrderId)
- `action` (action)
- `user_id` (userId)
- `note` (note)
- `created_at` (createdAt)

## Tham chiếu (references → bảng Drizzle)

- `productsTable`
- `purchaseOrdersTable`
- `shopsTable`
- `suppliersTable`
- `usersTable`

Tổng quan quan hệ: `reference/database.md`.
