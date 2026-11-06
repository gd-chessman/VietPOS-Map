# Schema: `stockRequests`

**Mô tả:** Drizzle stockRequests.ts — 3 bảng, 32 cột (stock_requests, stock_request_logs, stock_request_items).

**Mã nguồn Shop:** `lib/db/src/schema/stockRequests.ts`

## Cách đọc trang này

Mỗi **bảng Postgres** có bảng cột: kiểu Drizzle, `NOT NULL` / **PK**, khóa ngoại (cột FK → tên bảng đích), và ghi chú JSDoc từ mã nguồn. Enum và index được liệt kê riêng khi có trong file.

## Liên kết nhanh

- **HTTP API:** [phieu-nhap-xuat](../../module-api/phieu-nhap-xuat/) (`routes/stock-requests.ts`)
- **Giao diện:** [phieu-nhap-xuat](../../trang/phieu-nhap-xuat/)

## Bảng `stock_requests`

- **Biến Drizzle:** `stockRequestsTable`

| Cột SQL | Thuộc tính TS | Kiểu | Ràng buộc | FK → bảng | Ghi chú |
|---------|---------------|------|-----------|-----------|---------|
| `id` | `id` | serial | **PK** | — | — |
| `shop_id` | `shopId` | integer | NOT NULL | `shops` | — |
| `from_shop_id` | `fromShopId` | integer | — | `shops` | — |
| `to_shop_id` | `toShopId` | integer | — | `shops` | — |
| `warehouse_id` | `warehouseId` | integer | — | `warehouses` | — |
| `request_type` | `requestType` | text | NOT NULL, default `import` | — | — |
| `status` | `status` | text | NOT NULL, default `pending` | — | — |
| `requested_by` | `requestedBy` | integer | NOT NULL | `users` | — |
| `approved_by` | `approvedBy` | integer | — | `users` | — |
| `rejected_by` | `rejectedBy` | integer | — | `users` | — |
| `completed_by` | `completedBy` | integer | — | `users` | — |
| `cancelled_by` | `cancelledBy` | integer | — | `users` | — |
| `reject_note` | `rejectNote` | text | — | — | — |
| `cancel_note` | `cancelNote` | text | — | — | — |
| `receiver_name` | `receiverName` | text | — | — | — |
| `note` | `note` | text | — | — | — |
| `created_at` | `createdAt` | timestamp("created_at", { withTimezone: true }) | NOT NULL, default `now()` | — | — |
| `approved_at` | `approvedAt` | timestamp("approved_at", { withTimezone: true }) | — | — | — |
| `completed_at` | `completedAt` | timestamp("completed_at", { withTimezone: true }) | — | — | — |
| `cancelled_at` | `cancelledAt` | timestamp("cancelled_at", { withTimezone: true }) | — | — | — |

## Bảng `stock_request_logs`

*Nhật ký thao tác trên phiếu (tạo, duyệt, từ chối, hoàn thành, huỷ).*

- **Biến Drizzle:** `stockRequestLogsTable`

| Cột SQL | Thuộc tính TS | Kiểu | Ràng buộc | FK → bảng | Ghi chú |
|---------|---------------|------|-----------|-----------|---------|
| `id` | `id` | serial | **PK** | — | — |
| `request_id` | `requestId` | integer | NOT NULL | `stock_requests` | — |
| `action` | `action` | text | NOT NULL | — | — |
| `user_id` | `userId` | integer | NOT NULL | `users` | — |
| `note` | `note` | text | — | — | — |
| `created_at` | `createdAt` | timestamp("created_at", { withTimezone: true }) | NOT NULL, default `now()` | — | — |

## Bảng `stock_request_items`

- **Biến Drizzle:** `stockRequestItemsTable`

| Cột SQL | Thuộc tính TS | Kiểu | Ràng buộc | FK → bảng | Ghi chú |
|---------|---------------|------|-----------|-----------|---------|
| `id` | `id` | serial | **PK** | — | — |
| `request_id` | `requestId` | integer | NOT NULL | `stock_requests` | — |
| `product_id` | `productId` | integer | NOT NULL | — | — |
| `variant_id` | `variantId` | integer | — | — | — |
| `quantity` | `quantity` | integer | NOT NULL | — | — |
| `note` | `note` | text | — | — | — |

## Kiểu & Zod (insert)

- `insertStockRequestSchema` — `createInsertSchema` (xem file TS)
- `export type InsertStockRequest`

Tổng quan ER / naming: [../../tham-chieu/co-so-du-lieu-goc/](../../tham-chieu/co-so-du-lieu-goc/).
