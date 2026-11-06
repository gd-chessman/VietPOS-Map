# Frontend: `chain.tsx`

**Mô tả:** Sửa tổ chức: shop, Viettel, CQT, Trợ lý AI, URL feedback. (URL /chain, Chain, ~4155 dòng).

**Source Shop:** `artifacts/pos-app/src/pages/chain.tsx`

**URL (wouter):** `/chain`
**Component:** `Chain`
**Độ lớn:** ~4155 dòng.

**Route:** `/chain`

Sửa tổ chức: thông tin, shop, Viettel inbound/outbound, CQT, Trợ lý AI, URL feedback công khai.

## Quyền (phát hiện trong source)

- Có kiểm tra role **`super_admin`** (hoặc redirect dashboard).

## Tab UI (`TabsTrigger` value)

- `agent`
- `bank`
- `config`
- `gdt`
- `info`
- `smtp`
- `viettel`

## JSX component dùng trong file (PascalCase)

- `<AdjustForm />`
- `<AgentAccessRow />`
- `<AlertTriangle />`
- `<AllowedDevice />`
- `<Area />`
- `<AreaChart />`
- `<ArrowDown />`
- `<ArrowRightLeft />`
- `<ArrowUp />`
- `<Badge />`
- `<Ban />`
- `<Banknote />`
- `<BranchDashboardDialog />`
- `<Building2 />`
- `<Button />`
- `<Card />`
- `<CardContent />`
- `<CartesianGrid />`
- `<ChainApiKeysTab />`
- `<ChartPoint />`
- `<Check />`
- `<CheckCircle />`
- `<ChevronDown />`
- `<ChevronRight />`
- `<ChevronUp />`
- … 80 component khác

## Dialog / modal (tiêu đề)

- Chi tiết đơn {resolveOrderInvoiceCode(selectedOrder)}
- Sắp xếp chi nhánh

## Biểu thức quyền / guard trong file

- `userCanEditShopOperationalSettings`
- `userCanManageChain`
- `userCanManageOrganizations`

## Import chính (đầu file)

- `import { useState, useEffect, Fragment, useMemo, useRef } from "react";`
- `import { useQuery, useMutation, useQueryClient } from "@tanstack/react-query";`
- `import { Card, CardContent } from "@/components/ui/card";`
- `import { Button } from "@/components/ui/button";`
- `import { Input } from "@/components/ui/input";`
- `import { Table, TableBody, TableCell, TableHead, TableHeader, TableRow } from "@/components/ui/table";`
- `import { Dialog, DialogContent, DialogHeader, DialogTitle, useNestedDialogGuard } from "@/components/ui/dialog";`
- `import { Tabs, TabsContent, TabsList, TabsTrigger } from "@/components/ui/tabs";`
- `import { Badge } from "@/components/ui/badge";`
- `import { Switch } from "@/components/ui/switch";`
- `import { useToast } from "@/hooks/use-toast";`
- `import {`
- `import {`
- `import { formatVND, formatChartAxisMoney } from "@/lib/utils";`
- `import { resolveOrderInvoiceCode, resolveOrderStt } from "@/lib/order-invoice-code";`
- `import { format } from "date-fns";`
- `import { vi } from "date-fns/locale";`
- `import { DashboardChartTooltip, type DashboardChartDataPoint } from "@/components/DashboardChartTooltip";`
- … 10 import khác

## Module `@/lib/...` được import

- `@/lib/chain-access`
- `@/lib/order-invoice-code`
- `@/lib/sales-api`
- `@/lib/shop-display-order`
- `@/lib/use-session-user`
- `@/lib/utils`

## Chuỗi `/api/...` (page + component con, 36 mục)

- `/api/agent/assistant-access` → [`api-modules/agent.md`](../api-modules/agent.md)
- `/api/agent/assistant-access?organizationId=${org.id}` → [`api-modules/agent.md`](../api-modules/agent.md)
- `/api/dashboard/low-stock?shopId=${shopId}` → [`api-modules/dashboard.md`](../api-modules/dashboard.md)
- `/api/dashboard/orders-today?shopId=${shopId}` → [`api-modules/dashboard.md`](../api-modules/dashboard.md)
- `/api/dashboard/revenue-chart?${params.toString()}` → [`api-modules/dashboard.md`](../api-modules/dashboard.md)
- `/api/dashboard/top-products?shopId=${shopId}&limit=10` → [`api-modules/dashboard.md`](../api-modules/dashboard.md)
- `/api/dashboard?shopId=${shopId}`
- `/api/organizations`
- `/api/organizations/${editId}`
- `/api/organizations/${editId}/gdt/captcha`
- `/api/organizations/${editId}/gdt/test-connect`
- `/api/organizations/${id}`
- `/api/organizations/${org.id}/gdt/status`
- `/api/organizations/${sortOrgId}/shop-display-order`
- `/api/shops` → [`api-modules/shops.md`](../api-modules/shops.md)
- `/api/shops/${id}` → [`api-modules/shops.md`](../api-modules/shops.md)
- `/api/shops/${shopId}` → [`api-modules/shops.md`](../api-modules/shops.md)
- `/api/shops/${shopId}/admin-email` → [`api-modules/shops.md`](../api-modules/shops.md)
- `/api/shops/${shopId}/create-admin` → [`api-modules/shops.md`](../api-modules/shops.md)
- `/api/shops/${shopId}/devices` → [`api-modules/shops.md`](../api-modules/shops.md)
- `/api/shops/${shopId}/devices/${device!.id}/login-events?page=${page}&limit=${pageSize}` → [`api-modules/shops.md`](../api-modules/shops.md)
- `/api/shops/${shopId}/devices/${deviceRowId}` → [`api-modules/shops.md`](../api-modules/shops.md)
- `/api/shops/${shopId}/reset-password` → [`api-modules/shops.md`](../api-modules/shops.md)
- `/api/transfers`
- `/api/transfers/${expandedTransfer}/items`
- `/api/transfers/${id}`
- `/api/transfers/${id}/approve`
- `/api/transfers/${id}/receive`
- `/api/transfers/${id}/ship`
- `/api/warehouses`
- `/api/warehouses/${fromWh}/inventory`
- `/api/warehouses/${id}`
- `/api/warehouses/${warehouse.id}/adjust-stock`
- `/api/warehouses/${warehouse.id}/inventory`
- `/api/warehouses/${warehouse.id}/movements`
- `/api/warehouses/${warehouse.id}/products`

## File liên quan

- Route khai báo: `artifacts/pos-app/src/App.tsx`
- Layout/menu: `components/layout/app-layout.tsx`
- Session: `lib/session-cache.ts`, `lib/use-session-user.ts`
