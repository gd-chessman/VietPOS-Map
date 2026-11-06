# Trang giao diện: `vat-invoice-public.tsx`

**Mô tả:** Form công khai tra cứu/xem HĐ VAT /vat-invoice. (URL /vat-invoice, VatInvoicePublicForm, ~689 dòng).

**Mã nguồn Shop:** `artifacts/pos-app/src/pages/vat-invoice-public.tsx`

**Đường dẫn URL:** `/vat-invoice`
**Tên component React:** `VatInvoicePublicForm`
**Quy mô:** ~689 dòng.

## Thông tin hiển thị

Nội dung người dùng **nhìn thấy** trên màn hình (trích nhãn từ TSX; số liệu động từ API).

### `vat-invoice-public.tsx`

**Thẻ / chỉ số (CardTitle):**
- Không tìm thấy hóa đơn
- Thiếu mã truy cập
**Tooltip / mô tả ngắn (title=):**
- Vui lòng nhập tên công ty / Company name required
- MST: 10 số hoặc 10-3 / Tax code: 10 digits or 10-3
- Vui lòng nhập email hợp lệ / Valid email required
- Vui lòng nhập địa chỉ / Address required
- Số điện thoại không hợp lệ / Invalid phone

## Thao tác người dùng

Hành động chính (nút, menu, mục dialog) — không liệt kê mọi nút icon-only.

### `vat-invoice-public.tsx`

**Thao tác:**
- setReceiptOpen(true)} > Hóa đơn mua hàng
- Tải PDF HĐĐT
- Xem trước hóa đơn mua hàng

**Hộp thoại (tiêu đề):**
- Hóa đơn mua hàng

**Đường dẫn:** `/vat-invoice`

Form công khai tra cứu/xem HĐ VAT `/vat-invoice`.

## Component con (logic UI chính)

- `@/components/ui/button` → `artifacts/pos-app/src/components/ui/button.tsx`
- `@/components/ui/input` → `artifacts/pos-app/src/components/ui/input.tsx`
- `@/components/ui/label` → `artifacts/pos-app/src/components/ui/label.tsx`
- `@/components/ui/card` → `artifacts/pos-app/src/components/ui/card.tsx`
- `@/components/ui/badge` → `artifacts/pos-app/src/components/ui/badge.tsx`
- `@/components/ui/dialog` → `artifacts/pos-app/src/components/ui/dialog.tsx`
- `@/components/PdfPreview` → `artifacts/pos-app/src/components/PdfPreview.tsx`
- `@/components/ThermalReceiptPreview` → `artifacts/pos-app/src/components/ThermalReceiptPreview.tsx`
- `@/components/PaymentBreakdown` → `artifacts/pos-app/src/components/PaymentBreakdown.tsx`

## Cách đọc code

- API: tìm `useQuery`, `useMutation`, `apiFetch`, hoặc mục **Chuỗi `/api/...`** bên dưới.
- Quyền: `lib/session-permissions.ts`, biểu thức trong `app-layout.tsx` và file page.
- Offline: các trang POS có thể gọi Dexie qua `@/lib/offline/...`.

## Module API liên quan (trong Map)

- [`public`](../../module-api/public/) — nhóm `/api/public`

**Đọc tiếp:** [Hướng dẫn đọc Map](../../huong-dan-doc/)

## JSX component dùng trong file (PascalCase)

- `<ArrayBuffer />`
- `<Badge />`
- `<Button />`
- `<Card />`
- `<CardContent />`
- `<CardDescription />`
- `<CardHeader />`
- `<CardTitle />`
- `<CheckCircle2 />`
- `<DetailRow />`
- `<Dialog />`
- `<DialogContent />`
- `<DialogHeader />`
- `<DialogTitle />`
- `<Download />`
- `<Eye />`
- `<FileText />`
- `<FileX2 />`
- `<FormValues />`
- `<Input />`
- `<IssuedInvoiceDetails />`
- `<Label />`
- `<Loader2 />`
- `<Lock />`
- `<PdfPreview />`
- … 6 component khác

## Dialog / modal (tiêu đề)

- Hóa đơn mua hàng

## Biểu thức quyền / guard trong file

- `required`

## Import chính (đầu file)

- `import { useEffect, useMemo, useState, type ReactNode } from "react";`
- `import { useMutation, useQuery, useQueryClient } from "@tanstack/react-query";`
- `import { Button } from "@/components/ui/button";`
- `import { Input } from "@/components/ui/input";`
- `import { Label } from "@/components/ui/label";`
- `import { Card, CardContent, CardDescription, CardHeader, CardTitle } from "@/components/ui/card";`
- `import { Badge } from "@/components/ui/badge";`
- `import { CheckCircle2, Download, Eye, FileText, FileX2, Loader2, Lock } from "lucide-react";`
- `import { cn, formatVND } from "@/lib/utils";`
- `import {`
- `import { PdfPreview } from "@/components/PdfPreview";`
- `import { ThermalReceiptPreview } from "@/components/ThermalReceiptPreview";`
- `import { getOrderPaymentLabel } from "@/components/PaymentBreakdown";`
- `import type { ThermalReceipt } from "@/lib/thermal-usb";`

## Module `@/lib/...` được import

- `@/lib/thermal-usb`
- `@/lib/utils`

## Component `@/components/...` (đã quét API lớp 1)

- `ui/button` → `artifacts/pos-app/src/components/ui/button.tsx`
- `ui/input` → `artifacts/pos-app/src/components/ui/input.tsx`
- `ui/label` → `artifacts/pos-app/src/components/ui/label.tsx`
- `ui/card` → `artifacts/pos-app/src/components/ui/card.tsx`
- `ui/badge` → `artifacts/pos-app/src/components/ui/badge.tsx`
- `ui/dialog` → `artifacts/pos-app/src/components/ui/dialog.tsx`
- `PdfPreview` → `artifacts/pos-app/src/components/PdfPreview.tsx`
- `ThermalReceiptPreview` → `artifacts/pos-app/src/components/ThermalReceiptPreview.tsx`
- `PaymentBreakdown` → `artifacts/pos-app/src/components/PaymentBreakdown.tsx`

## Chuỗi `/api/...` (page + component con, 2 mục)

- `/api/public/vat-invoice/pdf?token=${encodeURIComponent(token)}`
- `/api/public/vat-invoice?token=${encodeURIComponent(token)}`

## Liên kết mã

- Khai báo URL: `artifacts/pos-app/src/App.tsx`
- Menu/layout: `components/layout/app-layout.tsx`
- Phiên đăng nhập: `lib/session-cache.ts`, `lib/use-session-user.ts`
