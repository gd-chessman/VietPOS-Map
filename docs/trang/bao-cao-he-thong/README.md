# Trang giao diện: `system-reports.tsx`

**Mô tả:** Báo cáo hệ thống, sự kiện, lỗi.

**Mã nguồn Shop:** `artifacts/pos-app/src/pages/system-reports.tsx`

**Đường dẫn URL:** `/system-reports`
**Tên component React:** `SystemReportsPage`
**Quy mô:** ~269 dòng.

## Thông tin hiển thị

Nội dung người dùng **nhìn thấy** trên màn hình (trích nhãn từ TSX; số liệu động từ API).

### `system-reports.tsx`

**Tiêu đề trang:** “Báo cáo hệ thống”
**Thẻ / chỉ số (CardTitle):**
- Tổng sự kiện (kỳ)
- Trên trang — cảnh báo
- Chi tiết
**Nhãn lọc / preset / placeholder:**
- Ô nhập: Chi nhánh
- Ô nhập: Loại
- Ô nhập: Mức

## Thao tác người dùng

Hành động chính (nút, menu, mục dialog) — không liệt kê mọi nút icon-only.

**Đường dẫn:** `/system-reports`

Báo cáo hệ thống, sự kiện, lỗi.

## Menu sidebar

- **Nhãn:** Báo cáo hệ thống
- **Điều kiện hiện menu (`show`):** `isSuperAdmin`

## Component con (logic UI chính)

- `@/components/ui/card` → `artifacts/pos-app/src/components/ui/card.tsx`
- `@/components/ui/badge` → `artifacts/pos-app/src/components/ui/badge.tsx`
- `@/components/pagination-bar` → `artifacts/pos-app/src/components/pagination-bar.tsx`
- `@/components/date-range-filter` → `artifacts/pos-app/src/components/date-range-filter.tsx`
- `@/components/ui/select` → `artifacts/pos-app/src/components/ui/select.tsx`

## Cách đọc code

- API: tìm `useQuery`, `useMutation`, `apiFetch`, hoặc mục **Chuỗi `/api/...`** bên dưới.
- Quyền: `lib/session-permissions.ts`, biểu thức trong `app-layout.tsx` và file page.
- Offline: các trang POS có thể gọi Dexie qua `@/lib/offline/...`.

## Module API liên quan (trong Map)

- [`dashboard`](../../module-api/bang-dieu-khiem-api/) — nhóm `/api/dashboard`
- [`shops`](../../module-api/cua-hang/) — nhóm `/api/shops`
- [`system-events?${params}`](../../module-api/system-events?${params}/) — nhóm `/api/system-events?${params}`

**Đọc tiếp:** [Hướng dẫn đọc Map](../../huong-dan-doc/)

## Quyền (phát hiện trong source)

- Có kiểm tra role **`super_admin`** (hoặc redirect dashboard).

## JSX component dùng trong file (PascalCase)

- `<AlertTriangle />`
- `<Badge />`
- `<Card />`
- `<CardContent />`
- `<CardHeader />`
- `<CardTitle />`
- `<DateFilter />`
- `<DateRangeFilter />`
- `<PaginationBar />`
- `<ScrollText />`
- `<Select />`
- `<SelectContent />`
- `<SelectItem />`
- `<SelectTrigger />`
- `<SelectValue />`
- `<SystemEventRow />`
- `<SystemEventsPage />`

## Import chính (đầu file)

- `import { useEffect, useMemo, useState } from "react";`
- `import { useGetMe, getGetMeQueryKey } from "@workspace/api-client-react";`
- `import { useQuery } from "@tanstack/react-query";`
- `import { format } from "date-fns";`
- `import { vi } from "date-fns/locale";`
- `import { AlertTriangle, ScrollText } from "lucide-react";`
- `import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";`
- `import { Badge } from "@/components/ui/badge";`
- `import { PaginationBar } from "@/components/pagination-bar";`
- `import { DateRangeFilter, resolveDateRange, type DateFilter, todayStr } from "@/components/date-range-filter";`
- `import { apiGet } from "@/lib/sales-api";`
- `import {`

## Module `@/lib/...` được import

- `@/lib/sales-api`

## Component `@/components/...` (đã quét API lớp 1)

- `ui/card` → `artifacts/pos-app/src/components/ui/card.tsx`
- `ui/badge` → `artifacts/pos-app/src/components/ui/badge.tsx`
- `pagination-bar` → `artifacts/pos-app/src/components/pagination-bar.tsx`
- `date-range-filter` → `artifacts/pos-app/src/components/date-range-filter.tsx`
- `ui/select` → `artifacts/pos-app/src/components/ui/select.tsx`

## Chuỗi `/api/...` (page + component con, 3 mục)

- `/api/dashboard/revenue-chart` → [`dashboard`](../../module-api/bang-dieu-khiem-api/)
- `/api/shops` → [`shops`](../../module-api/cua-hang/)
- `/api/system-events?${params}`

## Liên kết mã

- Khai báo URL: `artifacts/pos-app/src/App.tsx`
- Menu/layout: `components/layout/app-layout.tsx`
- Phiên đăng nhập: `lib/session-cache.ts`, `lib/use-session-user.ts`
