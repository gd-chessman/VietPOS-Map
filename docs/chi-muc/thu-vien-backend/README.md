# Chỉ mục thư viện backend

**Mô tả:** Danh sách 98 file lib — nhóm theo thư mục, không đọc tuần tự hết.

← [Bản đồ chính](../../README.md) · [Hướng dẫn đọc](../../huong-dan-doc/)

---

### `agent-chat-persist/`

- [agent-chat-persist](../../thu-vien/agent-chat-persist/) — [Trợ lý AI] agent-chat-persist.ts — AGENT_CHAT_CONTEXT_LIMIT, getOrCreateAgentChatThread, appendAge…

### `allowed-device-names/`

- [allowed-device-names](../../thu-vien/allowed-device-names/) — [Kiến trúc / dùng chung] allowed-device-names.ts — lookupDeviceNamesByDeviceIds.

### `api-access-observations/`

- [api-access-observations](../../thu-vien/api-access-observations/) — [An ninh] api-access-observations.ts — recordApiAccessObservation, summarizeAccessObservationsToday…

### `chain-shop-scope/`

- [chain-shop-scope](../../thu-vien/chain-shop-scope/) — [Chuỗi cửa hàng] chain-shop-scope.ts — parseOptionalShopId, resolveChainShopScope, resolveStatistic…

### `change-log/`

- [change-log](../../thu-vien/change-log/) — [Kiến trúc / dùng chung] change-log.ts — recordProductChange, recordInventoryChange.

### `cong-cqt/`

- [captcha-store](../../thu-vien/cong-cqt/captcha-store/) — [Hóa đơn đầu vào] gdt-portal/captcha-store.ts — getOrCreateCaptchaClient, dropCaptchaClient.
- [client](../../thu-vien/cong-cqt/client/) — [Hóa đơn đầu vào] gdt-portal/client.ts — captchaDataUrl.
- [connect-with-captcha](../../thu-vien/cong-cqt/connect-with-captcha/) — [Hóa đơn đầu vào] gdt-portal/connect-with-captcha.ts — gdtPortalConnectWithCaptcha, gdtPortalFetchC…
- [export-xml](../../thu-vien/cong-cqt/export-xml/) — [Hóa đơn đầu vào] gdt-portal/export-xml.ts — extractFirstXmlFromExportPayload, lineItemsFromExportX…
- [fetch-inbound](../../thu-vien/cong-cqt/fetch-inbound/) — [Hóa đơn đầu vào] gdt-portal/fetch-inbound.ts — fetchGdtInboundInvoices.
- [http-session](../../thu-vien/cong-cqt/http-session/) — [Hóa đơn đầu vào] gdt-portal/http-session.ts — (không export tên rõ).
- [map-inbound](../../thu-vien/cong-cqt/map-inbound/) — [Hóa đơn đầu vào] gdt-portal/map-inbound.ts — formatGdtVatRateLabel, mapGdtPurchaseRow, applyGdtDet…
- [org-session](../../thu-vien/cong-cqt/org-session/) — [Hóa đơn đầu vào] gdt-portal/org-session.ts — normalizeVatInboundProvider, getGdtSessionPublic, sav…
- [xml-lines](../../thu-vien/cong-cqt/xml-lines/) — [Hóa đơn đầu vào] gdt-portal/xml-lines.ts — parseLineItemsFromCqtXml.

### `cors-config/`

- [cors-config](../../thu-vien/cors-config/) — [Kiến trúc / dùng chung] cors-config.ts — parseFrontendUrls, getCorsOptions.

### `customer-public-urls/`

- [customer-public-urls](../../thu-vien/customer-public-urls/) — [Kiến trúc / dùng chung] customer-public-urls.ts — normalizePublicBaseUrl, buildPublicPageUrl, publ…

### `dashboard-period/`

- [dashboard-period](../../thu-vien/dashboard-period/) — [Chuỗi cửa hàng] dashboard-period.ts — resolveDashboardPeriodRange, parseDashboardChartGranularity,…

### `dashboard-visitor-stats/`

- [dashboard-visitor-stats](../../thu-vien/dashboard-visitor-stats/) — [Chuỗi cửa hàng] dashboard-visitor-stats.ts — visitDateString, visitorsPerBuyer, sumVisitorsForShop…

### `device-denylist/`

- [device-denylist](../../thu-vien/device-denylist/) — [An ninh] device-denylist.ts — blockedDeviceCount, normalizeDeviceId, deviceIdFromRequest, isValidB…

### `entity-status/`

- [entity-status](../../thu-vien/entity-status/) — [Kiến trúc / dùng chung] entity-status.ts — getOperationalContext, getShopOperationalBlock, isShopA…

### `hoa-don-viettel/`

- [build-payload](../../thu-vien/hoa-don-viettel/build-payload/) — [Hóa đơn bán ra] viettel-sinvoice/build-payload.ts — mergeOrderLinesByProductForEinvoice, assertEin…
- [client](../../thu-vien/hoa-don-viettel/client/) — [Hóa đơn bán ra] viettel-sinvoice/client.ts — isTransientViettelPdfError, createViettelInvoice, sea…
- [config](../../thu-vien/hoa-don-viettel/config/) — [Hóa đơn bán ra] viettel-sinvoice/config.ts — toGdtPortalTaxCode, loadOrgViettelRow, resolveOrganiz…
- [download-pdf](../../thu-vien/hoa-don-viettel/download-pdf/) — [Hóa đơn bán ra] viettel-sinvoice/download-pdf.ts — fetchViettelInvoicePdf, fetchViettelInvoicePdfF…
- [inbound-pdf](../../thu-vien/hoa-don-viettel/inbound-pdf/) — [Hóa đơn bán ra] viettel-sinvoice/inbound-pdf.ts — toViettelPortalIssueDate, fetchViettelInboundInv…
- [issue](../../thu-vien/hoa-don-viettel/issue/) — [Hóa đơn bán ra] viettel-sinvoice/issue.ts — issueViettelInvoiceForOrder.
- [search-inbound](../../thu-vien/hoa-don-viettel/search-inbound/) — [Hóa đơn bán ra] viettel-sinvoice/search-inbound.ts — mapViettelInboundInvoice, splitInboundDateRan…

### `inbound-stock-receive/`

- [inbound-stock-receive](../../thu-vien/inbound-stock-receive/) — [Hóa đơn đầu vào] inbound-stock-receive.ts — applyInvoiceInventoryReceive, reverseInvoiceInventoryR…

### `inventory-variant/`

- [inventory-variant](../../thu-vien/inventory-variant/) — [Sản phẩm & kho] inventory-variant.ts — upsertShopStockByProduct, upsertShopExtraVariantStock, upse…

### `ip-denylist/`

- [ip-denylist](../../thu-vien/ip-denylist/) — [An ninh] ip-denylist.ts — normalizeClientIp, blockedIpCount, clientIpFromRequest, describeSeenClie…

### `logger/`

- [logger](../../thu-vien/logger/) — [Kiến trúc / dùng chung] logger.ts — logger.

### `order-audit/`

- [order-audit](../../thu-vien/order-audit/) — [POS & đơn hàng] order-audit.ts — mapAuditLogRow, insertOrderAuditLog, listOrderAuditLogs.

### `order-direct-cancel/`

- [order-direct-cancel](../../thu-vien/order-direct-cancel/) — [POS & đơn hàng] order-direct-cancel.ts — directCancelWithoutRequestSql, sumDirectCancelledInPeriod…

### `order-discount/`

- [order-discount](../../thu-vien/order-discount/) — [POS & đơn hàng] order-discount.ts — computeOrderDiscountAmount, fetchDashboardChartOrders, sumComp…

### `order-fraud/`

- [order-fraud](../../thu-vien/order-fraud/) — [POS & đơn hàng] order-fraud.ts — isOrderSyncSuspicious.

### `order-invoice-code/`

- [order-invoice-code](../../thu-vien/order-invoice-code/) — [POS & đơn hàng] order-invoice-code.ts — normalizeShopCode, formatOrderInvoiceCode, unpadOrderInvoi…

### `order-invoice-list-filters/`

- [order-invoice-list-filters](../../thu-vien/order-invoice-list-filters/) — [POS & đơn hàng] order-invoice-list-filters.ts — invoiceListFilters.

### `order-list-period-summary/`

- [order-list-period-summary](../../thu-vien/order-list-period-summary/) — [POS & đơn hàng] order-list-period-summary.ts — appendOrderListDateFilters, fetchOrderListPeriodSum…

### `order-preprint/`

- [order-preprint](../../thu-vien/order-preprint/) — [POS & đơn hàng] order-preprint.ts — newInvoicePublicToken, upsertOrderPreprintReservation, loadPre…

### `order-shop-sequence/`

- [order-shop-sequence](../../thu-vien/order-shop-sequence/) — [POS & đơn hàng] order-shop-sequence.ts — allocateShopOrderSequence, resolveShopOrderSequence, quer…

### `orders-scope/`

- [orders-scope](../../thu-vien/orders-scope/) — [POS & đơn hàng] orders-scope.ts — parseOptionalShopId, resolveOrderListScope, orderShopFilter, can…

### `org-agent-llm-settings/`

- [org-agent-llm-settings](../../thu-vien/org-agent-llm-settings/) — [Kiến trúc / dùng chung] org-agent-llm-settings.ts — maskAgentApiKeyForDisplay, stripOrgAgentLlmSec…

### `org-gdt-settings/`

- [org-gdt-settings](../../thu-vien/org-gdt-settings/) — [Kiến trúc / dùng chung] org-gdt-settings.ts — stripOrgGdtPassword, applyGdtSettingsFromBody, gdtCr…

### `org-smtp-settings/`

- [org-smtp-settings](../../thu-vien/org-smtp-settings/) — [Kiến trúc / dùng chung] org-smtp-settings.ts — stripOrgSmtpPassword, smtpConfigFromOrgRow, loadOrg…

### `org-viettel-settings/`

- [org-viettel-settings](../../thu-vien/org-viettel-settings/) — [Hóa đơn bán ra] org-viettel-settings.ts — viettelConfigReadiness, stripOrgViettelPassword, toPubli…

### `payment-revenue/`

- [payment-revenue](../../thu-vien/payment-revenue/) — [POS & đơn hàng] payment-revenue.ts — emptyPaymentRevenue, addOrderPaymentRevenue, sumOrdersPayment…

### `pin-challenge/`

- [pin-challenge](../../thu-vien/pin-challenge/) — [Đăng nhập & phiên] pin-challenge.ts — PIN_CHALLENGE_PURPOSE, signPinChallengeToken, verifyPinChall…

### `pin-reset-requests/`

- [pin-reset-requests](../../thu-vien/pin-reset-requests/) — [Đăng nhập & phiên] pin-reset-requests.ts — upsertPendingPinResetRequest, canSetPinWithoutPasswordA…

### `platform-notification-settings/`

- [platform-notification-settings](../../thu-vien/platform-notification-settings/) — [Kiến trúc / dùng chung] platform-notification-settings.ts — RECIPIENT_ROLE_OPTIONS, invalidateNoti…

### `product-audit/`

- [product-audit](../../thu-vien/product-audit/) — [Sản phẩm & kho] product-audit.ts — recordProductAudit, buildProductFieldChanges.

### `product-category/`

- [product-category](../../thu-vien/product-category/) — [Sản phẩm & kho] product-category.ts — findCategoryByName, resolveProductCategory, syncProductCateg…

### `product-supplier/`

- [product-supplier](../../thu-vien/product-supplier/) — [Sản phẩm & kho] product-supplier.ts — parseSupplierImportStatus, findSupplierByName, resolveProduc…

### `product-variants/`

- [product-variants](../../thu-vien/product-variants/) — [Sản phẩm & kho] product-variants.ts — suggestVariantCode, getVariant0, ensureVariantColumns, ensur…

### `product-vat/`

- [product-vat](../../thu-vien/product-vat/) — [Sản phẩm & kho] product-vat.ts — DEFAULT_UNIT, DEFAULT_VAT_RATE, DEFAULT_TNCN_RATE, ALLOWED_VAT_RA…

### `product-vat-name/`

- [product-vat-name](../../thu-vien/product-vat-name/) — [Sản phẩm & kho] product-vat-name.ts — normalizeVatNameKey, findSupplierVatNameConflict, assertUniq…

### `rate-limit/`

- [rate-limit](../../thu-vien/rate-limit/) — [Kiến trúc / dùng chung] rate-limit.ts — isRateLimitEnabled, isTrustProxyEnabled, configureTrustPro…

### `record-device-login/`

- [record-device-login](../../thu-vien/record-device-login/) — [Kiến trúc / dùng chung] record-device-login.ts — recordDeviceLoginEvent.

### `report-pos-staff/`

- [report-pos-staff](../../thu-vien/report-pos-staff/) — [Kiến trúc / dùng chung] report-pos-staff.ts — buildPosStaffReport.

### `report-sales-staff-performance/`

- [report-sales-staff-performance](../../thu-vien/report-sales-staff-performance/) — [Kiến trúc / dùng chung] report-sales-staff-performance.ts — buildSalesStaffPerformanceReport.

### `secret-box/`

- [secret-box](../../thu-vien/secret-box/) — [Kiến trúc / dùng chung] secret-box.ts — encryptSecret, decryptSecret.

### `session-cookie/`

- [session-cookie](../../thu-vien/session-cookie/) — [Đăng nhập & phiên] session-cookie.ts — SESSION_COOKIE_NAME, setSessionCookie, clearSessionCookie.

### `shift-sessions/`

- [shift-sessions](../../thu-vien/shift-sessions/) — [POS & đơn hàng] shift-sessions.ts — getActiveShiftSession, isShiftSessionRestrictedRole, assertSta…

### `shop-display-order/`

- [shop-display-order](../../thu-vien/shop-display-order/) — [POS & đơn hàng] shop-display-order.ts — shopsOrderByDisplay, compareShopsByDisplay, sortShopsByDis…

### `shop-operational-events/`

- [shop-operational-events](../../thu-vien/shop-operational-events/) — [Kiến trúc / dùng chung] shop-operational-events.ts — syncShopOperationalState, runShopPresenceSwee…

### `shop-presence/`

- [shop-presence](../../thu-vien/shop-presence/) — [Chuỗi cửa hàng] shop-presence.ts — SHOP_PRESENCE_TIMEOUT_MS, isShopOnline, CLOCK_DRIFT_WARNING_MS,…

### `shop-presence-sweep/`

- [shop-presence-sweep](../../thu-vien/shop-presence-sweep/) — [Chuỗi cửa hàng] shop-presence-sweep.ts — startShopPresenceSweepScheduler.

### `shop-vat-settings/`

- [shop-vat-settings](../../thu-vien/shop-vat-settings/) — [Kiến trúc / dùng chung] shop-vat-settings.ts — isVatInvoicePublicEnabledForShop.

### `staff-role-rank/`

- [staff-role-rank](../../thu-vien/staff-role-rank/) — [Kiến trúc / dùng chung] staff-role-rank.ts — roleRank, callerCanManageTargetRole.

### `system-error-capture/`

- [system-error-capture](../../thu-vien/system-error-capture/) — [Kiến trúc / dùng chung] system-error-capture.ts — markSystemEventLogged, captureUnhandledProcessEr…

### `system-event-log/`

- [system-event-log](../../thu-vien/system-event-log/) — [Kiến trúc / dùng chung] system-event-log.ts — recordSystemEvent, recordEmailSystemFailure, recordE…

### `system-event-query/`

- [system-event-query](../../thu-vien/system-event-query/) — [Kiến trúc / dùng chung] system-event-query.ts — vnTodayYmd, querySystemEventLogs.

### `time-drift/`

- [time-drift](../../thu-vien/time-drift/) — [Kiến trúc / dùng chung] time-drift.ts — getTimeDriftWarningThresholdMs.

### `tro-ly-ai-lib/`

- [agent-tool-dates](../../thu-vien/tro-ly-ai-lib/agent-tool-dates/) — [Trợ lý AI] agent/agent-tool-dates.ts — formatAgentToolPayloadForLlm.
- [chat](../../thu-vien/tro-ly-ai-lib/chat/) — [Trợ lý AI] agent/chat.ts — resolveAgentLlmForAuth, isAgentLlmConfiguredForAuth, runAgentChat.
- [read-business-data](../../thu-vien/tro-ly-ai-lib/read-business-data/) — [Trợ lý AI] agent/read-business-data.ts — AGENT_READ_DATASETS, readBusinessDataSchema, runReadBusin…
- [read-deep-handlers](../../thu-vien/tro-ly-ai-lib/read-deep-handlers/) — [Trợ lý AI] agent/read-deep-handlers.ts — readRevenueChartDaily, readVatQueueCounts, readVatInbound…
- [system-info](../../thu-vien/tro-ly-ai-lib/system-info/) — [Trợ lý AI] agent/system-info.ts — buildAgentSystemInfo.
- [tools](../../thu-vien/tro-ly-ai-lib/tools/) — [Trợ lý AI] agent/tools.ts — agentToolDefinitionsForAuth, invokeAgentTool.

### `user-email/`

- [user-email](../../thu-vien/user-email/) — [Đăng nhập & phiên] user-email.ts — normalizeEmail, EMAIL_ALREADY_USED_MSG, ORG_EMAIL_TAKEN_MSG, fi…

### `user-notifications/`

- [user-notifications](../../thu-vien/user-notifications/) — [Đăng nhập & phiên] user-notifications.ts — formatVatInboundInvoiceCode, clearVatInboundReceiptActi…

### `user-pin/`

- [user-pin](../../thu-vien/user-pin/) — [Đăng nhập & phiên] user-pin.ts — PIN_LENGTH, roleRequiresPin, normalizePin, validatePinFormat, has…

### `vat-inbound-audit/`

- [vat-inbound-audit](../../thu-vien/vat-inbound-audit/) — [Hóa đơn đầu vào] vat-inbound-audit.ts — insertVatInboundAuditLog, listVatInboundAuditLogs.

### `vat-inbound-auto-archive-mst/`

- [vat-inbound-auto-archive-mst](../../thu-vien/vat-inbound-auto-archive-mst/) — [Hóa đơn đầu vào] vat-inbound-auto-archive-mst.ts — taxDigitsOnly, parseVatInboundAutoArchiveTaxCod…

### `vat-inbound-auto-process/`

- [vat-inbound-auto-process](../../thu-vien/vat-inbound-auto-process/) — [Hóa đơn đầu vào] vat-inbound-auto-process.ts — invoiceEligibleForAutoMap, processVatInboundAutoFor…

### `vat-inbound-auto-sync/`

- [vat-inbound-auto-sync](../../thu-vien/vat-inbound-auto-sync/) — [Hóa đơn đầu vào] vat-inbound-auto-sync.ts — isVatInboundAutoSyncWindow, vatInboundAutoSyncSlotKey,…

### `vat-inbound-excluded/`

- [vat-inbound-excluded](../../thu-vien/vat-inbound-excluded/) — [Hóa đơn đầu vào] vat-inbound-excluded.ts — listExcludedLineIndexes.

### `vat-inbound-mapped-products/`

- [vat-inbound-mapped-products](../../thu-vien/vat-inbound-mapped-products/) — [Hóa đơn đầu vào] vat-inbound-mapped-products.ts — isVatInvoiceInboundMappedOnlyForShop, INBOUND_MA…

### `vat-inbound-marked-mst-backfill/`

- [vat-inbound-marked-mst-backfill](../../thu-vien/vat-inbound-marked-mst-backfill/) — [Hóa đơn đầu vào] vat-inbound-marked-mst-backfill.ts — backfillVatInboundArchiveByMarkedMst.

### `vat-inbound-product-code/`

- [vat-inbound-product-code](../../thu-vien/vat-inbound-product-code/) — [Hóa đơn đầu vào] vat-inbound-product-code.ts — initialsFromVatName, vatLinePriceThousands, buildAu…

### `vat-inbound-tax-sync/`

- [vat-inbound-tax-sync](../../thu-vien/vat-inbound-tax-sync/) — [Hóa đơn đầu vào] vat-inbound-tax-sync.ts — syncVatInboundInvoicesFromTax.

### `vat-invoice/`

- [vat-invoice](../../thu-vien/vat-invoice/) — [Hóa đơn bán ra] vat-invoice.ts — normalizeTaxCode, isValidTaxCode, isNumericTaxCode, isValidEmail,…

### `vat-invoice-auto-issue/`

- [vat-invoice-auto-issue](../../thu-vien/vat-invoice-auto-issue/) — [Hóa đơn bán ra] vat-invoice-auto-issue.ts — AUTO_ISSUE_BATCH_MINUTE_OF_DAY_VN, minutesOfDayVN, ord…

### `vat-invoice-buyer-email/`

- [vat-invoice-buyer-email](../../thu-vien/vat-invoice-buyer-email/) — [Hóa đơn bán ra] vat-invoice-buyer-email.ts — deliverVatInvoiceEmailToBuyer.

### `vat-invoice-public-window/`

- [vat-invoice-public-window](../../thu-vien/vat-invoice-public-window/) — [Hóa đơn bán ra] vat-invoice-public-window.ts — VAT_INVOICE_PUBLIC_EDIT_WINDOW_MS, orderPurchaseAt,…

### `vietnam-calendar/`

- [vietnam-calendar](../../thu-vien/vietnam-calendar/) — [Kiến trúc / dùng chung] vietnam-calendar.ts — VN_TZ, formatVnDateTime, vnCalendarDay, vnAddCalenda…

### `vn-order-period/`

- [vn-order-period](../../thu-vien/vn-order-period/) — [POS & đơn hàng] vn-order-period.ts — VN_YMD_RE, vnYmdStartInstant, vnYmdEndInclusiveInstant, resol…

### `weighted-average-cost/`

- [weighted-average-cost](../../thu-vien/weighted-average-cost/) — [Sản phẩm & kho] weighted-average-cost.ts — roundMoney2, weightedAverageCost, reverseWeightedAverag…

### `widget-home/`

- [widget-home](../../thu-vien/widget-home/) — [Kiến trúc / dùng chung] widget-home.ts — computeDayBlockForShops, computeInbound, computeActions,…

