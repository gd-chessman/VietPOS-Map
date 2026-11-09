# Trang giao diện: `not-found.tsx`

**Mô tả:** Trang 404 SPA.

**Mã nguồn Shop:** `artifacts/pos-app/src/pages/not-found.tsx`

**Đường dẫn URL:** `*(public hoặc redirect — xem App.tsx)*`
**Tên component React:** `NotFound`
**Quy mô:** ~22 dòng.

## Thông tin hiển thị

Nội dung người dùng **nhìn thấy** trên màn hình (trích nhãn từ TSX; số liệu động từ API).

### `not-found.tsx`

**Tiêu đề trang:** “404 Page Not Found”

## Thao tác người dùng

Hành động chính (nút, menu, mục dialog) — không liệt kê mọi nút icon-only.

**Đường dẫn:** `*(public hoặc redirect — xem App.tsx)*`

Trang 404 SPA.

## Component con (logic UI chính)

- `@/components/ui/card` → `artifacts/pos-app/src/components/ui/card.tsx`

## Cách đọc code

- API: tìm `useQuery`, `useMutation`, `apiFetch`, hoặc mục **Chuỗi `/api/...`** bên dưới.
- Quyền: `lib/session-permissions.ts`, biểu thức trong `app-layout.tsx` và file page.
- Offline: các trang POS có thể gọi Dexie qua `@/lib/offline/...`.

**Đọc tiếp:** [Hướng dẫn đọc Map](../../huong-dan-doc/)

## JSX component dùng trong file (PascalCase)

- `<AlertCircle />`
- `<Card />`
- `<CardContent />`

## Import chính (đầu file)

- `import { Card, CardContent } from "@/components/ui/card";`
- `import { AlertCircle } from "lucide-react";`

## Component `@/components/...` (đã quét API lớp 1)

- `ui/card` → `artifacts/pos-app/src/components/ui/card.tsx`

## Liên kết mã

- Khai báo URL: `artifacts/pos-app/src/App.tsx`
- Menu/layout: `components/layout/app-layout.tsx`
- Phiên đăng nhập: `lib/session-cache.ts`, `lib/use-session-user.ts`
