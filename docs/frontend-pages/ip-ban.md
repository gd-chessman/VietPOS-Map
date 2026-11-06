# Frontend: `ip-ban.tsx`

**Mô tả:** Redirect legacy → access-block tab IP. (URL *(public hoặc redirect — xem App.tsx)*, *(default export)*, ~266 dòng).

**Source Shop:** `artifacts/pos-app/src/pages/ip-ban.tsx`

**URL (wouter):** `*(public hoặc redirect — xem App.tsx)*`
**Component:** `*(default export)*`
**Độ lớn:** ~266 dòng.

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

## Section / component export trong file

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

- `/api/blocked-ips` → [`api-modules/blocked-ips.md`](../api-modules/blocked-ips.md)
- `/api/blocked-ips/${id}` → [`api-modules/blocked-ips.md`](../api-modules/blocked-ips.md)

## File liên quan

- Route khai báo: `artifacts/pos-app/src/App.tsx`
- Layout/menu: `components/layout/app-layout.tsx`
- Session: `lib/session-cache.ts`, `lib/use-session-user.ts`
