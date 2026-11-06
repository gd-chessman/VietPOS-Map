# Trang giao diện: `customer-feedback.tsx`

**Mô tả:** Quản lý phản hồi khách đã gửi từ form công khai. (URL /customer-feedback, CustomerFeedbackPage, ~369 dòng).

**Mã nguồn Shop:** `artifacts/pos-app/src/pages/customer-feedback.tsx`

**Đường dẫn URL:** `/customer-feedback`
**Tên component React:** `CustomerFeedbackPage`
**Quy mô:** ~369 dòng.

**Đường dẫn:** `/customer-feedback`

Quản lý phản hồi khách đã gửi từ form công khai.

## Menu sidebar

- **Nhãn:** Góp ý khách hàng
- **Điều kiện hiện menu (`show`):** `isAdminOrManager`

## Component con (logic UI chính)

- `@/components/ui/card` → `artifacts/pos-app/src/components/ui/card.tsx`
- `@/components/ui/button` → `artifacts/pos-app/src/components/ui/button.tsx`
- `@/components/ui/input` → `artifacts/pos-app/src/components/ui/input.tsx`
- `@/components/ui/badge` → `artifacts/pos-app/src/components/ui/badge.tsx`
- `@/components/ui/select` → `artifacts/pos-app/src/components/ui/select.tsx`
- `@/components/pagination-bar` → `artifacts/pos-app/src/components/pagination-bar.tsx`
- `@/components/ImageLightbox` → `artifacts/pos-app/src/components/ImageLightbox.tsx`

## Cách đọc code

- API: tìm `useQuery`, `useMutation`, `apiFetch`, hoặc mục **Chuỗi `/api/...`** bên dưới.
- Quyền: `lib/session-permissions.ts`, biểu thức trong `app-layout.tsx` và file page.
- Offline: các trang POS có thể gọi Dexie qua `@/lib/offline/...`.

## Module API liên quan (trong Map)

- [`feedback`](../../module-api/phan-hoi-api/) — nhóm `/api/feedback`
- [`feedback?page=${page}&limit=${pageSize}${shopQueryParam ? `](../../module-api/feedback?page=${page}&limit=${pageSize}${shopQueryParam ? /) — nhóm `/api/feedback?page=${page}&limit=${pageSize}${shopQueryParam ? `
- [`shops`](../../module-api/cua-hang/) — nhóm `/api/shops`

**Đọc tiếp:** [Hướng dẫn đọc Map](../../huong-dan-doc/)

## JSX component dùng trong file (PascalCase)

- `<Badge />`
- `<Button />`
- `<Card />`
- `<CardContent />`
- `<CardHeader />`
- `<CardTitle />`
- `<Copy />`
- `<FeedbackListResponse />`
- `<FeedbackStatsResponse />`
- `<ImageLightbox />`
- `<Input />`
- `<MessageSquare />`
- `<PaginationBar />`
- `<Phone />`
- `<QRCodeSVG />`
- `<QrCode />`
- `<RatingBar />`
- `<RatingStars />`
- `<Select />`
- `<SelectContent />`
- `<SelectItem />`
- `<SelectTrigger />`
- `<SelectValue />`
- `<ShopRow />`
- `<Star />`

## Import chính (đầu file)

- `import { useState } from "react";`
- `import { useQuery } from "@tanstack/react-query";`
- `import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";`
- `import { Button } from "@/components/ui/button";`
- `import { Input } from "@/components/ui/input";`
- `import { Badge } from "@/components/ui/badge";`
- `import {`
- `import { MessageSquare, Star, Phone, QrCode, Copy } from "lucide-react";`
- `import { QRCodeSVG } from "qrcode.react";`
- `import { apiGet } from "@/lib/sales-api";`
- `import { useFeedbackUrl } from "@/hooks/useFeedbackUrl";`
- `import { useToast } from "@/hooks/use-toast";`
- `import { PaginationBar, DEFAULT_PAGE_SIZE } from "@/components/pagination-bar";`
- `import { ImageLightbox } from "@/components/ImageLightbox";`

## Module `@/lib/...` được import

- `@/lib/sales-api`

## Component `@/components/...` (đã quét API lớp 1)

- `ui/card` → `artifacts/pos-app/src/components/ui/card.tsx`
- `ui/button` → `artifacts/pos-app/src/components/ui/button.tsx`
- `ui/input` → `artifacts/pos-app/src/components/ui/input.tsx`
- `ui/badge` → `artifacts/pos-app/src/components/ui/badge.tsx`
- `ui/select` → `artifacts/pos-app/src/components/ui/select.tsx`
- `pagination-bar` → `artifacts/pos-app/src/components/pagination-bar.tsx`
- `ImageLightbox` → `artifacts/pos-app/src/components/ImageLightbox.tsx`

## Chuỗi `/api/...` (page + component con, 3 mục)

- `/api/feedback/stats${shopQueryParam ? ` → [`feedback`](../../module-api/phan-hoi-api/)
- `/api/feedback?page=${page}&limit=${pageSize}${shopQueryParam ? `
- `/api/shops` → [`shops`](../../module-api/cua-hang/)

## Liên kết mã

- Khai báo URL: `artifacts/pos-app/src/App.tsx`
- Menu/layout: `components/layout/app-layout.tsx`
- Phiên đăng nhập: `lib/session-cache.ts`, `lib/use-session-user.ts`
