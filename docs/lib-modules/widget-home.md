# Lib: `widget-home.ts`

**Mô tả:** Logic backend widget-home.ts (~525 dòng) — export: computeDayBlockForShops, computeInbound, computeActions, WIDGET_SUPER_ADMIN_ONLY_MESSAGE, assertWidgetSuperAdmin, ….

**Source Shop:** `artifacts/api-server/src/lib/widget-home.ts`

**Độ lớn:** ~525 dòng.

Thư viện backend dùng chung giữa nhiều route handler — đọc file gốc để biết thuật toán đầy đủ.

## Export (6 symbol)

- `computeDayBlockForShops`
- `computeInbound`
- `computeActions`
- `WIDGET_SUPER_ADMIN_ONLY_MESSAGE`
- `assertWidgetSuperAdmin`
- `buildWidgetHomePayload`

## Import DB / schema

- `} from "@workspace/db";`

## Xem trước đầu file

```typescript
import {
  db,
  ordersTable,
  shopsTable,
  organizationsTable,
  purchaseOrdersTable,
  stockRequestsTable,
  userNotificationsTable,
  vatInboundInvoicesTable,
  inventoryTable,
  resolveOrderPayments,
} from "@workspace/db";
import { and, asc, eq, gte, inArray, isNull, lt, sql, desc } from "drizzle-orm";
import { shopsOrderByDisplay } from "./shop-display-order";
import type { AuthPayload } from "../middlewares/auth";
import { userCanViewChainDashboard, resolveOrganizationId } from "../middlewares/auth";
import { resolveChainShopScope, type ChainShopScope } from "./chain-shop-scope";
import { sumOrdersPaymentRevenue } from "./payment-revenue";
import { sumVisitorsForShopOnDate, sumVisitorsForChainScopeOnDate } from "./dashboard-visitor-stats";
import { vnCalendarDay, vnDayBoundsExclusive } from "./vietnam-calendar";
import { resolveInvoiceStatus } from "./vat-invoice";

export type WidgetPaymentBreakdown = {
  cash: number;
  card: number;
  transfer: number;
};

export type WidgetAlertCounts = {
  pendingCancelOrders: number;
  pendingCancelRevenue: number;
  cancelledOrders: number;
  cancelledRevenue: number;
  vatPendingOrders: number;
  vatPendingRevenue: number;
```
