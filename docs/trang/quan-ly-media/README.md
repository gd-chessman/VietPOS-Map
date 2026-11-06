# Trang giao diện: `media.tsx`

**Mô tả:** Thư viện media/upload ảnh sản phẩm. (URL /media, MediaPage, ~603 dòng).

**Mã nguồn Shop:** `artifacts/pos-app/src/pages/media.tsx`

**Đường dẫn URL:** `/media`
**Tên component React:** `MediaPage`
**Quy mô:** ~603 dòng.

**Đường dẫn:** `/media`

Thư viện media/upload ảnh sản phẩm.

## Menu sidebar

- **Nhãn:** Thư viện ảnh
- **Điều kiện hiện menu (`show`):** `canViewMedia`

## Component con (logic UI chính)

- `@/components/MediaOrderViewDialog` → `artifacts/pos-app/src/components/MediaOrderViewDialog.tsx`
- `@/components/ui/input` → `artifacts/pos-app/src/components/ui/input.tsx`
- `@/components/ui/badge` → `artifacts/pos-app/src/components/ui/badge.tsx`
- `@/components/ui/select` → `artifacts/pos-app/src/components/ui/select.tsx`
- `@/components/ImageLightbox` → `artifacts/pos-app/src/components/ImageLightbox.tsx`
- `@/components/pagination-bar` → `artifacts/pos-app/src/components/pagination-bar.tsx`
- `@/components/date-range-filter` → `artifacts/pos-app/src/components/date-range-filter.tsx`
- `@/components/three-day-date-bar` → `artifacts/pos-app/src/components/three-day-date-bar.tsx`

## Cách đọc code

- API: tìm `useQuery`, `useMutation`, `apiFetch`, hoặc mục **Chuỗi `/api/...`** bên dưới.
- Quyền: `lib/session-permissions.ts`, biểu thức trong `app-layout.tsx` và file page.
- Offline: các trang POS có thể gọi Dexie qua `@/lib/offline/...`.

## Module API liên quan (trong Map)

- [`dashboard`](../../module-api/bang-dieu-khiem-api/) — nhóm `/api/dashboard`
- [`media?${params}`](../../module-api/media?${params}/) — nhóm `/api/media?${params}`

**Đọc tiếp:** [Hướng dẫn đọc Map](../../huong-dan-doc/)

## Query string URL (đọc trong code)

- `orderId`
- `type`

## JSX component dùng trong file (PascalCase)

- `<Badge />`
- `<DateFilter />`
- `<Download />`
- `<FileText />`
- `<Icon />`
- `<ImageLightbox />`
- `<Images />`
- `<Input />`
- `<MediaOrderViewDialog />`
- `<MediaResponse />`
- `<MediaType />`
- `<PaginationBar />`
- `<Search />`
- `<Select />`
- `<SelectContent />`
- `<SelectItem />`
- `<SelectTrigger />`
- `<SelectValue />`
- `<ThreeDayDateBar />`

## Import chính (đầu file)

- `import { useEffect, useMemo, useState } from "react";`
- `import { useLocation } from "wouter";`
- `import { useQuery } from "@tanstack/react-query";`
- `import {`
- `import { MediaOrderViewDialog } from "@/components/MediaOrderViewDialog";`
- `import { Input } from "@/components/ui/input";`
- `import { Badge } from "@/components/ui/badge";`
- `import {`
- `import { apiGet } from "@/lib/sales-api";`
- `import { ImageLightbox, downloadImage, imageDownloadFilename } from "@/components/ImageLightbox";`
- `import { PaginationBar } from "@/components/pagination-bar";`
- `import {`
- `import { cn } from "@/lib/utils";`
- `import { useSessionUser } from "@/lib/use-session-user";`
- `import {`

## Module `@/lib/...` được import

- `@/lib/sales-api`
- `@/lib/use-session-user`
- `@/lib/utils`

## Component `@/components/...` (đã quét API lớp 1)

- `MediaOrderViewDialog` → `artifacts/pos-app/src/components/MediaOrderViewDialog.tsx`
- `ui/input` → `artifacts/pos-app/src/components/ui/input.tsx`
- `ui/badge` → `artifacts/pos-app/src/components/ui/badge.tsx`
- `ui/select` → `artifacts/pos-app/src/components/ui/select.tsx`
- `ImageLightbox` → `artifacts/pos-app/src/components/ImageLightbox.tsx`
- `pagination-bar` → `artifacts/pos-app/src/components/pagination-bar.tsx`
- `date-range-filter` → `artifacts/pos-app/src/components/date-range-filter.tsx`
- `three-day-date-bar` → `artifacts/pos-app/src/components/three-day-date-bar.tsx`

## Chuỗi `/api/...` (page + component con, 2 mục)

- `/api/dashboard/revenue-chart` → [`dashboard`](../../module-api/bang-dieu-khiem-api/)
- `/api/media?${params}`

## Liên kết mã

- Khai báo URL: `artifacts/pos-app/src/App.tsx`
- Menu/layout: `components/layout/app-layout.tsx`
- Phiên đăng nhập: `lib/session-cache.ts`, `lib/use-session-user.ts`
