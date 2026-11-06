# Schema: `vatInboundInvoices`

**Mô tả:** Drizzle vatInboundInvoices.ts — 1 bảng, 55 cột, 3 index (vat_inbound_invoices).

**Mã nguồn Shop:** `lib/db/src/schema/vatInboundInvoices.ts`

## Cách đọc trang này

Mỗi **bảng Postgres** có bảng cột: kiểu Drizzle, `NOT NULL` / **PK**, khóa ngoại (cột FK → tên bảng đích), và ghi chú JSDoc từ mã nguồn. Enum và index được liệt kê riêng khi có trong file.

## Liên kết nhanh

- **HTTP API:** [hoa-don-dau-vao](../../module-api/hoa-don-dau-vao/) (`routes/vat-inbound.ts`)

## Bảng `vat_inbound_invoices`

- **Biến Drizzle:** `vatInboundInvoicesTable`

| Cột SQL | Thuộc tính TS | Kiểu | Ràng buộc | FK → bảng | Ghi chú |
|---------|---------------|------|-----------|-----------|---------|
| `id` | `id` | serial | **PK** | — | — |
| `shop_id` | `shopId` | integer | NOT NULL | `shops` | — |
| `imported_by` | `importedBy` | integer | — | `users` | — |
| `client_id` | `clientId` | text | NOT NULL | — | — |
| `file_name` | `fileName` | text | NOT NULL | — | — |
| `imported_at` | `importedAt` | timestamp("imported_at", { withTimezone: true }) | NOT NULL, default `now()` | — | — |
| `invoice_date` | `invoiceDate` | date | — | — | — |
| `invoice_no` | `invoiceNo` | text | — | — | — |
| `series` | `series` | text | — | — | — |
| `template_no` | `templateNo` | text | — | — | — |
| `form_code` | `formCode` | text | — | — | — |
| `seller_name` | `sellerName` | text | — | — | — |
| `seller_tax_code` | `sellerTaxCode` | text | — | — | — |
| `seller_address` | `sellerAddress` | text | — | — | — |
| `seller_phone` | `sellerPhone` | text | — | — | — |
| `seller_bank` | `sellerBank` | text | — | — | — |
| `buyer_name` | `buyerName` | text | — | — | — |
| `buyer_person_name` | `buyerPersonName` | text | — | — | — |
| `buyer_tax_code` | `buyerTaxCode` | text | — | — | — |
| `buyer_address` | `buyerAddress` | text | — | — | — |
| `buyer_id_card` | `buyerIdCard` | text | — | — | — |
| `buyer_passport` | `buyerPassport` | text | — | — | — |
| `payment_method` | `paymentMethod` | text | — | — | — |
| `currency` | `currency` | text | — | — | — |
| `exchange_rate` | `exchangeRate` | text | — | — | — |
| `amount_untaxed` | `amountUntaxed` | numeric("amount_untaxed", { precision: 14, scale: 2 }) | — | — | — |
| `tax_amount` | `taxAmount` | numeric("tax_amount", { precision: 14, scale: 2 }) | — | — | — |
| `fee_amount` | `feeAmount` | numeric("fee_amount", { precision: 14, scale: 2 }) | — | — | — |
| `commercial_discount` | `commercialDiscount` | numeric("commercial_discount", { precision: 14, scale: 2 }) | — | — | — |
| `total_amount` | `totalAmount` | numeric("total_amount", { precision: 14, scale: 2 }) | — | — | — |
| `amount_in_words` | `amountInWords` | text | — | — | — |
| `tax_authority_code` | `taxAuthorityCode` | text | — | — | — |
| `signed_by` | `signedBy` | text | — | — | — |
| `signed_at` | `signedAt` | text | — | — | — |
| `line_items` | `lineItems` | jsonb | NOT NULL, JSON typed | — | — |
| `tax_breakdown` | `taxBreakdown` | jsonb | NOT NULL, JSON typed | — | — |
| `parse_revision` | `parseRevision` | integer | — | — | — |
| `raw_text` | `rawText` | text | NOT NULL | — | — |
| `pdf_base64` | `pdfBase64` | text | NOT NULL | — | — |
| `purchase_order_id` | `purchaseOrderId` | integer | — | `purchase_orders` | — |
| `stock_status` | `stockStatus` | text | JSON typed | — | — |
| `stock_lines` | `stockLines` | jsonb | JSON typed | — | — |
| `stock_excluded_line_indexes` | `stockExcludedLineIndexes` | jsonb | JSON typed | — | — |
| `stock_excluded_lines_dismissed_at` | `stockExcludedLinesDismissedAt` | timestamp("stock_excluded_lines_dismissed_at", { withTimezone: true }) | — | — | — |
| `undo_dismiss_excluded_request_note` | `undoDismissExcludedRequestNote` | text | — | — | — |
| `undo_dismiss_excluded_requested_by` | `undoDismissExcludedRequestedBy` | integer | — | `users` | — |
| `undo_dismiss_excluded_requested_at` | `undoDismissExcludedRequestedAt` | timestamp("undo_dismiss_excluded_requested_at", { withTimezone: true }) | — | — | — |
| `stock_mapped_at` | `stockMappedAt` | timestamp("stock_mapped_at", { withTimezone: true }) | — | — | — |
| `stock_rollback_note` | `stockRollbackNote` | text | — | — | — |
| `stock_rollback_from_status` | `stockRollbackFromStatus` | text | JSON typed | — | — |
| `stock_rollback_requested_by` | `stockRollbackRequestedBy` | integer | — | `users` | — |
| `stock_rollback_requested_at` | `stockRollbackRequestedAt` | timestamp("stock_rollback_requested_at", { withTimezone: true }) | — | — | — |
| `archived_at` | `archivedAt` | timestamp("archived_at", { withTimezone: true }) | — | — | — |
| `created_at` | `createdAt` | timestamp("created_at", { withTimezone: true }) | NOT NULL, default `now()` | — | — |
| `updated_at` | `updatedAt` | timestamp("updated_at", { withTimezone: true }) | NOT NULL, default `now()` | — | — |

**Index:**

- `vat_inbound_shop_client_uidx` on `shopId`, `clientId`
- UNIQUE `vat_inbound_shop_imported_idx` on `shopId`, `importedAt`
- `vat_inbound_shop_seller_invoice_idx` on `shopId`, `sellerTaxCode`, `series`, `invoiceNo`

## Kiểu & Zod (insert)

- `export type VatInboundLineItem`
- `export type VatInboundTaxRow`
- `export type VatInboundStockLine`
- `export type VatInboundStockStatus`
- `export type VatInboundInvoiceRow`

Tổng quan ER / naming: [../../tham-chieu/co-so-du-lieu-goc/](../../tham-chieu/co-so-du-lieu-goc/).
