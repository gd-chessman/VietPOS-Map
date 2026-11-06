<!-- Mirror: Shop-Manager-System-Offline/docs/database.md -->

# Database schema overview (Postgres + Drizzle)

**Mô tả:** Bản mirror doc Shop docs/database.md — Database schema overview (Postgres + Drizzle).

The DB schema is defined in `lib/db/src/schema/*.ts` using Drizzle ORM for Postgres.

## Core entities

### Organizations

- `organizations`
  - `id`, `code`, `name`, `status`, `created_at`

Represents a “chain/company” that can contain multiple shops.

### Shops

- `shops`
  - `id`, `organization_id?`, `code?`, `name`, `type`, `status`

Represents a retail store/branch. Most operational data is scoped to `shop_id`.

### Users

- `users`
  - `id`, `name?`, `email`, `password`, `role`, `organization_id?`, `shop_id`

Represents an employee account. Login is email/password; authorization uses `role`.

### Products

- `products`
  - `id`, `internal_code?`, `internal_name?`, `vat_name?`, `unit` (default `Cái`), `vat_rate` (default `10`), `material?`, `dimensions?`, `weight?`, `manufacturer?`, `name`, `price`, `cost_price`, `shop_id`, `status`, `thumbnail_url?`

### Order items — VAT snapshots

- `unit_snapshot`, `vat_rate_snapshot` (copied from product at checkout)

### Orders — VAT invoice request (POS)

- `invoice_requested` (`true`/`false` text)
- `buyer_company_name`, `buyer_tax_code`, `buyer_email`, `buyer_address`, `buyer_phone` (nullable; set when invoice requested)

Product master is currently scoped by `shop_id` (each shop owns its catalog row).

### Inventory

- `inventory`
  - `id`, `product_id`, `warehouse_id?`, `shop_id?`, `quantity`
  - uniqueness: `(product_id, warehouse_id)` and `(product_id, shop_id)`

Represents stock levels. The system uses shop-level inventory (rows with `shop_id` and `warehouse_id` NULL) for POS flows.

### Orders

- `orders`
  - `id`, `shop_id`, `user_id`, `total_amount`, `status`, `payment_method`, `cancel_note?`, `cancelled_by?`, `cancelled_at?`, `note?`, `created_at`

### Order items

- `order_items`
  - (line items for each order; quantity, price, notes)

## Warehouse & logistics entities

### Warehouses

- `warehouses`
  - `id`, `organization_id`, `shop_id?`, `name`, `warehouse_type`, `status`, `created_at`

### Inventory movements

- `inventory_movements`
  - `id`, `product_id`, `warehouse_id`, `movement_type`, `quantity_delta`, `reference_type?`, `reference_id?`, `note?`, `created_at`

Used for auditability of warehouse-level adjustments and transfer flows.

### Stock requests (import/export)

- `stock_requests`
  - `id`, `shop_id`, `warehouse_id?`, `request_type`, `status`, `requested_by`, `approved_by?`, `rejected_by?`, `reject_note?`, `note?`, timestamps
- `stock_request_items`
  - `request_id`, `product_id`, `quantity`, `note?`

### Stock transfers

- `stock_transfers`
  - `from_warehouse_id`, `to_warehouse_id`, `requested_by`, `approved_by?`, `status`, timestamps
- `stock_transfer_items`
  - `transfer_id`, `product_id`, `requested_qty`, `shipped_qty`, `received_qty`

## Reporting/audit

- `reprint_logs`: tracks receipt reprint actions by user/order/time.

