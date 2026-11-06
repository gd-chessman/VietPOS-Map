# Frontend: `statistics.tsx`

**Mô tả:** Thống kê bán theo sản phẩm/kỳ. (URL /statistics, Statistics, ~1208 dòng).

**Source Shop:** `artifacts/pos-app/src/pages/statistics.tsx`

**URL (wouter):** `/statistics`
**Component:** `Statistics`
**Độ lớn:** ~1208 dòng.

**Route:** `/statistics`

Thống kê bán theo sản phẩm/kỳ.

## Menu sidebar

- **Nhãn:** Thống kê
- **Điều kiện hiện menu (`show`):** `canViewChainStatistics`

## Component con (logic UI chính)

- `@/components/PaymentBreakdown` → `artifacts/pos-app/src/components/PaymentBreakdown.tsx`
- `@/components/ui/card` → `artifacts/pos-app/src/components/ui/card.tsx`
- `@/components/ui/table` → `artifacts/pos-app/src/components/ui/table.tsx`
- `@/components/ui/button` → `artifacts/pos-app/src/components/ui/button.tsx`
- `@/components/ui/dialog` → `artifacts/pos-app/src/components/ui/dialog.tsx`
- `@/components/ui/calendar` → `artifacts/pos-app/src/components/ui/calendar.tsx`
- `@/components/DashboardPeriodSelector` → `artifacts/pos-app/src/components/DashboardPeriodSelector.tsx`
- `@/components/CatalogStatisticsPanel` → `artifacts/pos-app/src/components/CatalogStatisticsPanel.tsx`
- `@/components/DashboardMonthlyBreakdownCards` → `artifacts/pos-app/src/components/DashboardMonthlyBreakdownCards.tsx`
- `@/components/DashboardChartTooltip` → `artifacts/pos-app/src/components/DashboardChartTooltip.tsx`
- `@/components/QuarterChartGranularityToggle` → `artifacts/pos-app/src/components/QuarterChartGranularityToggle.tsx`

## Cách đọc code

- API: tìm `useQuery`, `useMutation`, `apiFetch`, hoặc mục **Chuỗi `/api/...`** bên dưới.
- Quyền: `lib/session-permissions.ts`, biểu thức trong `app-layout.tsx` và file page.
- Offline: các trang POS có thể gọi Dexie qua `@/lib/offline/...`.

## API modules (map sang docs)

- [`api-modules/chain-dashboard.md`](../api-modules/chain-dashboard.md) — prefix `/api/chain-dashboard`
- [`api-modules/shops.md`](../api-modules/shops.md) — prefix `/api/shops`
- [`api-modules/statistics.md`](../api-modules/statistics.md) — prefix `/api/statistics`

## JSX component dùng trong file (PascalCase)

- `<Area />`
- `<Button />`
- `<Calendar />`
- `<Card />`
- `<CardContent />`
- `<CardHeader />`
- `<CardTitle />`
- `<CartesianGrid />`
- `<CatalogStatisticsPanel />`
- `<ChangeCell />`
- `<ChevronLeft />`
- `<ChevronRight />`
- `<ComparePreset />`
- `<ComposedChart />`
- `<DashboardChartDataPoint />`
- `<DashboardMonthlyBreakdownCards />`
- `<DashboardPeriodSelector />`
- `<Delta />`
- `<Dialog />`
- `<DialogContent />`
- `<DialogFooter />`
- `<DialogHeader />`
- `<DialogTitle />`
- `<DollarSign />`
- `<FileSpreadsheet />`
- … 26 component khác

## Dialog / modal (tiêu đề)

- Chọn khoảng thời gian

## Import chính (đầu file)

- `import { useState, useEffect, useMemo, useRef } from "react";`
- `import { useQuery } from "@tanstack/react-query";`
- `import { useGetMe, getGetMeQueryKey } from "@workspace/api-client-react";`
- `import { formatVND, formatChartAxisMoney } from "@/lib/utils";`
- `import { PaymentBreakdownLines } from "@/components/PaymentBreakdown";`
- `import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";`
- `import { Table, TableBody, TableCell, TableHead, TableHeader, TableRow } from "@/components/ui/table";`
- `import { Button } from "@/components/ui/button";`
- `import { Dialog, DialogContent, DialogFooter, DialogHeader, DialogTitle } from "@/components/ui/dialog";`
- `import { Calendar } from "@/components/ui/calendar";`
- `import { DashboardPeriodSelector } from "@/components/DashboardPeriodSelector";`
- `import { CatalogStatisticsPanel } from "@/components/CatalogStatisticsPanel";`
- `import { DashboardMonthlyBreakdownCards } from "@/components/DashboardMonthlyBreakdownCards";`
- `import {`
- `import { useVietnamCalendarDay } from "@/lib/use-vietnam-calendar-day";`
- `import type { DashboardChartDataPoint } from "@/components/DashboardChartTooltip";`
- `import { QuarterChartGranularityToggle } from "@/components/QuarterChartGranularityToggle";`
- `import { chartPointsForMonthlyBreakdown, showsDashboardMonthlyBreakdown } from "@/lib/dashboard-chart-breakdown";`
- … 10 import khác

## Module `@/lib/...` được import

- `@/lib/chain-analytics-excel-export`
- `@/lib/dashboard-chart-breakdown`
- `@/lib/dashboard-period`
- `@/lib/dashboard-visitor-metrics`
- `@/lib/sales-api`
- `@/lib/session-permissions`
- `@/lib/use-vietnam-calendar-day`
- `@/lib/utils`

## Component `@/components/...` (đã quét API lớp 1)

- `PaymentBreakdown` → `artifacts/pos-app/src/components/PaymentBreakdown.tsx`
- `ui/card` → `artifacts/pos-app/src/components/ui/card.tsx`
- `ui/table` → `artifacts/pos-app/src/components/ui/table.tsx`
- `ui/button` → `artifacts/pos-app/src/components/ui/button.tsx`
- `ui/dialog` → `artifacts/pos-app/src/components/ui/dialog.tsx`
- `ui/calendar` → `artifacts/pos-app/src/components/ui/calendar.tsx`
- `DashboardPeriodSelector` → `artifacts/pos-app/src/components/DashboardPeriodSelector.tsx`
- `CatalogStatisticsPanel` → `artifacts/pos-app/src/components/CatalogStatisticsPanel.tsx`
- `DashboardMonthlyBreakdownCards` → `artifacts/pos-app/src/components/DashboardMonthlyBreakdownCards.tsx`
- `DashboardChartTooltip` → `artifacts/pos-app/src/components/DashboardChartTooltip.tsx`
- `QuarterChartGranularityToggle` → `artifacts/pos-app/src/components/QuarterChartGranularityToggle.tsx`

## Chuỗi `/api/...` (page + component con, 6 mục)

- `/api/chain-dashboard/period-sold-stats${chartQs}`
- `/api/chain-dashboard/period-visitor-stats${chartQs}`
- `/api/chain-dashboard/revenue-chart${chartQs}`
- `/api/shops` → [`api-modules/shops.md`](../api-modules/shops.md)
- `/api/statistics/overview?${filterParams(filters, shopId)}` → [`api-modules/statistics.md`](../api-modules/statistics.md)
- `/api/statistics/trend?${filterParams(filters, shopId)}` → [`api-modules/statistics.md`](../api-modules/statistics.md)

## File liên quan

- Route khai báo: `artifacts/pos-app/src/App.tsx`
- Layout/menu: `components/layout/app-layout.tsx`
- Session: `lib/session-cache.ts`, `lib/use-session-user.ts`
