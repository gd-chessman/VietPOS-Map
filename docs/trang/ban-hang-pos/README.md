# Trang giao diện: `pos.tsx`

**Mô tả:** Màn bán hàng: giỏ, thanh toán, in bill, checkout offline. (URL /pos, POS, ~1988 dòng).

**Mã nguồn Shop:** `artifacts/pos-app/src/pages/pos.tsx`

**Đường dẫn URL:** `/pos`
**Tên component React:** `POS`
**Quy mô:** ~1988 dòng.

**Đường dẫn:** `/pos`

Màn hình bán hàng chính: tìm SP, giỏ hàng, thanh toán, yêu cầu HĐ VAT, mở/đóng ca.
Offline: ghi Dexie qua `checkoutOffline()`; sync sau khi có mạng.

**File lớn** — tìm theo: cart state, barcode, payment method, print bill, de nghị hủy đơn.
**Quyền:** `userCanUsePos`, NV bán hàng / thu ngân.

**Đọc tiếp:** [Hướng dẫn đọc Map](../../huong-dan-doc/)

## JSX component dùng trong file (PascalCase)

- `<AlertDialog />`
- `<AlertDialogAction />`
- `<AlertDialogCancel />`
- `<AlertDialogContent />`
- `<AlertDialogDescription />`
- `<AlertDialogFooter />`
- `<AlertDialogHeader />`
- `<AlertDialogTitle />`
- `<Badge />`
- `<Barcode />`
- `<Button />`
- `<Camera />`
- `<Card />`
- `<CardContent />`
- `<CartCheckoutFooter />`
- `<CartItem />`
- `<CartItemRow />`
- `<CreditCard />`
- `<CustomerNotice />`
- `<HTMLInputElement />`
- `<History />`
- `<Input />`
- `<Kbd />`
- `<LayoutGrid />`
- `<Minus />`
- … 21 component khác

## Dialog / modal (tiêu đề)

- {pendingConfirm?.kind === "closeTab" && `Xóa tab "${pendingConfirm.label}"?`}
              {pendingConfirm?.kind === "clearCart" && `Xóa tất cả sản phẩm trong "${pendingConfirm.label}"?`}
              {pendingConfirm?.kind === "removeItem" && `Xóa "${pendingConfirm.productName}"?`}

## Import chính (đầu file)

- `import { useState, useMemo, useRef, useEffect, useLayoutEffect, useCallback } from "react";`
- `import { getListOrdersQueryKey, getGetDashboardQueryKey, getGetTopProductsQueryKey, useGetTopProducts } from "@workspace/api-client-react";`
- `import { useSessionUser } from "@/lib/use-session-user";`
- `import { usePosProducts, checkoutOffline, type OfflineOrder } from "@/lib/offline";`
- `import { formatOrderInvoiceCode, resolveOrderInvoiceCode } from "@/lib/order-invoice-code";`
- `import { fetchOrderPreprintForPrint } from "@/lib/order-preprint";`
- `import { broadcastLanOfflineSale } from "@/lib/lan-offline-sale";`
- `import { getOrCreateDeviceId } from "@/lib/device/device-id";`
- `import { useShiftSessionContext } from "@/lib/offline/shift-session";`
- `import { useQuery, useQueryClient } from "@tanstack/react-query";`
- `import { apiGet } from "@/lib/sales-api";`
- `import { getBearerTokenForApi } from "@/lib/session-cache";`
- `import { cn, formatVND, productImageUrl } from "@/lib/utils";`
- `import { Button } from "@/components/ui/button";`
- `import { Kbd } from "@/components/ui/kbd";`
- `import { Input } from "@/components/ui/input";`
- `import { Card, CardContent } from "@/components/ui/card";`
- `import { Badge } from "@/components/ui/badge";`
- … 19 import khác

## Module `@/lib/...` được import

- `@/lib/device/device-id`
- `@/lib/lan-offline-sale`
- `@/lib/media-access`
- `@/lib/offline`
- `@/lib/offline/shift-session`
- `@/lib/order-invoice-code`
- `@/lib/order-preprint`
- `@/lib/pos-keyboard-shortcuts`
- `@/lib/pos-sellables`
- `@/lib/pos-tab-focus`
- `@/lib/pos-tabs`
- `@/lib/print-receipt`
- `@/lib/receipt-header-name`
- `@/lib/sales-api`
- `@/lib/session-cache`
- `@/lib/staff-cart-edit`
- `@/lib/use-session-user`
- `@/lib/utils`

## Chuỗi `/api/...` (page + component con, 8 mục)

- `/api/orders/${moderateConfirm.orderId}/${moderateConfirm.action}` → [`orders`](../../module-api/don-hang-api/)
- `/api/orders/${o.id}/notify-reprint` → [`orders`](../../module-api/don-hang-api/)
- `/api/orders/${order!.id}` → [`orders`](../../module-api/don-hang-api/)
- `/api/orders/${order.id}/${action}` → [`orders`](../../module-api/don-hang-api/)
- `/api/orders/period-summary?${params}` → [`orders`](../../module-api/don-hang-api/)
- `/api/orders?${params}`
- `/api/products/variant-sales` → [`products`](../../module-api/san-pham-api/)
- `/api/shops` → [`shops`](../../module-api/cua-hang/)

## Luồng nghiệp vụ (doc)

- [02-pos-ban-hang](../../nghiep-vu/02-pos-ban-hang/)

## Liên kết mã

- Khai báo URL: `artifacts/pos-app/src/App.tsx`
- Menu/layout: `components/layout/app-layout.tsx`
- Phiên đăng nhập: `lib/session-cache.ts`, `lib/use-session-user.ts`
