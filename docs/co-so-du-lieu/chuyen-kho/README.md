# Schema: `stockTransfers`

**Mô tả:** Drizzle stockTransfers.ts — 2 bảng, 17 cột (stock_transfers, stock_transfer_items).

**Mã nguồn Shop:** `lib/db/src/schema/stockTransfers.ts`

## Cách đọc trang này

Mỗi **bảng Postgres** có bảng cột: kiểu Drizzle, `NOT NULL` / **PK**, khóa ngoại (cột FK → tên bảng đích), và ghi chú JSDoc từ mã nguồn. Enum và index được liệt kê riêng khi có trong file.

## Liên kết nhanh

- **HTTP API:** [chuoi-api](../../module-api/chuoi-api/) (`routes/chain.ts`)

## Bảng `stock_transfers`

- **Biến Drizzle:** `stockTransfersTable`

| Cột SQL | Thuộc tính TS | Kiểu | Ràng buộc | FK → bảng | Ghi chú |
|---------|---------------|------|-----------|-----------|---------|
| `id` | `id` | serial | **PK** | — | — |
| `from_warehouse_id` | `fromWarehouseId` | integer | NOT NULL | `warehouses` | — |
| `to_warehouse_id` | `toWarehouseId` | integer | NOT NULL | `warehouses` | — |
| `requested_by` | `requestedBy` | integer | NOT NULL | `users` | — |
| `approved_by` | `approvedBy` | integer | — | `users` | — |
| `status` | `status` | text | NOT NULL, default `draft` | — | — |
| `note` | `note` | text | — | — | — |
| `created_at` | `createdAt` | timestamp("created_at", { withTimezone: true }) | NOT NULL, default `now()` | — | — |
| `approved_at` | `approvedAt` | timestamp("approved_at", { withTimezone: true }) | — | — | — |
| `shipped_at` | `shippedAt` | timestamp("shipped_at", { withTimezone: true }) | — | — | — |
| `received_at` | `receivedAt` | timestamp("received_at", { withTimezone: true }) | — | — | — |

## Bảng `stock_transfer_items`

- **Biến Drizzle:** `stockTransferItemsTable`

| Cột SQL | Thuộc tính TS | Kiểu | Ràng buộc | FK → bảng | Ghi chú |
|---------|---------------|------|-----------|-----------|---------|
| `id` | `id` | serial | **PK** | — | — |
| `transfer_id` | `transferId` | integer | NOT NULL | `stock_transfers` | — |
| `product_id` | `productId` | integer | NOT NULL | — | — |
| `requested_qty` | `requestedQty` | integer | NOT NULL | — | — |
| `shipped_qty` | `shippedQty` | integer | NOT NULL, default `0` | — | — |
| `received_qty` | `receivedQty` | integer | NOT NULL, default `0` | — | — |

## Kiểu & Zod (insert)

- `insertStockTransferSchema` — `createInsertSchema` (xem file TS)
- `export type InsertStockTransfer`

Tổng quan ER / naming: [../../tham-chieu/co-so-du-lieu-goc/](../../tham-chieu/co-so-du-lieu-goc/).
