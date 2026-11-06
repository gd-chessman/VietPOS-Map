# Frontend: `system-reports.tsx`

**Mô tả:** Báo cáo hệ thống, sự kiện, lỗi. (URL /system-reports, SystemReportsPage, ~269 dòng).

**Source Shop:** `artifacts/pos-app/src/pages/system-reports.tsx`

**URL (wouter):** `/system-reports`
**Component:** `SystemReportsPage`
**Độ lớn:** ~269 dòng.

**Route:** `/system-reports`

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

## API modules (map sang docs)

- [`api-modules/dashboard.md`](../api-modules/dashboard.md) — prefix `/api/dashboard`
- [`api-modules/shops.md`](../api-modules/shops.md) — prefix `/api/shops`
- [`api-modules/system-events?${params}.md`](../api-modules/system-events?${params}.md) — prefix `/api/system-events?${params}`

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

- `/api/dashboard/revenue-chart` → [`api-modules/dashboard.md`](../api-modules/dashboard.md)
- `/api/shops` → [`api-modules/shops.md`](../api-modules/shops.md)
- `/api/system-events?${params}`

## File liên quan

- Route khai báo: `artifacts/pos-app/src/App.tsx`
- Layout/menu: `components/layout/app-layout.tsx`
- Session: `lib/session-cache.ts`, `lib/use-session-user.ts`
