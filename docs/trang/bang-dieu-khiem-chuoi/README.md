# Trang giao diện: `chain-dashboard.tsx`

**Mô tả:** Dashboard tổng hợp chuỗi cửa hàng theo quyền. (URL /chain-dashboard, ChainDashboard, ~2003 dòng).

**Mã nguồn Shop:** `artifacts/pos-app/src/pages/chain-dashboard.tsx`

**Đường dẫn URL:** `/chain-dashboard`
**Tên component React:** `ChainDashboard`
**Quy mô:** ~2003 dòng.

**Đường dẫn:** `/chain-dashboard`

Dashboard tổng hợp chuỗi cửa hàng theo quyền.

## Menu sidebar

- **Nhãn:** Dashboard chuỗi
- **Điều kiện hiện menu (`show`):** `canViewChainDashboard`

## Component con (logic UI chính)

- `@/components/NotificationBell` → `artifacts/pos-app/src/components/NotificationBell.tsx`
- `@/components/ZoomableThumb` → `artifacts/pos-app/src/components/ZoomableThumb.tsx`
- `@/components/ProductDisplayName` → `artifacts/pos-app/src/components/ProductDisplayName.tsx`
- `@/components/TopRankBadge` → `artifacts/pos-app/src/components/TopRankBadge.tsx`
- `@/components/DashboardChartTooltip` → `artifacts/pos-app/src/components/DashboardChartTooltip.tsx`
- `@/components/EditInvoiceDialog` → `artifacts/pos-app/src/components/EditInvoiceDialog.tsx`
- `@/components/PaymentBreakdown` → `artifacts/pos-app/src/components/PaymentBreakdown.tsx`
- `@/components/ui/card` → `artifacts/pos-app/src/components/ui/card.tsx`
- `@/components/ui/button` → `artifacts/pos-app/src/components/ui/button.tsx`
- `@/components/QuarterChartGranularityToggle` → `artifacts/pos-app/src/components/QuarterChartGranularityToggle.tsx`
- `@/components/DashboardMonthlyBreakdownCards` → `artifacts/pos-app/src/components/DashboardMonthlyBreakdownCards.tsx`
- `@/components/DashboardPeriodCancelCards` → `artifacts/pos-app/src/components/DashboardPeriodCancelCards.tsx`
- `@/components/DashboardPeriodStatCell` → `artifacts/pos-app/src/components/DashboardPeriodStatCell.tsx`
- `@/components/pagination-bar` → `artifacts/pos-app/src/components/pagination-bar.tsx`
- `@/components/DashboardPeriodWithCustomRange` → `artifacts/pos-app/src/components/DashboardPeriodWithCustomRange.tsx`
- `@/components/ChainDashboardInboundActionsPanel` → `artifacts/pos-app/src/components/ChainDashboardInboundActionsPanel.tsx`
- `@/components/ui/dialog` → `artifacts/pos-app/src/components/ui/dialog.tsx`
- `@/components/ui/table` → `artifacts/pos-app/src/components/ui/table.tsx`
- `@/components/ui/badge` → `artifacts/pos-app/src/components/ui/badge.tsx`
- `@/components/OrderModerateConfirmDialog` → `artifacts/pos-app/src/components/OrderModerateConfirmDialog.tsx`

## Cách đọc code

- API: tìm `useQuery`, `useMutation`, `apiFetch`, hoặc mục **Chuỗi `/api/...`** bên dưới.
- Quyền: `lib/session-permissions.ts`, biểu thức trong `app-layout.tsx` và file page.
- Offline: các trang POS có thể gọi Dexie qua `@/lib/offline/...`.

## Module API liên quan (trong Map)

- [`chain-dashboard`](../../module-api/bang-dieu-khiem-chuoi/) — nhóm `/api/chain-dashboard`
- [`chain-dashboard${qs}`](../../module-api/chain-dashboard${qs}/) — nhóm `/api/chain-dashboard${qs}`
- [`orders`](../../module-api/don-hang-api/) — nhóm `/api/orders`
- [`shops`](../../module-api/cua-hang/) — nhóm `/api/shops`

**Đọc tiếp:** [Hướng dẫn đọc Map](../../huong-dan-doc/)

## Quyền (phát hiện trong source)

- Có kiểm tra role **`super_admin`** (hoặc redirect dashboard).

## JSX component dùng trong file (PascalCase)

- `<AlertTriangle />`
- `<Area />`
- `<AreaChart />`
- `<ArrowDownRight />`
- `<ArrowLeftRight />`
- `<ArrowUpRight />`
- `<Badge />`
- `<BadgePercent />`
- `<Ban />`
- `<Banknote />`
- `<Building2 />`
- `<Button />`
- `<Card />`
- `<CardContent />`
- `<CardHeader />`
- `<CardTitle />`
- `<CartesianGrid />`
- `<ChainDashboardInboundActionsPanel />`
- `<CheckCircle2 />`
- `<ChevronRight />`
- `<CreditCard />`
- `<DashboardChartPeriod />`
- `<DashboardChartTooltip />`
- `<DashboardMonthlyBreakdownCards />`
- `<DashboardPeriodCancelCards />`
- … 61 component khác

## Dialog / modal (tiêu đề)

- Hàng sắp hết — {shopName}

## Import chính (đầu file)

- `import { useEffect, useMemo, useRef, useState } from "react";`
- `import { useLocation } from "wouter";`
- `import { useGetMe, getGetMeQueryKey } from "@workspace/api-client-react";`
- `import { useQuery, useQueryClient } from "@tanstack/react-query";`
- `import { format, formatDistanceToNow } from "date-fns";`
- `import { vi } from "date-fns/locale";`
- `import { BarChart, Bar, XAxis, YAxis, CartesianGrid, Tooltip as RechartsTooltip, ResponsiveContainer, LineChart, Line, AreaChart, Area } from "recharts";`
- `import { DollarSign, ShoppingBag, PackageX, Banknote, CreditCard, ArrowLeftRight, AlertTriangle, ChevronRight, Ban, Building2, FileText, Pencil, CheckCircle2, XCircle, RotateCcw, FileSpreadsheet, BadgePercent, ArrowUpRight, ArrowDownRight, Minus, Receipt, Users, UserCheck, CalendarDays, TrendingUp } from "lucide-react";`
- `import { NotificationInboxPanel } from "@/components/NotificationBell";`
- `import { useToast } from "@/hooks/use-toast";`
- `import { apiFetch } from "@/lib/api-auth-fetch";`
- `import { apiGet } from "@/lib/sales-api";`
- `import { cn, formatVND, productImageUrl, formatChartAxisMoney } from "@/lib/utils";`
- `import { orderDiscountAmount } from "@/lib/order-discount";`
- `import { ZoomableThumb } from "@/components/ZoomableThumb";`
- `import { ProductDisplayName } from "@/components/ProductDisplayName";`
- `import { TopRankBadge } from "@/components/TopRankBadge";`
- `import { DashboardChartTooltip, type DashboardChartDataPoint } from "@/components/DashboardChartTooltip";`
- … 14 import khác

## Module `@/lib/...` được import

- `@/lib/api-auth-fetch`
- `@/lib/cancel-order`
- `@/lib/chain-analytics-excel-export`
- `@/lib/dashboard-chart-breakdown`
- `@/lib/dashboard-chart-period`
- `@/lib/dashboard-period`
- `@/lib/dashboard-visitor-metrics`
- `@/lib/order-discount`
- `@/lib/order-invoice-code`
- `@/lib/sales-api`
- `@/lib/use-vietnam-calendar-day`
- `@/lib/utils`

## Component `@/components/...` (đã quét API lớp 1)

- `NotificationBell` → `artifacts/pos-app/src/components/NotificationBell.tsx`
- `ZoomableThumb` → `artifacts/pos-app/src/components/ZoomableThumb.tsx`
- `ProductDisplayName` → `artifacts/pos-app/src/components/ProductDisplayName.tsx`
- `TopRankBadge` → `artifacts/pos-app/src/components/TopRankBadge.tsx`
- `DashboardChartTooltip` → `artifacts/pos-app/src/components/DashboardChartTooltip.tsx`
- `EditInvoiceDialog` → `artifacts/pos-app/src/components/EditInvoiceDialog.tsx`
- `PaymentBreakdown` → `artifacts/pos-app/src/components/PaymentBreakdown.tsx`
- `ui/card` → `artifacts/pos-app/src/components/ui/card.tsx`
- `ui/button` → `artifacts/pos-app/src/components/ui/button.tsx`
- `QuarterChartGranularityToggle` → `artifacts/pos-app/src/components/QuarterChartGranularityToggle.tsx`
- `DashboardMonthlyBreakdownCards` → `artifacts/pos-app/src/components/DashboardMonthlyBreakdownCards.tsx`
- `DashboardPeriodCancelCards` → `artifacts/pos-app/src/components/DashboardPeriodCancelCards.tsx`
- `DashboardPeriodStatCell` → `artifacts/pos-app/src/components/DashboardPeriodStatCell.tsx`
- `pagination-bar` → `artifacts/pos-app/src/components/pagination-bar.tsx`
- `DashboardPeriodWithCustomRange` → `artifacts/pos-app/src/components/DashboardPeriodWithCustomRange.tsx`
- `ChainDashboardInboundActionsPanel` → `artifacts/pos-app/src/components/ChainDashboardInboundActionsPanel.tsx`
- `ui/dialog` → `artifacts/pos-app/src/components/ui/dialog.tsx`
- `ui/table` → `artifacts/pos-app/src/components/ui/table.tsx`
- `ui/badge` → `artifacts/pos-app/src/components/ui/badge.tsx`
- `OrderModerateConfirmDialog` → `artifacts/pos-app/src/components/OrderModerateConfirmDialog.tsx`

## Chuỗi `/api/...` (page + component con, 12 mục)

- `/api/chain-dashboard${qs}`
- `/api/chain-dashboard/low-stock${qs}`
- `/api/chain-dashboard/orders-today`
- `/api/chain-dashboard/period-cancel-stats${chartQs}`
- `/api/chain-dashboard/period-sold-stats${chartQs}`
- `/api/chain-dashboard/period-visitor-stats${chartQs}`
- `/api/chain-dashboard/revenue-chart${chartQs}`
- `/api/chain-dashboard/top-products${topQs}`
- `/api/chain-dashboard/top-products?${exportParams}`
- `/api/orders/${order.id}/${action}` → [`orders`](../../module-api/don-hang-api/)
- `/api/orders/${orderId}/${action}` → [`orders`](../../module-api/don-hang-api/)
- `/api/shops` → [`shops`](../../module-api/cua-hang/)

## Liên kết mã

- Khai báo URL: `artifacts/pos-app/src/App.tsx`
- Menu/layout: `components/layout/app-layout.tsx`
- Phiên đăng nhập: `lib/session-cache.ts`, `lib/use-session-user.ts`
