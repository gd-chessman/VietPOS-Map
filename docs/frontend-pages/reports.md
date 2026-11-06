# Frontend: `reports.tsx`

**Mô tả:** Báo cáo nhân viên, in lại bill, doanh số. (URL /reports, Reports, ~2178 dòng).

**Source Shop:** `artifacts/pos-app/src/pages/reports.tsx`

**URL (wouter):** `/reports`
**Component:** `Reports`
**Độ lớn:** ~2178 dòng.

**Route:** `/reports`

Báo cáo nhân viên, in lại bill, doanh số.

## Menu sidebar

- **Nhãn:** Báo cáo nhân viên
- **Điều kiện hiện menu (`show`):** `isAdminOrManager`

## Component con (logic UI chính)

- `@/components/ui/card` → `artifacts/pos-app/src/components/ui/card.tsx`
- `@/components/ui/table` → `artifacts/pos-app/src/components/ui/table.tsx`
- `@/components/ui/badge` → `artifacts/pos-app/src/components/ui/badge.tsx`
- `@/components/ui/button` → `artifacts/pos-app/src/components/ui/button.tsx`
- `@/components/ui/input` → `artifacts/pos-app/src/components/ui/input.tsx`
- `@/components/date-range-filter` → `artifacts/pos-app/src/components/date-range-filter.tsx`
- `@/components/OrderAuditSensitivityBadge` → `artifacts/pos-app/src/components/OrderAuditSensitivityBadge.tsx`
- `@/components/pagination-bar` → `artifacts/pos-app/src/components/pagination-bar.tsx`

## Cách đọc code

- API: tìm `useQuery`, `useMutation`, `apiFetch`, hoặc mục **Chuỗi `/api/...`** bên dưới.
- Quyền: `lib/session-permissions.ts`, biểu thức trong `app-layout.tsx` và file page.
- Offline: các trang POS có thể gọi Dexie qua `@/lib/offline/...`.

## API modules (map sang docs)

- [`api-modules/reports.md`](../api-modules/reports.md) — prefix `/api/reports`
- [`api-modules/shops.md`](../api-modules/shops.md) — prefix `/api/shops`

## Quyền (phát hiện trong source)

- Có kiểm tra role **`super_admin`** (hoặc redirect dashboard).

## Query string URL (đọc trong code)

- `shopId`

## JSX component dùng trong file (PascalCase)

- `<AlertTriangle />`
- `<ArrowRightLeft />`
- `<Badge />`
- `<Button />`
- `<CalendarDays />`
- `<Card />`
- `<CardContent />`
- `<CardHeader />`
- `<CardTitle />`
- `<ChevronDown />`
- `<ChevronUp />`
- `<ClipboardList />`
- `<DateFilter />`
- `<DateRangeFilter />`
- `<DetailTab />`
- `<Download />`
- `<HTMLDivElement />`
- `<OrderAuditAction />`
- `<OrderAuditRow />`
- `<OrderAuditSensitivityBadge />`
- `<OrderAuditSensitivityLevel />`
- `<OrderAuditSummary />`
- `<Package />`
- `<PaginationBar />`
- `<PosAuditRow />`
- … 37 component khác

## Import chính (đầu file)

- `import { useState, useEffect, useRef, Fragment } from "react";`
- `import { useQuery } from "@tanstack/react-query";`
- `import { useGetMe, getGetMeQueryKey } from "@workspace/api-client-react";`
- `import { formatVND } from "@/lib/utils";`
- `import { displayOrderInvoiceCode } from "@/lib/order-invoice-code";`
- `import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";`
- `import { Table, TableBody, TableCell, TableHead, TableHeader, TableRow } from "@/components/ui/table";`
- `import { Badge } from "@/components/ui/badge";`
- `import { Button } from "@/components/ui/button";`
- `import { Input } from "@/components/ui/input";`
- `import {`
- `import { format } from "date-fns";`
- `import { vi } from "date-fns/locale";`
- `import {`
- `import { apiGet, type SalesStaffReport } from "@/lib/sales-api";`
- `import { useToast } from "@/hooks/use-toast";`
- `import {`
- `import {`
- … 1 import khác

## Module `@/lib/...` được import

- `@/lib/offline`
- `@/lib/order-audit`
- `@/lib/order-invoice-code`
- `@/lib/pos-cart-audit`
- `@/lib/product-audit`
- `@/lib/purchase-order-audit`
- `@/lib/report-export`
- `@/lib/sales-api`
- `@/lib/stock-request-audit`
- `@/lib/utils`

## Component `@/components/...` (đã quét API lớp 1)

- `ui/card` → `artifacts/pos-app/src/components/ui/card.tsx`
- `ui/table` → `artifacts/pos-app/src/components/ui/table.tsx`
- `ui/badge` → `artifacts/pos-app/src/components/ui/badge.tsx`
- `ui/button` → `artifacts/pos-app/src/components/ui/button.tsx`
- `ui/input` → `artifacts/pos-app/src/components/ui/input.tsx`
- `date-range-filter` → `artifacts/pos-app/src/components/date-range-filter.tsx`
- `OrderAuditSensitivityBadge` → `artifacts/pos-app/src/components/OrderAuditSensitivityBadge.tsx`
- `pagination-bar` → `artifacts/pos-app/src/components/pagination-bar.tsx`

## Chuỗi `/api/...` (page + component con, 21 mục)

- `/api/reports/order-audit/summary?${dateParams}` → [`api-modules/reports.md`](../api-modules/reports.md)
- `/api/reports/order-audit?${exportOrderAuditParams}` → [`api-modules/reports.md`](../api-modules/reports.md)
- `/api/reports/order-audit?${orderAuditFilterParams}` → [`api-modules/reports.md`](../api-modules/reports.md)
- `/api/reports/pos-cart-audit/summary?${dateParams}` → [`api-modules/reports.md`](../api-modules/reports.md)
- `/api/reports/pos-cart-audit?${auditFilterParams}` → [`api-modules/reports.md`](../api-modules/reports.md)
- `/api/reports/pos-cart-audit?${exportAuditParams}` → [`api-modules/reports.md`](../api-modules/reports.md)
- `/api/reports/product-audit/summary?${dateParams}` → [`api-modules/reports.md`](../api-modules/reports.md)
- `/api/reports/product-audit?${exportProductAuditParams}` → [`api-modules/reports.md`](../api-modules/reports.md)
- `/api/reports/product-audit?${productAuditFilterParams}` → [`api-modules/reports.md`](../api-modules/reports.md)
- `/api/reports/purchase-order-audit/summary?${dateParams}` → [`api-modules/reports.md`](../api-modules/reports.md)
- `/api/reports/purchase-order-audit?${exportPoAuditParams}` → [`api-modules/reports.md`](../api-modules/reports.md)
- `/api/reports/purchase-order-audit?${poAuditFilterParams}` → [`api-modules/reports.md`](../api-modules/reports.md)
- `/api/reports/reprints?${dateParams}` → [`api-modules/reports.md`](../api-modules/reports.md)
- `/api/reports/reprints?${dateParams}&limit=${EXPORT_ROW_LIMIT}` → [`api-modules/reports.md`](../api-modules/reports.md)
- `/api/reports/sales-staff?${dateParams}` → [`api-modules/reports.md`](../api-modules/reports.md)
- `/api/reports/staff/${userId}/detail?${detailParams}` → [`api-modules/reports.md`](../api-modules/reports.md)
- `/api/reports/staff?${dateParams}` → [`api-modules/reports.md`](../api-modules/reports.md)
- `/api/reports/stock-request-audit/summary?${dateParams}` → [`api-modules/reports.md`](../api-modules/reports.md)
- `/api/reports/stock-request-audit?${exportStockAuditParams}` → [`api-modules/reports.md`](../api-modules/reports.md)
- `/api/reports/stock-request-audit?${stockAuditFilterParams}` → [`api-modules/reports.md`](../api-modules/reports.md)
- `/api/shops` → [`api-modules/shops.md`](../api-modules/shops.md)

## File liên quan

- Route khai báo: `artifacts/pos-app/src/App.tsx`
- Layout/menu: `components/layout/app-layout.tsx`
- Session: `lib/session-cache.ts`, `lib/use-session-user.ts`
