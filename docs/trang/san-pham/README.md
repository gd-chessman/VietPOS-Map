# Trang giao diện: `products.tsx`

**Mô tả:** Danh mục sản phẩm, variant, import Excel, giá.

**Mã nguồn Shop:** `artifacts/pos-app/src/pages/products.tsx`

**Đường dẫn URL:** `/products`
**Tên component React:** `Products`
**Quy mô:** ~2689 dòng.

## Thông tin hiển thị

Nội dung người dùng **nhìn thấy** trên màn hình (trích nhãn từ TSX; số liệu động từ API).

### `products.tsx`

**Tiêu đề trang:** “Danh mục sản phẩm”
**Cột bảng:**
- Ảnh
- Mã sản phẩm
- Tên sản phẩm
- Tên tiếng Anh
- Tên VAT
- Loại
- ĐVT
- VAT%
- TNCN%
- Giá bán
- Giá vốn
- Tồn
- Trạng thái
- Mã SP gốc
- Mã biến thể
- Tên biến thể
- Kích thước
- Cân nặng
- Lượt bán
- Tồn kho
**Tab / khu vực:**
- Thông tin
- Biến thể
- Sản phẩm
- Loại sản phẩm
- Sản phẩm ( / )
- Biến thể ( / )
**Nhãn lọc / preset / placeholder:**
- Ô nhập: Hoặc dán URL ảnh...
- Ô nhập: SP001 hoặc 8938505...
- Ô nhập: Tên gọi trong kho...
- Ô nhập: Tên bán hàng
- Ô nhập: English name
- Ô nhập: Tìm theo tên, mã, tên VAT, tên TA...
- Tất cả
**Tooltip / mô tả ngắn (title=):**
- Thông tin cơ bản
- Giá & tồn kho
- Tổng tồn biến thể khác tồn gốc — cần phân bổ lại trong tab Biến thể
- Ngừng kinh doanh
- Kích hoạt lại

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

### `@/components/ProductCategoriesPanel`

**Cột bảng:**
- Tên loại
- Ghi chú
- Trạng thái
**Nhãn lọc / preset / placeholder:**
- Ô nhập: VD: Quà lưu niệm, Đồ trang sức, Gốm sứ…
- Ô nhập: Tuỳ chọn
- Đang dùng
- Ngừng

## Thao tác người dùng

Hành động chính (nút, menu, mục dialog) — không liệt kê mọi nút icon-only.

### `products.tsx`

**Thao tác:**
- fileRef.current?.click()} disabled= >
- catch }} > Tải file mẫu
- fileInputRef.current?.click()} disabled= >
- void handleExportExcel()} disabled= >
- Thêm sản phẩm
- setImportSelecting((v) => !v)} title= aria-label= >
- Huỷ
- setBulkConfirm( ) } > Ngừng kinh doanh ( )
- setBulkConfirm( ) } > Kích hoạt lại ( )
- setSelectedProductIds(new Set())} > Bỏ chọn
- setEditProduct(product)}>
- setStatusConfirm( )}>
- Chọn tất cả
- Chọn tất cả biến thể
- Chọn tất cả trên trang

**Hộp thoại (tiêu đề):**
- Thêm sản phẩm mới
- Chỉnh sửa sản phẩm
- Xem trước dữ liệu nhập

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

### `@/components/ProductCategoriesPanel`

**Thao tác:**
- Thêm loại
- setEditRow(row)} >

**Hộp thoại (tiêu đề):**
- Thêm loại sản phẩm
- Sửa loại sản phẩm

**Đường dẫn:** `/products`

Danh mục SP: grid/table, import Excel, variant, giá, ảnh.

**Đọc tiếp:** [Hướng dẫn đọc Map](../../huong-dan-doc/)

## Quyền (phát hiện trong source)

- Có kiểm tra role **`super_admin`** (hoặc redirect dashboard).

## Tab UI (`TabsTrigger` value)

- `categories`
- `info`
- `products`
- `variants`

## JSX component dùng trong file (PascalCase)

- `<AddForm />`
- `<AddFormInput />`
- `<AlertDialog />`
- `<AlertDialogAction />`
- `<AlertDialogCancel />`
- `<AlertDialogContent />`
- `<AlertDialogDescription />`
- `<AlertDialogFooter />`
- `<AlertDialogHeader />`
- `<AlertDialogTitle />`
- `<AlertTriangle />`
- `<Badge />`
- `<Ban />`
- `<Button />`
- `<CheckCircle2 />`
- `<Checkbox />`
- `<ChevronDown />`
- `<ChevronRight />`
- `<Dialog />`
- `<DialogContent />`
- `<DialogHeader />`
- `<DialogTitle />`
- `<DialogTrigger />`
- `<Download />`
- `<EditForm />`
- … 43 component khác

## Dialog / modal (tiêu đề)

- {bulkConfirm?.action === "discontinue"
                ? `Ngừng kinh doanh ${bulkConfirm?.ids.length ?? 0} sản phẩm?`
                : `Kích hoạt lại ${bulkConfirm?.ids.length ?? 0} sản phẩm?`}
- {statusConfirm?.action === "discontinue" ? "Ngừng kinh doanh?" : "Kích hoạt lại?"}
- Chỉnh sửa sản phẩm
- Thêm sản phẩm mới
- Xem trước dữ liệu nhập

## Import chính (đầu file)

- `import { useState, useRef, useMemo, useEffect, Fragment, type ReactNode } from "react";`
- `import { PaginationBar, DEFAULT_PAGE_SIZE } from "@/components/pagination-bar";`
- `import { useQuery, useQueryClient } from "@tanstack/react-query";`
- `import {`
- `import { cn, formatVND, productImageUrl } from "@/lib/utils";`
- `import { ZoomableThumb } from "@/components/ZoomableThumb";`
- `import { useForm, useWatch, type Control, type Resolver } from "react-hook-form";`
- `import { zodResolver } from "@hookform/resolvers/zod";`
- `import * as z from "zod";`
- `import { Button } from "@/components/ui/button";`
- `import { Input } from "@/components/ui/input";`
- `import { Checkbox } from "@/components/ui/checkbox";`
- `import { Select, SelectContent, SelectItem, SelectTrigger, SelectValue } from "@/components/ui/select";`
- `import { Table, TableBody, TableCell, TableHead, TableHeader, TableRow } from "@/components/ui/table";`
- `import { Dialog, DialogContent, DialogHeader, DialogTitle, DialogTrigger, dialogIgnoreFloatingDismiss } from "@/components/ui/dialog";`
- `import {`
- `import { Form, FormControl, FormField, FormItem, FormLabel, FormMessage } from "@/components/ui/form";`
- `import { Badge } from "@/components/ui/badge";`
- … 12 import khác

## Module `@/lib/...` được import

- `@/lib/api-auth-fetch`
- `@/lib/offline`
- `@/lib/product-excel-export`
- `@/lib/product-excel-import`
- `@/lib/session-cache`
- `@/lib/use-session-user`
- `@/lib/utils`
- `@/lib/variant-stock`
- `@/lib/vat`

## Chuỗi `/api/...` (page + component con, 7 mục)

- `/api/me`
- `/api/products/${id}` → [`products`](../../module-api/san-pham-api/)
- `/api/products/import` → [`products`](../../module-api/san-pham-api/)
- `/api/products/variant-sales` → [`products`](../../module-api/san-pham-api/)
- `/api/products?includeDiscontinued=true`
- `/api/suppliers?active=true`
- `/api/suppliers?limit=300&page=${page}`

## Luồng nghiệp vụ (doc)

- [03-san-pham-va-ton](../../nghiep-vu/03-san-pham-va-ton/)

## Liên kết mã

- Khai báo URL: `artifacts/pos-app/src/App.tsx`
- Menu/layout: `components/layout/app-layout.tsx`
- Phiên đăng nhập: `lib/session-cache.ts`, `lib/use-session-user.ts`
