# Trang giao diện: `ip-ban.tsx`

**Mô tả:** Redirect legacy → access-block tab IP.

**Mã nguồn Shop:** `artifacts/pos-app/src/pages/ip-ban.tsx`

**Đường dẫn URL:** `*(public hoặc redirect — xem App.tsx)*`
**Tên component React:** `*(default export)*`
**Quy mô:** ~266 dòng.

## Thông tin hiển thị

Nội dung người dùng **nhìn thấy** trên màn hình (trích nhãn từ TSX; số liệu động từ API).

### `ip-ban.tsx`

**Thẻ / chỉ số (CardTitle):**
- Thêm IP bị chặn
- Danh sách đang chặn
**Cột bảng:**
- IP
- Ghi chú
- Thêm lúc
- Người thêm
**Nhãn lọc / preset / placeholder:**
- Địa chỉ IP
- Ghi chú (tuỳ chọn)
- Ô nhập: Spam login, bot quét…
**Tooltip / mô tả ngắn (title=):**
- Bỏ chặn

## Thao tác người dùng

Hành động chính (nút, menu, mục dialog) — không liệt kê mọi nút icon-only.

### `ip-ban.tsx`

**Thao tác:**
- Chặn IP
- setConfirmRemove( )} >
- ); }} > Bỏ chặn
- Huỷ

**Hộp thoại (tiêu đề):**
- Bỏ chặn IP này?

**Export:** `IpBanSection` (dùng trong `access-block.tsx`, tab **Chặn IP**).

## API (React Query `["blocked-ips"]`)

| Thao tác | HTTP |
|----------|------|
| Tải danh sách | `GET /api/blocked-ips` |
| Thêm | `POST /api/blocked-ips` body `{ ip, note? }` |
| Bỏ chặn | `DELETE /api/blocked-ips/:id` |

Response GET gồm `items[]`, `envDenylistEnabled` (denylist từ biến môi trường).

## UI

- Form: IP + ghi chú (optional) → **Thêm IP**.
- Bảng: IP, ghi chú, người tạo, thời gian; **Bỏ chặn** (AlertDialog).
- Card cảnh báo nếu `envDenylistEnabled` (IP chặn thêm từ env, không chỉ DB).

**Đọc tiếp:** [Hướng dẫn đọc Map](../../huong-dan-doc/)

## Component con export trong file

- `IpBanSection`

## React Query keys

- `["blocked-ips"]`

## Hàm fetch API (trích)

- `fetchBlockedIps` → `/api/blocked-ips`
- `addBlockedIp` → `/api/blocked-ips`

## JSX component dùng trong file (PascalCase)

- `<AlertDialog />`
- `<AlertDialogAction />`
- `<AlertDialogCancel />`
- `<AlertDialogContent />`
- `<AlertDialogDescription />`
- `<AlertDialogFooter />`
- `<AlertDialogHeader />`
- `<AlertDialogTitle />`
- `<BlockedIpRow />`
- `<Button />`
- `<Card />`
- `<CardContent />`
- `<CardDescription />`
- `<CardHeader />`
- `<CardTitle />`
- `<Input />`
- `<Label />`
- `<ListResponse />`
- `<ShieldAlert />`
- `<Table />`
- `<TableBody />`
- `<TableCell />`
- `<TableHead />`
- `<TableHeader />`
- `<TableRow />`
- … 1 component khác

## Dialog / modal (tiêu đề)

- Bỏ chặn IP này?

## Import chính (đầu file)

- `import { useState } from "react";`
- `import { useMutation, useQuery, useQueryClient } from "@tanstack/react-query";`
- `import { format } from "date-fns";`
- `import { vi } from "date-fns/locale";`
- `import { ShieldAlert, Trash2 } from "lucide-react";`
- `import { withApiAuthHeaders } from "@/lib/api-auth-fetch";`
- `import { Card, CardContent, CardDescription, CardHeader, CardTitle } from "@/components/ui/card";`
- `import { Button } from "@/components/ui/button";`
- `import { Input } from "@/components/ui/input";`
- `import { Label } from "@/components/ui/label";`
- `import {`
- `import { useToast } from "@/hooks/use-toast";`
- `import {`

## Module `@/lib/...` được import

- `@/lib/api-auth-fetch`

## Chuỗi `/api/...` (page + component con, 2 mục)

- `/api/blocked-ips` → [`blocked-ips`](../../module-api/chan-ip-api/)
- `/api/blocked-ips/${id}` → [`blocked-ips`](../../module-api/chan-ip-api/)

## Liên kết mã

- Khai báo URL: `artifacts/pos-app/src/App.tsx`
- Menu/layout: `components/layout/app-layout.tsx`
- Phiên đăng nhập: `lib/session-cache.ts`, `lib/use-session-user.ts`
