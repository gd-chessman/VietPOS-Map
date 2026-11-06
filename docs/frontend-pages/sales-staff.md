# Frontend: `sales-staff.tsx`

**Mô tả:** Nhân viên bán hàng (sales staff) gắn POS. (URL /sales-staff, SalesStaffPage, ~470 dòng).

**Source Shop:** `artifacts/pos-app/src/pages/sales-staff.tsx`

**URL (wouter):** `/sales-staff`
**Component:** `SalesStaffPage`
**Độ lớn:** ~470 dòng.

**Route:** `/sales-staff`

Nhân viên bán hàng (sales staff) gắn POS.

## Menu sidebar

- **Nhãn:** Nhân viên bán hàng
- **Điều kiện hiện menu (`show`):** `isAdminOrManager`

## Component con (logic UI chính)

- `@/components/ui/button` → `artifacts/pos-app/src/components/ui/button.tsx`
- `@/components/ui/input` → `artifacts/pos-app/src/components/ui/input.tsx`
- `@/components/ui/textarea` → `artifacts/pos-app/src/components/ui/textarea.tsx`
- `@/components/ui/select` → `artifacts/pos-app/src/components/ui/select.tsx`
- `@/components/ui/table` → `artifacts/pos-app/src/components/ui/table.tsx`
- `@/components/ui/dialog` → `artifacts/pos-app/src/components/ui/dialog.tsx`
- `@/components/ui/form` → `artifacts/pos-app/src/components/ui/form.tsx`
- `@/components/ui/badge` → `artifacts/pos-app/src/components/ui/badge.tsx`
- `@/components/ShiftSessionBar` → `artifacts/pos-app/src/components/ShiftSessionBar.tsx`

## Cách đọc code

- API: tìm `useQuery`, `useMutation`, `apiFetch`, hoặc mục **Chuỗi `/api/...`** bên dưới.
- Quyền: `lib/session-permissions.ts`, biểu thức trong `app-layout.tsx` và file page.
- Offline: các trang POS có thể gọi Dexie qua `@/lib/offline/...`.

## API modules (map sang docs)

- [`api-modules/sales-staff.md`](../api-modules/sales-staff.md) — prefix `/api/sales-staff`
- [`api-modules/sales-staff${listShopParam}.md`](../api-modules/sales-staff${listShopParam}.md) — prefix `/api/sales-staff${listShopParam}`

## JSX component dùng trong file (PascalCase)

- `<Badge />`
- `<BranchSelect />`
- `<Button />`
- `<Dialog />`
- `<DialogContent />`
- `<DialogHeader />`
- `<DialogTitle />`
- `<DialogTrigger />`
- `<Form />`
- `<FormControl />`
- `<FormField />`
- `<FormItem />`
- `<FormLabel />`
- `<FormMessage />`
- `<FormValues />`
- `<Input />`
- `<MapPin />`
- `<Pencil />`
- `<Phone />`
- `<Plus />`
- `<SalesStaffFull />`
- `<Select />`
- `<SelectContent />`
- `<SelectItem />`
- `<SelectTrigger />`
- … 11 component khác

## Dialog / modal (tiêu đề)

- Chỉnh sửa hồ sơ
- Thêm nhân viên bán hàng

## Biểu thức quyền / guard trong file

- `userCanManageChain`

## Import chính (đầu file)

- `import { useState, useEffect } from "react";`
- `import { useQuery, useQueryClient } from "@tanstack/react-query";`
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
- `import { Plus, Pencil, UserCircle, Phone, MapPin } from "lucide-react";`
- `import {`
- `import { cacheActiveSalesStaff } from "@workspace/local-db";`
- `import { useSessionUser } from "@/lib/use-session-user";`
- … 3 import khác

## Module `@/lib/...` được import

- `@/lib/chain-access`
- `@/lib/sales-api`
- `@/lib/use-session-user`

## Component `@/components/...` (đã quét API lớp 1)

- `ui/button` → `artifacts/pos-app/src/components/ui/button.tsx`
- `ui/input` → `artifacts/pos-app/src/components/ui/input.tsx`
- `ui/textarea` → `artifacts/pos-app/src/components/ui/textarea.tsx`
- `ui/select` → `artifacts/pos-app/src/components/ui/select.tsx`
- `ui/table` → `artifacts/pos-app/src/components/ui/table.tsx`
- `ui/dialog` → `artifacts/pos-app/src/components/ui/dialog.tsx`
- `ui/form` → `artifacts/pos-app/src/components/ui/form.tsx`
- `ui/badge` → `artifacts/pos-app/src/components/ui/badge.tsx`
- `ShiftSessionBar` → `artifacts/pos-app/src/components/ShiftSessionBar.tsx`

## Chuỗi `/api/...` (page + component con, 4 mục)

- `/api/sales-staff` → [`api-modules/sales-staff.md`](../api-modules/sales-staff.md)
- `/api/sales-staff${listShopParam}`
- `/api/sales-staff/${editRow.id}` → [`api-modules/sales-staff.md`](../api-modules/sales-staff.md)
- `/api/sales-staff/${id}` → [`api-modules/sales-staff.md`](../api-modules/sales-staff.md)

## File liên quan

- Route khai báo: `artifacts/pos-app/src/App.tsx`
- Layout/menu: `components/layout/app-layout.tsx`
- Session: `lib/session-cache.ts`, `lib/use-session-user.ts`
