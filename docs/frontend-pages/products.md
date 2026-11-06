# Frontend: `products.tsx`

**Mô tả:** Danh mục sản phẩm, variant, import Excel, giá. (URL /products, Products, ~2689 dòng).

**Source Shop:** `artifacts/pos-app/src/pages/products.tsx`

**URL (wouter):** `/products`
**Component:** `Products`
**Độ lớn:** ~2689 dòng.

**Route:** `/products`

Danh mục SP: grid/table, import Excel, variant, giá, ảnh.

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
- `/api/products/${id}` → [`api-modules/products.md`](../api-modules/products.md)
- `/api/products/import` → [`api-modules/products.md`](../api-modules/products.md)
- `/api/products/variant-sales` → [`api-modules/products.md`](../api-modules/products.md)
- `/api/products?includeDiscontinued=true`
- `/api/suppliers?active=true`
- `/api/suppliers?limit=300&page=${page}`

## Luồng nghiệp vụ (doc)

- `nghiep-vu/03-san-pham-va-ton.md`

## File liên quan

- Route khai báo: `artifacts/pos-app/src/App.tsx`
- Layout/menu: `components/layout/app-layout.tsx`
- Session: `lib/session-cache.ts`, `lib/use-session-user.ts`
