# Frontend: `not-found.tsx`

**Mô tả:** Trang 404 SPA. (URL *(public hoặc redirect — xem App.tsx)*, NotFound, ~22 dòng).

**Source Shop:** `artifacts/pos-app/src/pages/not-found.tsx`

**URL (wouter):** `*(public hoặc redirect — xem App.tsx)*`
**Component:** `NotFound`
**Độ lớn:** ~22 dòng.

**Route:** `*(public hoặc redirect — xem App.tsx)*`

Trang 404 SPA.

## Component con (logic UI chính)

- `@/components/ui/card` → `artifacts/pos-app/src/components/ui/card.tsx`

## Cách đọc code

- API: tìm `useQuery`, `useMutation`, `apiFetch`, hoặc mục **Chuỗi `/api/...`** bên dưới.
- Quyền: `lib/session-permissions.ts`, biểu thức trong `app-layout.tsx` và file page.
- Offline: các trang POS có thể gọi Dexie qua `@/lib/offline/...`.

## JSX component dùng trong file (PascalCase)

- `<AlertCircle />`
- `<Card />`
- `<CardContent />`

## Import chính (đầu file)

- `import { Card, CardContent } from "@/components/ui/card";`
- `import { AlertCircle } from "lucide-react";`

## Component `@/components/...` (đã quét API lớp 1)

- `ui/card` → `artifacts/pos-app/src/components/ui/card.tsx`

## File liên quan

- Route khai báo: `artifacts/pos-app/src/App.tsx`
- Layout/menu: `components/layout/app-layout.tsx`
- Session: `lib/session-cache.ts`, `lib/use-session-user.ts`
