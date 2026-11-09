# Trang giao diện: `reports.tsx`

**Mô tả:** Báo cáo nhân viên, in lại bill, doanh số.

**Mã nguồn Shop:** `artifacts/pos-app/src/pages/reports.tsx`

**Đường dẫn URL:** `/reports`
**Tên component React:** `Reports`
**Quy mô:** ~2178 dòng.

## Thông tin hiển thị

Nội dung người dùng **nhìn thấy** trên màn hình (trích nhãn từ TSX; số liệu động từ API).

### `reports.tsx`

**Tiêu đề trang:** “Báo cáo nhân viên”
**Thẻ / chỉ số (CardTitle):**
- Doanh thu theo nhân viên bán hàng
- Top NV — sự kiện rủi ro cao
- Top NV — thao tác nhạy cảm
- Top NV — thao tác trên sản phẩm
- Top NV — thao tác phiếu NX
- Top người thực hiện — thao tác đặt hàng
**Cột bảng:**
- Mã đơn
- Thời gian tạo
- Trạng thái
- Tổng tiền
- Lý do huỷ
- Thời gian in
- Trạng thái đơn
- Ghi chú đơn
- Chi nhánh
- Nhân viên
- Vai trò
- Tổng đơn
- Hoàn thành
- Đơn trong ca
- Đã huỷ
- Đề nghị huỷ
- Doanh thu
- In lại
- Họ tên
- Số ca
- Doanh thu ca
- Đơn phân bổ
- Doanh thu phân bổ
- Thời gian
- Người tạo đơn
- Người in lại
- Rủi ro cao
- Ca
- NV ca
- Tab
- Hành động
- Sản phẩm
- SL
- Giá trị
- Rủi ro
- Số sự kiện
- Mô tả
- Nhạy cảm
- Tác động TM
- Ghi chú
**Nhãn lọc / preset / placeholder:**
- Quản trị hệ thống
- Quản trị viên
- Quản lý
- Kế toán
- Thủ kho
- Nhân viên
- Tất cả hành động
- Tất cả mức rủi ro

## Thao tác người dùng

Hành động chính (nút, menu, mục dialog) — không liệt kê mọi nút icon-only.

### `reports.tsx`

**Thao tác:**
- void handleExport()} >

**Đường dẫn:** `/reports`

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

## Module API liên quan (trong Map)

- [`reports`](../../module-api/bao-cao-api/) — nhóm `/api/reports`
- [`shops`](../../module-api/cua-hang/) — nhóm `/api/shops`

**Đọc tiếp:** [Hướng dẫn đọc Map](../../huong-dan-doc/)

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

- `/api/reports/order-audit/summary?${dateParams}` → [`reports`](../../module-api/bao-cao-api/)
- `/api/reports/order-audit?${exportOrderAuditParams}` → [`reports`](../../module-api/bao-cao-api/)
- `/api/reports/order-audit?${orderAuditFilterParams}` → [`reports`](../../module-api/bao-cao-api/)
- `/api/reports/pos-cart-audit/summary?${dateParams}` → [`reports`](../../module-api/bao-cao-api/)
- `/api/reports/pos-cart-audit?${auditFilterParams}` → [`reports`](../../module-api/bao-cao-api/)
- `/api/reports/pos-cart-audit?${exportAuditParams}` → [`reports`](../../module-api/bao-cao-api/)
- `/api/reports/product-audit/summary?${dateParams}` → [`reports`](../../module-api/bao-cao-api/)
- `/api/reports/product-audit?${exportProductAuditParams}` → [`reports`](../../module-api/bao-cao-api/)
- `/api/reports/product-audit?${productAuditFilterParams}` → [`reports`](../../module-api/bao-cao-api/)
- `/api/reports/purchase-order-audit/summary?${dateParams}` → [`reports`](../../module-api/bao-cao-api/)
- `/api/reports/purchase-order-audit?${exportPoAuditParams}` → [`reports`](../../module-api/bao-cao-api/)
- `/api/reports/purchase-order-audit?${poAuditFilterParams}` → [`reports`](../../module-api/bao-cao-api/)
- `/api/reports/reprints?${dateParams}` → [`reports`](../../module-api/bao-cao-api/)
- `/api/reports/reprints?${dateParams}&limit=${EXPORT_ROW_LIMIT}` → [`reports`](../../module-api/bao-cao-api/)
- `/api/reports/sales-staff?${dateParams}` → [`reports`](../../module-api/bao-cao-api/)
- `/api/reports/staff/${userId}/detail?${detailParams}` → [`reports`](../../module-api/bao-cao-api/)
- `/api/reports/staff?${dateParams}` → [`reports`](../../module-api/bao-cao-api/)
- `/api/reports/stock-request-audit/summary?${dateParams}` → [`reports`](../../module-api/bao-cao-api/)
- `/api/reports/stock-request-audit?${exportStockAuditParams}` → [`reports`](../../module-api/bao-cao-api/)
- `/api/reports/stock-request-audit?${stockAuditFilterParams}` → [`reports`](../../module-api/bao-cao-api/)
- `/api/shops` → [`shops`](../../module-api/cua-hang/)

## Liên kết mã

- Khai báo URL: `artifacts/pos-app/src/App.tsx`
- Menu/layout: `components/layout/app-layout.tsx`
- Phiên đăng nhập: `lib/session-cache.ts`, `lib/use-session-user.ts`
