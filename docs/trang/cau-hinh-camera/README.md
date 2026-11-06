# Trang giao diện: `camera-settings.tsx`

**Mô tả:** Cấu hình camera (desktop) phục vụ POS/media. (URL /camera-settings, CameraSettingsPage, ~370 dòng).

**Mã nguồn Shop:** `artifacts/pos-app/src/pages/camera-settings.tsx`

**Đường dẫn URL:** `/camera-settings`
**Tên component React:** `CameraSettingsPage`
**Quy mô:** ~370 dòng.

**Đường dẫn:** `/camera-settings`

Cấu hình camera (desktop) phục vụ POS/media.

## Component con (logic UI chính)

- `@/components/ui/card` → `artifacts/pos-app/src/components/ui/card.tsx`
- `@/components/ui/label` → `artifacts/pos-app/src/components/ui/label.tsx`
- `@/components/ui/radio-group` → `artifacts/pos-app/src/components/ui/radio-group.tsx`
- `@/components/ui/select` → `artifacts/pos-app/src/components/ui/select.tsx`
- `@/components/ui/button` → `artifacts/pos-app/src/components/ui/button.tsx`
- `@/components/ui/alert` → `artifacts/pos-app/src/components/ui/alert.tsx`
- `@/components/ui/kbd` → `artifacts/pos-app/src/components/ui/kbd.tsx`

## Cách đọc code

- API: tìm `useQuery`, `useMutation`, `apiFetch`, hoặc mục **Chuỗi `/api/...`** bên dưới.
- Quyền: `lib/session-permissions.ts`, biểu thức trong `app-layout.tsx` và file page.
- Offline: các trang POS có thể gọi Dexie qua `@/lib/offline/...`.

**Đọc tiếp:** [Hướng dẫn đọc Map](../../huong-dan-doc/)

## JSX component dùng trong file (PascalCase)

- `<Alert />`
- `<AlertDescription />`
- `<AlertTitle />`
- `<Button />`
- `<Camera />`
- `<Card />`
- `<CardContent />`
- `<CardDescription />`
- `<CardHeader />`
- `<CardTitle />`
- `<Kbd />`
- `<Label />`
- `<LanWidgetPhone />`
- `<Link />`
- `<Loader2 />`
- `<RadioGroup />`
- `<RadioGroupItem />`
- `<RefreshCw />`
- `<Select />`
- `<SelectContent />`
- `<SelectItem />`
- `<SelectTrigger />`
- `<SelectValue />`
- `<Smartphone />`
- `<VideoInputDevice />`

## Import chính (đầu file)

- `import { useCallback, useEffect, useRef, useState } from "react";`
- `import { Camera, Loader2, RefreshCw, Smartphone } from "lucide-react";`
- `import { Card, CardContent, CardDescription, CardHeader, CardTitle } from "@/components/ui/card";`
- `import { Label } from "@/components/ui/label";`
- `import { RadioGroup, RadioGroupItem } from "@/components/ui/radio-group";`
- `import {`
- `import { Button } from "@/components/ui/button";`
- `import { Alert, AlertDescription, AlertTitle } from "@/components/ui/alert";`
- `import { Link } from "wouter";`
- `import { isTauriRuntime } from "@/lib/tauri-runtime";`
- `import {`
- `import { listVideoInputDevices, type VideoInputDevice } from "@/lib/camera-access";`
- `import {`
- `import { formatChordLabel, usePosShortcutBindings } from "@/lib/pos-keyboard-shortcuts";`
- `import { Kbd } from "@/components/ui/kbd";`

## Module `@/lib/...` được import

- `@/lib/camera-access`
- `@/lib/camera-capture-settings`
- `@/lib/pos-keyboard-shortcuts`
- `@/lib/tauri-lan-peers`
- `@/lib/tauri-runtime`

## Component `@/components/...` (đã quét API lớp 1)

- `ui/card` → `artifacts/pos-app/src/components/ui/card.tsx`
- `ui/label` → `artifacts/pos-app/src/components/ui/label.tsx`
- `ui/radio-group` → `artifacts/pos-app/src/components/ui/radio-group.tsx`
- `ui/select` → `artifacts/pos-app/src/components/ui/select.tsx`
- `ui/button` → `artifacts/pos-app/src/components/ui/button.tsx`
- `ui/alert` → `artifacts/pos-app/src/components/ui/alert.tsx`
- `ui/kbd` → `artifacts/pos-app/src/components/ui/kbd.tsx`

## Liên kết mã

- Khai báo URL: `artifacts/pos-app/src/App.tsx`
- Menu/layout: `components/layout/app-layout.tsx`
- Phiên đăng nhập: `lib/session-cache.ts`, `lib/use-session-user.ts`
