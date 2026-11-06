# VietPOS-Map — Mục lục đầy đủ

Tài liệu **chi tiết theo file code** trong Shop-Manager-System-Offline, cộng **luồng nghiệp vụ** và **mirror** doc gốc Shop.

**Regenerate:** `python3 docs/gen.py` (sau khi đổi routes/pages/schema ở Shop).

Mỗi file doc có dòng **Mô tả:** ở đầu; mục lục bên dưới lặp lại mô tả sau tên file.

---

## Sơ đồ kiến trúc

```
pos-app (React) ──/api──► api-server (Express) ──► PostgreSQL
     │                         ▲
  local-db/sync               cloud-sync → Railway
 Widget / ESP32 ──API key──► visitor-counts, widget
```

---

## Hệ thống & workspace (4 mục)

1. [01-kien-truc-runtime.md](he-thong/01-kien-truc-runtime.md) — Sơ đồ runtime: client React → Express API → PostgreSQL; tùy chọn cloud-sync Railway.
2. [02-workspace-luu-niem.md](he-thong/02-workspace-luu-niem.md) — Các repo trong LuuNiem (Shop, Deploy, Widget, Map, ESP32) và vai trò từng thư mục.
3. [03-monorepo-packages.md](he-thong/03-monorepo-packages.md) — Cấu trúc pnpm workspace: artifacts, lib, scripts trong Shop-Manager.
4. [04-docker-va-cloud-sync.md](he-thong/04-docker-va-cloud-sync.md) — Docker Compose local, biến CLOUD_DATABASE_URL, worker cloud-sync và Trợ lý AI.

## Nghiệp vụ (luồng chi tiết) (12 mục)

5. [01-dang-nhap-va-shop-context.md](nghiep-vu/01-dang-nhap-va-shop-context.md) — Đăng nhập, JWT gắn shop/role, hub shop và ngữ cảnh vận hành API.
6. [02-pos-ban-hang.md](nghiep-vu/02-pos-ban-hang.md) — Luồng POS: ca làm việc, giỏ hàng, thanh toán, in bill, hủy đơn và audit.
7. [03-san-pham-va-ton.md](nghiep-vu/03-san-pham-va-ton.md) — CRUD sản phẩm, import Excel, tồn shop và điều chỉnh inventory.
8. [04-phieu-nhap-xuat-chuyen-kho.md](nghiep-vu/04-phieu-nhap-xuat-chuyen-kho.md) — Phiếu stock-request, chuyển kho chuỗi, PO và liên kết nhập hàng.
9. [05-hoa-don-vat-xuat.md](nghiep-vu/05-hoa-don-vat-xuat.md) — Hóa đơn VAT bán ra qua Viettel SInvoice và cấu hình org.
10. [06-hoa-don-dau-vao-tong-quan.md](nghiep-vu/06-hoa-don-dau-vao-tong-quan.md) — Vòng đời HĐ mua vào: import, ghép SP, nhập kho, trạng thái stockStatus.
11. [07-hd-dau-vao-mst-loc.md](nghiep-vu/07-hd-dau-vao-mst-loc.md) — MST lọc tự archive HĐ; tab Khác / Lưu trữ / Đang dùng; modal trên trang HĐ đầu vào.
12. [08-hd-dau-vao-cqt-sync.md](nghiep-vu/08-hd-dau-vao-cqt-sync.md) — Kéo HĐ từ CQT (GDT direct): captcha, sync-tax, map XML vào DB.
13. [09-chuoi-va-da-chi-nhanh.md](nghiep-vu/09-chuoi-va-da-chi-nhanh.md) — Organization, nhiều shop, kho trung tâm, dashboard chuỗi và heartbeat.
14. [10-truy-cap-an-ninh.md](nghiep-vu/10-truy-cap-an-ninh.md) — Chặn IP/thiết bị, quan sát truy cập và RBAC liên quan.
15. [11-offline-va-sync-client.md](nghiep-vu/11-offline-va-sync-client.md) — IndexedDB local-db, checkout offline, pull/push sync với server.
16. [12-widget-va-dem-khach.md](nghiep-vu/12-widget-va-dem-khach.md) — App widget Android, ESP32 visitor-counts và shop API keys.

## API modules (từng file routes/*.ts) (39 mục)

17. [access-observations.md](api-modules/access-observations.md) — File routes access-observations.ts — 1 endpoint HTTP cho /api/.... Tổng hợp cặp (deviceId, IP) đã gọi API — lưu in-memory (TTL giờ, xem accessObservationTtlHours). - Dùng tab Tổng quan t…
18. [agent.md](api-modules/agent.md) — File routes agent.ts — 10 endpoint HTTP cho /api/.... Trợ lý AI: chat, system info (DB, cloud sync, shops online), cấp quyền agent_assistant_enabled. Frontend: pages/agent-a…
19. [auth.md](api-modules/auth.md) — File routes auth.ts — 8 endpoint HTTP cho /api/.... REST handlers cho domain auth.
20. [blocked-devices.md](api-modules/blocked-devices.md) — File routes blocked-devices.ts — 3 endpoint HTTP cho /api/.... Danh sách Device ID (header client) bị chặn mọi /api/*. - Quyền: super_admin (giống blocked-ips). - Device ID lấy từ cl…
21. [blocked-ips.md](api-modules/blocked-ips.md) — File routes blocked-ips.ts — 3 endpoint HTTP cho /api/.... Danh sách IP bị chặn toàn cục trên mọi request /api/*. - Quyền: requireAuth + role super_admin (403 nếu không đủ). - Sa…
22. [chain.md](api-modules/chain.md) — File routes chain.ts — 29 endpoint HTTP cho /api/.... Tổ chức, shop, kho, điều chuyển (transfers). Cấu hình org (Viettel, CQT, feedback URL, agent LLM). Frontend: pages/chai…
23. [dashboard.md](api-modules/dashboard.md) — File routes dashboard.ts — 17 endpoint HTTP cho /api/.... REST handlers cho domain dashboard.
24. [feedback.md](api-modules/feedback.md) — File routes feedback.ts — 5 endpoint HTTP cho /api/.... REST handlers cho domain feedback.
25. [health.md](api-modules/health.md) — File routes health.ts — 1 endpoint HTTP cho /api/.... REST handlers cho domain health.
26. [inventory.md](api-modules/inventory.md) — File routes inventory.ts — 2 endpoint HTTP cho /api/.... REST handlers cho domain inventory.
27. [media.md](api-modules/media.md) — File routes media.ts — 1 endpoint HTTP cho /api/.... REST handlers cho domain media.
28. [notification-settings.md](api-modules/notification-settings.md) — File routes notification-settings.ts — 2 endpoint HTTP cho /api/.... REST handlers cho domain notification-settings.
29. [notifications.md](api-modules/notifications.md) — File routes notifications.ts — 2 endpoint HTTP cho /api/.... REST handlers cho domain notifications.
30. [order-audit-reports.md](api-modules/order-audit-reports.md) — File routes order-audit-reports.ts — 2 endpoint HTTP cho /api/.... REST handlers cho domain order-audit-reports.
31. [orders.md](api-modules/orders.md) — File routes orders.ts — 21 endpoint HTTP cho /api/.... Đơn hàng POS: tạo, hủy, duyệt hủy, in lại, thông báo reprint. Gắn ca (shift-sessions), audit cart. Frontend: pages/pos.…
32. [org-gdt-portal.md](api-modules/org-gdt-portal.md) — File routes org-gdt-portal.ts — 4 endpoint HTTP cho /api/.... Session CQT trực tiếp (captcha, connect) — dùng chung org với HĐ đầu vào.
33. [org-viettel-settings.md](api-modules/org-viettel-settings.md) — File routes org-viettel-settings.ts — 2 endpoint HTTP cho /api/.... REST handlers cho domain org-viettel-settings.
34. [pos-cart-audit.md](api-modules/pos-cart-audit.md) — File routes pos-cart-audit.ts — 3 endpoint HTTP cho /api/.... REST handlers cho domain pos-cart-audit.
35. [product-audit-reports.md](api-modules/product-audit-reports.md) — File routes product-audit-reports.ts — 2 endpoint HTTP cho /api/.... REST handlers cho domain product-audit-reports.
36. [product-categories.md](api-modules/product-categories.md) — File routes product-categories.ts — 3 endpoint HTTP cho /api/.... REST handlers cho domain product-categories.
37. [products.md](api-modules/products.md) — File routes products.ts — 11 endpoint HTTP cho /api/.... CRUD sản phẩm, import Excel, variant, ẩn/hiện SP, giá/giá vốn theo role. Frontend: pages/products.tsx.
38. [public-vat-invoice.md](api-modules/public-vat-invoice.md) — File routes public-vat-invoice.ts — 3 endpoint HTTP cho /api/.... REST handlers cho domain public-vat-invoice.
39. [purchase-order-audit-reports.md](api-modules/purchase-order-audit-reports.md) — File routes purchase-order-audit-reports.ts — 2 endpoint HTTP cho /api/.... REST handlers cho domain purchase-order-audit-reports.
40. [purchase-orders.md](api-modules/purchase-orders.md) — File routes purchase-orders.ts — 9 endpoint HTTP cho /api/.... REST handlers cho domain purchase-orders.
41. [reports.md](api-modules/reports.md) — File routes reports.ts — 4 endpoint HTTP cho /api/.... REST handlers cho domain reports.
42. [sales-staff.md](api-modules/sales-staff.md) — File routes sales-staff.ts — 4 endpoint HTTP cho /api/.... REST handlers cho domain sales-staff.
43. [shift-sessions.md](api-modules/shift-sessions.md) — File routes shift-sessions.ts — 3 endpoint HTTP cho /api/.... REST handlers cho domain shift-sessions.
44. [shop-api-keys.md](api-modules/shop-api-keys.md) — File routes shop-api-keys.ts — 8 endpoint HTTP cho /api/.... API key cho widget / thiết bị (ESP32 visitor-counts). Frontend: pages/chain-api-keys.tsx (nếu có).
45. [shops.md](api-modules/shops.md) — File routes shops.ts — 3 endpoint HTTP cho /api/.... REST handlers cho domain shops.
46. [staff.md](api-modules/staff.md) — File routes staff.ts — 7 endpoint HTTP cho /api/.... REST handlers cho domain staff.
47. [statistics.md](api-modules/statistics.md) — File routes statistics.ts — 6 endpoint HTTP cho /api/.... REST handlers cho domain statistics.
48. [stock-request-audit-reports.md](api-modules/stock-request-audit-reports.md) — File routes stock-request-audit-reports.ts — 2 endpoint HTTP cho /api/.... REST handlers cho domain stock-request-audit-reports.
49. [stock-requests.md](api-modules/stock-requests.md) — File routes stock-requests.ts — 14 endpoint HTTP cho /api/.... Phiếu yêu cầu nhập/xuất nội bộ: tạo → duyệt → hoàn tất → cập nhật tồn. Frontend: pages/stock-requests.tsx.
50. [suppliers.md](api-modules/suppliers.md) — File routes suppliers.ts — 4 endpoint HTTP cho /api/.... REST handlers cho domain suppliers.
51. [sync.md](api-modules/sync.md) — File routes sync.ts — 2 endpoint HTTP cho /api/.... Endpoint đồng bộ client (pull/push) cho offline IndexedDB.
52. [system-events.md](api-modules/system-events.md) — File routes system-events.ts — 1 endpoint HTTP cho /api/.... REST handlers cho domain system-events.
53. [vat-inbound.md](api-modules/vat-inbound.md) — File routes vat-inbound.ts — 28 endpoint HTTP cho /api/.... Module lớn nhất về HĐ mua vào VAT: import PDF/Excel, kéo CQT/Viettel, ghép SP, nhập kho, lưu trữ, MST lọc (tab Khác), a…
54. [walk-in-customers.md](api-modules/walk-in-customers.md) — File routes walk-in-customers.ts — 2 endpoint HTTP cho /api/.... REST handlers cho domain walk-in-customers.
55. [widget.md](api-modules/widget.md) — File routes widget.ts — 1 endpoint HTTP cho /api/.... API phục vụ app Android widget: thống kê quầy (JWT / shop context). Repo: VietPOS-Widget/.

## Thư viện backend (lib-modules, từng file lib/*.ts) (98 mục)

56. [agent-chat-persist.md](lib-modules/agent-chat-persist.md) — Logic backend agent-chat-persist.ts (~262 dòng) — export: AGENT_CHAT_CONTEXT_LIMIT, getOrCreateAgentChatThread, appendAgentChatMessage, loadAgentChatContextForUser, clearAgentChatForUser, ….
57. [agent-tool-dates.md](lib-modules/agent/agent-tool-dates.md) — Logic backend agent/agent-tool-dates.ts (~51 dòng) — export: formatAgentToolPayloadForLlm.
58. [chat.md](lib-modules/agent/chat.md) — Logic backend agent/chat.ts (~178 dòng) — export: resolveAgentLlmForAuth, isAgentLlmConfiguredForAuth, runAgentChat.
59. [read-business-data.md](lib-modules/agent/read-business-data.md) — Logic backend agent/read-business-data.ts (~1011 dòng) — export: AGENT_READ_DATASETS, readBusinessDataSchema, runReadBusinessData.
60. [read-deep-handlers.md](lib-modules/agent/read-deep-handlers.md) — Logic backend agent/read-deep-handlers.ts (~603 dòng) — export: readRevenueChartDaily, readVatQueueCounts, readVatInboundList, readReprintsList, readShiftSessionsRecent, ….
61. [system-info.md](lib-modules/agent/system-info.md) — Logic backend agent/system-info.ts (~176 dòng) — export: buildAgentSystemInfo.
62. [tools.md](lib-modules/agent/tools.md) — Logic backend agent/tools.ts (~317 dòng) — export: agentToolDefinitionsForAuth, invokeAgentTool.
63. [allowed-device-names.md](lib-modules/allowed-device-names.md) — Logic backend allowed-device-names.ts (~94 dòng) — export: lookupDeviceNamesByDeviceIds.
64. [api-access-observations.md](lib-modules/api-access-observations.md) — Logic backend api-access-observations.ts (~157 dòng) — export: recordApiAccessObservation, summarizeAccessObservationsToday, listAccessObservations, accessObservationMiddleware, startAccessObservatio…
65. [chain-shop-scope.md](lib-modules/chain-shop-scope.md) — Logic backend chain-shop-scope.ts (~106 dòng) — export: parseOptionalShopId, resolveChainShopScope, resolveStatisticsShopScope, resolveReportShopScope, shopIdFilter, ….
66. [change-log.md](lib-modules/change-log.md) — Logic backend change-log.ts (~30 dòng) — export: recordProductChange, recordInventoryChange.
67. [cors-config.md](lib-modules/cors-config.md) — Logic backend cors-config.ts (~30 dòng) — export: parseFrontendUrls, getCorsOptions.
68. [customer-public-urls.md](lib-modules/customer-public-urls.md) — Logic backend customer-public-urls.ts (~92 dòng) — export: normalizePublicBaseUrl, buildPublicPageUrl, publicUrlsFromBase, normalizeFeedbackPublicUrl, applyCustomerPublicUrlFields.
69. [dashboard-period.md](lib-modules/dashboard-period.md) — Logic backend dashboard-period.ts (~284 dòng) — export: resolveDashboardPeriodRange, parseDashboardChartGranularity, parseQuarterChartGranularity, buildDashboardRevenueChartBuckets.
70. [dashboard-visitor-stats.md](lib-modules/dashboard-visitor-stats.md) — Logic backend dashboard-visitor-stats.ts (~240 dòng) — export: visitDateString, visitorsPerBuyer, sumVisitorsForShopOnDate, visitorsByShopOnDate, sumVisitorsForShopsOnDate, ….
71. [device-denylist.md](lib-modules/device-denylist.md) — Logic backend device-denylist.ts (~91 dòng) — export: blockedDeviceCount, normalizeDeviceId, deviceIdFromRequest, isValidBlockedDeviceId, refreshDeviceDenylistFromDb, ….
72. [entity-status.md](lib-modules/entity-status.md) — Logic backend entity-status.ts (~220 dòng) — export: getOperationalContext, getShopOperationalBlock, isShopActive, assertVoucherTransition, assertWarehouseOperational, ….
73. [captcha-store.md](lib-modules/gdt-portal/captcha-store.md) — Logic backend gdt-portal/captcha-store.ts (~19 dòng) — export: getOrCreateCaptchaClient, dropCaptchaClient.
74. [client.md](lib-modules/gdt-portal/client.md) — Logic backend gdt-portal/client.ts (~345 dòng) — export: captchaDataUrl.
75. [connect-with-captcha.md](lib-modules/gdt-portal/connect-with-captcha.md) — Logic backend gdt-portal/connect-with-captcha.ts (~61 dòng) — export: gdtPortalConnectWithCaptcha, gdtPortalFetchCaptcha, gdtPortalConnectFailed.
76. [export-xml.md](lib-modules/gdt-portal/export-xml.md) — Logic backend gdt-portal/export-xml.ts (~23 dòng) — export: extractFirstXmlFromExportPayload, lineItemsFromExportXmlBytes.
77. [fetch-inbound.md](lib-modules/gdt-portal/fetch-inbound.md) — Logic backend gdt-portal/fetch-inbound.ts (~106 dòng) — export: fetchGdtInboundInvoices.
78. [http-session.md](lib-modules/gdt-portal/http-session.md) — Logic backend gdt-portal/http-session.ts (~53 dòng) — export: (không export tên rõ).
79. [map-inbound.md](lib-modules/gdt-portal/map-inbound.md) — Logic backend gdt-portal/map-inbound.ts (~209 dòng) — export: formatGdtVatRateLabel, mapGdtPurchaseRow, applyGdtDetailToMapped.
80. [org-session.md](lib-modules/gdt-portal/org-session.md) — Logic backend gdt-portal/org-session.ts (~153 dòng) — export: normalizeVatInboundProvider, getGdtSessionPublic, saveGdtSessionToken, markGdtTestFailed, clearGdtSession, ….
81. [xml-lines.md](lib-modules/gdt-portal/xml-lines.md) — Logic backend gdt-portal/xml-lines.ts (~46 dòng) — export: parseLineItemsFromCqtXml.
82. [inbound-stock-receive.md](lib-modules/inbound-stock-receive.md) — Logic backend inbound-stock-receive.ts (~170 dòng) — export: applyInvoiceInventoryReceive, reverseInvoiceInventoryReceive.
83. [inventory-variant.md](lib-modules/inventory-variant.md) — Logic backend inventory-variant.ts (~328 dòng) — export: upsertShopStockByProduct, upsertShopExtraVariantStock, upsertShopStockByVariant, getShopStockQty, mapShopExtraVariantQuantities, ….
84. [ip-denylist.md](lib-modules/ip-denylist.md) — Logic backend ip-denylist.ts (~159 dòng) — export: normalizeClientIp, blockedIpCount, clientIpFromRequest, describeSeenClientIp, refreshIpDenylistFromDb, ….
85. [logger.md](lib-modules/logger.md) — Logic backend logger.ts (~21 dòng) — export: logger.
86. [order-audit.md](lib-modules/order-audit.md) — Logic backend order-audit.ts (~151 dòng) — export: mapAuditLogRow, insertOrderAuditLog, listOrderAuditLogs.
87. [order-direct-cancel.md](lib-modules/order-direct-cancel.md) — Logic backend order-direct-cancel.ts (~64 dòng) — export: directCancelWithoutRequestSql, sumDirectCancelledInPeriod, directCancelWithoutRequestOrderIds.
88. [order-discount.md](lib-modules/order-discount.md) — Logic backend order-discount.ts (~108 dòng) — export: computeOrderDiscountAmount, fetchDashboardChartOrders, sumCompletedOrderDiscount.
89. [order-fraud.md](lib-modules/order-fraud.md) — Logic backend order-fraud.ts (~16 dòng) — export: isOrderSyncSuspicious.
90. [order-invoice-code.md](lib-modules/order-invoice-code.md) — Logic backend order-invoice-code.ts (~33 dòng) — export: normalizeShopCode, formatOrderInvoiceCode, unpadOrderInvoiceCode, formatOrderStt.
91. [order-invoice-list-filters.md](lib-modules/order-invoice-list-filters.md) — Logic backend order-invoice-list-filters.ts (~45 dòng) — export: invoiceListFilters.
92. [order-list-period-summary.md](lib-modules/order-list-period-summary.md) — Logic backend order-list-period-summary.ts (~147 dòng) — export: appendOrderListDateFilters, fetchOrderListPeriodSummary.
93. [order-preprint.md](lib-modules/order-preprint.md) — Logic backend order-preprint.ts (~170 dòng) — export: newInvoicePublicToken, upsertOrderPreprintReservation, loadPreprintForClientOrder, findPreprintByPublicToken.
94. [order-shop-sequence.md](lib-modules/order-shop-sequence.md) — Logic backend order-shop-sequence.ts (~70 dòng) — export: allocateShopOrderSequence, resolveShopOrderSequence, queryMaxShopOrderSequence.
95. [orders-scope.md](lib-modules/orders-scope.md) — Logic backend orders-scope.ts (~107 dòng) — export: parseOptionalShopId, resolveOrderListScope, orderShopFilter, canAccessOrder, loadOrderForCancelModeration.
96. [org-agent-llm-settings.md](lib-modules/org-agent-llm-settings.md) — Logic backend org-agent-llm-settings.ts (~167 dòng) — export: maskAgentApiKeyForDisplay, stripOrgAgentLlmSecret, envAgentLlmConfig, resolveAgentLlmConfigForOrg, isAgentLlmConfiguredForOrg, ….
97. [org-gdt-settings.md](lib-modules/org-gdt-settings.md) — Logic backend org-gdt-settings.ts (~92 dòng) — export: stripOrgGdtPassword, applyGdtSettingsFromBody, gdtCredentialsReady, buildVatInboundChannelStatus.
98. [org-smtp-settings.md](lib-modules/org-smtp-settings.md) — Logic backend org-smtp-settings.ts (~119 dòng) — export: stripOrgSmtpPassword, smtpConfigFromOrgRow, loadOrgSmtpConfig, applySmtpSettingsFromBody.
99. [org-viettel-settings.md](lib-modules/org-viettel-settings.md) — Logic backend org-viettel-settings.ts (~126 dòng) — export: viettelConfigReadiness, stripOrgViettelPassword, toPublicViettelSettings, applyViettelSettingsFromBody.
100. [payment-revenue.md](lib-modules/payment-revenue.md) — Logic backend payment-revenue.ts (~31 dòng) — export: emptyPaymentRevenue, addOrderPaymentRevenue, sumOrdersPaymentRevenue.
101. [pin-challenge.md](lib-modules/pin-challenge.md) — Logic backend pin-challenge.ts (~56 dòng) — export: PIN_CHALLENGE_PURPOSE, signPinChallengeToken, verifyPinChallengeToken, isPinChallengeJwtPayload.
102. [pin-reset-requests.md](lib-modules/pin-reset-requests.md) — Logic backend pin-reset-requests.ts (~98 dòng) — export: upsertPendingPinResetRequest, canSetPinWithoutPasswordAfterUserSetsReset, clearUserPin, setUserPin, markPinResetRequestResolved, ….
103. [platform-notification-settings.md](lib-modules/platform-notification-settings.md) — Logic backend platform-notification-settings.ts (~467 dòng) — export: RECIPIENT_ROLE_OPTIONS, invalidateNotificationSettingsCache, defaultRecipientRolesForType, effectiveRecipientRoles, getRecipientR…
104. [product-audit.md](lib-modules/product-audit.md) — Logic backend product-audit.ts (~63 dòng) — export: recordProductAudit, buildProductFieldChanges.
105. [product-category.md](lib-modules/product-category.md) — Logic backend product-category.ts (~98 dòng) — export: findCategoryByName, resolveProductCategory, syncProductCategoryNameFromCategory.
106. [product-supplier.md](lib-modules/product-supplier.md) — Logic backend product-supplier.ts (~200 dòng) — export: parseSupplierImportStatus, findSupplierByName, resolveProductSupplier, syncProductManufacturerFromSupplier.
107. [product-variants.md](lib-modules/product-variants.md) — Logic backend product-variants.ts (~451 dòng) — export: suggestVariantCode, getVariant0, ensureVariantColumns, ensureVariant0, syncProductFromVariant0, ….
108. [product-vat-name.md](lib-modules/product-vat-name.md) — Logic backend product-vat-name.ts (~62 dòng) — export: normalizeVatNameKey, findSupplierVatNameConflict, assertUniqueSupplierVatName.
109. [product-vat.md](lib-modules/product-vat.md) — Logic backend product-vat.ts (~61 dòng) — export: DEFAULT_UNIT, DEFAULT_VAT_RATE, DEFAULT_TNCN_RATE, ALLOWED_VAT_RATES, normalizeUnit, ….
110. [rate-limit.md](lib-modules/rate-limit.md) — Logic backend rate-limit.ts (~83 dòng) — export: isRateLimitEnabled, isTrustProxyEnabled, configureTrustProxy.
111. [record-device-login.md](lib-modules/record-device-login.md) — Logic backend record-device-login.ts (~37 dòng) — export: recordDeviceLoginEvent.
112. [report-pos-staff.md](lib-modules/report-pos-staff.md) — Logic backend report-pos-staff.ts (~110 dòng) — export: buildPosStaffReport.
113. [report-sales-staff-performance.md](lib-modules/report-sales-staff-performance.md) — Logic backend report-sales-staff-performance.ts (~172 dòng) — export: buildSalesStaffPerformanceReport.
114. [secret-box.md](lib-modules/secret-box.md) — Logic backend secret-box.ts (~37 dòng) — export: encryptSecret, decryptSecret.
115. [session-cookie.md](lib-modules/session-cookie.md) — Logic backend session-cookie.ts (~27 dòng) — export: SESSION_COOKIE_NAME, setSessionCookie, clearSessionCookie.
116. [shift-sessions.md](lib-modules/shift-sessions.md) — Logic backend shift-sessions.ts (~40 dòng) — export: getActiveShiftSession, isShiftSessionRestrictedRole, assertStaffOrderInActiveShiftSession.
117. [shop-display-order.md](lib-modules/shop-display-order.md) — Logic backend shop-display-order.ts (~16 dòng) — export: shopsOrderByDisplay, compareShopsByDisplay, sortShopsByDisplay.
118. [shop-operational-events.md](lib-modules/shop-operational-events.md) — Logic backend shop-operational-events.ts (~147 dòng) — export: syncShopOperationalState, runShopPresenceSweep.
119. [shop-presence-sweep.md](lib-modules/shop-presence-sweep.md) — Logic backend shop-presence-sweep.ts (~12 dòng) — export: startShopPresenceSweepScheduler.
120. [shop-presence.md](lib-modules/shop-presence.md) — Logic backend shop-presence.ts (~25 dòng) — export: SHOP_PRESENCE_TIMEOUT_MS, isShopOnline, CLOCK_DRIFT_WARNING_MS, hasClockDrift.
121. [shop-vat-settings.md](lib-modules/shop-vat-settings.md) — Logic backend shop-vat-settings.ts (~11 dòng) — export: isVatInvoicePublicEnabledForShop.
122. [staff-role-rank.md](lib-modules/staff-role-rank.md) — Logic backend staff-role-rank.ts (~18 dòng) — export: roleRank, callerCanManageTargetRole.
123. [system-error-capture.md](lib-modules/system-error-capture.md) — Logic backend system-error-capture.ts (~125 dòng) — export: markSystemEventLogged, captureUnhandledProcessError, captureHttpServerError, systemErrorCaptureMiddleware, systemExpressErrorHandler.
124. [system-event-log.md](lib-modules/system-event-log.md) — Logic backend system-event-log.ts (~177 dòng) — export: recordSystemEvent, recordEmailSystemFailure, recordEmailSmtpNotConfigured, recordVatSystemEvent, recordSyncSystemEvent, ….
125. [system-event-query.md](lib-modules/system-event-query.md) — Logic backend system-event-query.ts (~153 dòng) — export: vnTodayYmd, querySystemEventLogs.
126. [time-drift.md](lib-modules/time-drift.md) — Logic backend time-drift.ts (~14 dòng) — export: getTimeDriftWarningThresholdMs.
127. [user-email.md](lib-modules/user-email.md) — Logic backend user-email.ts (~50 dòng) — export: normalizeEmail, EMAIL_ALREADY_USED_MSG, ORG_EMAIL_TAKEN_MSG, findUserByNormalizedEmail, findUserByOrgEmail.
128. [user-notifications.md](lib-modules/user-notifications.md) — Logic backend user-notifications.ts (~1266 dòng) — export: formatVatInboundInvoiceCode, clearVatInboundReceiptActiveNotifications, notifyVatInboundReceiptMapped, notifyVatInboundReceiptExcluded, noti…
129. [user-pin.md](lib-modules/user-pin.md) — Logic backend user-pin.ts (~35 dòng) — export: PIN_LENGTH, roleRequiresPin, normalizePin, validatePinFormat, hashPin, ….
130. [vat-inbound-audit.md](lib-modules/vat-inbound-audit.md) — Logic backend vat-inbound-audit.ts (~66 dòng) — export: insertVatInboundAuditLog, listVatInboundAuditLogs.
131. [vat-inbound-auto-archive-mst.md](lib-modules/vat-inbound-auto-archive-mst.md) — Logic backend vat-inbound-auto-archive-mst.ts (~58 dòng) — export: taxDigitsOnly, parseVatInboundAutoArchiveTaxCodes, normalizeVatInboundAutoArchiveTaxCodesInput, formatVatInboundAutoArchiveTaxCodesF…
132. [vat-inbound-auto-process.md](lib-modules/vat-inbound-auto-process.md) — Logic backend vat-inbound-auto-process.ts (~563 dòng) — export: invoiceEligibleForAutoMap, processVatInboundAutoForInvoice, processVatInboundAutoBatch.
133. [vat-inbound-auto-sync.md](lib-modules/vat-inbound-auto-sync.md) — Logic backend vat-inbound-auto-sync.ts (~151 dòng) — export: isVatInboundAutoSyncWindow, vatInboundAutoSyncSlotKey, vatInboundAutoSyncDateRange, runVatInboundAutoSyncBatch, startVatInboundAutoSyncSch…
134. [vat-inbound-excluded.md](lib-modules/vat-inbound-excluded.md) — Logic backend vat-inbound-excluded.ts (~47 dòng) — export: listExcludedLineIndexes.
135. [vat-inbound-mapped-products.md](lib-modules/vat-inbound-mapped-products.md) — Logic backend vat-inbound-mapped-products.ts (~163 dòng) — export: isVatInvoiceInboundMappedOnlyForShop, INBOUND_MAPPED_NO_ELIGIBLE_LINES_MSG, filterProductIdsForInboundMappedIssue, validateOrderForI…
136. [vat-inbound-marked-mst-backfill.md](lib-modules/vat-inbound-marked-mst-backfill.md) — Logic backend vat-inbound-marked-mst-backfill.ts (~50 dòng) — export: backfillVatInboundArchiveByMarkedMst.
137. [vat-inbound-product-code.md](lib-modules/vat-inbound-product-code.md) — Logic backend vat-inbound-product-code.ts (~33 dòng) — export: initialsFromVatName, vatLinePriceThousands, buildAutoInternalCodeBase, buildAutoInternalCodeDuplicate.
138. [vat-inbound-tax-sync.md](lib-modules/vat-inbound-tax-sync.md) — Logic backend vat-inbound-tax-sync.ts (~400 dòng) — export: syncVatInboundInvoicesFromTax.
139. [vat-invoice-auto-issue.md](lib-modules/vat-invoice-auto-issue.md) — Logic backend vat-invoice-auto-issue.ts (~172 dòng) — export: AUTO_ISSUE_BATCH_MINUTE_OF_DAY_VN, minutesOfDayVN, orderPurchaseAt, isEligiblePurchaseDayForAutoIssue, isPurchaseTodayVN, ….
140. [vat-invoice-buyer-email.md](lib-modules/vat-invoice-buyer-email.md) — Logic backend vat-invoice-buyer-email.ts (~50 dòng) — export: deliverVatInvoiceEmailToBuyer.
141. [vat-invoice-public-window.md](lib-modules/vat-invoice-public-window.md) — Logic backend vat-invoice-public-window.ts (~22 dòng) — export: VAT_INVOICE_PUBLIC_EDIT_WINDOW_MS, orderPurchaseAt, vatInvoiceEditDeadline, isVatInvoicePublicEditable.
142. [vat-invoice.md](lib-modules/vat-invoice.md) — Logic backend vat-invoice.ts (~262 dòng) — export: normalizeTaxCode, isValidTaxCode, isNumericTaxCode, isValidEmail, normalizePhone, ….
143. [vietnam-calendar.md](lib-modules/vietnam-calendar.md) — Logic backend vietnam-calendar.ts (~105 dòng) — export: VN_TZ, formatVnDateTime, vnCalendarDay, vnAddCalendarDays, vnDayStartFromInstant, ….
144. [build-payload.md](lib-modules/viettel-sinvoice/build-payload.md) — Logic backend viettel-sinvoice/build-payload.ts (~198 dòng) — export: mergeOrderLinesByProductForEinvoice, assertEinvoiceCatalogVatNames, buildViettelInvoicePayload.
145. [client.md](lib-modules/viettel-sinvoice/client.md) — Logic backend viettel-sinvoice/client.ts (~489 dòng) — export: isTransientViettelPdfError, createViettelInvoice, searchViettelInvoiceByTransactionUuid, searchViettelInboundByTax, sleep, ….
146. [config.md](lib-modules/viettel-sinvoice/config.md) — Logic backend viettel-sinvoice/config.ts (~163 dòng) — export: toGdtPortalTaxCode, loadOrgViettelRow, resolveOrganizationIdForShop, getViettelInboundConfig, getViettelSinvoiceConfig, ….
147. [download-pdf.md](lib-modules/viettel-sinvoice/download-pdf.md) — Logic backend viettel-sinvoice/download-pdf.ts (~103 dòng) — export: fetchViettelInvoicePdf, fetchViettelInvoicePdfForOrder.
148. [inbound-pdf.md](lib-modules/viettel-sinvoice/inbound-pdf.md) — Logic backend viettel-sinvoice/inbound-pdf.ts (~134 dòng) — export: toViettelPortalIssueDate, fetchViettelInboundInvoicePdf.
149. [issue.md](lib-modules/viettel-sinvoice/issue.md) — Logic backend viettel-sinvoice/issue.ts (~308 dòng) — export: issueViettelInvoiceForOrder.
150. [search-inbound.md](lib-modules/viettel-sinvoice/search-inbound.md) — Logic backend viettel-sinvoice/search-inbound.ts (~361 dòng) — export: mapViettelInboundInvoice, splitInboundDateRange, isViettelDemoTaxCode, fetchViettelInboundInvoices, assertViettelInboundInvoiceE…
151. [vn-order-period.md](lib-modules/vn-order-period.md) — Logic backend vn-order-period.ts (~117 dòng) — export: VN_YMD_RE, vnYmdStartInstant, vnYmdEndInclusiveInstant, resolveChartAlignedOrderPeriodBounds, appendChartAlignedOrderPeriodFilters, ….
152. [weighted-average-cost.md](lib-modules/weighted-average-cost.md) — Logic backend weighted-average-cost.ts (~47 dòng) — export: roundMoney2, weightedAverageCost, reverseWeightedAverageCost.
153. [widget-home.md](lib-modules/widget-home.md) — Logic backend widget-home.ts (~525 dòng) — export: computeDayBlockForShops, computeInbound, computeActions, WIDGET_SUPER_ADMIN_ONLY_MESSAGE, assertWidgetSuperAdmin, ….

## Frontend pages (từng pages/*.tsx) (36 mục)

154. [access-block.md](frontend-pages/access-block.md) — Chặn IP/thiết bị và tab tổng quan truy cập bất thường. (URL /access-block, AccessBlockPage, ~78 dòng).
155. [access-overview-section.md](frontend-pages/access-overview-section.md) — Section embed tổng quan access trong trang chặn truy cập. (URL *(public hoặc redirect — xem App.tsx)*, *(default export)*, ~453 dòng).
156. [agent-assistant.md](frontend-pages/agent-assistant.md) — Trợ lý AI chat + panel trạng thái hệ thống (DB, cloud sync, shop online). (URL /agent-assistant, AgentAssistantPage, ~419 dòng).
157. [agent-chat-audit.md](frontend-pages/agent-chat-audit.md) — Xem lịch sử hội thoại Trợ lý AI đã lưu. (URL /agent-chat-audit, AgentChatAuditPage, ~269 dòng).
158. [camera-settings.md](frontend-pages/camera-settings.md) — Cấu hình camera (desktop) phục vụ POS/media. (URL /camera-settings, CameraSettingsPage, ~370 dòng).
159. [chain-api-keys.md](frontend-pages/chain-api-keys.md) — Tạo API key shop cho widget và thiết bị ESP32. (URL *(public hoặc redirect — xem App.tsx)*, ChainApiKeysTab, ~405 dòng).
160. [chain-dashboard.md](frontend-pages/chain-dashboard.md) — Dashboard tổng hợp chuỗi cửa hàng theo quyền. (URL /chain-dashboard, ChainDashboard, ~2003 dòng).
161. [chain.md](frontend-pages/chain.md) — Sửa tổ chức: shop, Viettel, CQT, Trợ lý AI, URL feedback. (URL /chain, Chain, ~4155 dòng).
162. [customer-feedback.md](frontend-pages/customer-feedback.md) — Quản lý phản hồi khách đã gửi từ form công khai. (URL /customer-feedback, CustomerFeedbackPage, ~369 dòng).
163. [dashboard.md](frontend-pages/dashboard.md) — Tổng quan doanh thu, đơn, tồn thấp theo shop. (URL /dashboard, Dashboard, ~1221 dòng).
164. [device-ban.md](frontend-pages/device-ban.md) — Redirect legacy → access-block tab thiết bị. (URL *(public hoặc redirect — xem App.tsx)*, *(default export)*, ~282 dòng).
165. [feedback-form.md](frontend-pages/feedback-form.md) — Form công khai /feedback cho khách gửi ý kiến. (URL /feedback, FeedbackFormPage, ~360 dòng).
166. [inventory.md](frontend-pages/inventory.md) — Tồn kho shop, điều chỉnh số lượng, cảnh báo sắp hết. (URL /inventory, Inventory, ~1066 dòng).
167. [ip-ban.md](frontend-pages/ip-ban.md) — Redirect legacy → access-block tab IP. (URL *(public hoặc redirect — xem App.tsx)*, *(default export)*, ~266 dòng).
168. [keyboard-shortcuts.md](frontend-pages/keyboard-shortcuts.md) — Bảng phím tắt POS/desktop. (URL /keyboard-shortcuts, KeyboardShortcutsPage, ~396 dòng).
169. [lan-devices.md](frontend-pages/lan-devices.md) — Thiết bị LAN peer (in, widget nội bộ). (URL /lan-devices, LanDevicesPage, ~382 dòng).
170. [login.md](frontend-pages/login.md) — Đăng nhập email/PIN, lưu phiên thiết bị. (URL /login, Login, ~1080 dòng).
171. [media.md](frontend-pages/media.md) — Thư viện media/upload ảnh sản phẩm. (URL /media, MediaPage, ~603 dòng).
172. [my-permissions.md](frontend-pages/my-permissions.md) — Giải thích quyền role và menu hiện tại. (URL /my-permissions, MyPermissions, ~767 dòng).
173. [not-found.md](frontend-pages/not-found.md) — Trang 404 SPA. (URL *(public hoặc redirect — xem App.tsx)*, NotFound, ~22 dòng).
174. [notification-settings.md](frontend-pages/notification-settings.md) — Cấu hình thông báo platform/org. (URL /notification-settings, NotificationSettingsPage, ~487 dòng).
175. [orders.md](frontend-pages/orders.md) — Danh sách đơn, hủy/duyệt hủy, in lại. (URL /orders, Orders, ~22 dòng).
176. [page-status.md](frontend-pages/page-status.md) — Trạng thái triển khai từng trang (dev/ops). (URL /page-status, PageStatus, ~338 dòng).
177. [pos.md](frontend-pages/pos.md) — Màn bán hàng: giỏ, thanh toán, in bill, checkout offline. (URL /pos, POS, ~1988 dòng).
178. [products.md](frontend-pages/products.md) — Danh mục sản phẩm, variant, import Excel, giá. (URL /products, Products, ~2689 dòng).
179. [purchase-orders.md](frontend-pages/purchase-orders.md) — Phiếu đặt mua (PO) và trạng thái nhận hàng. (URL /purchase-orders, PurchaseOrdersPage, ~2359 dòng).
180. [reports.md](frontend-pages/reports.md) — Báo cáo nhân viên, in lại bill, doanh số. (URL /reports, Reports, ~2178 dòng).
181. [sales-staff.md](frontend-pages/sales-staff.md) — Nhân viên bán hàng (sales staff) gắn POS. (URL /sales-staff, SalesStaffPage, ~470 dòng).
182. [staff.md](frontend-pages/staff.md) — Quản lý tài khoản nhân viên (admin). (URL /staff, Staff, ~863 dòng).
183. [statistics.md](frontend-pages/statistics.md) — Thống kê bán theo sản phẩm/kỳ. (URL /statistics, Statistics, ~1208 dòng).
184. [stock-requests.md](frontend-pages/stock-requests.md) — Phiếu yêu cầu nhập/xuất nội bộ giữa shop. (URL /stock-requests, StockRequestsPage, ~1874 dòng).
185. [suppliers.md](frontend-pages/suppliers.md) — Danh mục nhà cung cấp. (URL /suppliers, SuppliersPage, ~593 dòng).
186. [system-reports.md](frontend-pages/system-reports.md) — Báo cáo hệ thống, sự kiện, lỗi. (URL /system-reports, SystemReportsPage, ~269 dòng).
187. [vat-inbound.md](frontend-pages/vat-inbound.md) — HĐ đầu vào VAT: import, kéo CQT, MST lọc, ghép SP, nhập kho. (URL /vat-inbound, VatInboundInvoices, ~5847 dòng).
188. [vat-invoice-public.md](frontend-pages/vat-invoice-public.md) — Form công khai tra cứu/xem HĐ VAT /vat-invoice. (URL /vat-invoice, VatInvoicePublicForm, ~689 dòng).
189. [vat-invoices.md](frontend-pages/vat-invoices.md) — Phát hành và quản lý HĐ VAT bán ra (Viettel). (URL /vat-invoices, VatInvoices, ~395 dòng).

## Database schema (từng file schema/*.ts) (43 mục)

190. [agentChat.md](schema/agentChat.md) — Drizzle schema agentChat.ts — 12 cột trên 2 bảng Postgres (agent_chat_threads, agent_chat_messages).
191. [allowedDevices.md](schema/allowedDevices.md) — Drizzle schema allowedDevices.ts — 8 cột trên 1 bảng Postgres (allowed_devices).
192. [blockedDevices.md](schema/blockedDevices.md) — Drizzle schema blockedDevices.ts — 5 cột trên 1 bảng Postgres (blocked_devices).
193. [blockedIps.md](schema/blockedIps.md) — Drizzle schema blockedIps.ts — 5 cột trên 1 bảng Postgres (blocked_ips).
194. [changeLog.md](schema/changeLog.md) — Drizzle schema changeLog.ts — 6 cột trên 1 bảng Postgres (change_log).
195. [customerFeedback.md](schema/customerFeedback.md) — Drizzle schema customerFeedback.ts — 8 cột trên 1 bảng Postgres (customer_feedback).
196. [deviceLoginEvents.md](schema/deviceLoginEvents.md) — Drizzle schema deviceLoginEvents.ts — 8 cột trên 1 bảng Postgres (device_login_events).
197. [inventory.md](schema/inventory.md) — Drizzle schema inventory.ts — 6 cột trên 1 bảng Postgres (inventory).
198. [inventoryMovements.md](schema/inventoryMovements.md) — Drizzle schema inventoryMovements.ts — 9 cột trên 1 bảng Postgres (inventory_movements).
199. [invoiceChangeLogs.md](schema/invoiceChangeLogs.md) — Drizzle schema invoiceChangeLogs.ts — 7 cột trên 1 bảng Postgres (invoice_change_logs).
200. [orderAuditLogs.md](schema/orderAuditLogs.md) — Drizzle schema orderAuditLogs.ts — 11 cột trên 1 bảng Postgres (order_audit_logs).
201. [orderItems.md](schema/orderItems.md) — Drizzle schema orderItems.ts — 13 cột trên 1 bảng Postgres (order_items).
202. [orderPreprintReservations.md](schema/orderPreprintReservations.md) — Drizzle schema orderPreprintReservations.ts — 10 cột trên 1 bảng Postgres (order_preprint_reservations).
203. [orderSyncKeys.md](schema/orderSyncKeys.md) — Drizzle schema orderSyncKeys.ts — 4 cột trên 1 bảng Postgres (order_sync_keys).
204. [orders.md](schema/orders.md) — Drizzle schema orders.ts — 39 cột trên 1 bảng Postgres (orders).
205. [orgGdtTaxSessions.md](schema/orgGdtTaxSessions.md) — Drizzle schema orgGdtTaxSessions.ts — 8 cột trên 1 bảng Postgres (org_gdt_tax_sessions).
206. [organizations.md](schema/organizations.md) — Drizzle schema organizations.ts — 39 cột trên 1 bảng Postgres (organizations).
207. [paymentChangeLogs.md](schema/paymentChangeLogs.md) — Drizzle schema paymentChangeLogs.ts — 8 cột trên 1 bảng Postgres (payment_change_logs).
208. [pinResetRequests.md](schema/pinResetRequests.md) — Drizzle schema pinResetRequests.ts — 8 cột trên 1 bảng Postgres (pin_reset_requests).
209. [platformNotificationSettings.md](schema/platformNotificationSettings.md) — Drizzle schema platformNotificationSettings.ts — 5 cột trên 1 bảng Postgres (platform_notification_settings).
210. [posCartAuditLogs.md](schema/posCartAuditLogs.md) — Drizzle schema posCartAuditLogs.ts — 17 cột trên 1 bảng Postgres (pos_cart_audit_logs).
211. [productAuditLogs.md](schema/productAuditLogs.md) — Drizzle schema productAuditLogs.ts — 9 cột trên 1 bảng Postgres (product_audit_logs).
212. [productCategories.md](schema/productCategories.md) — Drizzle schema productCategories.ts — 7 cột trên 1 bảng Postgres (product_categories).
213. [productVariants.md](schema/productVariants.md) — Drizzle schema productVariants.ts — 14 cột trên 1 bảng Postgres (product_variants).
214. [products.md](schema/products.md) — Drizzle schema products.ts — 21 cột trên 1 bảng Postgres (products).
215. [purchaseOrders.md](schema/purchaseOrders.md) — Drizzle schema purchaseOrders.ts — 32 cột trên 3 bảng Postgres (purchase_orders, purchase_order_items, purchase_order_logs).
216. [reprintLogs.md](schema/reprintLogs.md) — Drizzle schema reprintLogs.ts — 5 cột trên 1 bảng Postgres (reprint_logs).
217. [salesStaff.md](schema/salesStaff.md) — Drizzle schema salesStaff.ts — 13 cột trên 1 bảng Postgres (sales_staff).
218. [shiftSessions.md](schema/shiftSessions.md) — Drizzle schema shiftSessions.ts — 7 cột trên 2 bảng Postgres (shift_sessions, shift_session_staff).
219. [shopApiKeys.md](schema/shopApiKeys.md) — Drizzle schema shopApiKeys.ts — 9 cột trên 1 bảng Postgres (shop_api_keys).
220. [shopDailyVisitorCounts.md](schema/shopDailyVisitorCounts.md) — Drizzle schema shopDailyVisitorCounts.ts — 5 cột trên 1 bảng Postgres (shop_daily_visitor_counts).
221. [shopOperationalEvents.md](schema/shopOperationalEvents.md) — Drizzle schema shopOperationalEvents.ts — 6 cột trên 1 bảng Postgres (shop_operational_events).
222. [shopVariantStock.md](schema/shopVariantStock.md) — Drizzle schema shopVariantStock.ts — 5 cột trên 1 bảng Postgres (shop_variant_stock).
223. [shops.md](schema/shops.md) — Drizzle schema shops.ts — 31 cột trên 1 bảng Postgres (shops).
224. [stockRequests.md](schema/stockRequests.md) — Drizzle schema stockRequests.ts — 32 cột trên 3 bảng Postgres (stock_requests, stock_request_logs, stock_request_items).
225. [stockTransfers.md](schema/stockTransfers.md) — Drizzle schema stockTransfers.ts — 17 cột trên 2 bảng Postgres (stock_transfers, stock_transfer_items).
226. [suppliers.md](schema/suppliers.md) — Drizzle schema suppliers.ts — 12 cột trên 1 bảng Postgres (suppliers).
227. [systemEventLogs.md](schema/systemEventLogs.md) — Drizzle schema systemEventLogs.ts — 11 cột trên 1 bảng Postgres (system_event_logs).
228. [userNotifications.md](schema/userNotifications.md) — Drizzle schema userNotifications.ts — 11 cột trên 1 bảng Postgres (user_notifications).
229. [users.md](schema/users.md) — Drizzle schema users.ts — 13 cột trên 1 bảng Postgres (users).
230. [vatInboundAuditLogs.md](schema/vatInboundAuditLogs.md) — Drizzle schema vatInboundAuditLogs.ts — 8 cột trên 1 bảng Postgres (vat_inbound_audit_logs).
231. [vatInboundInvoices.md](schema/vatInboundInvoices.md) — Drizzle schema vatInboundInvoices.ts — 55 cột trên 1 bảng Postgres (vat_inbound_invoices).
232. [warehouses.md](schema/warehouses.md) — Drizzle schema warehouses.ts — 7 cột trên 1 bảng Postgres (warehouses).

## Reference mirror Shop (15 mục)

233. [api-routes.md](reference/api-routes.md) — Bản mirror doc Shop docs/api-routes.md — API routes.
234. [api-server.md](reference/api-server.md) — Bản mirror doc Shop docs/code-tour/api-server.md — Code tour — API server (artifacts/api-server).
235. [architecture.md](reference/architecture.md) — Bản mirror doc Shop docs/architecture.md — Architecture.
236. [business-flows.md](reference/business-flows.md) — Bản mirror doc Shop docs/business-flows.md — Business flows (how the system operates).
237. [code-annotations.md](reference/code-annotations.md) — Bản mirror doc Shop docs/code-annotations.md — Code annotations (high-signal).
238. [database.md](reference/database.md) — Bản mirror doc Shop docs/database.md — Database schema overview (Postgres + Drizzle).
239. [db.md](reference/db.md) — Bản mirror doc Shop docs/code-tour/db.md — Code tour — DB library (lib/db).
240. [docker-may-chu.md](reference/docker-may-chu.md) — Bản mirror doc Shop docs/docker-may-chu.md — Chạy VietPOS bằng Docker (DB + API + Web) và đóng gói .tar.
241. [offline-first-audit.md](reference/offline-first-audit.md) — Bản mirror doc Shop docs/offline-first-audit.md — Đánh giá mức độ Offline-First (audit).
242. [offline-first-roadmap.md](reference/offline-first-roadmap.md) — Bản mirror doc Shop docs/offline-first-roadmap.md — Roadmap: Offline-first toàn bộ ứng dụng.
243. [offline-first.md](reference/offline-first.md) — Bản mirror doc Shop docs/offline-first.md — Offline-first (PWA + IndexedDB).
244. [pos-app.md](reference/pos-app.md) — Bản mirror doc Shop docs/code-tour/pos-app.md — Code tour — POS web app (artifacts/pos-app).
245. [public-access.md](reference/public-access.md) — Bản mirror doc Shop docs/public-access.md — Public site local ra internet (cho người khác truy cập/test).
246. [rbac.md](reference/rbac.md) — Bản mirror doc Shop docs/rbac.md — RBAC (roles & permissions).
247. [running-local.md](reference/running-local.md) — Bản mirror doc Shop docs/running-local.md — Running locally (Windows + Docker).

---

## Chỉ mục API đầy đủ (235 endpoint)

Mỗi dòng trỏ tới file module; chi tiết handler nằm ở mục **Chi tiết từng endpoint** trong file đó.

1. `GET` `/api/access-observations` — Tổng hợp cặp (deviceId, IP) đã gọi API — lưu in-memory (TTL giờ, xem accessObservationTtlHours). -… — [`access-observations`](api-modules/access-observations.md)
2. `GET` `/api/agent/assistant-access` — Trợ lý AI: chat, system info (DB, cloud sync, shops online), cấp quyền agent_assistant_enabled. Fro… — [`agent`](api-modules/agent.md)
3. `PATCH` `/api/agent/assistant-access` — Trợ lý AI: chat, system info (DB, cloud sync, shops online), cấp quyền agent_assistant_enabled. Fro… — [`agent`](api-modules/agent.md)
4. `POST` `/api/agent/chat` — Trợ lý AI: chat, system info (DB, cloud sync, shops online), cấp quyền agent_assistant_enabled. Fro… — [`agent`](api-modules/agent.md)
5. `GET` `/api/agent/chat/audit/threads` — Trợ lý AI: chat, system info (DB, cloud sync, shops online), cấp quyền agent_assistant_enabled. Fro… — [`agent`](api-modules/agent.md)
6. `DELETE` `/api/agent/chat/audit/threads/:threadId` — Trợ lý AI: chat, system info (DB, cloud sync, shops online), cấp quyền agent_assistant_enabled. Fro… — [`agent`](api-modules/agent.md)
7. `GET` `/api/agent/chat/audit/threads/:threadId/messages` — Trợ lý AI: chat, system info (DB, cloud sync, shops online), cấp quyền agent_assistant_enabled. Fro… — [`agent`](api-modules/agent.md)
8. `DELETE` `/api/agent/chat/history` — Trợ lý AI: chat, system info (DB, cloud sync, shops online), cấp quyền agent_assistant_enabled. Fro… — [`agent`](api-modules/agent.md)
9. `GET` `/api/agent/chat/history` — Trợ lý AI: chat, system info (DB, cloud sync, shops online), cấp quyền agent_assistant_enabled. Fro… — [`agent`](api-modules/agent.md)
10. `GET` `/api/agent/chat/status` — Trợ lý AI: chat, system info (DB, cloud sync, shops online), cấp quyền agent_assistant_enabled. Fro… — [`agent`](api-modules/agent.md)
11. `GET` `/api/agent/chat/system` — Trợ lý AI: chat, system info (DB, cloud sync, shops online), cấp quyền agent_assistant_enabled. Fro… — [`agent`](api-modules/agent.md)
12. `POST` `/api/auth/login` — REST `POST` trên module `auth`. — [`auth`](api-modules/auth.md)
13. `POST` `/api/auth/logout` — REST `POST` trên module `auth`. — [`auth`](api-modules/auth.md)
14. `GET` `/api/auth/me` — REST `GET` trên module `auth`. — [`auth`](api-modules/auth.md)
15. `POST` `/api/auth/pin/device` — REST `POST` trên module `auth`. — [`auth`](api-modules/auth.md)
16. `POST` `/api/auth/pin/forgot-request` — REST `POST` trên module `auth`. — [`auth`](api-modules/auth.md)
17. `POST` `/api/auth/pin/set` — REST `POST` trên module `auth`. — [`auth`](api-modules/auth.md)
18. `POST` `/api/auth/pin/setup` — REST `POST` trên module `auth`. — [`auth`](api-modules/auth.md)
19. `POST` `/api/auth/pin/verify` — REST `POST` trên module `auth`. — [`auth`](api-modules/auth.md)
20. `GET` `/api/blocked-devices` — Danh sách Device ID (header client) bị chặn mọi /api/*. - Quyền: super_admin (giống blocked-ips). -… — [`blocked-devices`](api-modules/blocked-devices.md)
21. `POST` `/api/blocked-devices` — Danh sách Device ID (header client) bị chặn mọi /api/*. - Quyền: super_admin (giống blocked-ips). -… — [`blocked-devices`](api-modules/blocked-devices.md)
22. `DELETE` `/api/blocked-devices/:id` — Danh sách Device ID (header client) bị chặn mọi /api/*. - Quyền: super_admin (giống blocked-ips). -… — [`blocked-devices`](api-modules/blocked-devices.md)
23. `GET` `/api/blocked-ips` — Danh sách IP bị chặn toàn cục trên mọi request /api/*. - Quyền: requireAuth + role super_admin (403… — [`blocked-ips`](api-modules/blocked-ips.md)
24. `POST` `/api/blocked-ips` — Danh sách IP bị chặn toàn cục trên mọi request /api/*. - Quyền: requireAuth + role super_admin (403… — [`blocked-ips`](api-modules/blocked-ips.md)
25. `DELETE` `/api/blocked-ips/:id` — Danh sách IP bị chặn toàn cục trên mọi request /api/*. - Quyền: requireAuth + role super_admin (403… — [`blocked-ips`](api-modules/blocked-ips.md)
26. `GET` `/api/chain-dashboard` — REST `GET` trên module `dashboard`. — [`dashboard`](api-modules/dashboard.md)
27. `GET` `/api/chain-dashboard/low-stock` — REST `GET` trên module `dashboard`. — [`dashboard`](api-modules/dashboard.md)
28. `GET` `/api/chain-dashboard/orders-today` — REST `GET` trên module `dashboard`. — [`dashboard`](api-modules/dashboard.md)
29. `GET` `/api/chain-dashboard/orders-yesterday` — REST `GET` trên module `dashboard`. — [`dashboard`](api-modules/dashboard.md)
30. `GET` `/api/chain-dashboard/period-cancel-stats` — REST `GET` trên module `dashboard`. — [`dashboard`](api-modules/dashboard.md)
31. `GET` `/api/chain-dashboard/period-sold-stats` — REST `GET` trên module `dashboard`. — [`dashboard`](api-modules/dashboard.md)
32. `GET` `/api/chain-dashboard/period-visitor-stats` — REST `GET` trên module `dashboard`. — [`dashboard`](api-modules/dashboard.md)
33. `GET` `/api/chain-dashboard/revenue-chart` — REST `GET` trên module `dashboard`. — [`dashboard`](api-modules/dashboard.md)
34. `GET` `/api/chain-dashboard/top-products` — REST `GET` trên module `dashboard`. — [`dashboard`](api-modules/dashboard.md)
35. `GET` `/api/dashboard` — REST `GET` trên module `dashboard`. — [`dashboard`](api-modules/dashboard.md)
36. `GET` `/api/dashboard/low-stock` — REST `GET` trên module `dashboard`. — [`dashboard`](api-modules/dashboard.md)
37. `GET` `/api/dashboard/orders-today` — REST `GET` trên module `dashboard`. — [`dashboard`](api-modules/dashboard.md)
38. `GET` `/api/dashboard/period-cancel-stats` — REST `GET` trên module `dashboard`. — [`dashboard`](api-modules/dashboard.md)
39. `GET` `/api/dashboard/period-sold-stats` — REST `GET` trên module `dashboard`. — [`dashboard`](api-modules/dashboard.md)
40. `GET` `/api/dashboard/period-visitor-stats` — REST `GET` trên module `dashboard`. — [`dashboard`](api-modules/dashboard.md)
41. `GET` `/api/dashboard/revenue-chart` — REST `GET` trên module `dashboard`. — [`dashboard`](api-modules/dashboard.md)
42. `GET` `/api/dashboard/top-products` — REST `GET` trên module `dashboard`. — [`dashboard`](api-modules/dashboard.md)
43. `GET` `/api/feedback` — REST `GET` trên module `feedback`. — [`feedback`](api-modules/feedback.md)
44. `GET` `/api/feedback/public-url` — REST `GET` trên module `feedback`. — [`feedback`](api-modules/feedback.md)
45. `PATCH` `/api/feedback/public-url` — REST `PATCH` trên module `feedback`. — [`feedback`](api-modules/feedback.md)
46. `GET` `/api/feedback/stats` — REST `GET` trên module `feedback`. — [`feedback`](api-modules/feedback.md)
47. `GET` `/api/healthz` — REST `GET` trên module `health`. — [`health`](api-modules/health.md)
48. `GET` `/api/inventory` — REST `GET` trên module `inventory`. — [`inventory`](api-modules/inventory.md)
49. `PATCH` `/api/inventory/:productId` — REST `PATCH` trên module `inventory`. — [`inventory`](api-modules/inventory.md)
50. `GET` `/api/media` — REST `GET` trên module `media`. — [`media`](api-modules/media.md)
51. `GET` `/api/notification-settings` — REST `GET` trên module `notification-settings`. — [`notification-settings`](api-modules/notification-settings.md)
52. `PATCH` `/api/notification-settings` — REST `PATCH` trên module `notification-settings`. — [`notification-settings`](api-modules/notification-settings.md)
53. `GET` `/api/notifications` — REST `GET` trên module `notifications`. — [`notifications`](api-modules/notifications.md)
54. `POST` `/api/notifications/read` — REST `POST` trên module `notifications`. — [`notifications`](api-modules/notifications.md)
55. `GET` `/api/orders` — Đơn hàng POS: tạo, hủy, duyệt hủy, in lại, thông báo reprint. Gắn ca (shift-sessions), audit cart.… — [`orders`](api-modules/orders.md)
56. `POST` `/api/orders` — Đơn hàng POS: tạo, hủy, duyệt hủy, in lại, thông báo reprint. Gắn ca (shift-sessions), audit cart.… — [`orders`](api-modules/orders.md)
57. `GET` `/api/orders/:id` — Đơn hàng POS: tạo, hủy, duyệt hủy, in lại, thông báo reprint. Gắn ca (shift-sessions), audit cart.… — [`orders`](api-modules/orders.md)
58. `PATCH` `/api/orders/:id/approve-cancel` — Đơn hàng POS: tạo, hủy, duyệt hủy, in lại, thông báo reprint. Gắn ca (shift-sessions), audit cart.… — [`orders`](api-modules/orders.md)
59. `GET` `/api/orders/:id/audit-logs` — Đơn hàng POS: tạo, hủy, duyệt hủy, in lại, thông báo reprint. Gắn ca (shift-sessions), audit cart.… — [`orders`](api-modules/orders.md)
60. `PATCH` `/api/orders/:id/cancel` — Đơn hàng POS: tạo, hủy, duyệt hủy, in lại, thông báo reprint. Gắn ca (shift-sessions), audit cart.… — [`orders`](api-modules/orders.md)
61. `PATCH` `/api/orders/:id/invoice` — Đơn hàng POS: tạo, hủy, duyệt hủy, in lại, thông báo reprint. Gắn ca (shift-sessions), audit cart.… — [`orders`](api-modules/orders.md)
62. `GET` `/api/orders/:id/invoice-logs` — Đơn hàng POS: tạo, hủy, duyệt hủy, in lại, thông báo reprint. Gắn ca (shift-sessions), audit cart.… — [`orders`](api-modules/orders.md)
63. `PATCH` `/api/orders/:id/invoice/issue` — Đơn hàng POS: tạo, hủy, duyệt hủy, in lại, thông báo reprint. Gắn ca (shift-sessions), audit cart.… — [`orders`](api-modules/orders.md)
64. `GET` `/api/orders/:id/invoice/pdf` — Đơn hàng POS: tạo, hủy, duyệt hủy, in lại, thông báo reprint. Gắn ca (shift-sessions), audit cart.… — [`orders`](api-modules/orders.md)
65. `PATCH` `/api/orders/:id/note` — Đơn hàng POS: tạo, hủy, duyệt hủy, in lại, thông báo reprint. Gắn ca (shift-sessions), audit cart.… — [`orders`](api-modules/orders.md)
66. `POST` `/api/orders/:id/notify-oversight` — Đơn hàng POS: tạo, hủy, duyệt hủy, in lại, thông báo reprint. Gắn ca (shift-sessions), audit cart.… — [`orders`](api-modules/orders.md)
67. `POST` `/api/orders/:id/notify-reprint` — Đơn hàng POS: tạo, hủy, duyệt hủy, in lại, thông báo reprint. Gắn ca (shift-sessions), audit cart.… — [`orders`](api-modules/orders.md)
68. `PATCH` `/api/orders/:id/payment` — Đơn hàng POS: tạo, hủy, duyệt hủy, in lại, thông báo reprint. Gắn ca (shift-sessions), audit cart.… — [`orders`](api-modules/orders.md)
69. `GET` `/api/orders/:id/payment-logs` — Đơn hàng POS: tạo, hủy, duyệt hủy, in lại, thông báo reprint. Gắn ca (shift-sessions), audit cart.… — [`orders`](api-modules/orders.md)
70. `PATCH` `/api/orders/:id/product-proof` — Đơn hàng POS: tạo, hủy, duyệt hủy, in lại, thông báo reprint. Gắn ca (shift-sessions), audit cart.… — [`orders`](api-modules/orders.md)
71. `PATCH` `/api/orders/:id/reject-cancel` — Đơn hàng POS: tạo, hủy, duyệt hủy, in lại, thông báo reprint. Gắn ca (shift-sessions), audit cart.… — [`orders`](api-modules/orders.md)
72. `PATCH` `/api/orders/:id/uncancel` — Đơn hàng POS: tạo, hủy, duyệt hủy, in lại, thông báo reprint. Gắn ca (shift-sessions), audit cart.… — [`orders`](api-modules/orders.md)
73. `GET` `/api/orders/period-summary` — Đơn hàng POS: tạo, hủy, duyệt hủy, in lại, thông báo reprint. Gắn ca (shift-sessions), audit cart.… — [`orders`](api-modules/orders.md)
74. `POST` `/api/orders/preprint` — Đơn hàng POS: tạo, hủy, duyệt hủy, in lại, thông báo reprint. Gắn ca (shift-sessions), audit cart.… — [`orders`](api-modules/orders.md)
75. `GET` `/api/orders/vat-queue-counts` — Đơn hàng POS: tạo, hủy, duyệt hủy, in lại, thông báo reprint. Gắn ca (shift-sessions), audit cart.… — [`orders`](api-modules/orders.md)
76. `GET` `/api/organizations` — Tổ chức, shop, kho, điều chuyển (transfers). Cấu hình org (Viettel, CQT, feedback URL, agent LLM).… — [`chain`](api-modules/chain.md)
77. `POST` `/api/organizations` — Tổ chức, shop, kho, điều chuyển (transfers). Cấu hình org (Viettel, CQT, feedback URL, agent LLM).… — [`chain`](api-modules/chain.md)
78. `PATCH` `/api/organizations/:id` — Tổ chức, shop, kho, điều chuyển (transfers). Cấu hình org (Viettel, CQT, feedback URL, agent LLM).… — [`chain`](api-modules/chain.md)
79. `POST` `/api/organizations/:orgId/gdt/captcha` — Session CQT trực tiếp (captcha, connect) — dùng chung org với HĐ đầu vào. — [`org-gdt-portal`](api-modules/org-gdt-portal.md)
80. `POST` `/api/organizations/:orgId/gdt/disconnect` — Session CQT trực tiếp (captcha, connect) — dùng chung org với HĐ đầu vào. — [`org-gdt-portal`](api-modules/org-gdt-portal.md)
81. `GET` `/api/organizations/:orgId/gdt/status` — Session CQT trực tiếp (captcha, connect) — dùng chung org với HĐ đầu vào. — [`org-gdt-portal`](api-modules/org-gdt-portal.md)
82. `POST` `/api/organizations/:orgId/gdt/test-connect` — Session CQT trực tiếp (captcha, connect) — dùng chung org với HĐ đầu vào. — [`org-gdt-portal`](api-modules/org-gdt-portal.md)
83. `PUT` `/api/organizations/:orgId/shop-display-order` — Tổ chức, shop, kho, điều chuyển (transfers). Cấu hình org (Viettel, CQT, feedback URL, agent LLM).… — [`chain`](api-modules/chain.md)
84. `GET` `/api/organizations/current` — Tổ chức, shop, kho, điều chuyển (transfers). Cấu hình org (Viettel, CQT, feedback URL, agent LLM).… — [`chain`](api-modules/chain.md)
85. `POST` `/api/pos/cart-audit` — REST `POST` trên module `pos-cart-audit`. — [`pos-cart-audit`](api-modules/pos-cart-audit.md)
86. `GET` `/api/product-categories` — REST `GET` trên module `product-categories`. — [`product-categories`](api-modules/product-categories.md)
87. `POST` `/api/product-categories` — REST `POST` trên module `product-categories`. — [`product-categories`](api-modules/product-categories.md)
88. `PATCH` `/api/product-categories/:id` — REST `PATCH` trên module `product-categories`. — [`product-categories`](api-modules/product-categories.md)
89. `GET` `/api/products` — CRUD sản phẩm, import Excel, variant, ẩn/hiện SP, giá/giá vốn theo role. Frontend: pages/products.t… — [`products`](api-modules/products.md)
90. `POST` `/api/products` — CRUD sản phẩm, import Excel, variant, ẩn/hiện SP, giá/giá vốn theo role. Frontend: pages/products.t… — [`products`](api-modules/products.md)
91. `DELETE` `/api/products/:id` — CRUD sản phẩm, import Excel, variant, ẩn/hiện SP, giá/giá vốn theo role. Frontend: pages/products.t… — [`products`](api-modules/products.md)
92. `GET` `/api/products/:id` — CRUD sản phẩm, import Excel, variant, ẩn/hiện SP, giá/giá vốn theo role. Frontend: pages/products.t… — [`products`](api-modules/products.md)
93. `PATCH` `/api/products/:id` — CRUD sản phẩm, import Excel, variant, ẩn/hiện SP, giá/giá vốn theo role. Frontend: pages/products.t… — [`products`](api-modules/products.md)
94. `POST` `/api/products/:id/variants` — CRUD sản phẩm, import Excel, variant, ẩn/hiện SP, giá/giá vốn theo role. Frontend: pages/products.t… — [`products`](api-modules/products.md)
95. `DELETE` `/api/products/:id/variants/:variantId` — CRUD sản phẩm, import Excel, variant, ẩn/hiện SP, giá/giá vốn theo role. Frontend: pages/products.t… — [`products`](api-modules/products.md)
96. `PATCH` `/api/products/:id/variants/:variantId` — CRUD sản phẩm, import Excel, variant, ẩn/hiện SP, giá/giá vốn theo role. Frontend: pages/products.t… — [`products`](api-modules/products.md)
97. `POST` `/api/products/import` — CRUD sản phẩm, import Excel, variant, ẩn/hiện SP, giá/giá vốn theo role. Frontend: pages/products.t… — [`products`](api-modules/products.md)
98. `GET` `/api/products/product-sales` — CRUD sản phẩm, import Excel, variant, ẩn/hiện SP, giá/giá vốn theo role. Frontend: pages/products.t… — [`products`](api-modules/products.md)
99. `GET` `/api/products/variant-sales` — CRUD sản phẩm, import Excel, variant, ẩn/hiện SP, giá/giá vốn theo role. Frontend: pages/products.t… — [`products`](api-modules/products.md)
100. `POST` `/api/public/feedback` — REST `POST` trên module `feedback`. — [`feedback`](api-modules/feedback.md)
101. `GET` `/api/public/vat-invoice` — REST `GET` trên module `public-vat-invoice`. — [`public-vat-invoice`](api-modules/public-vat-invoice.md)
102. `PATCH` `/api/public/vat-invoice` — REST `PATCH` trên module `public-vat-invoice`. — [`public-vat-invoice`](api-modules/public-vat-invoice.md)
103. `GET` `/api/public/vat-invoice/pdf` — REST `GET` trên module `public-vat-invoice`. — [`public-vat-invoice`](api-modules/public-vat-invoice.md)
104. `GET` `/api/purchase-orders` — REST `GET` trên module `purchase-orders`. — [`purchase-orders`](api-modules/purchase-orders.md)
105. `POST` `/api/purchase-orders` — REST `POST` trên module `purchase-orders`. — [`purchase-orders`](api-modules/purchase-orders.md)
106. `GET` `/api/purchase-orders/:id` — REST `GET` trên module `purchase-orders`. — [`purchase-orders`](api-modules/purchase-orders.md)
107. `PATCH` `/api/purchase-orders/:id` — REST `PATCH` trên module `purchase-orders`. — [`purchase-orders`](api-modules/purchase-orders.md)
108. `PATCH` `/api/purchase-orders/:id/cancel` — REST `PATCH` trên module `purchase-orders`. — [`purchase-orders`](api-modules/purchase-orders.md)
109. `PATCH` `/api/purchase-orders/:id/close-short` — REST `PATCH` trên module `purchase-orders`. — [`purchase-orders`](api-modules/purchase-orders.md)
110. `PATCH` `/api/purchase-orders/:id/receive` — REST `PATCH` trên module `purchase-orders`. — [`purchase-orders`](api-modules/purchase-orders.md)
111. `PATCH` `/api/purchase-orders/:id/send` — REST `PATCH` trên module `purchase-orders`. — [`purchase-orders`](api-modules/purchase-orders.md)
112. `GET` `/api/purchase-orders/sales-hints` — REST `GET` trên module `purchase-orders`. — [`purchase-orders`](api-modules/purchase-orders.md)
113. `GET` `/api/reports/order-audit` — REST `GET` trên module `order-audit-reports`. — [`order-audit-reports`](api-modules/order-audit-reports.md)
114. `GET` `/api/reports/order-audit/summary` — REST `GET` trên module `order-audit-reports`. — [`order-audit-reports`](api-modules/order-audit-reports.md)
115. `GET` `/api/reports/pos-cart-audit` — REST `GET` trên module `pos-cart-audit`. — [`pos-cart-audit`](api-modules/pos-cart-audit.md)
116. `GET` `/api/reports/pos-cart-audit/summary` — REST `GET` trên module `pos-cart-audit`. — [`pos-cart-audit`](api-modules/pos-cart-audit.md)
117. `GET` `/api/reports/product-audit` — REST `GET` trên module `product-audit-reports`. — [`product-audit-reports`](api-modules/product-audit-reports.md)
118. `GET` `/api/reports/product-audit/summary` — REST `GET` trên module `product-audit-reports`. — [`product-audit-reports`](api-modules/product-audit-reports.md)
119. `GET` `/api/reports/purchase-order-audit` — REST `GET` trên module `purchase-order-audit-reports`. — [`purchase-order-audit-reports`](api-modules/purchase-order-audit-reports.md)
120. `GET` `/api/reports/purchase-order-audit/summary` — REST `GET` trên module `purchase-order-audit-reports`. — [`purchase-order-audit-reports`](api-modules/purchase-order-audit-reports.md)
121. `GET` `/api/reports/reprints` — REST `GET` trên module `reports`. — [`reports`](api-modules/reports.md)
122. `GET` `/api/reports/sales-staff` — REST `GET` trên module `reports`. — [`reports`](api-modules/reports.md)
123. `GET` `/api/reports/staff` — REST `GET` trên module `reports`. — [`reports`](api-modules/reports.md)
124. `GET` `/api/reports/staff/:userId/detail` — REST `GET` trên module `reports`. — [`reports`](api-modules/reports.md)
125. `GET` `/api/reports/stock-request-audit` — REST `GET` trên module `stock-request-audit-reports`. — [`stock-request-audit-reports`](api-modules/stock-request-audit-reports.md)
126. `GET` `/api/reports/stock-request-audit/summary` — REST `GET` trên module `stock-request-audit-reports`. — [`stock-request-audit-reports`](api-modules/stock-request-audit-reports.md)
127. `GET` `/api/sales-staff` — REST `GET` trên module `sales-staff`. — [`sales-staff`](api-modules/sales-staff.md)
128. `POST` `/api/sales-staff` — REST `POST` trên module `sales-staff`. — [`sales-staff`](api-modules/sales-staff.md)
129. `GET` `/api/sales-staff/:id` — REST `GET` trên module `sales-staff`. — [`sales-staff`](api-modules/sales-staff.md)
130. `PATCH` `/api/sales-staff/:id` — REST `PATCH` trên module `sales-staff`. — [`sales-staff`](api-modules/sales-staff.md)
131. `POST` `/api/shift-sessions` — REST `POST` trên module `shift-sessions`. — [`shift-sessions`](api-modules/shift-sessions.md)
132. `PATCH` `/api/shift-sessions/:id/end` — REST `PATCH` trên module `shift-sessions`. — [`shift-sessions`](api-modules/shift-sessions.md)
133. `GET` `/api/shift-sessions/current` — REST `GET` trên module `shift-sessions`. — [`shift-sessions`](api-modules/shift-sessions.md)
134. `GET` `/api/shop-api-keys` — API key cho widget / thiết bị (ESP32 visitor-counts). Frontend: pages/chain-api-keys.tsx (nếu có). — [`shop-api-keys`](api-modules/shop-api-keys.md)
135. `POST` `/api/shop-api-keys` — API key cho widget / thiết bị (ESP32 visitor-counts). Frontend: pages/chain-api-keys.tsx (nếu có). — [`shop-api-keys`](api-modules/shop-api-keys.md)
136. `DELETE` `/api/shop-api-keys/:id` — API key cho widget / thiết bị (ESP32 visitor-counts). Frontend: pages/chain-api-keys.tsx (nếu có). — [`shop-api-keys`](api-modules/shop-api-keys.md)
137. `PATCH` `/api/shop-api-keys/:id` — API key cho widget / thiết bị (ESP32 visitor-counts). Frontend: pages/chain-api-keys.tsx (nếu có). — [`shop-api-keys`](api-modules/shop-api-keys.md)
138. `GET` `/api/shop-api-keys/overview` — API key cho widget / thiết bị (ESP32 visitor-counts). Frontend: pages/chain-api-keys.tsx (nếu có). — [`shop-api-keys`](api-modules/shop-api-keys.md)
139. `PATCH` `/api/shop-api-keys/shops/:shopId` — API key cho widget / thiết bị (ESP32 visitor-counts). Frontend: pages/chain-api-keys.tsx (nếu có). — [`shop-api-keys`](api-modules/shop-api-keys.md)
140. `GET` `/api/shops` — REST `GET` trên module `shops`. — [`shops`](api-modules/shops.md)
141. `POST` `/api/shops` — Tổ chức, shop, kho, điều chuyển (transfers). Cấu hình org (Viettel, CQT, feedback URL, agent LLM).… — [`chain`](api-modules/chain.md)
142. `PATCH` `/api/shops/:id` — Tổ chức, shop, kho, điều chuyển (transfers). Cấu hình org (Viettel, CQT, feedback URL, agent LLM).… — [`chain`](api-modules/chain.md)
143. `PATCH` `/api/shops/:id/admin-email` — Tổ chức, shop, kho, điều chuyển (transfers). Cấu hình org (Viettel, CQT, feedback URL, agent LLM).… — [`chain`](api-modules/chain.md)
144. `POST` `/api/shops/:id/create-admin` — Tổ chức, shop, kho, điều chuyển (transfers). Cấu hình org (Viettel, CQT, feedback URL, agent LLM).… — [`chain`](api-modules/chain.md)
145. `GET` `/api/shops/:id/devices` — Tổ chức, shop, kho, điều chuyển (transfers). Cấu hình org (Viettel, CQT, feedback URL, agent LLM).… — [`chain`](api-modules/chain.md)
146. `PATCH` `/api/shops/:id/devices/:deviceRowId` — Tổ chức, shop, kho, điều chuyển (transfers). Cấu hình org (Viettel, CQT, feedback URL, agent LLM).… — [`chain`](api-modules/chain.md)
147. `GET` `/api/shops/:id/devices/:deviceRowId/login-events` — Tổ chức, shop, kho, điều chuyển (transfers). Cấu hình org (Viettel, CQT, feedback URL, agent LLM).… — [`chain`](api-modules/chain.md)
148. `POST` `/api/shops/:id/devices/register` — Tổ chức, shop, kho, điều chuyển (transfers). Cấu hình org (Viettel, CQT, feedback URL, agent LLM).… — [`chain`](api-modules/chain.md)
149. `PATCH` `/api/shops/:id/reset-password` — Tổ chức, shop, kho, điều chuyển (transfers). Cấu hình org (Viettel, CQT, feedback URL, agent LLM).… — [`chain`](api-modules/chain.md)
150. `POST` `/api/shops/:shopId/walk-in-customers` — REST `POST` trên module `walk-in-customers`. — [`walk-in-customers`](api-modules/walk-in-customers.md)
151. `GET` `/api/shops/:shopId/walk-in-customers/today` — REST `GET` trên module `walk-in-customers`. — [`walk-in-customers`](api-modules/walk-in-customers.md)
152. `POST` `/api/shops/heartbeat` — REST `POST` trên module `shops`. — [`shops`](api-modules/shops.md)
153. `GET` `/api/shops/operational-events` — REST `GET` trên module `shops`. — [`shops`](api-modules/shops.md)
154. `GET` `/api/staff` — REST `GET` trên module `staff`. — [`staff`](api-modules/staff.md)
155. `POST` `/api/staff` — REST `POST` trên module `staff`. — [`staff`](api-modules/staff.md)
156. `DELETE` `/api/staff/:id` — REST `DELETE` trên module `staff`. — [`staff`](api-modules/staff.md)
157. `PATCH` `/api/staff/:id` — REST `PATCH` trên module `staff`. — [`staff`](api-modules/staff.md)
158. `GET` `/api/staff/pin-reset-requests` — REST `GET` trên module `staff`. — [`staff`](api-modules/staff.md)
159. `POST` `/api/staff/pin-reset-requests/:id/dismiss` — REST `POST` trên module `staff`. — [`staff`](api-modules/staff.md)
160. `POST` `/api/staff/pin-reset-requests/:id/resolve` — REST `POST` trên module `staff`. — [`staff`](api-modules/staff.md)
161. `GET` `/api/statistics/catalog` — REST `GET` trên module `statistics`. — [`statistics`](api-modules/statistics.md)
162. `GET` `/api/statistics/overview` — REST `GET` trên module `statistics`. — [`statistics`](api-modules/statistics.md)
163. `GET` `/api/statistics/product-sales` — REST `GET` trên module `statistics`. — [`statistics`](api-modules/statistics.md)
164. `GET` `/api/statistics/products` — REST `GET` trên module `statistics`. — [`statistics`](api-modules/statistics.md)
165. `GET` `/api/statistics/top-products` — REST `GET` trên module `statistics`. — [`statistics`](api-modules/statistics.md)
166. `GET` `/api/statistics/trend` — REST `GET` trên module `statistics`. — [`statistics`](api-modules/statistics.md)
167. `GET` `/api/stock-requests` — Phiếu yêu cầu nhập/xuất nội bộ: tạo → duyệt → hoàn tất → cập nhật tồn. Frontend: pages/stock-reques… — [`stock-requests`](api-modules/stock-requests.md)
168. `POST` `/api/stock-requests` — Phiếu yêu cầu nhập/xuất nội bộ: tạo → duyệt → hoàn tất → cập nhật tồn. Frontend: pages/stock-reques… — [`stock-requests`](api-modules/stock-requests.md)
169. `GET` `/api/stock-requests/:id` — Phiếu yêu cầu nhập/xuất nội bộ: tạo → duyệt → hoàn tất → cập nhật tồn. Frontend: pages/stock-reques… — [`stock-requests`](api-modules/stock-requests.md)
170. `PATCH` `/api/stock-requests/:id/approve` — Phiếu yêu cầu nhập/xuất nội bộ: tạo → duyệt → hoàn tất → cập nhật tồn. Frontend: pages/stock-reques… — [`stock-requests`](api-modules/stock-requests.md)
171. `PATCH` `/api/stock-requests/:id/cancel` — Phiếu yêu cầu nhập/xuất nội bộ: tạo → duyệt → hoàn tất → cập nhật tồn. Frontend: pages/stock-reques… — [`stock-requests`](api-modules/stock-requests.md)
172. `PATCH` `/api/stock-requests/:id/complete` — Phiếu yêu cầu nhập/xuất nội bộ: tạo → duyệt → hoàn tất → cập nhật tồn. Frontend: pages/stock-reques… — [`stock-requests`](api-modules/stock-requests.md)
173. `PATCH` `/api/stock-requests/:id/reject` — Phiếu yêu cầu nhập/xuất nội bộ: tạo → duyệt → hoàn tất → cập nhật tồn. Frontend: pages/stock-reques… — [`stock-requests`](api-modules/stock-requests.md)
174. `PATCH` `/api/stock-requests/:id/ship` — Phiếu yêu cầu nhập/xuất nội bộ: tạo → duyệt → hoàn tất → cập nhật tồn. Frontend: pages/stock-reques… — [`stock-requests`](api-modules/stock-requests.md)
175. `GET` `/api/stock-requests/approved-count` — Phiếu yêu cầu nhập/xuất nội bộ: tạo → duyệt → hoàn tất → cập nhật tồn. Frontend: pages/stock-reques… — [`stock-requests`](api-modules/stock-requests.md)
176. `GET` `/api/stock-requests/in-transit-count` — Phiếu yêu cầu nhập/xuất nội bộ: tạo → duyệt → hoàn tất → cập nhật tồn. Frontend: pages/stock-reques… — [`stock-requests`](api-modules/stock-requests.md)
177. `GET` `/api/stock-requests/meta/hub-inventory` — Phiếu yêu cầu nhập/xuất nội bộ: tạo → duyệt → hoàn tất → cập nhật tồn. Frontend: pages/stock-reques… — [`stock-requests`](api-modules/stock-requests.md)
178. `GET` `/api/stock-requests/meta/hub-shop` — Phiếu yêu cầu nhập/xuất nội bộ: tạo → duyệt → hoàn tất → cập nhật tồn. Frontend: pages/stock-reques… — [`stock-requests`](api-modules/stock-requests.md)
179. `GET` `/api/stock-requests/meta/shop-inventory` — Phiếu yêu cầu nhập/xuất nội bộ: tạo → duyệt → hoàn tất → cập nhật tồn. Frontend: pages/stock-reques… — [`stock-requests`](api-modules/stock-requests.md)
180. `GET` `/api/stock-requests/pending-count` — Phiếu yêu cầu nhập/xuất nội bộ: tạo → duyệt → hoàn tất → cập nhật tồn. Frontend: pages/stock-reques… — [`stock-requests`](api-modules/stock-requests.md)
181. `GET` `/api/suppliers` — REST `GET` trên module `suppliers`. — [`suppliers`](api-modules/suppliers.md)
182. `POST` `/api/suppliers` — REST `POST` trên module `suppliers`. — [`suppliers`](api-modules/suppliers.md)
183. `GET` `/api/suppliers/:id` — REST `GET` trên module `suppliers`. — [`suppliers`](api-modules/suppliers.md)
184. `PATCH` `/api/suppliers/:id` — REST `PATCH` trên module `suppliers`. — [`suppliers`](api-modules/suppliers.md)
185. `GET` `/api/sync/catalog` — Endpoint đồng bộ client (pull/push) cho offline IndexedDB. — [`sync`](api-modules/sync.md)
186. `GET` `/api/sync/shift-orders` — Endpoint đồng bộ client (pull/push) cho offline IndexedDB. — [`sync`](api-modules/sync.md)
187. `GET` `/api/system-events` — REST `GET` trên module `system-events`. — [`system-events`](api-modules/system-events.md)
188. `GET` `/api/transfers` — Tổ chức, shop, kho, điều chuyển (transfers). Cấu hình org (Viettel, CQT, feedback URL, agent LLM).… — [`chain`](api-modules/chain.md)
189. `POST` `/api/transfers` — Tổ chức, shop, kho, điều chuyển (transfers). Cấu hình org (Viettel, CQT, feedback URL, agent LLM).… — [`chain`](api-modules/chain.md)
190. `DELETE` `/api/transfers/:id` — Tổ chức, shop, kho, điều chuyển (transfers). Cấu hình org (Viettel, CQT, feedback URL, agent LLM).… — [`chain`](api-modules/chain.md)
191. `PATCH` `/api/transfers/:id` — Tổ chức, shop, kho, điều chuyển (transfers). Cấu hình org (Viettel, CQT, feedback URL, agent LLM).… — [`chain`](api-modules/chain.md)
192. `POST` `/api/transfers/:id/approve` — Tổ chức, shop, kho, điều chuyển (transfers). Cấu hình org (Viettel, CQT, feedback URL, agent LLM).… — [`chain`](api-modules/chain.md)
193. `GET` `/api/transfers/:id/items` — Tổ chức, shop, kho, điều chuyển (transfers). Cấu hình org (Viettel, CQT, feedback URL, agent LLM).… — [`chain`](api-modules/chain.md)
194. `POST` `/api/transfers/:id/receive` — Tổ chức, shop, kho, điều chuyển (transfers). Cấu hình org (Viettel, CQT, feedback URL, agent LLM).… — [`chain`](api-modules/chain.md)
195. `POST` `/api/transfers/:id/ship` — Tổ chức, shop, kho, điều chuyển (transfers). Cấu hình org (Viettel, CQT, feedback URL, agent LLM).… — [`chain`](api-modules/chain.md)
196. `GET` `/api/vat-inbound` — Danh sách HĐ mua vào của hub shop; không trả pdfBase64 (chỉ cờ hasPdf); tự relink PO nếu thiếu; join trạng thái PO. — [`vat-inbound`](api-modules/vat-inbound.md)
197. `POST` `/api/vat-inbound` — Upsert HĐ (import PDF/Excel từ client); parse fields; sync archive MST on write. — [`vat-inbound`](api-modules/vat-inbound.md)
198. `DELETE` `/api/vat-inbound/:id` — Xóa HĐ (policy + trạng thái kho); thường admin. — [`vat-inbound`](api-modules/vat-inbound.md)
199. `GET` `/api/vat-inbound/:id` — Chi tiết một HĐ (metadata + stock lines, không full PDF trong list). — [`vat-inbound`](api-modules/vat-inbound.md)
200. `POST` `/api/vat-inbound/:id/approve-rollback` — Duyệt rollback — trừ lại tồn đã nhập. — [`vat-inbound`](api-modules/vat-inbound.md)
201. `POST` `/api/vat-inbound/:id/approve-undo-dismiss-excluded` — Quản lý duyệt hoàn tác bỏ qua dòng. — [`vat-inbound`](api-modules/vat-inbound.md)
202. `POST` `/api/vat-inbound/:id/archive` — Lưu trữ thủ công (archivedAt). — [`vat-inbound`](api-modules/vat-inbound.md)
203. `GET` `/api/vat-inbound/:id/audit-logs` — Nhật ký thao tác trên HĐ (vat_inbound_audit_logs). — [`vat-inbound`](api-modules/vat-inbound.md)
204. `POST` `/api/vat-inbound/:id/close-short` — Chốt nhập thiếu — đóng phiếu với trạng thái closed_short. — [`vat-inbound`](api-modules/vat-inbound.md)
205. `POST` `/api/vat-inbound/:id/dismiss-excluded-lines` — Bỏ qua dòng không nhập (phí, dịch vụ…) — ghi audit. — [`vat-inbound`](api-modules/vat-inbound.md)
206. `GET` `/api/vat-inbound/:id/pdf` — Tải PDF base64 đã lưu hoặc fetch Viettel nếu thiếu. — [`vat-inbound`](api-modules/vat-inbound.md)
207. `GET` `/api/vat-inbound/:id/purchase-order` — Lấy PO gắn HĐ (nếu có). — [`vat-inbound`](api-modules/vat-inbound.md)
208. `POST` `/api/vat-inbound/:id/receive-stock` — Nhập kho theo dòng đã ghép; cập nhật tồn + giá vốn BQ; đổi stockStatus. — [`vat-inbound`](api-modules/vat-inbound.md)
209. `POST` `/api/vat-inbound/:id/reject-rollback` — Từ chối yêu cầu rollback. — [`vat-inbound`](api-modules/vat-inbound.md)
210. `POST` `/api/vat-inbound/:id/reject-undo-dismiss-excluded` — Từ chối yêu cầu hoàn tác bỏ qua dòng. — [`vat-inbound`](api-modules/vat-inbound.md)
211. `POST` `/api/vat-inbound/:id/request-rollback` — Yêu cầu hoàn tác nhập kho (rollback inventory). — [`vat-inbound`](api-modules/vat-inbound.md)
212. `POST` `/api/vat-inbound/:id/request-undo-dismiss-excluded` — NV gửi yêu cầu hoàn tác bỏ qua dòng. — [`vat-inbound`](api-modules/vat-inbound.md)
213. `POST` `/api/vat-inbound/:id/restore-line` — Khôi phục dòng đã loại trừ khỏi ghép hàng. — [`vat-inbound`](api-modules/vat-inbound.md)
214. `POST` `/api/vat-inbound/:id/stock-receipt` — Ghép dòng HĐ ↔ SP; tạo/cập nhật stockLines; có thể tạo SP/NCC/PO inline. — [`vat-inbound`](api-modules/vat-inbound.md)
215. `POST` `/api/vat-inbound/:id/unarchive` — Bỏ lưu trữ. — [`vat-inbound`](api-modules/vat-inbound.md)
216. `POST` `/api/vat-inbound/:id/undo-dismiss-excluded-lines` — Hoàn tác bỏ qua dòng (nếu policy cho phép). — [`vat-inbound`](api-modules/vat-inbound.md)
217. `POST` `/api/vat-inbound/:id/verify-viettel` — Xác thực HĐ với Viettel SInvoice; cập nhật trạng thái verify. — [`vat-inbound`](api-modules/vat-inbound.md)
218. `POST` `/api/vat-inbound/backfill-marked-mst-archive` — Chạy lại backfill archive theo MST (ops / sau migration). — [`vat-inbound`](api-modules/vat-inbound.md)
219. `POST` `/api/vat-inbound/gdt/captcha` — Lấy captcha CQT cho org gdt_direct — trả session tạm captcha store. — [`vat-inbound`](api-modules/vat-inbound.md)
220. `POST` `/api/vat-inbound/gdt/reconnect` — Đăng nhập lại CQT sau captcha; lưu session org GDT. — [`vat-inbound`](api-modules/vat-inbound.md)
221. `GET` `/api/vat-inbound/marked-mst-archive` — Đọc chuỗi MST lọc từ organizations.vat_inbound_auto_archive_tax_codes. — [`vat-inbound`](api-modules/vat-inbound.md)
222. `PATCH` `/api/vat-inbound/marked-mst-archive` — Lưu MST lọc (admin/manager); normalize input; backfill archive HĐ trùng MST ngay sau lưu. — [`vat-inbound`](api-modules/vat-inbound.md)
223. `POST` `/api/vat-inbound/sync-tax` — Kéo HĐ từ CQT/Viettel theo from/to; map XML → DB; auto archive MST; có thể split khoảng dài. — [`vat-inbound`](api-modules/vat-inbound.md)
224. `GET` `/api/viettel-invoice/settings` — REST `GET` trên module `org-viettel-settings`. — [`org-viettel-settings`](api-modules/org-viettel-settings.md)
225. `PATCH` `/api/viettel-invoice/settings` — REST `PATCH` trên module `org-viettel-settings`. — [`org-viettel-settings`](api-modules/org-viettel-settings.md)
226. `POST` `/api/visitor-counts` — API key cho widget / thiết bị (ESP32 visitor-counts). Frontend: pages/chain-api-keys.tsx (nếu có). — [`shop-api-keys`](api-modules/shop-api-keys.md)
227. `POST` `/api/visitor-counts/status` — API key cho widget / thiết bị (ESP32 visitor-counts). Frontend: pages/chain-api-keys.tsx (nếu có). — [`shop-api-keys`](api-modules/shop-api-keys.md)
228. `GET` `/api/warehouses` — Tổ chức, shop, kho, điều chuyển (transfers). Cấu hình org (Viettel, CQT, feedback URL, agent LLM).… — [`chain`](api-modules/chain.md)
229. `POST` `/api/warehouses` — Tổ chức, shop, kho, điều chuyển (transfers). Cấu hình org (Viettel, CQT, feedback URL, agent LLM).… — [`chain`](api-modules/chain.md)
230. `PATCH` `/api/warehouses/:id` — Tổ chức, shop, kho, điều chuyển (transfers). Cấu hình org (Viettel, CQT, feedback URL, agent LLM).… — [`chain`](api-modules/chain.md)
231. `POST` `/api/warehouses/:id/adjust-stock` — Tổ chức, shop, kho, điều chuyển (transfers). Cấu hình org (Viettel, CQT, feedback URL, agent LLM).… — [`chain`](api-modules/chain.md)
232. `GET` `/api/warehouses/:id/inventory` — Tổ chức, shop, kho, điều chuyển (transfers). Cấu hình org (Viettel, CQT, feedback URL, agent LLM).… — [`chain`](api-modules/chain.md)
233. `GET` `/api/warehouses/:id/movements` — Tổ chức, shop, kho, điều chuyển (transfers). Cấu hình org (Viettel, CQT, feedback URL, agent LLM).… — [`chain`](api-modules/chain.md)
234. `GET` `/api/warehouses/:id/products` — Tổ chức, shop, kho, điều chuyển (transfers). Cấu hình org (Viettel, CQT, feedback URL, agent LLM).… — [`chain`](api-modules/chain.md)
235. `GET` `/api/widget/home` — API phục vụ app Android widget: thống kê quầy (JWT / shop context). Repo: VietPOS-Widget/. — [`widget`](api-modules/widget.md)

---

## Lộ trình đọc gợi ý

1. `he-thong/01-kien-truc-runtime.md` → `he-thong/04-docker-va-cloud-sync.md`
2. `nghiep-vu/01-dang-nhap-va-shop-context.md` → … → `12-widget-va-dem-khach.md`
3. Sửa API: `api-modules/<ten>.md` + `lib-modules/...` nếu logic nằm lib
4. Sửa UI: `frontend-pages/<ten>.md`
5. DB: `schema/<ten>.md` + `reference/database.md`
6. HĐ đầu vào: `nghiep-vu/06`–`08`, `api-modules/vat-inbound.md`, `frontend-pages/vat-inbound.md`

**Tổng số mục file trong mục lục:** 247
**Tổng endpoint REST (trích routes):** 235
