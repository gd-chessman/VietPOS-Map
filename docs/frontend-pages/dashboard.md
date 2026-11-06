# Frontend: `dashboard.tsx`

**Mô tả:** Tổng quan doanh thu, đơn, tồn thấp theo shop. (URL /dashboard, Dashboard, ~1221 dòng).

**Source Shop:** `artifacts/pos-app/src/pages/dashboard.tsx`

**URL (wouter):** `/dashboard`
**Component:** `Dashboard`
**Độ lớn:** ~1221 dòng.

**Route:** `/dashboard`

Tổng quan doanh thu, đơn, tồn thấp — theo quyền và scope shop.

## Quyền (phát hiện trong source)

- Có kiểm tra role **`super_admin`** (hoặc redirect dashboard).

## JSX component dùng trong file (PascalCase)

- `<AlertTriangle />`
- `<Area />`
- `<AreaChart />`
- `<ArrowLeftRight />`
- `<Badge />`
- `<BadgePercent />`
- `<Ban />`
- `<Banknote />`
- `<Button />`
- `<Card />`
- `<CardContent />`
- `<CardHeader />`
- `<CardTitle />`
- `<CartesianGrid />`
- `<ChevronRight />`
- `<CreditCard />`
- `<DashTopProduct />`
- `<DashboardChartPeriod />`
- `<DashboardChartTooltip />`
- `<DashboardMonthlyBreakdownCards />`
- `<DashboardPeriodCancelCards />`
- `<DashboardPeriodStatCell />`
- `<DashboardPeriodWithCustomRange />`
- `<Dialog />`
- `<DialogContent />`
- … 35 component khác

## Import chính (đầu file)

- `import { useEffect, useMemo, useState } from "react";`
- `import { useQuery } from "@tanstack/react-query";`
- `import { apiGet } from "@/lib/sales-api";`
- `import { useLocation } from "wouter";`
- `import {`
- `import { useSessionUser } from "@/lib/use-session-user";`
- `import { formatVND, productImageUrl, formatChartAxisMoney } from "@/lib/utils";`
- `import { ZoomableThumb } from "@/components/ZoomableThumb";`
- `import { ProductDisplayName } from "@/components/ProductDisplayName";`
- `import { TopRankBadge } from "@/components/TopRankBadge";`
- `import { PaginationBar, DEFAULT_PAGE_SIZE } from "@/components/pagination-bar";`
- `import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";`
- `import { Button } from "@/components/ui/button";`
- `import { Dialog, DialogContent, DialogHeader, DialogTitle, useNestedDialogGuard } from "@/components/ui/dialog";`
- `import { Table, TableBody, TableCell, TableHead, TableHeader, TableRow } from "@/components/ui/table";`
- `import { Badge } from "@/components/ui/badge";`
- `import {`
- `import { DollarSign, ShoppingBag, PackageX, TrendingUp, ChevronRight, AlertTriangle, Ban, Banknote, CreditCard, ArrowLeftRight, FileText, Pencil, BadgePercent, FileSpreadsheet, Receipt, Users, UserCheck, CalendarDays } from "lucide-react";`
- … 11 import khác

## Module `@/lib/...` được import

- `@/lib/chain-analytics-excel-export`
- `@/lib/dashboard-chart-breakdown`
- `@/lib/dashboard-chart-period`
- `@/lib/dashboard-period`
- `@/lib/dashboard-visitor-metrics`
- `@/lib/offline`
- `@/lib/order-invoice-code`
- `@/lib/sales-api`
- `@/lib/use-session-user`
- `@/lib/use-vietnam-calendar-day`
- `@/lib/utils`

## Chuỗi `/api/...` (page + component con, 5 mục)

- `/api/dashboard/period-cancel-stats${periodVisitorQs}` → [`api-modules/dashboard.md`](../api-modules/dashboard.md)
- `/api/dashboard/period-sold-stats${periodVisitorQs}` → [`api-modules/dashboard.md`](../api-modules/dashboard.md)
- `/api/dashboard/period-visitor-stats${periodVisitorQs}` → [`api-modules/dashboard.md`](../api-modules/dashboard.md)
- `/api/dashboard/top-products?${exportTopParams}` → [`api-modules/dashboard.md`](../api-modules/dashboard.md)
- `/api/dashboard/top-products?${topProductsQs}` → [`api-modules/dashboard.md`](../api-modules/dashboard.md)

## Luồng nghiệp vụ (doc)

- `nghiep-vu/01-dang-nhap-va-shop-context.md`

## File liên quan

- Route khai báo: `artifacts/pos-app/src/App.tsx`
- Layout/menu: `components/layout/app-layout.tsx`
- Session: `lib/session-cache.ts`, `lib/use-session-user.ts`
