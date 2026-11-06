# Frontend: `vat-inbound.tsx`

**Mô tả:** HĐ đầu vào VAT: import, kéo CQT, MST lọc, ghép SP, nhập kho. (URL /vat-inbound, VatInboundInvoices, ~5847 dòng).

**Source Shop:** `artifacts/pos-app/src/pages/vat-inbound.tsx`

**URL (wouter):** `/vat-inbound`
**Component:** `VatInboundInvoices`
**Độ lớn:** ~5847 dòng.

**Route:** `/vat-inbound`

## Cấu trúc UI

- **Tab Hoá đơn:** lọc archive (Tất cả / Đang dùng / Lưu trữ / **Khác**), lọc trạng thái ghép hàng, lọc ngày.
- **Tab Danh sách phiếu:** HĐ đã ghép — chờ nhập kho, thiếu, đã nhận, đề nghị hoàn tác, ghép thiếu dòng.
- **Toolbar:** MST lọc (modal), Mẫu Excel, Nhập Excel, Nhập PDF.
- **Khối Lấy từ cơ quan thuế:** chọn from/to, POST sync-tax; toast archive MST.

## State & logic quan trọng

- `PageTab`: `invoices` | `receipts`.
- `InvoiceArchiveFilter`: `active` | `archived` | `other` | `all` — HĐ trùng MST lọc vào **Khác**.
- IndexedDB `allRows` merge server qua `mergeServerInvoices`, `listVatInboundInvoices`.
- Parse PDF local: `parseVatInboundPdfBytes`, revision `VAT_INBOUND_PARSE_REVISION`.
- Ghép hàng: `openStockReceipt`, `createVatInboundStockReceipt`, PO inline trên HĐ.
- Dialog chi tiết HĐ: dòng VAT, ghép SP, nhật ký audit, PDF preview.

## API client (`lib/vat-inbound-api.ts`)

- `syncVatInboundFromTax`, `saveVatInboundMarkedMstArchive`, `getVatInboundMarkedMstArchive`
- `createVatInboundStockReceipt`, `receiveVatInboundStock`, `archiveVatInboundInvoice`
- Upsert/list: `listVatInboundFromApi`, `upsertVatInboundToApi`

## Quyền

- `canAccess`: hub + role accountant/manager/admin/warehouse_keeper (xem file đầu component).
- `canEditMarkedMst`: admin/manager — MST lọc modal.

## Quyền (phát hiện trong source)

- Có kiểm tra role **`super_admin`** (hoặc redirect dashboard).

## Tab UI (`TabsTrigger` value)

- `invoices`
- `receipts`

## JSX component dùng trong file (PascalCase)

- `<AlertDialog />`
- `<AlertDialogAction />`
- `<AlertDialogCancel />`
- `<AlertDialogContent />`
- `<AlertDialogDescription />`
- `<AlertDialogFooter />`
- `<AlertDialogHeader />`
- `<AlertDialogTitle />`
- `<AlertTriangle />`
- `<Archive />`
- `<ArchiveRestore />`
- `<Badge />`
- `<Bookmark />`
- `<Button />`
- `<Check />`
- `<Checkbox />`
- `<ChevronDown />`
- `<ChevronRight />`
- `<CircleAlert />`
- `<CircleCheck />`
- `<ClipboardCheck />`
- `<ClipboardList />`
- `<CloudDownload />`
- `<DateFilter />`
- `<DateRangeFilter />`
- … 69 component khác

## Dialog / modal (tiêu đề)

- Chi tiết hoá đơn{" "}
              {detail ? [detail.series, detail.invoiceNo].filter(Boolean).join(" ") || "" : ""}
- {canDirectRollback ? "Hoàn tác nhập kho?" : "Đề nghị hoàn tác nhập kho?"}
- {receivePo?.status === "partial" ? "Nhận bổ sung từ hoá đơn VAT" : "Nhập kho từ hoá đơn VAT"}
- Bỏ lưu trữ hoá đơn?
- Ghép hàng từ HĐ VAT
- Hoàn tác chốt ghép thiếu?
- Khôi phục sản phẩm vào phiếu nhập kho
- Không ghép các dòng HĐ còn lại?
- Lưu trữ hoá đơn?
- Phiếu nhập kho tổng
- Tạo sản phẩm mới
- Xem trước dữ liệu nhập
- Đóng phần thiếu?

## Import chính (đầu file)

- `import { Fragment, useCallback, useEffect, useMemo, useRef, useState, type ReactNode } from "react";`
- `import { useQuery, useQueryClient } from "@tanstack/react-query";`
- `import { format, subDays } from "date-fns";`
- `import { vi } from "date-fns/locale";`
- `import { useGetMe } from "@workspace/api-client-react";`
- `import {`
- `import { withApiAuthHeaders } from "@/lib/api-auth-fetch";`
- `import { cn, formatVND, productImageUrl } from "@/lib/utils";`
- `import { DEFAULT_VAT_RATE, formatVatRateDisplayLabel } from "@/lib/vat";`
- `import { getStockExcludedLineIndexes, hasStockExcludedLines } from "@/lib/vat-inbound-excluded-lines";`
- `import {`
- `import {`
- `import {`
- `import {`
- `import {`

## Module `@/lib/...` được import

- `@/lib/api-auth-fetch`
- `@/lib/offline/products`
- `@/lib/parse-vat-inbound-pdf`
- `@/lib/print-pdf`
- `@/lib/sales-api`
- `@/lib/utils`
- `@/lib/variant-stock`
- `@/lib/vat`
- `@/lib/vat-inbound-api`
- `@/lib/vat-inbound-audit`
- `@/lib/vat-inbound-auto-archive-mst`
- `@/lib/vat-inbound-excel-import`
- `@/lib/vat-inbound-excluded-lines`
- `@/lib/vat-inbound-stock-status`

## Chuỗi `/api/...` (page + component con, 3 mục)

- `/api/organizations/current`
- `/api/products/${productId}/variants/${v.id}` → [`api-modules/products.md`](../api-modules/products.md)
- `/api/suppliers?active=true`

## Luồng nghiệp vụ (doc)

- `nghiep-vu/06-hoa-don-dau-vao-tong-quan.md`

## File liên quan

- Route khai báo: `artifacts/pos-app/src/App.tsx`
- Layout/menu: `components/layout/app-layout.tsx`
- Session: `lib/session-cache.ts`, `lib/use-session-user.ts`
