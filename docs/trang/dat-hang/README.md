# Trang giao diện: `purchase-orders.tsx`

**Mô tả:** Phiếu đặt mua (PO) và trạng thái nhận hàng. (URL /purchase-orders, PurchaseOrdersPage, ~2359 dòng).

**Mã nguồn Shop:** `artifacts/pos-app/src/pages/purchase-orders.tsx`

**Đường dẫn URL:** `/purchase-orders`
**Tên component React:** `PurchaseOrdersPage`
**Quy mô:** ~2359 dòng.

## Thông tin hiển thị

Nội dung người dùng **nhìn thấy** trên màn hình (trích nhãn từ TSX; số liệu động từ API).

### `purchase-orders.tsx`

**Tiêu đề trang:** “Không có quyền truy cập”, “Đặt hàng”
**Thẻ / chỉ số (CardTitle):**
- Chưa gán nhà cung cấp
**Cột bảng:**
- Ảnh
- Nhà cung cấp
- Giá nhập
- Tồn kho
- Số lượng đặt
- Mã phiếu
- Trạng thái
- Số mặt hàng
- Tổng số lượng
- Người lập
- Ngày tạo
- Thao tác
- Sản phẩm
- Mã sản phẩm
- Tồn
- SL đặt
- Giá bán
**Tab / khu vực:**
- Tạo phiếu
- Danh sách phiếu )}
**Nhãn lọc / preset / placeholder:**
- Ô nhập: Tìm tên, mã sản phẩm, nhà cung cấp…
- Ô nhập: Nhà cung cấp
- Ô nhập: Tồn kho
- Ô nhập: Ghi chú chung trên phiếu đặt hàng (tuỳ chọn)
- Ô nhập: Tìm mã phiếu, nhà cung cấp, người lập…
- Ô nhập: Ghi chú sản phẩm…
- Ô nhập: Nhập lý do huỷ phiếu…
- Chờ gửi
- Đã gửi nhà cung cấp
- Nhận còn thiếu
- Đã nhận (thiếu)
- Đã nhận (đủ)
- Đã huỷ
- Tất cả
- Đã gửi

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

### `purchase-orders.tsx`

**Thao tác:**
- Gợi ý SL (bán 30 ngày)
- void openDetail(o.id)}> Chi tiết
- void runStatusAction(o.id, "send")} > Đã gửi
- ); setCancelReason(""); }} > Huỷ
- setPreviewOpen(false)}> Đóng
- void saveEditingOrder()}>
- void printActivePreview()} >
- void downloadAllPreviewFiles()} > Xuất tất cả ( )
- setDetailOpen(false)}> Đóng
- ); setCancelReason(""); }} > Huỷ phiếu
- void openUpdatePdf(detail)} > Cập nhật
- void previewSavedOrder(detail)} > Xem phiếu đặt hàng
- } > Đóng
- void confirmCancelOrder()} >
- Chọn tất cả trên trang này

**Hộp thoại (tiêu đề):**
- Chi tiết phiếu {detail?.code ?? ""}
- Huỷ phiếu đặt hàng?

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

**Đường dẫn:** `/purchase-orders`

Phiếu đặt mua (PO) và trạng thái nhận hàng.

## Menu sidebar

- **Nhãn:** Đặt hàng
- **Điều kiện hiện menu (`show`):** `(isAdminOrManager || isWarehouseKeeper) && isHubShop`

## Nghiệp vụ (doc)

- `nghiep-vu/04-phieu-nhap-xuat-chuyen-kho/README.md`

## Component con (logic UI chính)

- `@/components/ui/button` → `artifacts/pos-app/src/components/ui/button.tsx`
- `@/components/ui/input` → `artifacts/pos-app/src/components/ui/input.tsx`
- `@/components/ui/badge` → `artifacts/pos-app/src/components/ui/badge.tsx`
- `@/components/ui/checkbox` → `artifacts/pos-app/src/components/ui/checkbox.tsx`
- `@/components/ui/select` → `artifacts/pos-app/src/components/ui/select.tsx`
- `@/components/ui/card` → `artifacts/pos-app/src/components/ui/card.tsx`
- `@/components/ui/table` → `artifacts/pos-app/src/components/ui/table.tsx`
- `@/components/ui/textarea` → `artifacts/pos-app/src/components/ui/textarea.tsx`
- `@/components/ui/dialog` → `artifacts/pos-app/src/components/ui/dialog.tsx`
- `@/components/ui/tabs` → `artifacts/pos-app/src/components/ui/tabs.tsx`
- `@/components/pagination-bar` → `artifacts/pos-app/src/components/pagination-bar.tsx`
- `@/components/ZoomableThumb` → `artifacts/pos-app/src/components/ZoomableThumb.tsx`
- `@/components/PdfPreview` → `artifacts/pos-app/src/components/PdfPreview.tsx`
- `@/components/PurchaseOrderPrint` → `artifacts/pos-app/src/components/PurchaseOrderPrint.tsx`
- `@/components/pages/suppliers` → `artifacts/pos-app/src/pages/suppliers.tsx`

## Cách đọc code

- API: tìm `useQuery`, `useMutation`, `apiFetch`, hoặc mục **Chuỗi `/api/...`** bên dưới.
- Quyền: `lib/session-permissions.ts`, biểu thức trong `app-layout.tsx` và file page.
- Offline: các trang POS có thể gọi Dexie qua `@/lib/offline/...`.

## Module API liên quan (trong Map)

- [`organizations`](../../module-api/organizations/) — nhóm `/api/organizations`
- [`purchase-orders`](../../module-api/dat-hang/) — nhóm `/api/purchase-orders`
- [`purchase-orders?status=${listStatus}`](../../module-api/purchase-orders?status=${listStatus}/) — nhóm `/api/purchase-orders?status=${listStatus}`
- [`suppliers?active=true`](../../module-api/suppliers?active=true/) — nhóm `/api/suppliers?active=true`

**Đọc tiếp:** [Hướng dẫn đọc Map](../../huong-dan-doc/)

## Quyền (phát hiện trong source)

- Có kiểm tra role **`super_admin`** (hoặc redirect dashboard).

## Tab UI (`TabsTrigger` value)

- `create`
- `list`

## JSX component dùng trong file (PascalCase)

- `<AlertTriangle />`
- `<Badge />`
- `<Button />`
- `<Card />`
- `<CardContent />`
- `<CardHeader />`
- `<CardTitle />`
- `<Checkbox />`
- `<ChevronDown />`
- `<ChevronRight />`
- `<ClipboardList />`
- `<CreatePayload />`
- `<Dialog />`
- `<DialogContent />`
- `<DialogDescription />`
- `<DialogFooter />`
- `<DialogHeader />`
- `<DialogTitle />`
- `<Eye />`
- `<FileDown />`
- `<History />`
- `<Input />`
- `<Layers />`
- `<POPrintData />`
- `<Package />`
- … 40 component khác

## Dialog / modal (tiêu đề)

- Chi tiết phiếu {detail?.code ?? ""}
- {editingOrder
                ? `Cập nhật phiếu ${editingOrder.code ?? `#${editingOrder.id}`}`
                : previewKind === "confirm"
                  ? `Xem phiếu nhập kho tổng${activePrintData?.code ? ` · ${activePrintData.code}` : ""}`
                  : `Xem phiếu đặt hàng (${previewFiles.length} nhà cung cấp)`}
- Huỷ phiếu đặt hàng?

## Import chính (đầu file)

- `import { Fragment, useEffect, useMemo, useRef, useState } from "react";`
- `import { useQuery, useQueryClient } from "@tanstack/react-query";`
- `import { format } from "date-fns";`
- `import { vi } from "date-fns/locale";`
- `import { Button } from "@/components/ui/button";`
- `import { Input } from "@/components/ui/input";`
- `import { Badge } from "@/components/ui/badge";`
- `import { Checkbox } from "@/components/ui/checkbox";`
- `import { Select, SelectContent, SelectItem, SelectTrigger, SelectValue } from "@/components/ui/select";`
- `import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";`
- `import { Table, TableBody, TableCell, TableHead, TableHeader, TableRow } from "@/components/ui/table";`
- `import { Textarea } from "@/components/ui/textarea";`
- `import { Dialog, DialogContent, DialogDescription, DialogFooter, DialogHeader, DialogTitle } from "@/components/ui/dialog";`
- `import { Tabs, TabsContent, TabsList, TabsTrigger } from "@/components/ui/tabs";`
- `import { PaginationBar, DEFAULT_PAGE_SIZE } from "@/components/pagination-bar";`
- `import { useToast } from "@/hooks/use-toast";`
- `import { formatVND, productImageUrl, cn } from "@/lib/utils";`
- `import { ZoomableThumb } from "@/components/ZoomableThumb";`
- … 10 import khác

## Module `@/lib/...` được import

- `@/lib/offline`
- `@/lib/print-pdf`
- `@/lib/purchase-order-audit`
- `@/lib/sales-api`
- `@/lib/session-cache`
- `@/lib/use-session-user`
- `@/lib/utils`

## Component `@/components/...` (đã quét API lớp 1)

- `ui/button` → `artifacts/pos-app/src/components/ui/button.tsx`
- `ui/input` → `artifacts/pos-app/src/components/ui/input.tsx`
- `ui/badge` → `artifacts/pos-app/src/components/ui/badge.tsx`
- `ui/checkbox` → `artifacts/pos-app/src/components/ui/checkbox.tsx`
- `ui/select` → `artifacts/pos-app/src/components/ui/select.tsx`
- `ui/card` → `artifacts/pos-app/src/components/ui/card.tsx`
- `ui/table` → `artifacts/pos-app/src/components/ui/table.tsx`
- `ui/textarea` → `artifacts/pos-app/src/components/ui/textarea.tsx`
- `ui/dialog` → `artifacts/pos-app/src/components/ui/dialog.tsx`
- `ui/tabs` → `artifacts/pos-app/src/components/ui/tabs.tsx`
- `pagination-bar` → `artifacts/pos-app/src/components/pagination-bar.tsx`
- `ZoomableThumb` → `artifacts/pos-app/src/components/ZoomableThumb.tsx`
- `PdfPreview` → `artifacts/pos-app/src/components/PdfPreview.tsx`
- `PurchaseOrderPrint` → `artifacts/pos-app/src/components/PurchaseOrderPrint.tsx`
- `pages/suppliers` → `artifacts/pos-app/src/pages/suppliers.tsx`

## Chuỗi `/api/...` (page + component con, 8 mục)

- `/api/organizations/current`
- `/api/purchase-orders` → [`purchase-orders`](../../module-api/dat-hang/)
- `/api/purchase-orders/${editingOrder.id}` → [`purchase-orders`](../../module-api/dat-hang/)
- `/api/purchase-orders/${id}` → [`purchase-orders`](../../module-api/dat-hang/)
- `/api/purchase-orders/${id}/${action}` → [`purchase-orders`](../../module-api/dat-hang/)
- `/api/purchase-orders/sales-hints?days=30` → [`purchase-orders`](../../module-api/dat-hang/)
- `/api/purchase-orders?status=${listStatus}`
- `/api/suppliers?active=true`

## Luồng nghiệp vụ (doc)

- [04-phieu-nhap-xuat-chuyen-kho](../../nghiep-vu/04-phieu-nhap-xuat-chuyen-kho/)

## Liên kết mã

- Khai báo URL: `artifacts/pos-app/src/App.tsx`
- Menu/layout: `components/layout/app-layout.tsx`
- Phiên đăng nhập: `lib/session-cache.ts`, `lib/use-session-user.ts`
