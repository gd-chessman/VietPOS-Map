# Schema: `purchaseOrders`

**Mô tả:** Drizzle purchaseOrders.ts — 3 bảng, 32 cột, 5 index (purchase_orders, purchase_order_items, purchase_order_logs).

**Mã nguồn Shop:** `lib/db/src/schema/purchaseOrders.ts`

## Cách đọc trang này

Mỗi **bảng Postgres** có bảng cột: kiểu Drizzle, `NOT NULL` / **PK**, khóa ngoại (cột FK → tên bảng đích), và ghi chú JSDoc từ mã nguồn. Enum và index được liệt kê riêng khi có trong file.

## Liên kết nhanh

- **HTTP API:** [dat-hang](../../module-api/dat-hang/) (`routes/purchase-orders.ts`)
- **Giao diện:** [dat-hang](../../trang/dat-hang/)

## Bảng `purchase_orders`

*Trạng thái phiếu đặt hàng: - pending: Chờ gửi - sent: Đã gửi nhà cung cấp (Đặt hàng dừng ở đây) - partial / received / closed_short: trạng thái cũ khi còn nhập kho trên phiếu - cancelled: Đã huỷ*

- **Biến Drizzle:** `purchaseOrdersTable`

| Cột SQL | Thuộc tính TS | Kiểu | Ràng buộc | FK → bảng | Ghi chú |
|---------|---------------|------|-----------|-----------|---------|
| `id` | `id` | serial | **PK** | — | — |
| `shop_id` | `shopId` | integer | NOT NULL | `shops` | — |
| `supplier_id` | `supplierId` | integer | — | `suppliers` | — |
| `supplier_name` | `supplierName` | text | NOT NULL | — | — |
| `status` | `status` | text | NOT NULL, default `pending` | — | — |
| `note` | `note` | text | — | — | — |
| `code` | `code` | text | — | — | — |
| `requested_by` | `requestedBy` | integer | NOT NULL | `users` | — |
| `sent_at` | `sentAt` | timestamp("sent_at", { withTimezone: true }) | — | — | — |
| `received_at` | `receivedAt` | timestamp("received_at", { withTimezone: true }) | — | — | — |
| `cancelled_at` | `cancelledAt` | timestamp("cancelled_at", { withTimezone: true }) | — | — | — |
| `cancelled_by` | `cancelledBy` | integer | — | `users` | — |
| `cancel_note` | `cancelNote` | text | — | — | — |
| `created_at` | `createdAt` | timestamp("created_at", { withTimezone: true }) | NOT NULL, default `now()` | — | — |
| `updated_at` | `updatedAt` | timestamp("updated_at", { withTimezone: true }) | NOT NULL, default `now()` | — | — |

**Index:**

- `purchase_orders_shop_status_idx` on `shopId`, `status`
- `purchase_orders_shop_created_idx` on `shopId`, `createdAt`

## Bảng `purchase_order_items`

- **Biến Drizzle:** `purchaseOrderItemsTable`

| Cột SQL | Thuộc tính TS | Kiểu | Ràng buộc | FK → bảng | Ghi chú |
|---------|---------------|------|-----------|-----------|---------|
| `id` | `id` | serial | **PK** | — | — |
| `purchase_order_id` | `purchaseOrderId` | integer | NOT NULL | `purchase_orders` | — |
| `product_id` | `productId` | integer | — | `products` | — |
| `product_name` | `productName` | text | NOT NULL | — | — |
| `internal_code` | `internalCode` | text | — | — | — |
| `unit` | `unit` | text | — | — | — |
| `stock_qty` | `stockQty` | integer | NOT NULL, default `0` | — | — |
| `order_qty` | `orderQty` | integer | NOT NULL | — | — |
| `received_qty` | `receivedQty` | integer | NOT NULL, default `0` | — | — |
| `cost_price` | `costPrice` | numeric("cost_price", { precision: 14, scale: 2 }) | — | — | — |
| `note` | `note` | text | — | — | — |

**Index:**

- `purchase_order_items_po_idx` on `purchaseOrderId`
- `purchase_order_logs_po_created_idx` on `purchaseOrderId`, `createdAt`

## Bảng `purchase_order_logs`

*Nhật ký thao tác trên phiếu đặt hàng.*

- **Biến Drizzle:** `purchaseOrderLogsTable`

| Cột SQL | Thuộc tính TS | Kiểu | Ràng buộc | FK → bảng | Ghi chú |
|---------|---------------|------|-----------|-----------|---------|
| `id` | `id` | serial | **PK** | — | — |
| `purchase_order_id` | `purchaseOrderId` | integer | NOT NULL | `purchase_orders` | — |
| `action` | `action` | text | NOT NULL | — | — |
| `user_id` | `userId` | integer | NOT NULL | `users` | — |
| `note` | `note` | text | — | — | — |
| `created_at` | `createdAt` | timestamp("created_at", { withTimezone: true }) | NOT NULL, default `now()` | — | — |

**Index:**

- `purchase_order_logs_po_created_idx` on `purchaseOrderId`, `createdAt`

## Kiểu & Zod (insert)

- `export type PurchaseOrder`
- `export type PurchaseOrderItem`
- `export type PurchaseOrderLog`

Tổng quan ER / naming: [../../tham-chieu/co-so-du-lieu-goc/](../../tham-chieu/co-so-du-lieu-goc/).
