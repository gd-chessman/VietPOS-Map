# Trang giao diện: `login.tsx`

**Mô tả:** Đăng nhập email/PIN, lưu phiên thiết bị. (URL /login, Login, ~1080 dòng).

**Mã nguồn Shop:** `artifacts/pos-app/src/pages/login.tsx`

**Đường dẫn URL:** `/login`
**Tên component React:** `Login`
**Quy mô:** ~1080 dòng.

**Đường dẫn:** `/login`

Email/password, PIN máy, tài khoản đã lưu trên thiết bị. JWT → `pos_token`.

**Đọc tiếp:** [Hướng dẫn đọc Map](../../huong-dan-doc/)

## Quyền (phát hiện trong source)

- Có kiểm tra role **`super_admin`** (hoặc redirect dashboard).

## JSX component dùng trong file (PascalCase)

- `<Button />`
- `<Card />`
- `<CardContent />`
- `<CardDescription />`
- `<CardFooter />`
- `<CardHeader />`
- `<CardTitle />`
- `<DeviceBlockedScreen />`
- `<ForgotPinPasswordDialog />`
- `<Form />`
- `<FormControl />`
- `<FormField />`
- `<FormItem />`
- `<FormLabel />`
- `<FormMessage />`
- `<Input />`
- `<LoginFormValues />`
- `<PinCodeDialog />`
- `<SavedAccount />`
- `<SetPinWithPasswordDialog />`
- `<User />`
- `<UserCircle />`
- `<WifiOff />`

## Biểu thức quyền / guard trong file

- `requirePassword`
- `required`

## Import chính (đầu file)

- `import { useEffect, useRef, useState } from "react";`
- `import { useLocation } from "wouter";`
- `import { useForm } from "react-hook-form";`
- `import { zodResolver } from "@hookform/resolvers/zod";`
- `import * as z from "zod";`
- `import {`
- `import { useQueryClient } from "@tanstack/react-query";`
- `import { Button } from "@/components/ui/button";`
- `import { Input } from "@/components/ui/input";`
- `import { Card, CardContent, CardDescription, CardHeader, CardTitle, CardFooter } from "@/components/ui/card";`
- `import { Form, FormControl, FormField, FormItem, FormLabel, FormMessage } from "@/components/ui/form";`
- `import { useToast } from "@/hooks/use-toast";`
- `import { UserCircle, WifiOff } from "lucide-react";`
- `import {`
- `import { syncAuthTokenGetter, clearAuthTokenGetter } from "@/lib/auth-session";`
- `import { isTauriRuntime } from "@/lib/tauri-runtime";`
- `import { roleRequiresPin, staffUsesDevicePin } from "@/lib/user-pin";`
- `import { hashDevicePin, verifyDevicePin } from "@/lib/staff-device-pin";`
- … 1 import khác

## Module `@/lib/...` được import

- `@/lib/auth-session`
- `@/lib/device/use-device-gate`
- `@/lib/home-path`
- `@/lib/offline`
- `@/lib/pin-lock`
- `@/lib/pin-reset-api`
- `@/lib/sales-api`
- `@/lib/session-cache`
- `@/lib/staff-device-pin`
- `@/lib/tauri-runtime`
- `@/lib/user-pin`

## Chuỗi `/api/...` (page + component con, 2 mục)

- `/api/auth/me` → [`auth`](../../module-api/xac-thuc/)
- `/api/auth/pin/set` → [`auth`](../../module-api/xac-thuc/)

## Luồng nghiệp vụ (doc)

- [01-dang-nhap-va-shop-context](../../nghiep-vu/01-dang-nhap-va-shop-context/)

## Liên kết mã

- Khai báo URL: `artifacts/pos-app/src/App.tsx`
- Menu/layout: `components/layout/app-layout.tsx`
- Phiên đăng nhập: `lib/session-cache.ts`, `lib/use-session-user.ts`
