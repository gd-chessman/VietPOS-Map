# Trang giao diện: `stock-requests.tsx`

**Mô tả:** Phiếu yêu cầu nhập/xuất nội bộ giữa shop. (URL /stock-requests, StockRequestsPage, ~1874 dòng).

**Mã nguồn Shop:** `artifacts/pos-app/src/pages/stock-requests.tsx`

**Đường dẫn URL:** `/stock-requests`
**Tên component React:** `StockRequestsPage`
**Quy mô:** ~1874 dòng.

**Đường dẫn:** `/stock-requests`

Phiếu nhập/xuất: trạng thái chờ duyệt, vận chuyển, nhận hàng, huỷ.

**Đọc tiếp:** [Hướng dẫn đọc Map](../../huong-dan-doc/)

## Quyền (phát hiện trong source)

- Có kiểm tra role **`super_admin`** (hoặc redirect dashboard).

## JSX component dùng trong file (PascalCase)

- `<AlertTriangle />`
- `<ArrowDownToLine />`
- `<ArrowUpFromLine />`
- `<AuditTimeline />`
- `<Badge />`
- `<Building2 />`
- `<Button />`
- `<CancelDialog />`
- `<CheckCircle />`
- `<ChevronDown />`
- `<ChevronUp />`
- `<ClipboardList />`
- `<Clock />`
- `<CreateDialog />`
- `<CreateItem />`
- `<DateFilter />`
- `<DateRangeFilter />`
- `<Dialog />`
- `<DialogContent />`
- `<DialogHeader />`
- `<DialogTitle />`
- `<HTMLDivElement />`
- `<History />`
- `<Info />`
- `<Input />`
- … 27 component khác

## Dialog / modal (tiêu đề)

- Huỷ phiếu

## Import chính (đầu file)

- `import { useState, useRef, useEffect, Fragment, useMemo } from "react";`
- `import { useQuery, useQueryClient } from "@tanstack/react-query";`
- `import { useGetMe, getGetMeQueryKey } from "@workspace/api-client-react";`
- `import { format } from "date-fns";`
- `import { vi } from "date-fns/locale";`
- `import { Button } from "@/components/ui/button";`
- `import { Input } from "@/components/ui/input";`
- `import { Badge } from "@/components/ui/badge";`
- `import { Dialog, DialogContent, DialogHeader, DialogTitle } from "@/components/ui/dialog";`
- `import { Table, TableBody, TableCell, TableHead, TableHeader, TableRow } from "@/components/ui/table";`
- `import { useToast } from "@/hooks/use-toast";`
- `import {`
- `import { printStockRequest } from "@/components/StockRequestPrint";`
- `import { productImageUrl } from "@/lib/utils";`
- `import { useOfflineStatus } from "@/lib/offline";`
- `import { apiGet, apiPatch, apiPost } from "@/lib/sales-api";`
- `import { WifiOff } from "lucide-react";`
- `import { PaginationBar, DEFAULT_PAGE_SIZE } from "@/components/pagination-bar";`
- … 1 import khác

## Module `@/lib/...` được import

- `@/lib/offline`
- `@/lib/sales-api`
- `@/lib/utils`

## Chuỗi `/api/...` (page + component con, 9 mục)

- `/api/products?includeDiscontinued=false`
- `/api/shops` → [`shops`](../../module-api/cua-hang/)
- `/api/stock-requests` → [`stock-requests`](../../module-api/phieu-nhap-xuat/)
- `/api/stock-requests${statusFilter !== "all" ? `
- `/api/stock-requests/${id}` → [`stock-requests`](../../module-api/phieu-nhap-xuat/)
- `/api/stock-requests/${id}/${action}` → [`stock-requests`](../../module-api/phieu-nhap-xuat/)
- `/api/stock-requests/meta/hub-inventory` → [`stock-requests`](../../module-api/phieu-nhap-xuat/)
- `/api/stock-requests/meta/hub-shop` → [`stock-requests`](../../module-api/phieu-nhap-xuat/)
- `/api/stock-requests/meta/shop-inventory?shopId=${toShopId}` → [`stock-requests`](../../module-api/phieu-nhap-xuat/)

## Luồng nghiệp vụ (doc)

- [04-phieu-nhap-xuat-chuyen-kho](../../nghiep-vu/04-phieu-nhap-xuat-chuyen-kho/)

## Liên kết mã

- Khai báo URL: `artifacts/pos-app/src/App.tsx`
- Menu/layout: `components/layout/app-layout.tsx`
- Phiên đăng nhập: `lib/session-cache.ts`, `lib/use-session-user.ts`
