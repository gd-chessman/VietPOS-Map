# Frontend: `vat-invoices.tsx`

**Mô tả:** Phát hành và quản lý HĐ VAT bán ra (Viettel). (URL /vat-invoices, VatInvoices, ~395 dòng).

**Source Shop:** `artifacts/pos-app/src/pages/vat-invoices.tsx`

**URL (wouter):** `/vat-invoices`
**Component:** `VatInvoices`
**Độ lớn:** ~395 dòng.

**Route:** `/vat-invoices`

HĐ VAT **xuất** (Viettel SInvoice): phát hành, tra cứu, điều chỉnh theo tích hợp Viettel.

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

- `/api/dashboard/revenue-chart` → [`api-modules/dashboard.md`](../api-modules/dashboard.md)
- `/api/orders/${order!.id}/invoice-logs` → [`api-modules/orders.md`](../api-modules/orders.md)
- `/api/orders/${order.id}/invoice` → [`api-modules/orders.md`](../api-modules/orders.md)
- `/api/orders/${order.id}/invoice/issue` → [`api-modules/orders.md`](../api-modules/orders.md)
- `/api/orders/${orderId}/invoice/pdf` → [`api-modules/orders.md`](../api-modules/orders.md)
- `/api/orders?${params}`
- `/api/shops` → [`api-modules/shops.md`](../api-modules/shops.md)
- `/api/viettel-invoice/settings`

## Luồng nghiệp vụ (doc)

- `nghiep-vu/05-hoa-don-vat-xuat.md`

## File liên quan

- Route khai báo: `artifacts/pos-app/src/App.tsx`
- Layout/menu: `components/layout/app-layout.tsx`
- Session: `lib/session-cache.ts`, `lib/use-session-user.ts`
