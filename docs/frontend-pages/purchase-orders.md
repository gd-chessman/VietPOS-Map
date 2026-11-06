# Frontend: `purchase-orders.tsx`

**Mô tả:** Phiếu đặt mua (PO) và trạng thái nhận hàng. (URL /purchase-orders, PurchaseOrdersPage, ~2359 dòng).

**Source Shop:** `artifacts/pos-app/src/pages/purchase-orders.tsx`

**URL (wouter):** `/purchase-orders`
**Component:** `PurchaseOrdersPage`
**Độ lớn:** ~2359 dòng.

**Route:** `/purchase-orders`

Phiếu đặt mua (PO) và trạng thái nhận hàng.

## Menu sidebar

- **Nhãn:** Đặt hàng
- **Điều kiện hiện menu (`show`):** `(isAdminOrManager || isWarehouseKeeper) && isHubShop`

## Nghiệp vụ (doc)

- `nghiep-vu/04-phieu-nhap-xuat-chuyen-kho.md`

## Component con (logic UI chính)

- `@/components/ui/button` → `artifacts/pos-app/src/components/ui/button.tsx`
- `@/components/ui/input` → `artifacts/pos-app/src/components/ui/input.tsx`
- `@/components/ui/badge` → `artifacts/pos-app/src/components/ui/badge.tsx`
- `@/components/ui/checkbox` → `artifacts/pos-app/src/components/ui/checkbox.tsx`
- `@/components/ui/select` → `artifacts/pos-app/src/components/ui/select.tsx`
- `@/components/ui/card` → `artifacts/pos-app/src/components/ui/card.tsx`
- `@/components/ui/table` → `artifacts/pos-app/src/components/ui/table.tsx`
- `@/components/ui/textarea` → `artifacts/pos-app/src/components/ui/textarea.tsx`
- `@/components/ui/dialog` → `artifacts/pos-app/src/components/ui/dialog.tsx`
- `@/components/ui/tabs` → `artifacts/pos-app/src/components/ui/tabs.tsx`
- `@/components/pagination-bar` → `artifacts/pos-app/src/components/pagination-bar.tsx`
- `@/components/ZoomableThumb` → `artifacts/pos-app/src/components/ZoomableThumb.tsx`
- `@/components/PdfPreview` → `artifacts/pos-app/src/components/PdfPreview.tsx`
- `@/components/PurchaseOrderPrint` → `artifacts/pos-app/src/components/PurchaseOrderPrint.tsx`

## Cách đọc code

- API: tìm `useQuery`, `useMutation`, `apiFetch`, hoặc mục **Chuỗi `/api/...`** bên dưới.
- Quyền: `lib/session-permissions.ts`, biểu thức trong `app-layout.tsx` và file page.
- Offline: các trang POS có thể gọi Dexie qua `@/lib/offline/...`.

## API modules (map sang docs)

- [`api-modules/organizations.md`](../api-modules/organizations.md) — prefix `/api/organizations`
- [`api-modules/purchase-orders.md`](../api-modules/purchase-orders.md) — prefix `/api/purchase-orders`
- [`api-modules/purchase-orders?status=${listStatus}.md`](../api-modules/purchase-orders?status=${listStatus}.md) — prefix `/api/purchase-orders?status=${listStatus}`
- [`api-modules/suppliers?active=true.md`](../api-modules/suppliers?active=true.md) — prefix `/api/suppliers?active=true`

## Quyền (phát hiện trong source)

- Có kiểm tra role **`super_admin`** (hoặc redirect dashboard).

## Tab UI (`TabsTrigger` value)

- `create`
- `list`

## JSX component dùng trong file (PascalCase)

- `<AlertTriangle />`
- `<Badge />`
- `<Button />`
- `<Card />`
- `<CardContent />`
- `<CardHeader />`
- `<CardTitle />`
- `<Checkbox />`
- `<ChevronDown />`
- `<ChevronRight />`
- `<ClipboardList />`
- `<CreatePayload />`
- `<Dialog />`
- `<DialogContent />`
- `<DialogDescription />`
- `<DialogFooter />`
- `<DialogHeader />`
- `<DialogTitle />`
- `<Eye />`
- `<FileDown />`
- `<History />`
- `<Input />`
- `<Layers />`
- `<POPrintData />`
- `<Package />`
- … 40 component khác

## Dialog / modal (tiêu đề)

- Chi tiết phiếu {detail?.code ?? ""}
- {editingOrder
                ? `Cập nhật phiếu ${editingOrder.code ?? `#${editingOrder.id}`}`
                : previewKind === "confirm"
                  ? `Xem phiếu nhập kho tổng${activePrintData?.code ? ` · ${activePrintData.code}` : ""}`
                  : `Xem phiếu đặt hàng (${previewFiles.length} nhà cung cấp)`}
- Huỷ phiếu đặt hàng?

## Import chính (đầu file)

- `import { Fragment, useEffect, useMemo, useRef, useState } from "react";`
- `import { useQuery, useQueryClient } from "@tanstack/react-query";`
- `import { format } from "date-fns";`
- `import { vi } from "date-fns/locale";`
- `import { Button } from "@/components/ui/button";`
- `import { Input } from "@/components/ui/input";`
- `import { Badge } from "@/components/ui/badge";`
- `import { Checkbox } from "@/components/ui/checkbox";`
- `import { Select, SelectContent, SelectItem, SelectTrigger, SelectValue } from "@/components/ui/select";`
- `import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";`
- `import { Table, TableBody, TableCell, TableHead, TableHeader, TableRow } from "@/components/ui/table";`
- `import { Textarea } from "@/components/ui/textarea";`
- `import { Dialog, DialogContent, DialogDescription, DialogFooter, DialogHeader, DialogTitle } from "@/components/ui/dialog";`
- `import { Tabs, TabsContent, TabsList, TabsTrigger } from "@/components/ui/tabs";`
- `import { PaginationBar, DEFAULT_PAGE_SIZE } from "@/components/pagination-bar";`
- `import { useToast } from "@/hooks/use-toast";`
- `import { formatVND, productImageUrl, cn } from "@/lib/utils";`
- `import { ZoomableThumb } from "@/components/ZoomableThumb";`
- … 10 import khác

## Module `@/lib/...` được import

- `@/lib/offline`
- `@/lib/print-pdf`
- `@/lib/purchase-order-audit`
- `@/lib/sales-api`
- `@/lib/session-cache`
- `@/lib/use-session-user`
- `@/lib/utils`

## Component `@/components/...` (đã quét API lớp 1)

- `ui/button` → `artifacts/pos-app/src/components/ui/button.tsx`
- `ui/input` → `artifacts/pos-app/src/components/ui/input.tsx`
- `ui/badge` → `artifacts/pos-app/src/components/ui/badge.tsx`
- `ui/checkbox` → `artifacts/pos-app/src/components/ui/checkbox.tsx`
- `ui/select` → `artifacts/pos-app/src/components/ui/select.tsx`
- `ui/card` → `artifacts/pos-app/src/components/ui/card.tsx`
- `ui/table` → `artifacts/pos-app/src/components/ui/table.tsx`
- `ui/textarea` → `artifacts/pos-app/src/components/ui/textarea.tsx`
- `ui/dialog` → `artifacts/pos-app/src/components/ui/dialog.tsx`
- `ui/tabs` → `artifacts/pos-app/src/components/ui/tabs.tsx`
- `pagination-bar` → `artifacts/pos-app/src/components/pagination-bar.tsx`
- `ZoomableThumb` → `artifacts/pos-app/src/components/ZoomableThumb.tsx`
- `PdfPreview` → `artifacts/pos-app/src/components/PdfPreview.tsx`
- `PurchaseOrderPrint` → `artifacts/pos-app/src/components/PurchaseOrderPrint.tsx`

## Chuỗi `/api/...` (page + component con, 8 mục)

- `/api/organizations/current`
- `/api/purchase-orders` → [`api-modules/purchase-orders.md`](../api-modules/purchase-orders.md)
- `/api/purchase-orders/${editingOrder.id}` → [`api-modules/purchase-orders.md`](../api-modules/purchase-orders.md)
- `/api/purchase-orders/${id}` → [`api-modules/purchase-orders.md`](../api-modules/purchase-orders.md)
- `/api/purchase-orders/${id}/${action}` → [`api-modules/purchase-orders.md`](../api-modules/purchase-orders.md)
- `/api/purchase-orders/sales-hints?days=30` → [`api-modules/purchase-orders.md`](../api-modules/purchase-orders.md)
- `/api/purchase-orders?status=${listStatus}`
- `/api/suppliers?active=true`

## Luồng nghiệp vụ (doc)

- `nghiep-vu/04-phieu-nhap-xuat-chuyen-kho.md`

## File liên quan

- Route khai báo: `artifacts/pos-app/src/App.tsx`
- Layout/menu: `components/layout/app-layout.tsx`
- Session: `lib/session-cache.ts`, `lib/use-session-user.ts`
