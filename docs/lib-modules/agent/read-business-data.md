# Lib: `agent/read-business-data.ts`

**Mô tả:** Logic backend agent/read-business-data.ts (~1011 dòng) — export: AGENT_READ_DATASETS, readBusinessDataSchema, runReadBusinessData.

**Source Shop:** `artifacts/api-server/src/lib/agent/read-business-data.ts`

**Độ lớn:** ~1011 dòng.

Thư viện backend dùng chung giữa nhiều route handler — đọc file gốc để biết thuật toán đầy đủ.

## Export (3 symbol)

- `AGENT_READ_DATASETS`
- `readBusinessDataSchema`
- `runReadBusinessData`

## Import DB / schema

- `} from "@workspace/db";`

## Xem trước đầu file

```typescript
import { z } from "zod/v4";
import {
  db,
  ordersTable,
  orderItemsTable,
  productsTable,
  inventoryTable,
  usersTable,
  suppliersTable,
  stockRequestsTable,
  customerFeedbackTable,
  purchaseOrdersTable,
  productCategoriesTable,
  shopsTable,
  shopDailyVisitorCountsTable,
} from "@workspace/db";
import {
  and,
  desc,
  eq,
  gte,
  ilike,
  inArray,
  isNull,
  lt,
  or,
  sql,
  type SQL,
} from "drizzle-orm";
import { formatOrderInvoiceCode, unpadOrderInvoiceCode } from "../order-invoice-code";
import type { AuthPayload } from "../../middlewares/auth";
import {
  isMasterAdmin,
  resolveOrganizationId,
  userCanSeeDashboardSalesProfit,
```
