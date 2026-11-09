# Trang giao diện: `access-overview-section.tsx`

**Mô tả:** Section embed tổng quan access trong trang chặn truy cập.

**Mã nguồn Shop:** `artifacts/pos-app/src/pages/access-overview-section.tsx`

**Đường dẫn URL:** `*(public hoặc redirect — xem App.tsx)*`
**Tên component React:** `*(default export)*`
**Quy mô:** ~453 dòng.

## Thông tin hiển thị

Nội dung người dùng **nhìn thấy** trên màn hình (trích nhãn từ TSX; số liệu động từ API).

### `access-overview-section.tsx`

**Thẻ / chỉ số (CardTitle):**
- Thiết bị & IP gần đây
**Cột bảng:**
- Tên thiết bị
- Device ID
- IP
- Hôm nay
- 48h
- Lần cuối
- Thao tác

## Thao tác người dùng

Hành động chính (nút, menu, mục dialog) — không liệt kê mọi nút icon-only.

### `access-overview-section.tsx`

**Thao tác:**
- void refetch()} > Làm mới
- Đã chặn IP
- setConfirmBlock( ) } > Chặn IP
- Đã chặn thiết bị
- setConfirmBlock( ) } > Chặn thiết bị
- Huỷ

**Không có route riêng** — embed trong tab **Tổng quan** của `/access-block`.

## API

- `GET /api/access-observations?limit=200` — React Query key `["access-observations"]`.
- Chặn nhanh: `POST /api/blocked-ips` hoặc `POST /api/blocked-devices` (note tự động ghi nguồn quan sát).

## UI chính

- Thẻ thống kê **hôm nay:** tổng hit, số device, số IP, số cặp active.
- Bảng: device (tên nếu có trong `allowed_devices`), IP, hit tổng / hit hôm nay, first/last seen.
- Nút **Làm mới**, **Chặn IP**, **Chặn thiết bị** trên từng dòng (confirm dialog).
- Trạng thái đã chặn: nút disabled + icon check.

## Ghi chú kỹ thuật

- Dữ liệu quan sát **không** lưu Postgres — mất khi restart API (TTL vài giờ).
- `deviceName` join từ `lookupDeviceNamesByDeviceIds`.

**Đọc tiếp:** [Hướng dẫn đọc Map](../../huong-dan-doc/)

## Component con export trong file

- `AccessOverviewSection`

## React Query keys

- `["access-observations"]`

## Hàm fetch API (trích)

- `fetchObservations` → `/api/access-observations?limit=200`
- `addBlockedIp` → `/api/blocked-ips`
- `fetchBlockedIpSet` → `/api/blocked-ips`
- `fetchBlockedDeviceSet` → `/api/blocked-devices`
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
- `<Ban />`
- `<BlockConfirm />`
- `<Button />`
- `<Card />`
- `<CardContent />`
- `<CardDescription />`
- `<CardHeader />`
- `<CardTitle />`
- `<Check />`
- `<ListResponse />`
- `<RefreshCw />`
- `<Set />`
- `<Smartphone />`
- `<Table />`
- `<TableBody />`
- `<TableCell />`
- `<TableHead />`
- … 2 component khác

## Dialog / modal (tiêu đề)

- {confirmBlock?.kind === "ip" ? "Chặn IP này?" : "Chặn thiết bị này?"}

## Import chính (đầu file)

- `import { useMemo, useState } from "react";`
- `import { useMutation, useQuery, useQueryClient } from "@tanstack/react-query";`
- `import { format } from "date-fns";`
- `import { vi } from "date-fns/locale";`
- `import { Ban, Check, RefreshCw, Smartphone } from "lucide-react";`
- `import { withApiAuthHeaders } from "@/lib/api-auth-fetch";`
- `import { cn } from "@/lib/utils";`
- `import { Card, CardContent, CardDescription, CardHeader, CardTitle } from "@/components/ui/card";`
- `import { Button } from "@/components/ui/button";`
- `import {`
- `import { useToast } from "@/hooks/use-toast";`
- `import {`

## Module `@/lib/...` được import

- `@/lib/api-auth-fetch`
- `@/lib/utils`

## Chuỗi `/api/...` (page + component con, 3 mục)

- `/api/access-observations?limit=200`
- `/api/blocked-devices` → [`blocked-devices`](../../module-api/chan-thiet-bi-api/)
- `/api/blocked-ips` → [`blocked-ips`](../../module-api/chan-ip-api/)

## Liên kết mã

- Khai báo URL: `artifacts/pos-app/src/App.tsx`
- Menu/layout: `components/layout/app-layout.tsx`
- Phiên đăng nhập: `lib/session-cache.ts`, `lib/use-session-user.ts`
