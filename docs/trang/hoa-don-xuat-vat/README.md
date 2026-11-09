# Trang giao diện: `vat-invoices.tsx`

**Mô tả:** Phát hành và quản lý HĐ VAT bán ra (Viettel).

**Mã nguồn Shop:** `artifacts/pos-app/src/pages/vat-invoices.tsx`

**Đường dẫn URL:** `/vat-invoices`
**Tên component React:** `VatInvoices`
**Quy mô:** ~395 dòng.

## Thông tin hiển thị

Nội dung người dùng **nhìn thấy** trên màn hình (trích nhãn từ TSX; số liệu động từ API).

### `vat-invoices.tsx`

**Tiêu đề trang:** “Không có quyền truy cập”, “Hoá đơn xuất VAT”
**Cột bảng:**
- Số HĐ VAT
- Số HĐ POS
- Chi nhánh
- Ngày giờ
- Thu ngân
- Thanh toán
- Trạng thái VAT
- Tổng tiền
**Nhãn lọc / preset / placeholder:**
- Chờ xuất hoá đơn VAT
- Đang xuất VAT
- Đã xuất hoá đơn VAT
- Xuất VAT lỗi
**Tooltip / mô tả ngắn (title=):**
- Sửa thông tin VAT
- Xem thông tin VAT

## Thao tác người dùng

Hành động chính (nút, menu, mục dialog) — không liệt kê mọi nút icon-only.

### `vat-invoices.tsx`

**Thao tác:**
- setEditOrder(order)} >

**Đường dẫn:** `/vat-invoices`

HĐ VAT **xuất** (Viettel SInvoice): phát hành, tra cứu, điều chỉnh theo tích hợp Viettel.

**Đọc tiếp:** [Hướng dẫn đọc Map](../../huong-dan-doc/)

## Quyền (phát hiện trong source)

- Có kiểm tra role **`super_admin`** (hoặc redirect dashboard).

## Query string URL (đọc trong code)

- `shopId`
- `vat`

## JSX component dùng trong file (PascalCase)

- `<Badge />`
- `<Building2 />`
- `<Button />`
- `<DateFilter />`
- `<DateRangeFilter />`
- `<EditInvoiceDialog />`
- `<FileText />`
- `<InvoiceStatusBadge />`
- `<OrderWithItems />`
- `<PaginationBar />`
- `<PaymentMethodCell />`
- `<Pencil />`
- `<Receipt />`
- `<Table />`
- `<TableBody />`
- `<TableCell />`
- `<TableHead />`
- `<TableHeader />`
- `<TableRow />`
- `<VatFilter />`
- `<ViettelConfigWarningBanner />`

## Import chính (đầu file)

- `import { useState, useMemo, useEffect } from "react";`
- `import { useLocation } from "wouter";`
- `import { useQuery, useQueryClient } from "@tanstack/react-query";`
- `import { format } from "date-fns";`
- `import { useGetMe } from "@workspace/api-client-react";`
- `import type { OrderWithItems } from "@workspace/api-client-react";`
- `import { formatVND } from "@/lib/utils";`
- `import { Table, TableBody, TableCell, TableHead, TableHeader, TableRow } from "@/components/ui/table";`
- `import { Badge } from "@/components/ui/badge";`
- `import { Button } from "@/components/ui/button";`
- `import { FileText, Building2, Pencil, Receipt } from "lucide-react";`
- `import { EditInvoiceDialog, type EditableInvoiceOrder, type InvoiceStatus, canRetryVatIssue, isActivelyIssuingAt } from "@/components/EditInvoiceDialog";`
- `import { PaymentMethodCell } from "@/components/PaymentBreakdown";`
- `import { PaginationBar, DEFAULT_PAGE_SIZE } from "@/components/pagination-bar";`
- `import {`
- `import { apiFetch } from "@/lib/api-auth-fetch";`
- `import { resolveOrderInvoiceCode } from "@/lib/order-invoice-code";`
- `import { ViettelConfigWarningBanner } from "@/components/ViettelConfigWarningBanner";`

## Module `@/lib/...` được import

- `@/lib/api-auth-fetch`
- `@/lib/order-invoice-code`
- `@/lib/utils`

## Chuỗi `/api/...` (page + component con, 8 mục)

- `/api/dashboard/revenue-chart` → [`dashboard`](../../module-api/bang-dieu-khiem-api/)
- `/api/orders/${order!.id}/invoice-logs` → [`orders`](../../module-api/don-hang-api/)
- `/api/orders/${order.id}/invoice` → [`orders`](../../module-api/don-hang-api/)
- `/api/orders/${order.id}/invoice/issue` → [`orders`](../../module-api/don-hang-api/)
- `/api/orders/${orderId}/invoice/pdf` → [`orders`](../../module-api/don-hang-api/)
- `/api/orders?${params}`
- `/api/shops` → [`shops`](../../module-api/cua-hang/)
- `/api/viettel-invoice/settings`

## Luồng nghiệp vụ (doc)

- [05-hoa-don-vat-xuat](../../nghiep-vu/05-hoa-don-vat-xuat/)

## Liên kết mã

- Khai báo URL: `artifacts/pos-app/src/App.tsx`
- Menu/layout: `components/layout/app-layout.tsx`
- Phiên đăng nhập: `lib/session-cache.ts`, `lib/use-session-user.ts`
