# Frontend: `chain-api-keys.tsx`

**Mô tả:** Tạo API key shop cho widget và thiết bị ESP32. (URL *(public hoặc redirect — xem App.tsx)*, ChainApiKeysTab, ~405 dòng).

**Source Shop:** `artifacts/pos-app/src/pages/chain-api-keys.tsx`

**URL (wouter):** `*(public hoặc redirect — xem App.tsx)*`
**Component:** `ChainApiKeysTab`
**Độ lớn:** ~405 dòng.

**Route:** `*(public hoặc redirect — xem App.tsx)*`

Tạo API key shop cho widget và thiết bị ESP32.

## Component con (logic UI chính)

- `@/components/ui/button` → `artifacts/pos-app/src/components/ui/button.tsx`
- `@/components/ui/card` → `artifacts/pos-app/src/components/ui/card.tsx`
- `@/components/ui/dialog` → `artifacts/pos-app/src/components/ui/dialog.tsx`
- `@/components/ui/alert-dialog` → `artifacts/pos-app/src/components/ui/alert-dialog.tsx`
- `@/components/ui/input` → `artifacts/pos-app/src/components/ui/input.tsx`
- `@/components/ui/switch` → `artifacts/pos-app/src/components/ui/switch.tsx`
- `@/components/ui/table` → `artifacts/pos-app/src/components/ui/table.tsx`

## Cách đọc code

- API: tìm `useQuery`, `useMutation`, `apiFetch`, hoặc mục **Chuỗi `/api/...`** bên dưới.
- Quyền: `lib/session-permissions.ts`, biểu thức trong `app-layout.tsx` và file page.
- Offline: các trang POS có thể gọi Dexie qua `@/lib/offline/...`.

## API modules (map sang docs)

- [`api-modules/shop-api-keys.md`](../api-modules/shop-api-keys.md) — prefix `/api/shop-api-keys`

## JSX component dùng trong file (PascalCase)

- `<AlertDialog />`
- `<AlertDialogAction />`
- `<AlertDialogCancel />`
- `<AlertDialogContent />`
- `<AlertDialogDescription />`
- `<AlertDialogFooter />`
- `<AlertDialogHeader />`
- `<AlertDialogTitle />`
- `<Button />`
- `<Card />`
- `<CardContent />`
- `<CardHeader />`
- `<CardTitle />`
- `<Check />`
- `<Copy />`
- `<CountMode />`
- `<CreatedKey />`
- `<Dialog />`
- `<DialogContent />`
- `<DialogHeader />`
- `<DialogTitle />`
- `<Input />`
- `<Plus />`
- `<Radio />`
- `<SecretRow />`
- … 10 component khác

## Dialog / modal (tiêu đề)

- Cảm biến — {created?.shopName}
- Xóa cảm biến?

## Import chính (đầu file)

- `import { useState } from "react";`
- `import { useMutation, useQuery, useQueryClient } from "@tanstack/react-query";`
- `import { Check, Copy, Plus, Radio, Trash2 } from "lucide-react";`
- `import { Button } from "@/components/ui/button";`
- `import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";`
- `import { Dialog, DialogContent, DialogHeader, DialogTitle } from "@/components/ui/dialog";`
- `import {`
- `import { Input } from "@/components/ui/input";`
- `import { Switch } from "@/components/ui/switch";`
- `import { Table, TableBody, TableCell, TableHead, TableHeader, TableRow } from "@/components/ui/table";`
- `import { useToast } from "@/hooks/use-toast";`
- `import { apiDelete, apiGet, apiPatch, apiPost } from "@/lib/sales-api";`

## Module `@/lib/...` được import

- `@/lib/sales-api`

## Component `@/components/...` (đã quét API lớp 1)

- `ui/button` → `artifacts/pos-app/src/components/ui/button.tsx`
- `ui/card` → `artifacts/pos-app/src/components/ui/card.tsx`
- `ui/dialog` → `artifacts/pos-app/src/components/ui/dialog.tsx`
- `ui/alert-dialog` → `artifacts/pos-app/src/components/ui/alert-dialog.tsx`
- `ui/input` → `artifacts/pos-app/src/components/ui/input.tsx`
- `ui/switch` → `artifacts/pos-app/src/components/ui/switch.tsx`
- `ui/table` → `artifacts/pos-app/src/components/ui/table.tsx`

## Chuỗi `/api/...` (page + component con, 4 mục)

- `/api/shop-api-keys` → [`api-modules/shop-api-keys.md`](../api-modules/shop-api-keys.md)
- `/api/shop-api-keys/${id}` → [`api-modules/shop-api-keys.md`](../api-modules/shop-api-keys.md)
- `/api/shop-api-keys/overview` → [`api-modules/shop-api-keys.md`](../api-modules/shop-api-keys.md)
- `/api/shop-api-keys/shops/${shopId}` → [`api-modules/shop-api-keys.md`](../api-modules/shop-api-keys.md)

## File liên quan

- Route khai báo: `artifacts/pos-app/src/App.tsx`
- Layout/menu: `components/layout/app-layout.tsx`
- Session: `lib/session-cache.ts`, `lib/use-session-user.ts`
