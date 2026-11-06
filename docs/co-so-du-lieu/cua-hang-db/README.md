# Schema: `shops`

**Mô tả:** Drizzle shops.ts — 1 bảng, 31 cột (shops).

**Mã nguồn Shop:** `lib/db/src/schema/shops.ts`

## Cách đọc trang này

Mỗi **bảng Postgres** có bảng cột: kiểu Drizzle, `NOT NULL` / **PK**, khóa ngoại (cột FK → tên bảng đích), và ghi chú JSDoc từ mã nguồn. Enum và index được liệt kê riêng khi có trong file.

## Liên kết nhanh

- **HTTP API:** [cua-hang](../../module-api/cua-hang/) (`routes/shops.ts`)

## Bảng `shops`

- **Biến Drizzle:** `shopsTable`

| Cột SQL | Thuộc tính TS | Kiểu | Ràng buộc | FK → bảng | Ghi chú |
|---------|---------------|------|-----------|-----------|---------|
| `id` | `id` | serial | **PK** | — | — |
| `organization_id` | `organizationId` | integer | — | `organizations` | — |
| `code` | `code` | text | — | — | — |
| `name` | `name` | text | NOT NULL | — | — |
| `address` | `address` | text | — | — | — |
| `phone` | `phone` | text | — | — | — |
| `type` | `type` | text | NOT NULL, default `store` | — | — |
| `status` | `status` | text | NOT NULL, default `active` | — | — |
| `display_order` | `displayOrder` | integer | NOT NULL, default `0` | — | — |
| `allow_overselling` | `allowOverselling` | boolean | NOT NULL, default `true` | — | — |
| `allow_order_edit` | `allowOrderEdit` | boolean | NOT NULL, default `true` | — | — |
| `allow_staff_edit_payment` | `allowStaffEditPayment` | boolean | NOT NULL, default `false` | — | — |
| `allow_staff_edit_cart` | `allowStaffEditCart` | boolean | NOT NULL, default `true` | — | — |
| `allow_staff_approve_stock` | `allowStaffApproveStock` | boolean | NOT NULL, default `false` | — | — |
| `device_control_enabled` | `deviceControlEnabled` | boolean | NOT NULL, default `false` | — | — |
| `weighted_average_cost_enabled` | `weightedAverageCostEnabled` | boolean | NOT NULL, default `true` | — | — |
| `vat_invoice_public_enabled` | `vatInvoicePublicEnabled` | boolean | NOT NULL, default `true` | — | — |
| `vat_invoice_auto_issue_enabled` | `vatInvoiceAutoIssueEnabled` | boolean | NOT NULL, default `false` | — | — |
| `vat_invoice_inbound_mapped_only_enabled` | `vatInvoiceInboundMappedOnlyEnabled` | boolean | NOT NULL, default `false` | — | — |
| `hub_admin_dashboard_profit_enabled` | `hubAdminDashboardProfitEnabled` | boolean | NOT NULL, default `false` | — | — |
| `hub_accountant_dashboard_profit_enabled` | `hubAccountantDashboardProfitEnabled` | boolean | NOT NULL, default `false` | — | — |
| `hub_manager_catalog_sales_count_enabled` | `hubManagerCatalogSalesCountEnabled` | boolean | NOT NULL, default `true` | — | — |
| `hub_accountant_catalog_sales_count_enabled` | `hubAccountantCatalogSalesCountEnabled` | boolean | NOT NULL, default `true` | — | — |
| `payment_proof_enabled` | `paymentProofEnabled` | boolean | NOT NULL, default `true` | — | — |
| `product_proof_enabled` | `productProofEnabled` | boolean | NOT NULL, default `true` | — | — |
| `manual_visitor_entry_enabled` | `manualVisitorEntryEnabled` | boolean | NOT NULL, default `true` | — | — |
| `mobile_web_pos_enabled` | `mobileWebPosEnabled` | boolean | NOT NULL, default `true` | — | — |
| `last_seen_at` | `lastSeenAt` | timestamp("last_seen_at", { withTimezone: true }) | — | — | — |
| `last_heartbeat_device_time` | `lastHeartbeatDeviceTime` | timestamp("last_heartbeat_device_time", { withTimezone: true }) | — | — | — |
| `presence_event_state` | `presenceEventState` | text | — | — | — |
| `clock_drift_event_state` | `clockDriftEventState` | boolean | — | — | — |

## Kiểu & Zod (insert)

- `insertShopSchema` — `createInsertSchema` (xem file TS)
- `export type InsertShop`
- `export type Shop`

Tổng quan ER / naming: [../../tham-chieu/co-so-du-lieu-goc/](../../tham-chieu/co-so-du-lieu-goc/).
