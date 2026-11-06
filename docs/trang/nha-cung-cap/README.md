# Trang giao diện: `suppliers.tsx`

**Mô tả:** Danh mục nhà cung cấp. (URL /suppliers, SuppliersPage, ~593 dòng).

**Mã nguồn Shop:** `artifacts/pos-app/src/pages/suppliers.tsx`

**Đường dẫn URL:** `/suppliers`
**Tên component React:** `SuppliersPage`
**Quy mô:** ~593 dòng.

**Đường dẫn:** `/suppliers`

Danh mục nhà cung cấp.

## Menu sidebar

- **Nhãn:** Nhà cung cấp
- **Điều kiện hiện menu (`show`):** `isAdminOrManager && isHubShop`

## Component con (logic UI chính)

- `@/components/pagination-bar` → `artifacts/pos-app/src/components/pagination-bar.tsx`
- `@/components/ui/button` → `artifacts/pos-app/src/components/ui/button.tsx`
- `@/components/ui/input` → `artifacts/pos-app/src/components/ui/input.tsx`
- `@/components/ui/textarea` → `artifacts/pos-app/src/components/ui/textarea.tsx`
- `@/components/ui/select` → `artifacts/pos-app/src/components/ui/select.tsx`
- `@/components/ui/table` → `artifacts/pos-app/src/components/ui/table.tsx`
- `@/components/ui/dialog` → `artifacts/pos-app/src/components/ui/dialog.tsx`
- `@/components/ui/form` → `artifacts/pos-app/src/components/ui/form.tsx`
- `@/components/ui/badge` → `artifacts/pos-app/src/components/ui/badge.tsx`

## Cách đọc code

- API: tìm `useQuery`, `useMutation`, `apiFetch`, hoặc mục **Chuỗi `/api/...`** bên dưới.
- Quyền: `lib/session-permissions.ts`, biểu thức trong `app-layout.tsx` và file page.
- Offline: các trang POS có thể gọi Dexie qua `@/lib/offline/...`.

## Module API liên quan (trong Map)

- [`suppliers`](../../module-api/nha-cung-cap-api/) — nhóm `/api/suppliers`
- [`suppliers?${params.toString()}`](../../module-api/suppliers?${params.toString()}/) — nhóm `/api/suppliers?${params.toString()}`

**Đọc tiếp:** [Hướng dẫn đọc Map](../../huong-dan-doc/)

## Quyền (phát hiện trong source)

- Có kiểm tra role **`super_admin`** (hoặc redirect dashboard).

## React Query keys

- `["suppliers"]`

## JSX component dùng trong file (PascalCase)

- `<Badge />`
- `<Building2 />`
- `<Button />`
- `<Dialog />`
- `<DialogContent />`
- `<DialogHeader />`
- `<DialogTitle />`
- `<DialogTrigger />`
- `<Eye />`
- `<Form />`
- `<FormControl />`
- `<FormField />`
- `<FormItem />`
- `<FormLabel />`
- `<FormMessage />`
- `<FormValues />`
- `<Input />`
- `<Mail />`
- `<MapPin />`
- `<PaginationBar />`
- `<Pencil />`
- `<Phone />`
- `<Plus />`
- `<Search />`
- `<Select />`
- … 14 component khác

## Dialog / modal (tiêu đề)

- Chi tiết nhà cung cấp
- Chỉnh sửa nhà cung cấp
- Thêm nhà cung cấp

## Import chính (đầu file)

- `import { useState } from "react";`
- `import { useQuery, useQueryClient } from "@tanstack/react-query";`
- `import { PaginationBar, DEFAULT_PAGE_SIZE } from "@/components/pagination-bar";`
- `import { useForm } from "react-hook-form";`
- `import { zodResolver } from "@hookform/resolvers/zod";`
- `import * as z from "zod";`
- `import { Button } from "@/components/ui/button";`
- `import { Input } from "@/components/ui/input";`
- `import { Textarea } from "@/components/ui/textarea";`
- `import { Select, SelectContent, SelectItem, SelectTrigger, SelectValue } from "@/components/ui/select";`
- `import { Table, TableBody, TableCell, TableHead, TableHeader, TableRow } from "@/components/ui/table";`
- `import { Dialog, DialogContent, DialogHeader, DialogTitle, DialogTrigger } from "@/components/ui/dialog";`
- `import { Form, FormControl, FormField, FormItem, FormLabel, FormMessage } from "@/components/ui/form";`
- `import { Badge } from "@/components/ui/badge";`
- `import { useToast } from "@/hooks/use-toast";`
- `import { Plus, Pencil, Eye, Building2, Phone, MapPin, Mail, Search } from "lucide-react";`
- `import { apiGet, apiPost, apiPatch } from "@/lib/sales-api";`
- `import { useSessionUser } from "@/lib/use-session-user";`

## Module `@/lib/...` được import

- `@/lib/sales-api`
- `@/lib/use-session-user`

## Component `@/components/...` (đã quét API lớp 1)

- `pagination-bar` → `artifacts/pos-app/src/components/pagination-bar.tsx`
- `ui/button` → `artifacts/pos-app/src/components/ui/button.tsx`
- `ui/input` → `artifacts/pos-app/src/components/ui/input.tsx`
- `ui/textarea` → `artifacts/pos-app/src/components/ui/textarea.tsx`
- `ui/select` → `artifacts/pos-app/src/components/ui/select.tsx`
- `ui/table` → `artifacts/pos-app/src/components/ui/table.tsx`
- `ui/dialog` → `artifacts/pos-app/src/components/ui/dialog.tsx`
- `ui/form` → `artifacts/pos-app/src/components/ui/form.tsx`
- `ui/badge` → `artifacts/pos-app/src/components/ui/badge.tsx`

## Chuỗi `/api/...` (page + component con, 4 mục)

- `/api/suppliers` → [`suppliers`](../../module-api/nha-cung-cap-api/)
- `/api/suppliers/${editRow.id}` → [`suppliers`](../../module-api/nha-cung-cap-api/)
- `/api/suppliers/${id}` → [`suppliers`](../../module-api/nha-cung-cap-api/)
- `/api/suppliers?${params.toString()}`

## Liên kết mã

- Khai báo URL: `artifacts/pos-app/src/App.tsx`
- Menu/layout: `components/layout/app-layout.tsx`
- Phiên đăng nhập: `lib/session-cache.ts`, `lib/use-session-user.ts`
