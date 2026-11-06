# Trang giao diện: `vat-inbound.tsx`

**Mô tả:** HĐ đầu vào VAT: import, kéo CQT, MST lọc, ghép SP, nhập kho. (URL /vat-inbound, VatInboundInvoices, ~5847 dòng).

**Mã nguồn Shop:** `artifacts/pos-app/src/pages/vat-inbound.tsx`

**Đường dẫn URL:** `/vat-inbound`
**Tên component React:** `VatInboundInvoices`
**Quy mô:** ~5847 dòng.

## Thông tin hiển thị

Nội dung người dùng **nhìn thấy** trên màn hình (trích nhãn từ TSX; số liệu động từ API).

### `vat-inbound.tsx`

**Tiêu đề trang:** “Không có quyền truy cập”, “Hoá đơn nhập VAT”
**Cột bảng:**
- STT
- Tên hàng
- Số lượng
- ĐVT
- Đơn giá
- VAT
- Thành tiền
- Thuế suất
- Chưa thuế
- Tiền thuế
- Cộng
- Ngày HĐ
- Số HĐ
- Ký hiệu
- Nhà cung cấp
- MST bán
- Tổng tiền
- Ghép hàng
- Trạng thái
- Ngày tạo
- Thao tác
- Ảnh
- Sản phẩm
- Mã sản phẩm
- Tồn
- Số lượng trên HĐ
- Đã nhận
- Giá nhập
- Giá bán
- Tên trên HĐ
- Thuế
- Sản phẩm (theo tên hóa đơn VAT nội bộ)
- File
- Nhận lần này
**Tab / khu vực:**
- Hoá đơn
- Danh sách phiếu )}
**Nhãn lọc / preset / placeholder:**
- Danh sách MST
- Lý do
- Tên sản phẩm
- Mã sản phẩm / Barcode
- Giá nhập
- Giá bán
- Tên VAT nội bộ
- ĐVT
- Nhà cung cấp
- Sản phẩm trong kho nội bộ
- Giá bán dự kiến
- Ô nhập: Trạng thái ghép hàng
- Ô nhập: VD: Cần ghép thêm dòng HĐ còn sót
- Ô nhập: Chọn sản phẩm…
- Ô nhập: Tên hiển thị trong hệ thống
- Ô nhập: Bắt buộc
- Ô nhập: Mặc định = giá nhập
- Ô nhập: VD: Nhập nhầm số lượng / sai phiếu
- Ô nhập: Tìm kiếm và chọn sản phẩm…
- Ô nhập: Nhập tên sản phẩm…
- Ô nhập: VD: SP00123
- Ô nhập: VD: 50000
- Tất cả
- Đang dùng
- Lưu trữ
**Tooltip / mô tả ngắn (title=):**
- Khôi phục dòng trong chi tiết hoá đơn nếu cần đưa vào phiếu
- Chi tiết
- Bỏ lưu trữ
- Lưu trữ
- Sửa ghép hàng
- Khôi phục dòng này
- Nhà cung cấp đã có trên hệ thống
- NCC chưa có trên hệ thống, sẽ được tạo tự động khi ghép hàng
- Đã khớp tên VAT nội bộ
- Tạo sản phẩm mới
- Hoàn tác / Khôi phục dòng này
- Bỏ dòng này (làm mờ)

### `@/components/ProductVariantsPanel`

**Nhãn lọc / preset / placeholder:**
- Ô nhập: Hoặc dán URL…
- Ô nhập: Nhập tên biến thể
- Ô nhập: Không bắt buộc
- Ô nhập: 10×8×3 cm
- Ô nhập: 150g
**Tooltip / mô tả ngắn (title=):**
- Xoá ảnh
- Bán lại
- Ngừng kinh doanh

### `@/pages/suppliers`

**Tiêu đề trang:** “Không có quyền truy cập”, “Nhà cung cấp”
**Cột bảng:**
- Tên nhà cung cấp
- Liên hệ
- MST
- Trạng thái
**Nhãn lọc / preset / placeholder:**
- Ô nhập: Làng nghề Bát Tràng
- Ô nhập: Nguyễn Văn A
- Ô nhập: ncc@example.com
- Ô nhập: Số nhà, phường, quận...
- Ô nhập: Ghi chú thêm...
- Ô nhập: Tìm tên, MST, SĐT, người liên hệ...
- Đang hợp tác
- Ngừng

## Thao tác người dùng

Hành động chính (nút, menu, mục dialog) — không liệt kê mọi nút icon-only.

### `vat-inbound.tsx`

**Thao tác:**
- feeOverride.onToggleLine(i)} >
- setMarkedMstDialogOpen(true)} > MST lọc ) : null}
- catch ); } }} > Mẫu Excel
- excelInputRef.current?.click()} >
- inputRef.current?.click()} >
- void pullFromTax()} >
- void openStockReceipt(row)} >
- setDetail(row)}>
- setPendingUnarchive(row)} >
- setPendingArchive(row)} >
- setDetail(row)}> Chi tiết
- void openReceiveStock(row)} >
- setCloseShortInvoice(row)} > Đóng thiếu
- setMarkedMstDialogOpen(false)}> Đóng
- void saveMarkedMstList()} >
- initDetailAllocDraft(productId, extras)} > Hoàn tác
- void saveDetailAllocation(productId, rootQty, extras) } > Lưu phân bổ
- setUndoDismissInvoice(detail)} > Hoàn tác chốt ghép thiếu
- openUndoDismissRequest(detail)} > Đề nghị hoàn tác chốt ghép thiếu
- setUndoDismissRequestInvoice(null)} > Huỷ
- void submitUndoDismissRequest()} >
- void submitApproveUndoDismissExcluded(detail)} > Duyệt hoàn tác chốt ghép thiếu
- void submitRejectUndoDismissExcluded(detail)} > Từ chối
- setDismissExcludedInvoice(detail)} > Không ghép các dòng còn lại
- void openStockReceipt(detail)} >
- }> Đóng
- void openReceiveStock(detail)} >
- setCloseShortInvoice(detail)} > Đóng thiếu
- openRollbackRequest(detail)} >
- void submitApproveRollback(detail)} > Duyệt hoàn tác nhập kho
- void submitRejectRollback(detail)} > Từ chối
- void previewStockReceiptPdf(detail)} > Xem phiếu nhập kho tổng
- setConfirmPdf(null)}> Đóng
- } > Xuất PDF
- } > In
- openCreateProductModal(idx)} > Sửa
- setStockDraft((prev) => prev.map((r, i) => i === idx ? : r, ), ) } > Huỷ
- openCreateProductModal(idx)} >
- setStockDraft((prev) => prev.map((r, i) => (i === idx ? : r)) ) } >
- } > Đóng

**Hộp thoại (tiêu đề):**
- Chi tiết hoá đơn{" "} {detail ? [detail.series, detail.invoiceNo].filter(Boolean).join(" ") || "" : ""}
- Phiếu nhập kho tổng
- Ghép hàng từ HĐ VAT
- Tạo sản phẩm mới
- Xem trước dữ liệu nhập
- Hoàn tác chốt ghép thiếu?
- Không ghép các dòng HĐ còn lại?
- Đóng phần thiếu?
- Lưu trữ hoá đơn?
- Bỏ lưu trữ hoá đơn?
- Khôi phục sản phẩm vào phiếu nhập kho

### `@/components/ProductVariantsPanel`

**Thao tác:**
- setRestoreConfirm(row)} >
- setDiscontinueConfirm(row)} >
- removeRow(row)} >
- Thêm biến thể
- Huỷ

**Hộp thoại (tiêu đề):**
- Ngừng kinh doanh?
- Bán lại?

### `@/pages/suppliers`

**Thao tác:**
- Thêm nhà cung cấp
- } > Sửa
- setViewRow(s)} title="Xem" >
- setEditRow(s)} title="Sửa" >

**Hộp thoại (tiêu đề):**
- Thêm nhà cung cấp
- Chỉnh sửa nhà cung cấp
- Chi tiết nhà cung cấp

**Đường dẫn:** `/vat-inbound`

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

**Đọc tiếp:** [Hướng dẫn đọc Map](../../huong-dan-doc/)

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
- `/api/products/${productId}/variants/${v.id}` → [`products`](../../module-api/san-pham-api/)
- `/api/suppliers?active=true`

## Luồng nghiệp vụ (doc)

- [06-hoa-don-dau-vao-tong-quan](../../nghiep-vu/06-hoa-don-dau-vao-tong-quan/)

## Liên kết mã

- Khai báo URL: `artifacts/pos-app/src/App.tsx`
- Menu/layout: `components/layout/app-layout.tsx`
- Phiên đăng nhập: `lib/session-cache.ts`, `lib/use-session-user.ts`
