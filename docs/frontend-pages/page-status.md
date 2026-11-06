# Frontend: `page-status.tsx`

**Mô tả:** Trạng thái triển khai từng trang (dev/ops). (URL /page-status, PageStatus, ~338 dòng).

**Source Shop:** `artifacts/pos-app/src/pages/page-status.tsx`

**URL (wouter):** `/page-status`
**Component:** `PageStatus`
**Độ lớn:** ~338 dòng.

**Route:** `/page-status`

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

## API modules (map sang docs)

- [`api-modules/dashboard.md`](../api-modules/dashboard.md) — prefix `/api/dashboard`
- [`api-modules/shops.md`](../api-modules/shops.md) — prefix `/api/shops`

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

- `/api/dashboard/revenue-chart` → [`api-modules/dashboard.md`](../api-modules/dashboard.md)
- `/api/shops` → [`api-modules/shops.md`](../api-modules/shops.md)
- `/api/shops/operational-events?${params}` → [`api-modules/shops.md`](../api-modules/shops.md)

## File liên quan

- Route khai báo: `artifacts/pos-app/src/App.tsx`
- Layout/menu: `components/layout/app-layout.tsx`
- Session: `lib/session-cache.ts`, `lib/use-session-user.ts`
