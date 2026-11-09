# Trang giao diện: `orders.tsx`

**Mô tả:** Danh sách đơn, hủy/duyệt hủy, in lại.

**Mã nguồn Shop:** `artifacts/pos-app/src/pages/orders.tsx`

**Đường dẫn URL:** `/orders`
**Tên component React:** `Orders`
**Quy mô:** ~22 dòng.

## Thông tin hiển thị

Nội dung người dùng **nhìn thấy** trên màn hình (trích nhãn từ TSX; số liệu động từ API).

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
