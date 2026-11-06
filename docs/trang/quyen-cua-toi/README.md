# Trang giao diện: `my-permissions.tsx`

**Mô tả:** Giải thích quyền role và menu hiện tại. (URL /my-permissions, MyPermissions, ~767 dòng).

**Mã nguồn Shop:** `artifacts/pos-app/src/pages/my-permissions.tsx`

**Đường dẫn URL:** `/my-permissions`
**Tên component React:** `MyPermissions`
**Quy mô:** ~767 dòng.

## Thông tin hiển thị

Nội dung người dùng **nhìn thấy** trên màn hình (trích nhãn từ TSX; số liệu động từ API).

### `my-permissions.tsx`

**Tiêu đề trang:** “Quyền của tôi”
**Nhãn lọc / preset / placeholder:**
- Đang ở chi nhánh chính (kho tổng)
- Quản trị tổng / hệ thống
- Quản trị viên chi nhánh chính
- Quản lý danh mục tại chi nhánh chính
- Bán hàng POS
- Xem / xử lý đơn hàng
- Lọc đơn theo chi nhánh (chuỗi)
- Bán vượt tồn
- Quản lý sửa đơn hàng
- Cửa hàng cho nhân viên sửa thanh toán
- Cửa hàng cho nhân viên xóa giỏ POS
- Tôi được sửa thanh toán (nhân viên)
- Tôi được xóa giỏ (nhân viên)
- Menu hoá đơn xuất VAT
- Đánh dấu đã xuất hoá đơn VAT
- Xem báo cáo nhật ký giỏ POS
- Xem trang sản phẩm
- Thêm / import sản phẩm
- Sửa giá / ngừng kinh doanh sản phẩm
- Xem cột giá vốn (danh mục)
- Xem tồn kho
- Xem giá bán trên tồn
- Xem giá vốn trên tồn
- Quản lý nhà cung cấp
- Đặt hàng nhà cung cấp

## Thao tác người dùng

Hành động chính (nút, menu, mục dialog) — không liệt kê mọi nút icon-only.

### `my-permissions.tsx`

**Thao tác:**
- setPinDialogOpen(true)}> ).pinConfigured ? "Đổi mã PIN" : "Thiết lập mã PIN"}

**Đường dẫn:** `/my-permissions`

Giải thích quyền role hiện tại (đối chiếu menu thực tế).

**Đọc tiếp:** [Hướng dẫn đọc Map](../../huong-dan-doc/)

## Quyền (phát hiện trong source)

- Có kiểm tra role **`super_admin`** (hoặc redirect dashboard).

## JSX component dùng trong file (PascalCase)

- `<Badge />`
- `<Button />`
- `<Card />`
- `<CardContent />`
- `<CardDescription />`
- `<CardHeader />`
- `<CardTitle />`
- `<Icon />`
- `<KeyRound />`
- `<PermissionGroup />`
- `<PermissionRow />`
- `<SetPinWithPasswordDialog />`
- `<Shield />`
- `<Switch />`

## Biểu thức quyền / guard trong file

- `requirePassword`
- `userCanEditShopOperationalSettings`
- `userCanManageChain`

## Import chính (đầu file)

- `import { useEffect, useState, type ComponentProps } from "react";`
- `import { Shield, MapPin, ShoppingCart, Package, ClipboardList, Settings, KeyRound, type LucideIcon } from "lucide-react";`
- `import { useSessionUser } from "@/lib/use-session-user";`
- `import { Card, CardContent, CardDescription, CardHeader, CardTitle } from "@/components/ui/card";`
- `import { Switch } from "@/components/ui/switch";`
- `import { Badge } from "@/components/ui/badge";`
- `import { Button } from "@/components/ui/button";`
- `import { cn } from "@/lib/utils";`
- `import { roleRequiresPin, staffUsesDevicePin } from "@/lib/user-pin";`
- `import { hashDevicePin } from "@/lib/staff-device-pin";`
- `import { updateSavedAccountDevicePinHash } from "@/lib/session-cache";`
- `import { SetPinWithPasswordDialog } from "@/components/SetPinWithPasswordDialog";`
- `import { useSetAuthPin } from "@workspace/api-client-react";`
- `import { useToast } from "@/hooks/use-toast";`
- `import { useQueryClient } from "@tanstack/react-query";`
- `import { getGetMeQueryKey } from "@workspace/api-client-react";`
- `import { useOfflineStatus } from "@/lib/offline";`
- `import { userCanManageChain, userCanEditShopOperationalSettings } from "@/lib/chain-access";`
- … 3 import khác

## Module `@/lib/...` được import

- `@/lib/agent-assistant-access`
- `@/lib/chain-access`
- `@/lib/media-access`
- `@/lib/offline`
- `@/lib/session-cache`
- `@/lib/session-permissions`
- `@/lib/staff-device-pin`
- `@/lib/use-session-user`
- `@/lib/user-pin`
- `@/lib/utils`

## Liên kết mã

- Khai báo URL: `artifacts/pos-app/src/App.tsx`
- Menu/layout: `components/layout/app-layout.tsx`
- Phiên đăng nhập: `lib/session-cache.ts`, `lib/use-session-user.ts`
