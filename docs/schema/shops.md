# Schema: `shops`

**Mô tả:** Drizzle schema shops.ts — 31 cột trên 1 bảng Postgres (shops).

**Source Shop:** `lib/db/src/schema/shops.ts`

## Bảng Postgres

- `shops`

## Cột (trích từ schema TS)

- `id` (id)
- `organization_id` (organizationId)
- `code` (code)
- `name` (name)
- `address` (address)
- `phone` (phone)
- `type` (type)
- `status` (status)
- `display_order` (displayOrder)
- `allow_overselling` (allowOverselling)
- `allow_order_edit` (allowOrderEdit)
- `allow_staff_edit_payment` (allowStaffEditPayment)
- `allow_staff_edit_cart` (allowStaffEditCart)
- `allow_staff_approve_stock` (allowStaffApproveStock)
- `device_control_enabled` (deviceControlEnabled)
- `weighted_average_cost_enabled` (weightedAverageCostEnabled)
- `vat_invoice_public_enabled` (vatInvoicePublicEnabled)
- `vat_invoice_auto_issue_enabled` (vatInvoiceAutoIssueEnabled)
- `vat_invoice_inbound_mapped_only_enabled` (vatInvoiceInboundMappedOnlyEnabled)
- `hub_admin_dashboard_profit_enabled` (hubAdminDashboardProfitEnabled)
- `hub_accountant_dashboard_profit_enabled` (hubAccountantDashboardProfitEnabled)
- `hub_manager_catalog_sales_count_enabled` (hubManagerCatalogSalesCountEnabled)
- `hub_accountant_catalog_sales_count_enabled` (hubAccountantCatalogSalesCountEnabled)
- `payment_proof_enabled` (paymentProofEnabled)
- `product_proof_enabled` (productProofEnabled)
- `manual_visitor_entry_enabled` (manualVisitorEntryEnabled)
- `mobile_web_pos_enabled` (mobileWebPosEnabled)
- `last_seen_at` (lastSeenAt)
- `last_heartbeat_device_time` (lastHeartbeatDeviceTime)
- `presence_event_state` (presenceEventState)
- `clock_drift_event_state` (clockDriftEventState)

## Tham chiếu (references → bảng Drizzle)

- `organizationsTable`

Tổng quan quan hệ: `reference/database.md`.
