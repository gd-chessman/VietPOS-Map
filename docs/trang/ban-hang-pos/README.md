# Trang giao diện: `pos.tsx`

**Mô tả:** Màn bán hàng: giỏ, thanh toán, in bill, checkout offline. (URL /pos, POS, ~1988 dòng).

**Mã nguồn Shop:** `artifacts/pos-app/src/pages/pos.tsx`

**Đường dẫn URL:** `/pos`
**Tên component React:** `POS`
**Quy mô:** ~1988 dòng.

## Thông tin hiển thị

Nội dung người dùng **nhìn thấy** trên màn hình (trích nhãn từ TSX; số liệu động từ API).

### `pos.tsx`

**Nhãn lọc / preset / placeholder:**
- Ô nhập: VD: bớt giá, tặng kèm...
**Tooltip / mô tả ngắn (title=):**
- Ghi chú / giảm giá
- Quét QR bằng camera
- Duyệt sản phẩm dạng lưới
- Tra cứu và thao tác đơn hàng

### `@/components/VatInvoiceCheckoutSection`

**Nhãn lọc / preset / placeholder:**
- Tên công ty *
- Mã số thuế (tuỳ chọn)
- SĐT (tuỳ chọn)
- Email nhận hóa đơn (tuỳ chọn)
- Địa chỉ công ty (tuỳ chọn)
- Ô nhập: Công ty TNHH ...
- Ô nhập: ketoan@congty.vn
- Ô nhập: Số nhà, phường, quận, tỉnh...

### `@/components/OrdersPanel`

**Tiêu đề trang:** “Đơn hàng”
**Cột bảng:**
- STT
- Số HĐ
- Chi nhánh
- Ngày giờ
- Thu ngân
- NV ca
- Thanh toán
- CT thanh toán
- CT sản phẩm
- Số món
- Ghi chú
- Tổng tiền
- Trạng thái
- Lý do
**Nhãn lọc / preset / placeholder:**
- Ô nhập: Thêm ghi chú nếu cần...
- Hoàn thành
- Đề nghị huỷ
- Đơn huỷ
- Đơn ghi chú
- Chờ xuất VAT
- Đã xuất VAT
- CT thanh toán
- CT sản phẩm
**Tooltip / mô tả ngắn (title=):**
- Chứng từ thanh toán
- Chứng từ sản phẩm
- Xem chi tiết
- Đổi thanh toán
- Sửa hoá đơn VAT
- In lại
- Duyệt huỷ
- Từ chối
- Khôi phục
- Chụp ảnh chứng từ sản phẩm
- In lại hoá đơn

## Thao tác người dùng

Hành động chính (nút, menu, mục dialog) — không liệt kê mọi nút icon-only.

### `pos.tsx`

**Thao tác:**
- setEditOpen(!editOpen)} title="Ghi chú / giảm giá">
- onRemove(sellKey)}>
- onUpdate(sellKey, -1)}>
- onUpdate(sellKey, 1)} disabled= >
- setEditOpen(false)}>Huỷ
- Lưu
- Total / Tổng tiền )}
- setLocation("/media?type=payment_proof")} > CT TT
- setLocation("/media?type=product_proof")} > CT SP
- setOrderHistoryOpen(true)} title="Tra cứu và thao tác đơn hàng" > Lịch sử )}
- Xoá tất cả
- Xóa
- Huỷ
- Số lượng

### `@/components/OrdersPanel`

**Thao tác:**
- onRequestModerate("approve-cancel")} >
- onRequestModerate("reject-cancel")} >
- onRequestModerate("uncancel")} >
- Huỷ bỏ
- Không, huỷ bỏ
- } className="bg-amber-500 hover:bg-amber-600"> Có, in lại
- } > Chụp ảnh
- openModerateConfirm("approve-cancel")} disabled= > Duyệt huỷ đơn
- openModerateConfirm("reject-cancel")} disabled= > Từ chối
- openModerateConfirm("uncancel")} disabled= > Khôi phục đơn hàng
- setChangePaymentOpen(true)}> Đổi phương thức thanh toán
- setProductCameraOpen(true)} > Thêm chứng từ sản phẩm
- onReprint(displayOrder)}> In lại hoá đơn
- setEditInvoiceOpen(true)}>
- void handleExportExcel()} >
- void handleExportPdf()} >
- setSelectedOrder(order)} >
- setEditInvoiceOrder(order)} >
- setReprintWarningOrder(order)} >
- setCancelOrder(order)} >
- openModerateConfirm(order, "approve-cancel")}>
- openModerateConfirm(order, "reject-cancel")}>
- openModerateConfirm(order, "uncancel")}>

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
