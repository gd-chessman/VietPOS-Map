# Trang giao diện: `feedback-form.tsx`

**Mô tả:** Form công khai /feedback cho khách gửi ý kiến. (URL /feedback, FeedbackFormPage, ~360 dòng).

**Mã nguồn Shop:** `artifacts/pos-app/src/pages/feedback-form.tsx`

**Đường dẫn URL:** `/feedback`
**Tên component React:** `FeedbackFormPage`
**Quy mô:** ~360 dòng.

## Thông tin hiển thị

Nội dung người dùng **nhìn thấy** trên màn hình (trích nhãn từ TSX; số liệu động từ API).

### `feedback-form.tsx`

**Tiêu đề trang:** “Thank you! / Cảm ơn bạn!”
**Thẻ / chỉ số (CardTitle):**
- Customer Feedback / Góp ý khách hàng
**Nhãn lọc / preset / placeholder:**
- Ô nhập: Your full name / Họ và tên của bạn
- Ô nhập: Optional / Không bắt buộc
- Ô nhập: Share your experience... / Chia sẻ trải nghiệm của bạn...

## Thao tác người dùng

Hành động chính (nút, menu, mục dialog) — không liệt kê mọi nút icon-only.

### `feedback-form.tsx`

**Thao tác:**
- fileRef.current?.click()} disabled=

**Đường dẫn:** `/feedback`

Form công khai `/feedback` cho khách gửi ý kiến.

## Component con (logic UI chính)

- `@/components/ui/button` → `artifacts/pos-app/src/components/ui/button.tsx`
- `@/components/ui/input` → `artifacts/pos-app/src/components/ui/input.tsx`
- `@/components/ui/textarea` → `artifacts/pos-app/src/components/ui/textarea.tsx`
- `@/components/ui/card` → `artifacts/pos-app/src/components/ui/card.tsx`
- `@/components/ui/form` → `artifacts/pos-app/src/components/ui/form.tsx`

## Cách đọc code

- API: tìm `useQuery`, `useMutation`, `apiFetch`, hoặc mục **Chuỗi `/api/...`** bên dưới.
- Quyền: `lib/session-permissions.ts`, biểu thức trong `app-layout.tsx` và file page.
- Offline: các trang POS có thể gọi Dexie qua `@/lib/offline/...`.

## Module API liên quan (trong Map)

- [`public`](../../module-api/public/) — nhóm `/api/public`

**Đọc tiếp:** [Hướng dẫn đọc Map](../../huong-dan-doc/)

## JSX component dùng trong file (PascalCase)

- `<Button />`
- `<Card />`
- `<CardContent />`
- `<CardDescription />`
- `<CardHeader />`
- `<CardTitle />`
- `<CheckCircle2 />`
- `<Form />`
- `<FormControl />`
- `<FormField />`
- `<FormItem />`
- `<FormLabel />`
- `<FormMessage />`
- `<FormValues />`
- `<HTMLInputElement />`
- `<ImageField />`
- `<ImagePlus />`
- `<Input />`
- `<MessageSquare />`
- `<Star />`
- `<StarRating />`
- `<Textarea />`

## Biểu thức quyền / guard trong file

- `required`

## Import chính (đầu file)

- `import { useRef, useState, useMemo } from "react";`
- `import { useMutation } from "@tanstack/react-query";`
- `import { useForm } from "react-hook-form";`
- `import { zodResolver } from "@hookform/resolvers/zod";`
- `import * as z from "zod";`
- `import { Button } from "@/components/ui/button";`
- `import { Input } from "@/components/ui/input";`
- `import { Textarea } from "@/components/ui/textarea";`
- `import { Card, CardContent, CardDescription, CardHeader, CardTitle } from "@/components/ui/card";`
- `import { Form, FormControl, FormField, FormItem, FormLabel, FormMessage } from "@/components/ui/form";`
- `import { MessageSquare, Star, CheckCircle2, ImagePlus, X } from "lucide-react";`
- `import { parseFeedbackShopFromSearch } from "@/lib/feedback-url";`

## Module `@/lib/...` được import

- `@/lib/feedback-url`

## Component `@/components/...` (đã quét API lớp 1)

- `ui/button` → `artifacts/pos-app/src/components/ui/button.tsx`
- `ui/input` → `artifacts/pos-app/src/components/ui/input.tsx`
- `ui/textarea` → `artifacts/pos-app/src/components/ui/textarea.tsx`
- `ui/card` → `artifacts/pos-app/src/components/ui/card.tsx`
- `ui/form` → `artifacts/pos-app/src/components/ui/form.tsx`

## Chuỗi `/api/...` (page + component con, 1 mục)

- `/api/public/feedback`

## Liên kết mã

- Khai báo URL: `artifacts/pos-app/src/App.tsx`
- Menu/layout: `components/layout/app-layout.tsx`
- Phiên đăng nhập: `lib/session-cache.ts`, `lib/use-session-user.ts`
