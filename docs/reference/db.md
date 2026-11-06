<!-- Mirror: Shop-Manager-System-Offline/docs/code-tour/db.md -->

# Code tour — DB library (`lib/db`)

**Mô tả:** Bản mirror doc Shop docs/code-tour/db.md — Code tour — DB library (lib/db).

## What this package does

Provides:

- a Postgres connection pool (`pg`)
- Drizzle ORM DB instance (`drizzle`)
- the schema tables/enums used by the API server

## Entry point

File: `src/index.ts`

- Requires `DATABASE_URL`
- Creates a `pg.Pool`
- Exports `db` (Drizzle) and the schema exports for queries

## Schema modules

Schema is defined in `src/schema/*.ts`.

### Organization / shop / user

- `organizations.ts`: chain/company
- `shops.ts`: store/branch
- `users.ts`: employees; includes `user_role` enum:
  - `super_admin`, `admin`, `manager`, `staff`, `accountant`, `warehouse_keeper`

### Products & stock

- `products.ts`: product master (currently scoped to `shop_id`)
- `inventory.ts`: stock levels (unique per `product_id + shop_id` and per `product_id + warehouse_id`)
- `inventoryMovements.ts`: audit log for warehouse stock movements

### POS orders

- `orders.ts`: order header (payment method, status, totals, cancel metadata)
- `orderItems.ts`: order lines

### Internal logistics

- `stockRequests.ts`: import/export requests (approval lifecycle)
- `stockTransfers.ts`: warehouse transfer lifecycle (draft → approve → ship → receive)
- `warehouses.ts`: warehouse definitions

### Audit/reporting

- `reprintLogs.ts`: receipt reprint tracking

## Business invariants to preserve

- `inventory` uniqueness must remain valid for both shop-level and warehouse-level rows.
- Order creation/cancellation in the API relies on shop-level inventory rows (`warehouse_id` NULL).
- Transfer workflows assume two warehouses and a stepwise lifecycle (approve/ship/receive).

