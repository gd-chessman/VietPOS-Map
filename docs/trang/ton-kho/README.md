# Trang giao diện: `inventory.tsx`

**Mô tả:** Tồn kho shop, điều chỉnh số lượng, cảnh báo sắp hết. (URL /inventory, Inventory, ~1066 dòng).

**Mã nguồn Shop:** `artifacts/pos-app/src/pages/inventory.tsx`

**Đường dẫn URL:** `/inventory`
**Tên component React:** `Inventory`
**Quy mô:** ~1066 dòng.

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
