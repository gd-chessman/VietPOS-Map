# Trang giao diện: `staff.tsx`

**Mô tả:** Quản lý tài khoản nhân viên (admin).

**Mã nguồn Shop:** `artifacts/pos-app/src/pages/staff.tsx`

**Đường dẫn URL:** `/staff`
**Tên component React:** `Staff`
**Quy mô:** ~863 dòng.

## Thông tin hiển thị

Nội dung người dùng **nhìn thấy** trên màn hình (trích nhãn từ TSX; số liệu động từ API).

### `staff.tsx`

**Tiêu đề trang:** “Quản lý nhân viên”
**Cột bảng:**
- Nhân viên
- Email
- Chi nhánh
- Vai trò
- Mã PIN
- Trạng thái
**Nhãn lọc / preset / placeholder:**
- Ô nhập: Nguyễn Văn A
- Quản trị viên
- Quản lý
- Kế toán
- Thủ kho
- Nhân viên
- Đang làm
- Tạm nghỉ
- Đã nghỉ
- Quản trị hệ thống
- Có
- Chưa
**Tooltip / mô tả ngắn (title=):**
- Đặt mã PIN mới
- Mã PIN đăng nhập (4 số)
- Đánh dấu đã nghỉ

## Thao tác người dùng

Hành động chính (nút, menu, mục dialog) — không liệt kê mọi nút icon-only.

### `staff.tsx`

**Thao tác:**
- Thêm nhân viên
- setConfirmUserSetsRequest(row)} > Để họ tự đặt
- setAdminPinForRequest(row)} > Đặt PIN giúp
- setConfirmDismissRequest(row)} > Xóa yêu cầu
- setEditStaff(s)} disabled= title= >
- onResign(s.id)} title="Đánh dấu đã nghỉ">
- Huỷ

**Hộp thoại (tiêu đề):**
- Thêm nhân viên mới
- Xóa yêu cầu quên PIN?
- Cho tự đặt mã PIN?
- Chỉnh sửa nhân viên

**Đường dẫn:** `/staff`

Quản lý tài khoản nhân viên (admin).

## Menu sidebar

- **Nhãn:** Nhân viên
- **Điều kiện hiện menu (`show`):** `isAdminOrManager`

## Component con (logic UI chính)

- `@/components/ui/button` → `artifacts/pos-app/src/components/ui/button.tsx`
- `@/components/ui/input` → `artifacts/pos-app/src/components/ui/input.tsx`
- `@/components/ui/select` → `artifacts/pos-app/src/components/ui/select.tsx`
- `@/components/ui/table` → `artifacts/pos-app/src/components/ui/table.tsx`
- `@/components/ui/dialog` → `artifacts/pos-app/src/components/ui/dialog.tsx`
- `@/components/ui/alert-dialog` → `artifacts/pos-app/src/components/ui/alert-dialog.tsx`
- `@/components/ui/form` → `artifacts/pos-app/src/components/ui/form.tsx`
- `@/components/ui/badge` → `artifacts/pos-app/src/components/ui/badge.tsx`
- `@/components/PinCodeDialog` → `artifacts/pos-app/src/components/PinCodeDialog.tsx`

## Cách đọc code

- API: tìm `useQuery`, `useMutation`, `apiFetch`, hoặc mục **Chuỗi `/api/...`** bên dưới.
- Quyền: `lib/session-permissions.ts`, biểu thức trong `app-layout.tsx` và file page.
- Offline: các trang POS có thể gọi Dexie qua `@/lib/offline/...`.

**Đọc tiếp:** [Hướng dẫn đọc Map](../../huong-dan-doc/)

## Quyền (phát hiện trong source)

- Có kiểm tra role **`super_admin`** (hoặc redirect dashboard).

## JSX component dùng trong file (PascalCase)

- `<AlertDialog />`
- `<AlertDialogAction />`
- `<AlertDialogCancel />`
- `<AlertDialogContent />`
- `<AlertDialogDescription />`
- `<AlertDialogFooter />`
- `<AlertDialogHeader />`
- `<AlertDialogTitle />`
- `<Badge />`
- `<BranchSelect />`
- `<Button />`
- `<CreateForm />`
- `<CreateValues />`
- `<Dialog />`
- `<DialogContent />`
- `<DialogHeader />`
- `<DialogTitle />`
- `<DialogTrigger />`
- `<EditForm />`
- `<EditValues />`
- `<Form />`
- `<FormControl />`
- `<FormField />`
- `<FormItem />`
- `<FormLabel />`
- … 27 component khác

## Dialog / modal (tiêu đề)

- Cho tự đặt mã PIN?
- Chỉnh sửa nhân viên
- Thêm nhân viên mới
- Xóa yêu cầu quên PIN?

## Import chính (đầu file)

- `import { useState } from "react";`
- `import { useQuery } from "@tanstack/react-query";`
- `import { useListStaff, useCreateStaff, useUpdateStaff, useDeleteStaff, useListShops, getListShopsQueryKey } from "@workspace/api-client-react";`
- `import type { StaffUser, StaffUserStatus, UpdateStaffBodyStatus } from "@workspace/api-client-react";`
- `import { useQueryClient } from "@tanstack/react-query";`
- `import { useForm } from "react-hook-form";`
- `import { zodResolver } from "@hookform/resolvers/zod";`
- `import * as z from "zod";`
- `import { Button } from "@/components/ui/button";`
- `import { Input } from "@/components/ui/input";`
- `import { Select, SelectContent, SelectItem, SelectTrigger, SelectValue } from "@/components/ui/select";`
- `import { Table, TableBody, TableCell, TableHead, TableHeader, TableRow } from "@/components/ui/table";`
- `import { Dialog, DialogContent, DialogHeader, DialogTitle, DialogTrigger } from "@/components/ui/dialog";`
- `import {`
- `import { Form, FormControl, FormField, FormItem, FormLabel, FormMessage } from "@/components/ui/form";`
- `import { Badge } from "@/components/ui/badge";`
- `import { useToast } from "@/hooks/use-toast";`
- `import { useSessionUser } from "@/lib/use-session-user";`
- … 4 import khác

## Module `@/lib/...` được import

- `@/lib/pin-reset-api`
- `@/lib/use-session-user`
- `@/lib/user-pin`

## Component `@/components/...` (đã quét API lớp 1)

- `ui/button` → `artifacts/pos-app/src/components/ui/button.tsx`
- `ui/input` → `artifacts/pos-app/src/components/ui/input.tsx`
- `ui/select` → `artifacts/pos-app/src/components/ui/select.tsx`
- `ui/table` → `artifacts/pos-app/src/components/ui/table.tsx`
- `ui/dialog` → `artifacts/pos-app/src/components/ui/dialog.tsx`
- `ui/alert-dialog` → `artifacts/pos-app/src/components/ui/alert-dialog.tsx`
- `ui/form` → `artifacts/pos-app/src/components/ui/form.tsx`
- `ui/badge` → `artifacts/pos-app/src/components/ui/badge.tsx`
- `PinCodeDialog` → `artifacts/pos-app/src/components/PinCodeDialog.tsx`

## Liên kết mã

- Khai báo URL: `artifacts/pos-app/src/App.tsx`
- Menu/layout: `components/layout/app-layout.tsx`
- Phiên đăng nhập: `lib/session-cache.ts`, `lib/use-session-user.ts`
