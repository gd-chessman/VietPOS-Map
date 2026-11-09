# Trang giao diện: `page-status.tsx`

**Mô tả:** Trạng thái triển khai từng trang (dev/ops).

**Mã nguồn Shop:** `artifacts/pos-app/src/pages/page-status.tsx`

**Đường dẫn URL:** `/page-status`
**Tên component React:** `PageStatus`
**Quy mô:** ~338 dòng.

## Thông tin hiển thị

Nội dung người dùng **nhìn thấy** trên màn hình (trích nhãn từ TSX; số liệu động từ API).

### `page-status.tsx`

**Tiêu đề trang:** “Trạng thái cửa hàng”
**Thẻ / chỉ số (CardTitle):**
- Trực tuyến
- Ngoại tuyến
- Chi tiết chi nhánh
**Tooltip / mô tả ngắn (title=):**
- Giờ thiết bị lệch so với giờ server ở lần heartbeat gần nhất

## Thao tác người dùng

Hành động chính (nút, menu, mục dialog) — không liệt kê mọi nút icon-only.

**Đường dẫn:** `/page-status`

Trạng thái triển khai từng trang (dev/ops).

## Menu sidebar

- **Nhãn:** Shop status
- **Điều kiện hiện menu (`show`):** `canViewChainDashboard`

## Component con (logic UI chính)

- `@/components/date-range-filter` → `artifacts/pos-app/src/components/date-range-filter.tsx`
- `@/components/ui/card` → `artifacts/pos-app/src/components/ui/card.tsx`
- `@/components/ui/badge` → `artifacts/pos-app/src/components/ui/badge.tsx`
- `@/components/pagination-bar` → `artifacts/pos-app/src/components/pagination-bar.tsx`

## Cách đọc code

- API: tìm `useQuery`, `useMutation`, `apiFetch`, hoặc mục **Chuỗi `/api/...`** bên dưới.
- Quyền: `lib/session-permissions.ts`, biểu thức trong `app-layout.tsx` và file page.
- Offline: các trang POS có thể gọi Dexie qua `@/lib/offline/...`.

## Module API liên quan (trong Map)

- [`dashboard`](../../module-api/bang-dieu-khiem-api/) — nhóm `/api/dashboard`
- [`shops`](../../module-api/cua-hang/) — nhóm `/api/shops`

**Đọc tiếp:** [Hướng dẫn đọc Map](../../huong-dan-doc/)

## Quyền (phát hiện trong source)

- Có kiểm tra role **`super_admin`** (hoặc redirect dashboard).

## JSX component dùng trong file (PascalCase)

- `<AlertTriangle />`
- `<Badge />`
- `<Building2 />`
- `<Card />`
- `<CardContent />`
- `<CardHeader />`
- `<CardTitle />`
- `<DateFilter />`
- `<DateRangeFilter />`
- `<History />`
- `<OperationalEventRow />`
- `<OperationalEventsPage />`
- `<PaginationBar />`
- `<ShopStatusRow />`
- `<Wifi />`
- `<WifiOff />`

## Import chính (đầu file)

- `import { useEffect, useMemo, useState } from "react";`
- `import { useGetMe, getGetMeQueryKey } from "@workspace/api-client-react";`
- `import { useQuery } from "@tanstack/react-query";`
- `import { format, formatDistanceToNow } from "date-fns";`
- `import { DateRangeFilter, resolveDateRange, type DateFilter, todayStr } from "@/components/date-range-filter";`
- `import { vi } from "date-fns/locale";`
- `import { Wifi, WifiOff, AlertTriangle, Building2, History } from "lucide-react";`
- `import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";`
- `import { Badge } from "@/components/ui/badge";`
- `import { PaginationBar } from "@/components/pagination-bar";`
- `import { apiGet } from "@/lib/sales-api";`

## Module `@/lib/...` được import

- `@/lib/sales-api`

## Component `@/components/...` (đã quét API lớp 1)

- `date-range-filter` → `artifacts/pos-app/src/components/date-range-filter.tsx`
- `ui/card` → `artifacts/pos-app/src/components/ui/card.tsx`
- `ui/badge` → `artifacts/pos-app/src/components/ui/badge.tsx`
- `pagination-bar` → `artifacts/pos-app/src/components/pagination-bar.tsx`

## Chuỗi `/api/...` (page + component con, 3 mục)

- `/api/dashboard/revenue-chart` → [`dashboard`](../../module-api/bang-dieu-khiem-api/)
- `/api/shops` → [`shops`](../../module-api/cua-hang/)
- `/api/shops/operational-events?${params}` → [`shops`](../../module-api/cua-hang/)

## Liên kết mã

- Khai báo URL: `artifacts/pos-app/src/App.tsx`
- Menu/layout: `components/layout/app-layout.tsx`
- Phiên đăng nhập: `lib/session-cache.ts`, `lib/use-session-user.ts`
