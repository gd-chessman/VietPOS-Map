# Trang giao diện: `orders.tsx`

**Mô tả:** Danh sách đơn, hủy/duyệt hủy, in lại. (URL /orders, Orders, ~22 dòng).

**Mã nguồn Shop:** `artifacts/pos-app/src/pages/orders.tsx`

**Đường dẫn URL:** `/orders`
**Tên component React:** `Orders`
**Quy mô:** ~22 dòng.

**Đường dẫn:** `/orders`

Trang **vỏ mỏng** (~20 dòng): toàn bộ UI/logic nằm trong **`OrdersPanel`** (`components/OrdersPanel.tsx`, prop `variant="page"`).

## Redirect query (useEffect)

| Query | Hành vi |
|-------|---------|
| `invoiceStatus` hoặc `vat=1` | Chuyển sang `/vat-invoices` (giữ `shopId` nếu có) |

Dùng cho link cũ / badge menu trỏ nhầm sang orders thay vì HĐ VAT.

## Nghiệp vụ (trong OrdersPanel)

- Danh sách đơn theo shop; lọc trạng thái, tìm kiếm.
- Hủy đơn / duyệt hủy (role admin); in lại bill → `reprint_logs`.
- API chủ yếu module **`orders`** — xem `module-api/don-hang-api/README.md`.

**Mirror:** `nghiep-vu/02-pos-ban-hang/README.md`.

**Đọc tiếp:** [Hướng dẫn đọc Map](../../huong-dan-doc/)

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

- `/api/orders/${moderateConfirm.orderId}/${moderateConfirm.action}` → [`orders`](../../module-api/don-hang-api/)
- `/api/orders/${o.id}/notify-reprint` → [`orders`](../../module-api/don-hang-api/)
- `/api/orders/${order!.id}` → [`orders`](../../module-api/don-hang-api/)
- `/api/orders/${order.id}/${action}` → [`orders`](../../module-api/don-hang-api/)
- `/api/orders/period-summary?${params}` → [`orders`](../../module-api/don-hang-api/)
- `/api/orders?${params}`
- `/api/shops` → [`shops`](../../module-api/cua-hang/)

## Luồng nghiệp vụ (doc)

- [02-pos-ban-hang](../../nghiep-vu/02-pos-ban-hang/)

## Liên kết mã

- Khai báo URL: `artifacts/pos-app/src/App.tsx`
- Menu/layout: `components/layout/app-layout.tsx`
- Phiên đăng nhập: `lib/session-cache.ts`, `lib/use-session-user.ts`
