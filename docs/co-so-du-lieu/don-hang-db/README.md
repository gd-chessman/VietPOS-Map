# Schema: `orders`

**Mô tả:** Drizzle orders.ts — 1 bảng, 39 cột, 2 enum, 4 index (orders).

**Mã nguồn Shop:** `lib/db/src/schema/orders.ts`

## Cách đọc trang này

Mỗi **bảng Postgres** có bảng cột: kiểu Drizzle, `NOT NULL` / **PK**, khóa ngoại (cột FK → tên bảng đích), và ghi chú JSDoc từ mã nguồn. Enum và index được liệt kê riêng khi có trong file.

## Liên kết nhanh

- **HTTP API:** [don-hang-api](../../module-api/don-hang-api/) (`routes/orders.ts`)
- **Giao diện:** [don-hang](../../trang/don-hang/)

## Enum Postgres

### `order_status` (`orderStatusEnum`)

- Giá trị: `["completed", "cancel_requested", "cancelled", "refunded"]`

### `payment_method` (`paymentMethodEnum`)

- Giá trị: `["cash", "card", "transfer"]`

## Bảng `orders`

- **Biến Drizzle:** `ordersTable`

| Cột SQL | Thuộc tính TS | Kiểu | Ràng buộc | FK → bảng | Ghi chú |
|---------|---------------|------|-----------|-----------|---------|
| `id` | `id` | serial | **PK** | — | — |
| `shop_id` | `shopId` | integer | NOT NULL | `shops` | — |
| `user_id` | `userId` | integer | NOT NULL | `users` | — |
| `shift_session_id` | `shiftSessionId` | integer | — | `shift_sessions` | — |
| `total_amount` | `totalAmount` | numeric("total_amount", { precision: 12, scale: 2 }) | NOT NULL | — | — |
| `status` | `status` | enum `order_status` | NOT NULL, default `completed` | — | — |
| `payment_method` | `paymentMethod` | enum `payment_method` | NOT NULL, default `cash` | — | — |
| `payments` | `payments` | jsonb | JSON typed | — | — |
| `cancel_note` | `cancelNote` | text | — | — | — |
| `cancelled_by` | `cancelledBy` | integer | — | `users` | — |
| `cancelled_at` | `cancelledAt` | timestamp("cancelled_at", { withTimezone: true }) | — | — | — |
| `note` | `note` | text | — | — | — |
| `invoice_requested` | `invoiceRequested` | text | NOT NULL, default `false` | — | — |
| `buyer_company_name` | `buyerCompanyName` | text | — | — | — |
| `buyer_tax_code` | `buyerTaxCode` | text | — | — | — |
| `buyer_email` | `buyerEmail` | text | — | — | — |
| `buyer_address` | `buyerAddress` | text | — | — | — |
| `buyer_phone` | `buyerPhone` | text | — | — | — |
| `invoice_issued_at` | `invoiceIssuedAt` | timestamp("invoice_issued_at", { withTimezone: true }) | — | — | — |
| `invoice_issued_by` | `invoiceIssuedBy` | integer | — | `users` | — |
| `einvoice_transaction_uuid` | `einvoiceTransactionUuid` | text | — | — | — |
| `einvoice_invoice_no` | `einvoiceInvoiceNo` | text | — | — | — |
| `einvoice_transaction_id` | `einvoiceTransactionId` | text | — | — | — |
| `einvoice_reservation_code` | `einvoiceReservationCode` | text | — | — | — |
| `einvoice_code_of_tax` | `einvoiceCodeOfTax` | text | — | — | — |
| `einvoice_issue_error` | `einvoiceIssueError` | text | — | — | — |
| `einvoice_issuing_at` | `einvoiceIssuingAt` | timestamp("einvoice_issuing_at", { withTimezone: true }) | — | — | — |
| `payment_proof_urls` | `paymentProofUrls` | jsonb | JSON typed | — | — |
| `payment_proof_uploaded_by` | `paymentProofUploadedBy` | integer | — | `users` | — |
| `payment_proof_uploaded_at` | `paymentProofUploadedAt` | timestamp("payment_proof_uploaded_at", { withTimezone: true }) | — | — | — |
| `product_proof_urls` | `productProofUrls` | jsonb | JSON typed | — | — |
| `product_proof_uploaded_by` | `productProofUploadedBy` | integer | — | `users` | — |
| `product_proof_uploaded_at` | `productProofUploadedAt` | timestamp("product_proof_uploaded_at", { withTimezone: true }) | — | — | — |
| `shop_sequence` | `shopSequence` | integer | NOT NULL | — | — |
| `invoice_code` | `invoiceCode` | text | — | — | — |
| `invoice_public_token` | `invoicePublicToken` | text | — | — | — |
| `created_at` | `createdAt` | timestamp("created_at", { withTimezone: true }) | NOT NULL, default `now()` | — | — |
| `client_created_at` | `clientCreatedAt` | timestamp("client_created_at", { withTimezone: true }) | — | — | — |
| `version` | `version` | integer | NOT NULL, default `1` | — | — |

**Index:**

- `orders_shop_created_at_idx` on `shopId`, `createdAt`
- `orders_shop_status_created_at_idx` on `shopId`, `status`, `createdAt`
- `orders_shift_session_idx` on `shiftSessionId`
- `orders_invoice_public_token_idx` on `invoicePublicToken`

## Kiểu & Zod (insert)

- `insertOrderSchema` — `createInsertSchema` (xem file TS)
- `export type InsertOrder`
- `export type Order`

Tổng quan ER / naming: [../../tham-chieu/co-so-du-lieu-goc/](../../tham-chieu/co-so-du-lieu-goc/).
