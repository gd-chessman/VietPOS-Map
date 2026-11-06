# Schema: `orders`

**Mô tả:** Drizzle schema orders.ts — 39 cột trên 1 bảng Postgres (orders).

**Mã nguồn Shop:** `lib/db/src/schema/orders.ts`

## Bảng Postgres

- `orders`

## Cột (trích từ schema TS)

- `id` (id)
- `shop_id` (shopId)
- `user_id` (userId)
- `shift_session_id` (shiftSessionId)
- `total_amount` (totalAmount)
- `status` (status)
- `payment_method` (paymentMethod)
- `payments` (payments)
- `cancel_note` (cancelNote)
- `cancelled_by` (cancelledBy)
- `cancelled_at` (cancelledAt)
- `note` (note)
- `invoice_requested` (invoiceRequested)
- `buyer_company_name` (buyerCompanyName)
- `buyer_tax_code` (buyerTaxCode)
- `buyer_email` (buyerEmail)
- `buyer_address` (buyerAddress)
- `buyer_phone` (buyerPhone)
- `invoice_issued_at` (invoiceIssuedAt)
- `invoice_issued_by` (invoiceIssuedBy)
- `einvoice_transaction_uuid` (einvoiceTransactionUuid)
- `einvoice_invoice_no` (einvoiceInvoiceNo)
- `einvoice_transaction_id` (einvoiceTransactionId)
- `einvoice_reservation_code` (einvoiceReservationCode)
- `einvoice_code_of_tax` (einvoiceCodeOfTax)
- `einvoice_issue_error` (einvoiceIssueError)
- `einvoice_issuing_at` (einvoiceIssuingAt)
- `payment_proof_urls` (paymentProofUrls)
- `payment_proof_uploaded_by` (paymentProofUploadedBy)
- `payment_proof_uploaded_at` (paymentProofUploadedAt)
- `product_proof_urls` (productProofUrls)
- `product_proof_uploaded_by` (productProofUploadedBy)
- `product_proof_uploaded_at` (productProofUploadedAt)
- `shop_sequence` (shopSequence)
- `invoice_code` (invoiceCode)
- `invoice_public_token` (invoicePublicToken)
- `created_at` (createdAt)
- `client_created_at` (clientCreatedAt)
- `version` (version)

## Tham chiếu (references → bảng Drizzle)

- `shiftSessionsTable`
- `shopsTable`
- `usersTable`

Tổng quan quan hệ: `tham-chieu/co-so-du-lieu-goc/README.md`.
