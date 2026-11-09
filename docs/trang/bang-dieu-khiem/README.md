# Trang giao diện: `dashboard.tsx`

**Mô tả:** Tổng quan doanh thu, đơn, tồn thấp theo shop.

**Mã nguồn Shop:** `artifacts/pos-app/src/pages/dashboard.tsx`

**Đường dẫn URL:** `/dashboard`
**Tên component React:** `Dashboard`
**Quy mô:** ~1221 dòng.

## Thông tin hiển thị

Nội dung người dùng **nhìn thấy** trên màn hình (trích nhãn từ TSX; số liệu động từ API).

### `dashboard.tsx`

**Tiêu đề trang:** “Dashboard”
**Thẻ / chỉ số (CardTitle):**
- Sản phẩm đã bán
- Cảnh báo tồn kho
- Phân tích doanh thu
**Cột bảng:**
- STT
- Số HĐ
- Giờ
- Thu ngân
- Thanh toán
- Trạng thái
- Số món
- Tổng tiền
- Ảnh
- Sản phẩm
- Mã nội bộ
- SL đã bán
- Doanh thu
- Tồn kho
- Giá bán
**Nhãn lọc / preset / placeholder:**
- Doanh thu
- Lợi nhuận
- Số lượng

## Thao tác người dùng

Hành động chính (nút, menu, mục dialog) — không liệt kê mọi nút icon-only.

### `dashboard.tsx`

**Thao tác:**
- setEditOpen(true)}> Sửa / xử lý hoá đơn VAT
- void handleExportExcel()} >
- setTopSort(opt.key)} >

**Đường dẫn:** `/dashboard`

Tổng quan doanh thu, đơn, tồn thấp — theo quyền và scope shop.

**Đọc tiếp:** [Hướng dẫn đọc Map](../../huong-dan-doc/)

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

- `/api/dashboard/period-cancel-stats${periodVisitorQs}` → [`dashboard`](../../module-api/bang-dieu-khiem-api/)
- `/api/dashboard/period-sold-stats${periodVisitorQs}` → [`dashboard`](../../module-api/bang-dieu-khiem-api/)
- `/api/dashboard/period-visitor-stats${periodVisitorQs}` → [`dashboard`](../../module-api/bang-dieu-khiem-api/)
- `/api/dashboard/top-products?${exportTopParams}` → [`dashboard`](../../module-api/bang-dieu-khiem-api/)
- `/api/dashboard/top-products?${topProductsQs}` → [`dashboard`](../../module-api/bang-dieu-khiem-api/)

## Luồng nghiệp vụ (doc)

- [01-dang-nhap-va-shop-context](../../nghiep-vu/01-dang-nhap-va-shop-context/)

## Liên kết mã

- Khai báo URL: `artifacts/pos-app/src/App.tsx`
- Menu/layout: `components/layout/app-layout.tsx`
- Phiên đăng nhập: `lib/session-cache.ts`, `lib/use-session-user.ts`
