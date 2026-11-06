# Trang giao diện: `sales-staff.tsx`

**Mô tả:** Nhân viên bán hàng (sales staff) gắn POS. (URL /sales-staff, SalesStaffPage, ~470 dòng).

**Mã nguồn Shop:** `artifacts/pos-app/src/pages/sales-staff.tsx`

**Đường dẫn URL:** `/sales-staff`
**Tên component React:** `SalesStaffPage`
**Quy mô:** ~470 dòng.

## Thông tin hiển thị

Nội dung người dùng **nhìn thấy** trên màn hình (trích nhãn từ TSX; số liệu động từ API).

### `sales-staff.tsx`

**Tiêu đề trang:** “Nhân viên bán hàng”
**Cột bảng:**
- Họ tên
- Chi nhánh
- Liên hệ
- Ngày vào / nghỉ
- Trạng thái
**Nhãn lọc / preset / placeholder:**
- Ô nhập: Nguyễn Văn A
- Ô nhập: Số nhà, phường, quận...
- Ô nhập: Lý do nghỉ việc, ghi chú khác...
- Đang làm
- Tạm nghỉ
- Đã nghỉ

## Thao tác người dùng

Hành động chính (nút, menu, mục dialog) — không liệt kê mọi nút icon-only.

### `sales-staff.tsx`

**Thao tác:**
- Thêm NV bán
- setEditRow(s)}>

**Hộp thoại (tiêu đề):**
- Thêm nhân viên bán hàng
- Chỉnh sửa hồ sơ

**Đường dẫn:** `/sales-staff`

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

## Module API liên quan (trong Map)

- [`sales-staff`](../../module-api/nhan-vien-ban-api/) — nhóm `/api/sales-staff`
- [`sales-staff${listShopParam}`](../../module-api/sales-staff${listShopParam}/) — nhóm `/api/sales-staff${listShopParam}`

**Đọc tiếp:** [Hướng dẫn đọc Map](../../huong-dan-doc/)

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

- `/api/sales-staff` → [`sales-staff`](../../module-api/nhan-vien-ban-api/)
- `/api/sales-staff${listShopParam}`
- `/api/sales-staff/${editRow.id}` → [`sales-staff`](../../module-api/nhan-vien-ban-api/)
- `/api/sales-staff/${id}` → [`sales-staff`](../../module-api/nhan-vien-ban-api/)

## Liên kết mã

- Khai báo URL: `artifacts/pos-app/src/App.tsx`
- Menu/layout: `components/layout/app-layout.tsx`
- Phiên đăng nhập: `lib/session-cache.ts`, `lib/use-session-user.ts`
