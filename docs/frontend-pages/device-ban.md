# Frontend: `device-ban.tsx`

**Mô tả:** Redirect legacy → access-block tab thiết bị. (URL *(public hoặc redirect — xem App.tsx)*, *(default export)*, ~282 dòng).

**Source Shop:** `artifacts/pos-app/src/pages/device-ban.tsx`

**URL (wouter):** `*(public hoặc redirect — xem App.tsx)*`
**Component:** `*(default export)*`
**Độ lớn:** ~282 dòng.

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

## Section / component export trong file

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

- `/api/blocked-devices` → [`api-modules/blocked-devices.md`](../api-modules/blocked-devices.md)
- `/api/blocked-devices/${id}` → [`api-modules/blocked-devices.md`](../api-modules/blocked-devices.md)

## File liên quan

- Route khai báo: `artifacts/pos-app/src/App.tsx`
- Layout/menu: `components/layout/app-layout.tsx`
- Session: `lib/session-cache.ts`, `lib/use-session-user.ts`
