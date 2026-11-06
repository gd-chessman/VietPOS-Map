# Trang giao diện: `keyboard-shortcuts.tsx`

**Mô tả:** Bảng phím tắt POS/desktop. (URL /keyboard-shortcuts, KeyboardShortcutsPage, ~396 dòng).

**Mã nguồn Shop:** `artifacts/pos-app/src/pages/keyboard-shortcuts.tsx`

**Đường dẫn URL:** `/keyboard-shortcuts`
**Tên component React:** `KeyboardShortcutsPage`
**Quy mô:** ~396 dòng.

**Đường dẫn:** `/keyboard-shortcuts`

Bảng phím tắt POS/desktop.

## Component con (logic UI chính)

- `@/components/ui/button` → `artifacts/pos-app/src/components/ui/button.tsx`
- `@/components/ui/alert-dialog` → `artifacts/pos-app/src/components/ui/alert-dialog.tsx`
- `@/components/ui/card` → `artifacts/pos-app/src/components/ui/card.tsx`
- `@/components/ui/kbd` → `artifacts/pos-app/src/components/ui/kbd.tsx`
- `@/components/ShortcutKeys` → `artifacts/pos-app/src/components/ShortcutKeys.tsx`

## Cách đọc code

- API: tìm `useQuery`, `useMutation`, `apiFetch`, hoặc mục **Chuỗi `/api/...`** bên dưới.
- Quyền: `lib/session-permissions.ts`, biểu thức trong `app-layout.tsx` và file page.
- Offline: các trang POS có thể gọi Dexie qua `@/lib/offline/...`.

**Đọc tiếp:** [Hướng dẫn đọc Map](../../huong-dan-doc/)

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
- `<CardDescription />`
- `<CardHeader />`
- `<CardTitle />`
- `<Kbd />`
- `<Keyboard />`
- `<ShortcutCaptureField />`
- `<ShortcutKeyParts />`
- `<ShortcutKeys />`
- `<ShortcutRecordingTarget />`
- `<ShortcutRow />`

## Dialog / modal (tiêu đề)

- Khôi phục phím tắt mặc định?

## Import chính (đầu file)

- `import { useEffect, useRef, useState } from "react";`
- `import { Keyboard } from "lucide-react";`
- `import { Button } from "@/components/ui/button";`
- `import {`
- `import { Card, CardContent, CardDescription, CardHeader, CardTitle } from "@/components/ui/card";`
- `import { Kbd } from "@/components/ui/kbd";`
- `import { useToast } from "@/hooks/use-toast";`
- `import { isTauriRuntime } from "@/lib/tauri-runtime";`
- `import { cn } from "@/lib/utils";`
- `import { ShortcutKeys, ShortcutKeyParts } from "@/components/ShortcutKeys";`
- `import {`

## Module `@/lib/...` được import

- `@/lib/pos-keyboard-shortcuts`
- `@/lib/tauri-runtime`
- `@/lib/utils`

## Component `@/components/...` (đã quét API lớp 1)

- `ui/button` → `artifacts/pos-app/src/components/ui/button.tsx`
- `ui/alert-dialog` → `artifacts/pos-app/src/components/ui/alert-dialog.tsx`
- `ui/card` → `artifacts/pos-app/src/components/ui/card.tsx`
- `ui/kbd` → `artifacts/pos-app/src/components/ui/kbd.tsx`
- `ShortcutKeys` → `artifacts/pos-app/src/components/ShortcutKeys.tsx`

## Liên kết mã

- Khai báo URL: `artifacts/pos-app/src/App.tsx`
- Menu/layout: `components/layout/app-layout.tsx`
- Phiên đăng nhập: `lib/session-cache.ts`, `lib/use-session-user.ts`
