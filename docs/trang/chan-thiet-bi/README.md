# Trang giao diện: `device-ban.tsx`

**Mô tả:** Redirect legacy → access-block tab thiết bị.

**Mã nguồn Shop:** `artifacts/pos-app/src/pages/device-ban.tsx`

**Đường dẫn URL:** `*(public hoặc redirect — xem App.tsx)*`
**Tên component React:** `*(default export)*`
**Quy mô:** ~282 dòng.

## Thông tin hiển thị

Nội dung người dùng **nhìn thấy** trên màn hình (trích nhãn từ TSX; số liệu động từ API).

### `device-ban.tsx`

**Thẻ / chỉ số (CardTitle):**
- Thêm thiết bị bị chặn
- Danh sách đang chặn
**Cột bảng:**
- Tên thiết bị
- Device ID
- Ghi chú
- Thêm lúc
- Người thêm
**Nhãn lọc / preset / placeholder:**
- Device ID
- Ghi chú (tuỳ chọn)
- Ô nhập: pos-…
- Ô nhập: Máy lạ, đã thu hồi…
**Tooltip / mô tả ngắn (title=):**
- Bỏ chặn

## Thao tác người dùng

Hành động chính (nút, menu, mục dialog) — không liệt kê mọi nút icon-only.

### `device-ban.tsx`

**Thao tác:**
- Chặn thiết bị
- setConfirmRemove( ) } >
- ); }} > Bỏ chặn
- Huỷ

**Hộp thoại (tiêu đề):**
- Bỏ chặn thiết bị này?

**Export:** `DeviceBanSection` (tab **Chặn thiết bị** trên `/access-block`).

## API (React Query `["blocked-devices"]`)

| Thao tác | HTTP |
|----------|------|
| Tải danh sách | `GET /api/blocked-devices` |
| Thêm | `POST /api/blocked-devices` body `{ deviceId, note? }` |
| Bỏ chặn | `DELETE /api/blocked-devices/:id` |

## UI

- Form nhập **Device ID** (client gửi qua header — xem `lib/device/device-id.ts`).
- Bảng tương tự IP ban; có thể hiển thị device id hiện tại của trình duyệt để tham chiếu.

**Đọc tiếp:** [Hướng dẫn đọc Map](../../huong-dan-doc/)

## Component con export trong file

- `DeviceBanSection`

## React Query keys

- `["blocked-devices"]`

## Hàm fetch API (trích)

- `fetchBlockedDevices` → `/api/blocked-devices`
- `addBlockedDevice` → `/api/blocked-devices`

## JSX component dùng trong file (PascalCase)

- `<AlertDialog />`
- `<AlertDialogAction />`
- `<AlertDialogCancel />`
- `<AlertDialogContent />`
- `<AlertDialogDescription />`
- `<AlertDialogFooter />`
- `<AlertDialogHeader />`
- `<AlertDialogTitle />`
- `<BlockedDeviceRow />`
- `<Button />`
- `<Card />`
- `<CardContent />`
- `<CardDescription />`
- `<CardHeader />`
- `<CardTitle />`
- `<Input />`
- `<Label />`
- `<ListResponse />`
- `<Table />`
- `<TableBody />`
- `<TableCell />`
- `<TableHead />`
- `<TableHeader />`
- `<TableRow />`
- `<Trash2 />`

## Dialog / modal (tiêu đề)

- Bỏ chặn thiết bị này?

## Import chính (đầu file)

- `import { useState } from "react";`
- `import { useMutation, useQuery, useQueryClient } from "@tanstack/react-query";`
- `import { format } from "date-fns";`
- `import { vi } from "date-fns/locale";`
- `import { Trash2 } from "lucide-react";`
- `import { withApiAuthHeaders } from "@/lib/api-auth-fetch";`
- `import { getOrCreateDeviceId } from "@/lib/device/device-id";`
- `import { Card, CardContent, CardDescription, CardHeader, CardTitle } from "@/components/ui/card";`
- `import { Button } from "@/components/ui/button";`
- `import { Input } from "@/components/ui/input";`
- `import { Label } from "@/components/ui/label";`
- `import {`
- `import { useToast } from "@/hooks/use-toast";`
- `import {`

## Module `@/lib/...` được import

- `@/lib/api-auth-fetch`
- `@/lib/device/device-id`

## Chuỗi `/api/...` (page + component con, 2 mục)

- `/api/blocked-devices` → [`blocked-devices`](../../module-api/chan-thiet-bi-api/)
- `/api/blocked-devices/${id}` → [`blocked-devices`](../../module-api/chan-thiet-bi-api/)

## Liên kết mã

- Khai báo URL: `artifacts/pos-app/src/App.tsx`
- Menu/layout: `components/layout/app-layout.tsx`
- Phiên đăng nhập: `lib/session-cache.ts`, `lib/use-session-user.ts`
