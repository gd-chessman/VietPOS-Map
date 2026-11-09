# Trang giao diện: `inventory.tsx`

**Mô tả:** Tồn kho shop, điều chỉnh số lượng, cảnh báo sắp hết.

**Mã nguồn Shop:** `artifacts/pos-app/src/pages/inventory.tsx`

**Đường dẫn URL:** `/inventory`
**Tên component React:** `Inventory`
**Quy mô:** ~1066 dòng.

## Thông tin hiển thị

Nội dung người dùng **nhìn thấy** trên màn hình (trích nhãn từ TSX; số liệu động từ API).

### `inventory.tsx`

**Tiêu đề trang:** “Quản lý tồn kho”
**Thẻ / chỉ số (CardTitle):**
- Giá trị tồn (giá bán) — {activeShopName}
- Giá trị tồn (giá vốn) — {activeShopName}
**Cột bảng:**
- Ảnh
- Mã sản phẩm
- Tên sản phẩm
- Tồn kho
- Giá bán
- Thành tiền (bán)
- Tồn
**Nhãn lọc / preset / placeholder:**
- Ô nhập: Tìm kiếm sản phẩm...
- Ô nhập: Mức tồn kho
**Tooltip / mô tả ngắn (title=):**
- Sửa tồn

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

### `@/pages/stock-requests`

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

### `inventory.tsx`

**Thao tác:**
- Tạo phiếu nhập ( )
- setStockEditItem( ) } >
- initAllocDraft(item)} > Hoàn tác
- void saveAllocation(item)} > Lưu phân bổ
- Chọn tất cả
- Sửa tồn

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

### `@/pages/stock-requests`

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

**Đường dẫn:** `/inventory`

Tồn kho shop: số lượng, tạo phiếu nhập từ SP sắp hết (thủ kho).

**Đọc tiếp:** [Hướng dẫn đọc Map](../../huong-dan-doc/)

## Quyền (phát hiện trong source)

- Có kiểm tra role **`super_admin`** (hoặc redirect dashboard).

## JSX component dùng trong file (PascalCase)

- `<AlertTriangle />`
- `<ArrowDownToLine />`
- `<Badge />`
- `<Building2 />`
- `<Button />`
- `<Card />`
- `<CardContent />`
- `<CardHeader />`
- `<CardTitle />`
- `<Checkbox />`
- `<ChevronDown />`
- `<ChevronRight />`
- `<CreateStockRequestDialog />`
- `<Eye />`
- `<Input />`
- `<InventoryStockEditDialog />`
- `<InventoryStockEditTarget />`
- `<Layers />`
- `<Loader2 />`
- `<Package />`
- `<PaginationBar />`
- `<Pencil />`
- `<Record />`
- `<Search />`
- `<Select />`
- … 14 component khác

## Import chính (đầu file)

- `import { useMemo, useState, Fragment } from "react";`
- `import { PaginationBar, DEFAULT_PAGE_SIZE } from "@/components/pagination-bar";`
- `import { useQuery, useQueryClient } from "@tanstack/react-query";`
- `import {`
- `import { Button } from "@/components/ui/button";`
- `import { Input } from "@/components/ui/input";`
- `import { Badge } from "@/components/ui/badge";`
- `import { Checkbox } from "@/components/ui/checkbox";`
- `import { Select, SelectContent, SelectItem, SelectTrigger, SelectValue } from "@/components/ui/select";`
- `import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";`
- `import { Table, TableBody, TableCell, TableHead, TableHeader, TableRow } from "@/components/ui/table";`
- `import { formatVND, productImageUrl, cn } from "@/lib/utils";`
- `import { ZoomableThumb } from "@/components/ZoomableThumb";`
- `import { Search, AlertTriangle, Building2, Eye, ArrowDownToLine, Package, Layers, ChevronDown, ChevronRight, Loader2, Pencil } from "lucide-react";`
- `import {`
- `import {`
- `import { usePosProducts, usePosProductsPaged, useOfflineStatus } from "@/lib/offline";`
- `import { withApiAuthHeaders } from "@/lib/api-auth-fetch";`
- … 6 import khác

## Module `@/lib/...` được import

- `@/lib/api-auth-fetch`
- `@/lib/offline`
- `@/lib/sales-api`
- `@/lib/session-cache`
- `@/lib/use-session-user`
- `@/lib/utils`
- `@/lib/variant-stock`

## Chuỗi `/api/...` (page + component con, 3 mục)

- `/api/me`
- `/api/products/${item.productId}/variants/${v.id}` → [`products`](../../module-api/san-pham-api/)
- `/api/shops` → [`shops`](../../module-api/cua-hang/)

## Luồng nghiệp vụ (doc)

- [03-san-pham-va-ton](../../nghiep-vu/03-san-pham-va-ton/)

## Liên kết mã

- Khai báo URL: `artifacts/pos-app/src/App.tsx`
- Menu/layout: `components/layout/app-layout.tsx`
- Phiên đăng nhập: `lib/session-cache.ts`, `lib/use-session-user.ts`
