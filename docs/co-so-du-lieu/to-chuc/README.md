# Schema: `organizations`

**Mô tả:** Drizzle organizations.ts — 1 bảng, 39 cột (organizations).

**Mã nguồn Shop:** `lib/db/src/schema/organizations.ts`

## Cách đọc trang này

Mỗi **bảng Postgres** có bảng cột: kiểu Drizzle, `NOT NULL` / **PK**, khóa ngoại (cột FK → tên bảng đích), và ghi chú JSDoc từ mã nguồn. Enum và index được liệt kê riêng khi có trong file.

## Bảng `organizations`

- **Biến Drizzle:** `organizationsTable`

| Cột SQL | Thuộc tính TS | Kiểu | Ràng buộc | FK → bảng | Ghi chú |
|---------|---------------|------|-----------|-----------|---------|
| `id` | `id` | serial | **PK** | — | — |
| `code` | `code` | text | NOT NULL | — | — |
| `name` | `name` | text | NOT NULL | — | — |
| `tax_code` | `taxCode` | text | — | — | — |
| `address` | `address` | text | — | — | — |
| `phone` | `phone` | text | — | — | — |
| `email` | `email` | text | — | — | — |
| `bank_name` | `bankName` | text | — | — | — |
| `bank_account` | `bankAccount` | text | — | — | — |
| `bank_account_name` | `bankAccountName` | text | — | — | — |
| `status` | `status` | text | NOT NULL, default `active` | — | — |
| `public_base_url` | `publicBaseUrl` | text | — | — | — |
| `viettel_invoice_api_url` | `viettelInvoiceApiUrl` | text | — | — | — |
| `viettel_invoice_auth_url` | `viettelInvoiceAuthUrl` | text | — | — | — |
| `viettel_invoice_username` | `viettelInvoiceUsername` | text | — | — | — |
| `viettel_invoice_password` | `viettelInvoicePassword` | text | — | — | — |
| `viettel_invoice_tax_code` | `viettelInvoiceTaxCode` | text | — | — | — |
| `viettel_invoice_template_code` | `viettelInvoiceTemplateCode` | text | — | — | — |
| `viettel_invoice_series` | `viettelInvoiceSeries` | text | — | — | — |
| `viettel_invoice_type` | `viettelInvoiceType` | text | — | — | — |
| `viettel_invoice_gdt_tax_code` | `viettelInvoiceGdtTaxCode` | text | — | — | — |
| `vat_inbound_provider` | `vatInboundProvider` | text | NOT NULL, default `viettel` | — | — |
| `gdt_portal_username` | `gdtPortalUsername` | text | — | — | — |
| `gdt_portal_password` | `gdtPortalPassword` | text | — | — | — |
| `vat_inbound_auto_sync_enabled` | `vatInboundAutoSyncEnabled` | boolean | NOT NULL, default `false` | — | — |
| `vat_inbound_auto_map_enabled` | `vatInboundAutoMapEnabled` | boolean | NOT NULL, default `false` | — | — |
| `vat_inbound_auto_receive_enabled` | `vatInboundAutoReceiveEnabled` | boolean | NOT NULL, default `false` | — | — |
| `vat_inbound_auto_archive_tax_codes` | `vatInboundAutoArchiveTaxCodes` | text | — | — | — |
| `smtp_host` | `smtpHost` | text | — | — | — |
| `smtp_port` | `smtpPort` | integer | — | — | — |
| `smtp_secure` | `smtpSecure` | boolean | NOT NULL, default `false` | — | — |
| `smtp_user` | `smtpUser` | text | — | — | — |
| `smtp_password` | `smtpPassword` | text | — | — | — |
| `smtp_from` | `smtpFrom` | text | — | — | — |
| `agent_openai_api_key_enc` | `agentOpenAiApiKeyEnc` | text | — | — | — |
| `agent_openai_api_key_enabled` | `agentOpenAiApiKeyEnabled` | boolean | NOT NULL, default `true` | — | — |
| `agent_openai_base_url` | `agentOpenAiBaseUrl` | text | — | — | — |
| `agent_openai_model` | `agentOpenAiModel` | text | — | — | — |
| `created_at` | `createdAt` | timestamp("created_at", { withTimezone: true }) | NOT NULL, default `now()` | — | — |

## Kiểu & Zod (insert)

- `insertOrganizationSchema` — `createInsertSchema` (xem file TS)
- `export type InsertOrganization`
- `export type Organization`

Tổng quan ER / naming: [../../tham-chieu/co-so-du-lieu-goc/](../../tham-chieu/co-so-du-lieu-goc/).
