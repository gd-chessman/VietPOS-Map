# Frontend: `orders.tsx`

**Mô tả:** Danh sách đơn, hủy/duyệt hủy, in lại. (URL /orders, Orders, ~22 dòng).

**Source Shop:** `artifacts/pos-app/src/pages/orders.tsx`

**URL (wouter):** `/orders`
**Component:** `Orders`
**Độ lớn:** ~22 dòng.

**Route:** `/orders`

Trang **vỏ mỏng** (~20 dòng): toàn bộ UI/logic nằm trong **`OrdersPanel`** (`components/OrdersPanel.tsx`, prop `variant="page"`).

## Redirect query (useEffect)

| Query | Hành vi |
|-------|---------|
| `invoiceStatus` hoặc `vat=1` | Chuyển sang `/vat-invoices` (giữ `shopId` nếu có) |

Dùng cho link cũ / badge menu trỏ nhầm sang orders thay vì HĐ VAT.

## Nghiệp vụ (trong OrdersPanel)

- Danh sách đơn theo shop; lọc trạng thái, tìm kiếm.
- Hủy đơn / duyệt hủy (role admin); in lại bill → `reprint_logs`.
- API chủ yếu module **`orders`** — xem `api-modules/orders.md`.

**Mirror:** `nghiep-vu/02-pos-ban-hang.md`.

## Query string URL (đọc trong code)

- `invoiceStatus`
- `shopId`
- `vat`

## JSX component dùng trong file (PascalCase)

- `<OrdersPanel />`

## Import chính (đầu file)

- `import { useEffect } from "react";`
- `import { useLocation } from "wouter";`
- `import { OrdersPanel } from "@/components/OrdersPanel";`

## Chuỗi `/api/...` (page + component con, 7 mục)

- `/api/orders/${moderateConfirm.orderId}/${moderateConfirm.action}` → [`api-modules/orders.md`](../api-modules/orders.md)
- `/api/orders/${o.id}/notify-reprint` → [`api-modules/orders.md`](../api-modules/orders.md)
- `/api/orders/${order!.id}` → [`api-modules/orders.md`](../api-modules/orders.md)
- `/api/orders/${order.id}/${action}` → [`api-modules/orders.md`](../api-modules/orders.md)
- `/api/orders/period-summary?${params}` → [`api-modules/orders.md`](../api-modules/orders.md)
- `/api/orders?${params}`
- `/api/shops` → [`api-modules/shops.md`](../api-modules/shops.md)

## Luồng nghiệp vụ (doc)

- `nghiep-vu/02-pos-ban-hang.md`

## File liên quan

- Route khai báo: `artifacts/pos-app/src/App.tsx`
- Layout/menu: `components/layout/app-layout.tsx`
- Session: `lib/session-cache.ts`, `lib/use-session-user.ts`
