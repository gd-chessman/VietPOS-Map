# Trang giao diện: `chain.tsx`

**Mô tả:** Sửa tổ chức: shop, Viettel, CQT, Trợ lý AI, URL feedback.

**Mã nguồn Shop:** `artifacts/pos-app/src/pages/chain.tsx`

**Đường dẫn URL:** `/chain`
**Tên component React:** `Chain`
**Quy mô:** ~4155 dòng.

## Thông tin hiển thị

Nội dung người dùng **nhìn thấy** trên màn hình (trích nhãn từ TSX; số liệu động từ API).

### `chain.tsx`

**Tiêu đề trang:** “Không có quyền truy cập”, “Quản lý chuỗi cửa hàng”
**Cột bảng:**
- ID
- Mã
- Tên tổ chức
- MST
- Ngân hàng
- Điện thoại
- Email
- Trạng thái
- Ngày tạo
- Thao tác
- STT
- Số HĐ
- Giờ
- Thu ngân
- Tổng tiền
- Sản phẩm
- Tồn kho
- Giá bán
- Thời gian
- Tài khoản
- IP
- Tên thiết bị
- Tên định danh
- Mã thiết bị
- Đăng ký lúc
- Đăng nhập
- Tên sản phẩm
- Loại
- Thay đổi
- Ghi chú
- Tên kho
- Cửa hàng
- Số lượng
- Tồn kho nguồn
- Từ kho
- Đến kho
**Tab / khu vực:**
- Thông tin
- Ngân hàng
- HĐ đầu vào
- Email SMTP
- Trợ lý AI
- Cấu hình
- Viettel
- Cơ quan thuế
**Nhãn lọc / preset / placeholder:**
- Ô nhập: VD: VPOS01
- Ô nhập: VD: Chuỗi VietPOS
- Ô nhập: VD: 0123456789
- Ô nhập: VD: 0901234567
- Ô nhập: VD: contact@company.vn
- Ô nhập: VD: 123 Nguyễn Huệ, Q.1, TP.HCM
- Ô nhập: VD: Vietcombank
- Ô nhập: Để trống thì dùng tên tổ chức
- Ô nhập: VD: 0100109106-507
- Ô nhập: Để trống nếu không đổi
- Ô nhập: VD: 1/001
- Ô nhập: VD: C26TYY
- Ô nhập: Để trống → dùng MST tổ chức
- Ô nhập: smtp.gmail.com
- Ô nhập: mail@company.vn
- Ô nhập: https://api.openai.com/v1
- Ô nhập: gpt-4o-mini
- Ô nhập: Tìm tên, email, chi nhánh, vai trò…
- Ô nhập: https://pos.cuahang.vn
- Ô nhập: VD: Chi nhánh Hà Nội
- Ô nhập: VD: HN01, 04TP
- Ô nhập: VD: 12 Nguyễn Huệ, Quận 1, TP.HCM
- Ô nhập: Nguyễn Văn A
- Ô nhập: admin.hanoi@shop.com
- Ô nhập: VD: HN01
**Tooltip / mô tả ngắn (title=):**
- Chỉnh sửa
- Sao chép mã thiết bị
- Xem lịch sử đăng nhập trên thiết bị này
- Chỉnh sửa kho
- Huỷ phiếu

### `@/pages/chain-api-keys`

**Cột bảng:**
- Tên
- Cách cộng
- API key
- Bật
- Xóa
**Nhãn lọc / preset / placeholder:**
- Ô nhập: VD: Cửa trước
- 2 tia · 1 người
- 1 tia · 1 người

## Thao tác người dùng

Hành động chính (nút, menu, mục dialog) — không liệt kê mọi nút icon-only.

### `chain.tsx`

**Thao tác:**
- Thêm tổ chức
- openEdit(org)} >
- requestDeactivateOrg(org)} disabled= >
- selectInboundProviderViettel()} >
- setFormGdtPasswordVisible(v => !v)} >
- void loadGdtCaptcha()} > Tải captcha
- void testGdtConnect()} >
- selectInboundProviderGdt()} >
- Huỷ
- setSortDialogOpen(true)}> Sắp xếp
- setShowForm(v => !v)}> Thêm cửa hàng
- moveSortShop(id, -1)} aria-label="Lên" >
- moveSortShop(id, 1)} aria-label="Xuống" >
- setSortDialogOpen(false)}>Huỷ
- saveShopOrder.mutate()} disabled= >
- setShowForm(false)}>Huỷ
- create.mutate()} disabled= >
- setDashboardShopId(shop.id)} > Tổng quan
- setDevicesShopId(shop.id)} > Thiết bị
- setEditId(shop.id)} > Sửa
- requestDeactivateShop(shop)} disabled= >
- Đóng
- update.mutate( )} disabled= > Lưu thông tin
- updateEmail.mutate(editEmail)} disabled= > Cập nhật email
- resetPwd.mutate(newPassword)} disabled={newPassword.length Đặt lại mật khẩu
- createAdmin.mutate( )} disabled=
- onSave(value.trim())} > Lưu
- Lịch sử
- updateDevice.mutate( )} > Duyệt
- updateDevice.mutate( )} > Thu hồi
- }> Lịch sử
- }> Nhập / điều chỉnh kho
- setShowAdjust(false)}>Huỷ
- adjust.mutate()} disabled= >
- setShowForm(v => !v)}> Thêm kho
- createWh.mutate()} disabled= >
- setExpanded(expanded === wh.id ? null : wh.id)} >
- setEditWhId(null)}>Huỷ
- updateWh.mutate( , })} disabled= >
- setShowForm(v => !v)} disabled={warehouses.length Tạo phiếu chuyển kho

**Hộp thoại (tiêu đề):**
- Sắp xếp chi nhánh
- Chi tiết đơn {resolveOrderInvoiceCode(selectedOrder)}

### `@/pages/chain-api-keys`

**Thao tác:**
- setDeleteTarget( )} >
- createKey.mutate( ) } > Tạo key
- setAddForShop(null)}> Huỷ
- } > Thêm cảm biến
- deleteTarget && deleteKey.mutate(deleteTarget.id)} > Xóa
- Huỷ

**Hộp thoại (tiêu đề):**
- Cảm biến — {created?.shopName}
- Xóa cảm biến?

**Đường dẫn:** `/chain`

Sửa tổ chức: thông tin, shop, Viettel inbound/outbound, CQT, Trợ lý AI, URL feedback công khai.

**Đọc tiếp:** [Hướng dẫn đọc Map](../../huong-dan-doc/)

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

- `/api/agent/assistant-access` → [`agent`](../../module-api/tro-ly-ai-api/)
- `/api/agent/assistant-access?organizationId=${org.id}` → [`agent`](../../module-api/tro-ly-ai-api/)
- `/api/dashboard/low-stock?shopId=${shopId}` → [`dashboard`](../../module-api/bang-dieu-khiem-api/)
- `/api/dashboard/orders-today?shopId=${shopId}` → [`dashboard`](../../module-api/bang-dieu-khiem-api/)
- `/api/dashboard/revenue-chart?${params.toString()}` → [`dashboard`](../../module-api/bang-dieu-khiem-api/)
- `/api/dashboard/top-products?shopId=${shopId}&limit=10` → [`dashboard`](../../module-api/bang-dieu-khiem-api/)
- `/api/dashboard?shopId=${shopId}`
- `/api/organizations`
- `/api/organizations/${editId}`
- `/api/organizations/${editId}/gdt/captcha`
- `/api/organizations/${editId}/gdt/test-connect`
- `/api/organizations/${id}`
- `/api/organizations/${org.id}/gdt/status`
- `/api/organizations/${sortOrgId}/shop-display-order`
- `/api/shops` → [`shops`](../../module-api/cua-hang/)
- `/api/shops/${id}` → [`shops`](../../module-api/cua-hang/)
- `/api/shops/${shopId}` → [`shops`](../../module-api/cua-hang/)
- `/api/shops/${shopId}/admin-email` → [`shops`](../../module-api/cua-hang/)
- `/api/shops/${shopId}/create-admin` → [`shops`](../../module-api/cua-hang/)
- `/api/shops/${shopId}/devices` → [`shops`](../../module-api/cua-hang/)
- `/api/shops/${shopId}/devices/${device!.id}/login-events?page=${page}&limit=${pageSize}` → [`shops`](../../module-api/cua-hang/)
- `/api/shops/${shopId}/devices/${deviceRowId}` → [`shops`](../../module-api/cua-hang/)
- `/api/shops/${shopId}/reset-password` → [`shops`](../../module-api/cua-hang/)
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

## Liên kết mã

- Khai báo URL: `artifacts/pos-app/src/App.tsx`
- Menu/layout: `components/layout/app-layout.tsx`
- Phiên đăng nhập: `lib/session-cache.ts`, `lib/use-session-user.ts`
