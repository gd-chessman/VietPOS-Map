# Trang giao diện: `notification-settings.tsx`

**Mô tả:** Cấu hình thông báo platform/org.

**Mã nguồn Shop:** `artifacts/pos-app/src/pages/notification-settings.tsx`

**Đường dẫn URL:** `/notification-settings`
**Tên component React:** `NotificationSettingsPage`
**Quy mô:** ~487 dòng.

## Thông tin hiển thị

Nội dung người dùng **nhìn thấy** trên màn hình (trích nhãn từ TSX; số liệu động từ API).

### `notification-settings.tsx`

**Tiêu đề trang:** “Thông báo hệ thống”
**Thẻ / chỉ số (CardTitle):**
- Tổng quan
**Nhãn lọc / preset / placeholder:**
- Quản trị hệ thống
- Quản trị tổng
- Quản trị chi nhánh
- Quản lý tổng
- Quản lý chi nhánh
- Kế toán tại cửa hàng
- Thủ kho tại cửa hàng

## Thao tác người dùng

Hành động chính (nút, menu, mục dialog) — không liệt kê mọi nút icon-only.

### `notification-settings.tsx`

**Thao tác:**
- setOpenRolesType(item.type)} > Vai trò nhận

**Hộp thoại (tiêu đề):**
- Vai trò nhận thông báo

**Đường dẫn:** `/notification-settings`

Cấu hình thông báo platform/org.

## Component con (logic UI chính)

- `@/components/ui/card` → `artifacts/pos-app/src/components/ui/card.tsx`
- `@/components/ui/badge` → `artifacts/pos-app/src/components/ui/badge.tsx`
- `@/components/ui/switch` → `artifacts/pos-app/src/components/ui/switch.tsx`
- `@/components/ui/checkbox` → `artifacts/pos-app/src/components/ui/checkbox.tsx`
- `@/components/ui/button` → `artifacts/pos-app/src/components/ui/button.tsx`
- `@/components/ui/dialog` → `artifacts/pos-app/src/components/ui/dialog.tsx`

## Cách đọc code

- API: tìm `useQuery`, `useMutation`, `apiFetch`, hoặc mục **Chuỗi `/api/...`** bên dưới.
- Quyền: `lib/session-permissions.ts`, biểu thức trong `app-layout.tsx` và file page.
- Offline: các trang POS có thể gọi Dexie qua `@/lib/offline/...`.

## Module API liên quan (trong Map)

- [`notification-settings`](../../module-api/cau-hinh-thong-bao-api/) — nhóm `/api/notification-settings`

**Đọc tiếp:** [Hướng dẫn đọc Map](../../huong-dan-doc/)

## Quyền (phát hiện trong source)

- Có kiểm tra role **`super_admin`** (hoặc redirect dashboard).

## React Query keys

- `["notification-settings"]`

## Redirect trong component

- → `/dashboard`

## Hàm fetch API (trích)

- `fetchSettings` → `/api/notification-settings`
- `patchSettings` → `/api/notification-settings`

## JSX component dùng trong file (PascalCase)

- `<Badge />`
- `<Bell />`
- `<Button />`
- `<Card />`
- `<CardContent />`
- `<CardDescription />`
- `<CardHeader />`
- `<CardTitle />`
- `<Checkbox />`
- `<Dialog />`
- `<DialogContent />`
- `<DialogDescription />`
- `<DialogHeader />`
- `<DialogTitle />`
- `<Mail />`
- `<SettingItem />`
- `<SettingsResponse />`
- `<ShieldAlert />`
- `<Switch />`
- `<Users />`

## Dialog / modal (tiêu đề)

- Vai trò nhận thông báo

## Import chính (đầu file)

- `import { useMemo, useState } from "react";`
- `import { useMutation, useQuery, useQueryClient } from "@tanstack/react-query";`
- `import { Bell, Mail, ShieldAlert, Users } from "lucide-react";`
- `import { useSessionUser } from "@/lib/use-session-user";`
- `import { Card, CardContent, CardDescription, CardHeader, CardTitle } from "@/components/ui/card";`
- `import { Badge } from "@/components/ui/badge";`
- `import { Switch } from "@/components/ui/switch";`
- `import { Checkbox } from "@/components/ui/checkbox";`
- `import { Button } from "@/components/ui/button";`
- `import {`
- `import { useToast } from "@/hooks/use-toast";`
- `import { Redirect } from "wouter";`
- `import { withApiAuthHeaders } from "@/lib/api-auth-fetch";`

## Module `@/lib/...` được import

- `@/lib/api-auth-fetch`
- `@/lib/use-session-user`

## Component `@/components/...` (đã quét API lớp 1)

- `ui/card` → `artifacts/pos-app/src/components/ui/card.tsx`
- `ui/badge` → `artifacts/pos-app/src/components/ui/badge.tsx`
- `ui/switch` → `artifacts/pos-app/src/components/ui/switch.tsx`
- `ui/checkbox` → `artifacts/pos-app/src/components/ui/checkbox.tsx`
- `ui/button` → `artifacts/pos-app/src/components/ui/button.tsx`
- `ui/dialog` → `artifacts/pos-app/src/components/ui/dialog.tsx`

## Chuỗi `/api/...` (page + component con, 1 mục)

- `/api/notification-settings` → [`notification-settings`](../../module-api/cau-hinh-thong-bao-api/)

## Liên kết mã

- Khai báo URL: `artifacts/pos-app/src/App.tsx`
- Menu/layout: `components/layout/app-layout.tsx`
- Phiên đăng nhập: `lib/session-cache.ts`, `lib/use-session-user.ts`
