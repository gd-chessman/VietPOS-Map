# Trang giao diện: `statistics.tsx`

**Mô tả:** Thống kê bán theo sản phẩm/kỳ.

**Mã nguồn Shop:** `artifacts/pos-app/src/pages/statistics.tsx`

**Đường dẫn URL:** `/statistics`
**Tên component React:** `Statistics`
**Quy mô:** ~1225 dòng.

## Thông tin hiển thị

Nội dung người dùng **nhìn thấy** trên màn hình (trích nhãn từ TSX; số liệu động từ API).

### `statistics.tsx`

**Tiêu đề trang:** “Thống kê”
**Thẻ / chỉ số (CardTitle):**
- Doanh thu
- Giá vốn
- Lợi nhuận
- Sản phẩm đã bán
- Đơn hàng
**Cột bảng:**
- Chỉ số
- Thay đổi
**Nhãn lọc / preset / placeholder:**
- Hôm nay
- Hôm qua
- 7 ngày qua
- 30 ngày qua
- Tuần này
- Tháng này
- Năm này
- Kỳ liền trước
- Cùng kỳ năm trước

### `@/components/CatalogStatisticsPanel`

**Thẻ / chỉ số (CardTitle):**
- Danh mục & tồn kho
**Cột bảng:**
- Ảnh
- Mã
- Sản phẩm
- Giá bán
- Giá vốn
- Lượt bán
- Doanh thu (kỳ)
- Lợi nhuận (kỳ)
- Tồn kho
**Nhãn lọc / preset / placeholder:**
- Ô nhập: Sắp xếp / lọc
- Ô nhập: Tìm tên, mã...

## Thao tác người dùng

Hành động chính (nút, menu, mục dialog) — không liệt kê mọi nút icon-only.

### `statistics.tsx`

**Thao tác:**
- void handleExportExcel()} >
- Tuỳ chọn
- pick(item.from, item.to)} >
- setShortcutYear((y) => y - 1)}>
- = thisYear} onClick= >
- setRangeModalOpen(false)}>Hủy
- Xem thống kê

**Hộp thoại (tiêu đề):**
- Chọn khoảng thời gian

**Đường dẫn:** `/statistics`

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
- `@/components/DashboardPeriodStatCell` → `artifacts/pos-app/src/components/DashboardPeriodStatCell.tsx`
- `@/components/DashboardChartTooltip` → `artifacts/pos-app/src/components/DashboardChartTooltip.tsx`
- `@/components/QuarterChartGranularityToggle` → `artifacts/pos-app/src/components/QuarterChartGranularityToggle.tsx`

## Cách đọc code

- API: tìm `useQuery`, `useMutation`, `apiFetch`, hoặc mục **Chuỗi `/api/...`** bên dưới.
- Quyền: `lib/session-permissions.ts`, biểu thức trong `app-layout.tsx` và file page.
- Offline: các trang POS có thể gọi Dexie qua `@/lib/offline/...`.

## Module API liên quan (trong Map)

- [`chain-dashboard`](../../module-api/bang-dieu-khiem-chuoi/) — nhóm `/api/chain-dashboard`
- [`shops`](../../module-api/cua-hang/) — nhóm `/api/shops`
- [`statistics`](../../module-api/thong-ke-api/) — nhóm `/api/statistics`

**Đọc tiếp:** [Hướng dẫn đọc Map](../../huong-dan-doc/)

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
- `<DashboardPeriodStatCell />`
- `<Delta />`
- `<Dialog />`
- `<DialogContent />`
- `<DialogFooter />`
- `<DialogHeader />`
- `<DialogTitle />`
- `<DollarSign />`
- … 27 component khác

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
- `import { DashboardPeriodStatCell } from "@/components/DashboardPeriodStatCell";`
- `import {`
- `import { useVietnamCalendarDay } from "@/lib/use-vietnam-calendar-day";`
- `import type { DashboardChartDataPoint } from "@/components/DashboardChartTooltip";`
- `import { QuarterChartGranularityToggle } from "@/components/QuarterChartGranularityToggle";`
- … 11 import khác

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
- `DashboardPeriodStatCell` → `artifacts/pos-app/src/components/DashboardPeriodStatCell.tsx`
- `DashboardChartTooltip` → `artifacts/pos-app/src/components/DashboardChartTooltip.tsx`
- `QuarterChartGranularityToggle` → `artifacts/pos-app/src/components/QuarterChartGranularityToggle.tsx`

## Chuỗi `/api/...` (page + component con, 6 mục)

- `/api/chain-dashboard/period-sold-stats${chartQs}`
- `/api/chain-dashboard/period-visitor-stats${chartQs}`
- `/api/chain-dashboard/revenue-chart${chartQs}`
- `/api/shops` → [`shops`](../../module-api/cua-hang/)
- `/api/statistics/overview?${filterParams(filters, shopId)}` → [`statistics`](../../module-api/thong-ke-api/)
- `/api/statistics/trend?${filterParams(filters, shopId)}` → [`statistics`](../../module-api/thong-ke-api/)

## Liên kết mã

- Khai báo URL: `artifacts/pos-app/src/App.tsx`
- Menu/layout: `components/layout/app-layout.tsx`
- Phiên đăng nhập: `lib/session-cache.ts`, `lib/use-session-user.ts`
