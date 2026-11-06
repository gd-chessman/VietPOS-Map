# Lib: `agent/read-deep-handlers.ts`

**Mô tả:** Logic backend agent/read-deep-handlers.ts (~603 dòng) — export: readRevenueChartDaily, readVatQueueCounts, readVatInboundList, readReprintsList, readShiftSessionsRecent, ….

**Source Shop:** `artifacts/api-server/src/lib/agent/read-deep-handlers.ts`

**Độ lớn:** ~603 dòng.

Thư viện backend dùng chung giữa nhiều route handler — đọc file gốc để biết thuật toán đầy đủ.

## Export (15 symbol)

- `readRevenueChartDaily`
- `readVatQueueCounts`
- `readVatInboundList`
- `readReprintsList`
- `readShiftSessionsRecent`
- `readStockRequestDetail`
- `readPurchaseOrderDetail`
- `readProductsList`
- `readProductsWithVariants`
- `readOrderAuditTrail`
- `readInvoiceChangeLogs`
- `readShopsOperational`
- `readStockRequestCounts`
- `readNotificationsRecent`
- `readTopProductsExtended`

## Import DB / schema

- `} from "@workspace/db";`

## Xem trước đầu file

```typescript
import {
  db,
  ordersTable,
  orderItemsTable,
  productsTable,
  productVariantsTable,
  stockRequestsTable,
  stockRequestItemsTable,
  purchaseOrdersTable,
  purchaseOrderItemsTable,
  suppliersTable,
  vatInboundInvoicesTable,
  shiftSessionsTable,
  reprintLogsTable,
  usersTable,
  shopsTable,
  userNotificationsTable,
  invoiceChangeLogsTable,
} from "@workspace/db";
import { and, desc, eq, gte, ilike, inArray, lt, lte, or, sql, type SQL } from "drizzle-orm";
import type { AuthPayload } from "../../middlewares/auth";
import {
  userCanAccessVatInvoices,
  userIsAtHubShop,
} from "../../middlewares/auth";
import { resolveStatisticsShopScope, shopIdFilter } from "../chain-shop-scope";
import { canAccessOrder, orderShopFilter, resolveOrderListScope } from "../orders-scope";
import { invoiceListFilters } from "../order-invoice-list-filters";
import { listOrderAuditLogs } from "../order-audit";
import { isShopOnline, hasClockDrift } from "../shop-presence";
import { resolveChartAlignedOrderPeriodBounds } from "../vn-order-period";
import { canViewPosAuditReports } from "../../middlewares/auth";
import { resolveReportShopScope, shopIdFilter as reportShopFilter } from "../chain-shop-scope";
import type { ReadBusinessDataInput } from "./read-business-data";

```
