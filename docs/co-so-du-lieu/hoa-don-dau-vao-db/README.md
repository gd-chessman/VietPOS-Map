# Schema: `vatInboundInvoices`

**Mô tả:** Drizzle schema vatInboundInvoices.ts — 55 cột trên 1 bảng Postgres (vat_inbound_invoices).

**Mã nguồn Shop:** `lib/db/src/schema/vatInboundInvoices.ts`

## Bảng Postgres

- `vat_inbound_invoices`

## Cột (trích từ schema TS)

- `id` (id)
- `shop_id` (shopId)
- `imported_by` (importedBy)
- `client_id` (clientId)
- `file_name` (fileName)
- `imported_at` (importedAt)
- `invoice_date` (invoiceDate)
- `invoice_no` (invoiceNo)
- `series` (series)
- `template_no` (templateNo)
- `form_code` (formCode)
- `seller_name` (sellerName)
- `seller_tax_code` (sellerTaxCode)
- `seller_address` (sellerAddress)
- `seller_phone` (sellerPhone)
- `seller_bank` (sellerBank)
- `buyer_name` (buyerName)
- `buyer_person_name` (buyerPersonName)
- `buyer_tax_code` (buyerTaxCode)
- `buyer_address` (buyerAddress)
- `buyer_id_card` (buyerIdCard)
- `buyer_passport` (buyerPassport)
- `payment_method` (paymentMethod)
- `currency` (currency)
- `exchange_rate` (exchangeRate)
- `amount_untaxed` (amountUntaxed)
- `tax_amount` (taxAmount)
- `fee_amount` (feeAmount)
- `commercial_discount` (commercialDiscount)
- `total_amount` (totalAmount)
- `amount_in_words` (amountInWords)
- `tax_authority_code` (taxAuthorityCode)
- `signed_by` (signedBy)
- `signed_at` (signedAt)
- `line_items` (lineItems)
- `tax_breakdown` (taxBreakdown)
- `parse_revision` (parseRevision)
- `raw_text` (rawText)
- `pdf_base64` (pdfBase64)
- `purchase_order_id` (purchaseOrderId)
- `stock_status` (stockStatus)
- `stock_lines` (stockLines)
- `stock_excluded_line_indexes` (stockExcludedLineIndexes)
- `stock_excluded_lines_dismissed_at` (stockExcludedLinesDismissedAt)
- `undo_dismiss_excluded_request_note` (undoDismissExcludedRequestNote)
- `undo_dismiss_excluded_requested_by` (undoDismissExcludedRequestedBy)
- `undo_dismiss_excluded_requested_at` (undoDismissExcludedRequestedAt)
- `stock_mapped_at` (stockMappedAt)
- `stock_rollback_note` (stockRollbackNote)
- `stock_rollback_from_status` (stockRollbackFromStatus)
- `stock_rollback_requested_by` (stockRollbackRequestedBy)
- `stock_rollback_requested_at` (stockRollbackRequestedAt)
- `archived_at` (archivedAt)
- `created_at` (createdAt)
- `updated_at` (updatedAt)

## Tham chiếu (references → bảng Drizzle)

- `purchaseOrdersTable`
- `shopsTable`
- `usersTable`

Tổng quan quan hệ: `tham-chieu/co-so-du-lieu-goc/README.md`.
