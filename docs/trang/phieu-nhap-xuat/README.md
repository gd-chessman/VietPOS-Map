# Trang giao diện: `stock-requests.tsx`

**Mô tả:** Phiếu yêu cầu nhập/xuất nội bộ giữa shop. (URL /stock-requests, StockRequestsPage, ~1874 dòng).

**Mã nguồn Shop:** `artifacts/pos-app/src/pages/stock-requests.tsx`

**Đường dẫn URL:** `/stock-requests`
**Tên component React:** `StockRequestsPage`
**Quy mô:** ~1874 dòng.

## Thông tin hiển thị

Nội dung người dùng **nhìn thấy** trên màn hình (trích nhãn từ TSX; số liệu động từ API).

### `stock-requests.tsx`

**Tiêu đề trang:** “Phiếu nhập/xuất kho”
**Cột bảng:**
- Sản phẩm
- Mã
- SL
- Tồn kho chính
- Tồn chi nhánh gửi
- Tồn chi nhánh nhận
- Số lượng
- Ghi chú
- Mã phiếu
- Loại
- Trạng thái
- Từ CN
- Đến CN
- Người yêu cầu
- Ngày tạo
- Thao tác
**Nhãn lọc / preset / placeholder:**
- Ô nhập: Tìm sản phẩm theo tên hoặc mã...
- Ô nhập: Lý do huỷ...
- Ô nhập: Lý do từ chối...
- Ô nhập: Họ tên người nhận...
- Ô nhập: Ghi chú...
- Ô nhập: Lý do, ghi chú thêm...
- Chờ duyệt
- Đã duyệt
- Đang vận chuyển
- Hoàn thành
- Từ chối
- Đã huỷ
- Tạo phiếu
- Duyệt
- Huỷ
- Tất cả
- Tất cả loại
- Phiếu nhập
- Phiếu xuất

## Thao tác người dùng

Hành động chính (nút, menu, mục dialog) — không liệt kê mọi nút icon-only.

### `stock-requests.tsx`

**Thao tác:**
- Đóng
- Xác nhận huỷ
- Huỷ
- Xác nhận từ chối
- onConfirm(trimmedReceiver)} disabled= > Xác nhận nhận hàng
- } > Tạo phiếu nhập
- } > Tạo phiếu xuất
- printStockRequest( )), })} > In
- doAction(req.id, "approve")} > Duyệt
- setRejectTarget(req.id)} > Từ chối
- doAction(req.id, "ship")} > Vận chuyển
- setCompleteTarget(req)} title= >
- setCancelTarget(req.id)} > Huỷ

**Hộp thoại (tiêu đề):**
- Huỷ phiếu

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
